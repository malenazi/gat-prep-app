"""Rebalance correct_option distribution across all question skills.

For each skill, shuffles option positions so A/B/C/D each get ~25%.
Preserves option text and correct answer — only swaps which slot holds
the correct answer.

Run: python rebalance_options.py
"""

import ast
import random
import sys
from pathlib import Path
from collections import Counter

QUESTIONS_DIR = Path(__file__).parent / "questions"

# Map skill_id to source file
SKILL_FILES = {
    "verbal_reading": "verbal_reading.py",
    "verbal_analogy": "verbal_analogy.py",
    "verbal_completion": "verbal_completion.py",
    "verbal_error": "verbal_error.py",
    "verbal_oddword": "verbal_oddword.py",
    "quant_arithmetic": "quant_arithmetic.py",
    "quant_geometry": "quant_geometry.py",
    "quant_algebra": "quant_algebra.py",
    "quant_statistics": "quant_statistics.py",
}


def load_questions_from_file(filepath):
    source = filepath.read_text(encoding="utf-8")
    tree = ast.parse(source)
    func = next(n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and n.name == "get_questions")
    ret = next(n for n in ast.walk(func) if isinstance(n, ast.Return))
    questions = []
    for call in ret.value.elts:
        q = {}
        for kw in call.keywords:
            if isinstance(kw.value, ast.Constant):
                q[kw.arg] = kw.value.value
        questions.append(q)
    return questions


def rebalance(questions):
    n = len(questions)
    if n < 4:
        return questions, 0

    # Build target slots: each key gets n/4 questions
    per_slot = n // 4
    remainder = n % 4
    slot_counts = {"a": per_slot, "b": per_slot, "c": per_slot, "d": per_slot}
    for i, k in enumerate("abcd"):
        if i < remainder:
            slot_counts[k] += 1

    # Build queue of target slots
    slot_queue = []
    for k in "abcd":
        slot_queue.extend([k] * slot_counts[k])
    random.shuffle(slot_queue)

    changes = 0
    for i, q in enumerate(questions):
        old_correct = q.get("correct_option", "a")
        new_correct = slot_queue[i]

        if old_correct == new_correct:
            continue

        # Swap the option values between old and new positions
        old_key = f"option_{old_correct}"
        new_key = f"option_{new_correct}"
        if old_key in q and new_key in q:
            q[old_key], q[new_key] = q[new_key], q[old_key]
            q["correct_option"] = new_correct
            changes += 1

    return questions, changes


def write_questions(filepath, questions):
    lines = ["from models import Question\n\ndef get_questions():\n    return ["]

    field_order = [
        "skill_id", "question_type", "difficulty", "text_ar",
        "option_a", "option_b", "option_c", "option_d", "correct_option",
        "explanation_ar", "solution_steps_ar", "tags", "stage",
        "rating_clarity", "rating_cognitive", "rating_fairness",
        "rating_distractors", "rating_difficulty_align", "rating_explanation",
        "rating_discrimination", "rating_overall", "source_key",
        "content_format",
    ]

    for i, q in enumerate(questions):
        parts = []
        for field in field_order:
            if field not in q:
                continue
            val = q[field]
            if isinstance(val, str):
                escaped = val.replace("\\", "\\\\").replace("'", "\\'").replace("\n", "\\n")
                parts.append(f"{field}='{escaped}'")
            elif isinstance(val, (int, float)):
                parts.append(f"{field}={val}")
        entry = "Question(" + ", ".join(parts) + ")"
        comma = "," if i < len(questions) - 1 else ""
        lines.append(f"        {entry}{comma}")

    lines.append("    ]")
    lines.append("")
    filepath.write_text("\n".join(lines), encoding="utf-8")


def main():
    random.seed(42)
    skills_to_fix = sys.argv[1:] if len(sys.argv) > 1 else list(SKILL_FILES.keys())

    for skill_id in skills_to_fix:
        if skill_id not in SKILL_FILES:
            print(f"Unknown skill: {skill_id}")
            continue

        filepath = QUESTIONS_DIR / SKILL_FILES[skill_id]
        if not filepath.exists():
            print(f"File not found: {filepath}")
            continue

        questions = load_questions_from_file(filepath)
        dist_before = Counter(q.get("correct_option", "?") for q in questions)

        questions, changes = rebalance(questions)
        dist_after = Counter(q.get("correct_option", "?") for q in questions)

        if changes == 0:
            print(f"{skill_id}: already balanced {dict(sorted(dist_before.items()))}")
            continue

        write_questions(filepath, questions)
        print(f"{skill_id}: rebalanced {changes}/{len(questions)} questions")
        print(f"  before: {dict(sorted(dist_before.items()))}")
        print(f"  after:  {dict(sorted(dist_after.items()))}")


if __name__ == "__main__":
    main()
