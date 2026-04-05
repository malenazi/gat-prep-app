import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { api } from '@/lib/api';
import { useAuth } from '@/hooks/useAuth';
import { ScoreRing } from '@/components/shared/ScoreRing';
import { SkeletonCard } from '@/components/shared/SkeletonCard';
import { FeedbackModal } from '@/components/shared/FeedbackModal';
import { pageShell, pageStack } from '@/lib/layout';
import type { TodayPlan, StudyPlanDay, ApiBadge } from '@/types';

export default function Dashboard() {
  const { user, loadUser, logout: onLogout } = useAuth();
  const [today, setToday] = useState<TodayPlan | null>(null);
  const [badges, setBadges] = useState<ApiBadge[]>([]);
  const [plan, setPlan] = useState<StudyPlanDay[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [advancing, setAdvancing] = useState(false);
  const [feedbackTrigger, setFeedbackTrigger] = useState<string | null>(null);

  const loadData = async () => {
    setLoading(true);
    setError('');
    try {
      const [t, b, p] = await Promise.all([api.today(), api.badges(), api.studyPlan()]);
      setToday(t);
      setBadges(b);
      setPlan(p);
    } catch (e: unknown) {
      setError(e instanceof Error ? e.message : 'Error loading data');
    }
    setLoading(false);
  };

  useEffect(() => { loadData(); }, []);

  // Smart feedback trigger — only once per day
  useEffect(() => {
    if (!today || loading || !user) return;
    const lastFB = localStorage.getItem('lastFeedbackDate');
    const todayStr = new Date().toISOString().split('T')[0];
    if (lastFB === todayStr) return;
    const sessionDone = today && !today.is_rest_day && today.completed_questions >= today.target_questions && today.target_questions > 0;
    if (sessionDone) setFeedbackTrigger('session_complete');
    else if (user.streak >= 7 && !lastFB) setFeedbackTrigger('streak');
  }, [today, loading, user]);

  const advanceDay = async () => {
    setAdvancing(true);
    try {
      await api.advanceDay();
      await loadUser();
      await loadData();
    } catch (e: unknown) {
      setError(e instanceof Error ? e.message : 'Error occurred');
    }
    setAdvancing(false);
  };

  if (loading) return (
    <div className={`${pageShell.wide} ${pageStack}`}>
      <SkeletonCard className="bg-white dark:bg-slate-900 shadow-card h-40" />
      <SkeletonCard className="bg-white dark:bg-slate-900 shadow-card h-24" />
      <div className="grid grid-cols-1 md:grid-cols-2 gap-3 lg:gap-6">
        <SkeletonCard className="bg-white dark:bg-slate-900 shadow-card h-48" />
        <SkeletonCard className="bg-white dark:bg-slate-900 shadow-card h-48" />
      </div>
    </div>
  );

  if (error) return (
    <div className="min-h-[60vh] flex flex-col items-center justify-center p-6 text-center page-enter">
      <div className="text-5xl mb-4">⚠️</div>
      <p className="text-red-500 text-sm mb-4">{error}</p>
      <button onClick={loadData} className="bg-teal-600 text-white font-bold py-2.5 px-8 rounded-xl shadow-brand">Retry</button>
    </div>
  );

  if (!user) return null;

  const score = user.predicted_score;
  const verbal = user.abilities?.filter(a => a.section === 'verbal') || [];
  const quant = user.abilities?.filter(a => a.section === 'quantitative') || [];
  const earnedBadges = badges.filter(b => b.earned);
  const sessionComplete = today && !today.is_rest_day && today.completed_questions >= today.target_questions && today.target_questions > 0;
  const sessionHref = today?.is_mock_day ? '/mock' : '/practice';

  // Accomplishment stats
  const completedDays = plan.filter(d => d.completed).length;
  const totalAnswered = user.abilities?.reduce((s, a) => s + a.questions_seen, 0) || 0;

  // Find weakest skill for guidance
  const allAbilities = user.abilities || [];
  const weakest = allAbilities.length > 0 ? allAbilities.reduce((w, a) => a.mastery < w.mastery ? a : w, allAbilities[0]) : null;

  return (
    <div className={`${pageShell.wide} ${pageStack} page-enter`} data-testid="dashboard-page">
      {/* ═══ Mobile Header ═══ */}
      <div className="lg:hidden flex items-center justify-between">
        <div>
          <p className="text-slate-500 text-sm">Hello</p>
          <h1 className="text-xl font-black text-slate-800 dark:text-slate-100">{user.name} 👋</h1>
        </div>
        <div className="flex items-center gap-2">
          <div className="bg-white shadow-card rounded-xl px-3 py-2 flex items-center gap-1.5">
            <span className={`text-base ${user.streak > 0 ? 'animate-fire' : ''}`}>🔥</span>
            <span className="font-bold text-slate-800 dark:text-slate-100 text-sm">{user.streak}</span>
          </div>
          <div className="bg-white shadow-card rounded-xl px-3 py-2 flex items-center gap-1.5">
            <span className="text-base">⚡</span>
            <span className="font-bold text-teal-600 dark:text-teal-400 text-sm">{user.xp}</span>
          </div>
        </div>
      </div>

      {/* ═══ Hero: Session CTA + Score Ring ═══ */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-3 lg:gap-6">
        <div className="lg:col-span-2">
          {today && !today.is_rest_day && !sessionComplete && (
            <Link to={sessionHref} className="block group" data-testid="dashboard-session-link">
              <div className="bg-gradient-to-l from-teal-500 to-teal-700 animate-gradient rounded-2xl p-4 lg:p-8 text-white shadow-card-lg card-hover relative overflow-hidden" data-testid="dashboard-session-card">
                <div className="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAiIGhlaWdodD0iNjAiIHZpZXdCb3g9IjAgMCA2MCA2MCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyBmaWxsPSJub25lIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiPjxnIGZpbGw9IiNmZmYiIGZpbGwtb3BhY2l0eT0iMC4wNSI+PHBhdGggZD0iTTM2IDM0djZoLTJ2LTZoMnptMC0xMHY2aC0ydi02aDJ6Ii8+PC9nPjwvZz48L3N2Zz4=')] opacity-30" />
                <div className="relative">
                  <div className="flex items-center justify-between mb-4">
                    <div>
                      <p className="text-teal-100 text-sm font-medium">Day {user.current_day} • {today.phase === 'foundation' ? 'Foundation Phase' : today.phase === 'building' ? 'Building Phase' : 'Mastery Phase'}</p>
                      <h2 className="text-white font-black text-xl lg:text-3xl mt-1">Today's Session</h2>
                    </div>
                    {today.is_mock_day && <span className="bg-white/20 backdrop-blur text-white text-sm font-bold px-4 py-1.5 rounded-full">Mock Exam</span>}
                  </div>
                  {today.focus_skills && (
                    <div className="flex flex-wrap gap-2 mb-5">
                      {today.focus_skills.map(s => (
                        <span key={s.id} className="bg-white/15 backdrop-blur text-teal-50 text-sm px-3 py-1.5 rounded-lg">{s.name_ar}</span>
                      ))}
                    </div>
                  )}
                  <div className="flex items-center justify-between">
                    <div className="flex items-center gap-3">
                      <div className="h-2 w-40 lg:w-56 bg-white/20 rounded-full overflow-hidden">
                        <div className="h-full bg-white rounded-full transition-all"
                          style={{ width: `${Math.min(100, (today.completed_questions / Math.max(1, today.target_questions)) * 100)}%` }} />
                      </div>
                      <span className="text-teal-100 text-sm">{today.completed_questions}/{today.target_questions}</span>
                    </div>
                    <span className="text-white font-bold text-sm group-hover:translate-x-[-4px] transition-transform">
                      {today.is_mock_day ? 'Start Mock Exam ←' : 'Start Practice ←'}
                    </span>
                  </div>
                </div>
              </div>
            </Link>
          )}

          {sessionComplete && (
            <div className="bg-gradient-to-l from-emerald-500 to-emerald-600 rounded-2xl p-4 lg:p-8 text-white shadow-card-lg relative overflow-hidden" data-testid="dashboard-session-complete">
              <div className="relative text-center lg:text-left">
                <div className="text-5xl mb-3 animate-float">🎉</div>
                <h2 className="text-white font-black text-lg lg:text-2xl">Session Complete!</h2>
                <p className="text-emerald-100 text-sm mt-1 mb-5">{today!.completed_questions}/{today!.target_questions} questions</p>
                <div className="flex gap-3 justify-center lg:justify-start">
                  <Link to="/practice" className="bg-white/20 backdrop-blur text-white font-bold py-2.5 px-6 rounded-xl text-sm hover:bg-white/30 transition">Extra Practice</Link>
                  {user.current_day < 30 && (
                    <button onClick={advanceDay} disabled={advancing}
                      data-testid="dashboard-advance-day"
                      className="bg-white text-emerald-700 font-bold py-2.5 px-6 rounded-xl text-sm hover:bg-emerald-50 transition disabled:opacity-50">
                      {advancing ? '...' : 'Go to Next Day ←'}
                    </button>
                  )}
                </div>
              </div>
            </div>
          )}

          {today?.is_rest_day && (
            <div className="bg-white dark:bg-slate-900 shadow-card rounded-2xl p-5 lg:p-8 text-center">
              <div className="text-6xl mb-3 animate-float">😴</div>
              <h2 className="text-slate-800 dark:text-slate-100 font-black text-lg lg:text-xl">Rest Day</h2>
              <p className="text-slate-500 text-sm mt-1">Rest today. You're ready!</p>
            </div>
          )}
        </div>

        {/* Score Ring */}
        <div className="bg-white shadow-card rounded-2xl p-4 lg:p-6 flex flex-col items-center justify-center card-hover dark:bg-slate-900" data-testid="dashboard-score-card">
          <p className="text-slate-500 dark:text-slate-400 text-sm mb-4">Predicted Score</p>
          <ScoreRing score={score.mid} label="of 100" />
          <div className="flex gap-6 mt-5 w-full">
            <div className="flex-1 text-center">
              <div className="h-1.5 bg-slate-100 dark:bg-slate-800 rounded-full overflow-hidden mb-1.5">
                <div className="h-full bg-blue-400 rounded-full" style={{ width: `${score.verbal_mastery * 100}%` }} />
              </div>
              <span className="text-sm text-slate-500 dark:text-slate-400">Verbal {Math.round(score.verbal_mastery * 100)}%</span>
            </div>
            <div className="flex-1 text-center">
              <div className="h-1.5 bg-slate-100 dark:bg-slate-800 rounded-full overflow-hidden mb-1.5">
                <div className="h-full bg-purple-400 rounded-full" style={{ width: `${score.quant_mastery * 100}%` }} />
              </div>
              <span className="text-sm text-slate-500 dark:text-slate-400">Quant {Math.round(score.quant_mastery * 100)}%</span>
            </div>
          </div>
        </div>
      </div>

      {/* ═══ Guidance Card — "What next?" ═══ */}
      {weakest && weakest.questions_seen > 0 && (
        <div className="bg-gradient-to-l from-indigo-50 to-blue-50 dark:from-indigo-950/30 dark:to-blue-950/30 border border-indigo-100 dark:border-indigo-800 rounded-2xl p-3 lg:p-5 flex items-center gap-4 stagger-2">
          <div className="w-12 h-12 bg-white rounded-xl shadow-sm flex items-center justify-center text-2xl shrink-0">
            {weakest.icon}
          </div>
          <div className="flex-1 min-w-0">
            <p className="text-indigo-800 dark:text-indigo-200 font-bold text-sm">💡 Tip to Improve Your Score</p>
            <p className="text-indigo-600/70 dark:text-indigo-400/70 text-sm mt-0.5">
              Focus on <span className="font-bold text-indigo-700 dark:text-indigo-300">{weakest.name_ar}</span> — your mastery is only {Math.round(weakest.mastery * 100)}%.
              {weakest.section === 'verbal' ? ' Practice reading and analysis.' : ' Practice systematic solving.'}
            </p>
          </div>
          <Link to="/practice" className="bg-indigo-600 text-white text-sm font-bold px-4 py-2 rounded-lg shrink-0 hover:bg-indigo-500 transition">
            Practice Now
          </Link>
        </div>
      )}

      {/* ═══ 30-Day Plan & Phases Timeline ═══ */}
      {plan.length > 0 && (
        <div className="bg-white shadow-card rounded-2xl p-4 lg:p-6 card-hover dark:bg-slate-900" data-testid="dashboard-plan-card">
          <div className="flex items-center justify-between mb-4 lg:mb-5">
            <h3 className="text-slate-800 dark:text-slate-100 font-bold text-base lg:text-lg">30-Day Plan</h3>
            <Link to="/plan" className="text-teal-600 text-sm font-bold hover:text-teal-500 transition">View Details ←</Link>
          </div>

          {/* Phase Progress Bar */}
          <div className="flex gap-1.5 mb-5">
            {([
              { key: 'foundation' as const, label: 'Foundation', range: '1-7', gradient: 'from-blue-400 to-blue-500', text: 'text-blue-600', bg: 'bg-blue-50' },
              { key: 'building' as const, label: 'Building', range: '8-22', gradient: 'from-teal-400 to-teal-500', text: 'text-teal-600', bg: 'bg-teal-50' },
              { key: 'peak' as const, label: 'Mastery', range: '23-30', gradient: 'from-amber-400 to-amber-500', text: 'text-amber-600', bg: 'bg-amber-50' },
            ]).map(ph => {
              const phDays = plan.filter(d => d.phase === ph.key);
              const phCompleted = phDays.filter(d => d.completed).length;
              const phPct = phDays.length > 0 ? (phCompleted / phDays.length) * 100 : 0;
              const isCurrent = plan.find(d => d.is_today)?.phase === ph.key;
              return (
                <div key={ph.key} className="flex-1">
                  <div className="flex items-center justify-between mb-1">
                    <span className={`text-sm font-bold ${isCurrent ? ph.text : 'text-slate-500'}`}>{ph.label}</span>
                    <span className="text-sm text-slate-500">{ph.range}</span>
                  </div>
                  <div className={`h-2.5 rounded-full overflow-hidden ${isCurrent ? ph.bg : 'bg-slate-100 dark:bg-slate-800'}`}>
                    <div className={`h-full bg-gradient-to-l ${ph.gradient} rounded-full transition-all duration-700`} style={{ width: `${phPct}%` }} />
                  </div>
                </div>
              );
            })}
          </div>

          {/* Compact 30-Day Calendar Strip */}
          <div className="grid grid-cols-6 md:grid-cols-10 lg:grid-cols-15 gap-1">
            {plan.map(day => {
              const isCurrent = day.is_today;
              let bg = 'bg-slate-100 dark:bg-slate-800';
              let ring = '';
              if (day.completed) bg = 'bg-emerald-400';
              else if (isCurrent) { bg = 'bg-teal-500'; ring = 'ring-2 ring-teal-300 ring-offset-1 animate-glow-ring'; }
              else if (day.is_rest_day) bg = 'bg-slate-200 dark:bg-slate-700';
              else if (day.is_mock_day) bg = 'bg-amber-300';

              return (
                <div key={day.day} title={`Day ${day.day}${day.completed ? ' ✓' : ''}${day.is_mock_day ? ' Mock' : ''}${day.is_rest_day ? ' Rest' : ''}`}
                  className={`aspect-square rounded-md ${bg} ${ring} flex items-center justify-center transition-all hover:scale-125 cursor-default`}>
                  {day.completed ? (
                    <svg className="w-2.5 h-2.5 text-white" fill="currentColor" viewBox="0 0 20 20"><path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" /></svg>
                  ) : isCurrent ? (
                    <span className="text-white text-sm font-black">{day.day}</span>
                  ) : null}
                </div>
              );
            })}
          </div>

          {/* Legend */}
          <div className="flex items-center gap-4 mt-3 text-sm text-slate-500">
            <span className="flex items-center gap-1"><span className="w-2.5 h-2.5 rounded bg-emerald-400 inline-block" /> Completed</span>
            <span className="flex items-center gap-1"><span className="w-2.5 h-2.5 rounded bg-teal-500 inline-block" /> Today</span>
            <span className="flex items-center gap-1"><span className="w-2.5 h-2.5 rounded bg-amber-300 inline-block" /> Mock</span>
            <span className="flex items-center gap-1"><span className="w-2.5 h-2.5 rounded bg-slate-200 inline-block" /> Rest</span>
            <span className="flex items-center gap-1"><span className="w-2.5 h-2.5 rounded bg-slate-100 inline-block" /> Upcoming</span>
          </div>
        </div>
      )}

      {/* ═══ Current Accomplishments ═══ */}
      <div data-testid="dashboard-accomplishments">
        <h3 className="text-slate-800 dark:text-slate-100 font-bold text-base lg:text-lg mb-3 lg:mb-4">Current Accomplishments</h3>
        <div className="grid grid-cols-2 lg:grid-cols-4 gap-2 lg:gap-3">
          <AccomplishmentCard icon="📅" value={`${completedDays}/30`} label="Days Completed" gradient="from-blue-500 to-blue-600" />
          <AccomplishmentCard icon="📝" value={totalAnswered} label="Questions Answered" gradient="from-teal-500 to-teal-600" />
          <AccomplishmentCard icon="🔥" value={`${user.streak} days`} label="Current Streak" gradient="from-orange-500 to-red-500" />
          <AccomplishmentCard icon="⚡" value={user.xp} label="XP Points" gradient="from-amber-500 to-amber-600" />
        </div>

        {/* Earned badges inline */}
        {earnedBadges.length > 0 && (
          <div className="mt-3 lg:mt-4 bg-white dark:bg-slate-900 shadow-card rounded-2xl p-3 lg:p-5 flex items-center gap-4">
            <div className="flex -space-x-1 space-x-reverse">
              {earnedBadges.slice(0, 5).map(b => (
                <div key={b.id} title={b.name_ar}
                  className="w-10 h-10 rounded-full bg-slate-50 border-2 border-white shadow-sm flex items-center justify-center text-lg">
                  {b.icon}
                </div>
              ))}
            </div>
            <div className="flex-1">
              <p className="text-slate-700 dark:text-slate-200 font-bold text-sm">{earnedBadges.length} Badge{earnedBadges.length !== 1 ? 's' : ''} Earned</p>
              <p className="text-slate-500 dark:text-slate-400 text-sm">{earnedBadges.map(b => b.name_ar).join(' • ')}</p>
            </div>
            {badges.length > earnedBadges.length && (
              <span className="text-slate-500 text-sm">{badges.length - earnedBadges.length} remaining</span>
            )}
          </div>
        )}
      </div>

      {/* ═══ Mock Exam CTA ═══ */}
      {user.current_day >= 25 && (
        <div className={`rounded-2xl p-5 lg:p-6 card-hover ${user.mock_attempts >= user.mock_max_attempts
          ? 'bg-emerald-50 dark:bg-emerald-950/30 border border-emerald-200 dark:border-emerald-800'
          : 'bg-gradient-to-l from-amber-500 to-orange-500 text-white shadow-lg'}`}>
          {user.mock_attempts >= user.mock_max_attempts ? (
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-3">
                <span className="text-3xl">✅</span>
                <div>
                  <p className="font-bold text-emerald-800 dark:text-emerald-200">All Attempts Completed</p>
                  <p className="text-sm text-emerald-600 dark:text-emerald-400">Best Score: {user.mock_score} of 100 ({user.mock_attempts} of {user.mock_max_attempts} attempts)</p>
                </div>
              </div>
              <a href="/mock" className="text-sm font-bold text-emerald-600 hover:text-emerald-700">View Results ←</a>
            </div>
          ) : user.mock_attempts === 0 ? (
            <div className="flex items-center justify-between">
              <div>
                <p className="font-black text-lg lg:text-xl">Final Mock Exam</p>
                <p className="text-amber-100 text-sm">65 questions • 70 minutes • {user.mock_max_attempts} attempts available</p>
              </div>
              <a href="/mock"
                className="bg-white text-amber-600 font-bold px-5 py-2.5 rounded-xl hover:bg-amber-50 transition text-sm">
                Start Mock Exam
              </a>
            </div>
          ) : (
            <div className="flex items-center justify-between">
              <div>
                <p className="font-black text-lg lg:text-xl">Final Mock Exam</p>
                <p className="text-amber-100 text-sm">Best Score: {user.mock_score} of 100</p>
              </div>
              <a href="/mock"
                className="bg-white text-amber-600 font-bold px-5 py-2.5 rounded-xl hover:bg-amber-50 transition text-sm">
                Start Next Attempt (Attempt {user.mock_attempts + 1} of {user.mock_max_attempts})
              </a>
            </div>
          )}
        </div>
      )}

      {/* ═══ Mastery Heatmap ═══ */}
      <div className="bg-white shadow-card rounded-2xl p-4 lg:p-6 card-hover dark:bg-slate-900" data-testid="dashboard-mastery-map">
        <h3 className="text-slate-800 dark:text-slate-100 font-bold text-base lg:text-lg mb-4 lg:mb-5">Mastery Map</h3>

        {/* Section summaries */}
        <div className="grid grid-cols-2 gap-3 mb-5">
          {(() => {
            const sections = [
              { label: 'Verbal', skills: verbal, icon: '📖',
                bg: 'bg-blue-50', border: 'border-blue-200', title: 'text-blue-700', score: 'text-blue-600',
                trackBg: 'bg-blue-100', bar: 'bg-blue-500', sub: 'text-blue-400' },
              { label: 'Quant', skills: quant, icon: '🔢',
                bg: 'bg-violet-50', border: 'border-violet-200', title: 'text-violet-700', score: 'text-violet-600',
                trackBg: 'bg-violet-100', bar: 'bg-violet-500', sub: 'text-violet-400' },
            ];
            return sections.map(sec => {
              const totalSeen = sec.skills.reduce((s, a) => s + a.questions_seen, 0);
              const totalCorrect = sec.skills.reduce((s, a) => s + a.correct_count, 0);
              const avgMastery = sec.skills.length > 0 ? Math.round(sec.skills.reduce((s, a) => s + a.mastery, 0) / sec.skills.length * 100) : 0;
              return (
                <div key={sec.label} className={`${sec.bg} border ${sec.border} rounded-xl p-3 flex items-center gap-3`}>
                  <span className="text-2xl">{sec.icon}</span>
                  <div className="flex-1">
                    <div className="flex items-center justify-between mb-1">
                      <span className={`text-sm font-bold ${sec.title}`}>{sec.label}</span>
                      <span className={`text-lg font-black ${sec.score}`}>{avgMastery}%</span>
                    </div>
                    <div className={`h-1.5 ${sec.trackBg} rounded-full overflow-hidden`}>
                      <div className={`h-full ${sec.bar} rounded-full transition-all duration-700`} style={{ width: `${avgMastery}%` }} />
                    </div>
                    <p className={`text-xs ${sec.sub} mt-1`}>{totalCorrect} correct of {totalSeen} questions</p>
                  </div>
                </div>
              );
            });
          })()}
        </div>

        {/* Skill rows */}
        <div className="space-y-2">
          {[...verbal, ...quant].map(a => {
            const pct = Math.round(a.mastery * 100);
            const barColor = pct >= 80 ? 'bg-emerald-500' : pct >= 50 ? 'bg-amber-500' : pct > 0 ? 'bg-red-400' : 'bg-slate-200';
            const textColor = pct >= 80 ? 'text-emerald-600' : pct >= 50 ? 'text-amber-600' : pct > 0 ? 'text-red-500' : 'text-slate-400';
            const bgColor = pct >= 80 ? 'bg-emerald-50 dark:bg-emerald-950/30' : pct >= 50 ? 'bg-amber-50 dark:bg-amber-950/30' : pct > 0 ? 'bg-red-50 dark:bg-red-950/30' : 'bg-slate-50 dark:bg-slate-900';
            const sectionColor = a.section === 'verbal' ? 'border-r-blue-400' : 'border-r-violet-400';
            return (
              <div key={a.skill_id} className={`${bgColor} border border-slate-100 dark:border-slate-800 border-r-4 ${sectionColor} rounded-lg p-3 flex items-center gap-3`}>
                <span className="text-lg shrink-0">{a.icon}</span>
                <div className="flex-1 min-w-0">
                  <div className="flex items-center justify-between mb-1">
                    <span className="text-sm font-medium text-slate-700 dark:text-slate-200 truncate">{a.name_ar}</span>
                    <span className={`text-sm font-black ${textColor}`}>{a.questions_seen > 0 ? `${pct}%` : '—'}</span>
                  </div>
                  <div className="h-1.5 bg-slate-100 rounded-full overflow-hidden">
                    <div className={`h-full ${barColor} rounded-full animate-bar-fill`} style={{ width: `${pct}%` }} />
                  </div>
                  <div className="flex items-center justify-between mt-1">
                    <span className="text-sm text-slate-400">{a.correct_count} / {a.questions_seen} questions</span>
                    {a.questions_seen > 0 && (
                      <span className="text-xs text-slate-400">θ = {a.theta > 0 ? '+' : ''}{a.theta.toFixed(1)}</span>
                    )}
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {/* ═══ League ═══ */}
      <div className="bg-white shadow-card rounded-2xl p-4 lg:p-6 card-hover flex items-center gap-5 dark:bg-slate-900" data-testid="dashboard-league">
        <div className="text-4xl animate-float">
          {{ bronze: '🥉', silver: '🥈', gold: '🥇', platinum: '💎', diamond: '👑', champion: '🏆' }[user.league] || '🥉'}
        </div>
        <div className="flex-1">
          <p className="text-slate-800 font-bold text-base lg:text-lg">
            {{bronze: 'Bronze', silver: 'Silver', gold: 'Gold', platinum: 'Platinum', diamond: 'Diamond', champion: 'Champion'}[user.league] || 'Bronze'}
          </p>
          <p className="text-slate-500 dark:text-slate-400 text-sm">Weekly League</p>
          <div className="mt-2 flex items-center gap-2">
            <div className="h-1.5 flex-1 bg-slate-100 dark:bg-slate-800 rounded-full overflow-hidden">
              <div className="h-full bg-amber-400 rounded-full" style={{ width: `${Math.min(100, (user.xp % 500) / 5)}%` }} />
            </div>
            <span className="text-sm text-slate-500">⚡ {user.xp} XP</span>
          </div>
        </div>
      </div>

      {/* Mobile Logout */}
      <button onClick={onLogout} className="lg:hidden text-slate-500 text-sm w-full text-center py-3 hover:text-red-500 transition" data-testid="logout-mobile">
        Logout
      </button>

      {/* Smart Feedback Modal */}
      {feedbackTrigger && (
        <FeedbackModal trigger={feedbackTrigger} onClose={() => setFeedbackTrigger(null)} />
      )}
    </div>
  );
}

interface AccomplishmentCardProps {
  icon: string;
  value: string | number;
  label: string;
  gradient: string;
}

function AccomplishmentCard({ icon, value, label, gradient }: AccomplishmentCardProps) {
  return (
    <div className={`bg-gradient-to-br ${gradient} rounded-2xl p-4 lg:p-5 text-white shadow-card-lg card-hover stat-card-shine`}>
      <div className="text-xl lg:text-2xl mb-1">{icon}</div>
      <div className="font-black text-xl lg:text-2xl">{value}</div>
      <div className="text-white/90 text-sm lg:text-sm">{label}</div>
    </div>
  );
}

