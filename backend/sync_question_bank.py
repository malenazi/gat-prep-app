import argparse
import json
from collections import defaultdict
from typing import Any

from sqlalchemy.orm import Session

from database import Base, SessionLocal, engine
from models import Question
from question_content import (
    clean_optional_text,
    deserialize_comparison_columns,
    ensure_question_content_columns,
    serialize_comparison_columns,
    validate_content_format,
)
from questions import load_all_questions
from question_visuals import serialize_table_payload


SYNCED_CONTENT_FIELDS = (
    "batch_id",
    "generation_prompt_version",
    "authoring_source",
    "variant_group",
    "skill_id",
    "question_type",
    "text_ar",
    "passage_ar",
    "content_format",
    "figure_svg",
    "figure_alt",
    "table_ar",
    "table_caption",
    "comparison_columns",
    "option_a",
    "option_b",
    "option_c",
    "option_d",
    "correct_option",
    "explanation_ar",
    "solution_steps_ar",
    "tags",
    "paper_only",
    "stage",
)


def _normalized_steps(raw_value: Any) -> str | None:
    if raw_value is None:
        return None
    if isinstance(raw_value, list):
        return json.dumps(raw_value, ensure_ascii=False)
    if isinstance(raw_value, str):
        trimmed = raw_value.strip()
        if not trimmed:
            return None
        try:
            parsed = json.loads(trimmed)
        except json.JSONDecodeError:
            return trimmed
        return json.dumps(parsed, ensure_ascii=False)
    return None


def _normalized_comparison(raw_value: Any) -> str | None:
    if raw_value is None:
        return None
    if isinstance(raw_value, str):
        trimmed = raw_value.strip()
        if not trimmed:
            return None
        try:
            parsed = deserialize_comparison_columns(trimmed)
        except ValueError:
            return trimmed
        return serialize_comparison_columns(parsed)
    return serialize_comparison_columns(raw_value)


def _normalized_table(raw_value: Any) -> str | None:
    if raw_value is None:
        return None
    if isinstance(raw_value, str):
        trimmed = raw_value.strip()
        return trimmed or None
    return serialize_table_payload(raw_value)


def question_signature(question: Any) -> tuple[Any, ...]:
    return (
        question.skill_id,
        question.question_type,
        clean_optional_text(getattr(question, "text_ar", None)),
        clean_optional_text(getattr(question, "passage_ar", None)),
        validate_content_format(getattr(question, "content_format", None)),
        clean_optional_text(getattr(question, "figure_svg", None)),
        clean_optional_text(getattr(question, "figure_alt", None)),
        _normalized_table(getattr(question, "table_ar", None)),
        clean_optional_text(getattr(question, "table_caption", None)),
        _normalized_comparison(getattr(question, "comparison_columns", None)),
        clean_optional_text(getattr(question, "option_a", None)),
        clean_optional_text(getattr(question, "option_b", None)),
        clean_optional_text(getattr(question, "option_c", None)),
        clean_optional_text(getattr(question, "option_d", None)),
        clean_optional_text(getattr(question, "correct_option", None)),
        clean_optional_text(getattr(question, "explanation_ar", None)),
        _normalized_steps(getattr(question, "solution_steps_ar", None)),
        clean_optional_text(getattr(question, "tags", None)),
        bool(getattr(question, "paper_only", False)),
        clean_optional_text(getattr(question, "stage", None)) or "general",
    )


def build_source_question_payload(source_question: Any) -> dict[str, Any]:
    return {
        "source_key": clean_optional_text(getattr(source_question, "source_key", None)),
        "batch_id": clean_optional_text(getattr(source_question, "batch_id", None)),
        "generation_prompt_version": clean_optional_text(
            getattr(source_question, "generation_prompt_version", None)
        ),
        "authoring_source": clean_optional_text(getattr(source_question, "authoring_source", None))
        or "human",
        "variant_group": clean_optional_text(getattr(source_question, "variant_group", None)),
        "skill_id": source_question.skill_id,
        "question_type": source_question.question_type,
        "difficulty": float(getattr(source_question, "difficulty", 0.5) or 0.5),
        "text_ar": source_question.text_ar,
        "passage_ar": getattr(source_question, "passage_ar", None),
        "content_format": validate_content_format(getattr(source_question, "content_format", None)),
        "figure_svg": getattr(source_question, "figure_svg", None),
        "figure_alt": clean_optional_text(getattr(source_question, "figure_alt", None)),
        "table_ar": _normalized_table(getattr(source_question, "table_ar", None)),
        "table_caption": clean_optional_text(getattr(source_question, "table_caption", None)),
        "comparison_columns": _normalized_comparison(getattr(source_question, "comparison_columns", None)),
        "option_a": source_question.option_a,
        "option_b": source_question.option_b,
        "option_c": source_question.option_c,
        "option_d": source_question.option_d,
        "correct_option": source_question.correct_option,
        "explanation_ar": getattr(source_question, "explanation_ar", None),
        "solution_steps_ar": _normalized_steps(getattr(source_question, "solution_steps_ar", None)),
        "tags": clean_optional_text(getattr(source_question, "tags", None)),
        "paper_only": bool(getattr(source_question, "paper_only", False)),
        "stage": clean_optional_text(getattr(source_question, "stage", None)) or "general",
        "status": clean_optional_text(getattr(source_question, "status", None)) or "active",
    }


