import json
import math
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from difflib import SequenceMatcher
from types import SimpleNamespace
from typing import Any, Iterable

from pydantic import BaseModel, Field, field_validator

from generated_question_bank import AUTHORING_SOURCE_AI, build_manifest
from question_content import (
    CONTENT_FORMAT_MARKDOWN_MATH,
    CONTENT_FORMAT_PLAIN,
    VALID_CONTENT_FORMATS,
    apply_content_refresh,
    clean_optional_text,
    collect_question_content_issues,
    collect_question_quality_metadata,
)
from questions import load_all_questions


PROMPT_VERSION_V1 = "ai-question-wave1-v1"

WAVE_BATCH_SPECS = {
    "wave1": {
        "quant_arithmetic": 180,
        "quant_algebra": 180,
        "quant_statistics": 180,
        "verbal_reading": 60,
    }
}

DIFFICULTY_DISTRIBUTION = {
    "foundation": 0.25,
    "target_core": 0.40,
    "challenging": 0.25,
    "stretch": 0.10,
}

STAGE_DISTRIBUTION = {
    "diagnostic": 0.10,
    "foundation": 0.25,
    "building": 0.45,
    "peak": 0.15,
    "mock": 0.05,
}

STEM_DUPLICATE_THRESHOLD = 0.985
STEM_NEAR_DUPLICATE_THRESHOLD = 0.93

SKILL_BLUEPRINTS = {
    "quant_arithmetic": [
        "percent-change",
        "ratio-proportion",
        "fraction-equivalence",
        "unit-rate",
        "work-rate",
        "average-and-mean",
        "mixed-operations",
        "number-properties",
        "decimals-and-place-value",
        "profit-loss-discount",
        "simple-interest",
        "time-speed-distance",
    ],
    "quant_algebra": [
        "linear-equations",
        "two-step-equations",
        "systems-of-equations",
        "inequalities",
        "exponents-and-powers",
        "polynomials",
        "factoring",
        "quadratic-patterns",
        "function-tables",
        "sequence-rules",
        "algebraic-word-problems",
        "substitution-and-simplification",
    ],
    "quant_statistics": [
        "mean-median-mode",
        "range-and-spread",
        "probability-basics",
        "compound-events",
        "data-interpretation",
        "tables-and-graphs",
        "sample-space",
        "weighted-average",
        "percent-of-data",
        "boxplot-reading",
        "frequency-distribution",
        "expected-value-basics",
    ],
    "verbal_reading": [
        "main-idea",
        "supporting-detail",
        "inference",
        "tone-and-attitude",
        "vocabulary-in-context",
        "structure-and-purpose",
    ],
}

SKILL_QUESTION_TYPES = {
    "quant_arithmetic": "arithmetic",
    "quant_algebra": "algebra",
    "quant_statistics": "statistics",
    "verbal_reading": "reading",
}

SKILL_TEMPLATE_NOTES = {
    "quant_arithmetic": (
        "Generate short, clear quantitative items using textbook-quality notation. "
        "Prefer everyday contexts, percentages, rates, fractions, and arithmetic reasoning."
    ),
    "quant_algebra": (
        "Generate algebra items with clean symbolic setup, balanced distractors, and worked solution steps."
    ),
    "quant_statistics": (
        "Generate statistics and data-interpretation items with tables or short data descriptions when helpful."
    ),
    "verbal_reading": (
        "Generate concise reading-comprehension items with a short passage and four plausible options."
    ),
}


