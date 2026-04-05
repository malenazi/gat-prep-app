import json
import re
from dataclasses import dataclass
from difflib import SequenceMatcher
from typing import Any, Iterable, Optional

from sqlalchemy import inspect, text

from question_visuals import deserialize_table_payload


CONTENT_FORMAT_PLAIN = "plain"
CONTENT_FORMAT_MARKDOWN_MATH = "markdown_math"
VALID_CONTENT_FORMATS = {CONTENT_FORMAT_PLAIN, CONTENT_FORMAT_MARKDOWN_MATH}

CONTENT_CLASS_READY = "ready"
CONTENT_CLASS_SAFE_AUTO = "safe-to-auto-convert"
CONTENT_CLASS_MANUAL = "needs-manual-cleanup"
CONTENT_CLASS_CORRUPTED = "content-corrupted"

RECOMMENDED_ACTION_READY = "keep-active"
RECOMMENDED_ACTION_AUTO_FIX = "auto-fix-and-sync"
RECOMMENDED_ACTION_MANUAL = "manual-review"
RECOMMENDED_ACTION_REVIEW = "keep-in-review"

RATING_FIELDS = (
    "rating_clarity",
    "rating_cognitive",
    "rating_distractors",
    "rating_difficulty_align",
    "rating_explanation",
    "rating_fairness",
    "rating_discrimination",
)

HIGH_PRIORITY_QUANT_SKILLS = {
    "quant_arithmetic",
    "quant_algebra",
    "quant_statistics",
}

AUTO_REVIEW_EXEMPT_AUTHORING_SOURCES = {
    "ai_generated",
}

CORRUPTION_SUSPECT_SKILLS = {
    "quant_geometry",
    "quant_statistics",
}

AUTO_FIXABLE_ISSUE_CODES = {
    "legacy_math_syntax",
    "missing_table_caption",
    "comparison_columns_missing",
    "weak_table_caption",
    "weak_figure_alt",
}

PLACEHOLDER_DISTRACTORS = {
    "",
    "-",
    "na",
    "n/a",
    "none",
    "...",
    "tbd",
    "placeholder",
}

CORRUPTION_PATTERNS = [
    re.compile(pattern)
    for pattern in (
        r"\uFFFD",
        r"Ãƒ.",
        r"Ã¢.",
        r"Ã°Å¸",
        r"\bArea ofof\b",
        r"\bVolume of =\b",
        r"\bdrawn Circle\b",
        r"\bCircle center, \(r\)\b",
    )
]

LEGACY_MATH_PATTERNS = [
    re.compile(pattern)
    for pattern in (
        r"(?<![$\\])\b\d+\s*/\s*\d+\b",
        r"\bsqrt\s*\(",
        r"(?<![$\\])\^[A-Za-z0-9(]",
        r"\+/-",
        r"[âˆšâˆ›]",
        r"[ÃƒÃ¢][Ã—Ã·]",
    )
]

COMPARISON_REGEX = re.compile(
    r"^(?P<intro>.*?)(?:\n+)?(?:[\u2022\u25B8*\-]\s*)?Column\s*\(?A\)?\s*:\s*(?P<a>.*?)(?:\n+)(?:[\u2022\u25B8*\-]\s*)?Column\s*\(?B\)?\s*:\s*(?P<b>.+)$",
    re.IGNORECASE | re.DOTALL,
)

ANSWER_MATCH_REGEX = re.compile(
    r"(?:correct answer|answer is|therefore option)\s*(?:is|:)?\s*[\(\[]?([a-d])[\)\]]?",
    re.IGNORECASE,
)

UNICODE_FRACTION_REPLACEMENTS = (
    ("Â½", r"\frac{1}{2}"),
    ("Â¼", r"\frac{1}{4}"),
    ("Â¾", r"\frac{3}{4}"),
    ("â…“", r"\frac{1}{3}"),
    ("â…”", r"\frac{2}{3}"),
    ("â…•", r"\frac{1}{5}"),
    ("â…—", r"\frac{3}{5}"),
    ("â…™", r"\frac{1}{6}"),
    ("â…›", r"\frac{1}{8}"),
)


