"""
Visual question validation and schema compatibility tests.
"""

import os
import sys

import pytest
from sqlalchemy import create_engine, inspect, text

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from question_visuals import (
    deserialize_table_payload,
    ensure_question_visual_columns,
    serialize_table_payload,
    validate_svg_markup,
)
from questions import load_all_questions


def test_validate_svg_accepts_basic_shapes():
    svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10"><rect x="1" y="1" width="8" height="8" fill="#fff" stroke="#000" stroke-width="1"/></svg>'
    assert validate_svg_markup(svg) == svg


def test_validate_svg_rejects_scripts():
    svg = '<svg xmlns="http://www.w3.org/2000/svg"><script>alert(1)</script></svg>'
    with pytest.raises(ValueError):
        validate_svg_markup(svg)


def test_table_payload_round_trip():
    payload = {
        "headers": ["Column", "Value"],
        "rows": [["A", "12"], ["B", "18"]],
    }
    serialized = serialize_table_payload(payload)
    assert deserialize_table_payload(serialized) == payload


def test_ensure_question_visual_columns_adds_missing_columns(tmp_path):
    db_path = tmp_path / "visuals.db"
    engine = create_engine(f"sqlite:///{db_path}")

    with engine.begin() as connection:
        connection.execute(
            text(
                """
                CREATE TABLE questions (
                    id INTEGER PRIMARY KEY,
                    skill_id TEXT NOT NULL,
                    question_type TEXT NOT NULL,
                    difficulty FLOAT DEFAULT 0.5,
                    text_ar TEXT NOT NULL,
                    passage_ar TEXT
                )
                """
            )
        )

    ensure_question_visual_columns(engine)
    columns = {column["name"] for column in inspect(engine).get_columns("questions")}

    assert "figure_svg" in columns
    assert "table_ar" in columns


def test_visual_refresh_adds_expected_question_support():
    questions = load_all_questions()

    visual_questions = [question for question in questions if question.figure_svg or question.table_ar]
    assert len(visual_questions) >= 36
    assert sum(1 for question in questions if question.skill_id == "quant_geometry" and question.figure_svg) >= 16
    assert sum(1 for question in questions if question.skill_id == "quant_statistics" and question.table_ar) >= 11
    assert sum(1 for question in questions if question.skill_id == "quant_arithmetic" and question.table_ar) >= 9