class GeneratedQuestionItem(BaseModel):
    source_key: str | None = None
    batch_id: str | None = None
    generation_prompt_version: str | None = None
    authoring_source: str = AUTHORING_SOURCE_AI
    blueprint_id: str = Field(min_length=1)
    variant_group: str = Field(min_length=1)
    skill_id: str
    question_type: str
    difficulty: float = Field(ge=0.0, le=1.0)
    text_ar: str = Field(min_length=1)
    passage_ar: str | None = None
    content_format: str = CONTENT_FORMAT_PLAIN
    figure_svg: str | None = None
    figure_alt: str | None = None
    table_ar: Any | None = None
    table_caption: str | None = None
    comparison_columns: dict[str, str] | None = None
    option_a: str = Field(min_length=1)
    option_b: str = Field(min_length=1)
    option_c: str = Field(min_length=1)
    option_d: str = Field(min_length=1)
    correct_option: str
    explanation_ar: str | None = None
    solution_steps_ar: list[str] | None = None
    tags: str | None = None
    paper_only: bool = False
    stage: str = "general"
    status: str = "active"

    @field_validator("content_format")
    @classmethod
    def _validate_content_format(cls, value: str) -> str:
        normalized = clean_optional_text(value) or CONTENT_FORMAT_PLAIN
        if normalized not in VALID_CONTENT_FORMATS:
            raise ValueError(f"content_format must be one of {sorted(VALID_CONTENT_FORMATS)}")
        return normalized

    @field_validator("correct_option")
    @classmethod
    def _validate_correct_option(cls, value: str) -> str:
        normalized = value.strip().lower()
        if normalized not in {"a", "b", "c", "d"}:
            raise ValueError("correct_option must be one of a/b/c/d")
        return normalized

    @field_validator("stage")
    @classmethod
    def _validate_stage(cls, value: str) -> str:
        normalized = clean_optional_text(value) or "general"
        if normalized not in {"diagnostic", "foundation", "building", "peak", "mock", "general"}:
            raise ValueError("stage must be one of diagnostic/foundation/building/peak/mock/general")
        return normalized

    @field_validator("authoring_source")
    @classmethod
    def _validate_authoring_source(cls, value: str) -> str:
        return clean_optional_text(value) or AUTHORING_SOURCE_AI


class GeneratedBatchManifest(BaseModel):
    batch_id: str = Field(min_length=1)
    generated_at: str | None = None
    generation_prompt_version: str = Field(min_length=1)
    authoring_source: str = AUTHORING_SOURCE_AI
    metadata: dict[str, Any] = Field(default_factory=dict)
    items: list[GeneratedQuestionItem]


@dataclass
class BatchIssue:
    severity: str
    code: str
    message: str


def _allocate_counts(total: int, distribution: dict[str, float]) -> dict[str, int]:
    raw_counts = {key: total * ratio for key, ratio in distribution.items()}
    counts = {key: int(math.floor(value)) for key, value in raw_counts.items()}
    assigned = sum(counts.values())
    remainder = total - assigned
    if remainder <= 0:
        return counts
    ranked = sorted(
        distribution.keys(),
        key=lambda key: raw_counts[key] - counts[key],
        reverse=True,
    )
    for key in ranked[:remainder]:
        counts[key] += 1
    return counts


def stage_targets(total: int) -> dict[str, int]:
    return _allocate_counts(total, STAGE_DISTRIBUTION)


def difficulty_targets(total: int) -> dict[str, int]:
    return _allocate_counts(total, DIFFICULTY_DISTRIBUTION)


def difficulty_bucket(value: float) -> str:
    if value <= 0.24:
        return "foundation"
    if value <= 0.59:
        return "target_core"
    if value <= 0.79:
        return "challenging"
    return "stretch"


def build_batch_id(skill_id: str, index: int) -> str:
    return f"{skill_id}-ai-batch-{index:03d}"


def canonical_source_key(skill_id: str, batch_id: str, index: int) -> str:
    return f"generated:{skill_id}:{batch_id}:{index:04d}"


def _slugify(value: str) -> str:
    normalized = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return normalized or "item"


def _normalize_compare_text(value: str | None) -> str:
    if not value:
        return ""
    normalized = value.lower()
    normalized = normalized.replace("$", " ")
    normalized = re.sub(r"\\[a-zA-Z]+", " ", normalized)
    normalized = re.sub(r"[^a-z0-9]+", " ", normalized)
    return re.sub(r"\s+", " ", normalized).strip()