@dataclass
class QuestionContentIssue:
    severity: str
    code: str
    field: str
    message: str


def clean_optional_text(value: Optional[str]) -> Optional[str]:
    if value is None:
        return None
    trimmed = value.strip()
    return trimmed or None


def is_quant_skill(skill_id: Optional[str]) -> bool:
    return bool(skill_id and skill_id.startswith("quant_"))


def validate_content_format(value: Optional[str]) -> str:
    normalized = clean_optional_text(value) or CONTENT_FORMAT_PLAIN
    if normalized not in VALID_CONTENT_FORMATS:
        raise ValueError(
            f"content_format must be one of: {', '.join(sorted(VALID_CONTENT_FORMATS))}"
        )
    return normalized


def validate_comparison_columns(value: Any) -> Optional[dict[str, str]]:
    if value is None:
        return None
    if not isinstance(value, dict):
        raise ValueError("comparison_columns must be an object with a and b")

    normalized: dict[str, str] = {}
    for key in ("a", "b"):
        raw = value.get(key)
        if not isinstance(raw, str) or not raw.strip():
            raise ValueError("comparison_columns requires non-empty a and b values")
        normalized[key] = raw.strip()
    return normalized


def serialize_comparison_columns(value: Any) -> Optional[str]:
    normalized = validate_comparison_columns(value)
    if normalized is None:
        return None
    return json.dumps(normalized, ensure_ascii=False)


def deserialize_comparison_columns(raw_value: Optional[str]) -> Optional[dict[str, str]]:
    raw_value = clean_optional_text(raw_value)
    if raw_value is None:
        return None
    try:
        parsed = json.loads(raw_value)
    except json.JSONDecodeError as exc:
        raise ValueError("Stored comparison_columns payload is not valid JSON") from exc
    return validate_comparison_columns(parsed)


def extract_comparison_columns(
    text: Optional[str],
) -> tuple[Optional[str], Optional[dict[str, str]]]:
    if not text:
        return text, None

    match = COMPARISON_REGEX.match(text.strip())
    if not match:
        return text, None

    intro = (match.group("intro") or "").strip().rstrip(":")
    return intro or "Compare the two columns.", {
        "a": match.group("a").strip(),
        "b": match.group("b").strip(),
    }


def _parse_solution_steps(raw_value: Any) -> list[str]:
    if raw_value is None:
        return []
    if isinstance(raw_value, list):
        return [step for step in raw_value if isinstance(step, str) and step.strip()]
    if isinstance(raw_value, str):
        try:
            parsed = json.loads(raw_value)
        except json.JSONDecodeError:
            return [raw_value] if raw_value.strip() else []
        if isinstance(parsed, list):
            return [step for step in parsed if isinstance(step, str) and step.strip()]
        if isinstance(parsed, str) and parsed.strip():
            return [parsed]
    return []


def repair_common_mojibake(value: str) -> str:
    repaired = value
    replacements = (
        ("Ãƒâ€”", "Ã—"),
        ("ÃƒÂ·", "Ã·"),
        ("Ã¢Ë†â€™", "âˆ’"),
        ("Ã¢â€°Â¤", "â‰¤"),
        ("Ã¢â€°Â¥", "â‰¥"),
        ("Ã¢â€°Â ", "â‰ "),
        ("Ã¢Ë†Å¡", "âˆš"),
        ("Ã¢Ë†â€º", "âˆ›"),
        ("Ãâ‚¬", "Ï€"),
    )
    for bad, good in replacements:
        repaired = repaired.replace(bad, good)
    return repaired


