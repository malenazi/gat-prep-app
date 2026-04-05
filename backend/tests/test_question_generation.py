import os
import sys
import subprocess


ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _run(script_name: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, os.path.join(ROOT_DIR, script_name)],
        capture_output=True,
        text=True,
        check=False,
    )


def test_generate_question_batch_is_disabled():
    result = _run("generate_question_batch.py")
    assert result.returncode != 0
    assert "Question generation is disabled" in result.stderr


def test_validate_question_batch_is_disabled():
    result = _run("validate_question_batch.py")
    assert result.returncode != 0
    assert "validation is disabled" in result.stderr


def test_import_question_batch_is_disabled():
    result = _run("import_question_batch.py")
    assert result.returncode != 0
    assert "import is disabled" in result.stderr


def test_report_generated_batch_is_disabled():
    result = _run("report_generated_batch.py")
    assert result.returncode != 0
    assert "reporting is disabled" in result.stderr
