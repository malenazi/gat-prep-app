import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '@/hooks/useAuth';
import { api } from '@/lib/api';
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, Cell, PieChart, Pie, RadarChart, Radar, PolarGrid, PolarAngleAxis, PolarRadiusAxis, Legend } from 'recharts';
import { Shield, BarChart3, MessageSquare, Users, BookOpen, Search, Plus, Pencil, Trash2, ChevronDown, ChevronUp, Star, Flame, X, ArrowRight, LogOut, Trophy, AlertTriangle } from 'lucide-react';
import type { AdminFeedbackAnalytics, AdminUsersResponse, AdminFeedbackItem, AdminQuestion, QuestionPayload, ApiSkill, QuestionAnalysis } from '@/types';

type TabKey = 'overview' | 'feedback' | 'users' | 'questions' | 'mock';

const triggerLabels: Record<string, string> = {
  session_complete: 'After Session',
  diagnostic: 'After Diagnostic',
  phase_change: 'Phase Change',
  streak: 'Streak',
};
const ratingEmojis = ['', '😡', '😕', '😐', '🙂', '😍'];
const ratingColors = ['', '#ef4444', '#f97316', '#94a3b8', '#22c55e', '#0d9488'];

export default function Admin() {
  const { user, logout } = useAuth();
  const nav = useNavigate();
  const [tab, setTab] = useState<TabKey>('overview');
  const [analytics, setAnalytics] = useState<AdminFeedbackAnalytics | null>(null);
  const [users, setUsers] = useState<AdminUsersResponse | null>(null);
  const [feedback, setFeedback] = useState<AdminFeedbackItem[]>([]);
  const [questions, setQuestions] = useState<AdminQuestion[]>([]);
  const [questionAnalysis, setQuestionAnalysis] = useState<QuestionAnalysis | null>(null);
  const [skills, setSkills] = useState<ApiSkill[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  const [triggerFilter, setTriggerFilter] = useState('');
  const [userSearch, setUserSearch] = useState('');
  const [skillFilter, setSkillFilter] = useState('');
  const [stageFilter, setStageFilter] = useState('');
  const [statusFilter, setStatusFilter] = useState('');
  const [questionSort, setQuestionSort] = useState('');
  const [expandedQ, setExpandedQ] = useState<number | null>(null);
  const [showAddQ, setShowAddQ] = useState(false);
  const [editQ, setEditQ] = useState<AdminQuestion | null>(null);
  const [sortCol, setSortCol] = useState<string>('current_day');
  const [sortAsc, setSortAsc] = useState(false);
  const [mockMaxAttempts, setMockMaxAttempts] = useState<number>(3);

  if (!user || !user.is_admin) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-slate-50">
        <p className="text-slate-500">Access not authorized</p>
      </div>
    );
  }

  useEffect(() => {
    setLoading(true);
    Promise.all([
      api.adminFeedbackAnalytics(),
      api.adminUsers(),
      api.adminFeedback(),
      api.adminQuestions(),
      api.skills(),
      api.adminQuestionAnalysis(),
    ]).then(([a, u, f, q, s, qa]) => {
      setAnalytics(a); setUsers(u); setFeedback(f); setQuestions(q); setSkills(s); setQuestionAnalysis(qa);
    }).catch(e => setError(e.message)).finally(() => setLoading(false));
    api.adminGetConfig().then(cfg => { if (cfg?.mock_max_attempts) setMockMaxAttempts(cfg.mock_max_attempts); }).catch(() => {});
  }, []);

  const refreshQuestions = () => api.adminQuestions().then(setQuestions);
  const saveMockConfig = async () => {
    try { await api.adminSetMockAttempts(mockMaxAttempts); } catch (e) { console.error(e); }
  };

  if (loading) return (
    <div className="min-h-screen flex items-center justify-center">
      <div className="w-8 h-8 border-3 border-amber-400 border-t-transparent rounded-full animate-spin" />
    </div>
  );

  if (error) return (
    <div className="min-h-screen flex items-center justify-center">
      <div className="bg-red-50 border border-red-200 rounded-xl p-6 text-center">
        <p className="text-red-500">{error}</p>
      </div>
    </div>
  );

  const tabs: { key: TabKey; label: string; icon: typeof BarChart3; count?: number }[] = [
    { key: 'overview', label: 'Overview', icon: BarChart3 },
    { key: 'feedback', label: 'Feedback', icon: MessageSquare, count: analytics?.total || 0 },
    { key: 'users', label: 'Users', icon: Users, count: users?.total_users || 0 },
    { key: 'questions', label: 'Question Bank', icon: BookOpen, count: questions.length },
    { key: 'mock', label: 'Mock Exam', icon: Trophy, count: users?.mock_taken || 0 },
  ];

  const ratingData = analytics ? [1,2,3,4,5].map(r => ({
    name: ratingEmojis[r], value: analytics.distribution[r] || 0, fill: ratingColors[r],
  })) : [];

  const filteredFeedback = triggerFilter ? feedback.filter(f => f.trigger === triggerFilter) : feedback;

  const filteredUsers = users?.users.filter(u =>
    !userSearch || u.name.includes(userSearch) || u.email.includes(userSearch)
  ).sort((a, b) => {
    const av = (a as Record<string, unknown>)[sortCol] ?? 0;
    const bv = (b as Record<string, unknown>)[sortCol] ?? 0;
    return sortAsc ? (av > bv ? 1 : -1) : (av < bv ? 1 : -1);
  }) || [];

  const filteredQuestions = questions
    .filter(q => !skillFilter || q.skill_id === skillFilter)
    .filter(q => !stageFilter || q.stage === stageFilter)
    .filter(q => !statusFilter || q.status === statusFilter)
    .sort((a, b) => {
      if (questionSort === 'accuracy') return a.accuracy - b.accuracy;
      if (questionSort === 'difficulty') return a.difficulty - b.difficulty;
      if (questionSort === 'times_answered') return b.times_answered - a.times_answered;
      if (questionSort === 'discrimination') return a.discrimination - b.discrimination;
      if (questionSort === 'rating') return (a.rating_overall || 0) - (b.rating_overall || 0);
      return 0;
    });
  const verbalCount = questions.filter(q => q.section === 'verbal').length;
  const quantCount = questions.filter(q => q.section === 'quantitative').length;

  const toggleSort = (col: string) => {
    if (sortCol === col) setSortAsc(!sortAsc);
    else { setSortCol(col); setSortAsc(false); }
  };

  return (
    <div className="min-h-screen bg-slate-50">
      {/* Admin Header */}
      <div className="bg-slate-800 text-white px-4 lg:px-8 py-3">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-3">
            <Shield className="w-6 h-6 text-amber-400" />
            <div>
              <h1 className="text-lg font-black">Admin Dashboard</h1>
              <p className="text-xs text-slate-400">Welcome, {user.name}</p>
            </div>
          </div>
          <div className="flex items-center gap-2">
            <button onClick={() => nav('/')}
              className="flex items-center gap-1.5 text-sm text-slate-300 hover:text-white bg-slate-700 hover:bg-slate-600 px-3 py-2 rounded-lg transition">
              <ArrowRight className="w-3.5 h-3.5" />
              <span className="hidden sm:inline">Back to App</span>
            </button>
            <button onClick={logout}
              className="flex items-center gap-1.5 text-sm text-slate-400 hover:text-red-400 bg-slate-700 hover:bg-slate-600 px-3 py-2 rounded-lg transition">
              <LogOut className="w-3.5 h-3.5" />
              <span className="hidden sm:inline">Logout</span>
            </button>
          </div>
        </div>
      </div>

      {/* Tab Bar */}
      <div className="bg-white border-b border-slate-200 px-4 lg:px-8 overflow-x-auto">
        <div className="flex gap-1">
          {tabs.map(t => {
            const Icon = t.icon;
            return (
              <button key={t.key} onClick={() => setTab(t.key)}
                className={`flex items-center gap-2 px-4 py-3 text-sm font-medium border-b-2 transition whitespace-nowrap
                  ${tab === t.key ? 'border-amber-500 text-amber-700 bg-amber-50/50' : 'border-transparent text-slate-500 hover:text-slate-700'}`}>
                <Icon className="w-4 h-4" />
                <span>{t.label}</span>
                {t.count !== undefined && (
                  <span className={`text-xs px-2 py-0.5 rounded-full ${tab === t.key ? 'bg-amber-100 text-amber-700' : 'bg-slate-100 text-slate-500'}`}>
                    {t.count}
                  </span>
                )}
              </button>
            );
          })}
        </div>
      </div>

      {/* Tab Content */}
      <div className="p-4 lg:p-8 max-w-7xl mx-auto">

        {/* Overview */}
        {tab === 'overview' && analytics && users && (
          <div className="space-y-6">
            <div className="grid grid-cols-2 lg:grid-cols-4 gap-3 lg:gap-4">
              {[
                { label: 'Total Users', value: users.total_users, icon: Users, accent: 'text-blue-600 bg-blue-50' },
                { label: 'Active Today', value: users.active_today, icon: Flame, accent: 'text-emerald-600 bg-emerald-50' },
                { label: 'Avg Rating', value: `${analytics.avg_rating}/5`, icon: Star, accent: 'text-amber-600 bg-amber-50' },
                { label: 'Completed Course', value: users.completed_course, icon: BookOpen, accent: 'text-violet-600 bg-violet-50' },
              ].map((kpi, i) => {
                const Icon = kpi.icon;
                return (
                  <div key={i} className="bg-white border border-slate-200 rounded-xl p-4">
                    <div className="flex items-center gap-3">
                      <div className={`w-10 h-10 rounded-lg flex items-center justify-center ${kpi.accent}`}>
                        <Icon className="w-5 h-5" />
                      </div>
                      <div>
                        <p className="text-2xl font-black text-slate-800">{kpi.value}</p>
                        <p className="text-xs text-slate-500">{kpi.label}</p>
                      </div>
                    </div>
                  </div>
                );
              })}
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
              <div className="bg-white border border-slate-200 rounded-xl p-5">
                <h3 className="font-bold text-slate-700 mb-4 text-sm">Rating Distribution</h3>
                <div style={{ direction: 'ltr' }}>
                  <ResponsiveContainer width="100%" height={180}>
                    <BarChart data={ratingData} layout="vertical">
                      <XAxis type="number" hide />
                      <YAxis dataKey="name" type="category" width={40} tick={{ fontSize: 20 }} />
                      <Tooltip formatter={(v: number) => [v, 'Count']} />
                      <Bar dataKey="value" radius={[0, 6, 6, 0]} barSize={24}>
                        {ratingData.map((d, i) => <Cell key={i} fill={d.fill} />)}
                      </Bar>
                    </BarChart>
                  </ResponsiveContainer>
                </div>
              </div>

              <div className="bg-white border border-slate-200 rounded-xl p-5">
                <h3 className="font-bold text-slate-700 mb-4 text-sm">Ratings by Context</h3>
                <div className="space-y-3">
                  {Object.entries(analytics.by_trigger).map(([trigger, data]) => (
                    <div key={trigger} className="flex items-center justify-between">
                      <span className="text-sm text-slate-600">{triggerLabels[trigger] || trigger}</span>
                      <div className="flex items-center gap-3">
                        <span className="text-xs text-slate-400">{data.count} rating(s)</span>
                        <div className="flex items-center gap-1">
                          <Star className="w-3.5 h-3.5 fill-amber-400 text-amber-400" />
                          <span className="text-sm font-bold text-slate-700">{data.avg_rating}</span>
                        </div>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            </div>

            <div className="grid grid-cols-2 lg:grid-cols-4 gap-3">
              {[
                { label: 'Avg Day', value: users.avg_day },
                { label: 'Avg Streak', value: users.avg_streak },
                { label: 'Total Questions', value: questions.length },
                { label: 'Total Ratings', value: analytics.total },
              ].map((s, i) => (
                <div key={i} className="bg-slate-800 text-white rounded-xl p-4 text-center">
                  <p className="text-xl font-black">{s.value}</p>
                  <p className="text-xs text-slate-400">{s.label}</p>
                </div>
              ))}
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
              <div className="bg-white border border-slate-200 rounded-2xl p-5">
                <h3 className="text-sm font-bold text-slate-700 mb-3">User Activity</h3>
                <ResponsiveContainer width="100%" height={200}>
                  <PieChart>
                    <Pie data={[
                      { name: 'Active Today', value: users?.active_today || 0, fill: '#10b981' },
                      { name: 'Inactive', value: (users?.total_users || 0) - (users?.active_today || 0), fill: '#e2e8f0' },
                    ]} cx="50%" cy="50%" innerRadius={50} outerRadius={80} dataKey="value" label={({name, value}) => `${name}: ${value}`} />
                  </PieChart>
                </ResponsiveContainer>
              </div>

              <div className="bg-white border border-slate-200 rounded-2xl p-5">
                <h3 className="text-sm font-bold text-slate-700 mb-3">Student Progress</h3>
                <ResponsiveContainer width="100%" height={200}>
                  <PieChart>
                    <Pie data={(() => {
                      const u = users?.users || [];
                      return [
                        { name: 'Not Started', value: u.filter(x => x.current_day === 0).length, fill: '#94a3b8' },
                        { name: 'Foundation (1-7)', value: u.filter(x => x.current_day >= 1 && x.current_day <= 7).length, fill: '#14b8a6' },
                        { name: 'Building (8-22)', value: u.filter(x => x.current_day >= 8 && x.current_day <= 22).length, fill: '#3b82f6' },
                        { name: 'Mastery (23-30)', value: u.filter(x => x.current_day >= 23).length, fill: '#8b5cf6' },
                      ].filter(d => d.value > 0);
                    })()} cx="50%" cy="50%" innerRadius={50} outerRadius={80} dataKey="value" label={({name, value}) => `${name}: ${value}`} />
                    <Legend />
                  </PieChart>
                </ResponsiveContainer>
              </div>
            </div>

            {analytics.recent_comments.length > 0 && (
              <div className="bg-white border border-slate-200 rounded-xl p-5">
                <h3 className="font-bold text-slate-700 mb-4 text-sm">Recent Comments</h3>
                <div className="space-y-3">
                  {analytics.recent_comments.slice(0, 5).map((c, i) => (
                    <div key={i} className="flex items-start gap-3 border-b border-slate-50 pb-3 last:border-0">
                      <span className="text-xl">{ratingEmojis[c.rating]}</span>
                      <div className="flex-1">
                        <p className="text-sm text-slate-700">{c.comment}</p>
                        <div className="flex items-center gap-2 mt-1">
                          <span className="text-xs bg-slate-100 text-slate-500 px-2 py-0.5 rounded-full">{triggerLabels[c.trigger] || c.trigger}</span>
                          <span className="text-xs text-slate-400">{new Date(c.created_at).toLocaleDateString()}</span>
                        </div>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>
        )}

        {/* Feedback */}
        {tab === 'feedback' && (
          <div className="space-y-4">
            <div className="flex items-center gap-3">
              <select value={triggerFilter} onChange={e => setTriggerFilter(e.target.value)}
                className="bg-white border border-slate-200 rounded-lg px-3 py-2 text-sm text-slate-700">
                <option value="">All Contexts</option>
                {Object.entries(triggerLabels).map(([k, v]) => <option key={k} value={k}>{v}</option>)}
              </select>
              <span className="text-xs text-slate-400">{filteredFeedback.length} feedback item(s)</span>
            </div>

            {filteredFeedback.length === 0 ? (
              <div className="bg-white border border-slate-200 rounded-xl p-10 text-center">
                <p className="text-slate-400">📭 No feedback available</p>
              </div>
            ) : (
              <div className="space-y-2">
                {filteredFeedback.map(f => (
                  <div key={f.id} className={`bg-white border rounded-xl p-4 flex items-start gap-4
                    ${f.rating <= 2 ? 'border-r-4 border-r-red-400 border-slate-200' :
                      f.rating === 3 ? 'border-r-4 border-r-amber-400 border-slate-200' :
                      'border-r-4 border-r-emerald-400 border-slate-200'}`}>
                    <div className="text-center shrink-0">
                      <span className="text-2xl">{ratingEmojis[f.rating]}</span>
                      <p className="text-xs font-bold text-slate-500">{f.rating}/5</p>
                    </div>
                    <div className="flex-1 min-w-0">
                      <p className="text-sm text-slate-700">{f.comment || <span className="text-slate-400 italic">No comment</span>}</p>
                      <div className="flex items-center gap-2 mt-2">
                        <span className="text-xs bg-amber-50 text-amber-600 px-2 py-0.5 rounded-full font-medium">{triggerLabels[f.trigger] || f.trigger}</span>
                        {f.page && <span className="text-xs bg-slate-100 text-slate-500 px-2 py-0.5 rounded-full">{f.page}</span>}
                      </div>
                    </div>
                    <span className="text-xs text-slate-400 shrink-0">{new Date(f.created_at).toLocaleDateString()}</span>
                  </div>
                ))}
              </div>
            )}
          </div>
        )}

        {/* Users */}
        {tab === 'users' && users && (
          <div className="space-y-4">
            <div className="flex items-center gap-3">
              <div className="relative flex-1 max-w-sm">
                <Search className="absolute right-3 top-1/2 -translate-y-1/2 w-4 h-4 text-slate-400" />
                <input value={userSearch} onChange={e => setUserSearch(e.target.value)}
                  placeholder="Search by name or email..."
                  className="w-full bg-white border border-slate-200 rounded-lg pr-10 pl-4 py-2 text-sm" />
              </div>
              <span className="text-xs text-slate-400">{filteredUsers.length} user(s)</span>
            </div>

            <div className="bg-white border border-slate-200 rounded-xl overflow-hidden">
              <div className="overflow-x-auto">
                <table className="w-full">
                  <thead>
                    <tr className="bg-slate-50 text-xs text-slate-500 uppercase">
                      {[
                        { key: 'name', label: 'Name' },
                        { key: 'current_day', label: 'Day' },
                        { key: 'xp', label: 'XP' },
                        { key: 'streak', label: 'Streak' },
                        { key: 'last_active', label: 'Last Active', hideOnMobile: true },
                      ].map(col => (
                        <th key={col.key} onClick={() => toggleSort(col.key)}
                          className={`px-3 lg:px-4 py-3 text-left cursor-pointer hover:bg-slate-100 transition select-none ${'hideOnMobile' in col && col.hideOnMobile ? 'hidden sm:table-cell' : ''}`}>
                          <span className="flex items-center gap-1">
                            {col.label}
                            {sortCol === col.key && (sortAsc ? <ChevronUp className="w-3 h-3" /> : <ChevronDown className="w-3 h-3" />)}
                          </span>
                        </th>
                      ))}
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-slate-100">
                    {filteredUsers.map((u, i) => (
                      <tr key={u.id} className={`hover:bg-slate-50 transition ${i % 2 === 1 ? 'bg-slate-50/50' : ''}`}>
                        <td className="px-3 lg:px-4 py-3">
                          <p className="font-medium text-sm text-slate-800">{u.name}</p>
                          <p className="text-xs text-slate-400">{u.email}</p>
                        </td>
                        <td className="px-3 lg:px-4 py-3">
                          <div className="flex items-center gap-2">
                            <div className="h-1.5 w-12 bg-slate-100 rounded-full overflow-hidden">
                              <div className="h-full bg-teal-500 rounded-full" style={{ width: `${(u.current_day / 30) * 100}%` }} />
                            </div>
                            <span className="text-xs text-slate-600 font-medium">{u.current_day}/30</span>
                          </div>
                        </td>
                        <td className="px-3 lg:px-4 py-3 text-sm font-bold text-amber-600">{u.xp.toLocaleString()}</td>
                        <td className="px-3 lg:px-4 py-3">
                          <span className={`text-sm font-medium ${u.streak >= 7 ? 'text-orange-500' : u.streak > 0 ? 'text-blue-500' : 'text-slate-400'}`}>
                            {u.streak > 0 ? `🔥 ${u.streak}` : '—'}
                          </span>
                        </td>
                        <td className="px-3 lg:px-4 py-3 text-xs text-slate-500 hidden sm:table-cell">{u.last_active || '—'}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        )}

        {/* Question Bank */}
        {tab === 'questions' && (
          <div className="space-y-4">
            <div className="grid grid-cols-3 gap-3">
              <div className="bg-white border border-slate-200 rounded-xl p-4 text-center">
                <p className="text-xl font-black text-slate-800">{questions.length}</p>
                <p className="text-xs text-slate-500">Total Questions</p>
              </div>
              <div className="bg-blue-50 border border-blue-200 rounded-xl p-4 text-center">
                <p className="text-xl font-black text-blue-700">{verbalCount}</p>
                <p className="text-xs text-blue-500">📖 Verbal</p>
              </div>
              <div className="bg-violet-50 border border-violet-200 rounded-xl p-4 text-center">
                <p className="text-xl font-black text-violet-700">{quantCount}</p>
                <p className="text-xs text-violet-500">🔢 Quant</p>
              </div>
            </div>

            {questionAnalysis && (
              <div className="grid grid-cols-1 lg:grid-cols-3 gap-4">
                {/* Stage Distribution Pie */}
                <div className="bg-white border border-slate-200 rounded-2xl p-5">
                  <h3 className="text-sm font-bold text-slate-700 mb-3">Stage Distribution</h3>
                  <ResponsiveContainer width="100%" height={200}>
                    <PieChart>
                      <Pie data={Object.entries(questionAnalysis.by_stage).map(([k, v]) => ({
                        name: k === 'diagnostic' ? 'Diagnostic' : k === 'foundation' ? 'Foundation' : k === 'building' ? 'Building' : k === 'peak' ? 'Mastery' : k === 'mock' ? 'Mock' : 'General',
                        value: v,
                        fill: k === 'diagnostic' ? '#06b6d4' : k === 'foundation' ? '#10b981' : k === 'building' ? '#f59e0b' : k === 'peak' ? '#ef4444' : k === 'mock' ? '#8b5cf6' : '#94a3b8',
                      }))} cx="50%" cy="50%" outerRadius={70} dataKey="value" label={({name, value}) => `${name}: ${value}`} />
                    </PieChart>
                  </ResponsiveContainer>
                </div>

                {/* Skill Distribution Bar */}
                <div className="bg-white border border-slate-200 rounded-2xl p-5">
                  <h3 className="text-sm font-bold text-slate-700 mb-3">Questions by Skill</h3>
                  <ResponsiveContainer width="100%" height={200}>
                    <BarChart data={Object.entries(questionAnalysis.by_skill).map(([k, v]) => ({
                      name: k.replace('verbal_', '').replace('quant_', '').slice(0, 6),
                      count: v,
                      fill: k.startsWith('verbal') ? '#3b82f6' : '#8b5cf6',
                    }))} layout="vertical">
                      <XAxis type="number" />
                      <YAxis type="category" dataKey="name" width={50} tick={{fontSize: 10}} />
                      <Tooltip />
                      <Bar dataKey="count" radius={[0, 4, 4, 0]}>
                        {Object.entries(questionAnalysis.by_skill).map(([k], i) => (
                          <Cell key={i} fill={k.startsWith('verbal') ? '#3b82f6' : '#8b5cf6'} />
                        ))}
                      </Bar>
                    </BarChart>
                  </ResponsiveContainer>
                </div>

                {/* Quality Rating Radar */}
                <div className="bg-white border border-slate-200 rounded-2xl p-5">
                  <h3 className="text-sm font-bold text-slate-700 mb-3">Average Question Quality</h3>
                  <ResponsiveContainer width="100%" height={200}>
                    <RadarChart data={(() => {
                      const qs = questions;
                      const avg = (field: string) => {
                        const vals = qs.map(q => (q as any)[field]).filter(Boolean);
                        return vals.length ? +(vals.reduce((a: number, b: number) => a + b, 0) / vals.length).toFixed(1) : 0;
                      };
                      return [
                        { subject: 'Clarity', value: avg('rating_clarity'), fullMark: 5 },
                        { subject: 'Cognitive', value: avg('rating_cognitive'), fullMark: 5 },
                        { subject: 'Distractors', value: avg('rating_distractors'), fullMark: 5 },
                        { subject: 'Difficulty', value: avg('rating_difficulty_align'), fullMark: 5 },
                        { subject: 'Explanation', value: avg('rating_explanation'), fullMark: 5 },
                        { subject: 'Fairness', value: avg('rating_fairness'), fullMark: 5 },
                        { subject: 'Discrimination', value: avg('rating_discrimination'), fullMark: 5 },
                      ];
                    })()}>
                      <PolarGrid />
                      <PolarAngleAxis dataKey="subject" tick={{fontSize: 11}} />
                      <PolarRadiusAxis angle={90} domain={[0, 5]} tick={{fontSize: 9}} />
                      <Radar dataKey="value" stroke="#0d9488" fill="#0d9488" fillOpacity={0.3} />
                    </RadarChart>
                  </ResponsiveContainer>
                </div>
              </div>
            )}

            {/* Flagged Questions Alert */}
            {questionAnalysis && questionAnalysis.flagged_count > 0 && (
              <div className="bg-amber-50 border border-amber-200 rounded-2xl p-4">
                <div className="flex items-center gap-2 mb-2">
                  <AlertTriangle className="w-5 h-5 text-amber-600" />
                  <h3 className="text-sm font-bold text-amber-700">{questionAnalysis.flagged_count} question(s) need review</h3>
                </div>
                <div className="flex flex-wrap gap-2">
                  {questionAnalysis.flagged.slice(0, 10).map(f => (
                    <span key={f.id} className="bg-white border border-amber-300 rounded-lg px-3 py-1 text-xs text-amber-700">
                      #{f.id} — {f.issues.join(', ')}
                    </span>
                  ))}
                  {questionAnalysis.flagged_count > 10 && <span className="text-xs text-amber-500">+{questionAnalysis.flagged_count - 10} more</span>}
                </div>
              </div>
            )}

            <div className="flex items-center gap-2 flex-wrap">
              <select value={skillFilter} onChange={e => setSkillFilter(e.target.value)}
                className="bg-white border border-slate-200 rounded-lg px-3 py-2 text-sm text-slate-700">
                <option value="">All Skills</option>
                {skills.map(s => <option key={s.id} value={s.id}>{s.icon} {s.name_ar}</option>)}
              </select>
              <select value={stageFilter} onChange={e => setStageFilter(e.target.value)}
                className="bg-white border border-slate-200 rounded-lg px-3 py-2 text-sm text-slate-700">
                <option value="">All Stages</option>
                <option value="diagnostic">Diagnostic</option>
                <option value="foundation">Foundation</option>
                <option value="building">Building</option>
                <option value="peak">Mastery</option>
                <option value="mock">Mock Exam</option>
                <option value="general">General</option>
              </select>
              <select value={statusFilter} onChange={e => setStatusFilter(e.target.value)}
                className="bg-white border border-slate-200 rounded-lg px-3 py-2 text-sm text-slate-700">
                <option value="">All Statuses</option>
                <option value="active">Active</option>
                <option value="review">Review</option>
                <option value="disabled">Disabled</option>
              </select>
              <select value={questionSort} onChange={e => setQuestionSort(e.target.value)}
                className="bg-white border border-slate-200 rounded-lg px-3 py-2 text-sm text-slate-700">
                <option value="">Default Sort</option>
                <option value="accuracy">Accuracy</option>
                <option value="difficulty">Difficulty</option>
                <option value="times_answered">Most Answered</option>
                <option value="discrimination">Discrimination</option>
                <option value="rating">Rating</option>
              </select>
              <span className="text-xs text-slate-400 flex-1">{filteredQuestions.length} question(s)</span>
              <button onClick={async () => {
                const result = await fetch('/api/admin/questions/calibrate?dry_run=true', {
                  method: 'POST', headers: { 'Authorization': `Bearer ${localStorage.getItem('gat_token')}` }
                }).then(r => r.json());
                if (result.calibrated === 0) { alert(`No questions need calibration (need at least ${10}+ answers)`); return; }
                if (confirm(`Calibrate ${result.calibrated} question(s)? (${result.skipped} skipped)`)) {
                  await fetch('/api/admin/questions/calibrate', {
                    method: 'POST', headers: { 'Authorization': `Bearer ${localStorage.getItem('gat_token')}` }
                  });
                  await refreshQuestions();
                }
              }}
                className="flex items-center gap-1.5 bg-teal-600 hover:bg-teal-700 text-white text-sm font-bold px-3 py-2 rounded-lg transition">
                Calibrate Difficulty
              </button>
              <button onClick={() => { setEditQ(null); setShowAddQ(true); }}
                className="flex items-center gap-1.5 bg-amber-500 hover:bg-amber-600 text-white text-sm font-bold px-4 py-2 rounded-lg transition">
                <Plus className="w-4 h-4" /> Add Question
              </button>
            </div>

            <div className="space-y-2">
              {filteredQuestions.map(q => (
                <div key={q.id} className="bg-white border border-slate-200 rounded-xl overflow-hidden">
                  <button onClick={() => setExpandedQ(expandedQ === q.id ? null : q.id)}
                    className="w-full px-4 py-3 flex items-center gap-3 hover:bg-slate-50 transition text-left">
                    <span className="text-xs font-bold text-slate-400 shrink-0">#{q.id}</span>
                    <span className={`text-xs px-2 py-0.5 rounded-full shrink-0 ${q.section === 'verbal' ? 'bg-blue-100 text-blue-600' : 'bg-violet-100 text-violet-600'}`}>
                      {q.skill_name_ar}
                    </span>
                    <span className={`text-xs px-1.5 py-0.5 rounded shrink-0 ${
                      q.stage === 'diagnostic' ? 'bg-cyan-100 text-cyan-700' :
                      q.stage === 'foundation' ? 'bg-emerald-100 text-emerald-700' :
                      q.stage === 'building' ? 'bg-amber-100 text-amber-700' :
                      q.stage === 'peak' ? 'bg-red-100 text-red-700' :
                      q.stage === 'mock' ? 'bg-purple-100 text-purple-700' :
                      'bg-slate-100 text-slate-500'
                    }`}>{q.stage}</span>
                    <span className="flex-1 text-sm text-slate-700 truncate">{q.text_ar}</span>
                    <div className="flex items-center gap-2 shrink-0">
                      <div className="h-1.5 w-10 bg-slate-100 rounded-full overflow-hidden" title={`Difficulty ${q.difficulty}`}>
                        <div className={`h-full rounded-full ${q.difficulty < 0.4 ? 'bg-emerald-400' : q.difficulty < 0.7 ? 'bg-amber-400' : 'bg-red-400'}`}
                          style={{ width: `${q.difficulty * 100}%` }} />
                      </div>
                      {q.rating_overall && <span className={`text-xs font-bold ${q.rating_overall >= 4.5 ? 'text-emerald-500' : q.rating_overall >= 3.5 ? 'text-teal-500' : q.rating_overall >= 3 ? 'text-amber-500' : 'text-red-500'}`}>★{q.rating_overall.toFixed(1)}</span>}
                      {q.times_answered > 0 && <span className="text-xs text-slate-400">{Math.round(q.accuracy * 100)}٪</span>}
                      {q.status === 'review' && <span className="text-xs text-amber-500">Review</span>}
                      {q.status === 'disabled' && <span className="text-xs text-red-500">Disabled</span>}
                      {expandedQ === q.id ? <ChevronUp className="w-4 h-4 text-slate-400" /> : <ChevronDown className="w-4 h-4 text-slate-400" />}
                    </div>
                  </button>

                  {expandedQ === q.id && (
                    <div className="border-t border-slate-100 p-4 bg-slate-50/50 space-y-3">
                      {q.passage_ar && (
                        <div className="bg-white border border-slate-200 rounded-lg p-3 text-sm text-slate-600">{q.passage_ar}</div>
                      )}
                      <p className="text-sm text-slate-800 font-medium whitespace-pre-line">{q.text_ar}</p>
                      <div className="grid grid-cols-2 gap-2">
                        {(['a','b','c','d'] as const).map(key => (
                          <div key={key} className={`border rounded-lg p-2.5 text-sm
                            ${key === q.correct_option ? 'border-emerald-400 bg-emerald-50 text-emerald-700' : 'border-slate-200 text-slate-600'}`}>
                            <span className="font-bold ml-1">{key === 'a' ? 'A' : key === 'b' ? 'B' : key === 'c' ? 'C' : 'D'}.</span>
                            {q[`option_${key}` as keyof AdminQuestion] as string}
                          </div>
                        ))}
                      </div>
                      {q.explanation_ar && (
                        <div className="bg-amber-50 border border-amber-200 rounded-lg p-3 text-sm text-amber-700">
                          <p className="font-bold mb-1">Explanation:</p>
                          <p className="whitespace-pre-line">{q.explanation_ar}</p>
                        </div>
                      )}
                      {q.tags && (
                        <div className="flex flex-wrap gap-1">
                          {q.tags.split(',').map((tag, i) => (
                            <span key={i} className="bg-slate-100 text-slate-500 text-xs px-2 py-0.5 rounded-full">{tag.trim()}</span>
                          ))}
                        </div>
                      )}
                      <div className="flex items-center gap-2 text-xs text-slate-500 flex-wrap">
                        <span>Answered: {q.times_answered}</span>
                        <span>•</span>
                        <span>Accuracy: {Math.round(q.accuracy * 100)}%</span>
                        <span>•</span>
                        <span>Avg Time: {q.avg_time_seconds?.toFixed(0) || 0}s</span>
                        <span>•</span>
                        <span>Discrimination: {q.discrimination?.toFixed(2) || '0.00'}</span>
                        {q.original_difficulty != null && q.original_difficulty !== q.difficulty && (
                          <>
                            <span>•</span>
                            <span className="text-amber-600">Original Difficulty: {q.original_difficulty.toFixed(2)} ← Calibrated: {q.difficulty.toFixed(2)}</span>
                          </>
                        )}
                        <span className="flex-1" />
                        <button onClick={() => { setEditQ(q); setShowAddQ(true); }}
                          className="flex items-center gap-1 text-blue-600 hover:text-blue-700 font-medium">
                          <Pencil className="w-3.5 h-3.5" /> Edit
                        </button>
                        <button onClick={async () => {
                          if (!confirm('Are you sure you want to delete this question?')) return;
                          await api.adminDeleteQuestion(q.id);
                          await refreshQuestions();
                          setExpandedQ(null);
                        }}
                          className="flex items-center gap-1 text-red-500 hover:text-red-600 font-medium">
                          <Trash2 className="w-3.5 h-3.5" /> Delete
                        </button>
                      </div>
                    </div>
                  )}
                </div>
              ))}
            </div>
          </div>
        )}
        {/* Mock Exam Results */}
        {tab === 'mock' && users && (
          <div className="space-y-6">
            {/* Preview Button */}
            <div className="flex items-center justify-between">
              <div>
                <h3 className="font-bold text-slate-800">Final Mock Exam</h3>
                <p className="text-xs text-slate-500">65 questions • 70 minutes • Verbal + Quant</p>
              </div>
              <a href="/mock?preview=true"
                className="flex items-center gap-2 bg-amber-500 hover:bg-amber-600 text-white text-sm font-bold px-5 py-2.5 rounded-lg transition">
                <Trophy className="w-4 h-4" />
                Preview Exam
              </a>
            </div>

            {/* Config */}
            <div className="bg-white border border-slate-200 rounded-xl p-4 flex items-center justify-between">
              <div>
                <p className="font-bold text-slate-700 text-sm">Max Attempts</p>
                <p className="text-xs text-slate-500">Number of attempts allowed per student</p>
              </div>
              <div className="flex items-center gap-2">
                <input type="number" min="1" max="10" value={mockMaxAttempts} onChange={e => setMockMaxAttempts(Number(e.target.value))}
                  className="w-16 border border-slate-200 rounded-lg px-2 py-1.5 text-center text-sm" />
                <button onClick={saveMockConfig} className="bg-amber-500 hover:bg-amber-600 text-white text-xs font-bold px-3 py-1.5 rounded-lg">
                  Save
                </button>
              </div>
            </div>

            {/* Mock Stats */}
            <div className="grid grid-cols-2 lg:grid-cols-4 gap-3">
              <div className="bg-white border border-slate-200 rounded-xl p-4">
                <div className="flex items-center gap-3">
                  <div className="w-10 h-10 rounded-lg flex items-center justify-center bg-amber-50 text-amber-600">
                    <Trophy className="w-5 h-5" />
                  </div>
                  <div>
                    <p className="text-2xl font-black text-slate-800">{users.mock_taken}</p>
                    <p className="text-xs text-slate-500">Completed Exam</p>
                  </div>
                </div>
              </div>
              <div className="bg-white border border-slate-200 rounded-xl p-4">
                <div className="flex items-center gap-3">
                  <div className="w-10 h-10 rounded-lg flex items-center justify-center bg-blue-50 text-blue-600">
                    <Star className="w-5 h-5" />
                  </div>
                  <div>
                    <p className="text-2xl font-black text-slate-800">{users.mock_avg_score || '—'}</p>
                    <p className="text-xs text-slate-500">Average Score</p>
                  </div>
                </div>
              </div>
              <div className="bg-white border border-slate-200 rounded-xl p-4">
                <div className="flex items-center gap-3">
                  <div className="w-10 h-10 rounded-lg flex items-center justify-center bg-emerald-50 text-emerald-600">
                    <Users className="w-5 h-5" />
                  </div>
                  <div>
                    <p className="text-2xl font-black text-slate-800">{users.users.filter(u => u.mock_attempts > 0 && u.mock_score >= 65).length}</p>
                    <p className="text-xs text-slate-500">Passed (65+)</p>
                  </div>
                </div>
              </div>
              <div className="bg-white border border-slate-200 rounded-xl p-4">
                <div className="flex items-center gap-3">
                  <div className="w-10 h-10 rounded-lg flex items-center justify-center bg-violet-50 text-violet-600">
                    <Users className="w-5 h-5" />
                  </div>
                  <div>
                    <p className="text-2xl font-black text-slate-800">{users.users.filter(u => u.mock_attempts > 0 && u.mock_score >= 80).length}</p>
                    <p className="text-xs text-slate-500">Excellent (80+)</p>
                  </div>
                </div>
              </div>
            </div>

            {/* Score distribution */}
            {users.mock_taken > 0 && (
              <div className="bg-white border border-slate-200 rounded-2xl p-5">
                <h3 className="text-sm font-bold text-slate-700 mb-3">Score Distribution</h3>
                <ResponsiveContainer width="100%" height={200}>
                  <BarChart data={(() => {
                    const mockUsers = (users?.users || []).filter(u => u.mock_attempts > 0);
                    return [
                      { range: '< 50', count: mockUsers.filter(u => u.mock_score < 50).length, fill: '#ef4444' },
                      { range: '50-64', count: mockUsers.filter(u => u.mock_score >= 50 && u.mock_score < 65).length, fill: '#f59e0b' },
                      { range: '65-79', count: mockUsers.filter(u => u.mock_score >= 65 && u.mock_score < 80).length, fill: '#3b82f6' },
                      { range: '80+', count: mockUsers.filter(u => u.mock_score >= 80).length, fill: '#10b981' },
                    ];
                  })()}>
                    <XAxis dataKey="range" />
                    <YAxis allowDecimals={false} />
                    <Tooltip />
                    <Bar dataKey="count" radius={[8, 8, 0, 0]}>
                      {[0,1,2,3].map(i => <Cell key={i} fill={['#ef4444','#f59e0b','#3b82f6','#10b981'][i]} />)}
                    </Bar>
                  </BarChart>
                </ResponsiveContainer>
              </div>
            )}

            {/* Users who took the mock */}
            <div className="bg-white border border-slate-200 rounded-xl overflow-hidden">
              <div className="px-4 py-3 border-b border-slate-100">
                <h3 className="font-bold text-slate-700 text-sm">Student Results</h3>
              </div>
              <div className="overflow-x-auto">
                <table className="w-full">
                  <thead>
                    <tr className="bg-slate-50 text-xs text-slate-500 uppercase">
                      <th className="px-4 py-3 text-left">Student</th>
                      <th className="px-4 py-3 text-left">Day</th>
                      <th className="px-4 py-3 text-left">Status</th>
                      <th className="px-4 py-3 text-left">Score</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-slate-100">
                    {users.users.filter(u => u.current_day >= 25).map((u, i) => (
                      <tr key={u.id} className={`hover:bg-slate-50 ${i % 2 === 1 ? 'bg-slate-50/50' : ''}`}>
                        <td className="px-4 py-3">
                          <p className="font-medium text-sm text-slate-800">{u.name}</p>
                          <p className="text-xs text-slate-400">{u.email}</p>
                        </td>
                        <td className="px-4 py-3 text-sm text-slate-600">{u.current_day}/30</td>
                        <td className="px-4 py-3">
                          {u.mock_attempts > 0 ? (
                            <span className="text-xs bg-emerald-100 text-emerald-700 px-2 py-1 rounded-full font-medium">Completed ({u.mock_attempts} attempts)</span>
                          ) : (
                            <span className="text-xs bg-slate-100 text-slate-500 px-2 py-1 rounded-full">Not Started</span>
                          )}
                        </td>
                        <td className="px-4 py-3">
                          {u.mock_attempts > 0 ? (
                            <span className={`text-lg font-black ${u.mock_score >= 80 ? 'text-emerald-600' : u.mock_score >= 65 ? 'text-blue-600' : u.mock_score >= 50 ? 'text-amber-600' : 'text-red-500'}`}>
                              {u.mock_score}
                            </span>
                          ) : (
                            <span className="text-slate-400">—</span>
                          )}
                        </td>
                      </tr>
                    ))}
                    {users.users.filter(u => u.current_day >= 25).length === 0 && (
                      <tr>
                        <td colSpan={4} className="px-4 py-8 text-center text-slate-400 text-sm">
                          No students have reached the mock exam stage yet
                        </td>
                      </tr>
                    )}
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        )}
      </div>

      {/* Add/Edit Question Modal */}
      {showAddQ && (
        <QuestionModal
          question={editQ}
          skills={skills}
          onClose={() => { setShowAddQ(false); setEditQ(null); }}
          onSave={async (payload) => {
            if (editQ) await api.adminUpdateQuestion(editQ.id, payload);
            else await api.adminAddQuestion(payload);
            await refreshQuestions();
            setShowAddQ(false);
            setEditQ(null);
          }}
        />
      )}
    </div>
  );
}

function QuestionModal({ question, skills, onClose, onSave }: {
  question: AdminQuestion | null; skills: ApiSkill[];
  onClose: () => void; onSave: (p: QuestionPayload) => Promise<void>;
}) {
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState('');
  const [form, setForm] = useState<QuestionPayload>({
    skill_id: question?.skill_id || skills[0]?.id || '',
    question_type: question?.question_type || 'reading',
    difficulty: question?.difficulty || 0.5,
    text_ar: question?.text_ar || '',
    passage_ar: question?.passage_ar || null,
    option_a: question?.option_a || '', option_b: question?.option_b || '',
    option_c: question?.option_c || '', option_d: question?.option_d || '',
    correct_option: question?.correct_option || 'a',
    explanation_ar: question?.explanation_ar || null,
    solution_steps_ar: null,
  });

  const update = (field: string, value: unknown) => setForm(prev => ({ ...prev, [field]: value }));

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setSaving(true); setError('');
    try { await onSave(form); }
    catch (err: unknown) { setError(err instanceof Error ? err.message : 'حدث خطأ'); }
    finally { setSaving(false); }
  };

  const qTypes = [
    { v: 'reading', l: 'Reading Comprehension' }, { v: 'analogy', l: 'Verbal Analogy' },
    { v: 'completion', l: 'Sentence Completion' }, { v: 'error', l: 'Contextual Error' },
    { v: 'oddword', l: 'Odd Word' }, { v: 'arithmetic', l: 'Arithmetic' },
    { v: 'geometry', l: 'Geometry' }, { v: 'algebra', l: 'Algebra' },
    { v: 'statistics', l: 'Statistics' }, { v: 'comparison', l: 'Comparison' },
  ];

  return (
    <div className="fixed inset-0 bg-slate-900/50 backdrop-blur-sm flex items-start justify-center z-50 p-4 overflow-y-auto">
      <div className="bg-white rounded-2xl shadow-2xl w-full max-w-2xl my-8">
        <div className="flex items-center justify-between p-5 border-b border-slate-100">
          <h3 className="font-bold text-slate-800">{question ? 'Edit Question' : 'Add New Question'}</h3>
          <button onClick={onClose} className="text-slate-400 hover:text-slate-600"><X className="w-5 h-5" /></button>
        </div>
        <form onSubmit={handleSubmit} className="p-5 space-y-4">
          <div className="grid grid-cols-2 gap-3">
            <div>
              <label className="text-xs font-medium text-slate-600 mb-1 block">Skill</label>
              <select value={form.skill_id} onChange={e => update('skill_id', e.target.value)}
                className="w-full border border-slate-200 rounded-lg px-3 py-2 text-sm">
                {skills.map(s => <option key={s.id} value={s.id}>{s.icon} {s.name_ar}</option>)}
              </select>
            </div>
            <div>
              <label className="text-xs font-medium text-slate-600 mb-1 block">Question Type</label>
              <select value={form.question_type} onChange={e => update('question_type', e.target.value)}
                className="w-full border border-slate-200 rounded-lg px-3 py-2 text-sm">
                {qTypes.map(t => <option key={t.v} value={t.v}>{t.l}</option>)}
              </select>
            </div>
          </div>
          <div>
            <label className="text-xs font-medium text-slate-600 mb-1 block">Difficulty: {form.difficulty}</label>
            <input type="range" min="0" max="1" step="0.1" value={form.difficulty}
              onChange={e => update('difficulty', parseFloat(e.target.value))} className="w-full accent-amber-500" />
            <div className="flex justify-between text-xs text-slate-400"><span>Easy</span><span>Medium</span><span>Hard</span></div>
          </div>
          <div>
            <label className="text-xs font-medium text-slate-600 mb-1 block">Passage Text (optional)</label>
            <textarea value={form.passage_ar || ''} onChange={e => update('passage_ar', e.target.value || null)}
              rows={2} className="w-full border border-slate-200 rounded-lg px-3 py-2 text-sm resize-none" />
          </div>
          <div>
            <label className="text-xs font-medium text-slate-600 mb-1 block">Question Text *</label>
            <textarea value={form.text_ar} onChange={e => update('text_ar', e.target.value)}
              rows={3} className="w-full border border-slate-200 rounded-lg px-3 py-2 text-sm resize-none" required />
          </div>
          <div className="grid grid-cols-2 gap-3">
            {[{ k: 'option_a', l: 'أ' }, { k: 'option_b', l: 'ب' }, { k: 'option_c', l: 'ج' }, { k: 'option_d', l: 'د' }].map(opt => (
              <div key={opt.k}>
                <label className="text-xs font-medium text-slate-600 mb-1 flex items-center gap-1">
                  <input type="radio" name="correct" value={opt.k.slice(-1)}
                    checked={form.correct_option === opt.k.slice(-1)}
                    onChange={() => update('correct_option', opt.k.slice(-1))} className="accent-emerald-500" />
                  Option {opt.l} {form.correct_option === opt.k.slice(-1) && <span className="text-emerald-500 text-[10px]">(Correct)</span>}
                </label>
                <input value={(form as unknown as Record<string, string>)[opt.k] || ''}
                  onChange={e => update(opt.k, e.target.value)}
                  className="w-full border border-slate-200 rounded-lg px-3 py-2 text-sm" required />
              </div>
            ))}
          </div>
          <div>
            <label className="text-xs font-medium text-slate-600 mb-1 block">Explanation (optional)</label>
            <textarea value={form.explanation_ar || ''} onChange={e => update('explanation_ar', e.target.value || null)}
              rows={2} className="w-full border border-slate-200 rounded-lg px-3 py-2 text-sm resize-none" />
          </div>
          {error && <p className="text-sm text-red-500 bg-red-50 rounded-lg p-2 text-center">{error}</p>}
          <div className="flex gap-3 pt-2">
            <button type="button" onClick={onClose} className="flex-1 text-slate-500 text-sm font-medium py-2.5 hover:text-slate-700">Cancel</button>
            <button type="submit" disabled={saving}
              className="flex-1 bg-amber-500 hover:bg-amber-600 text-white font-bold py-2.5 rounded-xl transition disabled:opacity-50">
              {saving ? '...' : question ? 'Save Changes' : 'Add Question'}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
