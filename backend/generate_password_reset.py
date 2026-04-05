import argparse

from database import SessionLocal
from password_reset import get_password_reset_ttl_minutes, issue_password_reset_token_for_email


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a one-time password reset code for a learner")
    parser.add_argument("email", help="Email address for the learner account")
    args = parser.parse_args()

    db = SessionLocal()
    try:
        token = issue_password_reset_token_for_email(db, args.email)
    finally:
        db.close()

    if not token:
        raise SystemExit(f"No learner account found for {args.email}")

    print(f"Reset code for {args.email}: {token}")
    print(f"Expires in about {get_password_reset_ttl_minutes()} minutes.")


if __name__ == "__main__":
    main()
