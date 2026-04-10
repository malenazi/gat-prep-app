import { useState, useRef, useEffect } from 'react';
import { HelpCircle } from 'lucide-react';

interface HelpTooltipProps {
  text: string;
  className?: string;
}

export function HelpTooltip({ text, className = '' }: HelpTooltipProps) {
  const [open, setOpen] = useState(false);
  const ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!open) return;
    const handler = (e: MouseEvent) => {
      if (ref.current && !ref.current.contains(e.target as Node)) setOpen(false);
    };
    document.addEventListener('mousedown', handler);
    return () => document.removeEventListener('mousedown', handler);
  }, [open]);

  return (
    <div ref={ref} className={`relative inline-flex ${className}`}>
      <button
        type="button"
        onClick={() => setOpen(!open)}
        className="rounded-full p-1 text-slate-400 hover:text-teal-500 hover:bg-slate-100 dark:text-slate-500 dark:hover:text-teal-400 dark:hover:bg-slate-800 transition"
        aria-label="Help"
      >
        <HelpCircle className="h-4 w-4" />
      </button>
      {open && (
        <div className="absolute bottom-full left-1/2 -translate-x-1/2 mb-2 z-50 w-64 rounded-xl border border-slate-200 bg-white p-3 text-xs text-slate-600 leading-relaxed shadow-lg animate-slide-down dark:border-slate-700 dark:bg-slate-900 dark:text-slate-300">
          {text}
          <div className="absolute top-full left-1/2 -translate-x-1/2 -mt-px">
            <div className="border-4 border-transparent border-t-white dark:border-t-slate-900" />
          </div>
        </div>
      )}
    </div>
  );
}
