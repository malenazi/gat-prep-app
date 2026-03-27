import { useState, useRef, useEffect } from 'react';
import { api } from '@/lib/api';
import { useAuth } from '@/hooks/useAuth';
import { ScoreRing } from '@/components/shared/ScoreRing';
import type { ApiQuestion, AnswerFeedback, DiagnosticCompleteResponse } from '@/types';

const DIAG_SESSION_KEY = 'diagnostic_session';
function saveDiagSession(progress: number) {
  localStorage.setItem(DIAG_SESSION_KEY, JSON.stringify({ phase: 'testing', progress }));
}
function clearDiagSession() { localStorage.removeItem(DIAG_SESSION_KEY); }

export default function Diagnostic() {
  const { loadUser, user } = useAuth();
  const [phase, setPhase] = useState<'intro' | 'testing' | 'feedback' | 'results'>('intro');
  const [question, setQuestion] = useState<ApiQuestion | null>(null);
  const [progress, setProgress] = useState(0);
  const total = 9;
  const [selected, setSelected] = useState<string | null>(null);
  const [feedback, setFeedback] = useState<AnswerFeedback | null>(null);
  const [results, setResults] = useState<DiagnosticCompleteResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [startTime, setStartTime] = useState<number>(0);
  const feedbackRef = useRef<HTMLDivElement>(null);

  // Auto-scroll to feedback/next button when it appears
  useEffect(() => {
    if (feedback && feedbackRef.current) {
      feedbackRef.current.scrollIntoView({ behavior: 'smooth', block: 'end' });
    }
  }, [feedback]);

  // Resume diagnostic session from localStorage
  useEffect(() => {
    if (user && !user.diagnostic_completed) {
      const saved = localStorage.getItem(DIAG_SESSION_KEY);
      if (saved) {
        // Resume — skip intro, load next question
        setPhase('testing');
        loadNext();
      }
    }
  }, []);

  const startDiag = async () => {
    setError('');
    try {
      await api.startDiagnostic();
      saveDiagSession(0);
      setPhase('testing');
      loadNext();
    } catch (e: unknown) {
      setError(e instanceof Error ? e.message : 'Error occurred');
    }
  };

  const loadNext = async () => {
    setLoading(true); setSelected(null); setFeedback(null); setError('');
    try {
      const data = await api.diagnosticNext();
      if (data.done) await completeDiag();
      else { setQuestion(data.question!); setProgress(data.progress!); saveDiagSession(data.progress!); setStartTime(Date.now()); }
    } catch (e: unknown) {
      setError(e instanceof Error ? e.message : 'Error occurred');
    }
    setLoading(false);
  };

  const submitAnswer = async (key: string) => {
    if (selected || !question) return;
    setSelected(key); setError('');
    try {
      const elapsed = Math.round((Date.now() - startTime) / 1000);
      const data = await api.diagnosticAnswer({ question_id: question.id, selected_option: key, time_spent_seconds: elapsed });
      setFeedback(data);
      // No explanation shown — auto-advance after brief delay
      setTimeout(() => { setPhase('testing'); loadNext(); }, 800);
    } catch (e: unknown) {
      setError(e instanceof Error ? e.message : 'حدث خطأ');
      setSelected(null);
    }
  };

  const completeDiag = async () => {
    try {
      const data = await api.completeDiagnostic();
      setResults(data); setPhase('results');
    } catch (e: unknown) {
      setError(e instanceof Error ? e.message : 'Error occurred');
    }
  };

  const finishSetup = async () => {
    setError('');
    clearDiagSession();
    try {
      await loadUser();
    } catch (e: unknown) {
      setError(e instanceof Error ? e.message : 'Error occurred');
    }
  };

  // ── Intro ──
  if (phase === 'intro') {
    return (
      <div className="min-h-screen flex items-center justify-center p-6">
        <div className="max-w-2xl w-full text-center page-enter">
          <div className="text-8xl mb-6 animate-float">🧠</div>
          <h1 className="text-4xl lg:text-5xl font-black text-slate-800 mb-4">Diagnostic Test</h1>
          <p className="text-slate-500 text-lg mb-2">9 questions — one for each skill</p>
          <p className="text-slate-500 text-sm mb-10">Takes about 5 minutes</p>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-10 text-sm">
            {[
              { icon: '📖', title: 'Verbal Questions', desc: 'Comprehension, analogy, completion, contextual error' },
              { icon: '🔢', title: 'Quantitative Questions', desc: 'Arithmetic, geometry, algebra, statistics' },
              { icon: '🎯', title: 'Smart Adaptation', desc: 'Questions adapt automatically to your level' },
            ].map((f, i) => (
              <div key={i} className="bg-white shadow-card rounded-2xl p-5 card-hover animate-slide-up" style={{ animationDelay: `${i * 0.1}s` }}>
                <div className="text-3xl mb-3">{f.icon}</div>
                <h3 className="font-bold text-slate-700 mb-1">{f.title}</h3>
                <p className="text-slate-500">{f.desc}</p>
              </div>
            ))}
          </div>

          {error && <p className="text-red-500 text-sm mb-4 bg-red-50 rounded-xl p-3">{error}</p>}

          <button onClick={startDiag}
            className="bg-gradient-to-l from-teal-600 to-teal-500 text-white font-bold text-lg py-4 px-16 rounded-2xl shadow-brand hover:shadow-lg active:scale-[0.97] transition-all">
            Start Now
          </button>
        </div>
      </div>
    );
  }

  // ── Results ──
  if (phase === 'results' && results) {
    const vMastery = Math.round(results.predicted_score.verbal_mastery * 100);
    const qMastery = Math.round(results.predicted_score.quant_mastery * 100);
    return (
      <div className="min-h-screen flex items-center justify-center p-6">
        <div className="max-w-lg w-full text-center page-enter">
          <div className="relative inline-block">
            <div className="text-7xl mb-4 animate-score-reveal">🎉</div>
            <div className="confetti-container"><div className="c" /><div className="c" /><div className="c" /><div className="c" /><div className="c" /><div className="c" /></div>
          </div>
          <h1 className="text-3xl font-black text-slate-800 mb-6 animate-slide-up" style={{ animationDelay: '0.1s' }}>Diagnostic Complete!</h1>

          <div className="bg-white shadow-card-lg rounded-2xl p-8 mb-6 animate-slide-up" style={{ animationDelay: '0.2s' }}>
            <p className="text-slate-500 text-sm mb-4">Predicted Score</p>
            <ScoreRing score={results.predicted_score.mid} label="of 100" />
            <p className="text-slate-500 text-sm mt-4">{results.predicted_score.low} – {results.predicted_score.high}</p>
          </div>

          <div className="grid grid-cols-2 gap-4 mb-8 animate-slide-up" style={{ animationDelay: '0.25s' }}>
            <div className="bg-blue-50 border border-blue-200 rounded-2xl p-4">
              <p className="text-blue-400 text-sm mb-1">📖 Verbal Section</p>
              <p className="text-blue-700 font-black text-2xl">{vMastery}%</p>
              <div className="h-1.5 bg-blue-100 rounded-full overflow-hidden mt-2">
                <div className="h-full bg-blue-400 rounded-full transition-all duration-1000" style={{ width: `${vMastery}%` }} />
              </div>
            </div>
            <div className="bg-purple-50 border border-purple-200 rounded-2xl p-4">
              <p className="text-purple-400 text-sm mb-1">🔢 Quantitative Section</p>
              <p className="text-purple-700 font-black text-2xl">{qMastery}%</p>
              <div className="h-1.5 bg-purple-100 rounded-full overflow-hidden mt-2">
                <div className="h-full bg-purple-400 rounded-full transition-all duration-1000" style={{ width: `${qMastery}%` }} />
              </div>
            </div>
          </div>

          {error && <p className="text-red-500 text-sm mb-4 bg-red-50 rounded-xl p-3">{error}</p>}

          <button onClick={finishSetup}
            className="bg-gradient-to-l from-teal-600 to-teal-500 text-white font-bold text-lg py-4 px-16 rounded-2xl shadow-brand hover:shadow-lg active:scale-[0.97] transition-all animate-slide-up"
            style={{ animationDelay: '0.3s' }}>
            Start Study Plan ←
          </button>
        </div>
      </div>
    );
  }

  // ── Question / Feedback ──
  if (loading && !question) return (
    <div className="min-h-screen flex items-center justify-center">
      <div className="w-8 h-8 border-3 border-teal-400 border-t-transparent rounded-full animate-spin" />
    </div>
  );

  const pct = Math.round(((progress + 1) / total) * 100);
  const milestone = progress === 3 ? '🚀 One third done!' : progress === 6 ? '💪 Two thirds! Almost there' : null;

  return (
    <div className="min-h-screen flex flex-col p-3 lg:p-10 max-w-3xl mx-auto page-enter">
      {milestone && !selected && (
        <div className="bg-gradient-to-l from-teal-500 to-teal-600 text-white rounded-xl px-4 py-2 mb-2 lg:mb-4 text-center font-bold text-sm animate-slide-up shadow-brand">
          {milestone}
        </div>
      )}

      <div className="mb-3 lg:mb-8">
        <div className="flex justify-between text-sm text-slate-500 mb-1.5">
          <span>Question {progress + 1} of {total}</span>
          <span className="font-bold text-teal-600">{pct}%</span>
        </div>
        <div className="h-2 lg:h-2.5 bg-slate-100 rounded-full overflow-hidden">
          <div className="h-full bg-gradient-to-l from-teal-400 to-teal-600 rounded-full transition-all duration-500" style={{ width: `${pct}%` }} />
        </div>
      </div>

      {error && (
        <div className="bg-red-50 border border-red-200 rounded-xl p-3 mb-4 text-center">
          <p className="text-red-500 text-sm mb-2">{error}</p>
          <button onClick={loadNext} className="text-teal-600 font-bold text-sm">Retry</button>
        </div>
      )}

      {question && (
        <div className="flex-1">
          {question.passage_ar && (
            <div className="bg-slate-50 border border-slate-200 rounded-xl lg:rounded-2xl p-3 lg:p-6 mb-3 lg:mb-5 text-sm text-slate-600 leading-relaxed max-h-28 lg:max-h-none overflow-y-auto">
              {question.passage_ar}
            </div>
          )}

          <h2 className="text-base lg:text-2xl font-bold text-slate-800 mb-3 lg:mb-8 leading-relaxed lg:leading-loose whitespace-pre-line math-text">{question.text_ar}</h2>

          <div className="space-y-2 lg:space-y-3">
            {question.options.map(opt => {
              let cls = 'bg-white border-slate-200 hover:border-teal-300 hover:shadow-sm';
              if (selected && feedback) {
                if (opt.key === feedback.correct_option) cls = 'bg-emerald-50 border-emerald-400';
                else if (opt.key === selected && !feedback.is_correct) cls = 'bg-red-50 border-red-400';
                else cls = 'bg-slate-50 border-slate-100 opacity-50';
              } else if (selected && opt.key === selected) {
                cls = 'bg-teal-50 border-teal-400';
              }
              const anim = selected && feedback && opt.key === selected ? (feedback.is_correct ? 'animate-correct' : 'animate-wrong') : '';

              return (
                <button key={opt.key} onClick={() => submitAnswer(opt.key)} disabled={!!selected}
                  className={`w-full text-left border-2 rounded-xl p-2.5 lg:p-5 transition-all ${cls} ${anim}`}>
                  <div className="flex items-start gap-3 lg:gap-4">
                    <span className={`w-8 h-8 lg:w-10 lg:h-10 rounded-lg lg:rounded-xl flex items-center justify-center text-xs lg:text-sm font-bold shrink-0
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

          {/* No explanation during diagnostic — auto-advances after 800ms */}
        </div>
      )}
    </div>
  );
}
