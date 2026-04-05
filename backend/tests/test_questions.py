"""
Question bank loading and validation tests.
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from questions import load_all_questions

EXPECTED_SKILLS = [
    'verbal_reading',
    'verbal_analogy',
    'verbal_completion',
    'verbal_error',
    'verbal_oddword',
    'quant_arithmetic',
    'quant_geometry',
    'quant_algebra',
    'quant_statistics',
]


def test_all_questions_load():
    questions = load_all_questions()
    print(f"Loaded {len(questions)} questions")

    assert questions, "No questions loaded"
    assert len(questions) >= 1300, f"Expected at least 1300 questions, got {len(questions)}"


def test_question_structure():
    questions = load_all_questions()
    required_fields = [
        'skill_id',
        'question_type',
        'text_ar',
        'option_a',
        'option_b',
        'option_c',
        'option_d',
        'correct_option',
        'explanation_ar',
        'difficulty',
    ]

    errors: list[str] = []
    for question in questions[:100]:
        for field in required_fields:
            if not hasattr(question, field) or getattr(question, field) is None:
                question_label = getattr(question, 'skill_id', 'unknown-skill')
                errors.append(f"Question ({question_label}) missing field: {field}")

    assert not errors, '\n'.join(errors[:10])


def test_skill_coverage():
    questions = load_all_questions()
    skills_found: dict[str, int] = {}

    for question in questions:
        skills_found[question.skill_id] = skills_found.get(question.skill_id, 0) + 1

    missing = [skill for skill in EXPECTED_SKILLS if skills_found.get(skill, 0) == 0]

    print('Skill counts:', {skill: skills_found.get(skill, 0) for skill in EXPECTED_SKILLS})
    assert not missing, f"Missing question coverage for: {', '.join(missing)}"


def test_english_content():
    questions = load_all_questions()
    arabic_pattern = re.compile(r'[\u0600-\u06FF]')

    issues: list[str] = []
    for question in questions:
        if question.skill_id == 'verbal_analogy':
            continue

        text = f"{question.text_ar} {question.option_a} {question.option_b} {question.option_c} {question.option_d}"
        arabic_chars = arabic_pattern.findall(text)
        if arabic_chars:
            issues.append(
                f"Q{question.id} ({question.skill_id}) contains {len(arabic_chars)} Arabic characters"
            )

    assert not issues, '\n'.join(issues[:10])


def test_correct_options():
    questions = load_all_questions()
    errors = [
        f"Q{question.id}: invalid correct_option '{question.correct_option}'"
        for question in questions
        if question.correct_option not in {'a', 'b', 'c', 'd'}
    ]

    assert not errors, '\n'.join(errors[:10])


def test_difficulty_range():
    questions = load_all_questions()
    errors = [
        f"Q{question.id}: difficulty {question.difficulty} out of range [0.0, 1.0]"
        for question in questions
        if not (0.0 <= question.difficulty <= 1.0)
    ]

    assert not errors, '\n'.join(errors[:10])


if __name__ == "__main__":
    import pytest

    raise SystemExit(pytest.main([__file__, "-s"]))