def normalize_math_markdown(value: Optional[str]) -> Optional[str]:
    if value is None:
        return None

    normalized = repair_common_mojibake(value)

    for raw_fraction, tex_fraction in UNICODE_FRACTION_REPLACEMENTS:
        normalized = normalized.replace(raw_fraction, f"${tex_fraction}$")

    normalized = re.sub(
        r"(?<![$\\])\b(\d+)\s*/\s*(\d+)\b",
        lambda match: f"$\\frac{{{match.group(1)}}}{{{match.group(2)}}}$",
        normalized,
    )
    normalized = re.sub(
        r"\bsqrt\s*\(\s*([^)]+?)\s*\)",
        lambda match: f"$\\sqrt{{{match.group(1).strip()}}}$",
        normalized,
    )
    normalized = re.sub(
        r"\b([A-Za-z0-9]+)\^\((-?\d+)\)",
        lambda match: f"${match.group(1)}^{{{match.group(2)}}}$",
        normalized,
    )
    normalized = re.sub(
        r"\b([A-Za-z0-9]+)\^(\d+)\b",
        lambda match: f"${match.group(1)}^{{{match.group(2)}}}$",
        normalized,
    )
    normalized = re.sub(
        r"\b([A-Za-z0-9]+)\^\(1/([23])\)",
        lambda match: f"$\\sqrt[{match.group(2)}]{{{match.group(1)}}}$",
        normalized,
    )
    normalized = re.sub(
        r"âˆš\s*([A-Za-z0-9]+)",
        lambda match: f"$\\sqrt{{{match.group(1)}}}$",
        normalized,
    )
    normalized = re.sub(
        r"âˆ›\s*([A-Za-z0-9]+)",
        lambda match: f"$\\sqrt[3]{{{match.group(1)}}}$",
        normalized,
    )
    normalized = re.sub(
        r"\bpi\b",
        lambda _match: r"$\pi$",
        normalized,
        flags=re.IGNORECASE,
    )

    normalized = normalized.replace("+/-", r"$\pm$")
    normalized = normalized.replace("Ã—", r" $\times$ ")
    normalized = normalized.replace("Ã·", r" $\div$ ")
    normalized = normalized.replace("â‰¤", r" $\leq$ ")
    normalized = normalized.replace("â‰¥", r" $\geq$ ")
    normalized = normalized.replace("â‰ ", r" $\neq$ ")
    normalized = normalized.replace("âˆ’", " - ")

    normalized = re.sub(r"[ \t]{2,}", " ", normalized)
    normalized = re.sub(r" ?\n ?", "\n", normalized)
    return normalized.strip()


def suggest_figure_alt(skill_id: str, question_type: str, text: str) -> str:
    stem = text.strip().splitlines()[0] if text.strip() else "question"
    return (
        f"Figure for {question_type} question in {skill_id.replace('_', ' ')}: "
        f"{stem[:80].rstrip('.')}."
    )


def suggest_table_caption(skill_id: str, question_type: str) -> str:
    return f"Data table for {question_type} question in {skill_id.replace('_', ' ')}."


def _normalized_option_key(value: Optional[str]) -> str:
    normalized = clean_optional_text(value) or ""
    normalized = re.sub(r"[$\\{}[\]()*^_]", " ", normalized)
    normalized = re.sub(r"[^A-Za-z0-9]+", "", normalized).lower()
    return normalized


def _collect_math_markup_issues(field_name: str, value: str) -> list[QuestionContentIssue]:
    issues: list[QuestionContentIssue] = []
    if not value.strip():
        return issues

    dollar_count = len(re.findall(r"(?<!\\)\$", value))
    if dollar_count % 2 != 0:
        issues.append(
            QuestionContentIssue(
                severity="error",
                code="malformed_math_markup",
                field=field_name,
                message=f"{field_name} contains unbalanced math delimiters.",
            )
        )

    if ("$" in value or "\\" in value) and value.count("{") != value.count("}"):
        issues.append(
            QuestionContentIssue(
                severity="error",
                code="malformed_math_markup",
                field=field_name,
                message=f"{field_name} contains unbalanced braces in Markdown/TeX content.",
            )
        )

    return issues


def get_missing_review_ratings(question: Any) -> list[str]:
    return [field for field in RATING_FIELDS if getattr(question, field, None) is None]


def ratings_complete(question: Any) -> bool:
    return len(get_missing_review_ratings(question)) == 0


def summarize_issue_counts(issues: Iterable[QuestionContentIssue]) -> dict[str, int]:
    counts = {"error": 0, "warning": 0, "info": 0}
    for issue in issues:
        counts[issue.severity] = counts.get(issue.severity, 0) + 1
    return counts