def question_stem_signature(question: Any) -> str:
    return " | ".join(
        part
        for part in (
            _normalize_compare_text(getattr(question, "passage_ar", None)),
            _normalize_compare_text(getattr(question, "text_ar", None)),
        )
        if part
    )


def _issue_dict(issue: Any) -> dict[str, Any]:
    return {
        "severity": issue.severity,
        "code": issue.code,
        "field": issue.field,
        "message": issue.message,
    }


def _batch_issue_dict(issue: BatchIssue) -> dict[str, Any]:
    return {
        "severity": issue.severity,
        "code": issue.code,
        "message": issue.message,
    }


def build_generation_prompt(skill_id: str, count: int, *, batch_id: str, prompt_version: str) -> dict[str, str]:
    blueprints = SKILL_BLUEPRINTS[skill_id]
    blueprint_quota = max(1, math.ceil(count / max(1, len(blueprints))))
    stage_mix = stage_targets(count)
    difficulty_mix = difficulty_targets(count)
    question_type = SKILL_QUESTION_TYPES[skill_id]
    content_hint = (
        "Use markdown_math for quant items and plain for verbal reading unless math notation is required."
    )
    system = (
        "You are generating exam-quality multiple-choice questions for an adaptive e-learning platform. "
        "Return only valid JSON matching the provided schema. "
        "Every question must be learner-ready, solvable, internally consistent, and free of placeholders."
    )
    user = (
        f"Create {count} English questions for skill `{skill_id}` in batch `{batch_id}` using prompt version `{prompt_version}`.\n"
        f"Question type should be `{question_type}`.\n"
        f"{SKILL_TEMPLATE_NOTES[skill_id]}\n"
        f"Difficulty targets: {json.dumps(difficulty_mix, ensure_ascii=False)} using numeric difficulty 0.0-1.0.\n"
        f"Stage targets: {json.dumps(stage_mix, ensure_ascii=False)}.\n"
        f"Blueprint families: {', '.join(blueprints)}.\n"
        f"Do not exceed {blueprint_quota} questions per blueprint family, and give every question a non-empty `variant_group`.\n"
        f"Include explanation_ar for every question, and include at least 2 solution_steps_ar entries for quantitative questions.\n"
        f"{content_hint}\n"
        "Avoid geometry. Avoid duplicate or near-duplicate stems. Avoid placeholder distractors. "
        "Figures/tables are optional, but if you provide one, include figure_alt/table_caption metadata.\n"
        "Return one manifest with batch metadata and an `items` array."
    )
    return {"system": system, "user": user}


def load_existing_questions_for_validation(*, exclude_source_keys: Iterable[str] | None = None) -> list[Any]:
    excluded = set(exclude_source_keys or [])
    return [
        question
        for question in load_all_questions(apply_refresh=True)
        if getattr(question, "source_key", None) not in excluded
    ]


