import { useState, useEffect, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import { api } from '@/lib/api';
import { useAuth } from '@/hooks/useAuth';
import type { ApiQuestion, PracticeAnswerFeedback, TodayPlan } from '@/types';

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
  const [selected, setSelected] = useState<string | null>(null);
  const [feedback, setFeedback] = useState<FeedbackWithLate | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [startTime, setStartTime] = useState<number | null>(null);
  const [sessionStats, setStats] = useState<SessionStats>({ total: 0, correct: 0, xp: 0 });
  const [done, setDone] = useState(false);
  const [streak, setStreak] = useState(0);
  const [showExitConfirm, setShowExitConfirm] = useState(false);
  const [xpPopup, setXpPopup] = useState<string | null>(null);
  const [todayTarget, setTodayTarget] = useState(15);
  const [todayCompleted, setTodayCompleted] = useState(0);
  const [countdown, setCountdown] = useState(90);
  const [_isLate, setIsLate] = useState(false);
  const feedbackRef = useRef<HTMLDivElement>(null);

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

  // Restore session stats from localStorage
  useEffect(() => {
    const saved = loadPracticeSession();
    if (saved) {
      setStats(saved.stats);
      setStreak(saved.streak);
    }
  }, []);

  useEffect(() => {
    api.today().then((t: TodayPlan) => {
      setTodayTarget(t.target_questions || 15);
      setTodayCompleted(t.completed_questions || 0);
    }).catch(() => {});
    loadNext();
  }, []);

  const loadNext = async () => {
    setLoading(true); setSelected(null); setFeedback(null); setError(''); setXpPopup(null); setIsLate(false); setCountdown(QUESTION_TIME);
    try {
      const data = await api.practiceNext();
      if (data.done) setDone(true);
      else { setQuestion(data.question!); setStartTime(Date.now()); setCountdown(QUESTION_TIME); }
    } catch (e: any) {
      if (sessionStats.total > 0) setDone(true);
      else setError(e.message || 'Error loading question');
    }
    setLoading(false);
  };

  const submitAnswer = async (key: string) => {
    if (selected) return;
    if (!startTime) return;
    setSelected(key);
    const wasLate = countdown <= 0;
    setIsLate(wasLate);
    try {
      const elapsed = Math.round((Date.now() - startTime!) / 1000);
      const data: PracticeAnswerFeedback = await api.practiceAnswer({ question_id: question!.id, selected_option: key, time_spent_seconds: elapsed });
      setFeedback({ ...data, wasLate });
      const newStreak = data.is_correct ? streak + 1 : 0;
      setStreak(newStreak);
      const newStats = { total: sessionStats.total + 1, correct: sessionStats.correct + (data.is_correct ? 1 : 0), xp: sessionStats.xp + data.xp_earned };
      setStats(newStats);
      savePracticeSession({
        date: new Date().toISOString().split('T')[0],
        stats: newStats,
        streak: newStreak,
      });
      setTodayCompleted(prev => prev + 1);
      // XP popup
      const bonusText = newStreak >= 3 ? ` (×2 🔥)` : '';
      setXpPopup(`+${data.xp_earned} XP${bonusText}`);
      setTimeout(() => setXpPopup(null), 2000);
    } catch (e: any) { setError(e.message || 'Error occurred'); setSelected(null); }
  };

  const finish = async () => { clearPracticeSession(); await loadUser(); nav('/'); };
  const tryExit = () => { if (sessionStats.total > 0 && !done) setShowExitConfirm(true); else finish(); };
  const accuracy = sessionStats.total > 0 ? Math.round(sessionStats.correct / sessionStats.total * 100) : 0;
  const dailyPct = Math.min(100, Math.round((todayCompleted / Math.max(1, todayTarget)) * 100));

  if (error && !question) return (
    <div className="min-h-[60vh] flex flex-col items-center justify-center p-6 text-center page-enter">
      <div className="text-5xl mb-4">⚠️</div>
      <p className="text-red-500 mb-4">{error}</p>
      <div className="flex gap-3">
        <button onClick={loadNext} className="bg-teal-600 text-white font-bold py-2.5 px-6 rounded-xl shadow-brand">Retry</button>
        <button onClick={finish} className="bg-white shadow-card text-slate-600 font-bold py-2.5 px-6 rounded-xl">Back</button>
      </div>
    </div>
  );

  if (done) return (
    <div className="min-h-[60vh] flex flex-col items-center justify-center p-6 text-center page-enter">
      <div className="relative">
        <div className="text-7xl mb-4 animate-score-reveal">💪</div>
        <Confetti />
      </div>
      <h1 className="text-3xl font-black text-slate-800 mb-2">Well Done!</h1>
      <p className="text-slate-500 mb-8">You completed your training session</p>
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4 w-full max-w-lg mb-8">
        <StatBox label="Questions" value={sessionStats.total} icon="📝" className="stagger-1" />
        <StatBox label="Correct" value={sessionStats.correct} icon="✅" color="text-emerald-500" className="stagger-2" />
        <StatBox label="Accuracy" value={`${accuracy}%`} icon="🎯" color="text-teal-600" className="stagger-3" />
        <StatBox label="XP" value={`+${sessionStats.xp}`} icon="⚡" color="text-amber-500" className="stagger-4" />
      </div>
      {dailyPct >= 100 && (
        <div className="mb-6 bg-gradient-to-l from-emerald-500 to-emerald-600 text-white rounded-2xl px-6 py-3 font-bold animate-slide-up flex items-center gap-2">
          <Confetti /> 🎉 You completed today's goal!
        </div>
      )}
      <button onClick={finish} className="bg-gradient-to-l from-teal-600 to-teal-500 text-white font-bold py-3.5 px-12 rounded-xl shadow-brand hover:shadow-lg transition-all">
        Back to Home
      </button>
    </div>
  );

  if (loading && !question) return (
    <div className="min-h-[60vh] flex items-center justify-center">
      <div className="w-8 h-8 border-3 border-teal-400 border-t-transparent rounded-full animate-spin" />
    </div>
  );

  return (
    <div className="p-3 lg:p-10 pt-12 lg:pt-10 max-w-6xl mx-auto page-enter">
      {/* Exit confirmation */}
      {showExitConfirm && (
        <div className="fixed inset-0 bg-slate-900/40 backdrop-blur-sm flex items-center justify-center z-50 p-6">
          <div className="bg-white rounded-2xl p-8 w-full max-w-sm text-center shadow-card-lg animate-slide-up">
            <p className="text-slate-800 font-bold text-lg mb-1">End Session?</p>
            <p className="text-slate-500 text-sm mb-6">You've answered {sessionStats.total} questions so far</p>
            <div className="flex gap-3">
              <button onClick={() => setShowExitConfirm(false)} className="flex-1 bg-slate-100 text-slate-700 font-bold py-3 rounded-xl hover:bg-slate-200 transition">Continue</button>
              <button onClick={finish} className="flex-1 bg-red-500 text-white font-bold py-3 rounded-xl hover:bg-red-600 transition">End</button>
            </div>
          </div>
        </div>
      )}

      {/* ═══ Daily Progress Bar (top) ═══ */}
      <div className="bg-white shadow-card rounded-2xl p-2 lg:p-4 mb-2 lg:mb-6 stagger-1">
        <div className="flex items-center justify-between mb-2">
          <span className="text-slate-600 text-sm font-bold">Question {sessionStats.total + 1} • Daily Goal</span>
          <div className="flex items-center gap-3">
            {/* Estimated time to finish today */}
            {todayCompleted < todayTarget && (
              <span className="text-sm text-slate-500 flex items-center gap-1">
                <svg className="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}><path strokeLinecap="round" strokeLinejoin="round" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                ~{Math.ceil((todayTarget - todayCompleted) * QUESTION_TIME / 60)} minutes remaining
              </span>
            )}
            <span className="text-sm font-bold text-teal-600">{todayCompleted}/{todayTarget}</span>
          </div>
        </div>
        <div className="h-2 lg:h-2.5 bg-slate-100 rounded-full overflow-hidden">
          <div className="h-full bg-gradient-to-l from-teal-400 to-teal-600 rounded-full transition-all duration-500" style={{ width: `${dailyPct}%` }} />
        </div>
        {dailyPct >= 100 && <p className="text-emerald-500 text-sm font-bold mt-1.5">🎉 Goal completed! Keep going for excellence</p>}
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-[1fr_280px] gap-8">
        {/* ═══ Main Question Area ═══ */}
        <div>
          <div className="flex items-center justify-between mb-3 lg:mb-6">
            <button onClick={tryExit} className="text-slate-500 hover:text-slate-700 text-sm transition flex items-center gap-1.5">
              <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}><path strokeLinecap="round" strokeLinejoin="round" d="M6 18L18 6M6 6l12 12" /></svg>
              End
            </button>
            <div className="flex items-center gap-2">
              {streak >= 3 && (
                <div className="flex items-center gap-1 bg-gradient-to-l from-amber-500 to-orange-500 text-white text-sm font-bold px-3 py-1.5 rounded-full animate-pulse-glow">
                  🔥 {streak} Streak • ×2 XP
                </div>
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
            <div className="mb-3 lg:mb-5 flex items-center justify-between">
              <span className="bg-slate-100 text-slate-500 text-sm px-4 py-1.5 rounded-full font-medium">
                {question.skill_id.startsWith('verbal') ? '📖 Verbal' : '🔢 Quant'} • {question.question_type}
              </span>
              {/* Countdown Timer */}
              {!selected && (
                <div className={`flex items-center gap-1.5 text-sm font-bold px-3 py-1.5 rounded-full transition-all
                  ${countdown > 30 ? 'bg-slate-100 text-slate-500' :
                    countdown > 10 ? 'bg-amber-50 text-amber-600' :
                    countdown > 0 ? 'bg-red-50 text-red-500 animate-pulse' :
                    'bg-red-100 text-red-600'}`}>
                  <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}><path strokeLinecap="round" strokeLinejoin="round" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                  {countdown > 0 ? (
                    <span>{Math.floor(countdown / 60)}:{String(countdown % 60).padStart(2, '0')}</span>
                  ) : (
                    <span>⏰ Time exceeded</span>
                  )}
                </div>
              )}
              {/* Late badge after answering */}
              {selected && feedback?.wasLate && (
                <span className="bg-red-50 text-red-500 text-sm font-bold px-3 py-1.5 rounded-full flex items-center gap-1">
                  ⏰ Late answer
                </span>
              )}
            </div>
          )}

          {question && (
            <div>
              {question.passage_ar && (
                <div className="bg-slate-50 border border-slate-200 rounded-xl lg:rounded-2xl p-3 lg:p-6 mb-3 lg:mb-5 text-sm text-slate-600 leading-relaxed max-h-28 lg:max-h-none overflow-y-auto">
                  {question.passage_ar}
                </div>
              )}

              <h2 className="text-base lg:text-2xl font-bold text-slate-800 mb-3 lg:mb-8 leading-relaxed lg:leading-loose whitespace-pre-line math-text">{question.text_ar}</h2>

              <div className="space-y-2 lg:space-y-3">
                {question.options.map(opt => {
                  let cls = 'bg-white border-slate-200 hover:border-teal-300 hover:shadow-sm active:scale-[0.99]';
                  if (selected && feedback) {
                    if (opt.key === feedback.correct_option) cls = 'bg-emerald-50 border-emerald-400 shadow-sm';
                    else if (opt.key === selected && !feedback.is_correct) cls = 'bg-red-50 border-red-400 shadow-sm';
                    else cls = 'bg-slate-50 border-slate-100 opacity-40';
                  } else if (selected && opt.key === selected) {
                    cls = 'bg-teal-50 border-teal-400 shadow-sm';
                  }
                  const anim = selected && feedback && opt.key === selected ? (feedback.is_correct ? 'animate-correct' : 'animate-wrong') : '';

                  return (
                    <button key={opt.key} onClick={() => submitAnswer(opt.key)} disabled={!!selected}
                      className={`w-full text-left border-2 rounded-xl p-2.5 lg:p-5 transition-all ${cls} ${anim}`}>
                      <div className="flex items-start gap-3 lg:gap-4">
                        <span className={`w-8 h-8 lg:w-10 lg:h-10 rounded-lg lg:rounded-xl flex items-center justify-center text-xs lg:text-sm font-bold shrink-0 transition-all
                          ${selected && feedback && opt.key === feedback.correct_option ? 'bg-emerald-500 text-white' :
                            selected && feedback && opt.key === selected && !feedback.is_correct ? 'bg-red-500 text-white' :
                            selected && !feedback && opt.key === selected ? 'bg-teal-500 text-white' :
                            'bg-slate-100 text-slate-600'}`}>
                          {opt.label}
                        </span>
                        <span className="text-sm lg:text-base text-slate-700 leading-relaxed">{opt.text_ar}</span>
                      </div>
                    </button>
                  );
                })}
              </div>

              {feedback && (
                <div ref={feedbackRef} className="mt-3 lg:mt-6 animate-slide-up">
                  <div className={`rounded-xl lg:rounded-2xl p-3 lg:p-6 ${feedback.is_correct ? 'bg-emerald-50 border border-emerald-200' : 'bg-amber-50 border border-amber-200'}`}>
                    <div className="flex items-center gap-2 mb-2">
                      <span className="text-2xl">{feedback.is_correct ? '💪' : '🤔'}</span>
                      <p className={`font-bold text-sm lg:text-base ${feedback.is_correct ? 'text-emerald-600' : 'text-amber-600'}`}>
                        {feedback.is_correct ? 'Correct! Well done' : 'Wrong — no worries'}
                      </p>
                      {feedback.wasLate && (
                        <span className="text-red-400 text-sm font-medium mr-auto">⏰ Late</span>
                      )}
                    </div>
                    <p className="text-slate-600 text-sm leading-loose whitespace-pre-line math-text">{feedback.explanation_ar}</p>
                    {feedback.solution_steps_ar && (
                      <div className="mt-3 space-y-1 border-t border-current/10 pt-3">
                        {feedback.solution_steps_ar.map((step, i) => (
                          <p key={i} className="text-slate-500 text-sm">{step}</p>
                        ))}
                      </div>
                    )}
                  </div>
                  <button onClick={loadNext}
                    className="w-full mt-3 lg:mt-4 bg-gradient-to-l from-teal-600 to-teal-500 text-white font-bold py-3 lg:py-4 rounded-xl shadow-brand hover:shadow-lg transition-all active:scale-[0.98]">
                    Next Question ←
                  </button>
                </div>
              )}
            </div>
          )}
        </div>

        {/* ═══ Desktop Stats Sidebar ═══ */}
        <div className="hidden lg:block">
          <div className="sticky top-24 space-y-4">
            <div className="bg-white shadow-card rounded-2xl p-5">
              <h3 className="text-slate-800 font-bold text-sm mb-4">Session Statistics</h3>
              <div className="space-y-4">
                <SideStatRow label="Questions" value={sessionStats.total} />
                <SideStatRow label="Correct" value={sessionStats.correct} color="text-emerald-500" />
                <SideStatRow label="Accuracy" value={`${accuracy}%`} color="text-teal-600" />
                <SideStatRow label="XP Earned" value={`+${sessionStats.xp}`} color="text-amber-500" />
              </div>
              <div className="mt-5 flex justify-center">
                <div className="relative w-20 h-20">
                  <svg viewBox="0 0 100 100" className="w-full h-full">
                    <circle cx="50" cy="50" r="40" fill="none" stroke="#e2e8f0" strokeWidth="8" />
                    <circle cx="50" cy="50" r="40" fill="none" stroke="#0d9488" strokeWidth="8"
                      strokeDasharray="251" strokeDashoffset={251 - (251 * accuracy / 100)} strokeLinecap="round"
                      transform="rotate(-90 50 50)" style={{ transition: 'stroke-dashoffset 0.5s ease' }} />
                  </svg>
                  <div className="absolute inset-0 flex items-center justify-center">
                    <span className="text-lg font-black text-slate-700">{accuracy}%</span>
                  </div>
                </div>
              </div>
            </div>

            {streak >= 3 && (
              <div className="bg-gradient-to-l from-amber-500 to-orange-500 rounded-2xl p-4 text-center text-white shadow-card-lg">
                <div className="text-3xl animate-fire mb-1">🔥</div>
                <p className="font-bold text-sm">{streak} Streak!</p>
                <p className="text-white/90 text-sm">×2 XP Multiplier</p>
              </div>
            )}
          </div>
        </div>

        {/* ═══ Mobile Stats Bar ═══ */}
        <div className="lg:hidden fixed top-0 inset-x-0 glass border-b border-slate-200/50 z-40 px-4 py-2.5">
          <div className="flex items-center justify-between max-w-lg mx-auto">
            <div className="flex items-center gap-2 text-sm">
              <span className="text-emerald-500 font-bold">{sessionStats.correct}</span>
              <span className="text-slate-500">/</span>
              <span className="text-slate-500">{sessionStats.total}</span>
            </div>
            {xpPopup && <span className="xp-popup text-teal-600 font-bold text-sm">{xpPopup}</span>}
            <div className="text-sm text-amber-500 font-bold">+{sessionStats.xp} XP</div>
          </div>
        </div>
      </div>
    </div>
  );
}

interface SideStatRowProps {
  label: string;
  value: string | number;
  color?: string;
}

function SideStatRow({ label, value, color = 'text-slate-800' }: SideStatRowProps) {
  return (
    <div className="flex justify-between items-center">
      <span className="text-slate-500 text-sm">{label}</span>
      <span className={`font-bold text-lg ${color}`}>{value}</span>
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