def collect_question_content_issues(question: Any) -> list[QuestionContentIssue]:
    issues: list[QuestionContentIssue] = []
    content_format = validate_content_format(getattr(question, "content_format", None))
    fields = {
        "text_ar": getattr(question, "text_ar", None),
        "passage_ar": getattr(question, "passage_ar", None),
        "option_a": getattr(question, "option_a", None),
        "option_b": getattr(question, "option_b", None),
        "option_c": getattr(question, "option_c", None),
        "option_d": getattr(question, "option_d", None),
        "explanation_ar": getattr(question, "explanation_ar", None),
    }
    for index, step in enumerate(_parse_solution_steps(getattr(question, "solution_steps_ar", None))):
        fields[f"solution_steps_ar[{index}]"] = step

    for field_name, value in fields.items():
        if not isinstance(value, str) or not value.strip():
            continue

        for pattern in CORRUPTION_PATTERNS:
            if pattern.search(value):
                issues.append(
                    QuestionContentIssue(
                        severity="error",
                        code="content_corruption",
                        field=field_name,
                        message=f"{field_name} appears to contain broken or corrupted text.",
                    )
                )
                break

        for pattern in LEGACY_MATH_PATTERNS:
            if pattern.search(value):
                issues.append(
                    QuestionContentIssue(
                        severity="warning",
                        code="legacy_math_syntax",
                        field=field_name,
                        message=f"{field_name} still uses legacy math syntax that should be migrated.",
                    )
                )
                break

        if content_format == CONTENT_FORMAT_MARKDOWN_MATH or "$" in value or "\\" in value:
            issues.extend(_collect_math_markup_issues(field_name, value))

    if getattr(question, "figure_svg", None):
        figure_alt = clean_optional_text(getattr(question, "figure_alt", None))
        if not figure_alt:
            issues.append(
                QuestionContentIssue(
                    severity="error",
                    code="missing_figure_alt",
                    field="figure_alt",
                    message="figure_alt is required when figure_svg is provided.",
                )
            )
        elif len(figure_alt) < 12:
            issues.append(
                QuestionContentIssue(
                    severity="warning",
                    code="weak_figure_alt",
                    field="figure_alt",
                    message="figure_alt is too brief to be helpful for assistive technology.",
                )
            )

    raw_table = getattr(question, "table_ar", None)
    if raw_table:
        try:
            deserialize_table_payload(raw_table if isinstance(raw_table, str) else json.dumps(raw_table, ensure_ascii=False))
        except (TypeError, ValueError):
            issues.append(
                QuestionContentIssue(
                    severity="error",
                    code="invalid_table_payload",
                    field="table_ar",
                    message="table_ar is not valid structured table data.",
                )
            )

        table_caption = clean_optional_text(getattr(question, "table_caption", None))
        if not table_caption:
            issues.append(
                QuestionContentIssue(
                    severity="warning",
                    code="missing_table_caption",
                    field="table_caption",
                    message="table_caption is required when table_ar is provided.",
                )
            )
        elif len(table_caption) < 12:
            issues.append(
                QuestionContentIssue(
                    severity="info",
                    code="weak_table_caption",
                    field="table_caption",
                    message="table_caption should explain the table more clearly.",
                )
            )

    comparison_columns = getattr(question, "comparison_columns", None)
    if isinstance(comparison_columns, str):
        try:
            comparison_columns = deserialize_comparison_columns(comparison_columns)
        except ValueError:
            issues.append(
                QuestionContentIssue(
                    severity="error",
                    code="invalid_comparison_columns",
                    field="comparison_columns",
                    message="comparison_columns is not valid JSON with a/b values.",
                )
            )
            comparison_columns = None

    if getattr(question, "question_type", "") == "comparison":
        if not comparison_columns:
            extracted_text, extracted_columns = extract_comparison_columns(getattr(question, "text_ar", None))
            if extracted_columns and extracted_text is not None:
                issues.append(
                    QuestionContentIssue(
                        severity="warning",
                        code="comparison_columns_missing",
                        field="comparison_columns",
                        message="comparison question should use comparison_columns instead of inline text.",
                    )
                )
            else:
                issues.append(
                    QuestionContentIssue(
                        severity="error",
                        code="comparison_columns_missing",
                        field="comparison_columns",
                        message="comparison questions require explicit Column A and Column B values.",
                    )
                )

    options = {
        "a": getattr(question, "option_a", None),
        "b": getattr(question, "option_b", None),
        "c": getattr(question, "option_c", None),
        "d": getattr(question, "option_d", None),
    }
    normalized_options: dict[str, str] = {}
    for key, value in options.items():
        normalized_value = _normalized_option_key(value)
        normalized_options[key] = normalized_value
        if normalized_value in PLACEHOLDER_DISTRACTORS:
            issues.append(
                QuestionContentIssue(
                    severity="warning",
                    code="placeholder_distractor",
                    field=f"option_{key}",
                    message=f"Option {key.upper()} is empty or placeholder-like.",
                )
            )

    option_items = list(normalized_options.items())
    for index, (left_key, left_value) in enumerate(option_items):
        if not left_value:
            continue
        for right_key, right_value in option_items[index + 1 :]:
            if not right_value:
                continue
            if left_value == right_value:
                issues.append(
                    QuestionContentIssue(
                        severity="warning",
                        code="duplicate_options",
                        field=f"option_{left_key}",
                        message=f"Options {left_key.upper()} and {right_key.upper()} are duplicates.",
                    )
                )
                continue
            similarity = SequenceMatcher(a=left_value, b=right_value).ratio()
            if similarity >= 0.93:
                issues.append(
                    QuestionContentIssue(
                        severity="warning",
                        code="near_duplicate_options",
                        field=f"option_{left_key}",
                        message=f"Options {left_key.upper()} and {right_key.upper()} are too similar.",
                    )
                )

    if is_quant_skill(getattr(question, "skill_id", None)):
        explanation = clean_optional_text(getattr(question, "explanation_ar", None))
        steps = _parse_solution_steps(getattr(question, "solution_steps_ar", None))
        if not explanation:
            issues.append(
                QuestionContentIssue(
                    severity="warning",
                    code="missing_explanation",
                    field="explanation_ar",
                    message="Quant questions need an explanation before they can return to active.",
                )
            )
        if not steps:
            issues.append(
                QuestionContentIssue(
                    severity="warning",
                    code="missing_solution_steps",
                    field="solution_steps_ar",
                    message="Quant questions need worked solution steps before they can return to active.",
                )
            )
        elif len(steps) < 2:
            issues.append(
                QuestionContentIssue(
                    severity="warning",
                    code="weak_solution_steps",
                    field="solution_steps_ar",
                    message="Solution steps should show more than a single-step shortcut.",
                )
            )

    explanation_text = clean_optional_text(getattr(question, "explanation_ar", None)) or ""
    correct_option = (getattr(question, "correct_option", "") or "").lower()
    answer_match = ANSWER_MATCH_REGEX.search(explanation_text)
    if answer_match and answer_match.group(1).lower() != correct_option:
        issues.append(
            QuestionContentIssue(
                severity="warning",
                code="answer_explanation_mismatch",
                field="explanation_ar",
                message="The explanation appears to reference a different correct option.",
            )
        )

    deduped: list[QuestionContentIssue] = []
    seen = set()
    for issue in issues:
        key = (issue.severity, issue.code, issue.field, issue.message)
        if key in seen:
            continue
        seen.add(key)
        deduped.append(issue)
    return deduped


