import json, math, datetime, os
from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional, List
import hashlib
from jose import jwt

from database import get_db, engine, Base
from models import User, Skill, Question, UserAbility, UserResponse, StudyPlan, Badge, UserBadge, Feedback, MockAttempt, AppConfig
from adaptive import update_ability, select_next_question, select_diagnostic_question, generate_study_plan, predict_score, recalculate_all_question_stats, calibrate_question_difficulties
from seed import seed_all

# ── App setup ────────────────────────────────────────────────────────────────
Base.metadata.create_all(bind=engine)
seed_all()

app = FastAPI(title="Qudra Academy — GAT Prep")
app.add_middleware(GZipMiddleware, minimum_size=500)
app.add_middleware(CORSMiddleware, allow_origins=os.getenv("CORS_ORIGINS", "*").split(","), allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.get("/")
async def root():
    return {"message": "Qudra Academy API", "status": "running"}

SECRET = os.getenv("SECRET_KEY", "gat-prep-secret-key-change-in-production")
def hash_pw(p): return hashlib.sha256((p + SECRET).encode()).hexdigest()
def verify_pw(p, h): return hash_pw(p) == h

def update_question_stats(q, is_correct: bool, time_spent: int):
    """Update question-level analytics after each answer."""
    q.times_answered = (q.times_answered or 0) + 1
    if is_correct:
        q.times_correct = (q.times_correct or 0) + 1
    prev_avg = q.avg_time_seconds or 0.0
    q.avg_time_seconds = (prev_avg * (q.times_answered - 1) + time_spent) / q.times_answered

# ── Schemas ──────────────────────────────────────────────────────────────────
class RegisterReq(BaseModel):
    name: str
    email: str
    password: str

class LoginReq(BaseModel):
    email: str
    password: str

class AnswerReq(BaseModel):
    question_id: int
    selected_option: str
    time_spent_seconds: int = 0

class SettingsReq(BaseModel):
    daily_minutes: int

# ── Auth helpers ─────────────────────────────────────────────────────────────
def create_token(user_id: int):
    return jwt.encode({"sub": str(user_id), "exp": datetime.datetime.utcnow() + datetime.timedelta(days=30)}, SECRET)

def get_current_user(db: Session = Depends(get_db), token: str = None):
    from fastapi import Header
    return None  # simplified for MVP; see auth endpoint

from fastapi import Header

def get_user(authorization: str = Header(None), db: Session = Depends(get_db)):
    if not authorization:
        raise HTTPException(401, "مطلوب تسجيل الدخول")
    try:
        token = authorization.replace("Bearer ", "")
        payload = jwt.decode(token, SECRET, algorithms=["HS256"])
        user = db.query(User).get(int(payload["sub"]))
        if not user:
            raise HTTPException(401, "المستخدم غير موجود")
        return user
    except (Exception,):
        raise HTTPException(401, "رمز غير صالح")

# ── Auth endpoints ───────────────────────────────────────────────────────────
@app.post("/api/auth/register")
def register(req: RegisterReq, db: Session = Depends(get_db)):
    if len(req.password) < 6:
        raise HTTPException(400, "كلمة المرور يجب أن تكون ٦ أحرف على الأقل")
    if db.query(User).filter_by(email=req.email).first():
        raise HTTPException(400, "البريد مسجل مسبقاً")
    user = User(name=req.name, email=req.email, password_hash=hash_pw(req.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    # Initialize abilities at 0
    for skill in db.query(Skill).all():
        db.add(UserAbility(user_id=user.id, skill_id=skill.id))
    db.commit()
    return {"token": create_token(user.id), "user": {"id": user.id, "name": user.name}}

@app.post("/api/auth/login")
def login(req: LoginReq, db: Session = Depends(get_db)):
    user = db.query(User).filter_by(email=req.email).first()
    if not user or not verify_pw(req.password, user.password_hash):
        raise HTTPException(401, "بيانات الدخول غير صحيحة")
    return {"token": create_token(user.id), "user": {"id": user.id, "name": user.name}}

# ── User profile ─────────────────────────────────────────────────────────────
@app.get("/api/me")
def get_me(user: User = Depends(get_user), db: Session = Depends(get_db)):
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
        "mock_max_attempts": int((db.query(AppConfig).get("mock_max_attempts") or type('', (), {'value': '2'})).value),
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
        raise HTTPException(400, "التشخيصي مكتمل مسبقاً")
    return {"message": "ابدأ الاختبار التشخيصي", "total_questions": 9}

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

    # Pick next skill and find a medium-difficulty question for it
    next_skill = remaining_skills[0]
    q = db.query(Question).filter(
        Question.skill_id == next_skill,
        ~Question.id.in_(answered_ids) if answered_ids else True
    ).order_by(Question.difficulty).all()

    # Pick a medium-difficulty question (closest to 0.5)
    if not q:
        return {"done": True, "total_answered": len(answered_ids)}
    q = min(q, key=lambda x: abs(x.difficulty - 0.5))

    return {
        "done": False,
        "progress": len(answered_ids),
        "total": 9,
        "question": format_question(q),
    }

@app.post("/api/diagnostic/answer")
def diagnostic_answer(req: AnswerReq, user: User = Depends(get_user), db: Session = Depends(get_db)):
    if user.diagnostic_completed:
        raise HTTPException(400, "التشخيصي مكتمل مسبقاً")
    q = db.query(Question).get(req.question_id)
    if not q:
        raise HTTPException(404, "السؤال غير موجود")

    is_correct = req.selected_option == q.correct_option
    resp = UserResponse(user_id=user.id, question_id=q.id, session_type="diagnostic",
                        selected_option=req.selected_option, is_correct=is_correct,
                        time_spent_seconds=req.time_spent_seconds)
    db.add(resp)
    update_ability(db, user.id, q.skill_id, is_correct, q.difficulty)
    update_question_stats(q, is_correct, req.time_spent_seconds)

    # Award XP
    user.xp += 10 if is_correct else 5
    db.commit()

    return {
        "is_correct": is_correct,
        "correct_option": q.correct_option,
        "explanation_ar": q.explanation_ar,
        "solution_steps_ar": json.loads(q.solution_steps_ar) if q.solution_steps_ar else None,
    }

@app.post("/api/diagnostic/complete")
def complete_diagnostic(user: User = Depends(get_user), db: Session = Depends(get_db)):
    user.diagnostic_completed = True
    user.current_day = 1
    user.course_started_at = datetime.datetime.utcnow()
    db.commit()
    generate_study_plan(db, user.id, user.daily_minutes)
    score = predict_score(db, user.id)
    return {"message": "تم إكمال التشخيصي!", "predicted_score": score}

# ── Study Plan ───────────────────────────────────────────────────────────────
@app.get("/api/study-plan")
def get_study_plan(user: User = Depends(get_user), db: Session = Depends(get_db)):
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
    plan = db.query(StudyPlan).filter_by(user_id=user.id, day_number=user.current_day).first()
    if not plan:
        return {"day": user.current_day, "phase": "", "focus_skills": [], "target_questions": 0,
                "completed_questions": 0, "is_mock_day": False, "is_rest_day": False, "remaining": 0,
                "message": "لا توجد خطة لليوم"}
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
        return {"done": True, "message": "أنهيت جميع الأسئلة المتاحة!"}

    return {"done": False, "question": format_question(q)}

@app.post("/api/practice/answer")
def practice_answer(req: AnswerReq, user: User = Depends(get_user), db: Session = Depends(get_db)):
    q = db.query(Question).get(req.question_id)
    if not q:
        raise HTTPException(404, "السؤال غير موجود")

    is_correct = req.selected_option == q.correct_option

    resp = UserResponse(user_id=user.id, question_id=q.id, session_type="drill",
                        selected_option=req.selected_option, is_correct=is_correct,
                        time_spent_seconds=req.time_spent_seconds)
    db.add(resp)
    update_ability(db, user.id, q.skill_id, is_correct, q.difficulty)
    update_question_stats(q, is_correct, req.time_spent_seconds)

    # Update plan progress
    plan = db.query(StudyPlan).filter_by(user_id=user.id, day_number=user.current_day).first()
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
        "explanation_ar": q.explanation_ar,
        "solution_steps_ar": json.loads(q.solution_steps_ar) if q.solution_steps_ar else None,
        "xp_earned": 10 if is_correct else 5,
    }

# ── Advance day ──────────────────────────────────────────────────────────────
@app.post("/api/advance-day")
def advance_day(user: User = Depends(get_user), db: Session = Depends(get_db)):
    if user.current_day >= 30:
        return {"current_day": user.current_day}
    plan = db.query(StudyPlan).filter_by(user_id=user.id, day_number=user.current_day).first()
    if plan and not plan.is_rest_day and plan.completed_questions < plan.target_questions:
        raise HTTPException(400, "أكمل أسئلة اليوم أولاً")
    user.current_day += 1
    db.commit()
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
def format_question(q: Question):
    return {
        "id": q.id,
        "skill_id": q.skill_id,
        "question_type": q.question_type,
        "difficulty": q.difficulty,
        "text_ar": q.text_ar,
        "passage_ar": q.passage_ar,
        "options": [
            {"key": "a", "label": "أ", "text_ar": q.option_a},
            {"key": "b", "label": "ب", "text_ar": q.option_b},
            {"key": "c", "label": "ج", "text_ar": q.option_c},
            {"key": "d", "label": "د", "text_ar": q.option_d},
        ],
        "paper_only": q.paper_only,
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

@app.post("/api/feedback")
def submit_feedback(req: FeedbackReq, user: User = Depends(get_user), db: Session = Depends(get_db)):
    if req.rating < 1 or req.rating > 5:
        raise HTTPException(400, "التقييم يجب أن يكون بين ١ و ٥")
    fb = Feedback(user_id=user.id, rating=req.rating, comment=req.comment, trigger=req.trigger, page=req.page)
    db.add(fb)
    db.commit()
    return {"message": "شكراً لملاحظاتك!"}

# ── Admin ────────────────────────────────────────────────────────────────────

def get_admin(user: User = Depends(get_user)):
    if not user.is_admin:
        raise HTTPException(403, "غير مصرح لك بالوصول")
    return user

@app.get("/api/admin/feedback")
def admin_feedback(days: int = Query(30), trigger: Optional[str] = None, admin: User = Depends(get_admin), db: Session = Depends(get_db)):
    cutoff = datetime.datetime.utcnow() - datetime.timedelta(days=days)
    q = db.query(Feedback).filter(Feedback.created_at >= cutoff)
    if trigger:
        q = q.filter(Feedback.trigger == trigger)
    items = q.order_by(Feedback.created_at.desc()).limit(200).all()
    return [{"id": f.id, "user_id": f.user_id, "rating": f.rating, "comment": f.comment,
             "trigger": f.trigger, "page": f.page, "created_at": f.created_at.isoformat()} for f in items]

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
    return int(cfg.value) if cfg else 2

class MockAnswerReq(BaseModel):
    question_id: int
    selected_option: str
    time_spent_seconds: int = 0
    attempt_id: int

@app.post("/api/mock/start")
def mock_start(preview: bool = Query(False), user: User = Depends(get_user), db: Session = Depends(get_db)):
    is_preview = preview and user.is_admin
    if not is_preview:
        max_attempts = get_mock_max(db)
        if user.mock_attempts >= max_attempts:
            raise HTTPException(400, f"تجاوزت الحد الأقصى من المحاولات ({max_attempts})")
        if user.current_day < 25:
            raise HTTPException(400, "اختبار المحاكاة متاح من اليوم ٢٥")

    import random
    verbal_skills = [s.id for s in db.query(Skill).filter_by(section="verbal").all()]
    quant_skills = [s.id for s in db.query(Skill).filter_by(section="quantitative").all()]

    # Exclude questions the user has already seen in practice or diagnostic
    practiced_ids = set(r.question_id for r in db.query(UserResponse).filter_by(user_id=user.id).filter(
        UserResponse.session_type.in_(["drill", "diagnostic"])).all())

    # Get unseen questions first — prefer mock-stage, then general, then any
    mock_stages = ["mock", "general"]
    unseen_verbal = [q for q in db.query(Question).filter(
        Question.skill_id.in_(verbal_skills), Question.stage.in_(mock_stages), Question.status != "disabled"
    ).all() if q.id not in practiced_ids]
    unseen_quant = [q for q in db.query(Question).filter(
        Question.skill_id.in_(quant_skills), Question.stage.in_(mock_stages), Question.status != "disabled"
    ).all() if q.id not in practiced_ids]
    random.shuffle(unseen_verbal)
    random.shuffle(unseen_quant)

    # If not enough unseen, fill with least-recently-answered questions
    if len(unseen_verbal) < MOCK_VERBAL_COUNT:
        seen_verbal = db.query(Question).filter(Question.skill_id.in_(verbal_skills), Question.id.in_(practiced_ids)).all()
        random.shuffle(seen_verbal)
        unseen_verbal += seen_verbal
    if len(unseen_quant) < MOCK_QUANT_COUNT:
        seen_quant = db.query(Question).filter(Question.skill_id.in_(quant_skills), Question.id.in_(practiced_ids)).all()
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
        raise HTTPException(404, "السؤال غير موجود")
    return format_question(q)

@app.post("/api/mock/answer")
def mock_answer(req: MockAnswerReq, user: User = Depends(get_user), db: Session = Depends(get_db)):
    q = db.query(Question).get(req.question_id)
    if not q:
        raise HTTPException(404, "السؤال غير موجود")
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
        raise HTTPException(404, "المحاولة غير موجودة")
    if attempt.completed_at:
        raise HTTPException(400, "تم إكمال هذه المحاولة مسبقاً")

    responses = db.query(UserResponse).filter_by(user_id=user.id, attempt_id=attempt.id).all()
    if not responses:
        raise HTTPException(400, "لم يتم الإجابة على أي سؤال")

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
        raise HTTPException(404, "المحاولة غير موجودة")
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
        raise HTTPException(404, "المحاولة غير موجودة")

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
        questions_detail.append({
            "question_id": q.id, "text_ar": q.text_ar, "passage_ar": q.passage_ar,
            "options": [{"key": "a", "text_ar": q.option_a}, {"key": "b", "text_ar": q.option_b},
                        {"key": "c", "text_ar": q.option_c}, {"key": "d", "text_ar": q.option_d}],
            "selected_option": r.selected_option, "correct_option": q.correct_option,
            "is_correct": r.is_correct, "time_spent_seconds": r.time_spent_seconds,
            "explanation_ar": q.explanation_ar,
            "skill_id": q.skill_id, "skill_name_ar": skill.name_ar if skill else "",
            "section": skill.section if skill else "",
        })
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
        raise HTTPException(400, "لم يتم إكمال اختبار المحاكاة بعد")
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
    cfg = db.query(AppConfig).get("mock_max_attempts")
    if cfg:
        cfg.value = str(req.value)
    else:
        db.add(AppConfig(key="mock_max_attempts", value=str(req.value)))
    db.commit()
    return {"mock_max_attempts": req.value}

# ── Question Bank (Admin) ───────────────────────────────────────────────────

class QuestionReq(BaseModel):
    skill_id: str
    question_type: str
    difficulty: float = 0.5
    text_ar: str
    passage_ar: Optional[str] = None
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

@app.get("/api/admin/questions")
def admin_questions(
    skill: Optional[str] = None,
    stage: Optional[str] = None,
    status: Optional[str] = None,
    tag: Optional[str] = None,
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
    if difficulty_min is not None:
        query = query.filter(Question.difficulty >= difficulty_min)
    if difficulty_max is not None:
        query = query.filter(Question.difficulty <= difficulty_max)

    questions = query.all()
    skills_map = {s.id: s for s in db.query(Skill).all()}

    result = []
    for q in questions:
        ta = q.times_answered or 0
        tc = q.times_correct or 0
        result.append({
            "id": q.id, "skill_id": q.skill_id,
            "skill_name_ar": skills_map[q.skill_id].name_ar if q.skill_id in skills_map else q.skill_id,
            "section": skills_map[q.skill_id].section if q.skill_id in skills_map else "",
            "question_type": q.question_type, "difficulty": q.difficulty,
            "text_ar": q.text_ar, "passage_ar": q.passage_ar,
            "option_a": q.option_a, "option_b": q.option_b,
            "option_c": q.option_c, "option_d": q.option_d,
            "correct_option": q.correct_option,
            "explanation_ar": q.explanation_ar,
            "solution_steps_ar": json.loads(q.solution_steps_ar) if q.solution_steps_ar else None,
            "tags": q.tags or "", "stage": q.stage or "general", "status": q.status or "active",
            "times_answered": ta, "times_correct": tc,
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
        })

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
    flagged = []
    for q in questions:
        ta = q.times_answered or 0
        tc = q.times_correct or 0
        acc = tc / max(1, ta) if ta > 0 else None
        issues = []
        if ta >= 10 and acc is not None and acc < 0.2:
            issues.append("very_low_accuracy")
        if ta >= 10 and acc is not None and acc > 0.95:
            issues.append("too_easy")
        if ta >= 10 and (q.discrimination or 0) < 0.1:
            issues.append("low_discrimination")
        if issues:
            flagged.append({"id": q.id, "skill_id": q.skill_id, "difficulty": q.difficulty, "accuracy": acc, "discrimination": q.discrimination, "issues": issues})
    return {
        "total": len(questions),
        "by_stage": dict(stage_counts),
        "by_status": dict(status_counts),
        "by_skill": dict(skill_counts),
        "flagged_count": len(flagged),
        "flagged": flagged[:50],
    }

@app.post("/api/admin/questions/recalculate")
def admin_recalculate(admin: User = Depends(get_admin), db: Session = Depends(get_db)):
    count = recalculate_all_question_stats(db)
    return {"message": f"تم إعادة حساب إحصائيات {count} سؤال"}

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
    q = Question(skill_id=req.skill_id, question_type=req.question_type, difficulty=req.difficulty,
                 text_ar=req.text_ar, passage_ar=req.passage_ar,
                 option_a=req.option_a, option_b=req.option_b,
                 option_c=req.option_c, option_d=req.option_d,
                 correct_option=req.correct_option, explanation_ar=req.explanation_ar,
                 solution_steps_ar=req.solution_steps_ar,
                 tags=req.tags, stage=req.stage, status=req.status)
    db.add(q)
    db.commit()
    db.refresh(q)
    return {"id": q.id, "message": "تمت إضافة السؤال"}

@app.put("/api/admin/questions/{question_id}")
def admin_update_question(question_id: int, req: QuestionReq, admin: User = Depends(get_admin), db: Session = Depends(get_db)):
    q = db.query(Question).get(question_id)
    if not q:
        raise HTTPException(404, "السؤال غير موجود")
    for field in ["skill_id", "question_type", "difficulty", "text_ar", "passage_ar",
                   "option_a", "option_b", "option_c", "option_d", "correct_option",
                   "explanation_ar", "solution_steps_ar", "tags", "stage", "status"]:
        setattr(q, field, getattr(req, field))
    db.commit()
    return {"message": "تم تحديث السؤال"}

@app.delete("/api/admin/questions/{question_id}")
def admin_delete_question(question_id: int, admin: User = Depends(get_admin), db: Session = Depends(get_db)):
    q = db.query(Question).get(question_id)
    if not q:
        raise HTTPException(404, "السؤال غير موجود")
    db.query(UserResponse).filter_by(question_id=q.id).delete()
    db.delete(q)
    db.commit()
    return {"message": "تم حذف السؤال"}

# ── Health check ─────────────────────────────────────────────────────────────
@app.get("/health")
async def health_check():
    return {"status": "ok", "timestamp": datetime.datetime.utcnow().isoformat()}

# ── Serve frontend ───────────────────────────────────────────────────────────
# Try multiple paths for Railway and local development
possible_dirs = [
    os.path.join(os.path.dirname(__file__), "static"),  # Production: backend/static
    os.path.join(os.path.dirname(__file__), "..", "frontend", "dist"),  # Local dev
    "/app/frontend/dist",  # Railway specific path
]

FRONTEND_DIR = None
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
        index_file = os.path.join(FRONTEND_DIR, "index.html")
        if os.path.exists(index_file):
            resp = FileResponse(index_file)
            resp.headers["Cache-Control"] = "no-cache"
            return resp
        raise HTTPException(status_code=404, detail="Not found")
