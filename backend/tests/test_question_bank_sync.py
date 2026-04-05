import os
import sys
from types import SimpleNamespace

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database import Base
from models import Question
from question_content import ensure_question_content_columns
import sync_question_bank as sync_module


def build_source_question(*, source_key: str, text_ar: str, difficulty: float = 0.4):
    return SimpleNamespace(
        source_key=source_key,
        batch_id="quant-arithmetic-ai-batch-001",
        generation_prompt_version="ai-question-wave1-v1",
        authoring_source="ai_generated",
        variant_group="percent-change-a",
        skill_id="quant_arithmetic",
        question_type="arithmetic",
        difficulty=difficulty,
        text_ar=text_ar,
        passage_ar=None,
        content_format="markdown_math",
        figure_svg=None,
        figure_alt=None,
        table_ar=None,
        table_caption=None,
        comparison_columns=None,
        option_a="1",
        option_b="2",
        option_c="3",
        option_d="4",
        correct_option="b",
        explanation_ar="Add the values carefully.",
        solution_steps_ar='["Step 1", "Step 2"]',
        tags="arithmetic",
        paper_only=False,
        stage="foundation",
        status="active",
    )


def test_sync_question_bank_preserves_identity_and_analytics(monkeypatch):
    engine = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False})
    TestingSession = sessionmaker(bind=engine)
    Base.metadata.create_all(bind=engine)
    ensure_question_content_columns(engine)

    session = TestingSession()
    try:
        existing = Question(
            skill_id="quant_arithmetic",
            question_type="arithmetic",
            difficulty=0.9,
            text_ar="Legacy text",
            content_format="plain",
            option_a="1",
            option_b="2",
            option_c="3",
            option_d="4",
            correct_option="b",
            explanation_ar="Old explanation",
            solution_steps_ar='["Old"]',
            stage="foundation",
            status="active",
        )
        existing.times_answered = 12
        existing.times_correct = 9
        existing.avg_time_seconds = 41.5
        existing.discrimination = 0.35
        existing.rating_clarity = 5
        existing.rating_cognitive = 4
        existing.rating_distractors = 4
        existing.rating_difficulty_align = 4
        existing.rating_explanation = 5
        existing.rating_fairness = 5
        existing.rating_discrimination = 4
        existing.rating_passes_done = 2
        existing.rating_notes = "Reviewed manually."
        session.add(existing)
        session.commit()

        monkeypatch.setattr(
            sync_module,
            "load_all_questions",
            lambda: [build_source_question(source_key="quant_arithmetic:0001", text_ar="Updated source text")],
        )

        report = sync_module.sync_question_bank(session)
        synced = session.query(Question).one()

        assert report["created"] == 0
        assert synced.id == existing.id
        assert synced.source_key == "quant_arithmetic:0001"
        assert synced.batch_id == "quant-arithmetic-ai-batch-001"
        assert synced.generation_prompt_version == "ai-question-wave1-v1"
        assert synced.authoring_source == "ai_generated"
        assert synced.variant_group == "percent-change-a"
        assert synced.text_ar == "Updated source text"
        assert synced.times_answered == 12
        assert synced.times_correct == 9
        assert synced.avg_time_seconds == 41.5
        assert synced.discrimination == 0.35
        assert synced.rating_notes == "Reviewed manually."
        assert synced.rating_passes_done == 2
        assert synced.difficulty == 0.9
    finally:
        session.close()