def classify_question_content(
    question: Any,
    issues: Optional[list[QuestionContentIssue]] = None,
) -> str:
    issues = issues or collect_question_content_issues(question)
    if any(issue.severity == "error" for issue in issues):
        return CONTENT_CLASS_CORRUPTED

    warning_codes = {issue.code for issue in issues if issue.severity == "warning"}
    if warning_codes and warning_codes.issubset(AUTO_FIXABLE_ISSUE_CODES):
        return CONTENT_CLASS_SAFE_AUTO
    if warning_codes:
        return CONTENT_CLASS_MANUAL
    return CONTENT_CLASS_READY


def recommended_action_for_classification(classification: str) -> str:
    if classification == CONTENT_CLASS_CORRUPTED:
        return RECOMMENDED_ACTION_REVIEW
    if classification == CONTENT_CLASS_MANUAL:
        return RECOMMENDED_ACTION_MANUAL
    if classification == CONTENT_CLASS_SAFE_AUTO:
        return RECOMMENDED_ACTION_AUTO_FIX
    return RECOMMENDED_ACTION_READY


def collect_question_quality_metadata(
    question: Any,
    issues: Optional[list[QuestionContentIssue]] = None,
) -> dict[str, Any]:
    issues = issues or collect_question_content_issues(question)
    classification = classify_question_content(question, issues)
    return {
        "content_classification": classification,
        "recommended_action": recommended_action_for_classification(classification),
        "content_issue_counts": summarize_issue_counts(issues),
        "ratings_complete": ratings_complete(question),
        "missing_review_ratings": get_missing_review_ratings(question),
        "source_key": clean_optional_text(getattr(question, "source_key", None)),
        "batch_id": clean_optional_text(getattr(question, "batch_id", None)),
        "generation_prompt_version": clean_optional_text(
            getattr(question, "generation_prompt_version", None)
        ),
        "authoring_source": clean_optional_text(getattr(question, "authoring_source", None)),
        "variant_group": clean_optional_text(getattr(question, "variant_group", None)),
    }


