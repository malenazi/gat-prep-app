from __future__ import annotations

import argparse
import json
import os
import secrets
import sys
import time
import urllib.error
import urllib.request


DEFAULT_BASE_URL = "https://gat-prep-prod-production.up.railway.app"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run post-deploy smoke checks against the public API."
    )
    parser.add_argument(
        "--base-url",
        default=os.getenv("PRODUCTION_CHECK_BASE", DEFAULT_BASE_URL),
        help="Application base URL.",
    )
    parser.add_argument(
        "--learner-email",
        default=os.getenv("SMOKE_EMAIL", ""),
        help="Existing learner email for authenticated smoke checks.",
    )
    parser.add_argument(
        "--learner-password",
        default=os.getenv("SMOKE_PASSWORD", ""),
        help="Existing learner password for authenticated smoke checks.",
    )
    parser.add_argument(
        "--learner-name",
        default=os.getenv("SMOKE_NAME", "Smoke Test Learner"),
        help="Name to use when auto-registering a learner.",
    )
    parser.add_argument(
        "--admin-email",
        default=os.getenv("SMOKE_ADMIN_EMAIL") or os.getenv("BOOTSTRAP_ADMIN_EMAIL", ""),
        help="Admin email for admin-only smoke checks.",
    )
    parser.add_argument(
        "--admin-password",
        default=os.getenv("SMOKE_ADMIN_PASSWORD") or os.getenv("BOOTSTRAP_ADMIN_PASSWORD", ""),
        help="Admin password for admin-only smoke checks.",
    )
    parser.add_argument(
        "--skip-admin",
        action="store_true",
        help="Skip admin-only smoke checks.",
    )
    parser.add_argument(
        "--no-auto-register",
        action="store_true",
        help="Fail learner-auth smoke checks if no learner credentials are provided.",
    )
    return parser.parse_args()


def request_json(
    method: str,
    url: str,
    *,
    payload: dict | None = None,
    headers: dict[str, str] | None = None,
    timeout: int = 15,
) -> tuple[int, dict]:
    request_headers = {"Accept": "application/json"}
    if headers:
        request_headers.update(headers)

    body = None
    if payload is not None:
        body = json.dumps(payload).encode("utf-8")
        request_headers["Content-Type"] = "application/json"

    request = urllib.request.Request(
        url,
        data=body,
        headers=request_headers,
        method=method,
    )

    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            text = response.read().decode("utf-8")
            return response.status, json.loads(text) if text else {}
    except urllib.error.HTTPError as exc:
        text = exc.read().decode("utf-8")
        payload = json.loads(text) if text else {}
        return exc.code, payload


def log_step(label: str, ok: bool, detail: str) -> None:
    status = "[OK]" if ok else "[FAIL]"
    print(f"{status} {label}: {detail}")


def login(base_url: str, email: str, password: str) -> dict:
    status, payload = request_json(
        "POST",
        f"{base_url}/api/auth/login",
        payload={"email": email, "password": password},
    )
    if status != 200 or "token" not in payload:
        raise RuntimeError(f"login failed with status {status}: {payload}")
    return payload


def register(base_url: str, name: str, email: str, password: str) -> dict:
    status, payload = request_json(
        "POST",
        f"{base_url}/api/auth/register",
        payload={"name": name, "email": email, "password": password},
    )
    if status != 200 or "token" not in payload:
        raise RuntimeError(f"register failed with status {status}: {payload}")
    return payload


def auth_headers(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}


def auto_register_credentials() -> tuple[str, str]:
    suffix = f"{int(time.time())}-{secrets.token_hex(3)}"
    email = f"smoke+{suffix}@qudra.academy"
    password = f"Smoke!{secrets.token_hex(6)}A1"
    return email, password


