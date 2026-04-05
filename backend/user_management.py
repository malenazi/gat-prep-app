from typing import Iterable

from sqlalchemy import func
from sqlalchemy.orm import Session

from auth_utils import (
    hash_password,
    normalize_email,
    validate_admin_password,
    validate_user_password,
)
from models import (
    Feedback,
    MockAttempt,
    PasswordResetToken,
    Skill,
    StudyPlan,
    User,
    UserAbility,
    UserBadge,
    UserResponse,
)

LEGACY_DEMO_EMAILS = (
    "student@gat.sa",
    "sara@gat.sa",
    "mohammed@gat.sa",
    "lujain@gat.sa",
    "admin@gat.sa",
)


def find_user_by_email(db: Session, email: str) -> User | None:
    normalized_email = normalize_email(email)
    return (
        db.query(User)
        .filter(func.lower(User.email) == normalized_email)
        .first()
    )


def ensure_user_abilities(db: Session, user_id: int) -> None:
    existing_skill_ids = {
        ability.skill_id
        for ability in db.query(UserAbility).filter_by(user_id=user_id).all()
    }
    for skill in db.query(Skill).all():
        if skill.id in existing_skill_ids:
            continue
        db.add(
            UserAbility(
                user_id=user_id,
                skill_id=skill.id,
                theta=0.0,
                mastery=0.3,
                questions_seen=0,
                correct_count=0,
            )
        )
    db.flush()


def create_user(
    db: Session,
    *,
    name: str,
    email: str,
    password: str,
    is_admin: bool = False,
    diagnostic_completed: bool = False,
    current_day: int = 0,
    daily_minutes: int = 120,
) -> User:
    cleaned_name = name.strip()
    normalized_email = normalize_email(email)
    if not cleaned_name:
        raise ValueError("Name is required")
    if find_user_by_email(db, normalized_email):
        raise ValueError("Email already registered")

    if is_admin:
        validate_admin_password(password)
    else:
        validate_user_password(password)

    user = User(
        name=cleaned_name,
        email=normalized_email,
        password_hash=hash_password(password),
        is_admin=is_admin,
        diagnostic_completed=diagnostic_completed,
        current_day=current_day,
        daily_minutes=daily_minutes,
    )
    db.add(user)
    db.flush()
    ensure_user_abilities(db, user.id)
    db.commit()
    db.refresh(user)
    return user


def bootstrap_admin_user(db: Session, *, name: str, email: str, password: str) -> User:
    if find_user_by_email(db, email):
        raise ValueError("Admin user already exists")
    return create_user(
        db,
        name=name,
        email=email,
        password=password,
        is_admin=True,
        diagnostic_completed=True,
        current_day=1,
    )


def purge_users_by_emails(db: Session, emails: Iterable[str]) -> int:
    normalized_emails = [normalize_email(email) for email in emails]
    users = db.query(User).filter(func.lower(User.email).in_(normalized_emails)).all()
    if not users:
        return 0

    user_ids = [user.id for user in users]
    db.query(UserResponse).filter(UserResponse.user_id.in_(user_ids)).delete(synchronize_session=False)
    db.query(MockAttempt).filter(MockAttempt.user_id.in_(user_ids)).delete(synchronize_session=False)
    db.query(UserAbility).filter(UserAbility.user_id.in_(user_ids)).delete(synchronize_session=False)
    db.query(UserBadge).filter(UserBadge.user_id.in_(user_ids)).delete(synchronize_session=False)
    db.query(StudyPlan).filter(StudyPlan.user_id.in_(user_ids)).delete(synchronize_session=False)
    db.query(Feedback).filter(Feedback.user_id.in_(user_ids)).delete(synchronize_session=False)
    db.query(PasswordResetToken).filter(PasswordResetToken.user_id.in_(user_ids)).delete(synchronize_session=False)
    db.query(User).filter(User.id.in_(user_ids)).delete(synchronize_session=False)
    db.commit()
    return len(user_ids)
