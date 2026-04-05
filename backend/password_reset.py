import datetime
import hashlib
import os
import secrets
from typing import Optional

from sqlalchemy.orm import Session

from auth_utils import hash_password, is_production_env, normalize_email, validate_user_password
from models import PasswordResetToken, User
from user_management import find_user_by_email

DEFAULT_PASSWORD_RESET_TTL_MINUTES = 30
PASSWORD_RESET_PREVIEW_ENV = "PASSWORD_RESET_PREVIEW"
PASSWORD_RESET_SUPPORT_EMAIL_ENV = "SUPPORT_EMAIL"


def get_password_reset_ttl_minutes() -> int:
    raw_value = os.getenv("PASSWORD_RESET_TTL_MINUTES", str(DEFAULT_PASSWORD_RESET_TTL_MINUTES)).strip()
    try:
        return max(5, int(raw_value))
    except ValueError:
        return DEFAULT_PASSWORD_RESET_TTL_MINUTES


def password_reset_preview_enabled() -> bool:
    raw_value = os.getenv(PASSWORD_RESET_PREVIEW_ENV, "").strip().lower()
    if raw_value in {"1", "true", "yes", "on"}:
        return True
    if raw_value in {"0", "false", "no", "off"}:
        return False
    return not is_production_env()


def get_password_reset_support_email() -> Optional[str]:
    support_email = os.getenv(PASSWORD_RESET_SUPPORT_EMAIL_ENV, "").strip()
    return support_email or None


def hash_password_reset_token(token: str) -> str:
    return hashlib.sha256(token.encode("utf-8")).hexdigest()


def issue_password_reset_token(db: Session, user: User) -> str:
    now = datetime.datetime.utcnow()
    ttl_minutes = get_password_reset_ttl_minutes()
    raw_token = secrets.token_urlsafe(18)

    db.query(PasswordResetToken).filter(
        PasswordResetToken.user_id == user.id,
        PasswordResetToken.used_at.is_(None),
    ).delete(synchronize_session=False)

    db.add(
        PasswordResetToken(
            user_id=user.id,
            token_hash=hash_password_reset_token(raw_token),
            expires_at=now + datetime.timedelta(minutes=ttl_minutes),
        )
    )
    db.commit()
    return raw_token


def issue_password_reset_token_for_email(db: Session, email: str) -> str | None:
    user = find_user_by_email(db, email)
    if not user:
        return None
    return issue_password_reset_token(db, user)


def reset_password_with_token(db: Session, *, email: str, reset_token: str, new_password: str) -> User:
    normalized_email = normalize_email(email)
    cleaned_token = reset_token.strip()
    if not cleaned_token:
        raise ValueError("Reset code is required")

    validate_user_password(new_password)

    user = find_user_by_email(db, normalized_email)
    if not user:
        raise ValueError("Invalid or expired reset code")

    now = datetime.datetime.utcnow()
    token_record = (
        db.query(PasswordResetToken)
        .filter(
            PasswordResetToken.user_id == user.id,
            PasswordResetToken.token_hash == hash_password_reset_token(cleaned_token),
            PasswordResetToken.used_at.is_(None),
        )
        .order_by(PasswordResetToken.id.desc())
        .first()
    )
    if not token_record or token_record.expires_at < now:
        raise ValueError("Invalid or expired reset code")

    user.password_hash = hash_password(new_password)
    token_record.used_at = now
    db.query(PasswordResetToken).filter(
        PasswordResetToken.user_id == user.id,
        PasswordResetToken.used_at.is_(None),
        PasswordResetToken.id != token_record.id,
    ).update({"used_at": now}, synchronize_session=False)
    db.commit()
    db.refresh(user)
    return user
