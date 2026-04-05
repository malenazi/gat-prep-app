import datetime
import random
from typing import Any

from sqlalchemy.orm import Session

from adaptive import generate_study_plan
from question_content import ensure_question_content_columns
from question_visuals import ensure_question_visual_columns
from models import Badge, Question, StudyPlan, User, UserBadge, UserResponse
from user_management import bootstrap_admin_user, create_user, purge_users_by_emails


def _seed_progressed_user(
    db: Session,
    user: User,
    *,
    ability_profile: dict[str, dict[str, float | int]],
    days_active: int,
    response_count: int,
    badge_ids: list[str],
) -> None:
    rng = random.Random(42)
    today = datetime.date.today().isoformat()
    all_questions = db.query(Question).all()

    for ability in user.abilities:
        profile = ability_profile.get(ability.skill_id, {})
        ability.theta = float(profile.get("theta", 0.0))
        ability.mastery = float(profile.get("mastery", 0.3))
        ability.questions_seen = int(profile.get("seen", 0))
        ability.correct_count = int(profile.get("correct", 0))

    available_questions = list(all_questions)
    rng.shuffle(available_questions)
    for index in range(min(response_count, len(available_questions))):
        question = available_questions[index]
        mastery = float(ability_profile.get(question.skill_id, {}).get("mastery", 0.4))
        is_correct = rng.random() < mastery
        options = ["a", "b", "c", "d"]
        if is_correct:
            selected_option = question.correct_option
        else:
            selected_option = rng.choice([option for option in options if option != question.correct_option])

        response = UserResponse(
            user_id=user.id,
            question_id=question.id,
            session_type="drill",
            selected_option=selected_option,
            is_correct=is_correct,
            time_spent_seconds=rng.randint(15, 80),
        )
        response.created_at = datetime.datetime.utcnow() - datetime.timedelta(days=rng.randint(0, max(1, days_active - 1)))
        db.add(response)

    user.xp = 420
    user.streak_current = days_active
    user.streak_longest = days_active
    user.league = "silver"
    user.last_active_date = today

    generate_study_plan(db, user.id, user.daily_minutes)
    plan_days = db.query(StudyPlan).filter_by(user_id=user.id).order_by(StudyPlan.day_number).all()
    for plan in plan_days:
        if plan.day_number < user.current_day:
            plan.completed = True
            plan.completed_questions = plan.target_questions

    for badge_id in badge_ids:
        if db.query(Badge).filter_by(id=badge_id).first():
            db.add(UserBadge(user_id=user.id, badge_id=badge_id))

    db.commit()


def bootstrap_sample_users(
    db: Session,
    *,
    new_student: dict[str, Any] | None = None,
    progressed: dict[str, Any] | None = None,
    admin: dict[str, Any] | None = None,
) -> None:
    ensure_question_visual_columns(db.get_bind())
    ensure_question_content_columns(db.get_bind())
    target_emails = [
        account["email"]
        for account in (new_student, progressed, admin)
        if account and account.get("email")
    ]
    if target_emails:
        purge_users_by_emails(db, target_emails)

    if new_student:
        create_user(
            db,
            name=new_student["name"],
            email=new_student["email"],
            password=new_student["password"],
            diagnostic_completed=False,
            current_day=0,
        )

    if progressed:
        progressed_user = create_user(
            db,
            name=progressed["name"],
            email=progressed["email"],
            password=progressed["password"],
            diagnostic_completed=True,
            current_day=5,
            daily_minutes=60,
        )
        _seed_progressed_user(
            db,
            progressed_user,
            ability_profile={
                "verbal_reading": {"theta": 0.3, "mastery": 0.55, "seen": 8, "correct": 4},
                "verbal_analogy": {"theta": -0.2, "mastery": 0.40, "seen": 6, "correct": 2},
                "verbal_completion": {"theta": 0.1, "mastery": 0.50, "seen": 5, "correct": 2},
                "verbal_error": {"theta": -0.1, "mastery": 0.33, "seen": 4, "correct": 1},
                "verbal_oddword": {"theta": 0.0, "mastery": 0.50, "seen": 2, "correct": 1},
                "quant_arithmetic": {"theta": 0.5, "mastery": 0.60, "seen": 10, "correct": 6},
                "quant_geometry": {"theta": -0.3, "mastery": 0.30, "seen": 5, "correct": 1},
                "quant_algebra": {"theta": 0.2, "mastery": 0.45, "seen": 6, "correct": 3},
                "quant_statistics": {"theta": 0.0, "mastery": 0.40, "seen": 4, "correct": 2},
            },
            days_active=5,
            response_count=50,
            badge_ids=["first_step"],
        )

    if admin:
        bootstrap_admin_user(
            db,
            name=admin["name"],
            email=admin["email"],
            password=admin["password"],
        )
