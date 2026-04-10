from dotenv import load_dotenv
load_dotenv()

import json, math, datetime, os
from uuid import uuid4
from fastapi import FastAPI, Depends, HTTPException, Query, Request, Header
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Any, Optional, List
from jose import jwt

from auth_utils import (
    auth_rate_limiter,
    get_client_ip,
    get_secret_key,
    normalize_email,
    resolve_cors_configuration,
    verify_password,
)
from database import get_db, engine, Base
from models import User, Skill, Question, UserAbility, UserResponse, StudyPlan, Badge, UserBadge, Feedback, MockAttempt, AppConfig
from adaptive import (
    SCHEDULED_MOCK_DAYS,
    update_ability,
    select_next_question,
    select_diagnostic_question,
    generate_study_plan,
    predict_score,
    recalculate_all_question_stats,
    calibrate_question_difficulties,
    maybe_auto_calibrate,
)
from password_reset import (
    get_password_reset_support_email,
    get_password_reset_ttl_minutes,
    issue_password_reset_token_for_email,
    password_reset_preview_enabled,
    reset_password_with_token,
)
from practice_support import (
    build_practice_adaptive_payload,
    build_practice_assistment_payload,
)
from question_content import (
    CONTENT_FORMAT_MARKDOWN_MATH,
    HIGH_PRIORITY_QUANT_SKILLS,
    activation_blockers,
    clean_optional_text,
    collect_question_quality_metadata,
    collect_question_content_issues,
    deserialize_comparison_columns,
    ensure_question_content_columns,
    extract_comparison_columns,
    get_missing_review_ratings,
    normalize_math_markdown,
    ratings_complete,
    recommended_action_for_classification,
    serialize_comparison_columns,
    suggest_figure_alt,
    suggest_table_caption,
    validate_comparison_columns,
    validate_content_format,
)
from question_visuals import (
    deserialize_table_payload,
    ensure_question_visual_columns,
    prepare_question_visual_fields,
)
from seed import seed_all
from sync_question_bank import generate_admin_source_key
from user_management import create_user, find_user_by_email

def ensure_feedback_columns(eng):
    """Add new feedback columns if they don't exist (safe for production)."""
    from sqlalchemy import inspect, text
    inspector = inspect(eng)
    if "feedback" not in inspector.get_table_names():
        return
    existing = {c["name"] for c in inspector.get_columns("feedback")}
    migrations = []
    if "category" not in existing:
        migrations.append("ALTER TABLE feedback ADD COLUMN category TEXT")
    if "priority" not in existing:
        migrations.append("ALTER TABLE feedback ADD COLUMN priority TEXT")
    if "question_code" not in existing:
        migrations.append("ALTER TABLE feedback ADD COLUMN question_code TEXT")
    if "status" not in existing:
        migrations.append("ALTER TABLE feedback ADD COLUMN status TEXT DEFAULT 'open'")
    if "admin_response" not in existing:
        migrations.append("ALTER TABLE feedback ADD COLUMN admin_response TEXT")
    if "responded_at" not in existing:
        migrations.append("ALTER TABLE feedback ADD COLUMN responded_at TIMESTAMP")
    if migrations:
        with eng.begin() as conn:
            for stmt in migrations:
                conn.execute(text(stmt))

# ── App setup ────────────────────────────────────────────────────────────────
SECRET = get_secret_key()
CORS_ORIGINS, CORS_ALLOW_CREDENTIALS = resolve_cors_configuration()

Base.metadata.create_all(bind=engine)
ensure_question_visual_columns(engine)
ensure_question_content_columns(engine)
ensure_feedback_columns(engine)
seed_all()

app = FastAPI(title="Qudra Academy — GAT Prep")
app.add_middleware(GZipMiddleware, minimum_size=500)
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=CORS_ALLOW_CREDENTIALS,
    allow_methods=["*"],
    allow_headers=["*"],
)

FRONTEND_DIR: Optional[str] = None


def api_root_payload() -> dict[str, str]:
    return {"message": "Qudra Academy API", "status": "running"}


def frontend_index_response() -> Optional[FileResponse]:
    if not FRONTEND_DIR:
        return None

    index_file = os.path.join(FRONTEND_DIR, "index.html")
    if not os.path.exists(index_file):
        return None

    response = FileResponse(index_file)
    response.headers["Cache-Control"] = "no-cache"
    return response


@app.get("/")
async def root():
    return frontend_index_response() or api_root_payload()


@app.get("/api")
async def api_root():
    return api_root_payload()

def update_question_stats(q, is_correct: bool, time_spent: int):
    """Update question-level analytics after each answer."""
    q.times_answered = (q.times_answered or 0) + 1
    if is_correct:
        q.times_correct = (q.times_correct or 0) + 1
    prev_avg = q.avg_time_seconds or 0.0
    q.avg_time_seconds = (prev_avg * (q.times_answered - 1) + time_spent) / q.times_answered


def get_plan_day(db: Session, user_id: int, day_number: int) -> Optional[StudyPlan]:
    return db.query(StudyPlan).filter_by(user_id=user_id, day_number=day_number).first()


def sync_current_day_plan(db: Session, user: User) -> Optional[StudyPlan]:
    plan = get_plan_day(db, user.id, user.current_day)
    if not plan:
        return None

    # Rest day is automatically considered complete when the learner reaches it.
    if plan.is_rest_day and not plan.completed:
        plan.completed_questions = max(plan.completed_questions, plan.target_questions)
        plan.completed = True
        db.commit()
        db.refresh(plan)

    return plan

# ── Schemas ──────────────────────────────────────────────────────────────────
class RegisterReq(BaseModel):
    name: str
    email: str
    password: str

class LoginReq(BaseModel):
    email: str
    password: str

class ForgotPasswordReq(BaseModel):
    email: str

class ResetPasswordReq(BaseModel):
    email: str
    reset_token: str
    new_password: str

class AnswerReq(BaseModel):
    question_id: int
    selected_option: str
    time_spent_seconds: int = 0

class SettingsReq(BaseModel):
    daily_minutes: int

# ── Auth helpers ─────────────────────────────────────────────────────────────
def create_token(user_id: int):
    return jwt.encode({"sub": str(user_id), "exp": datetime.datetime.utcnow() + datetime.timedelta(days=7)}, SECRET)

def get_current_user(db: Session = Depends(get_db), token: str = None):
    return None  # simplified for MVP; see auth endpoint

def get_user(authorization: str = Header(None), db: Session = Depends(get_db)):
    if not authorization:
        raise HTTPException(401, "Login required")
    try:
        token = authorization.replace("Bearer ", "")
        payload = jwt.decode(token, SECRET, algorithms=["HS256"], options={"verify_exp": True})
        user = db.query(User).get(int(payload["sub"]))
        if not user:
            raise HTTPException(401, "User not found")
        return user
    except jwt.ExpiredSignatureError:
        raise HTTPException(401, "Token expired")
    except (jwt.JWTError, ValueError, KeyError):
        raise HTTPException(401, "Invalid token")

# ── Auth endpoints ───────────────────────────────────────────────────────────
@app.post("/api/auth/register")
def register(req: RegisterReq, request: Request, db: Session = Depends(get_db)):
    client_ip = get_client_ip(request)
    retry_after = auth_rate_limiter.register_retry_after(client_ip)
    if retry_after is not None:
        raise HTTPException(
            429,
            "Too many registration attempts. Please try again later.",
            headers={"Retry-After": str(retry_after)},
        )

    try:
        user = create_user(
            db,
            name=req.name,
            email=req.email,
            password=req.password,
        )
    except ValueError as exc:
        raise HTTPException(400, str(exc)) from exc
    return {"token": create_token(user.id), "user": {"id": user.id, "name": user.name}}

@app.post("/api/auth/login")
def login(req: LoginReq, request: Request, db: Session = Depends(get_db)):
    email = normalize_email(req.email)
    client_ip = get_client_ip(request)
    retry_after = auth_rate_limiter.login_retry_after(client_ip, email)
    if retry_after is not None:
        raise HTTPException(
            429,
            "Too many failed login attempts. Please try again later.",
            headers={"Retry-After": str(retry_after)},
        )

    user = find_user_by_email(db, email)
    if not user or not verify_password(req.password, user.password_hash):
        auth_rate_limiter.record_login_failure(client_ip, email)
        raise HTTPException(401, "Invalid login credentials")
    auth_rate_limiter.clear_login_failures(client_ip, email)
    return {"token": create_token(user.id), "user": {"id": user.id, "name": user.name}}