def validate_generated_manifest(
    manifest_data: dict[str, Any],
    *,
    existing_questions: list[Any] | None = None,
) -> dict[str, Any]:
    manifest = GeneratedBatchManifest.model_validate(manifest_data)
    existing_questions = existing_questions or load_existing_questions_for_validation(
        exclude_source_keys={
            item.source_key for item in manifest.items if item.source_key
        }
    )

    existing_stems: dict[str, list[Any]] = defaultdict(list)
    existing_variant_counts: Counter[str] = Counter()
    for question in existing_questions:
        stem = question_stem_signature(question)
        if stem:
            existing_stems[stem].append(question)
        if getattr(question, "status", "active") == "active" and getattr(question, "variant_group", None):
            existing_variant_counts[getattr(question, "variant_group")] += 1

    per_skill_items: dict[str, list[GeneratedQuestionItem]] = defaultdict(list)
    for item in manifest.items:
        per_skill_items[item.skill_id].append(item)

    quota_issues: list[BatchIssue] = []
    quota_summary: dict[str, Any] = {}
    for skill_id, items in per_skill_items.items():
        stage_counter = Counter(item.stage for item in items)
        difficulty_counter = Counter(difficulty_bucket(item.difficulty) for item in items)
        stage_target = stage_targets(len(items))
        difficulty_target = difficulty_targets(len(items))
        tolerance = max(1, math.ceil(len(items) * 0.05))
        skill_issues: list[dict[str, Any]] = []
        for label, expected in stage_target.items():
            actual = stage_counter.get(label, 0)
            if abs(actual - expected) > tolerance:
                skill_issues.append(
                    {
                        "severity": "warning",
                        "code": "stage_quota_imbalance",
                        "message": f"{skill_id} stage {label} has {actual} items; target is {expected}.",
                    }
                )
        for label, expected in difficulty_target.items():
            actual = difficulty_counter.get(label, 0)
            if abs(actual - expected) > tolerance:
                skill_issues.append(
                    {
                        "severity": "warning",
                        "code": "difficulty_quota_imbalance",
                        "message": f"{skill_id} difficulty band {label} has {actual} items; target is {expected}.",
                    }
                )
        quota_summary[skill_id] = {
            "stage_target": dict(stage_target),
            "stage_actual": dict(stage_counter),
            "difficulty_target": dict(difficulty_target),
            "difficulty_actual": dict(difficulty_counter),
            "issues": skill_issues,
        }
        for issue in skill_issues:
            quota_issues.append(BatchIssue(**issue))

    item_reports: list[dict[str, Any]] = []
    batch_stems: list[tuple[str, dict[str, Any]]] = []
    batch_variant_counts: Counter[str] = Counter()

    for index, item in enumerate(manifest.items, start=1):
        item_data = item.model_dump()
        item_data["batch_id"] = item_data.get("batch_id") or manifest.batch_id
        item_data["generation_prompt_version"] = (
            item_data.get("generation_prompt_version") or manifest.generation_prompt_version
        )
        item_data["authoring_source"] = item_data.get("authoring_source") or manifest.authoring_source
        item_data["source_key"] = item_data.get("source_key") or canonical_source_key(
            item.skill_id, manifest.batch_id, index
        )
        item_data["variant_group"] = _slugify(item_data["variant_group"])
        item_data["blueprint_id"] = _slugify(item_data["blueprint_id"])
        item_data["status"] = "active"

        refreshed = apply_content_refresh([SimpleNamespace(**item_data)])[0]
        issues = [_issue_dict(issue) for issue in collect_question_content_issues(refreshed)]
        quality = collect_question_quality_metadata(refreshed)
        stem = question_stem_signature(refreshed)

        duplicate_matches: list[dict[str, Any]] = []
        if stem:
            for existing_stem, questions in existing_stems.items():
                similarity = SequenceMatcher(a=stem, b=existing_stem).ratio()
                if similarity >= STEM_DUPLICATE_THRESHOLD:
                    match_question = questions[0]
                    issues.append(
                        {
                            "severity": "error",
                            "code": "duplicate_stem_existing",
                            "field": "text_ar",
                            "message": "This generated question duplicates an existing bank stem.",
                        }
                    )
                    duplicate_matches.append(
                        {
                            "scope": "existing",
                            "source_key": getattr(match_question, "source_key", None),
                            "similarity": round(similarity, 3),
                        }
                    )
                    break
                if similarity >= STEM_NEAR_DUPLICATE_THRESHOLD:
                    match_question = questions[0]
                    issues.append(
                        {
                            "severity": "warning",
                            "code": "near_duplicate_stem_existing",
                            "field": "text_ar",
                            "message": "This generated question is too similar to an existing bank stem.",
                        }
                    )
                    duplicate_matches.append(
                        {
                            "scope": "existing",
                            "source_key": getattr(match_question, "source_key", None),
                            "similarity": round(similarity, 3),
                        }
                    )
                    break

        if stem:
            for seen_stem, seen_report in batch_stems:
                similarity = SequenceMatcher(a=stem, b=seen_stem).ratio()
                if similarity >= STEM_DUPLICATE_THRESHOLD:
                    issues.append(
                        {
                            "severity": "error",
                            "code": "duplicate_stem_in_batch",
                            "field": "text_ar",
                            "message": "This generated question duplicates another stem in the same batch.",
                        }
                    )
                    duplicate_matches.append(
                        {
                            "scope": "batch",
                            "source_key": seen_report["source_key"],
                            "similarity": round(similarity, 3),
                        }
                    )
                    break
                if similarity >= STEM_NEAR_DUPLICATE_THRESHOLD:
                    issues.append(
                        {
                            "severity": "warning",
                            "code": "near_duplicate_stem_in_batch",
                            "field": "text_ar",
                            "message": "This generated question is too similar to another stem in the same batch.",
                        }
                    )
                    duplicate_matches.append(
                        {
                            "scope": "batch",
                            "source_key": seen_report["source_key"],
                            "similarity": round(similarity, 3),
                        }
                    )
                    break

        if batch_variant_counts[item_data["variant_group"]] + existing_variant_counts[item_data["variant_group"]] >= 2:
            issues.append(
                {
                    "severity": "warning",
                    "code": "variant_group_cap",
                    "field": "variant_group",
                    "message": "This variant_group already has two active items and should be held in review.",
                }
            )

        batch_stems.append((stem, item_data))
        batch_variant_counts[item_data["variant_group"]] += 1

        blocking_issues = [issue for issue in issues if issue["severity"] in {"error", "warning"}]
        batch_blocked = bool(quota_issues)
        auto_publish = not blocking_issues and not batch_blocked
        final_status = "active" if auto_publish else "review"
        if auto_publish:
            item_data["status"] = "active"
        else:
            item_data["status"] = "review"

        item_reports.append(
            {
                "index": index,
                "source_key": item_data["source_key"],
                "batch_id": item_data["batch_id"],
                "generation_prompt_version": item_data["generation_prompt_version"],
                "authoring_source": item_data["authoring_source"],
                "variant_group": item_data["variant_group"],
                "blueprint_id": item_data["blueprint_id"],
                "skill_id": item_data["skill_id"],
                "stage": item_data["stage"],
                "difficulty": item_data["difficulty"],
                "difficulty_bucket": difficulty_bucket(item_data["difficulty"]),
                "status": final_status,
                "auto_publish": auto_publish,
                "content_classification": quality["content_classification"],
                "recommended_action": quality["recommended_action"],
                "content_issue_counts": quality["content_issue_counts"],
                "duplicate_matches": duplicate_matches,
                "issues": blocking_issues,
                "question": item_data,
            }
        )

    by_skill = Counter(item["skill_id"] for item in item_reports)
    rejected = 0
    held_in_review = sum(1 for item in item_reports if item["status"] == "review")
    auto_published = sum(1 for item in item_reports if item["status"] == "active")
    duplicate_count = sum(1 for item in item_reports if item["duplicate_matches"])

    return {
        "batch_id": manifest.batch_id,
        "generated_at": manifest.generated_at,
        "generation_prompt_version": manifest.generation_prompt_version,
        "authoring_source": manifest.authoring_source,
        "metadata": manifest.metadata,
        "summary": {
            "generated": len(item_reports),
            "auto_published": auto_published,
            "held_in_review": held_in_review,
            "blocked_by_qa": held_in_review,
            "rejected": rejected,
            "duplicate_rate": round(duplicate_count / max(1, len(item_reports)), 3),
        },
        "by_skill": dict(by_skill),
        "quota_summary": quota_summary,
        "quota_issues": [_batch_issue_dict(issue) for issue in quota_issues],
        "items": item_reports,
    }


def build_import_manifest(report: dict[str, Any]) -> dict[str, Any]:
    items = [dict(item["question"]) for item in report["items"]]
    return build_manifest(
        batch_id=report["batch_id"],
        items=items,
        generation_prompt_version=report["generation_prompt_version"],
        authoring_source=report["authoring_source"],
        generated_at=report.get("generated_at"),
        metadata={
            "validation_summary": report.get("summary", {}),
            "quota_summary": report.get("quota_summary", {}),
        },
    )
