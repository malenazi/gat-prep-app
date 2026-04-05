import { useState } from 'react';
import { RichTextContent } from '@/components/questions/RichTextContent';
import type { QuestionAppearance } from '@/lib/questionPresentation';
import { getQuestionContrastClass, getQuestionDensityClass, getQuestionTextScale } from '@/lib/questionPresentation';
import type { AnswerFeedback } from '@/types';

interface QuestionFeedbackCardProps {
  feedback: AnswerFeedback;
  selectedOption?: string | null;
  appearance: QuestionAppearance;
  title?: string;
  className?: string;
}

export function QuestionFeedbackCard({
  feedback,
  selectedOption = null,
  appearance,
  title,
  className = '',
}: QuestionFeedbackCardProps) {
  const stateTone = feedback.is_correct
    ? {
        panel: 'border-emerald-200 bg-emerald-50 dark:border-emerald-700 dark:bg-emerald-500/18',
        heading: 'text-emerald-700 dark:text-emerald-200',
        label: title || 'Correct answer',
        icon: 'Correct',
      }
    : {
        panel: 'border-amber-300 bg-amber-50 dark:border-amber-700 dark:bg-amber-500/18',
        heading: 'text-amber-700 dark:text-amber-200',
        label: title || 'Review this one',
        icon: 'Review',
      };

  return (
    <div
      className={`rounded-3xl border p-5 lg:p-6 ${stateTone.panel} ${getQuestionTextScale(appearance.textSize)} ${getQuestionDensityClass(appearance.density)} ${getQuestionContrastClass(appearance.contrast)} ${className}`}
    >
      <div className="mb-4 flex items-center gap-3">
        <span className={`rounded-full px-3 py-1 text-xs font-black uppercase tracking-[0.18em] ${stateTone.heading}`}>
          {stateTone.icon}
        </span>
        <h3 className={`text-base font-black lg:text-lg ${stateTone.heading}`}>{stateTone.label}</h3>
      </div>

      <div className="grid gap-3 lg:grid-cols-2">
        <div className="rounded-2xl border border-white/70 bg-white/75 p-4 dark:border-slate-800 dark:bg-slate-950/70">
          <p className="text-xs font-bold uppercase tracking-[0.16em] text-slate-400 dark:text-slate-500">Result</p>
          <p className="mt-2 text-sm font-semibold text-slate-700 dark:text-slate-200">
            {feedback.is_correct ? 'You chose the correct option.' : 'Your first answer needs a second look.'}
          </p>
          <p className="mt-2 text-sm text-slate-500 dark:text-slate-400">
            {selectedOption ? `Your answer: ${selectedOption.toUpperCase()}` : 'No answer recorded.'}
          </p>
          <p className="text-sm font-semibold text-slate-700 dark:text-slate-200">
            Correct answer: {feedback.correct_option.toUpperCase()}
          </p>
        </div>

        <div className="rounded-2xl border border-white/70 bg-white/75 p-4 dark:border-slate-800 dark:bg-slate-950/70">
          <p className="text-xs font-bold uppercase tracking-[0.16em] text-slate-400 dark:text-slate-500">Short Explanation</p>
          <RichTextContent
            content={feedback.explanation_ar || 'No explanation available yet.'}
            contentFormat={feedback.content_format}
            className="mt-2 text-sm leading-relaxed text-slate-700 dark:text-slate-200"
          />
        </div>
      </div>

      <CollapsibleSection
        title={feedback.is_correct ? 'Worked Steps' : 'Worked Steps And Common Trap'}
        defaultOpen={feedback.is_correct}
      >
        {!feedback.is_correct && (
          <p className="mb-2 text-sm text-slate-500 dark:text-slate-400">
            Compare each step below with the choice you selected to spot where the reasoning changed.
          </p>
        )}
        {feedback.solution_steps_ar?.length ? (
          <ol className="space-y-2">
            {feedback.solution_steps_ar.map((step, index) => (
              <li key={`${index}-${step.slice(0, 20)}`} className="flex gap-3">
                <span className="mt-0.5 flex h-6 w-6 shrink-0 items-center justify-center rounded-full bg-slate-100 text-xs font-black text-slate-600 dark:bg-slate-800 dark:text-slate-300">
                  {index + 1}
                </span>
                <RichTextContent
                  content={step}
                  contentFormat={feedback.content_format}
                  className="text-sm leading-relaxed text-slate-700 dark:text-slate-200"
                />
              </li>
            ))}
          </ol>
        ) : (
          <p className="text-sm text-slate-500 dark:text-slate-400">Detailed steps are not available for this item yet.</p>
        )}
      </CollapsibleSection>
    </div>
  );
}

function CollapsibleSection({ title, defaultOpen = true, children }: { title: string; defaultOpen?: boolean; children: React.ReactNode }) {
  const [open, setOpen] = useState(defaultOpen);
  return (
    <div className="mt-3 rounded-2xl border border-white/70 bg-white/75 dark:border-slate-800 dark:bg-slate-950/70 overflow-hidden">
      <button type="button" onClick={() => setOpen(v => !v)} className="w-full flex items-center justify-between p-4 text-left">
        <p className="text-xs font-bold uppercase tracking-[0.16em] text-slate-400 dark:text-slate-500">{title}</p>
        <svg className={`h-4 w-4 text-slate-400 transition-transform ${open ? 'rotate-180' : ''}`} fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
          <path strokeLinecap="round" strokeLinejoin="round" d="M19 9l-7 7-7-7" />
        </svg>
      </button>
      {open && <div className="px-4 pb-4">{children}</div>}
    </div>
  );
}
