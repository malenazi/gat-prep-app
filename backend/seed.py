import os

from database import Base, SessionLocal, engine
from models import AppConfig, Badge, Question, Skill, User
from question_content import ensure_question_content_columns
from question_visuals import ensure_question_visual_columns
from sync_question_bank import sync_question_bank
from user_management import LEGACY_DEMO_EMAILS, bootstrap_admin_user, purge_users_by_emails


def maybe_bootstrap_startup_admin(db) -> None:
    admin_password = os.getenv("BOOTSTRAP_ADMIN_PASSWORD", "").strip()
    if not admin_password:
        return

    existing_admin = db.query(User).filter(User.is_admin == True).first()
    if existing_admin:
        return

    admin_email = os.getenv("BOOTSTRAP_ADMIN_EMAIL", "admin@qudra.academy").strip() or "admin@qudra.academy"
    admin_name = os.getenv("BOOTSTRAP_ADMIN_NAME", "System Admin").strip() or "System Admin"
    bootstrap_admin_user(
        db,
        name=admin_name,
        email=admin_email,
        password=admin_password,
    )
    print(f"Bootstrapped startup admin: {admin_email}")


def seed_all() -> None:
    Base.metadata.create_all(bind=engine)
    ensure_question_visual_columns(engine)
    ensure_question_content_columns(engine)
    db = SessionLocal()

    try:
        if db.query(Skill).count() == 0:
            skills = [
                Skill(id="verbal_reading", section="verbal", name_ar="Reading Comprehension", name_en="Reading Comprehension", exam_weight=0.35, icon="📖"),
                Skill(id="verbal_analogy", section="verbal", name_ar="Verbal Analogy", name_en="Verbal Analogy", exam_weight=0.25, icon="🔗"),
                Skill(id="verbal_completion", section="verbal", name_ar="Sentence Completion", name_en="Sentence Completion", exam_weight=0.20, icon="✏️"),
                Skill(id="verbal_error", section="verbal", name_ar="Contextual Error", name_en="Contextual Error", exam_weight=0.15, icon="🔍"),
                Skill(id="verbal_oddword", section="verbal", name_ar="Odd Word Out", name_en="Odd Word Out", exam_weight=0.05, icon="❌"),
                Skill(id="quant_arithmetic", section="quantitative", name_ar="Arithmetic", name_en="Arithmetic", exam_weight=0.40, icon="🔢"),
                Skill(id="quant_geometry", section="quantitative", name_ar="Geometry", name_en="Geometry", exam_weight=0.24, icon="📐"),
                Skill(id="quant_algebra", section="quantitative", name_ar="Algebra", name_en="Algebra", exam_weight=0.23, icon="🧮"),
                Skill(id="quant_statistics", section="quantitative", name_ar="Statistics & Analysis", name_en="Statistics & Analysis", exam_weight=0.13, icon="📊"),
            ]
            db.add_all(skills)
            db.commit()

        if db.query(Badge).count() == 0:
            badges = [
                Badge(id="first_step", name_ar="First Step", description_ar="Answered your first question", icon="👣", criteria_type="questions", criteria_value=1),
                Badge(id="warrior", name_ar="Warrior", description_ar="Answered 100 questions", icon="⚔️", criteria_type="questions", criteria_value=100),
                Badge(id="legend", name_ar="Legend", description_ar="Answered 500 questions", icon="🏆", criteria_type="questions", criteria_value=500),
                Badge(id="streak_7", name_ar="Week Streak", description_ar="Maintained a 7-day streak", icon="🔥", criteria_type="streak", criteria_value=7),
                Badge(id="streak_14", name_ar="Two Weeks", description_ar="Maintained a 14-day streak", icon="💪", criteria_type="streak", criteria_value=14),
                Badge(id="streak_30", name_ar="Full Month", description_ar="Completed 30 consecutive days!", icon="👑", criteria_type="streak", criteria_value=30),
                Badge(id="first_mock", name_ar="First Mock", description_ar="Completed your first mock exam", icon="📝", criteria_type="mock", criteria_value=1),
                Badge(id="score_80", name_ar="Excellence", description_ar="Scored 80+ on a mock exam", icon="⭐", criteria_type="score", criteria_value=80),
                Badge(id="perfect_quiz", name_ar="Perfect Quiz", description_ar="Answered 10 consecutive questions correctly", icon="💎", criteria_type="streak", criteria_value=10),
            ]
            db.add_all(badges)
            db.commit()

        sync_report = sync_question_bank(db)
        print(
            "Synced question bank: "
            f"{sync_report['source_total']} source / "
            f"{sync_report['updated']} updated / "
            f"{sync_report['created']} created"
        )

        removed_legacy_users = purge_users_by_emails(db, LEGACY_DEMO_EMAILS)
        if removed_legacy_users:
            print(f"Removed {removed_legacy_users} legacy demo/admin users")

        maybe_bootstrap_startup_admin(db)

        if db.query(AppConfig).get("mock_max_attempts") is None:
            db.add(AppConfig(key="mock_max_attempts", value="4"))
            db.commit()
            print("Seeded config: mock_max_attempts=4")
    finally:
        db.close()


if __name__ == "__main__":
    seed_all()
