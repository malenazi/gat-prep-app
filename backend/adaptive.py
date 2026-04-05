import math, random, datetime
from sqlalchemy.orm import Session
from sqlalchemy import func
from models import UserAbility, Question, UserResponse, StudyPlan, Skill, User

SCHEDULED_MOCK_DAYS = (11, 18, 24, 27)

# ── Elo-based ability tracking ──────────────────────────────────────────────

def update_ability(db: Session, user_id: int, skill_id: str, is_correct: bool, item_difficulty: float):
    if item_difficulty is None:
        item_difficulty = 0.5  # safe default
    ability = db.query(UserAbility).filter_by(user_id=user_id, skill_id=skill_id).first()
    if not ability:
        ability = UserAbility(user_id=user_id, skill_id=skill_id, theta=0.0, questions_seen=0, correct_count=0)
        db.add(ability)
        db.flush()

    K = max(0.1, 0.4 - 0.003 * ability.questions_seen)
    diff = ability.theta - item_difficulty
    diff = max(-10.0, min(10.0, diff))  # prevent math overflow
    expected = 1 / (1 + math.exp(-diff))
    ability.theta += K * (int(is_correct) - expected)
    ability.theta = max(-3.0, min(3.0, ability.theta))  # clamp
    ability.questions_seen += 1
    if is_correct:
        ability.correct_count += 1
    ability.mastery = ability.correct_count / max(1, ability.questions_seen)
    ability.last_updated = datetime.datetime.utcnow()
    db.commit()
    return ability

# ── Adaptive item selection (ε-greedy) ──────────────────────────────────────

def _stage_for_day(current_day: int) -> list:
    """Return allowed stages based on user's current study day."""
    if current_day <= 7:
        return ["foundation", "general"]
    elif current_day <= 22:
        return ["building", "general"]
    else:
        return ["peak", "general"]

