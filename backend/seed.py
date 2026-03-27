import hashlib, os
from database import SessionLocal, engine, Base
from models import Skill, Question, Badge, User

def seed_all():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    # ── Skills ──────────────────────────────────────────────────────────────
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

    # ── Badges ──────────────────────────────────────────────────────────────
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

    # ── Questions ────────────────────────────────────────────────────────────
    current_q_count = db.query(Question).count()
    if current_q_count < 1503:
        if current_q_count > 0:
            db.query(Question).delete()
            db.commit()
            print(f"Cleared {current_q_count} old questions for re-seed")
        from questions import load_all_questions
        questions = load_all_questions()
        db.add_all(questions)
        db.commit()
        print(f"Seeded {len(questions)} questions")

    # ── Demo Users ──────────────────────────────────────────────────────────
    from models import UserAbility, UserResponse, UserBadge, StudyPlan, Feedback
    from adaptive import generate_study_plan
    import datetime, random

    SECRET = os.getenv("SECRET_KEY", "gat-prep-secret-key-change-in-production")
    pw = lambda p: hashlib.sha256((p + SECRET).encode()).hexdigest()
    today = datetime.date.today().isoformat()
    skills_list = [s.id for s in db.query(Skill).all()]
    all_questions = db.query(Question).all()

    def seed_user_data(user, ability_profile, days_active, response_count, badge_ids):
        """Populate abilities, responses, study plan, badges for a demo user."""
        # Abilities
        for skill_id in skills_list:
            profile = ability_profile.get(skill_id, {})
            theta = profile.get('theta', 0.0)
            mastery = profile.get('mastery', 0.3)
            seen = profile.get('seen', 0)
            correct = profile.get('correct', 0)
            db.add(UserAbility(user_id=user.id, skill_id=skill_id, theta=theta,
                               mastery=mastery, questions_seen=seen, correct_count=correct))

        # Responses — simulate answering questions
        available_qs = list(all_questions)
        random.shuffle(available_qs)
        for i in range(min(response_count, len(available_qs))):
            q = available_qs[i]
            is_correct = random.random() < ability_profile.get(q.skill_id, {}).get('mastery', 0.4)
            chosen = q.correct_option if is_correct else random.choice([o for o in ['a','b','c','d'] if o != q.correct_option])
            resp = UserResponse(user_id=user.id, question_id=q.id, session_type="drill",
                                selected_option=chosen, is_correct=is_correct,
                                time_spent_seconds=random.randint(15, 80))
            # Backdate responses
            day_offset = random.randint(0, max(1, days_active - 1))
            resp.created_at = datetime.datetime.now() - datetime.timedelta(days=day_offset)
            db.add(resp)

        # Study plan
        generate_study_plan(db, user.id, user.daily_minutes)

        # Mark completed days
        plan_days = db.query(StudyPlan).filter_by(user_id=user.id).order_by(StudyPlan.day_number).all()
        for p in plan_days:
            if p.day_number < user.current_day:
                p.completed = True
                p.completed_questions = p.target_questions

        # Badges
        for badge_id in badge_ids:
            if db.query(Badge).filter_by(id=badge_id).first():
                db.add(UserBadge(user_id=user.id, badge_id=badge_id))

        db.commit()

    # ── 1. New student (hasn't started) ──
    if db.query(User).filter_by(email="student@gat.sa").first() is None:
        db.add(User(name="New Student", email="student@gat.sa", password_hash=pw("123456"),
                    diagnostic_completed=False, current_day=0, xp=0, streak_current=0, league="bronze"))
        db.commit()
        print("Seeded: student@gat.sa (new)")

    # ── 2. Sara — Day 5, beginner, Foundation phase ──
    if db.query(User).filter_by(email="sara@gat.sa").first() is None:
        sara = User(name="Sara Al-Mutairi", email="sara@gat.sa", password_hash=pw("123456"),
                    diagnostic_completed=True, current_day=5, xp=420, streak_current=5,
                    streak_longest=5, league="silver", daily_minutes=60,
                    last_active_date=today)
        db.add(sara)
        db.commit()
        seed_user_data(sara, {
            'verbal_reading':    {'theta': 0.3,  'mastery': 0.55, 'seen': 8,  'correct': 4},
            'verbal_analogy':    {'theta': -0.2, 'mastery': 0.40, 'seen': 6,  'correct': 2},
            'verbal_completion': {'theta': 0.1,  'mastery': 0.50, 'seen': 5,  'correct': 2},
            'verbal_error':      {'theta': -0.1, 'mastery': 0.33, 'seen': 4,  'correct': 1},
            'verbal_oddword':    {'theta': 0.0,  'mastery': 0.50, 'seen': 2,  'correct': 1},
            'quant_arithmetic':  {'theta': 0.5,  'mastery': 0.60, 'seen': 10, 'correct': 6},
            'quant_geometry':    {'theta': -0.3, 'mastery': 0.30, 'seen': 5,  'correct': 1},
            'quant_algebra':     {'theta': 0.2,  'mastery': 0.45, 'seen': 6,  'correct': 3},
            'quant_statistics':  {'theta': 0.0,  'mastery': 0.40, 'seen': 4,  'correct': 2},
        }, days_active=5, response_count=50, badge_ids=['first_step'])
        print("Seeded: sara@gat.sa (day 5, Foundation)")

    # ── 3. Mohammed — Day 15, intermediate, Enhancement phase ──
    if db.query(User).filter_by(email="mohammed@gat.sa").first() is None:
        mohammed = User(name="Mohammed Al-Ghamdi", email="mohammed@gat.sa", password_hash=pw("123456"),
                        diagnostic_completed=True, current_day=15, xp=2850, streak_current=12,
                        streak_longest=15, league="gold", daily_minutes=120,
                        last_active_date=today)
        db.add(mohammed)
        db.commit()
        seed_user_data(mohammed, {
            'verbal_reading':    {'theta': 0.8,  'mastery': 0.72, 'seen': 22, 'correct': 16},
            'verbal_analogy':    {'theta': 0.5,  'mastery': 0.65, 'seen': 18, 'correct': 12},
            'verbal_completion': {'theta': 0.6,  'mastery': 0.68, 'seen': 16, 'correct': 11},
            'verbal_error':      {'theta': 0.3,  'mastery': 0.55, 'seen': 14, 'correct': 8},
            'verbal_oddword':    {'theta': 0.4,  'mastery': 0.60, 'seen': 8,  'correct': 5},
            'quant_arithmetic':  {'theta': 1.2,  'mastery': 0.82, 'seen': 28, 'correct': 23},
            'quant_geometry':    {'theta': 0.4,  'mastery': 0.58, 'seen': 16, 'correct': 9},
            'quant_algebra':     {'theta': 0.9,  'mastery': 0.75, 'seen': 20, 'correct': 15},
            'quant_statistics':  {'theta': 0.6,  'mastery': 0.65, 'seen': 12, 'correct': 8},
        }, days_active=15, response_count=154, badge_ids=['first_step', 'warrior', 'streak_7'])
        print("Seeded: mohammed@gat.sa (day 15, Enhancement)")

    # ── 4. Lujain — Day 25, advanced, Mastery phase ──
    if db.query(User).filter_by(email="lujain@gat.sa").first() is None:
        lujain = User(name="Lujain Al-Harbi", email="lujain@gat.sa", password_hash=pw("123456"),
                      diagnostic_completed=True, current_day=25, xp=8200, streak_current=25,
                      streak_longest=25, league="diamond", daily_minutes=120,
                      last_active_date=today)
        db.add(lujain)
        db.commit()
        seed_user_data(lujain, {
            'verbal_reading':    {'theta': 1.5,  'mastery': 0.88, 'seen': 35, 'correct': 31},
            'verbal_analogy':    {'theta': 1.2,  'mastery': 0.82, 'seen': 28, 'correct': 23},
            'verbal_completion': {'theta': 1.3,  'mastery': 0.85, 'seen': 25, 'correct': 21},
            'verbal_error':      {'theta': 0.9,  'mastery': 0.78, 'seen': 22, 'correct': 17},
            'verbal_oddword':    {'theta': 1.0,  'mastery': 0.80, 'seen': 12, 'correct': 10},
            'quant_arithmetic':  {'theta': 2.0,  'mastery': 0.92, 'seen': 45, 'correct': 41},
            'quant_geometry':    {'theta': 1.4,  'mastery': 0.84, 'seen': 30, 'correct': 25},
            'quant_algebra':     {'theta': 1.8,  'mastery': 0.90, 'seen': 35, 'correct': 32},
            'quant_statistics':  {'theta': 1.1,  'mastery': 0.80, 'seen': 18, 'correct': 14},
        }, days_active=25, response_count=250,
           badge_ids=['first_step', 'warrior', 'streak_7', 'streak_14', 'perfect_quiz'])
        print("Seeded: lujain@gat.sa (day 25, Mastery)")

    # ── 5. Admin ──
    if db.query(User).filter_by(email="admin@gat.sa").first() is None:
        db.add(User(name="System Admin", email="admin@gat.sa", password_hash=pw("admin123"),
                    is_admin=True, diagnostic_completed=True, current_day=1))
        db.commit()
        # Admin needs abilities for /api/me to work
        for skill_id in skills_list:
            db.add(UserAbility(user_id=db.query(User).filter_by(email="admin@gat.sa").first().id,
                               skill_id=skill_id, theta=0.0, mastery=0.3, questions_seen=0, correct_count=0))
        db.commit()
        print("Seeded: admin@gat.sa (admin)")

    # ── Seed some feedback from demo users ──
    if db.query(Feedback).count() == 0:
        demo_users = db.query(User).filter(User.is_admin == False, User.diagnostic_completed == True).all()
        feedback_data = [
            (4, "The platform is excellent and questions are diverse", "session_complete"),
            (5, "The explanations are very clear", "session_complete"),
            (3, None, "diagnostic"),
            (5, "The personalized plan helped me a lot", "phase_change"),
            (4, "I hope more questions are added", "session_complete"),
            (5, "The points system motivates me to continue", "streak"),
            (4, None, "session_complete"),
            (3, "Some questions need longer explanations", "session_complete"),
        ]
        for i, (rating, comment, trigger) in enumerate(feedback_data):
            if demo_users:
                user = demo_users[i % len(demo_users)]
                fb = Feedback(user_id=user.id, rating=rating, comment=comment, trigger=trigger, page="/practice")
                fb.created_at = datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 20))
                db.add(fb)
        db.commit()
        print(f"Seeded {len(feedback_data)} feedback entries")

    # ── App Config ───────────────────────────────────────────────────────
    from models import AppConfig
    if db.query(AppConfig).get("mock_max_attempts") is None:
        db.add(AppConfig(key="mock_max_attempts", value="2"))
        db.commit()
        print("Seeded config: mock_max_attempts=2")

    db.close()

if __name__ == "__main__":
    seed_all()
