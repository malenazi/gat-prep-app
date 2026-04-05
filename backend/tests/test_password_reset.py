import datetime
import sys
from pathlib import Path

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

backend_dir = Path(__file__).resolve().parent.parent
test_db_path = backend_dir / "gat_prep.reset-test.db"

sys.path.insert(0, str(backend_dir))

from auth_utils import verify_password
from database import Base
from models import PasswordResetToken, User
from password_reset import issue_password_reset_token, reset_password_with_token
from user_management import create_user

test_engine = create_engine(
    f"sqlite:///{test_db_path.as_posix()}",
    connect_args={"check_same_thread": False},
)
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)

Base.metadata.create_all(bind=test_engine)


def clear_reset_test_data() -> None:
    db = TestSessionLocal()
    try:
        db.query(PasswordResetToken).delete(synchronize_session=False)
        db.query(User).delete(synchronize_session=False)
        db.commit()
    finally:
        db.close()


def test_password_reset_token_updates_password_and_is_single_use():
    clear_reset_test_data()
    email = "reset-learner@example.com"

    db = TestSessionLocal()
    try:
        user = create_user(
            db,
            name="Reset Learner",
            email=email,
            password="OriginalPass123",
        )
        reset_token = issue_password_reset_token(db, user)
    finally:
        db.close()

    db = TestSessionLocal()
    try:
        updated_user = reset_password_with_token(
            db,
            email=email,
            reset_token=reset_token,
            new_password="UpdatedPass456",
        )
        assert verify_password("UpdatedPass456", updated_user.password_hash)

        stored_token = db.query(PasswordResetToken).filter_by(user_id=updated_user.id).one()
        assert stored_token.used_at is not None

        with pytest.raises(ValueError):
            reset_password_with_token(
                db,
                email=email,
                reset_token=reset_token,
                new_password="SecondPass789",
            )
    finally:
        db.close()


def test_password_reset_token_rejects_expired_codes():
    clear_reset_test_data()
    email = "expired-reset@example.com"

    db = TestSessionLocal()
    try:
        user = create_user(
            db,
            name="Expired Reset",
            email=email,
            password="OriginalPass123",
        )
        reset_token = issue_password_reset_token(db, user)

        token_record = db.query(PasswordResetToken).filter_by(user_id=user.id).one()
        token_record.expires_at = datetime.datetime.utcnow() - datetime.timedelta(minutes=1)
        db.commit()

        with pytest.raises(ValueError):
            reset_password_with_token(
                db,
                email=email,
                reset_token=reset_token,
                new_password="UpdatedPass456",
            )
    finally:
        db.close()
