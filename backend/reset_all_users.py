import argparse
import os

from auth_utils import generate_secure_password
from database import SessionLocal
from models import (
    Feedback,
    MockAttempt,
    PasswordResetToken,
    StudyPlan,
    User,
    UserAbility,
    UserBadge,
    UserResponse,
)
from user_management import bootstrap_admin_user


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Delete all users and bootstrap one fresh admin account."
    )
    parser.add_argument(
        "--admin-email",
        default=os.getenv("BOOTSTRAP_ADMIN_EMAIL", "admin@qudra.academy"),
        help="Email for the new admin account.",
    )
    parser.add_argument(
        "--admin-name",
        default=os.getenv("BOOTSTRAP_ADMIN_NAME", "System Admin"),
        help="Name for the new admin account.",
    )
    parser.add_argument(
        "--admin-password",
        default=os.getenv("BOOTSTRAP_ADMIN_PASSWORD", "").strip(),
        help="Password for the new admin account. If omitted, a strong password is generated.",
    )
    return parser.parse_args()


def delete_all_users() -> dict[str, int]:
    db = SessionLocal()
    try:
        counts = {
            "password_reset_tokens": db.query(PasswordResetToken).delete(synchronize_session=False),
            "user_responses": db.query(UserResponse).delete(synchronize_session=False),
            "mock_attempts": db.query(MockAttempt).delete(synchronize_session=False),
            "user_abilities": db.query(UserAbility).delete(synchronize_session=False),
            "user_badges": db.query(UserBadge).delete(synchronize_session=False),
            "study_plans": db.query(StudyPlan).delete(synchronize_session=False),
            "feedback": db.query(Feedback).delete(synchronize_session=False),
            "users": db.query(User).delete(synchronize_session=False),
        }
        db.commit()
        return counts
    finally:
        db.close()


def main() -> None:
    args = parse_args()
    password = args.admin_password or generate_secure_password()
    generated_password = not bool(args.admin_password)

    deleted_counts = delete_all_users()

    db = SessionLocal()
    try:
        admin = bootstrap_admin_user(
            db,
            name=args.admin_name,
            email=args.admin_email,
            password=password,
        )
    finally:
        db.close()

    print("Deleted user data:")
    for key, value in deleted_counts.items():
        print(f"- {key}: {value}")
    print(f"Bootstrapped admin user: {admin.email}")
    print("Store this password securely and rotate it after first login.")
    print(f"Admin password: {password}")
    if generated_password:
        print("Password source: generated")
    else:
        print("Password source: provided")


if __name__ == "__main__":
    main()
