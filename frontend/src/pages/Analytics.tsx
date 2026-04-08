import { useState, useEffect, useId } from 'react';
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, LineChart, Line, CartesianGrid } from 'recharts';
import { api } from '@/lib/api';
import { ScoreRing } from '@/components/shared/ScoreRing';
import { pageShell, pageStack } from '@/lib/layout';
import type { ApiAnalytics, SkillBreakdown } from '@/types';

function SkeletonCard({ className = '' }: { className?: string }) {
  return <div className={`animate-pulse rounded-2xl ${className}`} />;
}

interface StatCardProps {
  label: string;
  value: string | number;
  icon: string;
  gradient: string;
}

function StatCard({ label, value, icon, gradient }: StatCardProps) {
  return (
    <div className={`bg-gradient-to-br ${gradient} rounded-2xl p-3 lg:p-6 text-white shadow-card-lg card-hover stat-card-shine`}>
      <div className="text-xl lg:text-2xl mb-1 lg:mb-2">{icon}</div>
      <div className="font-black text-2xl lg:text-3xl">{value}</div>
      <div className="text-white/90 text-sm lg:text-sm">{label}</div>
    </div>
  );
}

interface SkillBarProps {
  skill: SkillBreakdown;
  color: string;
}

function SkillBar({ skill, color }: SkillBarProps) {
  const pct = Math.round(skill.accuracy * 100);
  return (
    <div>
      <div className="flex justify-between text-sm mb-1.5">
        <span className="text-slate-600 dark:text-slate-300 flex items-center gap-1.5 font-medium">
          <span>{skill.icon}</span>
          <span>{skill.name_ar}</span>
        </span>
        <span className="text-slate-500">{pct}% <span className="text-slate-500">({skill.correct}/{skill.total})</span></span>
      </div>
      <div className="h-2 bg-slate-100 dark:bg-slate-800 rounded-full overflow-hidden">
        <div className={`h-full ${color} rounded-full transition-all duration-700 animate-bar-fill`} style={{ width: `${pct}%` }} />
      </div>
    </div>
  );
}

