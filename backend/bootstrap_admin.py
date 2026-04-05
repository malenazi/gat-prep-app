import os

from auth_utils import generate_secure_password
from database import SessionLocal
from user_management import bootstrap_admin_user


def main() -> None:
    email = os.getenv("BOOTSTRAP_ADMIN_EMAIL", "admin@qudra.academy")
    name = os.getenv("BOOTSTRAP_ADMIN_NAME", "System Admin")
    password = os.getenv("BOOTSTRAP_ADMIN_PASSWORD") or generate_secure_password()
    generated_password = "BOOTSTRAP_ADMIN_PASSWORD" not in os.environ

    db = SessionLocal()
    try:
        user = bootstrap_admin_user(db, name=name, email=email, password=password)
    finally:
        db.close()

    print(f"Bootstrapped admin user: {user.email}")
    print("Store this password securely and rotate it after first login.")
    if generated_password:
        print(f"One-time admin password: {password}")


if __name__ == "__main__":
    main()
