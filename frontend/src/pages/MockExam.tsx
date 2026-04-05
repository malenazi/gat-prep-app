import { useState, useEffect, useRef, useCallback } from 'react';
import { useNavigate, useSearchParams } from 'react-router-dom';
import { api } from '@/lib/api';
import { QuestionFeedbackCard } from '@/components/questions/QuestionFeedbackCard';
import { QuestionOptions } from '@/components/questions/QuestionOptions';
import { QuestionPrompt } from '@/components/questions/QuestionPrompt';
import { useAuth } from '@/hooks/useAuth';
import { ScoreRing } from '@/components/shared/ScoreRing';
import { defaultQuestionAppearance } from '@/lib/questionPresentation';
import { nowMs } from '@/lib/time';
import type { ApiQuestion, MockStartResponse, MockCompleteResponse, MockAttemptSummary, MockAttemptDetail, TodayPlan } from '@/types';
import { Clock, BookOpen, Calculator, AlertTriangle, CheckCircle, Shield, ChevronRight, ArrowRight, History, XCircle, RotateCcw } from 'lucide-react';

const MOCK_SESSION_KEY = 'mock_exam_session';

interface MockSession {
  attemptId: number;
  questionIds: number[];
  currentIndex: number;
  section: 'verbal' | 'quant';
  timeLeft: number;
  verbalCount: number;
  quantCount: number;
}

function saveMockSession(session: MockSession) {
  localStorage.setItem(MOCK_SESSION_KEY, JSON.stringify(session));
}

function loadMockSession(): MockSession | null {
  try {
    const raw = localStorage.getItem(MOCK_SESSION_KEY);
    return raw ? JSON.parse(raw) : null;
  } catch { return null; }
}

function clearMockSession() {
  localStorage.removeItem(MOCK_SESSION_KEY);
}

type Phase = 'instructions' | 'exam' | 'results' | 'history' | 'detail';
type Section = 'verbal' | 'quant';

