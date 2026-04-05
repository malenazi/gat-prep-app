from __future__ import annotations

import argparse
import datetime as dt
import os
import sqlite3
import sys
from pathlib import Path


DEFAULT_DATABASE_URL = (
    f"sqlite:///{(Path(__file__).resolve().parent / 'backend' / 'gat_prep.db').as_posix()}"
)
DEFAULT_OUTPUT_DIR = Path("backups/sqlite")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a timestamped backup of the active SQLite database."
    )
    parser.add_argument(
        "--database-url",
        default=os.getenv("DATABASE_URL", DEFAULT_DATABASE_URL),
        help="SQLAlchemy-style database URL. Only sqlite:/// URLs are supported.",
    )
    parser.add_argument(
        "--output-dir",
        default=os.getenv("SQLITE_BACKUP_DIR", str(DEFAULT_OUTPUT_DIR)),
        help="Directory where the backup file will be written.",
    )
    parser.add_argument(
        "--label",
        default=os.getenv("SQLITE_BACKUP_LABEL", "sqlite-backup"),
        help="Short label to include in the backup filename.",
    )
    return parser.parse_args()


def sqlite_path_from_url(database_url: str) -> Path:
    prefix = "sqlite:///"
    if not database_url.startswith(prefix):
        raise ValueError(
            f"Only sqlite:/// URLs are supported for backups. Got: {database_url}"
        )

    raw_path = database_url[len(prefix) :].split("?", 1)[0]
    if os.name == "nt" and raw_path.startswith("/") and len(raw_path) > 2 and raw_path[2] == ":":
        raw_path = raw_path[1:]

    path = Path(raw_path)
    return path if path.is_absolute() else (Path.cwd() / path).resolve()


def backup_sqlite(source_path: Path, output_dir: Path, label: str) -> Path:
    if not source_path.exists():
        raise FileNotFoundError(f"SQLite database not found: {source_path}")

    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    backup_path = output_dir / f"{label}-{timestamp}.sqlite3"

    source_connection = sqlite3.connect(str(source_path))
    backup_connection = sqlite3.connect(str(backup_path))
    try:
        with backup_connection:
            source_connection.backup(backup_connection)
    finally:
        source_connection.close()
        backup_connection.close()

    return backup_path.resolve()


def main() -> int:
    args = parse_args()

    try:
        source_path = sqlite_path_from_url(args.database_url)
        backup_path = backup_sqlite(source_path, Path(args.output_dir), args.label)
    except Exception as exc:
        print(f"[FAIL] SQLite backup failed: {exc}", file=sys.stderr)
        return 1

    print("[OK] SQLite backup created")
    print(f"Source DB : {source_path}")
    print(f"Backup DB : {backup_path}")
    print("Copy this backup off the host before deploying if the runtime filesystem is ephemeral.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