@app.post("/api/auth/forgot-password")
def forgot_password(req: ForgotPasswordReq, db: Session = Depends(get_db)):
    from email_service import is_email_enabled, send_password_reset_email

    email = normalize_email(req.email)
    preview_enabled = password_reset_preview_enabled()
    support_email = get_password_reset_support_email()
    email_enabled = is_email_enabled()
    reset_token_preview = None
    ttl = get_password_reset_ttl_minutes()

    # Generate token if we can deliver it (preview mode or email enabled)
    if preview_enabled or email_enabled:
        token = issue_password_reset_token_for_email(db, email)
        if preview_enabled:
            reset_token_preview = token
        if email_enabled and token:
            send_password_reset_email(to=email, reset_code=token, expires_minutes=ttl)

    if preview_enabled:
        message = "If an account exists for that email, use the one-time reset code below to choose a new password."
    elif email_enabled:
        message = "If an account exists for that email, a reset code has been sent to your inbox."
    elif support_email:
        message = f"If an account exists for that email, contact {support_email} for a one-time reset code."
    else:
        message = "If an account exists for that email, contact the academy team for a one-time reset code."

    return {
        "message": message,
        "reset_token_preview": reset_token_preview,
        "expires_in_minutes": ttl if preview_enabled else None,
        "requires_support": not preview_enabled and not email_enabled,
        "support_email": support_email,
    }


@app.post("/api/auth/reset-password")
def reset_password(req: ResetPasswordReq, db: Session = Depends(get_db)):
    try:
        user = reset_password_with_token(
            db,
            email=req.email,
            reset_token=req.reset_token,
            new_password=req.new_password,
        )
    except ValueError as exc:
        raise HTTPException(400, str(exc)) from exc

    return {
        "message": "Password updated successfully. Sign in with your new password.",
        "user": {"id": user.id, "name": user.name},
    }

# ── User profile ─────────────────────────────────────────────────────────────
@app.get("/api/me")
def get_me(user: User = Depends(get_user), db: Session = Depends(get_db)):
    sync_current_day_plan(db, user)
    abilities = db.query(UserAbility).filter_by(user_id=user.id).all()
    skills = db.query(Skill).all()
    skill_map = {s.id: s for s in skills}
    score = predict_score(db, user.id)

    # Check/update streak
    today = datetime.date.today().isoformat()
    streak_active = user.last_active_date == today or user.last_active_date == (datetime.date.today() - datetime.timedelta(days=1)).isoformat()

    return {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "daily_minutes": user.daily_minutes,
        "current_day": user.current_day,
        "diagnostic_completed": user.diagnostic_completed,
        "xp": user.xp,
        "streak": user.streak_current,
        "streak_longest": user.streak_longest,
        "league": user.league,
        "is_admin": user.is_admin,
        "mock_attempts": user.mock_attempts,
        "mock_score": user.mock_score,
        "mock_max_attempts": get_mock_max(db),
        "streak_freezes": user.streak_freezes or 0,
        "course_started_at": user.course_started_at.isoformat() if user.course_started_at else None,
        "predicted_score": score,
        "abilities": [{
            "skill_id": a.skill_id,
            "name_ar": skill_map[a.skill_id].name_ar if a.skill_id in skill_map else "",
            "section": skill_map[a.skill_id].section if a.skill_id in skill_map else "",
            "icon": skill_map[a.skill_id].icon if a.skill_id in skill_map else "",
            "theta": round(a.theta, 2),
            "mastery": round(a.mastery, 2),
            "questions_seen": a.questions_seen,
            "correct_count": a.correct_count,
        } for a in abilities],
    }

@app.put("/api/me/settings")
def update_settings(req: SettingsReq, user: User = Depends(get_user), db: Session = Depends(get_db)):
    user.daily_minutes = req.daily_minutes
    db.commit()
    if user.diagnostic_completed:
        generate_study_plan(db, user.id, req.daily_minutes)
    return {"ok": True}

# ── Diagnostic ───────────────────────────────────────────────────────────────
@app.post("/api/diagnostic/start")
def start_diagnostic(user: User = Depends(get_user), db: Session = Depends(get_db)):
    if user.diagnostic_completed:
        raise HTTPException(400, "Diagnostic already completed")
    return {"message": "Start diagnostic test", "total_questions": 9}

@app.get("/api/diagnostic/next")
def diagnostic_next(user: User = Depends(get_user), db: Session = Depends(get_db)):
    # Get answered question ids in diagnostic
    answered = db.query(UserResponse).filter_by(user_id=user.id, session_type="diagnostic").all()
    answered_ids = [r.question_id for r in answered]

    if len(answered_ids) >= 9:
        return {"done": True, "total_answered": len(answered_ids)}

    # One question per skill — find which skills are not yet covered
    answered_skills = set()
    for r in answered:
        qq = db.query(Question).get(r.question_id)
        if qq:
            answered_skills.add(qq.skill_id)

    all_skills = [s.id for s in db.query(Skill).all()]
    remaining_skills = [s for s in all_skills if s not in answered_skills]

    if not remaining_skills:
        return {"done": True, "total_answered": len(answered_ids)}

    # Pick next skill randomly (not always the same order)
    import random
    random.shuffle(remaining_skills)
    next_skill = remaining_skills[0]
    q = db.query(Question).filter(
        Question.skill_id == next_skill,
        Question.status == "active",
        ~Question.id.in_(answered_ids) if answered_ids else True
    ).order_by(Question.difficulty).all()

    # Pick a question near medium difficulty with some randomness
    if not q:
        return {"done": True, "total_answered": len(answered_ids)}
    # Sort by distance from 0.5, then pick randomly from the 5 closest
    candidates = sorted(q, key=lambda x: abs(x.difficulty - 0.5))[:5]
    q = random.choice(candidates)

    return {
        "done": False,
        "progress": len(answered_ids),
        "total": 9,
        "question": format_question(q),
    }

@app.post("/api/diagnostic/answer")
def diagnostic_answer(req: AnswerReq, user: User = Depends(get_user), db: Session = Depends(get_db)):
    if user.diagnostic_completed:
        raise HTTPException(400, "Diagnostic already completed")
    q = db.query(Question).get(req.question_id)
    if not q:
        raise HTTPException(404, "Question not found")

    is_correct = req.selected_option == q.correct_option
    resp = UserResponse(user_id=user.id, question_id=q.id, session_type="diagnostic",
                        selected_option=req.selected_option, is_correct=is_correct,
                        time_spent_seconds=req.time_spent_seconds)
    db.add(resp)
    update_ability(db, user.id, q.skill_id, is_correct, q.difficulty, q.discrimination)
    update_question_stats(q, is_correct, req.time_spent_seconds)

    # Award XP
    user.xp += 10 if is_correct else 5
    db.commit()

    return {
        "is_correct": is_correct,
        "correct_option": q.correct_option,
        "explanation_ar": get_render_content(q)["explanation_ar"],
        "solution_steps_ar": get_render_content(q)["solution_steps_ar"],
        "content_format": get_render_content(q)["content_format"],
        "comparison_columns": get_render_content(q)["comparison_columns"],
        **serialize_question_visuals(q),
    }

@app.post("/api/diagnostic/complete")
def complete_diagnostic(user: User = Depends(get_user), db: Session = Depends(get_db)):
    user.diagnostic_completed = True
    user.current_day = 1
    user.course_started_at = datetime.datetime.utcnow()
    db.commit()
    generate_study_plan(db, user.id, user.daily_minutes)
    score = predict_score(db, user.id)
    return {"message": "Diagnostic completed!", "predicted_score": score}

# ── Study Plan ───────────────────────────────────────────────────────────────
@app.get("/api/study-plan")
def get_study_plan(user: User = Depends(get_user), db: Session = Depends(get_db)):
    sync_current_day_plan(db, user)
    plan = db.query(StudyPlan).filter_by(user_id=user.id).order_by(StudyPlan.day_number).all()
    skills = {s.id: s for s in db.query(Skill).all()}
    return [{
        "day": p.day_number,
        "phase": p.phase,
        "focus_skills": [{"id": sid, "name_ar": skills[sid].name_ar if sid in skills else sid} for sid in json.loads(p.focus_skills)],
        "target_questions": p.target_questions,
        "completed_questions": p.completed_questions,
        "is_mock_day": p.is_mock_day,
        "is_rest_day": p.is_rest_day,
        "completed": p.completed,
        "is_today": p.day_number == user.current_day,
    } for p in plan]

@app.get("/api/study-plan/today")
def get_today(user: User = Depends(get_user), db: Session = Depends(get_db)):
    plan = sync_current_day_plan(db, user)
    if not plan:
        return {"day": user.current_day, "phase": "", "focus_skills": [], "target_questions": 0,
                "completed_questions": 0, "is_mock_day": False, "is_rest_day": False, "remaining": 0,
                "message": "No plan for today"}
    skills = {s.id: s for s in db.query(Skill).all()}
    return {
        "day": plan.day_number,
        "phase": plan.phase,
        "focus_skills": [{"id": sid, "name_ar": skills[sid].name_ar if sid in skills else sid} for sid in json.loads(plan.focus_skills)],
        "target_questions": plan.target_questions,
        "completed_questions": plan.completed_questions,
        "is_mock_day": plan.is_mock_day,
        "is_rest_day": plan.is_rest_day,
        "remaining": max(0, plan.target_questions - plan.completed_questions),
    }

