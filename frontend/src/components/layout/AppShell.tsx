import { Link, useLocation, Outlet } from 'react-router-dom';
import { useAuth } from '@/hooks/useAuth';
import { Home, PenLine, CalendarDays, BarChart3, Settings, LogOut } from 'lucide-react';

const navItems = [
  { path: '/', label: 'Home', icon: Home },
  { path: '/practice', label: 'Practice', icon: PenLine },
  { path: '/plan', label: 'Plan', icon: CalendarDays },
  { path: '/analytics', label: 'Analytics', icon: BarChart3 },
];

function MiniScoreRing({ score }: { score: number }) {
  const pct = Math.max(0, Math.min(100, score));
  const offset = 283 - (283 * pct / 100);
  return (
    <svg width="40" height="40" viewBox="0 0 100 100" className="shrink-0">
      <circle cx="50" cy="50" r="45" fill="none" stroke="#e2e8f0" strokeWidth="8" />
      <circle cx="50" cy="50" r="45" fill="none" stroke="#00C8A0" strokeWidth="8"
        strokeDasharray="283" strokeDashoffset={offset} strokeLinecap="round"
        transform="rotate(-90 50 50)" className="score-ring-animate" />
      <text x="50" y="55" textAnchor="middle" className="text-[24px] font-black" fill="#0f172a">{pct}</text>
    </svg>
  );
}

function DesktopSidebar() {
  const loc = useLocation();
  const { user, logout } = useAuth();
  if (!user) return null;
  const score = user.predicted_score;

  return (
    <aside className="hidden lg:flex flex-col fixed left-0 top-0 h-screen w-64 bg-white border-r border-slate-200 z-40">
      {/* Logo */}
      <div className="p-6 border-b border-slate-100">
        <div className="flex items-center gap-3">
          <img src="/logo-icon.png" alt="Qudra Academy" className="w-10 h-10" />
          <div>
            <h1 className="font-black text-lg text-slate-800">Qudra Academy</h1>
            <p className="text-sm text-slate-500">Qudra Academy</p>
          </div>
        </div>
      </div>

      {/* Navigation */}
      <nav className="flex-1 p-4 space-y-1">
        {navItems.map(it => {
          const Icon = it.icon;
          return (
            <Link key={it.path} to={it.path}
              className={`flex items-center gap-3 px-4 py-3 rounded-xl text-sm font-medium transition-all
                ${loc.pathname === it.path
                  ? 'bg-teal-50 text-teal-700 shadow-sm'
                  : 'text-slate-500 hover:bg-slate-50 hover:text-slate-700'}`}>
              <Icon className="w-5 h-5" />
              <span>{it.label}</span>
            </Link>
          );
        })}
      </nav>

      {/* Admin Link */}
      {user.is_admin && (
        <div className="px-4 pb-2">
          <Link to="/admin"
            className={`flex items-center gap-3 px-4 py-3 rounded-xl text-sm font-medium transition-all
              ${loc.pathname === '/admin' ? 'bg-amber-50 text-amber-700 shadow-sm' : 'text-slate-500 hover:bg-slate-50 hover:text-slate-700'}`}>
            <Settings className="w-5 h-5" />
            <span>Admin Panel</span>
          </Link>
        </div>
      )}

      {/* Mini Stats */}
      <div className="p-4 border-t border-slate-100 space-y-3">
        <div className="flex items-center gap-3 px-2">
          <MiniScoreRing score={score.mid} />
          <div>
            <p className="text-sm text-slate-500">Predicted Score</p>
            <p className="font-bold text-slate-700">{score.low}–{score.high}</p>
          </div>
        </div>
        <div className="flex items-center justify-between px-2 text-sm">
          <span className="flex items-center gap-1.5 text-slate-500">
            <span className={user.streak > 0 ? 'animate-fire' : ''}>🔥</span> {user.streak} day
          </span>
          <span className="flex items-center gap-1.5 text-slate-500">
            ⚡ {user.xp} XP
          </span>
        </div>

        <button onClick={logout}
          className="flex items-center gap-2 px-4 py-2.5 w-full text-sm text-slate-500 hover:text-red-500 hover:bg-red-50 rounded-xl transition-all">
          <LogOut className="w-5 h-5" />
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
    <header className="hidden lg:flex items-center justify-between px-8 py-4 border-b border-slate-100 bg-white/80 backdrop-blur-sm sticky top-0 z-30">
      <div className="flex items-center gap-4">
        <h2 className="text-lg font-bold text-slate-700">Hello, {user.name}</h2>
        <span className="text-sm text-slate-500">Day {user.current_day} of 30</span>
      </div>
      <div className="flex items-center gap-3">
        <div className="flex items-center gap-2">
          <div className="h-2 w-40 bg-slate-100 rounded-full overflow-hidden">
            <div className="h-full bg-gradient-to-l from-teal-400 to-teal-600 rounded-full transition-all duration-500"
              style={{ width: `${(user.current_day / 30) * 100}%` }} />
          </div>
          <span className="text-sm text-slate-500 font-medium">{Math.round((user.current_day / 30) * 100)}%</span>
        </div>
        <div className="h-5 w-px bg-slate-200" />
        <div className="flex items-center gap-1.5 text-sm text-slate-600">
          <span className={user.streak > 0 ? 'animate-fire' : ''}>🔥</span>
          <span className="font-bold">{user.streak}</span>
        </div>
        <div className="flex items-center gap-1.5 text-sm text-teal-600">
          <span>⚡</span>
          <span className="font-bold">{user.xp}</span>
        </div>
        <div className="w-9 h-9 bg-gradient-to-br from-teal-400 to-teal-600 rounded-full flex items-center justify-center text-white font-bold text-sm shadow-brand">
          {user.name?.charAt(0)}
        </div>
      </div>
    </header>
  );
}

function MobileNav() {
  const loc = useLocation();
  const { user } = useAuth();
  const allItems = user?.is_admin
    ? [...navItems, { path: '/admin', label: 'Admin', icon: Settings }]
    : navItems;
  return (
    <nav className="lg:hidden fixed bottom-0 inset-x-0 glass border-t border-slate-200/50 flex justify-around py-1.5 px-1 z-50 pb-[max(0.375rem,env(safe-area-inset-bottom))]">
      {allItems.map(it => {
        const Icon = it.icon;
        return (
          <Link key={it.path} to={it.path}
            className={`flex flex-col items-center gap-0.5 px-2 py-1 rounded-xl text-xs transition-all
              ${loc.pathname === it.path ? (it.path === '/admin' ? 'text-amber-600' : 'text-teal-600') : 'text-slate-500'}`}>
            <Icon className="w-5 h-5" />
            <span className="font-medium">{it.label}</span>
          </Link>
        );
      })}
    </nav>
  );
}

export default function AppShell() {
  return (
    <div className="min-h-screen flex flex-col lg:flex-row">
      <DesktopSidebar />
      <main className="flex-1 pb-14 lg:pb-0 lg:ml-64">
        <TopBar />
        <div className="page-enter">
          <Outlet />
        </div>
      </main>
      <MobileNav />
    </div>
  );
}