def generate_admin_source_key(question_id: int | None = None) -> str:
    if question_id is not None:
        return f"admin:legacy-{question_id}"
    return "admin:pending"


def _apply_source_payload(existing: Question, payload: dict[str, Any]) -> bool:
    changed = False
    for field in SYNCED_CONTENT_FIELDS:
        next_value = payload[field]
        if getattr(existing, field) != next_value:
            setattr(existing, field, next_value)
            changed = True

    if existing.source_key != payload["source_key"]:
        existing.source_key = payload["source_key"]
        changed = True

    if existing.original_difficulty is None:
        existing.original_difficulty = payload["difficulty"]
        changed = True

    if existing.times_answered or existing.last_calibrated_at:
        pass
    else:
        if existing.difficulty != payload["difficulty"]:
            existing.difficulty = payload["difficulty"]
            changed = True

    source_status = payload["status"]
    if source_status == "review" and existing.status != "review":
        existing.status = "review"
        changed = True
    elif existing.status not in {"review", "disabled"} and existing.status != source_status:
        existing.status = source_status
        changed = True

    return changed


def sync_question_bank(db: Session, *, dry_run: bool = False) -> dict[str, Any]:
    source_questions = load_all_questions()
    source_payloads = [build_source_question_payload(question) for question in source_questions]
    existing_questions = db.query(Question).order_by(Question.id.asc()).all()
    legacy_unkeyed_questions = [
        question for question in existing_questions if not clean_optional_text(question.source_key)
    ]
    legacy_seed_candidates = legacy_unkeyed_questions[: len(source_payloads)]

    existing_by_source_key = {
        question.source_key: question
        for question in existing_questions
        if clean_optional_text(question.source_key)
    }
    signature_buckets: dict[tuple[Any, ...], list[Question]] = defaultdict(list)
    for question in existing_questions:
        signature_buckets[question_signature(question)].append(question)

    matched_ids: set[int] = set()
    stats = {
        "source_total": len(source_payloads),
        "existing_total": len(existing_questions),
        "matched_by_source_key": 0,
        "matched_by_signature": 0,
        "matched_by_legacy_order": 0,
        "updated": 0,
        "created": 0,
        "legacy_admin_source_keys_assigned": 0,
    }
    legacy_cursor = 0

    for index, payload in enumerate(source_payloads):
        source_key = payload["source_key"]
        existing = existing_by_source_key.get(source_key)
        if existing is not None:
            matched_ids.add(existing.id)
            stats["matched_by_source_key"] += 1
        else:
            candidates = signature_buckets.get(question_signature(type("SignatureRow", (), payload)()))
            existing = next((candidate for candidate in candidates or [] if candidate.id not in matched_ids), None)
            if existing is not None:
                matched_ids.add(existing.id)
                stats["matched_by_signature"] += 1
            else:
                while (
                    legacy_cursor < len(legacy_seed_candidates)
                    and legacy_seed_candidates[legacy_cursor].id in matched_ids
                ):
                    legacy_cursor += 1
                fallback = (
                    legacy_seed_candidates[legacy_cursor]
                    if legacy_cursor < len(legacy_seed_candidates)
                    else None
                )
                if fallback is not None:
                    existing = fallback
                    matched_ids.add(existing.id)
                    stats["matched_by_legacy_order"] += 1
                    legacy_cursor += 1

        if existing is None:
            stats["created"] += 1
            if not dry_run:
                new_question = Question(**payload)
                new_question.original_difficulty = payload["difficulty"]
                db.add(new_question)
            continue

        if _apply_source_payload(existing, payload):
            stats["updated"] += 1

    for question in existing_questions:
        if question.id in matched_ids:
            continue
        if clean_optional_text(question.source_key):
            continue
        stats["legacy_admin_source_keys_assigned"] += 1
        if not dry_run:
            question.source_key = generate_admin_source_key(question.id)

    if not dry_run:
        db.commit()

    stats["unmatched_existing"] = len(existing_questions) - len(matched_ids)
    return stats


def main() -> None:
    parser = argparse.ArgumentParser(description="Sync the repo question bank into the database by source_key.")
    parser.add_argument("--dry-run", action="store_true", help="Report changes without writing them.")
    parser.add_argument("--json", action="store_true", help="Print the sync report as JSON.")
    args = parser.parse_args()

    Base.metadata.create_all(bind=engine)
    ensure_question_content_columns(engine)
    db = SessionLocal()
    try:
        report = sync_question_bank(db, dry_run=args.dry_run)
    finally:
        db.close()

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return

    print("Question bank sync")
    for key, value in report.items():
        print(f"  - {key}: {value}")


if __name__ == "__main__":
    main()
