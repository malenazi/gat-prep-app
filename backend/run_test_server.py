import os
from pathlib import Path

default_test_db = Path(__file__).resolve().with_name("gat_prep.e2e.db")

os.environ.setdefault(
    "DATABASE_URL",
    os.getenv("E2E_DATABASE_URL", f"sqlite:///{default_test_db.as_posix()}"),
)

from reset_db import reset_database

reset_database()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=int(os.getenv("E2E_BACKEND_PORT", "8000")),
        reload=False,
    )
