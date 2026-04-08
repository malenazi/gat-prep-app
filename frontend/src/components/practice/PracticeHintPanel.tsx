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
      className="mb-4 rounded-2xl border border-indigo-100/80 bg-indigo-50/40 px-4 py-2.5 dark:border-indigo-900/40 dark:bg-indigo-500/8"
      data-testid="practice-hint-panel"
    >
      {/* Compact single-row layout */}
      <div className="flex items-center justify-between gap-3">
        <div className="flex items-center gap-2 min-w-0">
          <span className="text-indigo-500 text-sm">💡</span>
          <span className="text-sm font-bold text-slate-700 dark:text-slate-200">
            {revealedCount > 0 ? `${revealedCount} hint${revealedCount > 1 ? 's' : ''} revealed` : 'Hints available'}
          </span>
        </div>
        {nextHint && !disabled && (
          <button
            type="button"
            className="shrink-0 rounded-full bg-indigo-600 px-3 py-1.5 text-xs font-bold text-white transition hover:bg-indigo-700"
            data-testid="practice-hint-reveal"
            onClick={onReveal}
          >
            Reveal: {nextHint.title}
          </button>
        )}
      </div>

      {revealedCount > 0 && (
        <div className="mt-2 space-y-2">
          {assistment.hints.slice(0, revealedCount).map((hint) => (
            <div
              key={hint.index}
              className="rounded-xl border border-white/70 bg-white/80 px-3 py-2.5 dark:border-slate-800 dark:bg-slate-950/70"
              data-testid={`practice-hint-${hint.index}`}
            >
              <p className="text-xs font-black uppercase tracking-[0.14em] text-indigo-600 dark:text-indigo-200 mb-1">
                {hint.title}
              </p>
              <RichTextContent
                content={hint.text_ar}
                contentFormat={contentFormat}
                className="text-sm leading-relaxed text-slate-700 dark:text-slate-200"
              />
            </div>
          ))}
        </div>
      )}
    </section>
  );
}
