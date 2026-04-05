import os
import sys
from types import SimpleNamespace

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from practice_support import (
    build_practice_adaptive_payload,
    build_practice_assistment_payload,
    challenge_band_for_delta,
    difficulty_label_for_score,
    difficulty_score_from_value,
)


def test_difficulty_score_and_label_mapping_cover_all_bands():
    assert difficulty_score_from_value(0.0) == 0
    assert difficulty_score_from_value(0.52) == 52
    assert difficulty_score_from_value(1.0) == 100

    assert difficulty_label_for_score(12) == "Foundation"
    assert difficulty_label_for_score(32) == "Core"
    assert difficulty_label_for_score(52) == "Target"
    assert difficulty_label_for_score(72) == "Challenging"
    assert difficulty_label_for_score(92) == "Stretch"


def test_challenge_band_mapping_matches_theta_delta_rules():
    assert challenge_band_for_delta(-0.31) == "Reinforcement"
    assert challenge_band_for_delta(-0.10) == "At your level"
    assert challenge_band_for_delta(0.22) == "Stretch"
    assert challenge_band_for_delta(0.60) == "Challenge+"
    assert challenge_band_for_delta(None, calibrating=True) == "Calibrating"


def test_build_practice_adaptive_payload_uses_baseline_when_no_ability_record_exists():
    question = SimpleNamespace(skill_id="quant_geometry", difficulty=0.55)
    skill = SimpleNamespace(name_ar="Geometry", section="quant")

    payload = build_practice_adaptive_payload(question, skill, ability=None)

    assert payload["skill_name"] == "Geometry"
    assert payload["difficulty_score"] == 55
    assert payload["difficulty_label"] == "Target"
    assert payload["skill_mastery"] == 0
    assert payload["challenge_band"] == "Calibrating"
    assert "starting level" in payload["selection_reason"].lower()


def test_build_practice_adaptive_payload_generates_readable_band_reason():
    question = SimpleNamespace(skill_id="verbal_reading", difficulty=0.65)
    skill = SimpleNamespace(name_ar="Reading", section="verbal")
    ability = SimpleNamespace(theta=0.30, mastery=0.61, questions_seen=8)

    payload = build_practice_adaptive_payload(question, skill, ability)

    assert payload["skill_mastery"] == 61
    assert payload["challenge_band"] == "Stretch"
    assert payload["selection_reason"] == "Chosen as a stretch question in Reading."


def test_build_practice_assistment_payload_strips_giveaway_steps_and_adds_fallback():
    question = SimpleNamespace(
        skill_id="quant_arithmetic",
        question_type="arithmetic",
        solution_steps_ar='["Step 1: Identify the quantity being asked for", "Therefore option (b) is correct"]',
        explanation_ar="Half of 10 is 5.",
    )

    payload = build_practice_assistment_payload(question)

    assert payload["hints_available"] is True
    assert len(payload["hints"]) == 2
    assert payload["hints"][0]["title"] == "Hint 1: What to notice"
    assert "quantity being asked for" in payload["hints"][0]["text_ar"].lower()
    hint_text = " ".join(hint["text_ar"] for hint in payload["hints"]).lower()
    assert "option (b)" not in hint_text
    assert "correct answer" not in hint_text


def test_build_practice_assistment_payload_falls_back_when_steps_are_weak():
    question = SimpleNamespace(
        skill_id="verbal_reading",
        question_type="reading",
        solution_steps_ar='["Answer is (c)"]',
        explanation_ar="The passage supports choice C.",
    )

    payload = build_practice_assistment_payload(question)

    assert payload["hints_available"] is True
    assert len(payload["hints"]) == 2
    assert "passage" in payload["hints"][0]["text_ar"].lower()
