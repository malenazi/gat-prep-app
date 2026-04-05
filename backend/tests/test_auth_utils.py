import pytest
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from auth_utils import (
    InMemoryAuthRateLimiter,
    generate_secure_password,
    normalize_email,
    validate_admin_password,
    validate_user_password,
)


def test_normalize_email_trims_and_lowercases():
    assert normalize_email("  Test.User@Example.COM  ") == "test.user@example.com"


def test_validate_user_password_requires_letter_and_number():
    with pytest.raises(ValueError):
        validate_user_password("12345678")

    with pytest.raises(ValueError):
        validate_user_password("password")

    validate_user_password("Password123")


def test_validate_admin_password_requires_strong_format():
    with pytest.raises(ValueError):
        validate_admin_password("short")

    with pytest.raises(ValueError):
        validate_admin_password("alllowercasepassword123!")

    with pytest.raises(ValueError):
        validate_admin_password("ALLUPPERCASEPASSWORD123!")

    with pytest.raises(ValueError):
        validate_admin_password("NoSymbolsPassword1234")

    validate_admin_password("AdminBootstrapPassword!123")


def test_generated_admin_password_passes_validation():
    password = generate_secure_password()
    validate_admin_password(password)
    assert len(password) >= 20


def test_registration_rate_limiter_blocks_after_three_attempts():
    limiter = InMemoryAuthRateLimiter()

    assert limiter.register_retry_after("127.0.0.1") is None
    assert limiter.register_retry_after("127.0.0.1") is None
    assert limiter.register_retry_after("127.0.0.1") is None
    assert limiter.register_retry_after("127.0.0.1") is not None


def test_login_rate_limiter_blocks_after_ten_failures_and_clears_on_success():
    limiter = InMemoryAuthRateLimiter()
    ip = "127.0.0.1"
    email = "user@example.com"

    for _ in range(10):
        limiter.record_login_failure(ip, email)

    assert limiter.login_retry_after(ip, email) is not None
    limiter.clear_login_failures(ip, email)
    assert limiter.login_retry_after(ip, email) is None
