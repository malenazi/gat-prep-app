// ── Types matching actual backend API responses ──────────────────────────────

// ── Auth ─────────────────────────────────────────────────────────────────────
export interface RegisterPayload {
  name: string;
  email: string;
  password: string;
}

export interface LoginPayload {
  email: string;
  password: string;
}

export interface AuthResponse {
  token: string;
  user: { id: number; name: string };
}

// ── User (GET /api/me) ──────────────────────────────────────────────────────
export type LeagueTier = 'bronze' | 'silver' | 'gold' | 'platinum' | 'diamond' | 'champion';

export interface PredictedScore {
  low: number;
  mid: number;
  high: number;
  verbal_mastery: number;
  quant_mastery: number;
}

export interface UserAbility {
  skill_id: string;
  name_ar: string;
  section: string;
  icon: string;
  theta: number;
  mastery: number;
  questions_seen: number;
  correct_count: number;
}

export interface ApiUser {
  id: number;
  name: string;
  email: string;
  daily_minutes: number;
  current_day: number;
  diagnostic_completed: boolean;
  xp: number;
  streak: number;
  streak_longest: number;
  league: LeagueTier;
  is_admin: boolean;
  mock_attempts: number;
  mock_score: number;
  mock_max_attempts: number;
  predicted_score: PredictedScore;
  abilities: UserAbility[];
}

// ── Questions (from format_question) ────────────────────────────────────────
export interface QuestionOption {
  key: string;
  label: string;
  text_ar: string;
}

export interface ApiQuestion {
  id: number;
  skill_id: string;
  question_type: string;
  difficulty: number;
  text_ar: string;
  passage_ar: string | null;
  options: QuestionOption[];
  paper_only: boolean;
}

// ── Diagnostic ──────────────────────────────────────────────────────────────
export interface DiagnosticStartResponse {
  message: string;
  total_questions: number;
}

export interface DiagnosticNextResponse {
  done: boolean;
  progress?: number;
  total?: number;
  question?: ApiQuestion;
  total_answered?: number;
}

export interface AnswerPayload {
  question_id: number;
  selected_option: string;
  time_spent_seconds: number;
}

export interface AnswerFeedback {
  is_correct: boolean;
  correct_option: string;
  explanation_ar: string;
  solution_steps_ar: string[] | null;
}

export interface PracticeAnswerFeedback extends AnswerFeedback {
  xp_earned: number;
}

export interface DiagnosticCompleteResponse {
  message: string;
  predicted_score: PredictedScore;
}

// ── Study Plan ──────────────────────────────────────────────────────────────
export interface FocusSkill {
  id: string;
  name_ar: string;
}

export interface StudyPlanDay {
  day: number;
  phase: 'foundation' | 'building' | 'peak';
  focus_skills: FocusSkill[];
  target_questions: number;
  completed_questions: number;
  is_mock_day: boolean;
  is_rest_day: boolean;
  completed: boolean;
  is_today: boolean;
}

export interface TodayPlan {
  day: number;
  phase: string;
  focus_skills: FocusSkill[];
  target_questions: number;
  completed_questions: number;
  is_mock_day: boolean;
  is_rest_day: boolean;
  remaining: number;
  message?: string;
}

// ── Practice ────────────────────────────────────────────────────────────────
export interface PracticeNextResponse {
  done: boolean;
  question?: ApiQuestion;
  message?: string;
}

// ── Analytics ───────────────────────────────────────────────────────────────
export interface DailyTrend {
  date: string;
  accuracy: number;
  total: number;
}

export interface SkillBreakdown {
  skill_id: string;
  name_ar: string;
  section: string;
  icon: string;
  correct: number;
  total: number;
  accuracy: number;
}

export interface ApiAnalytics {
  total_questions: number;
  total_correct: number;
  accuracy: number;
  daily_trend: DailyTrend[];
  skill_breakdown: SkillBreakdown[];
  predicted_score: PredictedScore;
}

// ── Badges ──────────────────────────────────────────────────────────────────
export interface ApiBadge {
  id: string;
  name_ar: string;
  description_ar: string;
  icon: string;
  earned: boolean;
}

// ── Skills ──────────────────────────────────────────────────────────────────
export interface ApiSkill {
  id: string;
  section: string;
  name_ar: string;
  name_en: string;
  exam_weight: number;
  icon: string;
}

