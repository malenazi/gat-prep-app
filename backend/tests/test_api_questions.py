"""
Question API endpoint tests.
"""

import datetime
import os
import sys
from uuid import uuid4

import requests

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
default_test_db = os.path.join(backend_dir, "gat_prep.e2e.db").replace(os.sep, "/")
os.environ.setdefault("DATABASE_URL", f"sqlite:///{default_test_db}")

from adaptive import generate_study_plan
from database import SessionLocal
from models import StudyPlan, User
from test_support import bootstrap_sample_users

BASE_URL = os.getenv("API_BASE_URL", "http://127.0.0.1:8000/api")

API_TEST_USERS = {
    "new_student": {
        "name": "API New Learner",
        "email": f"api-new-{uuid4()}@example.com",
        "password": f"NewLearner!{uuid4().hex}9a",
    },
    "progress": {
        "name": "API Progress Learner",
        "email": f"api-progress-{uuid4()}@example.com",
        "password": f"ProgressLearner!{uuid4().hex}9a",
    },
    "admin": {
        "name": "API Admin",
        "email": f"api-admin-{uuid4()}@example.com",
        "password": f"AdminBootstrap!{uuid4().hex}9Aa#",
    },
}


def ensure_runtime_users() -> None:
    db = SessionLocal()
    try:
        bootstrap_sample_users(
            db,
            new_student=API_TEST_USERS["new_student"],
            progressed=API_TEST_USERS["progress"],
            admin=API_TEST_USERS["admin"],
        )
    finally:
        db.close()


ensure_runtime_users()


def login_user(email: str, password: str) -> str:
    response = requests.post(
        f"{BASE_URL}/auth/login",
        json={"email": email, "password": password},
        timeout=10,
    )
    assert response.status_code == 200, response.text
    return response.json()["token"]


def set_user_course_day(email: str, day: int, *, complete_current_day: bool = False) -> None:
    db = SessionLocal()
    try:
        user = db.query(User).filter_by(email=email).first()
        assert user is not None
        user.diagnostic_completed = True
        user.current_day = day
        user.daily_minutes = 120
        user.course_started_at = user.course_started_at or datetime.datetime.utcnow()
        user.mock_attempts = 0
        user.mock_score = 0
        db.commit()

        generate_study_plan(db, user.id, user.daily_minutes)

        for plan in db.query(StudyPlan).filter_by(user_id=user.id).all():
            if plan.day_number < day or (complete_current_day and plan.day_number == day):
                plan.completed = True
                plan.completed_questions = plan.target_questions
            else:
                plan.completed = False
                plan.completed_questions = 0

        db.commit()
    finally:
        db.close()


def test_skills_endpoint():
    response = requests.get(f"{BASE_URL}/skills", timeout=10)
    assert response.status_code == 200, response.text

    skills = response.json()
    print(f"Returned {len(skills)} skills")
    assert len(skills) >= 9

    for skill in skills[:3]:
        assert skill["id"]
        assert skill.get("name_ar")


def test_practice_next_endpoint():
    token = login_user(API_TEST_USERS["progress"]["email"], API_TEST_USERS["progress"]["password"])
    response = requests.get(
        f"{BASE_URL}/practice/next",
        headers={"Authorization": f"Bearer {token}"},
        timeout=10,
    )
    assert response.status_code == 200, response.text

    data = response.json()
    question = data.get("question")
    assert question, data
    assert question["id"]
    assert question["skill_id"]
    assert question["question_type"]
    assert question["text_ar"]
    assert "figure_svg" in question
    assert "table_ar" in question
    assert data["adaptive"]["skill_name"]
    assert isinstance(data["adaptive"]["difficulty_score"], int)
    assert data["adaptive"]["difficulty_label"]
    assert data["adaptive"]["challenge_band"]
    assert data["adaptive"]["selection_reason"]
    assert "hints_available" in data["assistment"]
    assert len(data["assistment"]["hints"]) <= 2


def test_practice_next_avoids_questions_answered_today():
    token = login_user(API_TEST_USERS["progress"]["email"], API_TEST_USERS["progress"]["password"])
    headers = {"Authorization": f"Bearer {token}"}

    first_response = requests.get(f"{BASE_URL}/practice/next", headers=headers, timeout=10)
    assert first_response.status_code == 200, first_response.text
    first_question = first_response.json()["question"]

    answer_response = requests.post(
        f"{BASE_URL}/practice/answer",
        headers=headers,
        json={
            "question_id": first_question["id"],
            "selected_option": "a",
            "time_spent_seconds": 15,
        },
        timeout=10,
    )
    assert answer_response.status_code == 200, answer_response.text

    second_response = requests.get(f"{BASE_URL}/practice/next", headers=headers, timeout=10)
    assert second_response.status_code == 200, second_response.text
    second_question = second_response.json()["question"]

    assert second_question["id"] != first_question["id"]


