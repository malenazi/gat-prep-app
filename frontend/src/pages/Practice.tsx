import { useState, useEffect, useRef, useCallback } from 'react';
import { useNavigate } from 'react-router-dom';
import { api } from '@/lib/api';
import { nowMs, todayIsoDate } from '@/lib/time';
import { PracticeAdaptivePanel } from '@/components/practice/PracticeAdaptivePanel';
import { PracticeHintPanel } from '@/components/practice/PracticeHintPanel';
import { QuestionFeedbackCard } from '@/components/questions/QuestionFeedbackCard';
import { QuestionOptions } from '@/components/questions/QuestionOptions';
import { QuestionPrompt } from '@/components/questions/QuestionPrompt';
import { useAuth } from '@/hooks/useAuth';
import { pageShell } from '@/lib/layout';
import { defaultQuestionAppearance } from '@/lib/questionPresentation';
import type {
  ApiQuestion,
  PracticeAdaptiveMeta,
  PracticeAnswerFeedback,
  PracticeAssistment,
  PracticeNextResponse,
  TodayPlan,
} from '@/types';

const PRACTICE_SESSION_KEY = 'practice_session';

interface PracticeSessionData {
  date: string;
  stats: { total: number; correct: number; xp: number };
  streak: number;
}

function savePracticeSession(data: PracticeSessionData) {
  localStorage.setItem(PRACTICE_SESSION_KEY, JSON.stringify(data));
}

function loadPracticeSession(): PracticeSessionData | null {
  try {
    const raw = localStorage.getItem(PRACTICE_SESSION_KEY);
    if (!raw) return null;
    const data = JSON.parse(raw);
    if (data.date !== new Date().toISOString().split('T')[0]) return null; // expired
    return data;
  } catch { return null; }
}

function clearPracticeSession() { localStorage.removeItem(PRACTICE_SESSION_KEY); }

interface SessionStats {
  total: number;
  correct: number;
  xp: number;
}

interface FeedbackWithLate extends PracticeAnswerFeedback {
  wasLate: boolean;
}

function Confetti() {
  return <div className="confetti-container"><div className="c"/><div className="c"/><div className="c"/><div className="c"/><div className="c"/><div className="c"/></div>;
}

