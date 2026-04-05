import os
import sys
from types import SimpleNamespace

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from question_content import (
    activation_blockers,
    classify_question_content,
    collect_question_quality_metadata,
    collect_question_content_issues,
    extract_comparison_columns,
    ratings_complete,
    normalize_math_markdown,
)


def test_normalize_math_markdown_converts_legacy_quant_syntax():
    normalized = normalize_math_markdown("What is 1/2 of sqrt(49) + x^2 +/- pi?")
    assert normalized == r"What is $\frac{1}{2}$ of $\sqrt{49}$ + $x^{2}$ $\pm$ $\pi$?"


def test_extract_comparison_columns_keeps_intro_and_panels():
    text, columns = extract_comparison_columns(
        "Compare the values.\nColumn (A): 25% of 200\nColumn (B): 50% of 100"
    )
    assert text == "Compare the values."
    assert columns == {"a": "25% of 200", "b": "50% of 100"}


def test_collect_question_content_issues_flags_missing_alt_and_legacy_math():
    question = SimpleNamespace(
        skill_id="quant_arithmetic",
        question_type="arithmetic",
        text_ar="Solve 1/2 + 3/4",
        passage_ar=None,
        option_a="1",
        option_b="2",
        option_c="3",
        option_d="4",
        explanation_ar="Use sqrt(25).",
        solution_steps_ar='["x^2 becomes 4"]',
        figure_svg="<svg></svg>",
        figure_alt=None,
    )
    issues = collect_question_content_issues(question)
    codes = {issue.code for issue in issues}
    assert "legacy_math_syntax" in codes
    assert "missing_figure_alt" in codes
    assert classify_question_content(question) == "content-corrupted"


def test_collect_question_content_issues_flags_duplicate_options_and_missing_quant_supporting_content():
    question = SimpleNamespace(
        skill_id="quant_statistics",
        question_type="statistics",
        content_format="markdown_math",
        text_ar="What is the probability?",
        passage_ar=None,
        option_a="$\\frac{1}{2}$",
        option_b="$\\frac{1}{2}$",
        option_c="...",
        option_d="$\\frac{3}{4}$",
        correct_option="a",
        explanation_ar=None,
        solution_steps_ar=None,
        figure_svg=None,
        figure_alt=None,
        table_ar=None,
        table_caption=None,
        comparison_columns=None,
    )

    issues = collect_question_content_issues(question)
    codes = {issue.code for issue in issues}
    assert "duplicate_options" in codes
    assert "placeholder_distractor" in codes
    assert "missing_explanation" in codes
    assert "missing_solution_steps" in codes
    assert classify_question_content(question, issues) == "needs-manual-cleanup"


def test_collect_question_quality_metadata_tracks_review_completion():
    question = SimpleNamespace(
        skill_id="verbal_reading",
        question_type="reading",
        source_key="verbal_reading:0001",
        content_format="plain",
        text_ar="Read the passage.",
        passage_ar=None,
        option_a="A",
        option_b="B",
        option_c="C",
        option_d="D",
        correct_option="a",
        explanation_ar="Because the first choice matches the passage.",
        solution_steps_ar=None,
        figure_svg=None,
        figure_alt=None,
        table_ar=None,
        table_caption=None,
        comparison_columns=None,
        rating_clarity=5,
        rating_cognitive=4,
        rating_distractors=4,
        rating_difficulty_align=4,
        rating_explanation=5,
        rating_fairness=5,
        rating_discrimination=4,
    )

    metadata = collect_question_quality_metadata(question)
    assert metadata["source_key"] == "verbal_reading:0001"
    assert metadata["content_classification"] == "ready"
    assert metadata["recommended_action"] == "keep-active"
    assert metadata["ratings_complete"] is True
    assert ratings_complete(question) is True


def test_activation_blockers_require_ratings_and_review_pass_for_active_content():
    question = SimpleNamespace(
        skill_id="quant_arithmetic",
        question_type="arithmetic",
        content_format="markdown_math",
        text_ar="What is $\\frac{1}{2}$ of 10?",
        passage_ar=None,
        option_a="3",
        option_b="5",
        option_c="7",
        option_d="10",
        correct_option="b",
        explanation_ar="Half of 10 is 5.",
        solution_steps_ar='["Take half of 10.", "5 is the result."]',
        figure_svg=None,
        figure_alt=None,
        table_ar=None,
        table_caption=None,
        comparison_columns=None,
        rating_clarity=5,
        rating_cognitive=4,
        rating_distractors=4,
        rating_difficulty_align=4,
        rating_explanation=5,
        rating_fairness=5,
        rating_discrimination=4,
        rating_passes_done=0,
    )

    blockers = activation_blockers(question)
    assert any("review pass" in blocker.lower() for blocker in blockers)


def test_activation_blockers_allow_ai_generated_questions_without_manual_review_fields():
    question = SimpleNamespace(
        skill_id="quant_algebra",
        question_type="algebra",
        authoring_source="ai_generated",
        content_format="markdown_math",
        text_ar="Solve $x + 4 = 9$.",
        passage_ar=None,
        option_a="3",
        option_b="4",
        option_c="5",
        option_d="6",
        correct_option="c",
        explanation_ar="Subtract 4 from both sides to isolate $x$.",
        solution_steps_ar=["Subtract 4 from both sides.", "$x = 5$."],
        figure_svg=None,
        figure_alt=None,
        table_ar=None,
        table_caption=None,
        comparison_columns=None,
        rating_passes_done=0,
    )

    blockers = activation_blockers(question)
    assert blockers == []