def test_practice_answer_endpoint():
    token = login_user(API_TEST_USERS["progress"]["email"], API_TEST_USERS["progress"]["password"])
    headers = {"Authorization": f"Bearer {token}"}

    next_response = requests.get(f"{BASE_URL}/practice/next", headers=headers, timeout=10)
    assert next_response.status_code == 200, next_response.text
    question = next_response.json()["question"]

    answer_response = requests.post(
        f"{BASE_URL}/practice/answer",
        headers=headers,
        json={
            "question_id": question["id"],
            "selected_option": "a",
            "time_spent_seconds": 30,
        },
        timeout=10,
    )
    assert answer_response.status_code == 200, answer_response.text

    result = answer_response.json()
    assert "is_correct" in result
    assert "xp_earned" in result


def test_diagnostic_endpoints():
    token = login_user(API_TEST_USERS["new_student"]["email"], API_TEST_USERS["new_student"]["password"])
    headers = {"Authorization": f"Bearer {token}"}

    start_response = requests.post(f"{BASE_URL}/diagnostic/start", headers=headers, timeout=10)
    assert start_response.status_code == 200, start_response.text

    next_response = requests.get(f"{BASE_URL}/diagnostic/next", headers=headers, timeout=10)
    assert next_response.status_code == 200, next_response.text

    data = next_response.json()
    assert not data.get("done"), data
    question = data.get("question")
    assert question, data
    assert question["id"]
    assert question["skill_id"]
    assert isinstance(data.get("progress"), int)


def test_register_normalizes_email_and_rejects_case_insensitive_duplicates():
    email = f"Register-{uuid4()}@Example.com"
    password = f"LearnerPass!{uuid4().hex[:12]}9a"
    headers = {"x-forwarded-for": f"203.0.113.{uuid4().int % 200 + 20}"}

    first_response = requests.post(
        f"{BASE_URL}/auth/register",
        headers=headers,
        json={
            "name": "Case Test Learner",
            "email": email,
            "password": password,
        },
        timeout=10,
    )
    assert first_response.status_code == 200, first_response.text

    duplicate_response = requests.post(
        f"{BASE_URL}/auth/register",
        headers=headers,
        json={
            "name": "Duplicate Learner",
            "email": email.upper(),
            "password": password,
        },
        timeout=10,
    )
    assert duplicate_response.status_code == 400, duplicate_response.text
    assert "Email already registered" in duplicate_response.text

    login_response = requests.post(
        f"{BASE_URL}/auth/login",
        json={"email": email.lower(), "password": password},
        timeout=10,
    )
    assert login_response.status_code == 200, login_response.text


def test_admin_question_visual_crud_validation():
    token = login_user(API_TEST_USERS["admin"]["email"], API_TEST_USERS["admin"]["password"])
    headers = {"Authorization": f"Bearer {token}"}
    payload = {
        "skill_id": "quant_geometry",
        "question_type": "geometry",
        "difficulty": 0.4,
        "text_ar": "Test visual geometry question",
        "passage_ar": None,
        "content_format": "plain",
        "figure_svg": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10"><rect x="1" y="1" width="8" height="8" fill="#fff" stroke="#000" stroke-width="1"/></svg>',
        "figure_alt": "Rectangle diagram with labeled sides.",
        "table_ar": None,
        "option_a": "8",
        "option_b": "10",
        "option_c": "12",
        "option_d": "14",
        "correct_option": "b",
        "explanation_ar": "A rectangle with sides 8 and 2 has perimeter 20.",
        "solution_steps_ar": '["Add the two sides.", "Double the sum."]',
        "status": "review",
    }

    create_response = requests.post(
        f"{BASE_URL}/admin/questions",
        headers=headers,
        json=payload,
        timeout=10,
    )
    assert create_response.status_code == 200, create_response.text
    created_id = create_response.json()["id"]

    invalid_update = requests.put(
        f"{BASE_URL}/admin/questions/{created_id}",
        headers=headers,
        json={
            **payload,
            "figure_svg": "<svg><script>alert(1)</script></svg>",
            "table_ar": {"headers": ["A", "B"], "rows": [["1"]]},
        },
        timeout=10,
    )
    assert invalid_update.status_code == 400, invalid_update.text

    questions_response = requests.get(
        f"{BASE_URL}/admin/questions",
        headers=headers,
        timeout=10,
    )
    assert questions_response.status_code == 200, questions_response.text
    created_question = next(q for q in questions_response.json() if q["id"] == created_id)
    assert created_question["figure_svg"]
    assert created_question["table_ar"] is None
    assert created_question["source_key"].startswith("admin:")
    assert created_question["content_classification"]
    assert created_question["recommended_action"]

    delete_response = requests.delete(
        f"{BASE_URL}/admin/questions/{created_id}",
        headers=headers,
        timeout=10,
    )
    assert delete_response.status_code == 200, delete_response.text


def test_question_types():
    token = login_user(API_TEST_USERS["progress"]["email"], API_TEST_USERS["progress"]["password"])
    headers = {"Authorization": f"Bearer {token}"}
    skill_ids: set[str] = set()

    for _ in range(10):
        next_response = requests.get(f"{BASE_URL}/practice/next", headers=headers, timeout=10)
        assert next_response.status_code == 200, next_response.text
        question = next_response.json().get("question")
        assert question, next_response.json()

        skill_ids.add(question["skill_id"])

        answer_response = requests.post(
            f"{BASE_URL}/practice/answer",
            headers=headers,
            json={
                "question_id": question["id"],
                "selected_option": "a",
                "time_spent_seconds": 10,
            },
            timeout=10,
        )
        assert answer_response.status_code == 200, answer_response.text

    print("Found skills:", sorted(skill_ids))
    assert len(skill_ids) >= 2