# ── Practice Session ─────────────────────────────────────────────────────────
@app.get("/api/practice/next")
def practice_next(user: User = Depends(get_user), db: Session = Depends(get_db)):
    plan = sync_current_day_plan(db, user)
    if plan and plan.is_mock_day and not plan.completed:
        raise HTTPException(400, "Today's session is a mock exam")

    # Get today's answered questions
    today_start = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
    today_responses = db.query(UserResponse).filter(
        UserResponse.user_id == user.id,
        UserResponse.session_type == "drill",
        UserResponse.created_at >= today_start
    ).all()
    excluded = [r.question_id for r in today_responses]

    q = select_next_question(db, user.id, "drill", excluded, current_day=user.current_day)
    if not q:
        return {"done": True, "message": "You have completed all available questions!"}

    skill = db.query(Skill).filter(Skill.id == q.skill_id).first()
    ability = db.query(UserAbility).filter(
        UserAbility.user_id == user.id,
        UserAbility.skill_id == q.skill_id,
    ).first()

    return {
        "done": False,
        "question": format_question(q),
        "adaptive": build_practice_adaptive_payload(q, skill, ability),
        "assistment": build_practice_assistment_payload(q),
    }

@app.post("/api/practice/answer")
def practice_answer(req: AnswerReq, user: User = Depends(get_user), db: Session = Depends(get_db)):
    plan = sync_current_day_plan(db, user)
    if plan and plan.is_mock_day and not plan.completed:
        raise HTTPException(400, "Today's session is a mock exam")

    q = db.query(Question).get(req.question_id)
    if not q:
        raise HTTPException(404, "Question not found")

    is_correct = req.selected_option == q.correct_option

    resp = UserResponse(user_id=user.id, question_id=q.id, session_type="drill",
                        selected_option=req.selected_option, is_correct=is_correct,
                        time_spent_seconds=req.time_spent_seconds)
    db.add(resp)
    update_ability(db, user.id, q.skill_id, is_correct, q.difficulty, q.discrimination)
    update_question_stats(q, is_correct, req.time_spent_seconds)
    maybe_auto_calibrate(db)

    # Update plan progress
    if plan:
        plan.completed_questions += 1
        if plan.completed_questions >= plan.target_questions:
            plan.completed = True

    # XP + streak
    user.xp += 10 if is_correct else 5
    today = datetime.date.today().isoformat()
    if user.last_active_date != today:
        yesterday = (datetime.date.today() - datetime.timedelta(days=1)).isoformat()
        if user.last_active_date == yesterday:
            user.streak_current += 1
        else:
            user.streak_current = 1
        user.last_active_date = today
        user.streak_longest = max(user.streak_longest, user.streak_current)

    db.commit()

    # Check badges
    total_questions = db.query(UserResponse).filter_by(user_id=user.id).count()
    check_badges(db, user.id, total_questions, user.streak_current)

    return {
        "is_correct": is_correct,
        "correct_option": q.correct_option,
        "explanation_ar": get_render_content(q)["explanation_ar"],
        "solution_steps_ar": get_render_content(q)["solution_steps_ar"],
        "content_format": get_render_content(q)["content_format"],
        "comparison_columns": get_render_content(q)["comparison_columns"],
        **serialize_question_visuals(q),
        "xp_earned": 10 if is_correct else 5,
    }

# ── Advance day ──────────────────────────────────────────────────────────────
@app.post("/api/advance-day")
def advance_day(user: User = Depends(get_user), db: Session = Depends(get_db)):
    if user.current_day >= 30:
        sync_current_day_plan(db, user)
        return {"current_day": user.current_day}
    plan = sync_current_day_plan(db, user)
    if plan and not plan.is_rest_day and plan.completed_questions < plan.target_questions:
        raise HTTPException(400, "Complete today's questions first")
    user.current_day += 1
    db.commit()
    sync_current_day_plan(db, user)
    return {"current_day": user.current_day}

# ── Analytics ────────────────────────────────────────────────────────────────
@app.get("/api/analytics")
def analytics(user: User = Depends(get_user), db: Session = Depends(get_db)):
    responses = db.query(UserResponse).filter_by(user_id=user.id).order_by(UserResponse.created_at).all()

    # Daily accuracy trend
    daily = {}
    for r in responses:
        day = r.created_at.strftime("%Y-%m-%d") if r.created_at else "unknown"
        if day not in daily:
            daily[day] = {"correct": 0, "total": 0}
        daily[day]["total"] += 1
        if r.is_correct:
            daily[day]["correct"] += 1

    trend = [{"date": d, "accuracy": round(v["correct"] / v["total"], 2), "total": v["total"]}
             for d, v in sorted(daily.items())]

    # Per skill breakdown
    skills = {s.id: s for s in db.query(Skill).all()}
    question_ids = list({r.question_id for r in responses})
    questions_map = {q.id: q for q in db.query(Question).filter(Question.id.in_(question_ids)).all()} if question_ids else {}
    skill_stats = {}
    for r in responses:
        q = questions_map.get(r.question_id)
        if q and q.skill_id not in skill_stats:
            skill_stats[q.skill_id] = {"correct": 0, "total": 0}
        if q:
            skill_stats[q.skill_id]["total"] += 1
            if r.is_correct:
                skill_stats[q.skill_id]["correct"] += 1

    return {
        "total_questions": len(responses),
        "total_correct": sum(1 for r in responses if r.is_correct),
        "accuracy": round(sum(1 for r in responses if r.is_correct) / max(1, len(responses)), 2),
        "daily_trend": trend,
        "skill_breakdown": [{
            "skill_id": sid,
            "name_ar": skills[sid].name_ar if sid in skills else sid,
            "section": skills[sid].section if sid in skills else "",
            "icon": skills[sid].icon if sid in skills else "",
            "correct": v["correct"],
            "total": v["total"],
            "accuracy": round(v["correct"] / max(1, v["total"]), 2),
        } for sid, v in skill_stats.items()],
        "predicted_score": predict_score(db, user.id),
    }

# ── Gamification ─────────────────────────────────────────────────────────────
@app.get("/api/badges")
def get_badges(user: User = Depends(get_user), db: Session = Depends(get_db)):
    all_badges = db.query(Badge).all()
    earned = {ub.badge_id for ub in db.query(UserBadge).filter_by(user_id=user.id).all()}
    return [{
        "id": b.id, "name_ar": b.name_ar, "description_ar": b.description_ar,
        "icon": b.icon, "earned": b.id in earned,
    } for b in all_badges]

# ── Skills list ──────────────────────────────────────────────────────────────
@app.get("/api/skills")
def get_skills(db: Session = Depends(get_db)):
    return [{"id": s.id, "section": s.section, "name_ar": s.name_ar, "name_en": s.name_en,
             "exam_weight": s.exam_weight, "icon": s.icon} for s in db.query(Skill).all()]

# ── Helpers ──────────────────────────────────────────────────────────────────
def parse_solution_steps(raw_value: Optional[str]):
    if not raw_value:
        return None
    try:
        return json.loads(raw_value)
    except json.JSONDecodeError:
        return [raw_value]


