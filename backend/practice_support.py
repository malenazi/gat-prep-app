import json
import math
import re
from typing import Any

from question_content import clean_optional_text


DIFFICULTY_LABEL_BANDS = (
    (24, "Foundation"),
    (44, "Core"),
    (59, "Target"),
    (79, "Challenging"),
    (100, "Stretch"),
)

ANSWER_GIVEAWAY_PATTERNS = [
    re.compile(pattern, re.IGNORECASE)
    for pattern in (
        r"\bcorrect answer\b",
        r"\banswer is\b",
        r"\btherefore\b",
        r"\bso option\b",
        r"\bchoose option\b",
        r"\boption\s*[\(\[]?[a-d][\)\]]?\b",
        r"\bselect\s*[\(\[]?[a-d][\)\]]?\b",
        r"\bresult is\b",
    )
]

STEP_PREFIX_PATTERN = re.compile(r"^\s*(?:step\s*\d+[:.)-]?\s*|[-*•]\s*)", re.IGNORECASE)
WHITESPACE_PATTERN = re.compile(r"\s+")
FINAL_NUMERIC_PATTERN = re.compile(
    r"(?:(?:=|is)\s*)[-+]?\d+(?:\.\d+)?(?:/\d+)?(?:\s*[a-z%]+)?\.?$",
    re.IGNORECASE,
)
OPTION_SUFFIX_PATTERN = re.compile(r"[,;:\-– ]*\(?[a-d]\)?\s*$", re.IGNORECASE)


def _clamp(value: float, lower: float, upper: float) -> float:
    return max(lower, min(upper, value))


def _parse_solution_steps(raw_value: Any) -> list[str]:
    if raw_value is None:
        return []
    if isinstance(raw_value, list):
        return [step.strip() for step in raw_value if isinstance(step, str) and step.strip()]
    if isinstance(raw_value, str):
        try:
            parsed = json.loads(raw_value)
        except json.JSONDecodeError:
            return [raw_value.strip()] if raw_value.strip() else []
        if isinstance(parsed, list):
            return [step.strip() for step in parsed if isinstance(step, str) and step.strip()]
        if isinstance(parsed, str) and parsed.strip():
            return [parsed.strip()]
    return []


def difficulty_score_from_value(difficulty: float | None) -> int:
    normalized = _clamp(float(difficulty or 0.0), 0.0, 1.0)
    return int(round(normalized * 100))


def difficulty_label_for_score(score: int) -> str:
    clamped = int(_clamp(score, 0, 100))
    for upper_bound, label in DIFFICULTY_LABEL_BANDS:
        if clamped <= upper_bound:
            return label
    return "Stretch"


def challenge_band_for_delta(delta: float | None, calibrating: bool = False) -> str:
    if calibrating:
        return "Calibrating"
    if delta is None:
        return "At your level"
    if delta <= -0.30:
        return "Reinforcement"
    if delta <= 0.15:
        return "At your level"
    if delta <= 0.45:
        return "Stretch"
    return "Challenge+"


def selection_reason_for_band(skill_name: str, challenge_band: str) -> str:
    if challenge_band == "Calibrating":
        return f"Chosen to establish your starting level in {skill_name}."
    if challenge_band == "Reinforcement":
        return f"Chosen to reinforce accuracy in {skill_name}."
    if challenge_band == "Stretch":
        return f"Chosen as a stretch question in {skill_name}."
    if challenge_band == "Challenge+":
        return f"Chosen as a higher challenge in {skill_name}."
    return f"Chosen at your current level in {skill_name}."


