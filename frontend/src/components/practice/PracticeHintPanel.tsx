import { RichTextContent } from '@/components/questions/RichTextContent';
import type { QuestionContentFormat, PracticeAssistment } from '@/types';

interface PracticeHintPanelProps {
  assistment: PracticeAssistment;
  contentFormat?: QuestionContentFormat | null;
  revealedCount: number;
  disabled?: boolean;
  onReveal: () => void;
}

export function PracticeHintPanel({
  assistment,
  contentFormat,
  revealedCount,
  disabled = false,
  onReveal,
}: PracticeHintPanelProps) {
  if (!assistment.hints_available || assistment.hints.length === 0) {
    return null;
  }

  const nextHint = assistment.hints[revealedCount];

  return (
    <section
      className="mb-5 rounded-3xl border border-indigo-100 bg-indigo-50/60 p-5 shadow-card dark:border-indigo-900/60 dark:bg-indigo-500/10"
      data-testid="practice-hint-panel"
    >
      <div className="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
        <div>
          <h3 className="text-base font-black text-slate-900 dark:text-slate-50">Need a hint?</h3>
          <p className="mt-1 text-sm text-slate-600 dark:text-slate-300">
            Reveal guided support one step at a time before you answer.
          </p>
        </div>
        {nextHint && !disabled && (
          <button
            type="button"
            className="rounded-full bg-indigo-600 px-4 py-2 text-sm font-bold text-white transition hover:bg-indigo-700 disabled:cursor-not-allowed disabled:opacity-60"
            data-testid="practice-hint-reveal"
            onClick={onReveal}
          >
            Reveal {nextHint.title}
          </button>
        )}
      </div>

      {revealedCount > 0 && (
        <div className="mt-4 space-y-3">
          {assistment.hints.slice(0, revealedCount).map((hint) => (
            <div
              key={hint.index}
              className="rounded-2xl border border-white/70 bg-white/80 p-4 dark:border-slate-800 dark:bg-slate-950/70"
              data-testid={`practice-hint-${hint.index}`}
            >
              <p className="text-xs font-black uppercase tracking-[0.16em] text-indigo-600 dark:text-indigo-300">
                {hint.title}
              </p>
              <RichTextContent
                content={hint.text_ar}
                contentFormat={contentFormat}
                className="mt-2 text-sm leading-relaxed text-slate-700 dark:text-slate-200"
              />
            </div>
          ))}
        </div>
      )}
    </section>
  );
}