def get_render_content(q: Question) -> dict[str, Any]:
    content_format = validate_content_format(getattr(q, "content_format", None))
    text_ar = q.text_ar
    passage_ar = q.passage_ar
    options = {
        "a": q.option_a,
        "b": q.option_b,
        "c": q.option_c,
        "d": q.option_d,
    }
    explanation_ar = q.explanation_ar
    solution_steps_ar = parse_solution_steps(q.solution_steps_ar)

    comparison_columns = getattr(q, "comparison_columns", None)
    if isinstance(comparison_columns, str):
        try:
            comparison_columns = deserialize_comparison_columns(comparison_columns)
        except ValueError:
            comparison_columns = None

    if not comparison_columns and q.question_type == "comparison":
        text_ar, comparison_columns = extract_comparison_columns(text_ar)

    if content_format != CONTENT_FORMAT_MARKDOWN_MATH and q.skill_id in HIGH_PRIORITY_QUANT_SKILLS:
        normalized_values = {
            "text_ar": normalize_math_markdown(text_ar) or text_ar,
            "passage_ar": normalize_math_markdown(passage_ar),
            "option_a": normalize_math_markdown(options["a"]) or options["a"],
            "option_b": normalize_math_markdown(options["b"]) or options["b"],
            "option_c": normalize_math_markdown(options["c"]) or options["c"],
            "option_d": normalize_math_markdown(options["d"]) or options["d"],
            "explanation_ar": normalize_math_markdown(explanation_ar),
            "solution_steps_ar": [
                normalize_math_markdown(step) or step
                for step in (solution_steps_ar or [])
            ] if solution_steps_ar else None,
        }
        if any(
            normalized_values[key] != value
            for key, value in (
                ("text_ar", text_ar),
                ("passage_ar", passage_ar),
                ("option_a", options["a"]),
                ("option_b", options["b"]),
                ("option_c", options["c"]),
                ("option_d", options["d"]),
                ("explanation_ar", explanation_ar),
                ("solution_steps_ar", solution_steps_ar),
            )
        ):
            content_format = CONTENT_FORMAT_MARKDOWN_MATH
            text_ar = normalized_values["text_ar"]
            passage_ar = normalized_values["passage_ar"]
            options = {
                "a": normalized_values["option_a"],
                "b": normalized_values["option_b"],
                "c": normalized_values["option_c"],
                "d": normalized_values["option_d"],
            }
            explanation_ar = normalized_values["explanation_ar"]
            solution_steps_ar = normalized_values["solution_steps_ar"]

    figure_alt = clean_optional_text(getattr(q, "figure_alt", None))
    table_caption = clean_optional_text(getattr(q, "table_caption", None))

    if q.figure_svg and not figure_alt:
        figure_alt = suggest_figure_alt(q.skill_id, q.question_type, text_ar or "")
    if q.table_ar and not table_caption:
        table_caption = suggest_table_caption(q.skill_id, q.question_type)

    return {
        "content_format": content_format,
        "text_ar": text_ar,
        "passage_ar": passage_ar,
        "options": options,
        "explanation_ar": explanation_ar,
        "solution_steps_ar": solution_steps_ar,
        "comparison_columns": comparison_columns,
        "figure_alt": figure_alt,
        "table_caption": table_caption,
    }


def serialize_question_visuals(q: Question):
    render_content = get_render_content(q)
    return {
        "figure_svg": q.figure_svg,
        "table_ar": deserialize_table_payload(q.table_ar),
        "figure_alt": render_content["figure_alt"],
        "table_caption": render_content["table_caption"],
    }


def build_question_review_payload(q: Question, skill: Optional[Skill] = None):
    render_content = get_render_content(q)
    payload = {
        "question_id": q.id,
        "text_ar": render_content["text_ar"],
        "passage_ar": render_content["passage_ar"],
        "options": [
            {"key": "a", "text_ar": render_content["options"]["a"]},
            {"key": "b", "text_ar": render_content["options"]["b"]},
            {"key": "c", "text_ar": render_content["options"]["c"]},
            {"key": "d", "text_ar": render_content["options"]["d"]},
        ],
        "selected_option": None,
        "correct_option": q.correct_option,
        "is_correct": None,
        "time_spent_seconds": 0,
        "explanation_ar": render_content["explanation_ar"],
        "solution_steps_ar": render_content["solution_steps_ar"],
        "skill_id": q.skill_id,
        "skill_name_ar": skill.name_ar if skill else "",
        "section": skill.section if skill else "",
        "content_format": render_content["content_format"],
        "comparison_columns": render_content["comparison_columns"],
    }
    payload.update(serialize_question_visuals(q))
    return payload


def format_question(q: Question):
    render_content = get_render_content(q)
    payload = {
        "id": q.id,
        "skill_id": q.skill_id,
        "question_type": q.question_type,
        "difficulty": q.difficulty,
        "text_ar": render_content["text_ar"],
        "passage_ar": render_content["passage_ar"],
        "options": [
            {"key": "a", "label": "A", "text_ar": render_content["options"]["a"]},
            {"key": "b", "label": "B", "text_ar": render_content["options"]["b"]},
            {"key": "c", "label": "C", "text_ar": render_content["options"]["c"]},
            {"key": "d", "label": "D", "text_ar": render_content["options"]["d"]},
        ],
        "paper_only": q.paper_only,
        "content_format": render_content["content_format"],
        "comparison_columns": render_content["comparison_columns"],
    }
    payload.update(serialize_question_visuals(q))
    return payload


def compute_question_analytics_flags(q: Question) -> list[str]:
    ta = q.times_answered or 0
    tc = q.times_correct or 0
    accuracy = tc / max(1, ta) if ta > 0 else None
    flags: list[str] = []
    if ta >= 10 and accuracy is not None and accuracy < 0.2:
        flags.append("very_low_accuracy")
    if ta >= 10 and accuracy is not None and accuracy > 0.95:
        flags.append("too_easy")
    if ta >= 10 and (q.discrimination or 0) < 0.1:
        flags.append("low_discrimination")
    return flags


def build_admin_question_payload(q: Question, skills_map: dict[str, Skill]) -> dict[str, Any]:
    render_content = get_render_content(q)
    ta = q.times_answered or 0
    tc = q.times_correct or 0
    issues = collect_question_content_issues(q)
    quality = collect_question_quality_metadata(q, issues)
    analytics_flags = compute_question_analytics_flags(q)

    return {
        "id": q.id,
        "source_key": quality["source_key"],
        "batch_id": quality["batch_id"],
        "generation_prompt_version": quality["generation_prompt_version"],
        "authoring_source": quality["authoring_source"] or "human",
        "variant_group": quality["variant_group"],
        "skill_id": q.skill_id,
        "skill_name_ar": skills_map[q.skill_id].name_ar if q.skill_id in skills_map else q.skill_id,
        "section": skills_map[q.skill_id].section if q.skill_id in skills_map else "",
        "question_type": q.question_type,
        "difficulty": q.difficulty,
        "text_ar": render_content["text_ar"],
        "passage_ar": render_content["passage_ar"],
        "content_format": render_content["content_format"],
        "figure_svg": q.figure_svg,
        "figure_alt": render_content["figure_alt"],
        "table_ar": deserialize_table_payload(q.table_ar),
        "table_caption": render_content["table_caption"],
        "comparison_columns": render_content["comparison_columns"],
        "option_a": render_content["options"]["a"],
        "option_b": render_content["options"]["b"],
        "option_c": render_content["options"]["c"],
        "option_d": render_content["options"]["d"],
        "correct_option": q.correct_option,
        "explanation_ar": render_content["explanation_ar"],
        "solution_steps_ar": render_content["solution_steps_ar"],
        "tags": q.tags or "",
        "stage": q.stage or "general",
        "status": q.status or "active",
        "times_answered": ta,
        "times_correct": tc,
        "accuracy": round(tc / max(1, ta), 2),
        "avg_time_seconds": round(q.avg_time_seconds or 0, 1),
        "discrimination": round(q.discrimination or 0, 3),
        "original_difficulty": round(q.original_difficulty, 3) if q.original_difficulty is not None else None,
        "last_calibrated_at": q.last_calibrated_at.isoformat() if q.last_calibrated_at else None,
        "rating_overall": round(q.rating_overall, 2) if q.rating_overall else None,
        "rating_clarity": q.rating_clarity,
        "rating_cognitive": q.rating_cognitive,
        "rating_distractors": q.rating_distractors,
        "rating_difficulty_align": q.rating_difficulty_align,
        "rating_explanation": q.rating_explanation,
        "rating_fairness": q.rating_fairness,
        "rating_discrimination": q.rating_discrimination,
        "rating_passes_done": q.rating_passes_done or 0,
        "rating_notes": q.rating_notes,
        "ratings_complete": quality["ratings_complete"],
        "missing_review_ratings": quality["missing_review_ratings"],
        "content_classification": quality["content_classification"],
        "recommended_action": quality["recommended_action"],
        "content_issue_counts": quality["content_issue_counts"],
        "analytics_flags": analytics_flags,
        "content_issues": [
            {
                "severity": issue.severity,
                "code": issue.code,
                "field": issue.field,
                "message": issue.message,
            }
            for issue in issues
        ],
    }

def check_badges(db: Session, user_id: int, total_questions: int, streak: int, mock_done: bool = False, mock_score: int = 0):
    earned = {ub.badge_id for ub in db.query(UserBadge).filter_by(user_id=user_id).all()}
    badges = db.query(Badge).all()
    for b in badges:
        if b.id in earned:
            continue
        award = False
        if b.criteria_type == "questions" and total_questions >= b.criteria_value:
            award = True
        elif b.criteria_type == "streak" and streak >= b.criteria_value:
            award = True
        elif b.criteria_type == "mock" and mock_done:
            award = True
        elif b.criteria_type == "score" and mock_score >= b.criteria_value:
            award = True
        if award:
            db.add(UserBadge(user_id=user_id, badge_id=b.id))
    db.commit()

# ── Feedback ─────────────────────────────────────────────────────────────────

class FeedbackReq(BaseModel):
    rating: int
    comment: Optional[str] = None
    trigger: str
    page: Optional[str] = None
    category: Optional[str] = None
    priority: Optional[str] = None
    question_code: Optional[str] = None