def build_practice_adaptive_payload(question: Any, skill: Any, ability: Any) -> dict[str, Any]:
    skill_name = (
        clean_optional_text(getattr(skill, "name_ar", None))
        or clean_optional_text(getattr(skill, "name_en", None))
        or clean_optional_text(getattr(question, "skill_id", None))
        or "this skill"
    )
    skill_section = clean_optional_text(getattr(skill, "section", None)) or "general"
    difficulty_score = difficulty_score_from_value(getattr(question, "difficulty", 0.0))
    difficulty_label = difficulty_label_for_score(difficulty_score)

    calibrating = ability is None or int(getattr(ability, "questions_seen", 0) or 0) <= 0
    theta = None if calibrating else float(getattr(ability, "theta", 0.0) or 0.0)
    delta = None if theta is None else float(getattr(question, "difficulty", 0.0) or 0.0) - theta
    challenge_band = challenge_band_for_delta(delta, calibrating=calibrating)

    if calibrating:
        skill_mastery = 0
    else:
        skill_mastery = int(round(_clamp(float(getattr(ability, "mastery", 0.0) or 0.0), 0.0, 1.0) * 100))

    return {
        "skill_name": skill_name,
        "skill_section": skill_section,
        "difficulty_score": difficulty_score,
        "difficulty_label": difficulty_label,
        "skill_mastery": skill_mastery,
        "challenge_band": challenge_band,
        "selection_reason": selection_reason_for_band(skill_name, challenge_band),
    }


def _is_giveaway(text: str) -> bool:
    if any(pattern.search(text) for pattern in ANSWER_GIVEAWAY_PATTERNS):
        return True
    return bool(FINAL_NUMERIC_PATTERN.search(text))


def _normalize_hint_candidate(text: str) -> str | None:
    candidate = STEP_PREFIX_PATTERN.sub("", text.strip())
    candidate = OPTION_SUFFIX_PATTERN.sub("", candidate)
    candidate = WHITESPACE_PATTERN.sub(" ", candidate).strip(" .,-:;")

    if not candidate:
        return None
    if _is_giveaway(candidate):
        return None

    if not re.search(r"[.?!]$", candidate):
        candidate = f"{candidate}."
    return candidate


def _fallback_hint(question: Any, index: int) -> str:
    skill_id = clean_optional_text(getattr(question, "skill_id", None)) or ""
    question_type = clean_optional_text(getattr(question, "question_type", None)) or ""

    if skill_id == "quant_geometry":
        return (
            "Focus on the measurement the figure gives you and match it to the formula the question is asking for."
            if index == 0
            else "Set up the relationship before calculating, and keep the units consistent."
        )
    if skill_id == "quant_statistics":
        return (
            "Read every value in the table carefully and decide which quantity the question wants."
            if index == 0
            else "Write the operation you need first, then substitute the numbers from the table."
        )
    if skill_id.startswith("quant_"):
        return (
            "Notice what quantity the question is asking for before you start computing."
            if index == 0
            else "Turn the wording into a short setup or equation before solving."
        )
    if question_type == "reading" or skill_id.startswith("verbal_reading"):
        return (
            "Return to the line in the passage that most directly supports the answer."
            if index == 0
            else "Eliminate options that go beyond what the passage actually says."
        )
    return (
        "Look for the relationship or clue that narrows the options before choosing an answer."
        if index == 0
        else "Test your best choice against the wording one more time before selecting it."
    )


def build_practice_assistment_payload(question: Any) -> dict[str, Any]:
    steps = _parse_solution_steps(getattr(question, "solution_steps_ar", None))
    candidate_steps = steps[:-1] if len(steps) > 1 else steps[:1]
    hints: list[dict[str, Any]] = []

    for raw_step in candidate_steps:
        normalized = _normalize_hint_candidate(raw_step)
        if not normalized:
            continue
        hints.append(
            {
                "index": len(hints) + 1,
                "title": "Hint 1: What to notice" if len(hints) == 0 else "Hint 2: How to set it up",
                "text_ar": normalized,
            }
        )
        if len(hints) == 2:
            break

    while len(hints) < 2:
        hint_index = len(hints)
        fallback = _fallback_hint(question, hint_index)
        if hints and fallback == hints[-1]["text_ar"]:
            break
        hints.append(
            {
                "index": hint_index + 1,
                "title": "Hint 1: What to notice" if hint_index == 0 else "Hint 2: How to set it up",
                "text_ar": fallback,
            }
        )

    return {
        "hints_available": len(hints) > 0,
        "hints": hints[:2],
    }
