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
  question: _question,
  countdown,
  selected,
  wasLate,
}: PracticeAdaptivePanelProps) {
  void _question;
  const [showReason, setShowReason] = useState(false);
  const isCalibrating = adaptive.challenge_band === 'Calibrating';

  const timerColor = countdown > 30
    ? 'bg-slate-100 text-slate-600 dark:bg-slate-800 dark:text-slate-200'
    : countdown > 10
      ? 'bg-amber-50 text-amber-700 dark:bg-amber-500/15 dark:text-amber-200'
      : countdown > 0
        ? 'bg-red-50 text-red-600 dark:bg-red-500/15 dark:text-red-200 animate-pulse'
        : 'bg-red-100 text-red-700 dark:bg-red-500/20 dark:text-red-100';

  const timerDisplay = countdown > 0
    ? `${Math.floor(countdown / 60)}:${String(countdown % 60).padStart(2, '0')}`
    : 'Time!';

  return (
    <section
      className="mb-4 rounded-2xl border border-slate-200/60 bg-slate-50/80 px-4 py-3 dark:border-slate-800 dark:bg-slate-900/60"
      data-testid="practice-adaptive-panel"
    >
      {/* Single compact row: chips + timer */}
      <div className="flex flex-wrap items-center gap-2">
        <span
          className="rounded-full bg-white dark:bg-slate-800 px-2.5 py-0.5 text-xs font-bold text-slate-700 dark:text-slate-300 shadow-sm dark:bg-slate-800 dark:text-slate-300"
          data-testid="practice-skill-chip"
        >
          {getSectionLabel(adaptive.skill_section)} &middot; {adaptive.skill_name}
        </span>
        <span
          className="rounded-full bg-teal-50 px-2.5 py-0.5 text-xs font-bold text-teal-700 dark:bg-teal-500/15 dark:text-teal-200"
          data-testid="practice-level-chip"
        >
          {adaptive.difficulty_label} {adaptive.difficulty_score}/100
        </span>
        <span
          className="rounded-full bg-amber-50 px-2.5 py-0.5 text-xs font-bold text-amber-700 dark:bg-amber-500/15 dark:text-amber-200"
          data-testid="practice-challenge-chip"
        >
          {adaptive.challenge_band}
        </span>

        {!isCalibrating && (
          <span className="text-xs text-slate-400 dark:text-slate-500" data-testid="practice-skill-mastery">
            Mastery: {adaptive.skill_mastery}%
          </span>
        )}
        {isCalibrating && (
          <span className="text-xs text-slate-400 dark:text-slate-500" data-testid="practice-skill-mastery">
            Starting level
          </span>
        )}

        {/* Timer - right aligned */}
        <div className="ml-auto flex items-center gap-2">
          {!selected && (
            <div
              data-testid="practice-timer"
              className={`flex items-center gap-1 rounded-full px-2.5 py-1 text-xs font-bold transition-all ${timerColor}`}
            >
              <svg className="h-3.5 w-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                <path strokeLinecap="round" strokeLinejoin="round" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              <span>{timerDisplay}</span>
            </div>
          )}
          {selected && wasLate && (
            <span className="rounded-full bg-red-50 px-2.5 py-1 text-xs font-bold text-red-600 dark:bg-red-500/15 dark:text-red-200">
              Late
            </span>
          )}

          {/* Why this question? - inline toggle */}
          <button
            type="button"
            className="text-xs text-teal-600 dark:text-teal-300 font-bold hover:text-teal-500 transition-colors"
            aria-expanded={showReason}
            data-testid="practice-selection-reason-toggle"
            onClick={() => setShowReason((value) => !value)}
          >
            {showReason ? 'Hide why' : 'Why?'}
          </button>
        </div>
      </div>

      {/* Expandable reason (collapsed by default) */}
      {showReason && (
        <div className="mt-2 rounded-xl bg-white/80 dark:bg-slate-950/60 border border-slate-200/50 dark:border-slate-800 px-3 py-2 animate-slide-down">
          <p
            className="text-xs leading-relaxed text-slate-600 dark:text-slate-300"
            data-testid="practice-selection-reason"
          >
            {isCalibrating
              ? 'We are using this question to estimate your starting level in this skill.'
              : adaptive.selection_reason}
          </p>
        </div>
      )}
    </section>
  );
}