VALID_CATEGORIES = {"bug", "feature", "question", "account", "other"}
VALID_PRIORITIES = {"low", "normal", "urgent"}

@app.post("/api/feedback")
def submit_feedback(req: FeedbackReq, user: User = Depends(get_user), db: Session = Depends(get_db)):
    if req.rating < 0 or req.rating > 5:
        raise HTTPException(400, "Rating must be between 0 and 5")
    if req.category and req.category not in VALID_CATEGORIES:
        raise HTTPException(400, f"Invalid category. Must be one of: {', '.join(VALID_CATEGORIES)}")
    if req.priority and req.priority not in VALID_PRIORITIES:
        raise HTTPException(400, f"Invalid priority. Must be one of: {', '.join(VALID_PRIORITIES)}")
    fb = Feedback(
        user_id=user.id, rating=req.rating, comment=req.comment,
        trigger=req.trigger, page=req.page,
        category=req.category, priority=req.priority, question_code=req.question_code,
    )
    db.add(fb)
    db.commit()

    # Send confirmation email if enabled
    from email_service import is_email_enabled, send_ticket_confirmation_email
    if is_email_enabled() and req.category:
        send_ticket_confirmation_email(to=user.email, ticket_id=fb.id, category=req.category)

    return {"message": "Thank you for your feedback!", "ticket_id": fb.id}

@app.get("/api/me/tickets")
def get_my_tickets(user: User = Depends(get_user), db: Session = Depends(get_db)):
    tickets = db.query(Feedback).filter_by(user_id=user.id).order_by(Feedback.created_at.desc()).limit(20).all()
    return [{
        "id": t.id,
        "category": t.category,
        "priority": t.priority,
        "comment": t.comment,
        "question_code": t.question_code,
        "status": t.status or "open",
        "admin_response": t.admin_response,
        "responded_at": t.responded_at.isoformat() if t.responded_at else None,
        "created_at": t.created_at.isoformat() if t.created_at else None,
    } for t in tickets]

# ── Admin ────────────────────────────────────────────────────────────────────

def get_admin(user: User = Depends(get_user)):
    if not user.is_admin:
        raise HTTPException(403, "Access denied")
    return user

@app.get("/api/admin/feedback")
def admin_feedback(days: int = Query(30), trigger: Optional[str] = None, admin: User = Depends(get_admin), db: Session = Depends(get_db)):
    cutoff = datetime.datetime.utcnow() - datetime.timedelta(days=days)
    q = db.query(Feedback).filter(Feedback.created_at >= cutoff)
    if trigger:
        q = q.filter(Feedback.trigger == trigger)
    items = q.order_by(Feedback.created_at.desc()).limit(200).all()
    return [{"id": f.id, "user_id": f.user_id, "rating": f.rating, "comment": f.comment,
             "trigger": f.trigger, "page": f.page, "category": f.category, "priority": f.priority,
             "question_code": f.question_code, "status": f.status or "open",
             "admin_response": f.admin_response, "responded_at": f.responded_at.isoformat() if f.responded_at else None,
             "created_at": f.created_at.isoformat()} for f in items]

@app.get("/api/admin/feedback/analytics")
def admin_feedback_analytics(admin: User = Depends(get_admin), db: Session = Depends(get_db)):
    all_fb = db.query(Feedback).all()
    if not all_fb:
        return {"total": 0, "avg_rating": 0, "distribution": {1:0,2:0,3:0,4:0,5:0}, "by_trigger": {}, "recent_comments": []}
    ratings = [f.rating for f in all_fb]
    dist = {i: ratings.count(i) for i in range(1, 6)}
    by_trigger = {}
    for f in all_fb:
        by_trigger.setdefault(f.trigger, {"count": 0, "total_rating": 0})
        by_trigger[f.trigger]["count"] += 1
        by_trigger[f.trigger]["total_rating"] += f.rating
    for k in by_trigger:
        by_trigger[k]["avg_rating"] = round(by_trigger[k]["total_rating"] / by_trigger[k]["count"], 1)
    recent = [{"rating": f.rating, "comment": f.comment, "trigger": f.trigger, "created_at": f.created_at.isoformat()}
              for f in sorted(all_fb, key=lambda x: x.created_at, reverse=True)[:20] if f.comment]
    return {
        "total": len(all_fb),
        "avg_rating": round(sum(ratings) / len(ratings), 1),
        "distribution": dist,
        "by_trigger": by_trigger,
        "recent_comments": recent,
    }

class AdminTicketResponse(BaseModel):
    status: Optional[str] = None
    admin_response: Optional[str] = None

@app.put("/api/admin/feedback/{ticket_id}")
def admin_respond_ticket(ticket_id: int, req: AdminTicketResponse, admin: User = Depends(get_admin), db: Session = Depends(get_db)):
    fb = db.query(Feedback).get(ticket_id)
    if not fb:
        raise HTTPException(404, "Ticket not found")
    if req.status:
        if req.status not in ("open", "in_review", "resolved"):
            raise HTTPException(400, "Invalid status")
        fb.status = req.status
    if req.admin_response is not None:
        fb.admin_response = req.admin_response
        fb.responded_at = datetime.datetime.utcnow()
    db.commit()
    return {"message": "Ticket updated"}

@app.get("/api/admin/users")
def admin_users(admin: User = Depends(get_admin), db: Session = Depends(get_db)):
    users = db.query(User).filter(User.is_admin == False).all()
    today = datetime.date.today().isoformat()
    active_today = sum(1 for u in users if u.last_active_date == today)
    avg_streak = round(sum(u.streak_current for u in users) / max(1, len(users)), 1)
    avg_day = round(sum(u.current_day for u in users) / max(1, len(users)), 1)
    completed = sum(1 for u in users if u.current_day >= 30)
    return {
        "total_users": len(users),
        "active_today": active_today,
        "avg_streak": avg_streak,
        "avg_day": avg_day,
        "completed_course": completed,
        "mock_taken": sum(1 for u in users if u.mock_attempts > 0),
        "mock_avg_score": round(sum(u.mock_score for u in users if u.mock_attempts > 0) / max(1, sum(1 for u in users if u.mock_attempts > 0)), 1),
        "users": [{"id": u.id, "name": u.name, "email": u.email, "current_day": u.current_day,
                    "xp": u.xp, "streak": u.streak_current, "last_active": u.last_active_date,
                    "mock_attempts": u.mock_attempts, "mock_score": u.mock_score} for u in users[:50]],
    }

# ── Mock Exam (Multi-Attempt) ───────────────────────────────────────────────

MOCK_VERBAL_COUNT = 34
MOCK_QUANT_COUNT = 31
MOCK_VERBAL_MINUTES = 35
MOCK_QUANT_MINUTES = 35

def get_mock_max(db):
    cfg = db.query(AppConfig).get("mock_max_attempts")
    configured = int(cfg.value) if cfg else 2
    return max(configured, len(SCHEDULED_MOCK_DAYS))

class MockAnswerReq(BaseModel):
    question_id: int
    selected_option: str
    time_spent_seconds: int = 0
    attempt_id: int

@app.post("/api/mock/start")
def mock_start(preview: bool = Query(False), user: User = Depends(get_user), db: Session = Depends(get_db)):
    is_preview = preview and user.is_admin
    current_plan = sync_current_day_plan(db, user)
    required_mock_day = bool(current_plan and current_plan.is_mock_day and not current_plan.completed)
    if not is_preview:
        max_attempts = get_mock_max(db)
        if user.mock_attempts >= max_attempts and not required_mock_day:
            raise HTTPException(400, f"Maximum attempts exceeded ({max_attempts})")
        if user.current_day < 25 and not required_mock_day:
            raise HTTPException(400, "Mock exam available from day 25")

    import random
    verbal_skills = [s.id for s in db.query(Skill).filter_by(section="verbal").all()]
    quant_skills = [s.id for s in db.query(Skill).filter_by(section="quantitative").all()]

    # Exclude questions the user has already seen in practice or diagnostic
    practiced_ids = set(r.question_id for r in db.query(UserResponse).filter_by(user_id=user.id).filter(
        UserResponse.session_type.in_(["drill", "diagnostic"])).all())

    # Get unseen questions first — prefer mock-stage, then general, then any
    mock_stages = ["mock", "general"]
    unseen_verbal = [q for q in db.query(Question).filter(
        Question.skill_id.in_(verbal_skills), Question.stage.in_(mock_stages), Question.status == "active"
    ).all() if q.id not in practiced_ids]
    unseen_quant = [q for q in db.query(Question).filter(
        Question.skill_id.in_(quant_skills), Question.stage.in_(mock_stages), Question.status == "active"
    ).all() if q.id not in practiced_ids]
    random.shuffle(unseen_verbal)
    random.shuffle(unseen_quant)

    # If not enough unseen, fill with least-recently-answered questions
    if len(unseen_verbal) < MOCK_VERBAL_COUNT:
        seen_verbal = db.query(Question).filter(
            Question.skill_id.in_(verbal_skills),
            Question.id.in_(practiced_ids),
            Question.status == "active",
        ).all()
        random.shuffle(seen_verbal)
        unseen_verbal += seen_verbal
    if len(unseen_quant) < MOCK_QUANT_COUNT:
        seen_quant = db.query(Question).filter(
            Question.skill_id.in_(quant_skills),
            Question.id.in_(practiced_ids),
            Question.status == "active",
        ).all()
        random.shuffle(seen_quant)
        unseen_quant += seen_quant

    selected_verbal = unseen_verbal[:MOCK_VERBAL_COUNT]
    selected_quant = unseen_quant[:MOCK_QUANT_COUNT]
    question_ids = [q.id for q in selected_verbal] + [q.id for q in selected_quant]

    attempt = MockAttempt(user_id=user.id, attempt_number=user.mock_attempts + 1,
                          total_questions=len(question_ids), is_preview=is_preview)
    db.add(attempt)
    db.commit()
    db.refresh(attempt)

    return {
        "attempt_id": attempt.id,
        "attempt_number": attempt.attempt_number,
        "total_questions": len(question_ids),
        "verbal_count": len(selected_verbal),
        "quant_count": len(selected_quant),
        "verbal_minutes": MOCK_VERBAL_MINUTES,
        "quant_minutes": MOCK_QUANT_MINUTES,
        "question_ids": question_ids,
    }

