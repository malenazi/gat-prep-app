"""Fix CE (Contextual Error) questions:
1. Rebalance correct_option distribution to ~25% each for A/B/C/D
2. Fix 8 inconsistent questions where correct != bracketed word
3. Improve distractors: replace sentence-word distractors with better alternatives

Run: python fix_ce_questions.py
"""

import ast
import random
import re
import sys
from pathlib import Path
from collections import Counter

QUESTIONS_FILE = Path(__file__).parent / "questions" / "verbal_error.py"
BRACKET_PAT = re.compile(r'\(([^)]{1,40})\)')

# Better distractor pools for CE questions - contextual words that could plausibly
# be errors but aren't, organized by theme
DISTRACTOR_POOLS = {
    "positive": ["progress", "growth", "achievement", "success", "improvement", "development",
                  "stability", "prosperity", "advancement", "benefit", "strength", "harmony"],
    "negative": ["decline", "weakness", "failure", "loss", "harm", "damage",
                 "neglect", "corruption", "isolation", "conflict", "scarcity", "stagnation"],
    "action": ["contribute", "establish", "maintain", "promote", "achieve", "develop",
               "enhance", "support", "encourage", "facilitate", "implement", "preserve"],
    "quality": ["essential", "significant", "effective", "valuable", "crucial", "fundamental",
                "comprehensive", "sustainable", "innovative", "strategic", "systematic", "reliable"],
}


def load_questions():
    """Load questions from the source file using AST parsing."""
    source = QUESTIONS_FILE.read_text(encoding="utf-8")
    tree = ast.parse(source)

    # Find the return statement in get_questions()
    func = next(node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef) and node.name == "get_questions")
    return_stmt = next(node for node in ast.walk(func) if isinstance(node, ast.Return))
    list_node = return_stmt.value

    questions = []
    for call in list_node.elts:
        q = {}
        for kw in call.keywords:
            if isinstance(kw.value, ast.Constant):
                q[kw.arg] = kw.value.value
        questions.append(q)

    return questions


def rebalance_options(questions):
    """Shuffle option positions so correct_option is evenly distributed across A/B/C/D."""
    target_per_slot = len(questions) // 4
    slots = {"a": 0, "b": 0, "c": 0, "d": 0}
    changes = 0

    # Assign each question a target slot
    slot_queue = ["a"] * (target_per_slot + 1) + ["b"] * (target_per_slot + 1) + \
                 ["c"] * (target_per_slot + 1) + ["d"] * (target_per_slot + 1)
    random.shuffle(slot_queue)
    slot_queue = slot_queue[:len(questions)]

    for i, q in enumerate(questions):
        old_correct = q["correct_option"]
        new_correct = slot_queue[i]

        if old_correct == new_correct:
            slots[new_correct] += 1
            continue

        # Swap option values
        old_correct_text = q[f"option_{old_correct}"]
        new_slot_text = q[f"option_{new_correct}"]

        q[f"option_{new_correct}"] = old_correct_text
        q[f"option_{old_correct}"] = new_slot_text
        q["correct_option"] = new_correct
        slots[new_correct] += 1
        changes += 1

    print(f"Rebalanced {changes} questions")
    print(f"Distribution: {dict(slots)}")
    return questions


def fix_inconsistent(questions):
    """Fix the 8 questions where correct answer != bracketed word."""
    fixed = 0
    for q in questions:
        text = q.get("text_ar", "")
        match = BRACKET_PAT.search(text)
        if not match:
            continue
        bracketed = match.group(1).strip().lower()
        correct = q["correct_option"]
        correct_text = q.get(f"option_{correct}", "").strip().lower()

        if correct_text != bracketed:
            # Find which option has the bracketed word
            for k in "abcd":
                if q.get(f"option_{k}", "").strip().lower() == bracketed:
                    # Swap: make the bracketed word the correct answer
                    old_correct_text = q[f"option_{correct}"]
                    q[f"option_{correct}"] = q[f"option_{k}"]
                    q[f"option_{k}"] = old_correct_text
                    fixed += 1
                    break
            else:
                # Bracketed word isn't in any option — put it in the correct slot
                q[f"option_{correct}"] = match.group(1).strip()
                fixed += 1

    print(f"Fixed {fixed} inconsistent questions")
    return questions


def improve_distractors(questions):
    """Replace sentence-word distractors with better contextual alternatives."""
    improved = 0
    for q in questions:
        text = q.get("text_ar", "")
        text_words = set(text.lower().replace("(", "").replace(")", "").split())
        correct = q["correct_option"]
        correct_text = q.get(f"option_{correct}", "").strip().lower()

        # Check each distractor
        for k in "abcd":
            if k == correct:
                continue
            opt = q.get(f"option_{k}", "").strip().lower()
            if opt in text_words and len(opt) > 3:
                # This distractor is a word from the sentence — replace it
                # Pick a word from distractor pools that isn't already used
                used = {q.get(f"option_{x}", "").strip().lower() for x in "abcd"}
                used.add(correct_text)
                all_pool = []
                for pool in DISTRACTOR_POOLS.values():
                    all_pool.extend(pool)
                candidates = [w for w in all_pool if w.lower() not in used and w.lower() not in text_words]
                if candidates:
                    new_word = random.choice(candidates)
                    q[f"option_{k}"] = new_word
                    improved += 1

    print(f"Improved {improved} distractors")
    return questions


def write_questions(questions):
    """Write questions back to the source file."""
    lines = ['from models import Question\n\ndef get_questions():\n    return [']

    for i, q in enumerate(questions):
        # Build the Question() call
        parts = []
        field_order = [
            "skill_id", "question_type", "difficulty", "text_ar",
            "option_a", "option_b", "option_c", "option_d", "correct_option",
            "explanation_ar", "solution_steps_ar", "tags", "stage",
            "rating_clarity", "rating_cognitive", "rating_fairness",
            "rating_distractors", "rating_difficulty_align", "rating_explanation",
            "rating_discrimination", "rating_overall", "source_key",
        ]
        for field in field_order:
            if field not in q:
                continue
            val = q[field]
            if isinstance(val, str):
                escaped = val.replace("\\", "\\\\").replace("'", "\\'")
                parts.append(f"{field}='{escaped}'")
            elif isinstance(val, (int, float)):
                parts.append(f"{field}={val}")

        entry = "Question(" + ", ".join(parts) + ")"
        comma = "," if i < len(questions) - 1 else ""
        lines.append(f"        {entry}{comma}")

    lines.append("    ]")
    lines.append("")

    QUESTIONS_FILE.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {len(questions)} questions to {QUESTIONS_FILE}")


def main():
    random.seed(42)  # Reproducible
    questions = load_questions()
    print(f"Loaded {len(questions)} CE questions")

    # Step 1: Fix inconsistent
    questions = fix_inconsistent(questions)

    # Step 2: Improve distractors
    questions = improve_distractors(questions)

    # Step 3: Rebalance
    questions = rebalance_options(questions)

    # Verify
    dist = Counter(q["correct_option"] for q in questions)
    print(f"\nFinal distribution: {dict(sorted(dist.items()))}")

    # Write
    write_questions(questions)


if __name__ == "__main__":
    main()
