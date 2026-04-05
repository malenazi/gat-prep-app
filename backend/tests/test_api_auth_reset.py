import os
import sys
from uuid import uuid4

import requests

backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
default_test_db = os.path.join(backend_dir, "gat_prep.e2e.db").replace(os.sep, "/")
os.environ.setdefault("DATABASE_URL", f"sqlite:///{default_test_db}")

sys.path.insert(0, backend_dir)

BASE_URL = os.getenv("API_BASE_URL", "http://127.0.0.1:8000/api")


def test_forgot_password_flow_returns_reset_code_and_accepts_new_password():
    email = f"reset-{uuid4()}@example.com"
    original_password = f"OriginalPass!{uuid4().hex[:10]}9a"
    updated_password = f"UpdatedPass!{uuid4().hex[:10]}8b"
    headers = {"x-forwarded-for": f"198.51.100.{uuid4().int % 150 + 25}"}

    register_response = requests.post(
        f"{BASE_URL}/auth/register",
        headers=headers,
        json={
            "name": "Reset Flow Learner",
            "email": email,
            "password": original_password,
        },
        timeout=10,
    )
    assert register_response.status_code == 200, register_response.text

    forgot_response = requests.post(
        f"{BASE_URL}/auth/forgot-password",
        json={"email": email},
        timeout=10,
    )
    assert forgot_response.status_code == 200, forgot_response.text

    forgot_payload = forgot_response.json()
    reset_token = forgot_payload.get("reset_token_preview")
    assert reset_token, forgot_payload

    reset_response = requests.post(
        f"{BASE_URL}/auth/reset-password",
        json={
            "email": email,
            "reset_token": reset_token,
            "new_password": updated_password,
        },
        timeout=10,
    )
    assert reset_response.status_code == 200, reset_response.text

    login_response = requests.post(
        f"{BASE_URL}/auth/login",
        json={"email": email.upper(), "password": updated_password},
        timeout=10,
    )
    assert login_response.status_code == 200, login_response.text
