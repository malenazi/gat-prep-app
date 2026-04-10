"""Email service using Resend API for transactional emails."""

import os
import logging

import resend

logger = logging.getLogger(__name__)

RESEND_API_KEY_ENV = "RESEND_API_KEY"
FROM_EMAIL_ENV = "FROM_EMAIL"
DEFAULT_FROM = "Qudra Academy <noreply@qudra.academy>"


def _get_api_key() -> str | None:
    return os.getenv(RESEND_API_KEY_ENV, "").strip() or None


def _get_from_email() -> str:
    return os.getenv(FROM_EMAIL_ENV, "").strip() or DEFAULT_FROM


def is_email_enabled() -> bool:
    return bool(_get_api_key())


def send_email(*, to: str, subject: str, html: str) -> bool:
    """Send an email via Resend. Returns True on success, False on failure."""
    api_key = _get_api_key()
    if not api_key:
        logger.warning("RESEND_API_KEY not set — email not sent to %s", to)
        return False

    resend.api_key = api_key
    try:
        resend.Emails.send({
            "from": _get_from_email(),
            "to": [to],
            "subject": subject,
            "html": html,
        })
        logger.info("Email sent to %s: %s", to, subject)
        return True
    except Exception as e:
        logger.error("Failed to send email to %s: %s", to, e)
        return False


def send_password_reset_email(*, to: str, reset_code: str, expires_minutes: int) -> bool:
    """Send password reset code email."""
    return send_email(
        to=to,
        subject="Your Qudra Academy Password Reset Code",
        html=f"""
        <div style="font-family: Arial, sans-serif; max-width: 480px; margin: 0 auto; padding: 32px;">
            <div style="text-align: center; margin-bottom: 24px;">
                <h1 style="color: #0d9488; font-size: 24px; margin: 0;">Qudra Academy</h1>
                <p style="color: #64748b; font-size: 14px;">Password Reset</p>
            </div>
            <div style="background: #f8fafc; border-radius: 12px; padding: 24px; text-align: center;">
                <p style="color: #334155; font-size: 14px; margin-bottom: 16px;">
                    Use the code below to reset your password. It expires in {expires_minutes} minutes.
                </p>
                <div style="background: #0d9488; color: white; font-size: 28px; font-weight: bold; letter-spacing: 4px; padding: 16px 32px; border-radius: 8px; display: inline-block;">
                    {reset_code}
                </div>
                <p style="color: #94a3b8; font-size: 12px; margin-top: 16px;">
                    If you did not request this, please ignore this email.
                </p>
            </div>
        </div>
        """,
    )


def send_ticket_confirmation_email(*, to: str, ticket_id: int, category: str) -> bool:
    """Send support ticket confirmation email."""
    return send_email(
        to=to,
        subject=f"Support Ticket #{ticket_id} Received",
        html=f"""
        <div style="font-family: Arial, sans-serif; max-width: 480px; margin: 0 auto; padding: 32px;">
            <div style="text-align: center; margin-bottom: 24px;">
                <h1 style="color: #0d9488; font-size: 24px; margin: 0;">Qudra Academy</h1>
                <p style="color: #64748b; font-size: 14px;">Support</p>
            </div>
            <div style="background: #f8fafc; border-radius: 12px; padding: 24px;">
                <p style="color: #334155; font-size: 14px;">
                    We received your <strong>{category}</strong> ticket (#{ticket_id}).
                    Our team will review it and get back to you.
                </p>
                <p style="color: #94a3b8; font-size: 12px; margin-top: 16px;">
                    You can check your ticket status in Settings &gt; Support.
                </p>
            </div>
        </div>
        """,
    )
