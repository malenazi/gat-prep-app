import os
from pathlib import Path


def sqlite_db_path(database_url: str) -> Path:
    prefix = "sqlite:///"
    if not database_url.startswith(prefix):
        raise ValueError(f"Only sqlite URLs are supported for reset: {database_url}")
    return Path(database_url[len(prefix):]).resolve()


def reset_database() -> Path:
    default_sqlite_url = f"sqlite:///{Path(__file__).resolve().with_name('gat_prep.db').as_posix()}"
    database_url = os.getenv(
        "DATABASE_URL",
        os.getenv("E2E_DATABASE_URL", default_sqlite_url),
    )
    db_path = sqlite_db_path(database_url)

    if db_path.exists():
        db_path.unlink()

    from database import SessionLocal
    from seed import seed_all
    from test_support import bootstrap_sample_users

    seed_all()
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
    return db_path


def _env_user(prefix: str) -> dict[str, str] | None:
    email = os.getenv(f"{prefix}_EMAIL", "").strip()
    password = os.getenv(f"{prefix}_PASSWORD", "").strip()
    name = os.getenv(f"{prefix}_NAME", "").strip()
    if not email or not password or not name:
        return None
    return {"email": email, "password": password, "name": name}


if __name__ == "__main__":
    path = reset_database()
    print(f"Reset database at {path}")