export default function Practice() {
  const { loadUser } = useAuth();
  const nav = useNavigate();
  const [question, setQuestion] = useState<ApiQuestion | null>(null);
  const [adaptive, setAdaptive] = useState<PracticeAdaptiveMeta | null>(null);
  const [assistment, setAssistment] = useState<PracticeAssistment | null>(null);
  const [selected, setSelected] = useState<string | null>(null);
  const [feedback, setFeedback] = useState<FeedbackWithLate | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [sessionStats, setStats] = useState<SessionStats>({ total: 0, correct: 0, xp: 0 });
  const [done, setDone] = useState(false);
  const [streak, setStreak] = useState(0);
  const [showExitConfirm, setShowExitConfirm] = useState(false);
  const [xpPopup, setXpPopup] = useState<string | null>(null);
  const [todayTarget, setTodayTarget] = useState(15);
  const [todayCompleted, setTodayCompleted] = useState(0);
  const [countdown, setCountdown] = useState(90);
  const [revealedHints, setRevealedHints] = useState(0);
  const feedbackRef = useRef<HTMLDivElement>(null);
  const startTimeRef = useRef(0);
  const initRef = useRef(false);
  const appearance = defaultQuestionAppearance;
  const [questionTransition, setQuestionTransition] = useState<'enter' | 'exit' | ''>('enter');
  const [submitting, setSubmitting] = useState(false);
  const [showVignette, setShowVignette] = useState(false);
  const [streakBroken, setStreakBroken] = useState(false);
  const [feedbackCollapsing, setFeedbackCollapsing] = useState(false);

  const QUESTION_TIME = 90; // seconds estimated per question

  // Auto-scroll to feedback/next button when it appears
  useEffect(() => {
    if (feedback && feedbackRef.current) {
      feedbackRef.current.scrollIntoView({ behavior: 'smooth', block: 'end' });
    }
  }, [feedback]);

  // Countdown timer
  useEffect(() => {
    if (!question || selected) return;
    const interval = setInterval(() => {
      setCountdown(prev => prev <= 0 ? 0 : prev - 1);
    }, 1000);
    return () => clearInterval(interval);
  }, [question, selected]);

  // Timer vignette flash when time expires
  useEffect(() => {
    if (countdown === 0 && !selected && question) {
      setShowVignette(true);
      setTimeout(() => setShowVignette(false), 1500);
    }
  }, [countdown, selected, question]);

  // Restore session stats from localStorage
  useEffect(() => {
    const saved = loadPracticeSession();
    if (saved) {
      setStats(saved.stats);
      setStreak(saved.streak);
    }
  }, []);

  const loadNext = useCallback(async () => {
    if (feedback) {
      setFeedbackCollapsing(true);
      await new Promise(r => setTimeout(r, 250));
      setFeedbackCollapsing(false);
    }
    if (question) {
      setQuestionTransition('exit');
      await new Promise(r => setTimeout(r, 200));
    }
    setLoading(true);
    setSelected(null);
    setSubmitting(false);
    setFeedback(null);
    setError('');
    setXpPopup(null);
    setCountdown(QUESTION_TIME);
    setRevealedHints(0);
    try {
      const data: PracticeNextResponse = await api.practiceNext();
      if (data.done) {
        setDone(true);
        setQuestion(null);
        setAdaptive(null);
        setAssistment(null);
      } else {
        setQuestion(data.question ?? null);
        setAdaptive(data.adaptive ?? null);
        setAssistment(data.assistment ?? null);
        startTimeRef.current = nowMs();
        setCountdown(QUESTION_TIME);
      }
    } catch (e: unknown) {
      if (sessionStats.total > 0) setDone(true);
      else setError(e instanceof Error ? e.message : 'Error loading question');
    }
    setLoading(false);
    setQuestionTransition('enter');
  }, [QUESTION_TIME, sessionStats.total, feedback, question]);

  useEffect(() => {
    if (initRef.current) return;
    initRef.current = true;
    api.today().then((t: TodayPlan) => {
      setTodayTarget(t.target_questions || 15);
      setTodayCompleted(t.completed_questions || 0);
    }).catch(() => {});
    void loadNext();
  }, [loadNext]);

  const submitAnswer = async (key: string) => {
    if (selected) return;
    if (!question || !startTimeRef.current) return;
    setSelected(key);
    setSubmitting(true);
    const wasLate = countdown <= 0;
    try {
      const elapsed = Math.round((nowMs() - startTimeRef.current) / 1000);
      const data: PracticeAnswerFeedback = await api.practiceAnswer({ question_id: question.id, selected_option: key, time_spent_seconds: elapsed });
      setSubmitting(false);
      setFeedback({ ...data, wasLate });
      const newStreak = data.is_correct ? streak + 1 : 0;
      if (!data.is_correct && streak > 0) {
        setStreakBroken(true);
        setTimeout(() => setStreakBroken(false), 2000);
      }
      setStreak(newStreak);
      const newStats = { total: sessionStats.total + 1, correct: sessionStats.correct + (data.is_correct ? 1 : 0), xp: sessionStats.xp + data.xp_earned };
      setStats(newStats);
      savePracticeSession({
        date: todayIsoDate(),
        stats: newStats,
        streak: newStreak,
      });
      setTodayCompleted(prev => prev + 1);
      // XP popup
      const bonusText = newStreak >= 3 ? ` (×2 🔥)` : '';
      setXpPopup(`+${data.xp_earned} XP${bonusText}`);
      setTimeout(() => setXpPopup(null), 2000);
    } catch (e: unknown) { setSubmitting(false); setError(e instanceof Error ? e.message : 'Error occurred'); setSelected(null); }
  };

  const finish = async () => { clearPracticeSession(); await loadUser(); nav('/'); };
  const tryExit = () => { if (sessionStats.total > 0 && !done) setShowExitConfirm(true); else finish(); };
  const revealNextHint = () => {
    if (!assistment || selected) return;
    setRevealedHints((count) => Math.min(count + 1, assistment.hints.length));
  };
  // Keyboard shortcuts: A/B/C/D to answer, Enter for next, H for hint
  useEffect(() => {
    const handler = (e: KeyboardEvent) => {
      if (e.target instanceof HTMLInputElement || e.target instanceof HTMLTextAreaElement) return;
      const k = e.key.toLowerCase();
      if (!selected && question && !done && ['a', 'b', 'c', 'd'].includes(k)) {
        e.preventDefault();
        submitAnswer(k);
      }
      if (k === 'h' && !selected && assistment) {
        e.preventDefault();
        revealNextHint();
      }
      if (e.key === 'Enter' && feedback && !done) {
        e.preventDefault();
        loadNext();
      }
    };
    window.addEventListener('keydown', handler);
    return () => window.removeEventListener('keydown', handler);
  });

  const accuracy = sessionStats.total > 0 ? Math.round(sessionStats.correct / sessionStats.total * 100) : 0;
  // dailyPct: use the higher of todayCompleted (API + increments) or session total (in case API didn't load yet)
  const effectiveCompleted = Math.max(todayCompleted, sessionStats.total);
  const dailyPct = Math.min(100, Math.round((effectiveCompleted / Math.max(1, todayTarget)) * 100));

  if (error && !question) return (
    <div className="min-h-[60vh] flex flex-col items-center justify-center p-6 text-center page-enter text-slate-800 dark:text-slate-100">
      <div className="text-5xl mb-4">⚠️</div>
      <p className="text-red-500 mb-4">{error}</p>
      <div className="flex gap-3">
        <button onClick={loadNext} className="bg-teal-600 text-white font-bold py-2.5 px-6 rounded-xl shadow-brand">Retry</button>
        <button onClick={finish} className="bg-white shadow-card text-slate-600 font-bold py-2.5 px-6 rounded-xl dark:bg-slate-900 dark:text-slate-300">Back</button>
      </div>
    </div>
  );

  if (done) return (
    <div className="min-h-[60vh] flex flex-col items-center justify-center p-6 text-center page-enter text-slate-800 dark:text-slate-100">
      <div className="relative">
        <div className="text-7xl mb-4 animate-score-reveal">💪</div>
        <Confetti />
      </div>
      <h1 className="text-3xl font-black text-slate-800 mb-2 dark:text-slate-100">Well Done!</h1>
      <p className="text-slate-500 mb-2 dark:text-slate-400">You completed your training session</p>
      {accuracy >= 80 && <p className="text-emerald-500 text-sm font-bold mb-4 stagger-1">Excellent accuracy! You're mastering this material.</p>}
      {accuracy >= 50 && accuracy < 80 && <p className="text-teal-500 text-sm font-bold mb-4 stagger-1">Good work! Review the questions you missed to keep improving.</p>}
      {accuracy > 0 && accuracy < 50 && <p className="text-amber-500 text-sm font-bold mb-4 stagger-1">Keep practicing! Focus on the feedback from each question.</p>}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4 w-full max-w-lg mb-6">
        <StatBox label="Questions" value={sessionStats.total} icon="📝" className="stagger-1" />
        <StatBox label="Correct" value={sessionStats.correct} icon="✅" color="text-emerald-500" className="stagger-2" />
        <StatBox label="Accuracy" value={`${accuracy}%`} icon="🎯" color="text-teal-600" className="stagger-3" />
        <StatBox label="XP" value={`+${sessionStats.xp}`} icon="⚡" color="text-amber-500" className="stagger-4" />
      </div>
      {streak >= 3 && (
        <div className="mb-4 flex items-center gap-2 text-amber-500 font-bold text-sm stagger-5">
          <span className="animate-fire">🔥</span> You kept a {streak}-question streak with ×2 XP bonus!
        </div>
      )}
      {dailyPct >= 100 && (
        <div className="mb-6 bg-gradient-to-l from-emerald-500 to-emerald-600 text-white rounded-2xl px-6 py-3 font-bold animate-slide-up flex items-center gap-2">
          <Confetti /> 🎉 You completed today's goal!
        </div>
      )}
      {dailyPct < 100 && (
        <p className="mb-4 text-slate-400 dark:text-slate-500 text-sm stagger-5">
          {todayTarget - todayCompleted} more questions to complete today's goal.
        </p>
      )}
      <button onClick={finish} className="bg-gradient-to-l from-teal-600 to-teal-500 text-white font-bold py-3.5 px-12 rounded-xl shadow-brand hover:shadow-lg transition-all">
        Back to Home
      </button>
    </div>
  );

  // Skip question (counts as wrong)
  const skipQuestion = () => {
    if (!question || selected) return;
    submitAnswer(['a', 'b', 'c', 'd'].find(k => k !== 'a') || 'b');
  };

  if (loading && !question) return (
    <div className={`${pageShell.standard} pt-14 lg:pt-10`}>
      {/* Skeleton: progress bar */}
      <div className="mb-2 rounded-2xl bg-white dark:bg-slate-900 p-3 shadow-card lg:mb-6 lg:p-4">
        <div className="flex justify-between mb-2"><div className="skeleton h-4 w-40" /><div className="skeleton h-4 w-20" /></div>
        <div className="skeleton h-2.5 w-full rounded-full" />
      </div>
      {/* Skeleton: adaptive panel */}
      <div className="rounded-3xl border border-slate-100 dark:border-slate-800 bg-white dark:bg-slate-900 p-5 shadow-card mb-5">
        <div className="flex gap-2 mb-4"><div className="skeleton h-6 w-28 rounded-full" /><div className="skeleton h-6 w-24 rounded-full" /><div className="skeleton h-6 w-20 rounded-full" /></div>
        <div className="skeleton h-7 w-64 mb-2" /><div className="skeleton h-4 w-40" />
      </div>
      {/* Skeleton: question */}
      <div className="rounded-[2rem] border border-slate-100 dark:border-slate-800 bg-white dark:bg-slate-900 p-6 shadow-card mb-5">
        <div className="skeleton h-5 w-20 rounded-full mb-4" />
        <div className="skeleton h-8 w-full mb-3" /><div className="skeleton h-8 w-3/4" />
      </div>
      {/* Skeleton: 4 options */}
      <div className="space-y-4">
        {[1, 2, 3, 4].map(i => (
          <div key={i} className="rounded-[2rem] border border-slate-100 dark:border-slate-800 bg-white dark:bg-slate-900 p-5 flex items-center gap-4">
            <div className="skeleton h-11 w-11 rounded-2xl shrink-0" />
            <div className="flex-1"><div className="skeleton h-5 w-full" /></div>
          </div>
        ))}
      </div>
    </div>
  );

  return (
    <div className={`${pageShell.standard} page-enter pt-14 lg:pt-10 text-slate-800 dark:text-slate-100`} data-testid="practice-page">
      {/* Exit confirmation */}
      {showVignette && <div className="timer-vignette" />}

      {showExitConfirm && (
        <div className="fixed inset-0 bg-slate-900/40 backdrop-blur-sm flex items-center justify-center z-50 p-6">
          <div className="bg-white rounded-2xl p-8 w-full max-w-sm text-center shadow-card-lg animate-slide-up dark:bg-slate-900" data-testid="practice-exit-confirm">
            <p className="text-slate-800 font-bold text-lg mb-1 dark:text-slate-100">End Session?</p>
            <p className="text-slate-500 text-sm mb-4 dark:text-slate-400">Your progress so far:</p>
            <div className="grid grid-cols-3 gap-2 mb-5">
              <div className="bg-slate-50 dark:bg-slate-800 rounded-xl p-2">
                <p className="font-black text-lg text-slate-800 dark:text-slate-100">{sessionStats.total}</p>
                <p className="text-xs text-slate-500">Questions</p>
              </div>
              <div className="bg-slate-50 dark:bg-slate-800 rounded-xl p-2">
                <p className="font-black text-lg text-emerald-500">{accuracy}%</p>
                <p className="text-xs text-slate-500">Accuracy</p>
              </div>
              <div className="bg-slate-50 dark:bg-slate-800 rounded-xl p-2">
                <p className="font-black text-lg text-amber-500">+{sessionStats.xp}</p>
                <p className="text-xs text-slate-500">XP</p>
              </div>
            </div>
            {streak >= 3 && <p className="text-amber-500 text-sm font-bold mb-3">🔥 You'll lose your {streak}-question streak!</p>}
            <div className="flex gap-3">
              <button onClick={() => setShowExitConfirm(false)} className="flex-1 bg-slate-100 text-slate-700 font-bold py-3 rounded-xl hover:bg-slate-200 transition dark:bg-slate-800 dark:text-slate-300" data-testid="practice-exit-continue">Continue</button>
              <button onClick={finish} className="flex-1 bg-red-500 text-white font-bold py-3 rounded-xl hover:bg-red-600 transition" data-testid="practice-exit-end">End</button>
            </div>
          </div>
        </div>
      )}

      {/* ═══ Daily Progress Bar (top) ═══ */}
      <div className="mb-3 rounded-2xl bg-white p-3 shadow-card stagger-1 lg:mb-5 lg:px-5 lg:py-3 dark:bg-slate-900" data-testid="practice-daily-progress">
        <div className="flex items-center justify-between mb-2">
          <div className="flex items-center gap-3">
            <span className="text-slate-800 dark:text-slate-100 text-sm font-black">Q{sessionStats.total + 1}<span className="text-slate-400 dark:text-slate-500 font-medium">/{todayTarget}</span></span>
            {todayCompleted < todayTarget && (
              <span className="text-xs text-slate-400 dark:text-slate-500 hidden sm:inline">
                ~{Math.ceil((todayTarget - todayCompleted) * QUESTION_TIME / 60)} min left
              </span>
            )}
          </div>
          <div className="flex items-center gap-2">
            {dailyPct >= 100 && <span className="text-emerald-500 text-xs font-bold">🎉 Goal done!</span>}
            <span className="text-xs font-bold text-teal-600 dark:text-teal-400 bg-teal-50 dark:bg-teal-500/10 px-2 py-0.5 rounded-full">{dailyPct}%</span>
          </div>
        </div>
        <div className="h-2 lg:h-2.5 bg-slate-200 dark:bg-slate-800 rounded-full overflow-hidden relative">
          <div className="h-full bg-gradient-to-l from-teal-400 to-teal-600 rounded-full transition-all duration-500" style={{ width: `${dailyPct}%` }} />
          <div className="progress-milestone-marker" style={{ left: '25%' }} />
          <div className="progress-milestone-marker" style={{ left: '50%' }} />
          <div className="progress-milestone-marker" style={{ left: '75%' }} />
        </div>
      </div>

      <div className="grid grid-cols-1 gap-6 xl:grid-cols-[minmax(0,1fr)_19rem] 2xl:gap-8">
        {/* ═══ Main Question Area ═══ */}
        <div>
          <div className="flex items-center justify-between mb-3 lg:mb-6">
            <div className="flex items-center gap-3">
              <button onClick={tryExit} className="text-slate-500 hover:text-slate-700 text-sm transition flex items-center gap-1.5 dark:text-slate-400 dark:hover:text-slate-100" data-testid="practice-end">
                <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}><path strokeLinecap="round" strokeLinejoin="round" d="M6 18L18 6M6 6l12 12" /></svg>
                End
              </button>
              {!selected && question && (
                <button onClick={skipQuestion} className="text-slate-500 hover:text-amber-600 text-sm font-medium transition flex items-center gap-1 dark:text-slate-400 dark:hover:text-amber-400">
                  <svg className="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}><path strokeLinecap="round" strokeLinejoin="round" d="M13 5l7 7-7 7M5 5l7 7-7 7" /></svg>
                  Skip
                </button>
              )}
            </div>
            <div className="flex items-center gap-2">
              {streak >= 3 && (
                <div className="flex items-center gap-1 bg-gradient-to-l from-amber-500 to-orange-500 text-white text-sm font-bold px-3 py-1.5 rounded-full animate-pulse-glow">
                  <span className={`${streak >= 7 ? 'streak-flame-lg' : streak >= 5 ? 'streak-flame-md' : 'streak-flame-sm'} animate-fire`}>🔥</span> {streak} Streak • ×2 XP
                </div>
              )}
              {streakBroken && (
                <div className="text-red-500 dark:text-red-400 font-bold text-sm animate-streak-break">Streak broken!</div>
              )}
              {/* XP Popup */}
              {xpPopup && (
                <div className="xp-popup text-teal-600 font-black text-lg">{xpPopup}</div>
              )}
            </div>
          </div>

          {error && (
            <div className="bg-red-50 border border-red-200 rounded-xl p-3 mb-4 text-center">
              <p className="text-red-500 text-sm">{error}</p>
            </div>
          )}

          {question && (
            <div data-testid="practice-question-card" className={`${questionTransition === 'enter' ? 'question-enter' : questionTransition === 'exit' ? 'question-exit' : ''} ${!selected && countdown <= 10 && countdown > 0 ? 'timer-urgent rounded-3xl' : ''}`}>
              {adaptive && (
                <PracticeAdaptivePanel
                  adaptive={adaptive}
                  question={question}
                  countdown={countdown}
                  selected={!!selected}
                  wasLate={feedback?.wasLate ?? false}
                />
              )}

              {assistment && !selected && (
                <PracticeHintPanel
                  assistment={assistment}
                  contentFormat={question.content_format}
                  revealedCount={revealedHints}
                  onReveal={revealNextHint}
                />
              )}

              <QuestionPrompt
                passage_ar={question.passage_ar}
                table_ar={question.table_ar}
                table_caption={question.table_caption}
                figure_svg={question.figure_svg}
                figure_alt={question.figure_alt}
                text_ar={question.text_ar}
                content_format={question.content_format}
                comparison_columns={question.comparison_columns}
                testIdPrefix="practice-question"
                appearance={appearance}
              />

              <div className={submitting && selected ? 'option-submitting rounded-2xl' : ''}>
                <QuestionOptions
                  options={question.options}
                  contentFormat={question.content_format}
                  selectedKey={selected}
                  correctOption={feedback?.correct_option ?? null}
                  disabled={!!selected}
                  onSelect={submitAnswer}
                  testIdPrefix="practice"
                  appearance={appearance}
                />
              </div>

              {/* Keyboard shortcuts hint (desktop, before answer) */}
              {!feedback && !selected && (
                <p className="hidden lg:flex items-center justify-center gap-3 mt-4 text-xs text-slate-400 dark:text-slate-500">
                  <span className="flex items-center gap-1"><span className="key-badge">A</span><span className="key-badge">B</span><span className="key-badge">C</span><span className="key-badge">D</span> select</span>
                  <span className="flex items-center gap-1"><span className="key-badge">H</span> hint</span>
                </p>
              )}

              {feedback && (
                <div ref={feedbackRef} className={`mt-3 lg:mt-6 ${feedbackCollapsing ? 'feedback-collapsing' : 'animate-slide-up'}`} data-testid="practice-feedback">
                  <QuestionFeedbackCard
                    feedback={feedback}
                    selectedOption={selected}
                    appearance={appearance}
                    title={feedback.is_correct ? 'Correct answer' : 'Review & Learn'}
                  />
                  {adaptive && (
                    <p className="mt-3 text-sm font-semibold text-slate-600 dark:text-slate-300" data-testid="practice-adaptive-recap">
                      You just solved a {adaptive.challenge_band} {adaptive.skill_name} item.
                    </p>
                  )}
                  {feedback.wasLate && (
                    <p className="mt-3 text-sm font-semibold text-red-500">Time note: the answer was submitted after the target timer expired.</p>
                  )}
                  <button onClick={loadNext} data-testid="practice-next"
                    className="w-full mt-3 lg:mt-4 bg-gradient-to-l from-teal-600 to-teal-500 text-white font-bold py-3 lg:py-4 rounded-xl shadow-brand hover:shadow-lg transition-all active:scale-[0.98]">
                    Next Question ← <span className="hidden lg:inline ml-2 key-badge">Enter ↵</span>
                  </button>
                </div>
              )}
            </div>
          )}
        </div>

        {/* ═══ Desktop Stats Sidebar ═══ */}
        <div className="hidden xl:block">
          <div className="sticky top-24 space-y-3">
            {/* Accuracy + key stats */}
            <div className="bg-white shadow-card rounded-2xl p-3.5 dark:bg-slate-900" data-testid="practice-session-stats">
              <div className="flex items-center gap-3">
                <div className="relative w-11 h-11 shrink-0">
                  <svg viewBox="0 0 100 100" className="w-full h-full">
                    <circle cx="50" cy="50" r="42" fill="none" stroke="currentColor" className="text-slate-200 dark:text-slate-700" strokeWidth="9" />
                    <circle cx="50" cy="50" r="42" fill="none" stroke="#0d9488" strokeWidth="9"
                      strokeDasharray="264" strokeDashoffset={264 - (264 * accuracy / 100)} strokeLinecap="round"
                      transform="rotate(-90 50 50)" style={{ transition: 'stroke-dashoffset 0.5s ease' }} />
                  </svg>
                  <div className="absolute inset-0 flex items-center justify-center">
                    <span className="text-xs font-black text-slate-800 dark:text-slate-100">{accuracy}%</span>
                  </div>
                </div>
                <div className="flex-1">
                  <div className="flex items-center gap-3 text-sm">
                    <span className="font-bold text-emerald-500">{sessionStats.correct}<span className="text-slate-400 font-medium">/{sessionStats.total}</span></span>
                    <span className="text-slate-300 dark:text-slate-600">|</span>
                    <span className="font-bold text-amber-500">+{sessionStats.xp} XP</span>
                  </div>
                </div>
              </div>
            </div>

            {/* Adaptive info */}
            {adaptive && (
              <div className="bg-white shadow-card rounded-2xl p-4 dark:bg-slate-900" data-testid="practice-session-trajectory">
                <div className="space-y-2 text-sm">
                  <div className="flex justify-between">
                    <span className="text-slate-500 dark:text-slate-400">Skill</span>
                    <span className="font-bold text-slate-800 dark:text-slate-100 text-right">{adaptive.skill_name}</span>
                  </div>
                  <div className="flex justify-between">
                    <span className="text-slate-500 dark:text-slate-400">Level</span>
                    <span className="font-bold text-indigo-600 dark:text-indigo-400">{adaptive.difficulty_label} {adaptive.difficulty_score}/100</span>
                  </div>
                  <div className="flex justify-between">
                    <span className="text-slate-500 dark:text-slate-400">Mastery</span>
                    <span className="font-bold text-teal-600 dark:text-teal-400">
                      {adaptive.challenge_band === 'Calibrating' ? 'Calibrating' : `${adaptive.skill_mastery}%`}
                    </span>
                  </div>
                </div>
                <div className="mt-2.5 flex items-start gap-2 rounded-lg bg-slate-50 dark:bg-slate-800/50 px-2.5 py-2">
                  <span className="text-xs mt-px">
                    {adaptive.challenge_band === 'Calibrating' ? '🔍' :
                     adaptive.challenge_band === 'Reinforcement' ? '🛡️' :
                     adaptive.challenge_band === 'At your level' ? '🎯' :
                     adaptive.challenge_band === 'Stretch' ? '📈' : '🚀'}
                  </span>
                  <p className="text-xs leading-relaxed text-slate-500 dark:text-slate-400">
                    {adaptive.challenge_band === 'Calibrating'
                      ? 'Estimating your starting level.'
                      : adaptive.challenge_band === 'Reinforcement' ? 'Below your level — reinforcement.'
                      : adaptive.challenge_band === 'At your level' ? 'Matches your current ability.'
                      : adaptive.challenge_band === 'Stretch' ? 'Slightly above — a good stretch.'
                      : adaptive.challenge_band === 'Challenge+' ? 'Well above — a real challenge.'
                      : adaptive.selection_reason}
                  </p>
                </div>
              </div>
            )}

            {/* Streak */}
            {streak >= 3 && (
              <div className="bg-gradient-to-l from-amber-500 to-orange-500 rounded-2xl p-3 text-center text-white shadow-card-lg">
                <span className="animate-fire text-xl">🔥</span>
                <span className="font-bold text-sm ml-1">{streak} Streak • ×2 XP</span>
              </div>
            )}
          </div>
        </div>

        {/* ═══ Mobile Stats Bar ═══ */}
        <div className="lg:hidden fixed top-0 inset-x-0 glass border-b border-slate-200/50 z-40 px-3 py-2 dark:border-slate-800/80">
          <div className="flex items-center justify-between max-w-lg mx-auto gap-2">
            <div className="flex items-center gap-2 text-sm">
              <span className="text-emerald-500 font-bold">{sessionStats.correct}</span>
              <span className="text-slate-400">/</span>
              <span className="text-slate-500">{sessionStats.total}</span>
            </div>
            {/* Mobile timer */}
            {!selected && question && (
              <div className={`text-xs font-bold px-2 py-0.5 rounded-full ${
                countdown > 30 ? 'text-slate-500' :
                countdown > 10 ? 'text-amber-600 bg-amber-50 dark:bg-amber-500/15' :
                countdown > 0 ? 'text-red-500 bg-red-50 dark:bg-red-500/15 animate-pulse' :
                'text-red-600 bg-red-100 dark:bg-red-500/20'
              }`}>
                {countdown > 0 ? `${Math.floor(countdown / 60)}:${String(countdown % 60).padStart(2, '0')}` : 'Time!'}
              </div>
            )}
            {streak >= 3 && <span className="text-amber-500 text-xs font-bold animate-fire">🔥{streak}</span>}
            {xpPopup && <span className="xp-popup text-teal-600 font-black text-xs">{xpPopup}</span>}
            <div className="text-xs text-amber-500 font-bold">+{sessionStats.xp} XP</div>
          </div>
          {/* Mini progress bar on mobile */}
          <div className="h-0.5 bg-slate-100 dark:bg-slate-800 rounded-full mt-1 overflow-hidden">
            <div className="h-full bg-teal-500 rounded-full transition-all duration-500" style={{ width: `${dailyPct}%` }} />
          </div>
        </div>
      </div>
    </div>
  );
}

interface StatBoxProps {
  label: string;
  value: string | number;
  icon: string;
  color?: string;
  className?: string;
}

function StatBox({ label, value, icon, color = 'text-slate-800', className = '' }: StatBoxProps) {
  return (
    <div className={`bg-white shadow-card rounded-xl p-4 text-center card-hover ${className}`}>
      <div className="text-xl mb-1">{icon}</div>
      <div className={`font-black text-2xl ${color}`}>{value}</div>
      <div className="text-slate-500 text-sm">{label}</div>
    </div>
  );
}