def main() -> int:
    args = parse_args()
    base_url = args.base_url.rstrip("/")

    failures = 0

    status, payload = request_json("GET", f"{base_url}/health")
    health_ok = status == 200 and payload.get("status") == "ok"
    log_step("Health", health_ok, f"status={status} payload={payload}")
    failures += 0 if health_ok else 1

    status, payload = request_json("GET", f"{base_url}/api/skills")
    skills_ok = status == 200 and isinstance(payload, list) and len(payload) >= 9
    log_step("Skills", skills_ok, f"status={status} count={len(payload) if isinstance(payload, list) else 'n/a'}")
    failures += 0 if skills_ok else 1

    learner_email = args.learner_email.strip()
    learner_password = args.learner_password.strip()

    try:
        if learner_email and learner_password:
            learner_auth = login(base_url, learner_email, learner_password)
            log_step("Learner login", True, learner_email)
        elif not args.no_auto_register:
            learner_email, learner_password = auto_register_credentials()
            learner_auth = register(
                base_url,
                args.learner_name,
                learner_email,
                learner_password,
            )
            log_step("Learner registration", True, learner_email)
        else:
            raise RuntimeError(
                "no learner credentials were supplied and auto-register is disabled"
            )

        learner_token = learner_auth["token"]
        status, me = request_json(
            "GET",
            f"{base_url}/api/me",
            headers=auth_headers(learner_token),
        )
        me_ok = status == 200 and me.get("email") == learner_email.lower()
        log_step("Learner profile", me_ok, f"status={status} email={me.get('email')}")
        failures += 0 if me_ok else 1

        if me.get("diagnostic_completed"):
            status, practice = request_json(
                "GET",
                f"{base_url}/api/practice/next",
                headers=auth_headers(learner_token),
            )
            practice_ok = status == 200 and isinstance(practice, dict)
            log_step("Practice access", practice_ok, f"status={status}")
            failures += 0 if practice_ok else 1
        else:
            status, start_payload = request_json(
                "POST",
                f"{base_url}/api/diagnostic/start",
                headers=auth_headers(learner_token),
            )
            start_ok = status == 200 and "total_questions" in start_payload
            log_step("Diagnostic start", start_ok, f"status={status}")
            failures += 0 if start_ok else 1

            status, next_payload = request_json(
                "GET",
                f"{base_url}/api/diagnostic/next",
                headers=auth_headers(learner_token),
            )
            next_ok = status == 200 and isinstance(next_payload, dict) and not next_payload.get("done")
            log_step("Diagnostic question", next_ok, f"status={status}")
            failures += 0 if next_ok else 1

    except Exception as exc:
        log_step("Learner flow", False, str(exc))
        failures += 1

    if args.skip_admin:
        log_step("Admin flow", True, "skipped by flag")
    elif args.admin_email.strip() and args.admin_password.strip():
        try:
            admin_auth = login(base_url, args.admin_email.strip(), args.admin_password.strip())
            log_step("Admin login", True, args.admin_email.strip())

            admin_token = admin_auth["token"]
            status, me = request_json(
                "GET",
                f"{base_url}/api/me",
                headers=auth_headers(admin_token),
            )
            admin_me_ok = status == 200 and me.get("is_admin") is True
            log_step("Admin profile", admin_me_ok, f"status={status} is_admin={me.get('is_admin')}")
            failures += 0 if admin_me_ok else 1

            status, config_payload = request_json(
                "GET",
                f"{base_url}/api/admin/config",
                headers=auth_headers(admin_token),
            )
            admin_config_ok = status == 200 and isinstance(config_payload, dict)
            log_step("Admin config", admin_config_ok, f"status={status}")
            failures += 0 if admin_config_ok else 1
        except Exception as exc:
            log_step("Admin flow", False, str(exc))
            failures += 1
    else:
        log_step("Admin flow", True, "skipped because no admin credentials were supplied")

    if failures:
        print(f"[FAIL] Smoke check finished with {failures} failure(s).", file=sys.stderr)
        return 1

    print("[OK] Smoke check completed successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