export default function Analytics() {
  const gradId = useId();
  const [data, setData] = useState<ApiAnalytics | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  const loadData = async () => {
    setLoading(true); setError('');
    try { setData(await api.analytics()); }
    catch (e: unknown) { setError(e instanceof Error ? e.message : 'Error occurred'); }
    setLoading(false);
  };

  useEffect(() => { loadData(); }, []);

  if (loading) return (
    <div className={`${pageShell.wide} ${pageStack}`}>
      <div className="grid grid-cols-3 gap-4"><SkeletonCard className="bg-white shadow-card h-28 dark:bg-slate-900" /><SkeletonCard className="bg-white shadow-card h-28 dark:bg-slate-900" /><SkeletonCard className="bg-white shadow-card h-28 dark:bg-slate-900" /></div>
      <SkeletonCard className="bg-white shadow-card h-64 dark:bg-slate-900" />
    </div>
  );

  if (error) return (
    <div className="min-h-[60vh] flex flex-col items-center justify-center p-6 text-center">
      <div className="text-5xl mb-4">⚠️</div>
      <p className="text-red-500 text-sm mb-4">{error}</p>
      <button onClick={loadData} className="bg-teal-600 text-white font-bold py-2.5 px-8 rounded-xl shadow-brand">Retry</button>
    </div>
  );

  if (!data) return null;

  const verbal = (data.skill_breakdown || []).filter(s => s.section === 'verbal');
  const quant = (data.skill_breakdown || []).filter(s => s.section === 'quantitative');

  // Find weakest skill for recommendation
  const allSkills = (data.skill_breakdown || []).filter(s => s.total > 0);
  const weakest = allSkills.length > 0 ? allSkills.reduce((w, s) => s.accuracy < w.accuracy ? s : w, allSkills[0]) : null;
  const strongest = allSkills.length > 0 ? allSkills.reduce((w, s) => s.accuracy > w.accuracy ? s : w, allSkills[0]) : null;

  return (
    <div className={`${pageShell.wide} ${pageStack} page-enter text-slate-800 dark:text-slate-100`} data-testid="analytics-page">
      <h1 className="text-2xl lg:text-3xl font-black text-slate-800 dark:text-slate-100">Analytics</h1>

      {/* Stat Cards Row */}
      <div className="grid grid-cols-1 sm:grid-cols-3 gap-2 lg:gap-6" data-testid="analytics-stats">
        <StatCard label="Questions" value={data.total_questions} icon="📝" gradient="from-slate-500 to-slate-600" />
        <StatCard label="Correct" value={data.total_correct} icon="✅" gradient="from-emerald-500 to-emerald-600" />
        <StatCard label="Accuracy" value={`${Math.round(data.accuracy * 100)}%`} icon="🎯" gradient="from-teal-500 to-teal-600" />
      </div>

      {/* Recommendations */}
      {weakest && data.total_questions > 0 && (
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
          <div className="bg-gradient-to-l from-amber-50 to-orange-50 dark:from-amber-950/30 dark:to-orange-950/30 border border-amber-200 dark:border-amber-800 rounded-2xl p-5 flex items-start gap-4 stagger-1 card-hover">
            <div className="w-11 h-11 bg-white dark:bg-slate-900 rounded-xl shadow-sm flex items-center justify-center text-xl shrink-0">{weakest.icon}</div>
            <div>
              <p className="text-amber-800 dark:text-amber-200 font-bold text-sm">⚡ Improvement Point</p>
              <p className="text-amber-700/70 dark:text-amber-300/70 text-sm mt-0.5">
                <span className="font-bold">{weakest.name_ar}</span> is your weakest skill at {Math.round(weakest.accuracy * 100)}% accuracy.
                Focusing on it will significantly improve your score.
              </p>
            </div>
          </div>
          {strongest && strongest.skill_id !== weakest.skill_id && (
            <div className="bg-gradient-to-l from-emerald-50 to-teal-50 dark:from-emerald-950/30 dark:to-teal-950/30 border border-emerald-200 dark:border-emerald-800 rounded-2xl p-5 flex items-start gap-4 stagger-2 card-hover">
              <div className="w-11 h-11 bg-white dark:bg-slate-900 rounded-xl shadow-sm flex items-center justify-center text-xl shrink-0">{strongest.icon}</div>
              <div>
                <p className="text-emerald-800 dark:text-emerald-200 font-bold text-sm">🌟 Strong Point</p>
                <p className="text-emerald-700/70 dark:text-emerald-300/70 text-sm mt-0.5">
                  <span className="font-bold">{strongest.name_ar}</span> is your strongest skill at {Math.round(strongest.accuracy * 100)}% accuracy.
                  Well done — keep it up!
                </p>
              </div>
            </div>
          )}
        </div>
      )}

      {/* Score + Trend Row */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Predicted Score */}
        <div className="bg-white shadow-card rounded-2xl p-6 flex flex-col items-center justify-center card-hover dark:bg-slate-900" data-testid="analytics-score-card">
          <p className="text-slate-500 text-sm mb-4 dark:text-slate-400">Predicted Score</p>
          <ScoreRing score={data.predicted_score.mid} label="out of 100" />
          <div className="flex gap-4 mt-5 w-full text-center">
            <div className="flex-1">
              <div className="h-1.5 bg-slate-100 dark:bg-slate-800 rounded-full overflow-hidden mb-1">
                <div className="h-full bg-blue-400 rounded-full" style={{ width: `${data.predicted_score.verbal_mastery * 100}%` }} />
              </div>
              <span className="text-sm text-slate-500">Verbal {Math.round(data.predicted_score.verbal_mastery * 100)}%</span>
            </div>
            <div className="flex-1">
              <div className="h-1.5 bg-slate-100 dark:bg-slate-800 rounded-full overflow-hidden mb-1">
                <div className="h-full bg-purple-400 rounded-full" style={{ width: `${data.predicted_score.quant_mastery * 100}%` }} />
              </div>
              <span className="text-sm text-slate-500">Quant {Math.round(data.predicted_score.quant_mastery * 100)}%</span>
            </div>
          </div>
        </div>

        {/* Daily Accuracy Trend */}
        <div className="lg:col-span-2 bg-white shadow-card rounded-2xl p-6 card-hover dark:bg-slate-900">
          <h3 className="text-slate-800 font-bold text-sm mb-4 dark:text-slate-100">Daily Accuracy Trend</h3>
          {data.daily_trend && data.daily_trend.length > 1 ? (
            <div style={{ direction: 'ltr' }}>
              <ResponsiveContainer width="100%" height={200}>
                <LineChart data={data.daily_trend}>
                  <CartesianGrid strokeDasharray="3 3" className="[&>line]:stroke-slate-200 dark:[&>line]:stroke-slate-800" stroke="currentColor" />
                  <XAxis dataKey="date" tick={{ fontSize: 13 }} className="[&_text]:fill-slate-500 dark:[&_text]:fill-slate-400" tickFormatter={(d: string) => d.slice(5)} />
                  <YAxis domain={[0, 1]} tick={{ fontSize: 13 }} className="[&_text]:fill-slate-500 dark:[&_text]:fill-slate-400" tickFormatter={(v: number) => `${Math.round(v * 100)}%`} />
                  <Tooltip formatter={(v: number) => `${Math.round(v * 100)}%`}
                    contentStyle={{ borderRadius: 12, fontSize: 12, boxShadow: '0 4px 12px rgba(0,0,0,0.15)', backgroundColor: 'var(--tooltip-bg, #fff)', border: '1px solid var(--tooltip-border, #e2e8f0)', color: 'var(--tooltip-text, #334155)' }}
                    labelStyle={{ color: 'var(--tooltip-text, #334155)', fontWeight: 600 }}
                    itemStyle={{ color: 'var(--tooltip-text, #334155)' }} />
                  <Line type="monotone" dataKey="accuracy" stroke={`url(#${gradId})`} strokeWidth={3} dot={{ fill: '#0d9488', r: 4, strokeWidth: 2 }} />
                  <defs>
                    <linearGradient id={gradId} x1="0" y1="0" x2="1" y2="0">
                      <stop offset="0%" stopColor="#14b8a6" />
                      <stop offset="100%" stopColor="#0d9488" />
                    </linearGradient>
                  </defs>
                </LineChart>
              </ResponsiveContainer>
            </div>
          ) : (
            <div className="flex items-center justify-center h-48 text-slate-500 text-sm">
              Not enough data yet
            </div>
          )}
        </div>
      </div>

      {/* Skill Breakdown */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Verbal Skills */}
        <div className="bg-white shadow-card rounded-2xl p-6 card-hover dark:bg-slate-900" data-testid="analytics-verbal">
          <h3 className="text-slate-800 font-bold text-sm mb-5 flex items-center gap-2 dark:text-slate-100">
            <span className="w-6 h-6 bg-blue-50 dark:bg-blue-900/40 rounded-lg flex items-center justify-center text-sm">📖</span>
            Verbal Section
          </h3>
          {verbal.length > 0 ? (
            <div className="space-y-4">
              {verbal.map(s => <SkillBar key={s.skill_id} skill={s} color="bg-blue-400" />)}
            </div>
          ) : (
            <p className="text-slate-500 text-sm text-center py-6">Not started yet</p>
          )}
        </div>

        {/* Quantitative Skills */}
        <div className="bg-white shadow-card rounded-2xl p-6 card-hover dark:bg-slate-900" data-testid="analytics-quant">
          <h3 className="text-slate-800 font-bold text-sm mb-5 flex items-center gap-2 dark:text-slate-100">
            <span className="w-6 h-6 bg-purple-50 dark:bg-purple-900/40 rounded-lg flex items-center justify-center text-sm">🔢</span>
            Quantitative Section
          </h3>
          {quant.length > 0 ? (
            <div className="space-y-4">
              {quant.map(s => <SkillBar key={s.skill_id} skill={s} color="bg-purple-400" />)}
            </div>
          ) : (
            <p className="text-slate-500 text-sm text-center py-6">Not started yet</p>
          )}
        </div>
      </div>

      {/* Questions per Skill Chart */}
      {data.skill_breakdown && data.skill_breakdown.length > 0 && (
        <div className="bg-white shadow-card rounded-2xl p-6 card-hover dark:bg-slate-900">
          <h3 className="text-slate-800 font-bold text-sm mb-4 dark:text-slate-100">Questions per Skill</h3>
          <div style={{ direction: 'ltr' }}>
            <ResponsiveContainer width="100%" height={Math.max(200, data.skill_breakdown.length * 40)}>
              <BarChart data={data.skill_breakdown} layout="vertical" margin={{ left: 10 }}>
                <XAxis type="number" tick={{ fontSize: 13 }} className="[&_text]:fill-slate-500 dark:[&_text]:fill-slate-400" />
                <YAxis type="category" dataKey="name_ar" tick={{ fontSize: 13 }} className="[&_text]:fill-slate-500 dark:[&_text]:fill-slate-400" width={90} />
                <Tooltip contentStyle={{ borderRadius: 12, fontSize: 12, boxShadow: '0 4px 12px rgba(0,0,0,0.15)', backgroundColor: 'var(--tooltip-bg, #fff)', border: '1px solid var(--tooltip-border, #e2e8f0)', color: 'var(--tooltip-text, #334155)' }}
                  labelStyle={{ color: 'var(--tooltip-text, #334155)', fontWeight: 600 }}
                  itemStyle={{ color: 'var(--tooltip-text, #334155)' }} />
                <Bar dataKey="correct" stackId="a" fill="#22c55e" radius={[0, 0, 0, 0]} name="Correct" />
                <Bar dataKey="total" stackId="b" className="fill-slate-200 dark:fill-slate-700" radius={[0, 4, 4, 0]} name="Total" />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>
      )}

      {data.total_questions === 0 && (
        <div className="text-center py-16">
          <div className="text-5xl mb-4 animate-float">📊</div>
          <p className="text-slate-500 dark:text-slate-400 text-lg">Start training to see your analytics here</p>
        </div>
      )}
    </div>
  );
}