def requires_manual_review(question: Any) -> bool:
    authoring_source = clean_optional_text(getattr(question, "authoring_source", None))
    return authoring_source not in AUTO_REVIEW_EXEMPT_AUTHORING_SOURCES


def activation_blockers(question: Any) -> list[str]:
    issues = collect_question_content_issues(question)
    blockers = [issue.message for issue in issues if issue.severity in {"error", "warning"}]

    if is_quant_skill(getattr(question, "skill_id", None)):
        if not clean_optional_text(getattr(question, "explanation_ar", None)):
            blockers.append("Quant questions must include an explanation before they can be active.")
        if not _parse_solution_steps(getattr(question, "solution_steps_ar", None)):
            blockers.append("Quant questions must include solution steps before they can be active.")

    if requires_manual_review(question):
        if not ratings_complete(question):
            blockers.append("All seven review ratings must be completed before a question can be active.")

        if int(getattr(question, "rating_passes_done", 0) or 0) < 1:
            blockers.append("At least one review pass is required before a question can be active.")

    deduped: list[str] = []
    for blocker in blockers:
        if blocker not in deduped:
            deduped.append(blocker)
    return deduped


def ensure_question_content_columns(engine) -> None:
    inspector = inspect(engine)
    if "questions" not in inspector.get_table_names():
        return

    existing_columns = {column["name"] for column in inspector.get_columns("questions")}
    statements: list[str] = []

    if "source_key" not in existing_columns:
        statements.append("ALTER TABLE questions ADD COLUMN source_key TEXT")
    if "content_format" not in existing_columns:
        statements.append("ALTER TABLE questions ADD COLUMN content_format TEXT DEFAULT 'plain'")
    if "figure_alt" not in existing_columns:
        statements.append("ALTER TABLE questions ADD COLUMN figure_alt TEXT")
    if "table_caption" not in existing_columns:
        statements.append("ALTER TABLE questions ADD COLUMN table_caption TEXT")
    if "comparison_columns" not in existing_columns:
        statements.append("ALTER TABLE questions ADD COLUMN comparison_columns TEXT")
    if "batch_id" not in existing_columns:
        statements.append("ALTER TABLE questions ADD COLUMN batch_id TEXT")
    if "generation_prompt_version" not in existing_columns:
        statements.append("ALTER TABLE questions ADD COLUMN generation_prompt_version TEXT")
    if "authoring_source" not in existing_columns:
        statements.append("ALTER TABLE questions ADD COLUMN authoring_source TEXT")
    if "variant_group" not in existing_columns:
        statements.append("ALTER TABLE questions ADD COLUMN variant_group TEXT")

    with engine.begin() as connection:
        for statement in statements:
            connection.execute(text(statement))
        connection.execute(
            text("CREATE INDEX IF NOT EXISTS ix_questions_source_key ON questions(source_key)")
        )
        connection.execute(
            text("CREATE INDEX IF NOT EXISTS ix_questions_batch_id ON questions(batch_id)")
        )
        connection.execute(
            text("CREATE INDEX IF NOT EXISTS ix_questions_variant_group ON questions(variant_group)")
        )


