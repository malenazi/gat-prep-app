import { Link, Outlet, useLocation } from 'react-router-dom';
import { BarChart3, CalendarDays, Home, LogOut, PenLine, Settings } from 'lucide-react';

import { useAuth } from '@/hooks/useAuth';
import { LogoMark } from '@/brand/Logo';

const navItems = [
  { path: '/', label: 'Home', icon: Home },
  { path: '/practice', label: 'Practice', icon: PenLine },
  { path: '/plan', label: 'Plan', icon: CalendarDays },
  { path: '/analytics', label: 'Analytics', icon: BarChart3 },
];

function navTestId(path: string) {
  if (path === '/') return 'nav-home';
  return `nav-${path.replace('/', '')}`;
}

function MiniScoreRing({ score }: { score: number }) {
  const pct = Math.max(0, Math.min(100, score));
  const offset = 283 - (283 * pct) / 100;

  return (
    <svg width="40" height="40" viewBox="0 0 100 100" className="shrink-0 text-slate-900 dark:text-slate-100">
      <circle cx="50" cy="50" r="45" fill="none" className="stroke-slate-200 dark:stroke-slate-700" strokeWidth="8" />
      <circle
        cx="50"
        cy="50"
        r="45"
        fill="none"
        stroke="#00C8A0"
        strokeWidth="8"
        strokeDasharray="283"
        strokeDashoffset={offset}
        strokeLinecap="round"
        transform="rotate(-90 50 50)"
        className="score-ring-animate"
      />
      <text x="50" y="55" textAnchor="middle" className="text-[24px] font-black" fill="currentColor">
        {pct}
      </text>
    </svg>
  );
}

function DesktopSidebar() {
  const loc = useLocation();
  const { user, logout } = useAuth();

  if (!user) return null;

  const score = user.predicted_score;

  return (
    <aside
      className="fixed left-0 top-0 z-40 hidden h-screen w-64 flex-col border-r border-slate-200 bg-white lg:flex dark:border-slate-800 dark:bg-slate-950"
      data-testid="app-sidebar"
    >
      <div className="border-b border-slate-100 p-6 dark:border-slate-800">
        <div className="flex items-center gap-3">
          <LogoMark size={40} />
          <div>
            <h1 className="text-lg font-black text-slate-800 dark:text-slate-100">Qudra Academy</h1>
            <p className="text-sm text-slate-500 dark:text-slate-400">Guided GAT prep</p>
          </div>
        </div>
      </div>

      <nav className="flex-1 space-y-1 p-4">
        {navItems.map((item) => {
          const Icon = item.icon;
          const active = loc.pathname === item.path;
          return (
            <Link
              key={item.path}
              to={item.path}
              data-testid={navTestId(item.path)}
              className={`interactive-press flex items-center gap-3 rounded-xl px-4 py-3 text-sm font-medium transition-all ${
                active
                  ? 'bg-teal-50 text-teal-700 shadow-sm dark:bg-teal-500/15 dark:text-teal-300'
                  : 'text-slate-500 hover:bg-slate-50 hover:text-slate-700 dark:text-slate-400 dark:hover:bg-slate-900 dark:hover:text-slate-100'
              }`}
            >
              <Icon className="h-5 w-5" />
              <span>{item.label}</span>
            </Link>
          );
        })}
      </nav>

      {user.is_admin && (
        <div className="px-4 pb-2">
          <Link
            to="/admin"
            data-testid="nav-admin"
            className={`interactive-press flex items-center gap-3 rounded-xl px-4 py-3 text-sm font-medium transition-all ${
              loc.pathname === '/admin'
                ? 'bg-amber-50 text-amber-700 shadow-sm dark:bg-amber-500/15 dark:text-amber-300'
                : 'text-slate-500 hover:bg-slate-50 hover:text-slate-700 dark:text-slate-400 dark:hover:bg-slate-900 dark:hover:text-slate-100'
            }`}
          >
            <Settings className="h-5 w-5" />
            <span>Admin Panel</span>
          </Link>
        </div>
      )}

      <div className="space-y-3 border-t border-slate-100 p-4 dark:border-slate-800">
        <div className="flex items-center gap-3 px-2">
          <MiniScoreRing score={score.mid} />
          <div>
            <p className="text-sm text-slate-500 dark:text-slate-400">Predicted Score</p>
            <p className="font-bold text-slate-700 dark:text-slate-200">
              {score.low}-{score.high}
            </p>
          </div>
        </div>
        <div className="flex items-center justify-between px-2 text-sm">
          <span className="flex items-center gap-1.5 text-slate-500 dark:text-slate-400">
            <span className={user.streak > 0 ? 'animate-fire' : ''}>*</span>
            {user.streak} day
          </span>
          <span className="flex items-center gap-1.5 text-slate-500 dark:text-slate-400">XP {user.xp}</span>
        </div>

        <button
          onClick={logout}
          data-testid="logout-desktop"
          className="flex w-full items-center gap-2 rounded-xl px-4 py-2.5 text-sm text-slate-500 transition-all hover:bg-red-50 hover:text-red-500 dark:text-slate-400 dark:hover:bg-red-500/10"
        >
          <LogOut className="h-5 w-5" />
          <span>Logout</span>
        </button>
      </div>
    </aside>
  );
}

