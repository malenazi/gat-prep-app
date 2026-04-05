import { useCallback, useEffect, useRef, useState } from 'react';
import { api } from '@/lib/api';
import { QuestionOptions } from '@/components/questions/QuestionOptions';
import { QuestionPrompt } from '@/components/questions/QuestionPrompt';
import { useAuth } from '@/hooks/useAuth';
import { ScoreRing } from '@/components/shared/ScoreRing';
import { pageShell } from '@/lib/layout';
import { defaultQuestionAppearance } from '@/lib/questionPresentation';
import { nowMs } from '@/lib/time';
import type { ApiQuestion, DiagnosticCompleteResponse } from '@/types';

const DIAG_SESSION_KEY = 'diagnostic_session';

function saveDiagSession(progress: number) {
  localStorage.setItem(DIAG_SESSION_KEY, JSON.stringify({ phase: 'testing', progress }));
}

function clearDiagSession() {
  localStorage.removeItem(DIAG_SESSION_KEY);
}

export default function Diagnostic() {
  const { loadUser, user } = useAuth();
  const [phase, setPhase] = useState<'intro' | 'testing' | 'results'>('intro');
  const [question, setQuestion] = useState<ApiQuestion | null>(null);
  const [progress, setProgress] = useState(0);
  const [selected, setSelected] = useState<string | null>(null);
  const [results, setResults] = useState<DiagnosticCompleteResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [submittingAnswer, setSubmittingAnswer] = useState(false);
  const [error, setError] = useState('');
  const startTimeRef = useRef(0);
  const resumeCheckedRef = useRef(false);
  const total = 9;
  const appearance = defaultQuestionAppearance;

  const completeDiag = useCallback(async () => {
    try {
      const data = await api.completeDiagnostic();
      setResults(data);
      setPhase('results');
    } catch (e: unknown) {
      setError(e instanceof Error ? e.message : 'Error occurred');
    }
  }, []);

  const loadNext = useCallback(async (options?: { preserveSelection?: boolean }) => {
    setLoading(true);
    if (!options?.preserveSelection) {
      setSelected(null);
    }
    setError('');
    try {
      const data = await api.diagnosticNext();
      if (data.done) {
        setSelected(null);
        await completeDiag();
      } else if (data.question && typeof data.progress === 'number') {
        setQuestion(data.question);
        setProgress(data.progress);
        saveDiagSession(data.progress);
        setSelected(null);
        startTimeRef.current = nowMs();
      }
    } catch (e: unknown) {
      setError(e instanceof Error ? e.message : 'Error occurred');
    } finally {
      setLoading(false);
    }
  }, [completeDiag]);

  useEffect(() => {
    if (!user || user.diagnostic_completed || resumeCheckedRef.current) return;
    resumeCheckedRef.current = true;
    if (!localStorage.getItem(DIAG_SESSION_KEY)) return;
    setPhase('testing');
    void loadNext();
  }, [loadNext, user]);

  const startDiag = async () => {
    setError('');
    try {
      await api.startDiagnostic();
      saveDiagSession(0);
      setPhase('testing');
      await loadNext();
    } catch (e: unknown) {
      setError(e instanceof Error ? e.message : 'Error occurred');
    }
  };

  const submitAnswer = async (key: string) => {
    if (selected || submittingAnswer || !question || !startTimeRef.current) return;
    setSelected(key);
    setSubmittingAnswer(true);
    setError('');
    try {
      const elapsed = Math.round((nowMs() - startTimeRef.current) / 1000);
      await api.diagnosticAnswer({
        question_id: question.id,
        selected_option: key,
        time_spent_seconds: elapsed,
      });
      await loadNext({ preserveSelection: true });
    } catch (e: unknown) {
      setError(e instanceof Error ? e.message : 'An error occurred');
      setSelected(null);
    } finally {
      setSubmittingAnswer(false);
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

  if (phase === 'intro') {
    return (
      <div className="min-h-screen flex items-center justify-center p-6 text-slate-800 dark:text-slate-100" data-testid="diagnostic-page">
        <div className="max-w-2xl w-full text-center page-enter">
          <div className="text-8xl mb-6 animate-float">Test</div>
          <h1 className="text-4xl lg:text-5xl font-black text-slate-800 mb-4 dark:text-slate-100">Diagnostic Test</h1>
          <p className="text-slate-500 text-lg mb-2 dark:text-slate-400">9 questions, one for each skill</p>
          <p className="text-slate-500 text-sm mb-10 dark:text-slate-400">Takes about 5 minutes</p>
          <p className="mx-auto mb-10 max-w-xl rounded-2xl border border-teal-100 dark:border-teal-800 bg-teal-50 dark:bg-teal-950/30 px-5 py-4 text-sm text-teal-700 dark:text-teal-300">
            The diagnostic runs like a real test. We record your answers during the session and show your score guidance after the full diagnostic is complete.
          </p>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-10 text-sm">
            {[
              { icon: 'Verbal', title: 'Verbal Questions', desc: 'Comprehension, analogy, completion, contextual error' },
              { icon: 'Quant', title: 'Quantitative Questions', desc: 'Arithmetic, geometry, algebra, statistics' },
              { icon: 'Smart', title: 'Smart Adaptation', desc: 'Questions adapt automatically to your level' },
            ].map((feature, index) => (
              <div
                key={feature.title}
                className="bg-white shadow-card rounded-2xl p-5 card-hover animate-slide-up dark:bg-slate-900"
                style={{ animationDelay: `${index * 0.1}s` }}
              >
                <div className="text-2xl font-black text-teal-600 dark:text-teal-400 mb-3">{feature.icon}</div>
                <h3 className="font-bold text-slate-700 mb-1 dark:text-slate-100">{feature.title}</h3>
                <p className="text-slate-500 dark:text-slate-400">{feature.desc}</p>
              </div>
            ))}
          </div>

          {error && <p className="text-red-500 text-sm mb-4 bg-red-50 rounded-xl p-3">{error}</p>}

          <button
            onClick={startDiag}
            data-testid="diagnostic-start"
            className="bg-gradient-to-l from-teal-600 to-teal-500 text-white font-bold text-lg py-4 px-16 rounded-2xl shadow-brand hover:shadow-lg active:scale-[0.97] transition-all"
          >
            Start Now
          </button>
        </div>
      </div>
    );
  }

  if (phase === 'results' && results) {
    const verbalMastery = Math.round(results.predicted_score.verbal_mastery * 100);
    const quantMastery = Math.round(results.predicted_score.quant_mastery * 100);

    return (
      <div className="min-h-screen flex items-center justify-center p-6 text-slate-800 dark:text-slate-100" data-testid="diagnostic-results">
        <div className="max-w-lg w-full text-center page-enter">
          <div className="relative inline-block">
            <div className="text-7xl mb-4 animate-score-reveal">Done</div>
            <div className="confetti-container"><div className="c" /><div className="c" /><div className="c" /><div className="c" /><div className="c" /><div className="c" /></div>
          </div>
          <h1 className="text-3xl font-black text-slate-800 mb-6 animate-slide-up dark:text-slate-100" style={{ animationDelay: '0.1s' }}>
            Diagnostic Complete!
          </h1>

          <div className="bg-white shadow-card-lg rounded-2xl p-8 mb-6 animate-slide-up dark:bg-slate-900" style={{ animationDelay: '0.2s' }}>
            <p className="text-slate-500 text-sm mb-4 dark:text-slate-400">Predicted Score</p>
            <ScoreRing score={results.predicted_score.mid} label="of 100" />
            <p className="text-slate-500 text-sm mt-4 dark:text-slate-400">
              {results.predicted_score.low} - {results.predicted_score.high}
            </p>
          </div>

          <div className="grid grid-cols-2 gap-4 mb-8 animate-slide-up" style={{ animationDelay: '0.25s' }}>
            <div className="bg-blue-50 dark:bg-blue-950/30 border border-blue-200 dark:border-blue-800 rounded-2xl p-4">
              <p className="text-blue-400 text-sm mb-1">Verbal Section</p>
              <p className="text-blue-700 dark:text-blue-300 font-black text-2xl">{verbalMastery}%</p>
              <div className="h-1.5 bg-blue-100 dark:bg-blue-900/40 rounded-full overflow-hidden mt-2">
                <div className="h-full bg-blue-400 rounded-full transition-all duration-1000" style={{ width: `${verbalMastery}%` }} />
              </div>
            </div>
            <div className="bg-purple-50 dark:bg-purple-950/30 border border-purple-200 dark:border-purple-800 rounded-2xl p-4">
              <p className="text-purple-400 text-sm mb-1">Quantitative Section</p>
              <p className="text-purple-700 dark:text-purple-300 font-black text-2xl">{quantMastery}%</p>
              <div className="h-1.5 bg-purple-100 dark:bg-purple-900/40 rounded-full overflow-hidden mt-2">
                <div className="h-full bg-purple-400 rounded-full transition-all duration-1000" style={{ width: `${quantMastery}%` }} />
              </div>
            </div>
          </div>

          {error && <p className="text-red-500 text-sm mb-4 bg-red-50 rounded-xl p-3">{error}</p>}

          <button
            onClick={finishSetup}
            data-testid="diagnostic-finish"
            className="bg-gradient-to-l from-teal-600 to-teal-500 text-white font-bold text-lg py-4 px-16 rounded-2xl shadow-brand hover:shadow-lg active:scale-[0.97] transition-all animate-slide-up"
            style={{ animationDelay: '0.3s' }}
          >
            Start Study Plan
          </button>
        </div>
      </div>
    );
  }

  if (loading && !question) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="w-8 h-8 border-3 border-teal-400 border-t-transparent rounded-full animate-spin" />
      </div>
    );
  }

  const pct = Math.round(((progress + 1) / total) * 100);
  const milestone = progress === 3 ? 'One third done!' : progress === 6 ? 'Two thirds done, almost there' : null;

  return (
    <div className={`min-h-screen flex flex-col ${pageShell.reading} page-enter text-slate-800 dark:text-slate-100`} data-testid="diagnostic-page">
      {milestone && !selected && (
        <div className="mb-3 rounded-[1.75rem] border border-teal-200/70 bg-white/85 px-5 py-3 text-center shadow-[0_18px_48px_-34px_rgba(13,148,136,0.4)] backdrop-blur animate-slide-up lg:mb-5 dark:border-teal-800 dark:bg-slate-900">
          <p className="text-[11px] font-black uppercase tracking-[0.22em] text-teal-500 dark:text-teal-300">Progress Milestone</p>
          <p className="mt-1 text-base font-black text-teal-700 dark:text-teal-300 lg:text-lg">{milestone}</p>
        </div>
      )}

      <div className="mb-4 rounded-[2rem] border border-white/70 bg-white/80 px-5 py-4 shadow-[0_24px_55px_-36px_rgba(15,23,42,0.28)] backdrop-blur lg:mb-8 lg:px-6 lg:py-5 dark:border-slate-700 dark:bg-slate-900 dark:shadow-[0_24px_55px_-36px_rgba(0,0,0,0.5)]" data-testid="diagnostic-progress">
        <div className="mb-3 flex items-end justify-between gap-4">
          <div>
            <p className="text-[11px] font-black uppercase tracking-[0.22em] text-slate-400 dark:text-slate-500">Diagnostic Progress</p>
            <h2 className="mt-1 text-xl font-black text-slate-800 lg:text-[1.75rem] dark:text-slate-100">Question {progress + 1} of {total}</h2>
          </div>
          <div className="text-right">
            <p className="text-2xl font-black text-teal-600 dark:text-teal-400 lg:text-[2rem]">{pct}%</p>
            <p className="text-xs font-medium text-slate-400 dark:text-slate-500">completed</p>
          </div>
        </div>
        <div className="h-3 rounded-full bg-slate-200 dark:bg-slate-700 overflow-hidden">
          <div className="h-full rounded-full bg-gradient-to-r from-teal-400 via-teal-500 to-cyan-500 transition-all duration-500" style={{ width: `${pct}%` }} />
        </div>
      </div>

      {error && (
        <div className="bg-red-50 border border-red-200 rounded-xl p-3 mb-4 text-center">
          <p className="text-red-500 text-sm mb-2">{error}</p>
          <button onClick={() => { void loadNext(); }} className="text-teal-600 font-bold text-sm">Retry</button>
        </div>
      )}

      <div className="mb-4 rounded-2xl border border-amber-200/80 dark:border-amber-800/80 bg-gradient-to-r from-amber-50 dark:from-amber-950/30 to-white dark:to-slate-900 px-4 py-2.5 flex items-center gap-3" data-testid="diagnostic-testing-note">
        <span className="text-[11px] font-black uppercase tracking-[0.18em] text-amber-600 dark:text-amber-400 shrink-0">Test Mode</span>
        <span className="text-sm text-slate-500 dark:text-slate-400">Review and explanations are hidden until the diagnostic is finished.</span>
      </div>

      {question && (
        <div className="flex-1" data-testid="diagnostic-question-card">
          <QuestionPrompt
            passage_ar={question.passage_ar}
            table_ar={question.table_ar}
            table_caption={question.table_caption}
            figure_svg={question.figure_svg}
            figure_alt={question.figure_alt}
            text_ar={question.text_ar}
            content_format={question.content_format}
            comparison_columns={question.comparison_columns}
            testIdPrefix="diagnostic-question"
            appearance={appearance}
          />

          <QuestionOptions
            options={question.options}
            contentFormat={question.content_format}
            selectedKey={selected}
            correctOption={null}
            disabled={!!selected || submittingAnswer || loading}
            onSelect={submitAnswer}
            testIdPrefix="diagnostic"
            appearance={appearance}
          />

          {(submittingAnswer || loading) && (
            <div className="mt-4 rounded-2xl border border-teal-100 dark:border-teal-800 bg-teal-50 dark:bg-teal-950/30 px-4 py-3 text-sm font-medium text-teal-700 dark:text-teal-300" data-testid="diagnostic-submitting">
              Answer saved. Moving to the next question...
            </div>
          )}
        </div>
      )}
    </div>
  );
}
