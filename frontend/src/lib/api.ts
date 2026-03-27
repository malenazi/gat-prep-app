import type {
  AuthResponse,
  RegisterPayload,
  LoginPayload,
  ApiUser,
  DiagnosticStartResponse,
  DiagnosticNextResponse,
  AnswerPayload,
  AnswerFeedback,
  PracticeAnswerFeedback,
  DiagnosticCompleteResponse,
  StudyPlanDay,
  TodayPlan,
  PracticeNextResponse,
  ApiAnalytics,
  ApiBadge,
  ApiSkill,
  FeedbackPayload,
  AdminFeedbackItem,
  AdminFeedbackAnalytics,
  AdminUsersResponse,
  AdminQuestion,
  QuestionPayload,
  MockStartResponse,
  MockCompleteResponse,
  MockAttemptSummary,
  MockAttemptDetail,
  ApiQuestion,
  QuestionAnalysis,
} from '@/types';

const BASE = '/api';

function getToken(): string | null {
  return localStorage.getItem('gat_token');
}

export function setToken(t: string): void {
  localStorage.setItem('gat_token', t);
}

export function clearToken(): void {
  localStorage.removeItem('gat_token');
}

async function req<T>(path: string, opts: RequestInit = {}): Promise<T> {
  const headers: Record<string, string> = { 'Content-Type': 'application/json' };
  const token = getToken();
  if (token) headers['Authorization'] = `Bearer ${token}`;
  const res = await fetch(`${BASE}${path}`, { ...opts, headers });
  if (res.status === 401) {
    clearToken();
    window.location.href = '/';
    throw new Error('unauthorized');
  }
  if (!res.ok) {
    const e = await res.json().catch(() => ({}));
    throw new Error(e.detail || e.message || res.statusText || 'خطأ في الخادم');
  }
  return res.json();
}

export const api = {
  // Auth
  register: (d: RegisterPayload) => req<AuthResponse>('/auth/register', { method: 'POST', body: JSON.stringify(d) }),
  login: (d: LoginPayload) => req<AuthResponse>('/auth/login', { method: 'POST', body: JSON.stringify(d) }),

  // User
  me: () => req<ApiUser>('/me'),
  updateSettings: (d: { daily_minutes: number }) => req<{ ok: boolean }>('/me/settings', { method: 'PUT', body: JSON.stringify(d) }),

  // Diagnostic
  startDiagnostic: () => req<DiagnosticStartResponse>('/diagnostic/start', { method: 'POST' }),
  diagnosticNext: () => req<DiagnosticNextResponse>('/diagnostic/next'),
  diagnosticAnswer: (d: AnswerPayload) => req<AnswerFeedback>('/diagnostic/answer', { method: 'POST', body: JSON.stringify(d) }),
  completeDiagnostic: () => req<DiagnosticCompleteResponse>('/diagnostic/complete', { method: 'POST' }),

  // Study Plan
  studyPlan: () => req<StudyPlanDay[]>('/study-plan'),
  today: () => req<TodayPlan>('/study-plan/today'),

  // Practice
  practiceNext: () => req<PracticeNextResponse>('/practice/next'),
  practiceAnswer: (d: AnswerPayload) => req<PracticeAnswerFeedback>('/practice/answer', { method: 'POST', body: JSON.stringify(d) }),

  // Utility
  advanceDay: () => req<{ current_day: number }>('/advance-day', { method: 'POST' }),
  analytics: () => req<ApiAnalytics>('/analytics'),
  badges: () => req<ApiBadge[]>('/badges'),
  skills: () => req<ApiSkill[]>('/skills'),

  // Feedback
  submitFeedback: (d: FeedbackPayload) => req<{ message: string }>('/feedback', { method: 'POST', body: JSON.stringify(d) }),

  // Admin
  adminFeedback: (days = 30, trigger = '') =>
    req<AdminFeedbackItem[]>(`/admin/feedback?days=${days}${trigger ? `&trigger=${trigger}` : ''}`),
  adminFeedbackAnalytics: () => req<AdminFeedbackAnalytics>('/admin/feedback/analytics'),
  adminUsers: () => req<AdminUsersResponse>('/admin/users'),
  adminQuestions: () => req<AdminQuestion[]>('/admin/questions'),
  adminAddQuestion: (d: QuestionPayload) => req<{ id: number; message: string }>('/admin/questions', { method: 'POST', body: JSON.stringify(d) }),
  adminUpdateQuestion: (id: number, d: QuestionPayload) => req<{ message: string }>(`/admin/questions/${id}`, { method: 'PUT', body: JSON.stringify(d) }),
  adminDeleteQuestion: (id: number) => req<{ message: string }>(`/admin/questions/${id}`, { method: 'DELETE' }),
  adminQuestionAnalysis: () => req<QuestionAnalysis>('/admin/questions/analysis'),

  // Mock Exam
  mockStart: (preview = false) => req<MockStartResponse>(`/mock/start?preview=${preview}`, { method: 'POST' }),
  mockQuestion: (id: number) => req<ApiQuestion>(`/mock/question/${id}`),
  mockAnswer: (d: { question_id: number; selected_option: string; time_spent_seconds: number; attempt_id: number }) =>
    req<{ is_correct: boolean }>('/mock/answer', { method: 'POST', body: JSON.stringify(d) }),
  mockComplete: (attempt_id: number) => req<MockCompleteResponse>('/mock/complete', { method: 'POST', body: JSON.stringify({ attempt_id }) }),
  mockResults: () => req<MockCompleteResponse>('/mock/results'),
  mockAttempts: () => req<MockAttemptSummary[]>('/mock/attempts'),
  mockAttemptDetail: (id: number) => req<MockAttemptDetail>(`/mock/attempts/${id}`),
  mockAttemptStatus: (id: number) => req<{ attempt_id: number; completed: boolean; answers_submitted: number; total_questions: number }>(`/mock/attempts/${id}/status`),
  adminGetConfig: () => req<{ mock_max_attempts: number }>('/admin/config'),
  adminSetMockAttempts: (value: number) => req<{ mock_max_attempts: number }>('/admin/config/mock-attempts', { method: 'PUT', body: JSON.stringify({ value }) }),
};
