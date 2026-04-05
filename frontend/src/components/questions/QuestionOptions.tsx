import { useMemo, useRef } from 'react';

import { RichTextContent } from '@/components/questions/RichTextContent';
import type { QuestionAppearance } from '@/lib/questionPresentation';
import { getQuestionContrastClass, getQuestionDensityClass, getQuestionTextScale } from '@/lib/questionPresentation';
import type { QuestionContentFormat, QuestionOption } from '@/types';

interface QuestionOptionsProps {
  options: QuestionOption[];
  contentFormat?: QuestionContentFormat | null;
  selectedKey?: string | null;
  correctOption?: string | null;
  disabled?: boolean;
  onSelect: (key: string) => void;
  testIdPrefix: string;
  appearance: QuestionAppearance;
  accent?: 'teal' | 'blue' | 'violet';
  maskUnselected?: boolean;
}

const accentClasses: Record<NonNullable<QuestionOptionsProps['accent']>, { selected: string; selectedBadge: string }> = {
  teal: { selected: 'border-teal-400 bg-teal-50 shadow-sm', selectedBadge: 'bg-teal-500 text-white' },
  blue: { selected: 'border-blue-400 bg-blue-50 shadow-sm', selectedBadge: 'bg-blue-500 text-white' },
  violet: { selected: 'border-violet-400 bg-violet-50 shadow-sm', selectedBadge: 'bg-violet-500 text-white' },
};

export function QuestionOptions({
  options,
  contentFormat = 'plain',
  selectedKey = null,
  correctOption = null,
  disabled = false,
  onSelect,
  testIdPrefix,
  appearance,
  accent = 'teal',
  maskUnselected = false,
}: QuestionOptionsProps) {
  const optionRefs = useRef<Array<HTMLButtonElement | null>>([]);
  const accentSet = accentClasses[accent];
  const feedbackVisible = disabled && !!correctOption;
  const optionTextClass = appearance.textSize === 'large'
    ? 'text-lg leading-8 text-slate-800 lg:text-[1.45rem] dark:text-slate-100'
    : 'text-base leading-7 text-slate-800 lg:text-[1.18rem] dark:text-slate-100';
  const optionPaddingClass = appearance.density === 'compact' ? 'p-4 lg:p-5' : 'p-5 lg:p-6';
  const optionBadgeClass = appearance.textSize === 'large'
    ? 'h-12 w-12 rounded-2xl text-xl'
    : 'h-11 w-11 rounded-2xl text-lg';

  const classes = useMemo(
    () => ({
      scale: getQuestionTextScale(appearance.textSize),
      density: getQuestionDensityClass(appearance.density),
      contrast: getQuestionContrastClass(appearance.contrast),
    }),
    [appearance],
  );

  const focusRelativeOption = (index: number, delta: number) => {
    const nextIndex = (index + delta + options.length) % options.length;
    optionRefs.current[nextIndex]?.focus();
  };

  return (
    <div className={`space-y-4 lg:space-y-5 ${classes.scale} ${classes.density} ${classes.contrast}`} role="radiogroup" aria-label="Answer choices">
      {options.map((option, index) => {
        const isSelected = selectedKey === option.key;
        const isCorrect = feedbackVisible && correctOption === option.key;
        const isIncorrectSelection = feedbackVisible && isSelected && !isCorrect;
        const isMuted = feedbackVisible && !isSelected && !isCorrect;
        const masked = maskUnselected && !isSelected && !feedbackVisible;

        let cardClass = 'border-slate-200/90 bg-white/95 hover:border-slate-300 hover:border-l-teal-400 hover:shadow-[0_22px_45px_-34px_rgba(15,23,42,0.3)] hover:-translate-y-1 dark:border-slate-800 dark:bg-slate-950/95 dark:hover:border-slate-700 dark:hover:border-l-teal-400';
        let badgeClass = 'bg-slate-100 text-slate-600 dark:bg-slate-800 dark:text-slate-300';
        let stateLabel = '';

        if (isCorrect) {
          cardClass = 'border-emerald-400 bg-emerald-50 shadow-[0_22px_45px_-34px_rgba(16,185,129,0.28)] dark:bg-emerald-500/12 animate-correct';
          badgeClass = 'bg-emerald-500 text-white';
          stateLabel = 'Correct answer';
        } else if (isIncorrectSelection) {
          cardClass = 'border-red-400 bg-red-50 shadow-[0_22px_45px_-34px_rgba(239,68,68,0.22)] dark:bg-red-500/12 animate-wrong';
          badgeClass = 'bg-red-500 text-white';
          stateLabel = 'Selected answer';
        } else if (isSelected) {
          cardClass = accentSet.selected;
          badgeClass = accentSet.selectedBadge;
          stateLabel = 'Selected';
        } else if (isMuted) {
          cardClass = 'border-slate-100 bg-slate-50 opacity-60 dark:border-slate-800 dark:bg-slate-900';
        } else if (masked) {
          cardClass = 'border-slate-100 bg-slate-50/80 opacity-75 dark:border-slate-800 dark:bg-slate-900/80';
        }

        return (
          <button
            key={option.key}
            ref={(element) => {
              optionRefs.current[index] = element;
            }}
            type="button"
            role="radio"
            aria-checked={isSelected}
            aria-describedby={stateLabel ? `${testIdPrefix}-state-${option.key}` : undefined}
            onClick={() => !disabled && onSelect(option.key)}
            onKeyDown={(event) => {
              if (event.key === 'ArrowDown' || event.key === 'ArrowRight') {
                event.preventDefault();
                focusRelativeOption(index, 1);
              } else if (event.key === 'ArrowUp' || event.key === 'ArrowLeft') {
                event.preventDefault();
                focusRelativeOption(index, -1);
              } else if ((event.key === 'Enter' || event.key === ' ') && !disabled) {
                event.preventDefault();
                onSelect(option.key);
              }
            }}
            disabled={disabled}
            data-testid={`${testIdPrefix}-option-${option.key}`}
            className={`w-full rounded-[2rem] border-2 text-left transition-all duration-200 focus-visible:outline-none focus-visible:ring-4 focus-visible:ring-teal-200 interactive-press ${cardClass}`}
          >
            <div className={`flex items-start gap-4 ${optionPaddingClass}`}>
              <span className={`flex shrink-0 items-center justify-center font-black ${optionBadgeClass} ${badgeClass}`}>
                {option.label}
              </span>
              <div className="min-w-0 flex-1">
                <RichTextContent
                  content={option.text_ar}
                  contentFormat={contentFormat}
                  className={optionTextClass}
                />
                {stateLabel && (
                  <p
                    id={`${testIdPrefix}-state-${option.key}`}
                    className={`mt-3 text-sm font-semibold ${isCorrect ? 'text-emerald-700 dark:text-emerald-300' : isIncorrectSelection ? 'text-red-600 dark:text-red-300' : 'text-slate-500 dark:text-slate-400'}`}
                  >
                    {stateLabel}
                  </p>
                )}
              </div>
            </div>
          </button>
        );
      })}
    </div>
  );
}
