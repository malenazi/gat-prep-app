"""Question bank quality validation tests.

Catches duplicate options, empty fields, invalid data, and SVG dark mode issues.
"""
import re
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from questions import load_all_questions


def _all_questions():
    return load_all_questions()


def test_no_duplicate_options():
    """Every question must have 4 unique options."""
    dupes = []
    for q in _all_questions():
        opts = [q.option_a, q.option_b, q.option_c, q.option_d]
        if len(set(opts)) < 4:
            repeated = [o for o in set(opts) if opts.count(o) > 1]
            dupes.append(f"{q.source_key}: duplicate option(s) {repeated}")
    assert dupes == [], f"Questions with duplicate options:\n" + "\n".join(dupes)


def test_no_empty_options():
    """Every question must have non-empty options."""
    empty = []
    for q in _all_questions():
        for letter in ('a', 'b', 'c', 'd'):
            val = getattr(q, f'option_{letter}', '')
            if not val or len(val.strip()) == 0:
                empty.append(f"{q.source_key}: empty option_{letter}")
    assert empty == [], f"Questions with empty options:\n" + "\n".join(empty)


def test_correct_option_valid():
    """correct_option must be a, b, c, or d."""
    invalid = []
    for q in _all_questions():
        if q.correct_option not in ('a', 'b', 'c', 'd'):
            invalid.append(f"{q.source_key}: correct_option='{q.correct_option}'")
    assert invalid == [], f"Invalid correct_option:\n" + "\n".join(invalid)


def test_difficulty_in_range():
    """Difficulty must be between 0.0 and 1.0."""
    out_of_range = []
    for q in _all_questions():
        if q.difficulty < 0 or q.difficulty > 1:
            out_of_range.append(f"{q.source_key}: difficulty={q.difficulty}")
    assert out_of_range == [], f"Difficulty out of range:\n" + "\n".join(out_of_range)


def test_explanations_not_empty():
    """Every question should have a meaningful explanation."""
    short = []
    for q in _all_questions():
        if not q.explanation_ar or len(q.explanation_ar) < 15:
            short.append(f"{q.source_key}: explanation too short ({len(q.explanation_ar or '')} chars)")
    assert short == [], f"Questions with short/missing explanations:\n" + "\n".join(short)


def test_no_problematic_svg_fills():
    """SVG figures should not have hardcoded light-only fills."""
    BAD_FILLS = ['#FFF8E1', '#FFFDE7', '#FFF9C4', '#FFEEBA']
    issues = []
    for q in _all_questions():
        if not q.figure_svg:
            continue
        svg_lower = q.figure_svg.lower()
        for fill in BAD_FILLS:
            if fill.lower() in svg_lower:
                issues.append(f"{q.source_key}: SVG has hardcoded fill {fill}")
    assert issues == [], f"SVG dark mode issues:\n" + "\n".join(issues)


def test_question_text_not_empty():
    """Question text must be at least 5 characters (analogies can be short like 'Sun : Day')."""
    empty = []
    for q in _all_questions():
        if not q.text_ar or len(q.text_ar.strip()) < 5:
            empty.append(f"{q.source_key}: text too short ({len(q.text_ar or '')} chars): '{q.text_ar}'")
    assert empty == [], f"Questions with short text:\n" + "\n".join(empty)