def select_next_question(db: Session, user_id: int, session_type: str = "drill", excluded_ids: list = None, current_day: int = 0):
    if excluded_ids is None:
        excluded_ids = []

    abilities = db.query(UserAbility).filter_by(user_id=user_id).all()
    skills = db.query(Skill).all()
    skill_map = {s.id: s for s in skills}

    # Determine stage filter
    stages = _stage_for_day(current_day) if current_day > 0 else ["foundation", "building", "peak", "general"]

    # Build priority scores
    priorities = []
    for skill in skills:
        ab = next((a for a in abilities if a.skill_id == skill.id), None)
        mastery = ab.mastery if ab else 0.0
        theta = ab.theta if ab else 0.0
        need = (1 - mastery) * skill.exam_weight
        priorities.append({"skill_id": skill.id, "need": need, "theta": theta, "mastery": mastery})

    priorities.sort(key=lambda x: x["need"], reverse=True)

    # ε-greedy selection
    r = random.random()
    if r < 0.7 and priorities:
        target_skill = priorities[0]["skill_id"]
        target_theta = priorities[0]["theta"]
    elif r < 0.9 and len(priorities) > 1:
        mid = priorities[len(priorities) // 2]
        target_skill = mid["skill_id"]
        target_theta = mid["theta"]
    else:
        chosen = random.choice(priorities) if priorities else None
        if not chosen:
            return None
        target_skill = chosen["skill_id"]
        target_theta = chosen["theta"]

    # Find best-matching question with stage filter
    base_filter = [
        Question.skill_id == target_skill,
        Question.stage.in_(stages),
        Question.status == "active",
    ]
    if excluded_ids:
        base_filter.append(~Question.id.in_(excluded_ids))

    questions = db.query(Question).filter(*base_filter).all()

    if not questions:
        # Fallback: any active question not yet seen (ignore stage)
        fallback_filter = [Question.status == "active"]
        if excluded_ids:
            fallback_filter.append(~Question.id.in_(excluded_ids))
        questions = db.query(Question).filter(*fallback_filter).all()

    if not questions:
        return None

    # Pick question closest to student's ability (target ~85% accuracy → slight undershoot)
    target_diff = target_theta - 0.3  # aim slightly easier for 85% zone
    questions.sort(key=lambda q: abs(q.difficulty - target_diff))
    # Add some randomness in top 5 matches
    top = questions[:min(5, len(questions))]
    return random.choice(top)

# ── Diagnostic item selection (CAT-style) ───────────────────────────────────

def select_diagnostic_question(db: Session, user_id: int, current_theta: float, section: str, excluded_ids: list):
    skills = db.query(Skill).filter(Skill.section == section).all()
    skill_ids = [s.id for s in skills]

    # Prefer diagnostic-stage questions, fall back to general
    base_filter = [
        Question.skill_id.in_(skill_ids),
        Question.stage.in_(["diagnostic", "general"]),
        Question.status == "active",
    ]
    if excluded_ids:
        base_filter.append(~Question.id.in_(excluded_ids))

    questions = db.query(Question).filter(*base_filter).all()

    if not questions:
        # Fallback: any active question in these skills
        fallback = [Question.skill_id.in_(skill_ids), Question.status == "active"]
        if excluded_ids:
            fallback.append(~Question.id.in_(excluded_ids))
        questions = db.query(Question).filter(*fallback).all()

    if not questions:
        return None

    # Select question maximizing information at current theta
    questions.sort(key=lambda q: abs(q.difficulty - current_theta))
    top = questions[:min(3, len(questions))]
    return random.choice(top)

# ── Study plan generator ────────────────────────────────────────────────────

def generate_study_plan(db: Session, user_id: int, daily_minutes: int):
    abilities = db.query(UserAbility).filter_by(user_id=user_id).all()
    skills = db.query(Skill).all()

    # Calculate per-skill need
    skill_needs = []
    for skill in skills:
        ab = next((a for a in abilities if a.skill_id == skill.id), None)
        mastery = ab.mastery if ab else 0.0
        need = (1 - mastery) * skill.exam_weight
        skill_needs.append({"skill_id": skill.id, "need": need, "section": skill.section})

    skill_needs.sort(key=lambda x: x["need"], reverse=True)

    # Questions per day based on time
    questions_per_day = max(10, daily_minutes // 4)  # ~4 min per question with review

    # Delete old plan
    db.query(StudyPlan).filter_by(user_id=user_id).delete()

    import json
    for day in range(1, 31):
        if day <= 7:
            phase = "foundation"
            # Focus on top 3 weakest skills
            focus = [s["skill_id"] for s in skill_needs[:3]]
        elif day <= 22:
            phase = "building"
            # Rotate through all skills, weighted by need
            offset = (day - 8) % len(skill_needs)
            focus = [skill_needs[(offset + i) % len(skill_needs)]["skill_id"] for i in range(4)]
        else:
            phase = "peak"
            # Focus on top 2 weakest + general review
            focus = [s["skill_id"] for s in skill_needs[:2]]

        is_mock = day in SCHEDULED_MOCK_DAYS
        is_rest = day == 30
        target = 120 if is_mock else (questions_per_day // 2 if is_rest else questions_per_day)

        plan_day = StudyPlan(
            user_id=user_id,
            day_number=day,
            phase=phase,
            focus_skills=json.dumps(focus),
            target_questions=target,
            is_mock_day=is_mock,
            is_rest_day=is_rest,
        )
        db.add(plan_day)

    db.commit()

# ── Score prediction ────────────────────────────────────────────────────────

def predict_score(db: Session, user_id: int):
    abilities = db.query(UserAbility).filter_by(user_id=user_id).all()
    skills = db.query(Skill).all()

    if not abilities:
        return {"low": 55, "mid": 65, "high": 75, "verbal_mastery": 0, "quant_mastery": 0}

    verbal_score = 0
    quant_score = 0
    verbal_weight_sum = 0
    quant_weight_sum = 0

    for skill in skills:
        ab = next((a for a in abilities if a.skill_id == skill.id), None)
        mastery = ab.mastery if ab else 0.3  # assume 30% baseline
        if skill.section == "verbal":
            verbal_score += mastery * skill.exam_weight
            verbal_weight_sum += skill.exam_weight
        else:
            quant_score += mastery * skill.exam_weight
            quant_weight_sum += skill.exam_weight

    verbal_pct = verbal_score / max(0.01, verbal_weight_sum)
    quant_pct = quant_score / max(0.01, quant_weight_sum)

    # GAT score: 50% verbal + 50% quant, mapped to 1-100 scale
    raw = (verbal_pct * 0.5 + quant_pct * 0.5)
    # Map to GAT scale (non-linear, centered around 65)
    estimated = 40 + raw * 55  # rough linear mapping
    estimated = max(40, min(100, estimated))

    return {
        "low": max(40, int(estimated - 5)),
        "mid": int(estimated),
        "high": min(100, int(estimated + 5)),
        "verbal_mastery": round(verbal_pct, 2),
        "quant_mastery": round(quant_pct, 2),
    }

# ── Question analytics ─────────────────────────────────────────────────────

def recalculate_all_question_stats(db: Session):
    """Recompute times_answered, times_correct, avg_time, discrimination for all questions."""
    questions = db.query(Question).all()
    # Build response lookup per question
    all_responses = db.query(UserResponse).all()
    from collections import defaultdict
    q_responses = defaultdict(list)
    for r in all_responses:
        q_responses[r.question_id].append(r)

    # Get user theta averages for discrimination calc
    user_thetas = {}
    for ua in db.query(UserAbility).all():
        if ua.user_id not in user_thetas:
            user_thetas[ua.user_id] = []
        user_thetas[ua.user_id].append(ua.theta)
    user_avg_theta = {uid: sum(ts) / len(ts) for uid, ts in user_thetas.items() if ts}

    for q in questions:
        resps = q_responses.get(q.id, [])
        q.times_answered = len(resps)
        q.times_correct = sum(1 for r in resps if r.is_correct)
        if resps:
            q.avg_time_seconds = sum(r.time_spent_seconds for r in resps) / len(resps)
        else:
            q.avg_time_seconds = 0.0

        # Discrimination: compare top 27% vs bottom 27% by theta
        if len(resps) >= 10 and user_avg_theta:
            scored = [(r, user_avg_theta.get(r.user_id, 0.0)) for r in resps if r.user_id in user_avg_theta]
            scored.sort(key=lambda x: x[1])
            n = max(1, len(scored) // 4)
            bottom = scored[:n]
            top = scored[-n:]
            top_acc = sum(1 for r, _ in top if r.is_correct) / max(1, len(top))
            bot_acc = sum(1 for r, _ in bottom if r.is_correct) / max(1, len(bottom))
            q.discrimination = round(top_acc - bot_acc, 3)
        else:
            q.discrimination = 0.0

    db.commit()
    return len(questions)


def calibrate_question_difficulties(db: Session, min_answers: int = 10, learning_rate: float = 0.3, dry_run: bool = False):
    """Auto-adjust difficulty values based on empirical accuracy data.

    Uses IRT-inspired approach: if actual accuracy >> expected, question is easier than rated.
    learning_rate controls how aggressively to adjust (0.0 = no change, 1.0 = jump to target).
    """
    questions = db.query(Question).all()
    changes = []
    calibrated = 0
    skipped = 0

    for q in questions:
        ta = q.times_answered or 0
        tc = q.times_correct or 0

        if ta < min_answers:
            skipped += 1
            continue

        # Preserve original difficulty on first calibration
        if q.original_difficulty is None:
            q.original_difficulty = q.difficulty

        empirical_accuracy = tc / ta

        # Target difficulty: 1 - accuracy (90% correct → 0.10 difficulty, 30% correct → 0.70)
        target_difficulty = 1.0 - empirical_accuracy

        # Smooth adjustment
        old_diff = q.difficulty
        new_diff = old_diff + learning_rate * (target_difficulty - old_diff)
        new_diff = max(0.15, min(0.90, round(new_diff, 3)))

        if abs(new_diff - old_diff) > 0.005:  # meaningful change
            changes.append({
                "id": q.id,
                "skill_id": q.skill_id,
                "old_difficulty": round(old_diff, 3),
                "new_difficulty": new_diff,
                "accuracy": round(empirical_accuracy, 3),
                "answers": ta,
                "discrimination": round(q.discrimination or 0, 3),
            })
            if not dry_run:
                q.difficulty = new_diff
                q.last_calibrated_at = datetime.datetime.utcnow()
            calibrated += 1
        else:
            skipped += 1

    if not dry_run:
        db.commit()

    return {"calibrated": calibrated, "skipped": skipped, "changes": changes}