@app.get("/api/mock/question/{question_id}")
def mock_question(question_id: int, user: User = Depends(get_user), db: Session = Depends(get_db)):
    q = db.query(Question).get(question_id)
    if not q:
        raise HTTPException(404, "Question not found")
    return format_question(q)

@app.post("/api/mock/answer")
def mock_answer(req: MockAnswerReq, user: User = Depends(get_user), db: Session = Depends(get_db)):
    q = db.query(Question).get(req.question_id)
    if not q:
        raise HTTPException(404, "Question not found")
    is_correct = req.selected_option == q.correct_option
    resp = UserResponse(user_id=user.id, question_id=q.id, session_type="mock",
                        attempt_id=req.attempt_id, selected_option=req.selected_option,
                        is_correct=is_correct, time_spent_seconds=req.time_spent_seconds)
    db.add(resp)
    update_question_stats(q, is_correct, req.time_spent_seconds)
    db.commit()
    return {"is_correct": is_correct}

class MockCompleteReq(BaseModel):
    attempt_id: int

@app.post("/api/mock/complete")
def mock_complete(req: MockCompleteReq, user: User = Depends(get_user), db: Session = Depends(get_db)):
    attempt = db.query(MockAttempt).get(req.attempt_id)
    if not attempt or attempt.user_id != user.id:
        raise HTTPException(404, "Attempt not found")
    if attempt.completed_at:
        raise HTTPException(400, "This attempt has already been completed")

    responses = db.query(UserResponse).filter_by(user_id=user.id, attempt_id=attempt.id).all()
    if not responses:
        raise HTTPException(400, "No questions answered")

    total = len(responses)
    correct = sum(1 for r in responses if r.is_correct)
    verbal_correct = verbal_total = quant_correct = quant_total = 0
    for r in responses:
        q = db.query(Question).get(r.question_id)
        if q:
            skill = db.query(Skill).get(q.skill_id)
            if skill and skill.section == "verbal":
                verbal_total += 1
                if r.is_correct: verbal_correct += 1
            else:
                quant_total += 1
                if r.is_correct: quant_correct += 1

    verbal_pct = verbal_correct / max(1, verbal_total)
    quant_pct = quant_correct / max(1, quant_total)
    raw = (verbal_pct * 0.5 + quant_pct * 0.5)
    score = max(40, min(100, int(40 + raw * 55)))

    attempt.score = score
    attempt.correct_count = correct
    attempt.verbal_correct = verbal_correct
    attempt.verbal_total = verbal_total
    attempt.quant_correct = quant_correct
    attempt.quant_total = quant_total
    attempt.completed_at = datetime.datetime.utcnow()

    current_plan = sync_current_day_plan(db, user)
    if current_plan and current_plan.is_mock_day:
        current_plan.completed_questions = max(current_plan.completed_questions, current_plan.target_questions)
        current_plan.completed = True

    if not attempt.is_preview:
        user.mock_attempts = (user.mock_attempts or 0) + 1
        if score > (user.mock_score or 0):
            user.mock_score = score
        user.xp = (user.xp or 0) + correct * 10 + (total - correct) * 5
    db.commit()

    if not attempt.is_preview:
        total_all = db.query(UserResponse).filter_by(user_id=user.id).count()
        check_badges(db, user.id, total_all, user.streak_current, mock_done=True, mock_score=score)

    return {
        "attempt_id": attempt.id,
        "attempt_number": attempt.attempt_number,
        "score": score, "total": total, "correct": correct,
        "verbal_correct": verbal_correct, "verbal_total": verbal_total,
        "quant_correct": quant_correct, "quant_total": quant_total,
        "verbal_pct": round(verbal_pct, 2), "quant_pct": round(quant_pct, 2),
    }

@app.get("/api/mock/attempts")
def mock_attempts(user: User = Depends(get_user), db: Session = Depends(get_db)):
    attempts = db.query(MockAttempt).filter_by(user_id=user.id, is_preview=False).filter(MockAttempt.completed_at != None).order_by(MockAttempt.attempt_number).all()
    return [{
        "id": a.id, "attempt_number": a.attempt_number, "score": a.score,
        "total": a.total_questions, "correct": a.correct_count,
        "verbal_correct": a.verbal_correct, "verbal_total": a.verbal_total,
        "quant_correct": a.quant_correct, "quant_total": a.quant_total,
        "verbal_pct": round(a.verbal_correct / max(1, a.verbal_total), 2),
        "quant_pct": round(a.quant_correct / max(1, a.quant_total), 2),
        "completed_at": a.completed_at.isoformat() if a.completed_at else None,
    } for a in attempts]

@app.get("/api/mock/attempts/{attempt_id}/status")
def mock_attempt_status(attempt_id: int, user: User = Depends(get_user), db: Session = Depends(get_db)):
    attempt = db.query(MockAttempt).get(attempt_id)
    if not attempt or attempt.user_id != user.id:
        raise HTTPException(404, "Attempt not found")
    answers_count = db.query(UserResponse).filter_by(attempt_id=attempt.id).count()
    return {
        "attempt_id": attempt.id,
        "completed": attempt.completed_at is not None,
        "answers_submitted": answers_count,
        "total_questions": attempt.total_questions,
    }

@app.get("/api/mock/attempts/{attempt_id}")
def mock_attempt_detail(attempt_id: int, user: User = Depends(get_user), db: Session = Depends(get_db)):
    attempt = db.query(MockAttempt).get(attempt_id)
    if not attempt or (attempt.user_id != user.id and not user.is_admin):
        raise HTTPException(404, "Attempt not found")

    responses = db.query(UserResponse).filter_by(attempt_id=attempt.id).order_by(UserResponse.id).all()
    skills_map = {s.id: s for s in db.query(Skill).all()}
    q_ids = list({r.question_id for r in responses})
    questions_map = {q.id: q for q in db.query(Question).filter(Question.id.in_(q_ids)).all()} if q_ids else {}

    questions_detail = []
    skill_stats = {}
    for r in responses:
        q = questions_map.get(r.question_id)
        if not q:
            continue
        skill = skills_map.get(q.skill_id)
        question_payload = build_question_review_payload(q, skill)
        question_payload.update({
            "selected_option": r.selected_option,
            "correct_option": q.correct_option,
            "is_correct": r.is_correct,
            "time_spent_seconds": r.time_spent_seconds,
        })
        questions_detail.append(question_payload)
        if q.skill_id not in skill_stats:
            skill_stats[q.skill_id] = {"skill_id": q.skill_id, "skill_name_ar": skill.name_ar if skill else "", "correct": 0, "total": 0}
        skill_stats[q.skill_id]["total"] += 1
        if r.is_correct:
            skill_stats[q.skill_id]["correct"] += 1

    return {
        "attempt_number": attempt.attempt_number, "score": attempt.score,
        "total": attempt.total_questions, "correct": attempt.correct_count,
        "verbal_correct": attempt.verbal_correct, "verbal_total": attempt.verbal_total,
        "quant_correct": attempt.quant_correct, "quant_total": attempt.quant_total,
        "completed_at": attempt.completed_at.isoformat() if attempt.completed_at else None,
        "questions": questions_detail,
        "skill_breakdown": [{"skill_id": s["skill_id"], "skill_name_ar": s["skill_name_ar"],
                             "correct": s["correct"], "total": s["total"],
                             "pct": round(s["correct"] / max(1, s["total"]), 2)} for s in skill_stats.values()],
    }

