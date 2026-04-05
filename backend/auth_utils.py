import os
import secrets
import string
import threading
import time
from typing import Optional

from fastapi import Request
from passlib.context import CryptContext

DEFAULT_SECRET_KEY = "gat-prep-secret-key-change-in-production"
PRODUCTION_ENV_NAMES = ("APP_ENV", "ENVIRONMENT", "RAILWAY_ENVIRONMENT", "RAILWAY_ENVIRONMENT_NAME")
PRODUCTION_ENV_VALUES = {"prod", "production"}
USER_PASSWORD_MIN_LENGTH = 8
ADMIN_PASSWORD_MIN_LENGTH = 20
BCRYPT_PASSWORD_MAX_BYTES = 72

_pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def is_production_env() -> bool:
    for name in PRODUCTION_ENV_NAMES:
        value = os.getenv(name)
        if value and value.strip().lower() in PRODUCTION_ENV_VALUES:
            return True
    return False


def get_secret_key() -> str:
    secret = os.getenv("SECRET_KEY", DEFAULT_SECRET_KEY)
    if is_production_env() and secret == DEFAULT_SECRET_KEY:
        raise RuntimeError("SECRET_KEY must be set explicitly in production")
    return secret


def resolve_cors_configuration() -> tuple[list[str], bool]:
    raw_origins = os.getenv("CORS_ORIGINS", "*").strip()
    origins = [origin.strip() for origin in raw_origins.split(",") if origin.strip()]
    if not origins:
        origins = ["*"]

    if is_production_env() and "*" in origins:
        raise RuntimeError("CORS_ORIGINS must list explicit origins in production")

    allow_credentials = "*" not in origins
    return origins, allow_credentials


def normalize_email(email: str) -> str:
    return email.strip().lower()


def validate_user_password(password: str) -> None:
    if len(password) < USER_PASSWORD_MIN_LENGTH:
        raise ValueError(f"Password must be at least {USER_PASSWORD_MIN_LENGTH} characters")
    if len(password.encode("utf-8")) > BCRYPT_PASSWORD_MAX_BYTES:
        raise ValueError(
            f"Password must be {BCRYPT_PASSWORD_MAX_BYTES} bytes or fewer"
        )
    if not any(ch.isalpha() for ch in password):
        raise ValueError("Password must include at least one letter")
    if not any(ch.isdigit() for ch in password):
        raise ValueError("Password must include at least one number")


def validate_admin_password(password: str) -> None:
    if len(password) < ADMIN_PASSWORD_MIN_LENGTH:
        raise ValueError(f"Admin password must be at least {ADMIN_PASSWORD_MIN_LENGTH} characters")
    if len(password.encode("utf-8")) > BCRYPT_PASSWORD_MAX_BYTES:
        raise ValueError(
            f"Admin password must be {BCRYPT_PASSWORD_MAX_BYTES} bytes or fewer"
        )
    if not any(ch.islower() for ch in password):
        raise ValueError("Admin password must include a lowercase letter")
    if not any(ch.isupper() for ch in password):
        raise ValueError("Admin password must include an uppercase letter")
    if not any(ch.isdigit() for ch in password):
        raise ValueError("Admin password must include a number")
    if not any(ch in string.punctuation for ch in password):
        raise ValueError("Admin password must include a symbol")


def hash_password(password: str) -> str:
    return _pwd_context.hash(password)


def verify_password(password: str, password_hash: str) -> bool:
    try:
        return _pwd_context.verify(password, password_hash)
    except (ValueError, TypeError):
        return False


def generate_secure_password(length: int = 24) -> str:
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation),
    ]
    password.extend(secrets.choice(alphabet) for _ in range(max(length, ADMIN_PASSWORD_MIN_LENGTH) - len(password)))
    secrets.SystemRandom().shuffle(password)
    generated = "".join(password)
    validate_admin_password(generated)
    return generated


def get_client_ip(request: Request) -> str:
    forwarded_for = request.headers.get("x-forwarded-for")
    if forwarded_for:
        return forwarded_for.split(",")[0].strip()
    if request.client and request.client.host:
        return request.client.host
    return "unknown"


class InMemoryAuthRateLimiter:
    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._registration_attempts: dict[str, list[float]] = {}
        self._failed_login_attempts: dict[str, list[float]] = {}

    def _prune(self, attempts: dict[str, list[float]], key: str, window_seconds: int, now: float) -> list[float]:
        values = [timestamp for timestamp in attempts.get(key, []) if now - timestamp < window_seconds]
        if values:
            attempts[key] = values
        elif key in attempts:
            attempts.pop(key, None)
        return values

    def register_retry_after(self, client_ip: str) -> Optional[int]:
        now = time.time()
        with self._lock:
            attempts = self._prune(self._registration_attempts, client_ip, 3600, now)
            if len(attempts) >= 3:
                oldest = min(attempts)
                return max(1, int(3600 - (now - oldest)))
            attempts.append(now)
            self._registration_attempts[client_ip] = attempts
        return None

    def login_retry_after(self, client_ip: str, email: str) -> Optional[int]:
        now = time.time()
        with self._lock:
            ip_key = f"ip:{client_ip}"
            email_key = f"email:{email}"
            ip_attempts = self._prune(self._failed_login_attempts, ip_key, 900, now)
            email_attempts = self._prune(self._failed_login_attempts, email_key, 900, now)
            max_attempts = max(len(ip_attempts), len(email_attempts))
            if max_attempts >= 10:
                combined = ip_attempts + email_attempts
                oldest = min(combined)
                return max(1, int(900 - (now - oldest)))
        return None

    def record_login_failure(self, client_ip: str, email: str) -> None:
        now = time.time()
        with self._lock:
            for key in (f"ip:{client_ip}", f"email:{email}"):
                attempts = self._prune(self._failed_login_attempts, key, 900, now)
                attempts.append(now)
                self._failed_login_attempts[key] = attempts

    def clear_login_failures(self, client_ip: str, email: str) -> None:
        with self._lock:
            self._failed_login_attempts.pop(f"ip:{client_ip}", None)
            self._failed_login_attempts.pop(f"email:{email}", None)


auth_rate_limiter = InMemoryAuthRateLimiter()
