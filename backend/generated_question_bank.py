import json
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace
from typing import Any


GENERATED_BATCH_ROOT = Path(__file__).resolve().parent / "generated_batches"
GENERATED_DRAFT_DIR = GENERATED_BATCH_ROOT / "drafts"
GENERATED_PUBLISHED_DIR = GENERATED_BATCH_ROOT / "published"
GENERATED_REPORT_DIR = GENERATED_BATCH_ROOT / "reports"

AUTHORING_SOURCE_AI = "ai_generated"
AUTHORING_SOURCE_HUMAN = "human"


def ensure_generated_batch_dirs() -> None:
    for path in (GENERATED_BATCH_ROOT, GENERATED_DRAFT_DIR, GENERATED_PUBLISHED_DIR, GENERATED_REPORT_DIR):
        path.mkdir(parents=True, exist_ok=True)


def batch_path(batch_id: str, *, kind: str) -> Path:
    ensure_generated_batch_dirs()
    safe_batch_id = batch_id.strip().replace(" ", "-")
    if kind == "draft":
        return GENERATED_DRAFT_DIR / f"{safe_batch_id}.json"
    if kind == "published":
        return GENERATED_PUBLISHED_DIR / f"{safe_batch_id}.json"
    if kind == "report":
        return GENERATED_REPORT_DIR / f"{safe_batch_id}.json"
    raise ValueError(f"Unsupported batch path kind: {kind}")


def list_batch_files(*, kind: str) -> list[Path]:
    ensure_generated_batch_dirs()
    if kind == "draft":
        root = GENERATED_DRAFT_DIR
    elif kind == "published":
        root = GENERATED_PUBLISHED_DIR
    elif kind == "report":
        root = GENERATED_REPORT_DIR
    else:
        raise ValueError(f"Unsupported batch file kind: {kind}")
    return sorted(root.glob("*.json"))


def load_batch_manifest(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_batch_manifest(path: Path, manifest: dict[str, Any]) -> None:
    ensure_generated_batch_dirs()
    path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def load_generated_questions() -> list[Any]:
    ensure_generated_batch_dirs()
    questions: list[Any] = []
    for path in list_batch_files(kind="published"):
        manifest = load_batch_manifest(path)
        batch_id = manifest.get("batch_id") or path.stem
        prompt_version = manifest.get("generation_prompt_version")
        authoring_source = manifest.get("authoring_source") or AUTHORING_SOURCE_AI
        for index, item in enumerate(manifest.get("items") or [], start=1):
            payload = dict(item)
            payload.setdefault("batch_id", batch_id)
            payload.setdefault("generation_prompt_version", prompt_version)
            payload.setdefault("authoring_source", authoring_source)
            payload.setdefault("status", "active")
            payload.setdefault(
                "source_key",
                f"generated:{payload.get('skill_id', 'question')}:{batch_id}:{index:04d}",
            )
            questions.append(SimpleNamespace(**payload))
    return questions


def build_manifest(
    *,
    batch_id: str,
    items: list[dict[str, Any]],
    generation_prompt_version: str,
    authoring_source: str = AUTHORING_SOURCE_AI,
    generated_at: str | None = None,
    metadata: dict[str, Any] | None = None,
) -> dict[str, Any]:
    return {
        "batch_id": batch_id,
        "generated_at": generated_at
        or datetime.now(timezone.utc).isoformat(),
        "generation_prompt_version": generation_prompt_version,
        "authoring_source": authoring_source,
        "metadata": metadata or {},
        "items": items,
    }
