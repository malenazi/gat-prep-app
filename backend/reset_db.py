import os
from pathlib import Path


def reset_database():
    from database import DATABASE_URL, engine, Base

    if DATABASE_URL.startswith("sqlite"):
        # SQLite: delete the file and recreate
        prefix = "sqlite:///"
        if DATABASE_URL.startswith(prefix):
            db_path = Path(DATABASE_URL[len(prefix):]).resolve()
            if db_path.exists():
                db_path.unlink()
    else:
        # PostgreSQL: drop all tables
        Base.metadata.drop_all(engine)

    # Re-import to pick up fresh engine state
    from seed import seed_all
    from test_support import bootstrap_sample_users

    seed_all()

    from database import SessionLocal
    db = SessionLocal()
    try:
        bootstrap_sample_users(
            db,
            new_student=_env_user("E2E_NEW_STUDENT"),
            progressed=_env_user("E2E_PROGRESS"),
            admin=_env_user("E2E_ADMIN"),
        )
    finally:
        db.close()

    return DATABASE_URL


def _env_user(prefix: str) -> dict[str, str] | None:
    email = os.getenv(f"{prefix}_EMAIL", "").strip()
    password = os.getenv(f"{prefix}_PASSWORD", "").strip()
    name = os.getenv(f"{prefix}_NAME", "").strip()
    if not email or not password or not name:
        return None
    return {"email": email, "password": password, "name": name}


if __name__ == "__main__":
    url = reset_database()
    print(f"Reset database: {url}")