// ── Feedback ────────────────────────────────────────────────────────────────
export interface FeedbackPayload {
  rating: number;
  comment?: string;
  trigger: string;
  page?: string;
}

// ── Admin ───────────────────────────────────────────────────────────────────
export interface AdminFeedbackItem {
  id: number;
  user_id: number;
  rating: number;
  comment: string | null;
  trigger: string;
  page: string | null;
  created_at: string;
}

export interface AdminFeedbackAnalytics {
  total: number;
  avg_rating: number;
  distribution: Record<number, number>;
  by_trigger: Record<string, { count: number; total_rating: number; avg_rating: number }>;
  recent_comments: { rating: number; comment: string; trigger: string; created_at: string }[];
}

export interface AdminQuestion {
  id: number;
  skill_id: string;
  skill_name_ar: string;
  section: string;
  question_type: string;
  difficulty: number;
  text_ar: string;
  passage_ar: string | null;
  option_a: string;
  option_b: string;
  option_c: string;
  option_d: string;
  correct_option: string;
  explanation_ar: string | null;
  solution_steps_ar: string[] | null;
  tags: string;
  stage: string;
  status: string;
  times_answered: number;
  times_correct: number;
  accuracy: number;
  avg_time_seconds: number;
  discrimination: number;
  original_difficulty: number | null;
  last_calibrated_at: string | null;
  rating_overall: number | null;
  rating_clarity: number | null;
  rating_cognitive: number | null;
  rating_distractors: number | null;
  rating_difficulty_align: number | null;
  rating_explanation: number | null;
  rating_fairness: number | null;
  rating_discrimination: number | null;
}

export interface QuestionAnalysis {
  total: number;
  by_stage: Record<string, number>;
  by_status: Record<string, number>;
  by_skill: Record<string, number>;
  flagged_count: number;
  flagged: Array<{
    id: number;
    skill_id: string;
    difficulty: number;
    accuracy: number | null;
    discrimination: number;
    issues: string[];
  }>;
}

export interface QuestionPayload {
  skill_id: string;
  question_type: string;
  difficulty: number;
  text_ar: string;
  passage_ar?: string | null;
  option_a: string;
  option_b: string;
  option_c: string;
  option_d: string;
  correct_option: string;
  explanation_ar?: string | null;
  solution_steps_ar?: string | null;
}

export interface AdminUsersResponse {
  total_users: number;
  active_today: number;
  avg_streak: number;
  avg_day: number;
  completed_course: number;
  mock_taken: number;
  mock_avg_score: number;
  users: {
    id: number;
    name: string;
    email: string;
    current_day: number;
    xp: number;
    streak: number;
    last_active: string | null;
    mock_attempts: number;
    mock_score: number;
  }[];
}

// ── Mock Exam ───────────────────────────────────────────────────────────────
export interface MockStartResponse {
  attempt_id: number;
  attempt_number: number;
  total_questions: number;
  verbal_count: number;
  quant_count: number;
  verbal_minutes: number;
  quant_minutes: number;
  question_ids: number[];
}

export interface MockCompleteResponse {
  attempt_id: number;
  attempt_number: number;
  score: number;
  total: number;
  correct: number;
  verbal_correct: number;
  verbal_total: number;
  quant_correct: number;
  quant_total: number;
  verbal_pct: number;
  quant_pct: number;
}

export interface MockAttemptSummary {
  id: number;
  attempt_number: number;
  score: number;
  total: number;
  correct: number;
  verbal_correct: number;
  verbal_total: number;
  quant_correct: number;
  quant_total: number;
  verbal_pct: number;
  quant_pct: number;
  completed_at: string;
}

export interface MockAttemptDetailQuestion {
  question_id: number;
  text_ar: string;
  passage_ar: string | null;
  options: { key: string; text_ar: string }[];
  selected_option: string;
  correct_option: string;
  is_correct: boolean;
  time_spent_seconds: number;
  explanation_ar: string | null;
  skill_id: string;
  skill_name_ar: string;
  section: string;
}

export interface MockAttemptDetail {
  attempt_number: number;
  score: number;
  total: number;
  correct: number;
  verbal_correct: number;
  verbal_total: number;
  quant_correct: number;
  quant_total: number;
  completed_at: string;
  questions: MockAttemptDetailQuestion[];
  skill_breakdown: { skill_id: string; skill_name_ar: string; correct: number; total: number; pct: number }[];
}