def apply_content_refresh(questions: Iterable[Any]) -> list[Any]:
    refreshed: list[Any] = []

    for question in questions:
        question.source_key = clean_optional_text(getattr(question, "source_key", None))
        question.batch_id = clean_optional_text(getattr(question, "batch_id", None))
        question.generation_prompt_version = clean_optional_text(
            getattr(question, "generation_prompt_version", None)
        )
        question.authoring_source = clean_optional_text(
            getattr(question, "authoring_source", None)
        ) or "human"
        question.variant_group = clean_optional_text(getattr(question, "variant_group", None))
        question.content_format = validate_content_format(
            getattr(question, "content_format", None)
        )
        question.status = getattr(question, "status", None) or "active"
        question.figure_alt = clean_optional_text(getattr(question, "figure_alt", None))
        question.table_caption = clean_optional_text(getattr(question, "table_caption", None))

        comparison_columns = getattr(question, "comparison_columns", None)
        if isinstance(comparison_columns, str):
            try:
                comparison_columns = deserialize_comparison_columns(comparison_columns)
            except ValueError:
                comparison_columns = None

        if not comparison_columns and getattr(question, "question_type", "") == "comparison":
            cleaned_text, extracted = extract_comparison_columns(getattr(question, "text_ar", None))
            if extracted:
                question.text_ar = cleaned_text or "Compare the two columns."
                comparison_columns = extracted

        question.comparison_columns = serialize_comparison_columns(comparison_columns)

        if getattr(question, "figure_svg", None) and not question.figure_alt:
            question.figure_alt = suggest_figure_alt(
                getattr(question, "skill_id", "question"),
                getattr(question, "question_type", "question"),
                getattr(question, "text_ar", ""),
            )

        if getattr(question, "table_ar", None) and not question.table_caption:
            question.table_caption = suggest_table_caption(
                getattr(question, "skill_id", "question"),
                getattr(question, "question_type", "question"),
            )

        if is_quant_skill(getattr(question, "skill_id", None)):
            question.text_ar = normalize_math_markdown(getattr(question, "text_ar", None)) or ""
            question.passage_ar = normalize_math_markdown(getattr(question, "passage_ar", None))
            question.option_a = normalize_math_markdown(getattr(question, "option_a", None)) or ""
            question.option_b = normalize_math_markdown(getattr(question, "option_b", None)) or ""
            question.option_c = normalize_math_markdown(getattr(question, "option_c", None)) or ""
            question.option_d = normalize_math_markdown(getattr(question, "option_d", None)) or ""
            question.explanation_ar = normalize_math_markdown(
                getattr(question, "explanation_ar", None)
            )

            steps = _parse_solution_steps(getattr(question, "solution_steps_ar", None))
            if steps:
                question.solution_steps_ar = json.dumps(
                    [normalize_math_markdown(step) or "" for step in steps],
                    ensure_ascii=False,
                )

            if getattr(question, "skill_id", "") in HIGH_PRIORITY_QUANT_SKILLS:
                question.content_format = CONTENT_FORMAT_MARKDOWN_MATH

        issues = collect_question_content_issues(question)
        classification = classify_question_content(question, issues)
        if classification == CONTENT_CLASS_CORRUPTED and question.status == "active":
            question.status = "review"
        elif (
            getattr(question, "skill_id", "") in CORRUPTION_SUSPECT_SKILLS
            and classification == CONTENT_CLASS_MANUAL
            and question.status == "active"
        ):
            question.status = "review"

        refreshed.append(question)

    return refreshed