function TopBar() {
  const { user } = useAuth();
  if (!user) return null;

  return (
    <header
      className="sticky top-0 z-30 hidden items-center justify-between border-b border-slate-100 bg-white/80 px-6 py-4 pr-20 backdrop-blur-sm xl:px-8 xl:pr-24 lg:flex dark:border-slate-800 dark:bg-slate-950/80"
      data-testid="app-topbar"
    >
      <div className="flex items-center gap-4">
        <h2 className="text-lg font-bold text-slate-700 dark:text-slate-100" data-testid="topbar-greeting">
          Hello, {user.name}
        </h2>
        <span className="text-sm text-slate-500 dark:text-slate-400" data-testid="topbar-day">
          Day {user.current_day} of 30
        </span>
      </div>
      <div className="flex items-center gap-4">
        {/* Performance indicators */}
        <div className="flex items-center gap-3">
          {/* Accuracy */}
          {(() => {
            const totalQ = user.abilities?.reduce((s: number, a: { questions_seen: number }) => s + a.questions_seen, 0) || 0;
            const totalC = user.abilities?.reduce((s: number, a: { correct_count: number }) => s + a.correct_count, 0) || 0;
            const acc = totalQ > 0 ? Math.round((totalC / totalQ) * 100) : 0;
            return totalQ > 0 ? (
              <div className="flex items-center gap-1.5 rounded-full bg-emerald-50 dark:bg-emerald-900/30 px-2.5 py-1">
                <span className="text-xs">🎯</span>
                <span className="text-xs font-bold text-emerald-600 dark:text-emerald-400">{acc}%</span>
              </div>
            ) : null;
          })()}
          {/* Streak */}
          <div className={`flex items-center gap-1 rounded-full px-2.5 py-1 ${user.streak > 0 ? 'bg-amber-50 dark:bg-amber-900/30' : 'bg-slate-50 dark:bg-slate-800'}`}>
            <span className={`text-xs ${user.streak > 0 ? 'animate-fire' : ''}`}>🔥</span>
            <span className={`text-xs font-bold ${user.streak > 0 ? 'text-amber-600 dark:text-amber-400' : 'text-slate-400 dark:text-slate-500'}`}>{user.streak}</span>
          </div>
          {/* XP */}
          <div className="flex items-center gap-1 rounded-full bg-teal-50 dark:bg-teal-900/30 px-2.5 py-1">
            <span className="text-xs">⚡</span>
            <span className="text-xs font-bold text-teal-600 dark:text-teal-400">{user.xp}</span>
          </div>
        </div>

        <div className="h-5 w-px bg-slate-200 dark:bg-slate-700" />

        {/* Course progress */}
        <div className="flex flex-col items-end gap-0.5">
          <div className="flex items-center gap-2">
            <div className="h-1.5 w-32 overflow-hidden rounded-full bg-slate-100 dark:bg-slate-800">
              <div
                className="h-full rounded-full bg-gradient-to-l from-teal-400 to-teal-600 transition-all duration-500"
                style={{ width: `${Math.round((user.current_day / 30) * 100)}%` }}
              />
            </div>
            <span className="text-xs font-bold text-teal-600 dark:text-teal-400">
              {Math.round((user.current_day / 30) * 100)}%
            </span>
          </div>
          <span className="text-[10px] text-slate-400 dark:text-slate-500">
            Day {user.current_day}/30 · {user.abilities?.reduce((s: number, a: { questions_seen: number }) => s + a.questions_seen, 0) || 0} Qs
          </span>
        </div>

        <div className="flex h-9 w-9 items-center justify-center rounded-full bg-gradient-to-br from-teal-400 to-teal-600 text-sm font-bold text-white shadow-brand">
          {user.name?.charAt(0)}
        </div>
      </div>
    </header>
  );
}

function MobileNav() {
  const loc = useLocation();
  const { user } = useAuth();
  const items = user?.is_admin ? [...navItems, { path: '/admin', label: 'Admin', icon: Settings }] : navItems;

  return (
    <nav
      className="glass fixed inset-x-0 bottom-0 z-50 flex justify-around border-t border-slate-200/50 px-1 py-1.5 pb-[max(0.375rem,env(safe-area-inset-bottom))] lg:hidden dark:border-slate-800/80"
      data-testid="mobile-nav"
    >
      {items.map((item) => {
        const Icon = item.icon;
        const active = loc.pathname === item.path;
        return (
          <Link
            key={item.path}
            to={item.path}
            data-testid={`mobile-${navTestId(item.path)}`}
            className={`interactive-press flex flex-col items-center gap-0.5 rounded-xl px-2 py-1 text-xs transition-all ${
              active
                ? item.path === '/admin'
                  ? 'text-amber-600 dark:text-amber-300'
                  : 'text-teal-600 dark:text-teal-300'
                : 'text-slate-500 dark:text-slate-400'
            }`}
          >
            <Icon className="h-5 w-5" />
            <span className="font-medium">{item.label}</span>
          </Link>
        );
      })}
    </nav>
  );
}

export default function AppShell() {
  return (
    <div className="min-h-screen flex-col text-slate-800 dark:text-slate-100 lg:flex lg:flex-row">
      <DesktopSidebar />
      <main className="min-w-0 flex-1 overflow-x-clip pb-14 lg:ml-64 lg:pb-0" data-testid="app-main">
        <TopBar />
        <div className="page-enter">
          <Outlet />
        </div>
      </main>
      <MobileNav />
    </div>
  );
}
