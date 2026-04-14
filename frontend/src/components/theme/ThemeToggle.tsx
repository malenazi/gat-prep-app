import { useEffect, useState } from 'react';
import { Moon, Sun } from 'lucide-react';
import { useTheme } from 'next-themes';

export function ThemeToggle() {
  const { resolvedTheme, setTheme } = useTheme();
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    setMounted(true);
  }, []);

  const activeTheme = mounted ? resolvedTheme : 'light';
  const isDark = activeTheme === 'dark';

  return (
    <div
      className="fixed bottom-[calc(env(safe-area-inset-bottom)+5rem)] right-4 z-[80] lg:bottom-4 lg:right-5 lg:top-auto"
      data-testid="theme-toggle"
    >
      <button
        type="button"
        title={isDark ? 'Switch to light theme' : 'Switch to dark theme'}
        aria-label={isDark ? 'Switch to light theme' : 'Switch to dark theme'}
        aria-pressed={isDark}
        data-testid="theme-toggle-button"
        onClick={() => setTheme(isDark ? 'light' : 'dark')}
        className="flex h-11 w-11 items-center justify-center rounded-full border border-slate-200/80 bg-white/88 text-slate-700 shadow-[0_18px_45px_-30px_rgba(15,23,42,0.32)] backdrop-blur transition hover:scale-[1.03] hover:bg-white dark:border-slate-700/80 dark:bg-slate-950/88 dark:text-teal-200 dark:hover:bg-slate-900"
      >
        {isDark ? <Sun className="h-5 w-5" /> : <Moon className="h-5 w-5" />}
      </button>
    </div>
  );
}
