import json, datetime
from sqlalchemy import Column, Integer, Float, String, Boolean, Text, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    daily_minutes = Column(Integer, default=120)  # chosen study time
    current_day = Column(Integer, default=0)  # 0=not started, 1-30
    course_started_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    # gamification
    xp = Column(Integer, default=0)
    streak_current = Column(Integer, default=0)
    streak_longest = Column(Integer, default=0)
    streak_freezes = Column(Integer, default=2)
    last_active_date = Column(String, nullable=True)
    league = Column(String, default="bronze")  # bronze/silver/gold/platinum/diamond/champion
    diagnostic_completed = Column(Boolean, default=False)
    # mock exam
    mock_attempts = Column(Integer, default=0)  # count of completed mock attempts
    mock_score = Column(Integer, default=0)  # best score across all attempts
    is_admin = Column(Boolean, default=False)

    abilities = relationship("UserAbility", back_populates="user")
    responses = relationship("UserResponse", back_populates="user")


class PasswordResetToken(Base):
    __tablename__ = "password_reset_tokens"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    token_hash = Column(String, unique=True, index=True, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    expires_at = Column(DateTime, nullable=False)
    used_at = Column(DateTime, nullable=True)

class Skill(Base):
    __tablename__ = "skills"
    id = Column(String, primary_key=True)
    section = Column(String, nullable=False)
    name_ar = Column(String, nullable=False)
    name_en = Column(String, nullable=False)
    exam_weight = Column(Float, nullable=False)
    icon = Column(String, default="📘")

class UserAbility(Base):
    __tablename__ = "user_abilities"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True, nullable=False)
    skill_id = Column(String, ForeignKey("skills.id"), index=True, nullable=False)
    theta = Column(Float, default=0.0)
    questions_seen = Column(Integer, default=0)
    correct_count = Column(Integer, default=0)
    mastery = Column(Float, default=0.0)
    last_updated = Column(DateTime, default=datetime.datetime.utcnow)
    user = relationship("User", back_populates="abilities")

class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    source_key = Column(String, index=True, nullable=True)
    batch_id = Column(String, index=True, nullable=True)
    generation_prompt_version = Column(String, nullable=True)
    authoring_source = Column(String, nullable=True)
    variant_group = Column(String, index=True, nullable=True)
    skill_id = Column(String, ForeignKey("skills.id"), index=True, nullable=False)
    question_type = Column(String, nullable=False)
    difficulty = Column(Float, default=0.5)
    text_ar = Column(Text, nullable=False)
    passage_ar = Column(Text, nullable=True)
    content_format = Column(String, default="plain")
    figure_svg = Column(Text, nullable=True)
    figure_alt = Column(Text, nullable=True)
    table_ar = Column(Text, nullable=True)
    table_caption = Column(Text, nullable=True)
    comparison_columns = Column(Text, nullable=True)
    option_a = Column(String, nullable=False)
    option_b = Column(String, nullable=False)
    option_c = Column(String, nullable=False)
    option_d = Column(String, nullable=False)
    correct_option = Column(String, nullable=False)
    explanation_ar = Column(Text, nullable=True)
    solution_steps_ar = Column(Text, nullable=True)
    tags = Column(String, nullable=True)  # comma-separated topic tags
    paper_only = Column(Boolean, default=False)
    # Classification
    stage = Column(String, default="general")  # diagnostic/foundation/building/peak/mock/general
    status = Column(String, default="active")  # active/review/disabled
    # Analytics (updated after each answer)
    times_answered = Column(Integer, default=0)
    times_correct = Column(Integer, default=0)
    avg_time_seconds = Column(Float, default=0.0)
    discrimination = Column(Float, default=0.0)  # IRT discrimination index
    # Calibration
    original_difficulty = Column(Float, nullable=True)  # seed value, preserved
    last_calibrated_at = Column(DateTime, nullable=True)
    # Quality Rating (IQ/aptitude test standards, averaged from 3 passes)
    rating_clarity = Column(Float, nullable=True)        # 1-5: text clarity, no ambiguity
    rating_cognitive = Column(Float, nullable=True)      # 1-5: cognitive level (Bloom's)
    rating_distractors = Column(Float, nullable=True)    # 1-5: distractor quality
    rating_difficulty_align = Column(Float, nullable=True) # 1-5: difficulty matches complexity
    rating_explanation = Column(Float, nullable=True)    # 1-5: explanation quality
    rating_fairness = Column(Float, nullable=True)       # 1-5: cultural fairness
    rating_discrimination = Column(Float, nullable=True) # 1-5: discriminating power potential
    rating_overall = Column(Float, nullable=True)        # average of 7 criteria
    rating_passes_done = Column(Integer, default=0)      # 0-3 review passes completed
    rating_notes = Column(Text, nullable=True)           # improvement notes from review

class UserResponse(Base):
    __tablename__ = "user_responses"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True, nullable=False)
    question_id = Column(Integer, ForeignKey("questions.id"), index=True, nullable=False)
    session_type = Column(String, nullable=False)  # diagnostic/drill/mock/review
    attempt_id = Column(Integer, ForeignKey("mock_attempts.id"), index=True, nullable=True)  # links mock answers to attempt
    selected_option = Column(String, nullable=False)
    is_correct = Column(Boolean, nullable=False)
    time_spent_seconds = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    user = relationship("User", back_populates="responses")

class MockAttempt(Base):
    __tablename__ = "mock_attempts"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True, nullable=False)
    attempt_number = Column(Integer, nullable=False)
    score = Column(Integer, default=0)
    total_questions = Column(Integer, default=0)
    correct_count = Column(Integer, default=0)
    verbal_correct = Column(Integer, default=0)
    verbal_total = Column(Integer, default=0)
    quant_correct = Column(Integer, default=0)
    quant_total = Column(Integer, default=0)
    is_preview = Column(Boolean, default=False)
    started_at = Column(DateTime, default=datetime.datetime.utcnow)
    completed_at = Column(DateTime, nullable=True)

class AppConfig(Base):
    __tablename__ = "app_config"
    key = Column(String, primary_key=True)
    value = Column(String, nullable=False)

class StudyPlan(Base):
    __tablename__ = "study_plans"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True, nullable=False)
    day_number = Column(Integer, nullable=False)
    phase = Column(String, nullable=False)
    focus_skills = Column(Text, nullable=False)
    target_questions = Column(Integer, default=30)
    completed_questions = Column(Integer, default=0)
    is_mock_day = Column(Boolean, default=False)
    is_rest_day = Column(Boolean, default=False)
    completed = Column(Boolean, default=False)

class Badge(Base):
    __tablename__ = "badges"
    id = Column(String, primary_key=True)
    name_ar = Column(String, nullable=False)
    description_ar = Column(String, nullable=False)
    icon = Column(String, default="🏆")
    criteria_type = Column(String, nullable=False)
    criteria_value = Column(Integer, default=0)

class UserBadge(Base):
    __tablename__ = "user_badges"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True, nullable=False)
    badge_id = Column(String, ForeignKey("badges.id"), index=True, nullable=False)
    earned_at = Column(DateTime, default=datetime.datetime.utcnow)

class Feedback(Base):
    __tablename__ = "feedback"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True, nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(Text, nullable=True)
    trigger = Column(String, nullable=False)
    page = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