@app.get("/api/mock/results")
def mock_results(user: User = Depends(get_user), db: Session = Depends(get_db)):
    """Alias: returns latest completed attempt summary."""
    latest = db.query(MockAttempt).filter_by(user_id=user.id, is_preview=False).filter(MockAttempt.completed_at != None).order_by(MockAttempt.attempt_number.desc()).first()
    if not latest:
        raise HTTPException(400, "Mock exam not completed yet")
    return {
        "attempt_id": latest.id, "score": latest.score,
        "total": latest.total_questions, "correct": latest.correct_count,
        "verbal_correct": latest.verbal_correct, "verbal_total": latest.verbal_total,
        "quant_correct": latest.quant_correct, "quant_total": latest.quant_total,
        "verbal_pct": round(latest.verbal_correct / max(1, latest.verbal_total), 2),
        "quant_pct": round(latest.quant_correct / max(1, latest.quant_total), 2),
    }

# ── Admin Config ────────────────────────────────────────────────────────────

class ConfigReq(BaseModel):
    value: int

@app.get("/api/admin/config")
def admin_get_config(admin: User = Depends(get_admin), db: Session = Depends(get_db)):
    return {"mock_max_attempts": get_mock_max(db)}

@app.put("/api/admin/config/mock-attempts")
def admin_set_mock_attempts(req: ConfigReq, admin: User = Depends(get_admin), db: Session = Depends(get_db)):
    effective_value = max(req.value, len(SCHEDULED_MOCK_DAYS))
    cfg = db.query(AppConfig).get("mock_max_attempts")
    if cfg:
        cfg.value = str(effective_value)
    else:
        db.add(AppConfig(key="mock_max_attempts", value=str(effective_value)))
    db.commit()
    return {"mock_max_attempts": effective_value}

# ── Question Bank (Admin) ───────────────────────────────────────────────────

class QuestionTableReq(BaseModel):
    headers: List[str]
    rows: List[List[str]]


class ComparisonColumnsReq(BaseModel):
    a: str
    b: str


class QuestionReq(BaseModel):
    skill_id: str
    question_type: str
    difficulty: float = 0.5
    text_ar: str
    passage_ar: Optional[str] = None
    content_format: Optional[str] = "plain"
    figure_svg: Optional[str] = None
    figure_alt: Optional[str] = None
    table_ar: Optional[QuestionTableReq] = None
    table_caption: Optional[str] = None
    comparison_columns: Optional[ComparisonColumnsReq] = None
    option_a: str
    option_b: str
    option_c: str
    option_d: str
    correct_option: str
    explanation_ar: Optional[str] = None
    solution_steps_ar: Optional[str] = None
    tags: Optional[str] = None
    stage: Optional[str] = "general"
    status: Optional[str] = "active"
    rating_clarity: Optional[float] = None
    rating_cognitive: Optional[float] = None
    rating_distractors: Optional[float] = None
    rating_difficulty_align: Optional[float] = None
    rating_explanation: Optional[float] = None
    rating_fairness: Optional[float] = None
    rating_discrimination: Optional[float] = None
    rating_overall: Optional[float] = None
    rating_passes_done: int = 0
    rating_notes: Optional[str] = None


def validate_admin_question_payload(req: QuestionReq) -> tuple[str, Optional[str], Optional[str], Optional[str]]:
    content_format = validate_content_format(req.content_format)
    figure_alt = clean_optional_text(req.figure_alt)
    table_caption = clean_optional_text(req.table_caption)
    comparison_columns = validate_comparison_columns(
        req.comparison_columns.model_dump() if req.comparison_columns else None
    )

    if req.figure_svg and not figure_alt:
        raise HTTPException(400, "figure_alt is required when figure_svg is provided")

    preview_question = type(
        "QuestionPreview",
        (),
        {
            "skill_id": req.skill_id,
            "question_type": req.question_type,
            "text_ar": req.text_ar,
            "passage_ar": req.passage_ar,
            "option_a": req.option_a,
            "option_b": req.option_b,
            "option_c": req.option_c,
            "option_d": req.option_d,
            "explanation_ar": req.explanation_ar,
            "solution_steps_ar": req.solution_steps_ar,
            "figure_svg": req.figure_svg,
            "figure_alt": figure_alt,
            "table_ar": req.table_ar.model_dump() if req.table_ar else None,
            "table_caption": table_caption,
            "comparison_columns": comparison_columns,
            "content_format": content_format,
            "correct_option": req.correct_option,
            "rating_clarity": req.rating_clarity,
            "rating_cognitive": req.rating_cognitive,
            "rating_distractors": req.rating_distractors,
            "rating_difficulty_align": req.rating_difficulty_align,
            "rating_explanation": req.rating_explanation,
            "rating_fairness": req.rating_fairness,
            "rating_discrimination": req.rating_discrimination,
            "rating_passes_done": req.rating_passes_done,
        },
    )()
    blockers = activation_blockers(preview_question) if req.status == "active" else []
    if blockers:
        raise HTTPException(400, blockers[0])

    return (
        content_format,
        figure_alt,
        table_caption,
        serialize_comparison_columns(comparison_columns),
    )

@app.get("/api/admin/questions")
def admin_questions(
    skill: Optional[str] = None,
    stage: Optional[str] = None,
    status: Optional[str] = None,
    tag: Optional[str] = None,
    batch_id: Optional[str] = None,
    authoring_source: Optional[str] = None,
    variant_group: Optional[str] = None,
    classification: Optional[str] = None,
    issue_code: Optional[str] = None,
    ratings_complete_filter: Optional[bool] = Query(None, alias="ratings_complete"),
    analytics_risk: Optional[str] = None,
    difficulty_min: Optional[float] = None,
    difficulty_max: Optional[float] = None,
    sort: Optional[str] = None,
    admin: User = Depends(get_admin), db: Session = Depends(get_db)
):
    query = db.query(Question)
    if skill:
        query = query.filter(Question.skill_id == skill)
    if stage:
        query = query.filter(Question.stage == stage)
    if status:
        query = query.filter(Question.status == status)
    if tag:
        query = query.filter(Question.tags.contains(tag))
    if batch_id:
        query = query.filter(Question.batch_id == batch_id)
    if authoring_source:
        query = query.filter(Question.authoring_source == authoring_source)
    if variant_group:
        query = query.filter(Question.variant_group == variant_group)
    if difficulty_min is not None:
        query = query.filter(Question.difficulty >= difficulty_min)
    if difficulty_max is not None:
        query = query.filter(Question.difficulty <= difficulty_max)

    questions = query.all()
    skills_map = {s.id: s for s in db.query(Skill).all()}

    result = [build_admin_question_payload(q, skills_map) for q in questions]

    if classification:
        result = [item for item in result if item["content_classification"] == classification]
    if issue_code:
        result = [
            item
            for item in result
            if any(issue["code"] == issue_code for issue in item["content_issues"])
        ]
    if ratings_complete_filter is not None:
        result = [
            item for item in result if item["ratings_complete"] is ratings_complete_filter
        ]
    if analytics_risk:
        result = [
            item for item in result if analytics_risk in item["analytics_flags"]
        ]

    if sort == "accuracy":
        result.sort(key=lambda x: x["accuracy"])
    elif sort == "difficulty":
        result.sort(key=lambda x: x["difficulty"])
    elif sort == "times_answered":
        result.sort(key=lambda x: x["times_answered"], reverse=True)
    elif sort == "discrimination":
        result.sort(key=lambda x: x["discrimination"])
    elif sort == "rating":
        result.sort(key=lambda x: x["rating_overall"] or 0)

    return result