def test_admin_active_question_requires_review_metadata():
    token = login_user(API_TEST_USERS["admin"]["email"], API_TEST_USERS["admin"]["password"])
    headers = {"Authorization": f"Bearer {token}"}
    payload = {
        "skill_id": "quant_arithmetic",
        "question_type": "arithmetic",
        "difficulty": 0.3,
        "text_ar": "What is $\\frac{1}{2}$ of 10?",
        "content_format": "markdown_math",
        "option_a": "3",
        "option_b": "5",
        "option_c": "7",
        "option_d": "10",
        "correct_option": "b",
        "explanation_ar": "Half of 10 is 5.",
        "solution_steps_ar": '["Take half of 10.", "5 is the result."]',
        "status": "active",
    }

    response = requests.post(
        f"{BASE_URL}/admin/questions",
        headers=headers,
        json=payload,
        timeout=10,
    )
    assert response.status_code == 400, response.text
    assert "review ratings" in response.text.lower() or "review pass" in response.text.lower()


def test_admin_question_analysis_includes_content_metadata():
    token = login_user(API_TEST_USERS["admin"]["email"], API_TEST_USERS["admin"]["password"])
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(
        f"{BASE_URL}/admin/questions/analysis",
        headers=headers,
        timeout=10,
    )
    assert response.status_code == 200, response.text
    analysis = response.json()
    assert "by_classification" in analysis
    assert "by_recommended_action" in analysis
    assert analysis["flagged"]
    first_flagged = analysis["flagged"][0]
    assert "content_classification" in first_flagged
    assert "recommended_action" in first_flagged
    assert "ratings_complete" in first_flagged


def test_scheduled_mock_day_unlocks_before_day_25_and_completes_the_day():
    set_user_course_day(API_TEST_USERS["new_student"]["email"], 11)
    token = login_user(API_TEST_USERS["new_student"]["email"], API_TEST_USERS["new_student"]["password"])
    headers = {"Authorization": f"Bearer {token}"}

    practice_response = requests.get(f"{BASE_URL}/practice/next", headers=headers, timeout=10)
    assert practice_response.status_code == 400, practice_response.text
    assert "mock exam" in practice_response.text.lower()

    start_response = requests.post(f"{BASE_URL}/mock/start", headers=headers, timeout=10)
    assert start_response.status_code == 200, start_response.text
    start = start_response.json()
    assert start["question_ids"]

    for question_id in start["question_ids"]:
        answer_response = requests.post(
            f"{BASE_URL}/mock/answer",
            headers=headers,
            json={
                "question_id": question_id,
                "selected_option": "a",
                "time_spent_seconds": 1,
                "attempt_id": start["attempt_id"],
            },
            timeout=10,
        )
        assert answer_response.status_code == 200, answer_response.text

    complete_response = requests.post(
        f"{BASE_URL}/mock/complete",
        headers=headers,
        json={"attempt_id": start["attempt_id"]},
        timeout=10,
    )
    assert complete_response.status_code == 200, complete_response.text

    today_response = requests.get(f"{BASE_URL}/study-plan/today", headers=headers, timeout=10)
    assert today_response.status_code == 200, today_response.text
    today = today_response.json()
    assert today["day"] == 11
    assert today["is_mock_day"] is True
    assert today["completed_questions"] == today["target_questions"]
    assert today["remaining"] == 0

    advance_response = requests.post(f"{BASE_URL}/advance-day", headers=headers, timeout=10)
    assert advance_response.status_code == 200, advance_response.text
    assert advance_response.json()["current_day"] == 12


def test_advancing_to_day_30_auto_completes_rest_day():
    set_user_course_day(API_TEST_USERS["new_student"]["email"], 29, complete_current_day=True)
    token = login_user(API_TEST_USERS["new_student"]["email"], API_TEST_USERS["new_student"]["password"])
    headers = {"Authorization": f"Bearer {token}"}

    advance_response = requests.post(f"{BASE_URL}/advance-day", headers=headers, timeout=10)
    assert advance_response.status_code == 200, advance_response.text
    assert advance_response.json()["current_day"] == 30

    today_response = requests.get(f"{BASE_URL}/study-plan/today", headers=headers, timeout=10)
    assert today_response.status_code == 200, today_response.text
    today = today_response.json()
    assert today["is_rest_day"] is True
    assert today["completed_questions"] == today["target_questions"]
    assert today["remaining"] == 0

    plan_response = requests.get(f"{BASE_URL}/study-plan", headers=headers, timeout=10)
    assert plan_response.status_code == 200, plan_response.text
    plan = plan_response.json()
    assert len(plan) == 30
    assert sum(1 for day in plan if day["completed"]) == 30


if __name__ == "__main__":
    import pytest

    raise SystemExit(pytest.main([__file__, "-s"]))
