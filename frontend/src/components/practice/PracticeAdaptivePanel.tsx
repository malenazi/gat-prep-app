import { useState } from 'react';

import type { ApiQuestion, PracticeAdaptiveMeta } from '@/types';

interface PracticeAdaptivePanelProps {
  adaptive: PracticeAdaptiveMeta;
  question: ApiQuestion;
  countdown: number;
  selected: boolean;
  wasLate: boolean;
}

function getSectionLabel(section: string) {
  if (section === 'verbal') return 'Verbal';
  if (section === 'quant') return 'Quant';
  return section || 'Practice';
}

export function PracticeAdaptivePanel({
  adaptive,
  question,
  countdown,
  selected,
  wasLate,
}: PracticeAdaptivePanelProps) {
  const [showReason, setShowReason] = useState(false);
  const [mobileExpanded, setMobileExpanded] = useState(false);
  const isCalibrating = adaptive.challenge_band === 'Calibrating';

  return (
    <section
      className="mb-5 rounded-3xl border border-teal-100 bg-white p-4 lg:p-5 shadow-card dark:border-slate-800 dark:bg-slate-900"
      data-testid="practice-adaptive-panel"
    >
      {/* ═══ Compact mobile header (always visible) ═══ */}
      <div className="flex flex-wrap items-center gap-2">
        <span
          className="rounded-full bg-slate-100 px-3 py-1 text-xs font-black uppercase tracking-[0.16em] text-slate-600 dark:bg-slate-800 dark:text-slate-300"
          data-testid="practice-skill-chip"
        >
          {adaptive.skill_name}
        </span>
        <span
          className="rounded-full bg-teal-50 px-3 py-1 text-sm font-bold text-teal-700 dark:bg-teal-500/15 dark:text-teal-200"
          data-testid="practice-level-chip"
        >
          {adaptive.difficulty_label} <span className="ml-1 text-teal-600/80 dark:text-teal-200/80">{adaptive.difficulty_score}/100</span>
        </span>
        <span
          className="rounded-full bg-amber-50 px-3 py-1 text-sm font-bold text-amber-700 dark:bg-amber-500/15 dark:text-amber-200"
          data-testid="practice-challenge-chip"
        >
          {adaptive.challenge_band}
        </span>

        {/* Timer inline on mobile */}
        <div className="flex items-center gap-2 ml-auto lg:hidden">
          {!selected && (
            <div
              className={`flex items-center gap-1 rounded-full px-2.5 py-1 text-xs font-bold transition-all ${
                countdown > 30 ? 'bg-slate-100 text-slate-600 dark:bg-slate-800 dark:text-slate-200' :
                countdown > 10 ? 'bg-amber-50 text-amber-700 dark:bg-amber-500/15 dark:text-amber-200' :
                countdown > 0 ? 'bg-red-50 text-red-600 dark:bg-red-500/15 dark:text-red-200 animate-pulse' :
                'bg-red-100 text-red-700 dark:bg-red-500/20 dark:text-red-100'
              }`}
            >
              <svg className="h-3.5 w-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                <path strokeLinecap="round" strokeLinejoin="round" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              {countdown > 0 ? <span>{Math.floor(countdown / 60)}:{String(countdown % 60).padStart(2, '0')}</span> : <span>Time!</span>}
            </div>
          )}
          {selected && wasLate && (
            <span className="rounded-full bg-red-50 px-2.5 py-1 text-xs font-bold text-red-600 dark:bg-red-500/15 dark:text-red-200">Late</span>
          )}
        </div>

        {/* Mobile expand toggle */}
        <button type="button" onClick={() => setMobileExpanded(v => !v)} className="lg:hidden text-xs text-teal-600 dark:text-teal-300 font-bold ml-1">
          {mobileExpanded ? 'Less' : 'More'}
        </button>
      </div>

      {/* ═══ Expanded details (always on desktop, toggle on mobile) ═══ */}
      <div className={`${mobileExpanded ? '' : 'hidden'} lg:block`}>
        <div className="flex flex-col gap-4 lg:flex-row lg:items-start lg:justify-between mt-4">
          <div className="min-w-0">
            <h2 className="text-2xl font-black text-slate-900 dark:text-slate-50">
              {adaptive.skill_name} practice
            </h2>
            <p className="mt-1 text-sm font-semibold uppercase tracking-[0.16em] text-slate-400 dark:text-slate-500">
              {getSectionLabel(adaptive.skill_section)} / {question.question_type.replace(/_/g, ' ')}
            </p>
            <p
              className="mt-3 text-sm font-medium text-slate-600 dark:text-slate-300"
              data-testid="practice-skill-mastery"
            >
              {isCalibrating
                ? 'Starting level: we are calibrating this skill for you.'
                : `Your mastery in this skill: ${adaptive.skill_mastery}%`}
            </p>
            {!isCalibrating && (
              <p className="mt-1 text-xs italic text-slate-400 dark:text-slate-500">
                {adaptive.challenge_band === 'Reinforcement' ? 'This is below your level \u2014 good for reinforcement.' :
                 adaptive.challenge_band === 'At your level' ? 'This matches your current ability.' :
                 adaptive.challenge_band === 'Stretch' ? 'This is slightly above your level \u2014 a good stretch.' :
                 adaptive.challenge_band === 'Challenge+' ? 'This is well above your level \u2014 a real challenge.' :
                 'Calibrating your level with this question.'}
              </p>
            )}
          </div>

          {/* Desktop-only timer */}
          <div className="hidden lg:flex flex-wrap items-center gap-2 lg:justify-end">
            {!selected && (
              <div
                data-testid="practice-timer"
                className={`flex items-center gap-1.5 rounded-full px-3 py-1.5 text-sm font-bold transition-all ${
                  countdown > 30
                    ? 'bg-slate-100 text-slate-600 dark:bg-slate-800 dark:text-slate-200'
                    : countdown > 10
                      ? 'bg-amber-50 text-amber-700 dark:bg-amber-500/15 dark:text-amber-200'
                      : countdown > 0
                        ? 'bg-red-50 text-red-600 dark:bg-red-500/15 dark:text-red-200'
                        : 'bg-red-100 text-red-700 dark:bg-red-500/20 dark:text-red-100'
                }`}
              >
                <svg className="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                  <path strokeLinecap="round" strokeLinejoin="round" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                {countdown > 0 ? (
                  <span>{Math.floor(countdown / 60)}:{String(countdown % 60).padStart(2, '0')}</span>
                ) : (
                  <span>Time exceeded</span>
                )}
              </div>
            )}

            {selected && wasLate && (
              <span className="rounded-full bg-red-50 px-3 py-1.5 text-sm font-bold text-red-600 dark:bg-red-500/15 dark:text-red-200">
                Late answer
              </span>
            )}
          </div>
        </div>
      </div>

      <div className="mt-4 rounded-2xl border border-slate-200 bg-slate-50 px-4 py-3 dark:border-slate-800 dark:bg-slate-950/70">
        <button
          type="button"
          className="flex w-full items-center justify-between gap-3 text-left"
          aria-expanded={showReason}
          data-testid="practice-selection-reason-toggle"
          onClick={() => setShowReason((value) => !value)}
        >
          <span className="text-sm font-bold text-slate-800 dark:text-slate-100">Why this question?</span>
          <span className="text-xs font-black uppercase tracking-[0.16em] text-teal-600 dark:text-teal-300">
            {showReason ? 'Hide' : 'Show'}
          </span>
        </button>
        {showReason && (
          <p
            className="mt-3 text-sm leading-relaxed text-slate-600 dark:text-slate-300"
            data-testid="practice-selection-reason"
          >
            {adaptive.selection_reason}
          </p>
        )}
      </div>
    </section>
  );
}