@app.get("/api/admin/questions/analysis")
def admin_question_analysis(admin: User = Depends(get_admin), db: Session = Depends(get_db)):
    questions = db.query(Question).all()
    from collections import Counter
    stage_counts = Counter(q.stage or "general" for q in questions)
    status_counts = Counter(q.status or "active" for q in questions)
    skill_counts = Counter(q.skill_id for q in questions)
    authoring_counts = Counter(clean_optional_text(q.authoring_source) or "human" for q in questions)
    classification_counts = Counter()
    recommended_actions = Counter()
    batch_rollups: dict[str, dict[str, Any]] = {}
    flagged = []
    for q in questions:
        issues = collect_question_content_issues(q)
        quality = collect_question_quality_metadata(q, issues)
        classification_counts[quality["content_classification"]] += 1
        recommended_actions[quality["recommended_action"]] += 1
        batch_key = quality["batch_id"] or "unbatched"
        batch_rollup = batch_rollups.setdefault(
            batch_key,
            {
                "batch_id": quality["batch_id"],
                "authoring_source": quality["authoring_source"] or "human",
                "total": 0,
                "active": 0,
                "review": 0,
                "disabled": 0,
                "auto_published": 0,
                "held_in_review": 0,
            },
        )
        batch_rollup["total"] += 1
        batch_rollup[q.status or "active"] = batch_rollup.get(q.status or "active", 0) + 1
        if (quality["authoring_source"] or "human") == "ai_generated":
            if (q.status or "active") == "active":
                batch_rollup["auto_published"] += 1
            elif (q.status or "active") == "review":
                batch_rollup["held_in_review"] += 1
        analytics_flags = compute_question_analytics_flags(q)
        ta = q.times_answered or 0
        tc = q.times_correct or 0
        acc = tc / max(1, ta) if ta > 0 else None
        issue_codes = sorted({issue.code for issue in issues})
        combined_flags = sorted(set(issue_codes + analytics_flags))
        if combined_flags:
            flagged.append(
                {
                    "id": q.id,
                    "source_key": quality["source_key"],
                    "batch_id": quality["batch_id"],
                    "authoring_source": quality["authoring_source"] or "human",
                    "skill_id": q.skill_id,
                    "difficulty": q.difficulty,
                    "accuracy": acc,
                    "discrimination": q.discrimination,
                    "issues": combined_flags,
                    "analytics_flags": analytics_flags,
                    "content_classification": quality["content_classification"],
                    "recommended_action": quality["recommended_action"],
                    "ratings_complete": quality["ratings_complete"],
                    "issue_counts": quality["content_issue_counts"],
                }
            )
    return {
        "total": len(questions),
        "by_stage": dict(stage_counts),
        "by_status": dict(status_counts),
        "by_skill": dict(skill_counts),
        "by_authoring_source": dict(authoring_counts),
        "by_classification": dict(classification_counts),
        "by_recommended_action": dict(recommended_actions),
        "by_batch": sorted(
            batch_rollups.values(),
            key=lambda item: (item["batch_id"] is None, item["batch_id"] or ""),
        )[:100],
        "flagged_count": len(flagged),
        "flagged": flagged[:50],
    }

@app.post("/api/admin/questions/recalculate")
def admin_recalculate(admin: User = Depends(get_admin), db: Session = Depends(get_db)):
    count = recalculate_all_question_stats(db)
    return {"message": f"Recalculated statistics for {count} questions"}

@app.post("/api/admin/questions/calibrate")
def admin_calibrate(
    min_answers: int = Query(10, ge=1),
    learning_rate: float = Query(0.3, ge=0.01, le=1.0),
    dry_run: bool = Query(False),
    admin: User = Depends(get_admin), db: Session = Depends(get_db)
):
    result = calibrate_question_difficulties(db, min_answers=min_answers, learning_rate=learning_rate, dry_run=dry_run)
    return result

@app.post("/api/admin/questions")
def admin_add_question(req: QuestionReq, admin: User = Depends(get_admin), db: Session = Depends(get_db)):
    try:
        figure_svg, table_ar = prepare_question_visual_fields(
            req.figure_svg,
            req.table_ar.model_dump() if req.table_ar else None,
        )
    except ValueError as exc:
        raise HTTPException(400, str(exc)) from exc
    content_format, figure_alt, table_caption, comparison_columns = validate_admin_question_payload(req)

    q = Question(skill_id=req.skill_id, question_type=req.question_type, difficulty=req.difficulty,
                 text_ar=req.text_ar, passage_ar=req.passage_ar,
                 figure_svg=figure_svg, table_ar=table_ar,
                 content_format=content_format, figure_alt=figure_alt,
                 table_caption=table_caption, comparison_columns=comparison_columns,
                 option_a=req.option_a, option_b=req.option_b,
                 option_c=req.option_c, option_d=req.option_d,
                 correct_option=req.correct_option, explanation_ar=req.explanation_ar,
                 solution_steps_ar=req.solution_steps_ar,
                 tags=req.tags, stage=req.stage, status=req.status,
                 source_key=f"admin:{uuid4().hex}",
                 authoring_source="human",
                 original_difficulty=req.difficulty,
                 rating_clarity=req.rating_clarity,
                 rating_cognitive=req.rating_cognitive,
                 rating_distractors=req.rating_distractors,
                 rating_difficulty_align=req.rating_difficulty_align,
                 rating_explanation=req.rating_explanation,
                 rating_fairness=req.rating_fairness,
                 rating_discrimination=req.rating_discrimination,
                 rating_overall=req.rating_overall,
                 rating_passes_done=req.rating_passes_done,
                 rating_notes=req.rating_notes)
    db.add(q)
    db.commit()
    db.refresh(q)
    return {"id": q.id, "message": "Question added"}

@app.put("/api/admin/questions/{question_id}")
def admin_update_question(question_id: int, req: QuestionReq, admin: User = Depends(get_admin), db: Session = Depends(get_db)):
    q = db.query(Question).get(question_id)
    if not q:
        raise HTTPException(404, "Question not found")
    try:
        figure_svg, table_ar = prepare_question_visual_fields(
            req.figure_svg,
            req.table_ar.model_dump() if req.table_ar else None,
        )
    except ValueError as exc:
        raise HTTPException(400, str(exc)) from exc
    content_format, figure_alt, table_caption, comparison_columns = validate_admin_question_payload(req)

    for field in ["skill_id", "question_type", "difficulty", "text_ar", "passage_ar",
                   "option_a", "option_b", "option_c", "option_d", "correct_option",
                   "explanation_ar", "solution_steps_ar", "tags", "stage", "status",
                   "rating_clarity", "rating_cognitive", "rating_distractors",
                   "rating_difficulty_align", "rating_explanation", "rating_fairness",
                   "rating_discrimination", "rating_overall", "rating_passes_done",
                   "rating_notes"]:
        setattr(q, field, getattr(req, field))
    q.figure_svg = figure_svg
    q.table_ar = table_ar
    q.content_format = content_format
    q.figure_alt = figure_alt
    q.table_caption = table_caption
    q.comparison_columns = comparison_columns
    if not q.source_key:
        q.source_key = generate_admin_source_key(q.id)
    if not q.authoring_source:
        q.authoring_source = "human"
    db.commit()
    return {"message": "Question updated"}

@app.delete("/api/admin/questions/{question_id}")
def admin_delete_question(question_id: int, admin: User = Depends(get_admin), db: Session = Depends(get_db)):
    q = db.query(Question).get(question_id)
    if not q:
        raise HTTPException(404, "Question not found")
    db.query(UserResponse).filter_by(question_id=q.id).delete()
    db.delete(q)
    db.commit()
    return {"message": "Question deleted"}

# ── Health check ─────────────────────────────────────────────────────────────
@app.get("/health")
async def health_check():
    return {
        "status": "ok",
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    }

# ── Serve frontend ───────────────────────────────────────────────────────────
# Try multiple paths for Railway and local development
possible_dirs = [
    os.path.join(os.path.dirname(__file__), "static"),  # Production: backend/static
    os.path.join(os.path.dirname(__file__), "..", "frontend", "dist"),  # Local dev
    "/app/frontend/dist",  # Railway specific path
]

for d in possible_dirs:
    print(f"Checking FRONTEND_DIR: {d} - exists: {os.path.exists(d)}")
    if os.path.exists(d):
        FRONTEND_DIR = d
        print(f"Selected FRONTEND_DIR: {FRONTEND_DIR}")
        break

if FRONTEND_DIR and os.path.exists(FRONTEND_DIR):
    assets_dir = os.path.join(FRONTEND_DIR, "assets")
    if os.path.exists(assets_dir):
        app.mount("/assets", StaticFiles(directory=assets_dir), name="assets")

    # Serve root-level static files (logo, favicon, robots.txt, etc.)
    for static_ext in ('.png', '.ico', '.svg', '.txt', '.xml', '.webmanifest'):
        for fname in os.listdir(FRONTEND_DIR):
            if fname.endswith(static_ext):
                fpath = os.path.join(FRONTEND_DIR, fname)
                if os.path.isfile(fpath):
                    @app.get(f"/{fname}")
                    async def _serve_static(f=fpath):
                        return FileResponse(f)
    
    @app.get("/{full_path:path}")
    async def serve_frontend(full_path: str):
        # Skip API routes
        if full_path.startswith("api/") or full_path in ["health", "docs", "openapi.json"]:
            raise HTTPException(status_code=404, detail="Not found")
        # Serve static files directly if they exist
        static_file = os.path.join(FRONTEND_DIR, full_path)
        if full_path and os.path.isfile(static_file):
            resp = FileResponse(static_file)
            if full_path.startswith("assets/"):
                resp.headers["Cache-Control"] = "public, max-age=31536000, immutable"
            return resp
        # Serve index.html for all other routes (SPA behavior)
        index_response = frontend_index_response()
        if index_response:
            return index_response
        raise HTTPException(status_code=404, detail="Not found")