export default function MockExam() {
  const { user, loadUser } = useAuth();
  const nav = useNavigate();
  const [searchParams] = useSearchParams();
  const isPreview = searchParams.get('preview') === 'true' && user?.is_admin;

  const [phase, setPhase] = useState<Phase>('instructions');
  const [config, setConfig] = useState<MockStartResponse | null>(null);
  const [results, setResults] = useState<MockCompleteResponse | null>(null);
  const [attemptId, setAttemptId] = useState<number | null>(null);
  const [todayPlan, setTodayPlan] = useState<TodayPlan | null | undefined>(isPreview ? null : undefined);

  // History / detail state
  const [attempts, setAttempts] = useState<MockAttemptSummary[]>([]);
  const [detail, setDetail] = useState<MockAttemptDetail | null>(null);
  const [historyLoading, setHistoryLoading] = useState(false);

  // Exam state
  const [questionIds, setQuestionIds] = useState<number[]>([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [question, setQuestion] = useState<ApiQuestion | null>(null);
  const [selected, setSelected] = useState<string | null>(null);
  const [section, setSection] = useState<Section>('verbal');
  const [timeLeft, setTimeLeft] = useState(0);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [, setAnswers] = useState<{ qid: number; option: string }[]>([]);
  const startTimeRef = useRef<number>(0);
  const initCheckedRef = useRef(false);
  const appearance = defaultQuestionAppearance;

  const attemptsUsed = user?.mock_attempts ?? 0;
  const maxAttempts = user?.mock_max_attempts ?? 1;
  const isRequiredTodayMock = Boolean(
    todayPlan &&
    todayPlan.is_mock_day &&
    todayPlan.completed_questions < todayPlan.target_questions,
  );
  const displayMaxAttempts = Math.max(
    maxAttempts,
    isRequiredTodayMock ? attemptsUsed + 1 : maxAttempts,
  );
  const allAttemptsUsed = attemptsUsed >= maxAttempts && !isPreview && !isRequiredTodayMock;
  const nextAttemptNumber = attemptsUsed + 1;
  const isLastAttempt = !isRequiredTodayMock && nextAttemptNumber === maxAttempts;
  const hasMoreAttempts = attemptsUsed < maxAttempts;

  useEffect(() => {
    if (isPreview) {
      setTodayPlan(null);
      return;
    }

    let cancelled = false;
    api.today()
      .then((plan) => {
        if (!cancelled) setTodayPlan(plan);
      })
      .catch(() => {
        if (!cancelled) setTodayPlan(null);
      });

    return () => {
      cancelled = true;
    };
  }, [isPreview]);

  const loadHistory = useCallback(async () => {
    setHistoryLoading(true);
    try {
      const list = await api.mockAttempts();
      setAttempts(list);
      setPhase('history');
    } catch {
      // Ignore history load failures and keep the current state unchanged.
    }
    setHistoryLoading(false);
  }, []);

  const loadQuestion = useCallback(async (qid: number) => {
    setSelected(null);
    setQuestion(null);
    try {
      const nextQuestion = await api.mockQuestion(qid);
      setQuestion(nextQuestion);
      startTimeRef.current = nowMs();
    } catch {
      setError('Error loading question');
    }
  }, []);

  const finishExam = useCallback(async () => {
    if (attemptId === null) return;
    setLoading(true);
    try {
      const res = await api.mockComplete(attemptId);
      setResults(res);
      setPhase('results');
      clearMockSession();
      await loadUser();
    } catch (e: unknown) {
      setError(e instanceof Error ? e.message : 'An error occurred');
    }
    setLoading(false);
  }, [attemptId, loadUser]);

  const handleSectionTimeout = useCallback(() => {
    if (section === 'verbal' && config) {
      const quantStart = config.verbal_count;
      if (quantStart >= questionIds.length || config.quant_count <= 0) {
        void finishExam();
        return;
      }
      setSection('quant');
      setCurrentIndex(quantStart);
      setTimeLeft(config.quant_minutes * 60);
      void loadQuestion(questionIds[quantStart]);
      return;
    }

    void finishExam();
  }, [config, finishExam, loadQuestion, questionIds, section]);

  // On mount: try to resume saved session, else check history
  useEffect(() => {
    if (initCheckedRef.current) return;
    if (!isPreview && todayPlan === undefined) return;
    initCheckedRef.current = true;
    const saved = loadMockSession();

    // Priority 1: Resume an in-progress exam from localStorage
    if (saved && !isPreview) {
      api.mockAttemptStatus(saved.attemptId).then(status => {
        if (!status.completed) {
          // Resume session
          setAttemptId(saved.attemptId);
          setQuestionIds(saved.questionIds);
          setCurrentIndex(saved.currentIndex);
          setSection(saved.section);
          setTimeLeft(saved.timeLeft);
          setConfig({
            attempt_id: saved.attemptId,
            attempt_number: 0,
            total_questions: saved.questionIds.length,
            verbal_count: saved.verbalCount,
            quant_count: saved.quantCount,
            verbal_minutes: 35,
            quant_minutes: 35,
            question_ids: saved.questionIds,
          });
          loadQuestion(saved.questionIds[saved.currentIndex]).then(() => {
            setPhase('exam');
          }).catch(() => {
            clearMockSession();
            if (allAttemptsUsed) void loadHistory();
          });
        } else {
          // Attempt already completed — clear and show history or start
          clearMockSession();
          if (allAttemptsUsed) void loadHistory();
        }
      }).catch(() => {
        clearMockSession();
        if (allAttemptsUsed) void loadHistory();
      });
      return; // Don't fall through
    }

    // Priority 2: No saved session — show history if all attempts used
    if (allAttemptsUsed) {
      void loadHistory();
    }
  }, [allAttemptsUsed, isPreview, loadHistory, loadQuestion, todayPlan]);

  // Timer
  useEffect(() => {
    if (phase !== 'exam' || timeLeft <= 0) return;
    const interval = setInterval(() => {
      setTimeLeft(prev => {
        const newTime = prev <= 1 ? 0 : prev - 1;
        // Save every 10 seconds
        if (newTime > 0 && newTime % 10 === 0) {
          const saved = loadMockSession();
          if (saved) saveMockSession({ ...saved, timeLeft: newTime });
        }
        if (prev <= 1) {
          clearInterval(interval);
          handleSectionTimeout();
        }
        return newTime;
      });
    }, 1000);
    return () => clearInterval(interval);
  }, [handleSectionTimeout, phase, timeLeft]);

  const loadAttemptDetail = async (id: number) => {
    setHistoryLoading(true);
    try {
      const d = await api.mockAttemptDetail(id);
      setDetail(d);
      setPhase('detail');
    } catch { /* ignore */ }
    setHistoryLoading(false);
  };

  const startExam = async () => {
    setLoading(true);
    setError('');
    try {
      const cfg = await api.mockStart(isPreview);
      setConfig(cfg);
      setAttemptId(cfg.attempt_id);
      setQuestionIds(cfg.question_ids);
      setSection('verbal');
      setTimeLeft(cfg.verbal_minutes * 60);
      setCurrentIndex(0);
      setAnswers([]);
      await loadQuestion(cfg.question_ids[0]);
      setPhase('exam');
      saveMockSession({
        attemptId: cfg.attempt_id,
        questionIds: cfg.question_ids,
        currentIndex: 0,
        section: 'verbal',
        timeLeft: cfg.verbal_minutes * 60,
        verbalCount: cfg.verbal_count,
        quantCount: cfg.quant_count,
      });
    } catch (e: unknown) {
      setError(e instanceof Error ? e.message : 'Error occurred');
    }
    setLoading(false);
  };

  const submitAnswer = async (option: string) => {
    if (selected || !question || attemptId === null) return;
    setSelected(option);
    const elapsed = Math.round((nowMs() - startTimeRef.current) / 1000);

    try {
      await api.mockAnswer({ question_id: question.id, selected_option: option, time_spent_seconds: elapsed, attempt_id: attemptId });
    } catch {
      console.warn('Failed to save answer, continuing');
    }
    setAnswers(prev => [...prev, { qid: question.id, option }]);

    setTimeout(() => {
      const nextIndex = currentIndex + 1;
      if (config && nextIndex >= questionIds.length) {
        void finishExam();
      } else if (config && section === 'verbal' && nextIndex >= config.verbal_count) {
        setSection('quant');
        setCurrentIndex(nextIndex);
        setTimeLeft(config.quant_minutes * 60);
        const saved = loadMockSession();
        if (saved) saveMockSession({ ...saved, currentIndex: nextIndex, section: 'quant', timeLeft: config.quant_minutes * 60 });
        void loadQuestion(questionIds[nextIndex]);
      } else {
        setCurrentIndex(nextIndex);
        const saved = loadMockSession();
        if (saved) saveMockSession({ ...saved, currentIndex: nextIndex });
        void loadQuestion(questionIds[nextIndex]);
      }
    }, 500);
  };

  const formatTime = (s: number) => {
    const m = Math.floor(s / 60);
    const sec = s % 60;
    return `${m}:${sec.toString().padStart(2, '0')}`;
  };

  const sectionLabel = section === 'verbal' ? 'Verbal Section' : 'Quantitative Section';
  const SectionIcon = section === 'verbal' ? BookOpen : Calculator;
  const sectionProgress = config ? (
    section === 'verbal'
      ? `${currentIndex + 1} / ${config.verbal_count}`
      : `${currentIndex - config.verbal_count + 1} / ${config.quant_count}`
  ) : '';

  const scoreColor = (score: number) =>
    score >= 80 ? 'text-emerald-600' : score >= 65 ? 'text-teal-600' : score >= 50 ? 'text-amber-600' : 'text-red-500';

  // ── Instructions Phase ──
  if (phase === 'instructions' && !isPreview && todayPlan === undefined) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-slate-50 dark:bg-slate-950">
        <div className="w-8 h-8 border-3 border-amber-400 border-t-transparent rounded-full animate-spin" />
      </div>
    );
  }

  if (phase === 'instructions' && !allAttemptsUsed) {
    return (
      <div className="min-h-screen bg-slate-50 flex items-center justify-center p-4 text-slate-800 dark:bg-slate-950 dark:text-slate-100" data-testid="mock-page">
        <div className="max-w-2xl w-full">
          {/* Header */}
          <div className="text-center mb-8">
            <div className="w-20 h-20 bg-gradient-to-br from-amber-500 to-orange-500 rounded-2xl flex items-center justify-center mx-auto mb-4 shadow-lg">
              <Shield className="w-10 h-10 text-white" />
            </div>
            <h1 className="text-3xl font-black text-slate-800 mb-2 dark:text-slate-100">Final Mock Exam</h1>
            <p className="text-slate-500 dark:text-slate-400">Full simulation of the general aptitude test</p>

            {/* Attempt counter */}
            <div className="inline-flex items-center gap-1.5 bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 text-sm font-bold px-4 py-2 rounded-full mt-3">
              Attempt {nextAttemptNumber} of {displayMaxAttempts}
            </div>

            {isPreview && (
              <div className="inline-flex items-center gap-1.5 bg-amber-100 text-amber-700 text-xs font-bold px-3 py-1.5 rounded-full mt-3 mr-2">
                <Shield className="w-3.5 h-3.5" /> Preview Mode — Score will not be saved
              </div>
            )}
          </div>

          {/* Exam Info Card */}
          <div className="bg-white rounded-2xl border border-slate-200 p-6 mb-6 space-y-4 dark:border-slate-800 dark:bg-slate-900">
            <h2 className="font-bold text-slate-800 text-lg mb-3 dark:text-slate-100">Exam Instructions</h2>

            <div className="grid grid-cols-2 gap-4">
              <div className="bg-blue-50 border border-blue-200 rounded-xl p-4 text-center">
                <BookOpen className="w-6 h-6 text-blue-600 mx-auto mb-2" />
                <p className="font-bold text-blue-800">Verbal Section</p>
                <p className="text-sm text-blue-600">34 questions • 35 minutes</p>
              </div>
              <div className="bg-violet-50 border border-violet-200 rounded-xl p-4 text-center">
                <Calculator className="w-6 h-6 text-violet-600 mx-auto mb-2" />
                <p className="font-bold text-violet-800">Quantitative Section</p>
                <p className="text-sm text-violet-600">31 questions • 35 minutes</p>
              </div>
            </div>

            {/* Last attempt warning */}
            {isLastAttempt && !isPreview && (
              <div className="bg-red-50 border border-red-200 rounded-xl p-4">
                <div className="flex items-start gap-3">
                  <AlertTriangle className="w-5 h-5 text-red-600 mt-0.5 shrink-0" />
                  <div className="text-sm text-red-800 font-bold">
                    This is your last attempt — the exam cannot be retaken after this
                  </div>
                </div>
              </div>
            )}

            <div className="bg-amber-50 border border-amber-200 rounded-xl p-4">
              <div className="flex items-start gap-3">
                <AlertTriangle className="w-5 h-5 text-amber-600 mt-0.5 shrink-0" />
                <div className="text-sm text-amber-800 space-y-1.5">
                  <p className="font-bold">Important Warnings:</p>
                  <p>• Total: <strong>65 questions</strong> in <strong>70 minutes</strong></p>
                  <p>• Questions <strong>are different from daily training</strong></p>
                  <p>• Correct answers are not shown during the exam</p>
                  <p>• Automatically moves to next section when time expires</p>
                  <p>• Cannot return to previous questions</p>
                </div>
              </div>
            </div>

            <div className="bg-slate-50 border border-slate-200 rounded-xl p-4 dark:border-slate-800 dark:bg-slate-950">
              <p className="text-sm text-slate-600"><strong>Tip:</strong> Read each question carefully. If you don't know the answer, choose your best guess and move to the next question. Don't spend too much time on one question.</p>
            </div>
          </div>

          {loadMockSession() && !isPreview && (
            <div className="bg-amber-50 border border-amber-200 rounded-xl p-4 mb-4">
              <p className="font-bold text-amber-800 mb-2">You have an exam in progress</p>
              <p className="text-sm text-amber-600 mb-3">You can resume the exam from where you left off</p>
              {/* The useEffect above will handle auto-resume */}
            </div>
          )}

          {error && (
            <div className="bg-red-50 border border-red-200 rounded-xl p-3 mb-4 text-center text-sm text-red-600">{error}</div>
          )}

          <div className="flex gap-3">
            <button onClick={() => nav(isPreview ? '/admin' : '/')}
              className="flex-1 text-slate-500 font-medium py-4 hover:text-slate-700 transition">
              Back
            </button>
            <button onClick={startExam} disabled={loading} data-testid="mock-start"
              className="flex-1 bg-gradient-to-l from-amber-600 to-amber-500 text-white font-bold text-lg py-4 rounded-xl shadow-lg hover:shadow-xl transition-all active:scale-[0.98] disabled:opacity-50">
              {loading ? '...' : 'Start Exam'}
            </button>
          </div>

          {/* Link to previous attempts */}
          {attemptsUsed > 0 && !isPreview && (
            <button onClick={loadHistory}
              className="w-full mt-4 flex items-center justify-center gap-2 text-teal-600 font-medium text-sm py-3 hover:text-teal-700 transition">
              <History className="w-4 h-4" />
              View Previous Attempts ({attemptsUsed})
            </button>
          )}
        </div>
      </div>
    );
  }

  // ── Exam Phase ──
  if (phase === 'exam' && question) {
    const isUrgent = timeLeft < 120;
    const isWarning = timeLeft < 300 && !isUrgent;

    return (
      <div className="min-h-screen bg-slate-50 flex flex-col dark:bg-slate-950" data-testid="mock-page">
        {/* Exam Header */}
        <div className={`px-4 py-3 flex items-center justify-between ${section === 'verbal' ? 'bg-blue-600' : 'bg-violet-600'} text-white`}>
          <div className="flex items-center gap-2">
            <SectionIcon className="w-5 h-5" />
            <span className="font-bold text-sm">{sectionLabel}</span>
            <span className="text-xs opacity-75">— Question {sectionProgress}</span>
          </div>
          <div className={`flex items-center gap-2 font-mono font-bold text-lg ${isUrgent ? 'text-red-200 animate-pulse' : isWarning ? 'text-amber-200' : ''}`} data-testid="mock-timer">
            <Clock className="w-4 h-4" />
            {formatTime(timeLeft)}
          </div>
        </div>

        {/* Progress bar */}
        <div className="h-1 bg-slate-200">
          <div className={`h-full transition-all duration-300 ${section === 'verbal' ? 'bg-blue-500' : 'bg-violet-500'}`}
            style={{ width: `${config ? ((currentIndex + 1) / questionIds.length) * 100 : 0}%` }} />
        </div>

        {/* Question */}
        <div className="flex-1 p-3 lg:p-8 max-w-3xl mx-auto w-full" data-testid="mock-question-card">
          <QuestionPrompt
            passage_ar={question.passage_ar}
            table_ar={question.table_ar}
            table_caption={question.table_caption}
            figure_svg={question.figure_svg}
            figure_alt={question.figure_alt}
            text_ar={question.text_ar}
            content_format={question.content_format}
            comparison_columns={question.comparison_columns}
            testIdPrefix="mock-question"
            passageClassName="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl p-3 lg:p-5 mb-3 text-xs lg:text-sm text-slate-600 dark:text-slate-400 leading-relaxed max-h-32 lg:max-h-48 overflow-y-auto"
            questionClassName="text-base lg:text-xl font-bold text-slate-800 dark:text-slate-100 mb-4 lg:mb-6 leading-relaxed whitespace-pre-line math-text"
            appearance={appearance}
          />

          <QuestionOptions
            options={question.options}
            contentFormat={question.content_format}
            selectedKey={selected}
            disabled={!!selected}
            onSelect={submitAnswer}
            testIdPrefix="mock"
            appearance={appearance}
            accent={section === 'verbal' ? 'blue' : 'violet'}
            maskUnselected={false}
          />
        </div>
      </div>
    );
  }

  // ── Loading during exam ──
  if (phase === 'exam' && !question) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-slate-50 dark:bg-slate-950">
        <div className="w-8 h-8 border-3 border-amber-400 border-t-transparent rounded-full animate-spin" />
      </div>
    );
  }

  // ── Results Phase ──
  if (phase === 'results' && results) {
    const passed = results.score >= 65;
    return (
      <div className="min-h-screen bg-slate-50 flex items-center justify-center p-4 text-slate-800 dark:bg-slate-950 dark:text-slate-100" data-testid="mock-results">
        <div className="max-w-lg w-full text-center">
          <div className="text-6xl mb-4">{passed ? '🎉' : '💪'}</div>
          <h1 className="text-3xl font-black text-slate-800 dark:text-slate-100 mb-2">
            {passed ? 'Excellent Performance!' : 'Good Attempt!'}
          </h1>
          <p className="text-slate-500 mb-2">
            {passed ? 'Your score shows good readiness for the real exam' : 'Continue training and your score will improve'}
          </p>
          <p className="text-sm text-slate-400 mb-8">Attempt {results.attempt_number} of {displayMaxAttempts}</p>

          {/* Score Ring */}
          <div className="bg-white rounded-2xl border border-slate-200 p-8 mb-6 dark:border-slate-800 dark:bg-slate-900">
            <p className="text-slate-500 text-sm mb-4 dark:text-slate-400">Predicted Score</p>
            <ScoreRing score={results.score} label="of 100" />
          </div>

          {/* Section Breakdown */}
          <div className="grid grid-cols-2 gap-4 mb-6">
            <div className="bg-blue-50 border border-blue-200 rounded-2xl p-5">
              <BookOpen className="w-6 h-6 text-blue-600 mx-auto mb-2" />
              <p className="text-blue-400 text-sm mb-1">Verbal Section</p>
              <p className="text-blue-700 font-black text-2xl">{Math.round(results.verbal_pct * 100)}%</p>
              <p className="text-xs text-blue-500">{results.verbal_correct} / {results.verbal_total}</p>
            </div>
            <div className="bg-violet-50 border border-violet-200 rounded-2xl p-5">
              <Calculator className="w-6 h-6 text-violet-600 mx-auto mb-2" />
              <p className="text-violet-400 text-sm mb-1">Quantitative Section</p>
              <p className="text-violet-700 font-black text-2xl">{Math.round(results.quant_pct * 100)}%</p>
              <p className="text-xs text-violet-500">{results.quant_correct} / {results.quant_total}</p>
            </div>
          </div>

          {/* Stats */}
          <div className="bg-white border border-slate-200 rounded-xl p-4 mb-6 dark:border-slate-800 dark:bg-slate-900">
            <div className="grid grid-cols-3 gap-3 text-center">
              <div>
                <p className="text-xl font-black text-slate-800 dark:text-slate-100">{results.total}</p>
                <p className="text-xs text-slate-500">Total Questions</p>
              </div>
              <div>
                <p className="text-xl font-black text-emerald-600">{results.correct}</p>
                <p className="text-xs text-slate-500">Correct Answers</p>
              </div>
              <div>
                <p className="text-xl font-black text-slate-800 dark:text-slate-100">{Math.round((results.correct / Math.max(1, results.total)) * 100)}%</p>
                <p className="text-xs text-slate-500">Overall Accuracy</p>
              </div>
            </div>
          </div>

          <div className="mb-6 rounded-2xl border border-amber-200 bg-amber-50 px-5 py-4 text-left">
            <p className="text-sm font-bold text-amber-800">Review comes after the exam</p>
            <p className="mt-1 text-sm text-amber-700">
              Practice questions show feedback right away. Mock exams keep answers hidden until the full attempt is complete, then you can open the full review.
            </p>
          </div>

          {/* Action buttons */}
          <div className="space-y-3">
            <button
              onClick={() => { void loadAttemptDetail(results.attempt_id); }}
              data-testid="mock-review-attempt"
              className="w-full flex items-center justify-center gap-2 bg-white border border-slate-200 text-slate-700 font-bold py-4 rounded-xl hover:border-teal-300 hover:text-teal-700 transition-all dark:border-slate-800 dark:bg-slate-900 dark:text-slate-100 dark:hover:text-teal-300"
            >
              <History className="w-5 h-5" />
              Review This Attempt
            </button>

            {hasMoreAttempts && !isPreview && (
              <button onClick={() => { setPhase('instructions'); setResults(null); setAttemptId(null); }}
                className="w-full flex items-center justify-center gap-2 bg-gradient-to-l from-amber-600 to-amber-500 text-white font-bold py-4 rounded-xl shadow-lg hover:shadow-xl transition-all active:scale-[0.98]">
                <RotateCcw className="w-5 h-5" />
                Start Next Attempt
              </button>
            )}

            <button onClick={() => nav('/')}
              className="w-full bg-gradient-to-l from-teal-600 to-teal-500 text-white font-bold py-4 rounded-xl shadow-brand hover:shadow-lg transition-all">
              Back to Dashboard
            </button>

            <button onClick={loadHistory}
              className="w-full flex items-center justify-center gap-2 text-teal-600 font-medium text-sm py-3 hover:text-teal-700 transition">
              <History className="w-4 h-4" />
              View All Attempts
            </button>
          </div>
        </div>
      </div>
    );
  }

  // ── History Phase ──
  if (phase === 'history') {
    return (
      <div className="min-h-screen bg-slate-50 p-4 text-slate-800 dark:bg-slate-950 dark:text-slate-100" data-testid="mock-history">
        <div className="max-w-2xl mx-auto">
          {/* Header */}
          <div className="text-center mb-8">
            <div className="w-16 h-16 bg-gradient-to-br from-teal-500 to-teal-600 rounded-2xl flex items-center justify-center mx-auto mb-4 shadow-lg">
              <History className="w-8 h-8 text-white" />
            </div>
            <h1 className="text-2xl font-black text-slate-800 dark:text-slate-100 mb-1">Attempt History</h1>
            <p className="text-slate-500 text-sm">{attemptsUsed} of {maxAttempts} attempts completed</p>
          </div>

          {historyLoading && (
            <div className="flex justify-center py-12">
              <div className="w-8 h-8 border-3 border-teal-400 border-t-transparent rounded-full animate-spin" />
            </div>
          )}

          {!historyLoading && attempts.length === 0 && (
            <div className="text-center py-12 text-slate-400">No previous attempts</div>
          )}

          {/* Attempt Cards */}
          <div className="space-y-3 mb-8">
            {attempts.map(a => (
              <button key={a.id} onClick={() => loadAttemptDetail(a.id)}
                className="w-full bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-5 hover:border-teal-300 hover:shadow-md transition-all text-left">
                <div className="flex items-center justify-between mb-3">
                  <ChevronRight className="w-5 h-5 text-slate-400" />
                  <div className="flex items-center gap-2">
                    <span className="bg-slate-100 text-slate-600 text-xs font-bold px-2.5 py-1 rounded-lg">
                      Attempt {a.attempt_number}
                    </span>
                    <span className={`font-black text-2xl ${scoreColor(a.score)}`}>{a.score}</span>
                  </div>
                </div>

                <div className="grid grid-cols-3 gap-3">
                  <div className="bg-blue-50 rounded-lg p-2 text-center">
                    <p className="text-xs text-blue-500 mb-0.5">Verbal</p>
                    <p className="text-sm font-bold text-blue-700">{Math.round(a.verbal_pct * 100)}%</p>
                  </div>
                  <div className="bg-violet-50 rounded-lg p-2 text-center">
                    <p className="text-xs text-violet-500 mb-0.5">Quant</p>
                    <p className="text-sm font-bold text-violet-700">{Math.round(a.quant_pct * 100)}%</p>
                  </div>
                  <div className="bg-slate-50 dark:bg-slate-800 rounded-lg p-2 text-center">
                    <p className="text-xs text-slate-500 mb-0.5">Date</p>
                    <p className="text-sm font-bold text-slate-700">
                      {new Date(a.completed_at).toLocaleDateString('en-US', { month: 'short', day: 'numeric' })}
                    </p>
                  </div>
                </div>
              </button>
            ))}
          </div>

          {/* Actions */}
          <div className="space-y-3">
            {hasMoreAttempts && !isPreview && (
              <button onClick={() => { setPhase('instructions'); }}
                className="w-full flex items-center justify-center gap-2 bg-gradient-to-l from-amber-600 to-amber-500 text-white font-bold py-4 rounded-xl shadow-lg hover:shadow-xl transition-all active:scale-[0.98]">
                <ArrowRight className="w-5 h-5" />
                Start Next Attempt
              </button>
            )}
            <button onClick={() => nav('/')}
              className="w-full text-slate-500 font-medium py-3 hover:text-slate-700 transition">
              Back to Dashboard
            </button>
          </div>
        </div>
      </div>
    );
  }

  // ── Detail Phase ──
  if (phase === 'detail' && detail) {
    const verbalPct = detail.verbal_total > 0 ? Math.round((detail.verbal_correct / detail.verbal_total) * 100) : 0;
    const quantPct = detail.quant_total > 0 ? Math.round((detail.quant_correct / detail.quant_total) * 100) : 0;

    return (
      <div className="min-h-screen bg-slate-50 p-4 text-slate-800 dark:bg-slate-950 dark:text-slate-100">
        <div className="max-w-3xl mx-auto">
          {/* Back button */}
          <button onClick={() => { setPhase('history'); setDetail(null); }}
            className="flex items-center gap-1.5 text-teal-600 font-medium text-sm mb-6 hover:text-teal-700 transition">
            <ArrowRight className="w-4 h-4 rotate-180" />
            Back to Attempt History
          </button>

          {/* Header with score */}
          <div className="text-center mb-8">
            <p className="text-sm text-slate-400 mb-3">Attempt {detail.attempt_number}</p>
            <ScoreRing score={detail.score} label="out of 100" />
            <p className="mt-4 text-sm text-slate-500">
              This review is shown after the full mock attempt is finished. Practice mode still gives immediate question-by-question feedback.
            </p>
          </div>

          {/* Section Breakdown */}
          <div className="grid grid-cols-2 gap-4 mb-6">
            <div className="bg-blue-50 border border-blue-200 rounded-2xl p-5 text-center">
              <BookOpen className="w-6 h-6 text-blue-600 mx-auto mb-2" />
              <p className="text-blue-400 text-sm mb-1">Verbal Section</p>
              <p className="text-blue-700 font-black text-2xl">{verbalPct}%</p>
              <p className="text-xs text-blue-500">{detail.verbal_correct} / {detail.verbal_total}</p>
            </div>
            <div className="bg-violet-50 border border-violet-200 rounded-2xl p-5 text-center">
              <Calculator className="w-6 h-6 text-violet-600 mx-auto mb-2" />
              <p className="text-violet-400 text-sm mb-1">Quantitative Section</p>
              <p className="text-violet-700 font-black text-2xl">{quantPct}%</p>
              <p className="text-xs text-violet-500">{detail.quant_correct} / {detail.quant_total}</p>
            </div>
          </div>

          {/* Per-Skill Accuracy Table */}
          {detail.skill_breakdown.length > 0 && (
            <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-5 mb-6">
              <h3 className="font-bold text-slate-800 dark:text-slate-100 mb-4">Skill Performance</h3>
              <div className="space-y-2">
                {detail.skill_breakdown.map(sk => {
                  const pct = sk.pct;
                  const barColor = pct >= 80 ? 'bg-emerald-500' : pct >= 50 ? 'bg-amber-500' : 'bg-red-500';
                  return (
                    <div key={sk.skill_id} className="flex items-center gap-3">
                      <span className="text-sm text-slate-700 dark:text-slate-300 font-medium w-32 shrink-0 text-left">{sk.skill_name_ar}</span>
                      <div className="flex-1 h-2.5 bg-slate-100 rounded-full overflow-hidden">
                        <div className={`h-full rounded-full ${barColor}`} style={{ width: `${pct}%` }} />
                      </div>
                      <span className="text-xs text-slate-500 font-mono w-20 shrink-0">{sk.correct}/{sk.total} ({Math.round(pct)}%)</span>
                    </div>
                  );
                })}
              </div>
            </div>
          )}

          {/* Question Review Table */}
          <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-5 mb-6">
            <h3 className="font-bold text-slate-800 dark:text-slate-100 mb-4">Question Review ({detail.questions.length})</h3>
            <div className="space-y-3">
              {detail.questions.map((q, i) => {
                const isCorrect = q.is_correct;
                return (
                  <div key={q.question_id} className={`border rounded-xl p-4 ${isCorrect ? 'border-emerald-200 bg-emerald-50/30' : 'border-red-200 bg-red-50/30'}`}>
                    <div className="flex items-start justify-between gap-3 mb-2">
                      <div className="flex items-center gap-2 shrink-0">
                        {isCorrect
                          ? <CheckCircle className="w-5 h-5 text-emerald-500" />
                          : <XCircle className="w-5 h-5 text-red-500" />
                        }
                        <span className="text-xs text-slate-400 font-mono">{i + 1}</span>
                      </div>
                      <div className="flex-1 text-left">
                        <QuestionPrompt
                          passage_ar={q.passage_ar}
                          table_ar={q.table_ar}
                          table_caption={q.table_caption}
                          figure_svg={q.figure_svg}
                          figure_alt={q.figure_alt}
                          text_ar={q.text_ar}
                          content_format={q.content_format}
                          comparison_columns={q.comparison_columns}
                          testIdPrefix={`mock-review-question-${q.question_id}`}
                          compact
                          passageClassName="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-lg p-3 mb-3 text-xs text-slate-600 dark:text-slate-400 leading-relaxed"
                          questionClassName="text-sm text-slate-700 dark:text-slate-300 leading-relaxed whitespace-pre-line math-text"
                          figureFrameClassName="mb-3 rounded-lg border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-950 p-3"
                          appearance={appearance}
                        />
                      </div>
                    </div>

                    <div className="flex items-center justify-between text-xs">
                      <span className="text-slate-400">{q.time_spent_seconds} seconds • {q.skill_name_ar}</span>
                      <div className="flex items-center gap-3">
                        <span className={isCorrect ? 'text-emerald-600 font-bold' : 'text-red-600 font-bold'}>
                          Your answer: {q.selected_option}
                        </span>
                        {!isCorrect && (
                          <span className="text-emerald-600 font-bold">Correct: {q.correct_option}</span>
                        )}
                      </div>
                    </div>

                    {/* Show explanation for wrong answers */}
                    {!isCorrect && q.explanation_ar && (
                      <div className="mt-3">
                        <QuestionFeedbackCard
                          feedback={{
                            is_correct: q.is_correct,
                            correct_option: q.correct_option,
                            explanation_ar: q.explanation_ar,
                            solution_steps_ar: q.solution_steps_ar ?? null,
                            content_format: q.content_format,
                            comparison_columns: q.comparison_columns,
                            figure_svg: q.figure_svg,
                            figure_alt: q.figure_alt,
                            table_ar: q.table_ar,
                            table_caption: q.table_caption,
                          }}
                          selectedOption={q.selected_option}
                          appearance={appearance}
                          title="Post-mock review"
                          className="text-sm"
                        />
                      </div>
                    )}
                  </div>
                );
              })}
            </div>
          </div>
        </div>
      </div>
    );
  }

  // ── Fallback: loading or all attempts used (loading history) ──
  return (
    <div className="min-h-screen flex items-center justify-center bg-slate-50 dark:bg-slate-950">
      {historyLoading ? (
        <div className="w-8 h-8 border-3 border-teal-400 border-t-transparent rounded-full animate-spin" />
      ) : (
        <div className="text-center">
          <CheckCircle className="w-12 h-12 text-emerald-500 mx-auto mb-3" />
          <p className="text-slate-600 dark:text-slate-400 font-bold mb-4">All attempts completed</p>
          {user?.mock_score ? (
            <p className="text-2xl font-black text-slate-800 dark:text-slate-100 mb-4">Best Score: {user.mock_score}</p>
          ) : null}
          <button onClick={loadHistory} className="text-teal-600 font-medium">View Attempt History</button>
        </div>
      )}
    </div>
  );
}
