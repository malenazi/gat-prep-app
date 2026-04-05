import { useId } from 'react';

interface ScoreRingProps {
  score: number;
  size?: number;
  strokeWidth?: number;
  label?: string;
}

export function ScoreRing({ score, size = 160, strokeWidth = 10, label }: ScoreRingProps) {
  const id = useId();
  const gradId = `scoreGrad${id}`;
  const pct = Math.max(0, Math.min(100, score));
  const r = (size - strokeWidth * 2) / 2;
  const circumference = 2 * Math.PI * r;
  const offset = circumference - (circumference * pct / 100);
  return (
    <div className="relative inline-flex items-center justify-center">
      <svg width={size} height={size} viewBox={`0 0 ${size} ${size}`}>
        <circle cx={size / 2} cy={size / 2} r={r} fill="none" stroke="currentColor" className="text-slate-200 dark:text-slate-700" strokeWidth={strokeWidth} />
        <circle cx={size / 2} cy={size / 2} r={r} fill="none" stroke={`url(#${gradId})`} strokeWidth={strokeWidth}
          strokeDasharray={circumference} strokeDashoffset={offset} strokeLinecap="round"
          transform={`rotate(-90 ${size / 2} ${size / 2})`} className="score-ring-animate" />
        <defs>
          <linearGradient id={gradId} x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stopColor="#00C8A0" />
            <stop offset="100%" stopColor="#00A888" />
          </linearGradient>
        </defs>
      </svg>
      <div className="absolute flex flex-col items-center">
        <span className="text-4xl lg:text-5xl font-black text-slate-800 dark:text-slate-100">{pct}</span>
        {label && <span className="text-sm text-slate-500 dark:text-slate-400 mt-0.5">{label === 'of' ? 'of' : label}</span>}
      </div>
    </div>
  );
}
