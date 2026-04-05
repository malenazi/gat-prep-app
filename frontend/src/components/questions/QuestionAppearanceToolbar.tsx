import type { QuestionAppearance } from '@/lib/questionPresentation';

interface QuestionAppearanceToolbarProps {
  appearance: QuestionAppearance;
  onChange: (next: QuestionAppearance) => void;
  showAnswerMasking?: boolean;
  className?: string;
}

function ToggleButton({
  active,
  label,
  onClick,
}: {
  active: boolean;
  label: string;
  onClick: () => void;
}) {
  return (
    <button
      type="button"
      onClick={onClick}
      className={`rounded-full border px-4 py-2 text-sm font-semibold transition ${
        active
          ? 'border-teal-500 bg-gradient-to-r from-teal-500 to-teal-600 text-white shadow-brand'
          : 'border-slate-200 bg-white text-slate-600 hover:border-slate-300 hover:bg-slate-50'
      }`}
    >
      {label}
    </button>
  );
}

export function QuestionAppearanceToolbar({
  appearance,
  onChange,
  showAnswerMasking = false,
  className = '',
}: QuestionAppearanceToolbarProps) {
  return (
    <div className={`rounded-[2rem] border border-slate-200/80 bg-white/90 px-4 py-4 shadow-[0_20px_50px_-36px_rgba(15,23,42,0.28)] backdrop-blur ${className}`}>
      <div className="flex flex-wrap items-start justify-between gap-4">
        <div className="min-w-[10rem]">
          <p className="text-[11px] font-black uppercase tracking-[0.22em] text-slate-400">Reading View</p>
          <p className="mt-1 text-sm text-slate-500">Adjust text size, spacing, and contrast for easier reading.</p>
        </div>

        <div className="flex flex-1 flex-wrap gap-3">
          <div className="rounded-[1.5rem] border border-slate-200 dark:border-slate-700 bg-slate-50/80 dark:bg-slate-800/80 p-2">
            <p className="px-2 pb-2 text-[11px] font-black uppercase tracking-[0.16em] text-slate-400">Text Size</p>
            <div className="flex flex-wrap gap-2">
              <ToggleButton
                active={appearance.textSize === 'normal'}
                label="Standard"
                onClick={() => onChange({ ...appearance, textSize: 'normal' })}
              />
              <ToggleButton
                active={appearance.textSize === 'large'}
                label="Large"
                onClick={() => onChange({ ...appearance, textSize: 'large' })}
              />
            </div>
          </div>

          <div className="rounded-[1.5rem] border border-slate-200 dark:border-slate-700 bg-slate-50/80 dark:bg-slate-800/80 p-2">
            <p className="px-2 pb-2 text-[11px] font-black uppercase tracking-[0.16em] text-slate-400">Spacing</p>
            <div className="flex flex-wrap gap-2">
              <ToggleButton
                active={appearance.density === 'comfortable'}
                label="Comfortable"
                onClick={() => onChange({ ...appearance, density: 'comfortable' })}
              />
              <ToggleButton
                active={appearance.density === 'compact'}
                label="Compact"
                onClick={() => onChange({ ...appearance, density: 'compact' })}
              />
            </div>
          </div>

          <div className="rounded-[1.5rem] border border-slate-200 dark:border-slate-700 bg-slate-50/80 dark:bg-slate-800/80 p-2">
            <p className="px-2 pb-2 text-[11px] font-black uppercase tracking-[0.16em] text-slate-400">Accessibility</p>
            <div className="flex flex-wrap gap-2">
              <ToggleButton
                active={appearance.contrast === 'high'}
                label="High Contrast"
                onClick={() =>
                  onChange({
                    ...appearance,
                    contrast: appearance.contrast === 'high' ? 'default' : 'high',
                  })
                }
              />
              {showAnswerMasking && (
                <ToggleButton
                  active={appearance.answerMasking}
                  label="Answer Masking"
                  onClick={() => onChange({ ...appearance, answerMasking: !appearance.answerMasking })}
                />
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
