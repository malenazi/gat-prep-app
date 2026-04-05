import argparse

from auth_utils import hash_password, validate_admin_password
from database import SessionLocal
from user_management import find_user_by_email, purge_users_by_emails


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Perform targeted user maintenance tasks without wiping the full database."
    )
    parser.add_argument(
        "--delete-email",
        action="append",
        dest="delete_emails",
        default=[],
        help="Delete a user and their related learner data by email. Can be provided multiple times.",
    )
    parser.add_argument(
        "--rotate-admin-email",
        help="Admin email whose password should be rotated.",
    )
    parser.add_argument(
        "--new-admin-password",
        help="New admin password to hash and store.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if args.rotate_admin_email and not args.new_admin_password:
        raise SystemExit("--new-admin-password is required when rotating an admin password")
    if args.new_admin_password and not args.rotate_admin_email:
        raise SystemExit("--rotate-admin-email is required when providing a new admin password")

    deleted_users = 0

    db = SessionLocal()
    try:
        if args.delete_emails:
            deleted_users = purge_users_by_emails(db, args.delete_emails)

        rotated_admin = None
        if args.rotate_admin_email:
            validate_admin_password(args.new_admin_password)
            rotated_admin = find_user_by_email(db, args.rotate_admin_email)
            if rotated_admin is None:
                raise SystemExit(f"Admin user not found: {args.rotate_admin_email}")
            if not rotated_admin.is_admin:
                raise SystemExit(f"User is not an admin: {rotated_admin.email}")
            rotated_admin.password_hash = hash_password(args.new_admin_password)
            db.add(rotated_admin)
            db.commit()

        print(f"deleted_users={deleted_users}")
        if rotated_admin is not None:
            print(f"rotated_admin={rotated_admin.email}")
    finally:
        db.close()


if __name__ == "__main__":
    main()
