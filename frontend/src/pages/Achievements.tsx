import { useState, useEffect } from 'react';
import { useAuth } from '@/hooks/useAuth';
import { api } from '@/lib/api';
import { pageShell, pageStack } from '@/lib/layout';
import type { ApiBadge, LeagueTier } from '@/types';

const LEAGUE_CONFIG: { key: LeagueTier; label: string; icon: string; xp: number; color: string }[] = [
  { key: 'bronze', label: 'Bronze', icon: '🥉', xp: 0, color: 'from-amber-600 to-amber-700' },
  { key: 'silver', label: 'Silver', icon: '🥈', xp: 500, color: 'from-slate-400 to-slate-500' },
  { key: 'gold', label: 'Gold', icon: '🥇', xp: 1000, color: 'from-yellow-400 to-yellow-600' },
  { key: 'platinum', label: 'Platinum', icon: '💎', xp: 2000, color: 'from-cyan-400 to-cyan-600' },
  { key: 'diamond', label: 'Diamond', icon: '👑', xp: 3000, color: 'from-violet-400 to-violet-600' },
  { key: 'champion', label: 'Champion', icon: '🏆', xp: 5000, color: 'from-amber-400 to-red-500' },
];

export default function Achievements() {
  const { user } = useAuth();
  const [badges, setBadges] = useState<ApiBadge[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    api.badges().then(b => { setBadges(b); setLoading(false); }).catch(() => setLoading(false));
  }, []);

  if (!user) return null;

  const earnedBadges = badges.filter(b => b.earned);
  const lockedBadges = badges.filter(b => !b.earned);
  const currentLeagueIndex = LEAGUE_CONFIG.findIndex(l => l.key === user.league);
  const currentLeague = LEAGUE_CONFIG[currentLeagueIndex] || LEAGUE_CONFIG[0];
  const nextLeague = LEAGUE_CONFIG[currentLeagueIndex + 1];
  const xpToNext = nextLeague ? nextLeague.xp - user.xp : 0;
  const leaguePct = nextLeague
    ? Math.min(100, Math.round(((user.xp - currentLeague.xp) / (nextLeague.xp - currentLeague.xp)) * 100))
    : 100;

  const totalAnswered = user.abilities?.reduce((s, a) => s + a.questions_seen, 0) || 0;
  const totalCorrect = user.abilities?.reduce((s, a) => s + a.correct_count, 0) || 0;
  const accuracy = totalAnswered > 0 ? Math.round((totalCorrect / totalAnswered) * 100) : 0;

  return (
    <div className={`${pageShell.standard} ${pageStack} page-enter`} data-testid="achievements-page">
      <h1 className="text-2xl font-black text-slate-800 dark:text-slate-100">Achievements</h1>

      {/* ═══ League Progress ═══ */}
      <div className="bg-white dark:bg-slate-900 shadow-card rounded-2xl p-5 lg:p-6">
        <h2 className="text-sm font-bold uppercase tracking-wider text-slate-400 dark:text-slate-500 mb-4">League Rank</h2>

        {/* Current League */}
        <div className="flex items-center gap-4 mb-5">
          <div className={`flex h-16 w-16 items-center justify-center rounded-2xl bg-gradient-to-br ${currentLeague.color} text-3xl shadow-lg`}>
            {currentLeague.icon}
          </div>
          <div>
            <p className="text-xl font-black text-slate-800 dark:text-slate-100">{currentLeague.label}</p>
            <p className="text-sm text-slate-500 dark:text-slate-400">{user.xp.toLocaleString()} XP total</p>
          </div>
        </div>

        {/* Progress to Next */}
        {nextLeague ? (
          <div className="mb-4">
            <div className="flex items-center justify-between mb-1.5">
              <span className="text-xs font-bold text-slate-500 dark:text-slate-400">
                Next: {nextLeague.icon} {nextLeague.label}
              </span>
              <span className="text-xs font-black text-teal-600 dark:text-teal-400">{xpToNext} XP to go</span>
            </div>
            <div className="h-3 rounded-full overflow-hidden bg-slate-100 dark:bg-slate-800">
              <div
                className={`h-full rounded-full bg-gradient-to-r ${currentLeague.color} transition-all duration-700`}
                style={{ width: `${leaguePct}%` }}
              />
            </div>
          </div>
        ) : (
          <p className="text-sm font-bold text-amber-600 dark:text-amber-400">You reached the highest rank!</p>
        )}

        {/* All Tiers */}
        <div className="flex gap-2 mt-4">
          {LEAGUE_CONFIG.map((tier, i) => {
            const reached = i <= currentLeagueIndex;
            return (
              <div key={tier.key} className={`flex-1 text-center rounded-xl py-2 ${reached ? 'bg-slate-100 dark:bg-slate-800' : 'bg-slate-50 dark:bg-slate-800/50 opacity-50'}`}>
                <div className="text-lg">{tier.icon}</div>
                <p className={`text-[10px] font-bold ${reached ? 'text-slate-700 dark:text-slate-200' : 'text-slate-400 dark:text-slate-500'}`}>{tier.label}</p>
                <p className="text-[9px] text-slate-400 dark:text-slate-500">{tier.xp}+</p>
              </div>
            );
          })}
        </div>
      </div>

      {/* ═══ Stats Overview ═══ */}
      <div className="grid grid-cols-2 lg:grid-cols-4 gap-3">
        <StatCard icon="📝" label="Questions" value={totalAnswered.toLocaleString()} />
        <StatCard icon="✅" label="Correct" value={totalCorrect.toLocaleString()} />
        <StatCard icon="🎯" label="Accuracy" value={`${accuracy}%`} />
        <StatCard icon="🔥" label="Best Streak" value={`${user.streak_longest} days`} />
      </div>

      {/* ═══ Streak Info ═══ */}
      <div className="bg-white dark:bg-slate-900 shadow-card rounded-2xl p-5">
        <h2 className="text-sm font-bold uppercase tracking-wider text-slate-400 dark:text-slate-500 mb-4">Streak</h2>
        <div className="flex items-center gap-6">
          <div className="text-center">
            <div className={`text-3xl font-black text-amber-500 ${user.streak > 0 ? 'animate-fire' : ''}`}>
              🔥 {user.streak}
            </div>
            <p className="text-xs text-slate-500 dark:text-slate-400 mt-1">Current</p>
          </div>
          <div className="h-12 w-px bg-slate-200 dark:bg-slate-700" />
          <div className="text-center">
            <div className="text-3xl font-black text-slate-700 dark:text-slate-200">
              {user.streak_longest}
            </div>
            <p className="text-xs text-slate-500 dark:text-slate-400 mt-1">Longest</p>
          </div>
          <div className="h-12 w-px bg-slate-200 dark:bg-slate-700" />
          <div className="text-center">
            <div className="text-3xl font-black text-blue-500">
              🛡️ {user.streak_freezes ?? 0}
            </div>
            <p className="text-xs text-slate-500 dark:text-slate-400 mt-1">Freezes Left</p>
          </div>
        </div>
        <p className="mt-3 text-xs text-slate-400 dark:text-slate-500">
          Practice every day to build your streak. Freezes protect your streak if you miss a day.
        </p>
      </div>

      {/* ═══ Badges ═══ */}
      <div className="bg-white dark:bg-slate-900 shadow-card rounded-2xl p-5">
        <h2 className="text-sm font-bold uppercase tracking-wider text-slate-400 dark:text-slate-500 mb-4">
          Badges <span className="text-teal-600 dark:text-teal-400">{earnedBadges.length}/{badges.length}</span>
        </h2>

        {loading ? (
          <div className="text-center py-8 text-slate-400">Loading badges...</div>
        ) : (
          <>
            {/* Earned */}
            {earnedBadges.length > 0 && (
              <div className="mb-5">
                <p className="text-xs font-bold text-emerald-600 dark:text-emerald-400 mb-3">Earned</p>
                <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-3">
                  {earnedBadges.map(b => (
                    <div key={b.id} className="rounded-xl border border-emerald-200 bg-emerald-50 dark:border-emerald-800 dark:bg-emerald-900/20 p-3 text-center">
                      <div className="text-3xl mb-1">{b.icon}</div>
                      <p className="text-sm font-bold text-slate-800 dark:text-slate-100">{b.name_ar}</p>
                      <p className="text-[11px] text-slate-500 dark:text-slate-400 mt-0.5">{b.description_ar}</p>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* Locked */}
            {lockedBadges.length > 0 && (
              <div>
                <p className="text-xs font-bold text-slate-400 dark:text-slate-500 mb-3">Locked</p>
                <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-3">
                  {lockedBadges.map(b => (
                    <div key={b.id} className="rounded-xl border border-slate-200 bg-slate-50 dark:border-slate-700 dark:bg-slate-800/50 p-3 text-center opacity-60">
                      <div className="text-3xl mb-1 grayscale">{b.icon}</div>
                      <p className="text-sm font-bold text-slate-500 dark:text-slate-400">{b.name_ar}</p>
                      <p className="text-[11px] text-slate-400 dark:text-slate-500 mt-0.5">{b.description_ar}</p>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </>
        )}
      </div>

      {/* ═══ How It Works ═══ */}
      <div className="bg-white dark:bg-slate-900 shadow-card rounded-2xl p-5">
        <h2 className="text-sm font-bold uppercase tracking-wider text-slate-400 dark:text-slate-500 mb-4">How It Works</h2>
        <div className="grid gap-3 text-sm text-slate-600 dark:text-slate-300">
          <div className="flex items-start gap-3">
            <span className="text-lg">⚡</span>
            <div><span className="font-bold">XP:</span> Earn 10 XP per correct answer, 5 XP per attempt. Streaks of 3+ give double XP.</div>
          </div>
          <div className="flex items-start gap-3">
            <span className="text-lg">🏅</span>
            <div><span className="font-bold">Leagues:</span> Advance through Bronze, Silver, Gold, Platinum, Diamond, and Champion as you earn XP.</div>
          </div>
          <div className="flex items-start gap-3">
            <span className="text-lg">🔥</span>
            <div><span className="font-bold">Streaks:</span> Practice daily to build your streak. Miss a day and a freeze is used automatically.</div>
          </div>
          <div className="flex items-start gap-3">
            <span className="text-lg">🏆</span>
            <div><span className="font-bold">Badges:</span> Unlock badges by reaching milestones — questions answered, streaks maintained, and more.</div>
          </div>
        </div>
      </div>
    </div>
  );
}

function StatCard({ icon, label, value }: { icon: string; label: string; value: string }) {
  return (
    <div className="bg-white dark:bg-slate-900 shadow-card rounded-2xl p-4 text-center">
      <div className="text-2xl mb-1">{icon}</div>
      <p className="text-lg font-black text-slate-800 dark:text-slate-100">{value}</p>
      <p className="text-xs text-slate-500 dark:text-slate-400">{label}</p>
    </div>
  );
}
