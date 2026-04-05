import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '@/hooks/useAuth';
import { api } from '@/lib/api';
import { QuestionOptions } from '@/components/questions/QuestionOptions';
import { QuestionPrompt } from '@/components/questions/QuestionPrompt';
import { defaultQuestionAppearance, validateMarkdownMathFields } from '@/lib/questionPresentation';
import { parseTableEditorValue, sanitizeInlineSvg } from '@/lib/questionVisuals';
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
const questionRatingMetrics = [
  { subject: 'Clarity', field: 'rating_clarity' },
  { subject: 'Cognitive', field: 'rating_cognitive' },
  { subject: 'Distractors', field: 'rating_distractors' },
  { subject: 'Difficulty', field: 'rating_difficulty_align' },
  { subject: 'Explanation', field: 'rating_explanation' },
  { subject: 'Fairness', field: 'rating_fairness' },
  { subject: 'Discrimination', field: 'rating_discrimination' },
] as const;

type QuestionRatingField = typeof questionRatingMetrics[number]['field'];

const contentClassificationLabels: Record<string, string> = {
  ready: 'Ready',
  'safe-to-auto-convert': 'Safe Auto-Fix',
  'needs-manual-cleanup': 'Manual Cleanup',
  'content-corrupted': 'Corrupted',
};

const recommendedActionLabels: Record<string, string> = {
  'keep-active': 'Keep Active',
  'auto-fix-and-sync': 'Auto-Fix + Sync',
  'manual-review': 'Manual Review',
  'keep-in-review': 'Keep in Review',
};

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
  const [batchFilter, setBatchFilter] = useState('');
  const [authoringSourceFilter, setAuthoringSourceFilter] = useState('');
  const [variantGroupFilter, setVariantGroupFilter] = useState('');
  const [classificationFilter, setClassificationFilter] = useState('');
  const [issueCodeFilter, setIssueCodeFilter] = useState('');
  const [ratingsFilter, setRatingsFilter] = useState('');
  const [analyticsRiskFilter, setAnalyticsRiskFilter] = useState('');
  const [questionSort, setQuestionSort] = useState('');
  const [expandedQ, setExpandedQ] = useState<number | null>(null);
  const [showAddQ, setShowAddQ] = useState(false);
  const [editQ, setEditQ] = useState<AdminQuestion | null>(null);
  const [sortCol, setSortCol] = useState<string>('current_day');
  const [sortAsc, setSortAsc] = useState(false);
  const [mockMaxAttempts, setMockMaxAttempts] = useState<number>(3);

  useEffect(() => {
    if (!user?.is_admin) {
      setLoading(false);
      return;
    }
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
  }, [user?.is_admin]);

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
    .filter(q => !batchFilter || q.batch_id === batchFilter)
    .filter(q => !authoringSourceFilter || (q.authoring_source || 'human') === authoringSourceFilter)
    .filter(q => !variantGroupFilter || q.variant_group === variantGroupFilter)
    .filter(q => !classificationFilter || q.content_classification === classificationFilter)
    .filter(q => !issueCodeFilter || !!q.content_issues?.some(issue => issue.code === issueCodeFilter))
    .filter(q => !ratingsFilter || (ratingsFilter === 'complete' ? q.ratings_complete : !q.ratings_complete))
    .filter(q => !analyticsRiskFilter || !!q.analytics_flags?.includes(analyticsRiskFilter))
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
  const reviewReadyCount = questions.filter(q => q.ratings_complete).length;
  const batchOptions = Array.from(
    new Set(questions.map((question) => question.batch_id).filter((value): value is string => Boolean(value))),
  ).sort();
  const authoringSourceOptions = Array.from(
    new Set(questions.map((question) => question.authoring_source || 'human')),
  ).sort();
  const variantGroupOptions = Array.from(
    new Set(questions.map((question) => question.variant_group).filter((value): value is string => Boolean(value))),
  ).sort();
  const issueCodeOptions = Array.from(
    new Set(
      questions.flatMap((question) => question.content_issues?.map((issue) => issue.code) || []),
    ),
  ).sort();

  const toggleSort = (col: string) => {
    if (sortCol === col) setSortAsc(!sortAsc);
    else { setSortCol(col); setSortAsc(false); }
  };

  const averageQuestionRating = (field: QuestionRatingField) => {
    const values = questions
      .map((question) => question[field])
      .filter((value): value is number => typeof value === 'number');

    if (!values.length) return 0;
    return +(values.reduce((sum, value) => sum + value, 0) / values.length).toFixed(1);
  };

  if (!user || !user.is_admin) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-slate-50 dark:bg-slate-950" data-testid="admin-page">
        <p className="text-slate-500 dark:text-slate-400">Access not authorized</p>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-slate-50 text-slate-800 dark:bg-slate-950 dark:text-slate-100" data-testid="admin-page">
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
      <div className="bg-white border-b border-slate-200 px-4 lg:px-8 overflow-x-auto dark:border-slate-800 dark:bg-slate-950">
        <div className="flex gap-1">
          {tabs.map(t => {
            const Icon = t.icon;
            return (
              <button key={t.key} onClick={() => setTab(t.key)} data-testid={`admin-tab-${t.key}`}
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
                  <div key={i} className="bg-white border border-slate-200 rounded-xl p-4 dark:bg-slate-900 dark:border-slate-800">
                    <div className="flex items-center gap-3">
                      <div className={`w-10 h-10 rounded-lg flex items-center justify-center ${kpi.accent}`}>
                        <Icon className="w-5 h-5" />
                      </div>
                      <div>
                        <p className="text-2xl font-black text-slate-800 dark:text-slate-100">{kpi.value}</p>
                        <p className="text-xs text-slate-500">{kpi.label}</p>
                      </div>
                    </div>
                  </div>
                );
              })}
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
              <div className="bg-white border border-slate-200 rounded-xl p-5 dark:bg-slate-900 dark:border-slate-800">
                <h3 className="font-bold text-slate-700 mb-4 text-sm dark:text-slate-200">Rating Distribution</h3>
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

              <div className="bg-white border border-slate-200 rounded-xl p-5 dark:bg-slate-900 dark:border-slate-800">
                <h3 className="font-bold text-slate-700 mb-4 text-sm dark:text-slate-200">Ratings by Context</h3>
                <div className="space-y-3">
                  {Object.entries(analytics.by_trigger).map(([trigger, data]) => (
                    <div key={trigger} className="flex items-center justify-between">
                      <span className="text-sm text-slate-600 dark:text-slate-400">{triggerLabels[trigger] || trigger}</span>
                      <div className="flex items-center gap-3">
                        <span className="text-xs text-slate-400">{data.count} rating(s)</span>
                        <div className="flex items-center gap-1">
                          <Star className="w-3.5 h-3.5 fill-amber-400 text-amber-400" />
                          <span className="text-sm font-bold text-slate-700 dark:text-slate-200">{data.avg_rating}</span>
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
              <div className="bg-white border border-slate-200 rounded-2xl p-5 dark:bg-slate-900 dark:border-slate-800">
                <h3 className="text-sm font-bold text-slate-700 mb-3 dark:text-slate-200">User Activity</h3>
                <ResponsiveContainer width="100%" height={200}>
                  <PieChart>
                    <Pie data={[
                      { name: 'Active Today', value: users?.active_today || 0, fill: '#10b981' },
                      { name: 'Inactive', value: (users?.total_users || 0) - (users?.active_today || 0), fill: '#e2e8f0' },
                    ]} cx="50%" cy="50%" innerRadius={50} outerRadius={80} dataKey="value" label={({name, value}) => `${name}: ${value}`} />
                  </PieChart>
                </ResponsiveContainer>
              </div>

              <div className="bg-white border border-slate-200 rounded-2xl p-5 dark:bg-slate-900 dark:border-slate-800">
                <h3 className="text-sm font-bold text-slate-700 mb-3 dark:text-slate-200">Student Progress</h3>
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
              <div className="bg-white border border-slate-200 rounded-xl p-5 dark:bg-slate-900 dark:border-slate-800">
                <h3 className="font-bold text-slate-700 mb-4 text-sm dark:text-slate-200">Recent Comments</h3>
                <div className="space-y-3">
                  {analytics.recent_comments.slice(0, 5).map((c, i) => (
                    <div key={i} className="flex items-start gap-3 border-b border-slate-50 pb-3 last:border-0">
                      <span className="text-xl">{ratingEmojis[c.rating]}</span>
                      <div className="flex-1">
                        <p className="text-sm text-slate-700 dark:text-slate-300">{c.comment}</p>
                        <div className="flex items-center gap-2 mt-1">
                          <span className="text-xs bg-slate-100 text-slate-500 px-2 py-0.5 rounded-full dark:bg-slate-800 dark:text-slate-400">{triggerLabels[c.trigger] || c.trigger}</span>
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
                className="bg-white border border-slate-200 rounded-lg px-3 py-2 text-sm text-slate-700 dark:bg-slate-900 dark:border-slate-700 dark:text-slate-300">
                <option value="">All Contexts</option>
                {Object.entries(triggerLabels).map(([k, v]) => <option key={k} value={k}>{v}</option>)}
              </select>
              <span className="text-xs text-slate-400">{filteredFeedback.length} feedback item(s)</span>
            </div>

            {filteredFeedback.length === 0 ? (
              <div className="bg-white border border-slate-200 rounded-xl p-10 text-center dark:bg-slate-900 dark:border-slate-800">
                <p className="text-slate-400">📭 No feedback available</p>
              </div>
            ) : (
              <div className="space-y-2">
                {filteredFeedback.map(f => (
                  <div key={f.id} className={`bg-white border rounded-xl p-4 flex items-start gap-4 dark:bg-slate-900
                    ${f.rating <= 2 ? 'border-r-4 border-r-red-400 border-slate-200' :
                      f.rating === 3 ? 'border-r-4 border-r-amber-400 border-slate-200' :
                      'border-r-4 border-r-emerald-400 border-slate-200'}`}>
                    <div className="text-center shrink-0">
                      <span className="text-2xl">{ratingEmojis[f.rating]}</span>
                      <p className="text-xs font-bold text-slate-500">{f.rating}/5</p>
                    </div>
                    <div className="flex-1 min-w-0">
                      <p className="text-sm text-slate-700 dark:text-slate-300">{f.comment || <span className="text-slate-400 italic">No comment</span>}</p>
                      <div className="flex items-center gap-2 mt-2">
                        <span className="text-xs bg-amber-50 text-amber-600 px-2 py-0.5 rounded-full font-medium">{triggerLabels[f.trigger] || f.trigger}</span>
                        {f.page && <span className="text-xs bg-slate-100 text-slate-500 px-2 py-0.5 rounded-full dark:bg-slate-800 dark:text-slate-400">{f.page}</span>}
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
                  className="w-full bg-white border border-slate-200 rounded-lg pr-10 pl-4 py-2 text-sm dark:bg-slate-900 dark:border-slate-700 dark:text-slate-100" />
              </div>
              <span className="text-xs text-slate-400">{filteredUsers.length} user(s)</span>
            </div>

            <div className="bg-white border border-slate-200 rounded-xl overflow-hidden dark:bg-slate-900 dark:border-slate-800">
              <div className="overflow-x-auto">
                <table className="w-full">
                  <thead>
                    <tr className="bg-slate-50 text-xs text-slate-500 uppercase dark:bg-slate-800 dark:text-slate-400">
                      {[
                        { key: 'name', label: 'Name' },
                        { key: 'current_day', label: 'Day' },
                        { key: 'xp', label: 'XP' },
                        { key: 'streak', label: 'Streak' },
                        { key: 'last_active', label: 'Last Active', hideOnMobile: true },
                      ].map(col => (
                        <th key={col.key} onClick={() => toggleSort(col.key)}
                          className={`px-3 lg:px-4 py-3 text-left cursor-pointer hover:bg-slate-100 transition select-none dark:hover:bg-slate-700 ${'hideOnMobile' in col && col.hideOnMobile ? 'hidden sm:table-cell' : ''}`}>
                          <span className="flex items-center gap-1">
                            {col.label}
                            {sortCol === col.key && (sortAsc ? <ChevronUp className="w-3 h-3" /> : <ChevronDown className="w-3 h-3" />)}
                          </span>
                        </th>
                      ))}
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-slate-100 dark:divide-slate-800">
                    {filteredUsers.map((u, i) => (
                      <tr key={u.id} className={`hover:bg-slate-50 transition dark:hover:bg-slate-800 ${i % 2 === 1 ? 'bg-slate-50/50 dark:bg-slate-950/50' : ''}`}>
                        <td className="px-3 lg:px-4 py-3">
                          <p className="font-medium text-sm text-slate-800 dark:text-slate-100">{u.name}</p>
                          <p className="text-xs text-slate-400">{u.email}</p>
                        </td>
                        <td className="px-3 lg:px-4 py-3">
                          <div className="flex items-center gap-2">
                            <div className="h-1.5 w-12 bg-slate-100 rounded-full overflow-hidden dark:bg-slate-800">
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
            <div className="grid grid-cols-2 lg:grid-cols-6 gap-3">
              <div className="bg-emerald-50 border border-emerald-200 rounded-xl p-4 text-center">
                <p className="text-xl font-black text-emerald-700">{questionAnalysis?.by_classification?.ready || 0}</p>
                <p className="text-xs text-emerald-600">Ready</p>
              </div>
              <div className="bg-amber-50 border border-amber-200 rounded-xl p-4 text-center">
                <p className="text-xl font-black text-amber-700">{questionAnalysis?.flagged_count || 0}</p>
                <p className="text-xs text-amber-600">Flagged</p>
              </div>
              <div className="bg-slate-900 border border-slate-800 rounded-xl p-4 text-center">
                <p className="text-xl font-black text-white">{reviewReadyCount}</p>
                <p className="text-xs text-slate-300">Ratings Complete</p>
              </div>
              <div className="bg-white border border-slate-200 rounded-xl p-4 text-center dark:bg-slate-900 dark:border-slate-800">
                <p className="text-xl font-black text-slate-800 dark:text-slate-100">{questions.length}</p>
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
              <div className="grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-4 gap-4">
                {/* Stage Distribution Pie */}
                <div className="bg-white border border-slate-200 rounded-2xl p-5 dark:bg-slate-900 dark:border-slate-800">
                  <h3 className="text-sm font-bold text-slate-700 mb-3 dark:text-slate-200">Stage Distribution</h3>
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
                <div className="bg-white border border-slate-200 rounded-2xl p-5 dark:bg-slate-900 dark:border-slate-800">
                  <h3 className="text-sm font-bold text-slate-700 mb-3 dark:text-slate-200">Questions by Skill</h3>
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
                <div className="bg-white border border-slate-200 rounded-2xl p-5 dark:bg-slate-900 dark:border-slate-800">
                  <h3 className="text-sm font-bold text-slate-700 mb-3 dark:text-slate-200">Average Question Quality</h3>
                  <ResponsiveContainer width="100%" height={200}>
                    <RadarChart
                      data={questionRatingMetrics.map((metric) => ({
                        subject: metric.subject,
                        value: averageQuestionRating(metric.field),
                        fullMark: 5,
                      }))}
                    >
                      <PolarGrid />
                      <PolarAngleAxis dataKey="subject" tick={{fontSize: 11}} />
                      <PolarRadiusAxis angle={90} domain={[0, 5]} tick={{fontSize: 9}} />
                      <Radar dataKey="value" stroke="#0d9488" fill="#0d9488" fillOpacity={0.3} />
                    </RadarChart>
                  </ResponsiveContainer>
                </div>

                <div className="bg-white border border-slate-200 rounded-2xl p-5 dark:bg-slate-900 dark:border-slate-800">
                  <h3 className="text-sm font-bold text-slate-700 mb-3 dark:text-slate-200">Generation Sources</h3>
                  <div className="space-y-3">
                    {Object.entries(questionAnalysis.by_authoring_source || {}).map(([source, count]) => (
                      <div key={source}>
                        <div className="flex items-center justify-between text-xs text-slate-500 mb-1">
                          <span>{source === 'ai_generated' ? 'AI generated' : source}</span>
                          <span>{count}</span>
                        </div>
                        <div className="h-2 bg-slate-100 rounded-full overflow-hidden dark:bg-slate-800">
                          <div
                            className={`${source === 'ai_generated' ? 'bg-teal-500' : 'bg-slate-400'} h-full rounded-full`}
                            style={{ width: `${(count / Math.max(1, questionAnalysis.total)) * 100}%` }}
                          />
                        </div>
                      </div>
                    ))}
                    {!!questionAnalysis.by_batch?.length && (
                      <div className="pt-2 border-t border-slate-100 dark:border-slate-800 space-y-1 text-xs text-slate-500">
                        <p className="font-semibold text-slate-700">Recent batches</p>
                        {questionAnalysis.by_batch.slice(0, 4).map((batch) => (
                          <p key={batch.batch_id || 'unbatched'}>
                            {batch.batch_id || 'Unbatched'}: {batch.auto_published} active, {batch.held_in_review} review
                          </p>
                        ))}
                      </div>
                    )}
                  </div>
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
                    <span key={f.id} className="bg-white dark:bg-slate-900 border border-amber-300 rounded-lg px-3 py-1 text-xs text-amber-700">
                      #{f.id} — {f.issues.join(', ')}
                    </span>
                  ))}
                  {questionAnalysis.flagged_count > 10 && <span className="text-xs text-amber-500">+{questionAnalysis.flagged_count - 10} more</span>}
                </div>
              </div>
            )}

            <div className="flex items-center gap-2 flex-wrap">
              <select value={skillFilter} onChange={e => setSkillFilter(e.target.value)}
                className="bg-white border border-slate-200 rounded-lg px-3 py-2 text-sm text-slate-700 dark:bg-slate-900 dark:border-slate-700 dark:text-slate-300">
                <option value="">All Skills</option>
                {skills.map(s => <option key={s.id} value={s.id}>{s.icon} {s.name_ar}</option>)}
              </select>
              <select value={stageFilter} onChange={e => setStageFilter(e.target.value)}
                className="bg-white border border-slate-200 rounded-lg px-3 py-2 text-sm text-slate-700 dark:bg-slate-900 dark:border-slate-700 dark:text-slate-300">
                <option value="">All Stages</option>
                <option value="diagnostic">Diagnostic</option>
                <option value="foundation">Foundation</option>
                <option value="building">Building</option>
                <option value="peak">Mastery</option>
                <option value="mock">Mock Exam</option>
                <option value="general">General</option>
              </select>
              <select value={statusFilter} onChange={e => setStatusFilter(e.target.value)}
                className="bg-white border border-slate-200 rounded-lg px-3 py-2 text-sm text-slate-700 dark:bg-slate-900 dark:border-slate-700 dark:text-slate-300">
                <option value="">All Statuses</option>
                <option value="active">Active</option>
                <option value="review">Review</option>
                <option value="disabled">Disabled</option>
              </select>
              <select value={batchFilter} onChange={e => setBatchFilter(e.target.value)}
                className="bg-white border border-slate-200 rounded-lg px-3 py-2 text-sm text-slate-700 dark:bg-slate-900 dark:border-slate-700 dark:text-slate-300">
                <option value="">All Batches</option>
                {batchOptions.map((batch) => <option key={batch} value={batch}>{batch}</option>)}
              </select>
              <select value={authoringSourceFilter} onChange={e => setAuthoringSourceFilter(e.target.value)}
                className="bg-white border border-slate-200 rounded-lg px-3 py-2 text-sm text-slate-700 dark:bg-slate-900 dark:border-slate-700 dark:text-slate-300">
                <option value="">All Sources</option>
                {authoringSourceOptions.map((source) => <option key={source} value={source}>{source}</option>)}
              </select>
              <select value={variantGroupFilter} onChange={e => setVariantGroupFilter(e.target.value)}
                className="bg-white border border-slate-200 rounded-lg px-3 py-2 text-sm text-slate-700 dark:bg-slate-900 dark:border-slate-700 dark:text-slate-300">
                <option value="">All Variant Groups</option>
                {variantGroupOptions.map((group) => <option key={group} value={group}>{group}</option>)}
              </select>
              <select value={classificationFilter} onChange={e => setClassificationFilter(e.target.value)}
                className="bg-white border border-slate-200 rounded-lg px-3 py-2 text-sm text-slate-700 dark:bg-slate-900 dark:border-slate-700 dark:text-slate-300">
                <option value="">All Classifications</option>
                {Object.entries(contentClassificationLabels).map(([value, label]) => (
                  <option key={value} value={value}>{label}</option>
                ))}
              </select>
              <select value={issueCodeFilter} onChange={e => setIssueCodeFilter(e.target.value)}
                className="bg-white border border-slate-200 rounded-lg px-3 py-2 text-sm text-slate-700 dark:bg-slate-900 dark:border-slate-700 dark:text-slate-300">
                <option value="">All Issue Codes</option>
                {issueCodeOptions.map((code) => <option key={code} value={code}>{code}</option>)}
              </select>
              <select value={ratingsFilter} onChange={e => setRatingsFilter(e.target.value)}
                className="bg-white border border-slate-200 rounded-lg px-3 py-2 text-sm text-slate-700 dark:bg-slate-900 dark:border-slate-700 dark:text-slate-300">
                <option value="">All Rating States</option>
                <option value="complete">Ratings Complete</option>
                <option value="missing">Missing Ratings</option>
              </select>
              <select value={analyticsRiskFilter} onChange={e => setAnalyticsRiskFilter(e.target.value)}
                className="bg-white border border-slate-200 rounded-lg px-3 py-2 text-sm text-slate-700 dark:bg-slate-900 dark:border-slate-700 dark:text-slate-300">
                <option value="">All Analytics Flags</option>
                <option value="very_low_accuracy">Very Low Accuracy</option>
                <option value="too_easy">Too Easy</option>
                <option value="low_discrimination">Low Discrimination</option>
              </select>
              <select value={questionSort} onChange={e => setQuestionSort(e.target.value)}
                className="bg-white border border-slate-200 rounded-lg px-3 py-2 text-sm text-slate-700 dark:bg-slate-900 dark:border-slate-700 dark:text-slate-300">
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
                <div key={q.id} className="bg-white border border-slate-200 rounded-xl overflow-hidden dark:bg-slate-900 dark:border-slate-800">
                  <button onClick={() => setExpandedQ(expandedQ === q.id ? null : q.id)}
                    className="w-full px-4 py-3 flex items-center gap-3 hover:bg-slate-50 transition text-left dark:hover:bg-slate-800">
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
                    {q.content_classification && (
                      <span className="text-xs px-1.5 py-0.5 rounded shrink-0 bg-slate-100 text-slate-600">
                        {contentClassificationLabels[q.content_classification] || q.content_classification}
                      </span>
                    )}
                    {q.authoring_source && (
                      <span className={`text-xs px-1.5 py-0.5 rounded shrink-0 ${q.authoring_source === 'ai_generated' ? 'bg-teal-100 text-teal-700' : 'bg-slate-100 text-slate-600'}`}>
                        {q.authoring_source}
                      </span>
                    )}
                    <span className="flex-1 text-sm text-slate-700 truncate dark:text-slate-300">{q.text_ar}</span>
                    <div className="flex items-center gap-2 shrink-0">
                      <div className="h-1.5 w-10 bg-slate-100 rounded-full overflow-hidden dark:bg-slate-800" title={`Difficulty ${q.difficulty}`}>
                        <div className={`h-full rounded-full ${q.difficulty < 0.4 ? 'bg-emerald-400' : q.difficulty < 0.7 ? 'bg-amber-400' : 'bg-red-400'}`}
                          style={{ width: `${q.difficulty * 100}%` }} />
                      </div>
                      {q.rating_overall && <span className={`text-xs font-bold ${q.rating_overall >= 4.5 ? 'text-emerald-500' : q.rating_overall >= 3.5 ? 'text-teal-500' : q.rating_overall >= 3 ? 'text-amber-500' : 'text-red-500'}`}>★{q.rating_overall.toFixed(1)}</span>}
                      {q.times_answered > 0 && <span className="text-xs text-slate-400">{Math.round(q.accuracy * 100)}%</span>}
                      {q.status === 'review' && <span className="text-xs text-amber-500">Review</span>}
                      {q.status === 'disabled' && <span className="text-xs text-red-500">Disabled</span>}
                      {expandedQ === q.id ? <ChevronUp className="w-4 h-4 text-slate-400" /> : <ChevronDown className="w-4 h-4 text-slate-400" />}
                    </div>
                  </button>

                  {expandedQ === q.id && (
                    <div className="border-t border-slate-100 p-4 bg-slate-50/50 space-y-3 dark:border-slate-800 dark:bg-slate-950/50">
                      <QuestionPrompt
                        passage_ar={q.passage_ar}
                        table_ar={q.table_ar}
                        table_caption={q.table_caption}
                        figure_svg={q.figure_svg}
                        figure_alt={q.figure_alt}
                        text_ar={q.text_ar}
                        content_format={q.content_format}
                        comparison_columns={q.comparison_columns}
                        testIdPrefix={`admin-question-${q.id}`}
                        compact
                        passageClassName="bg-white border border-slate-200 rounded-lg p-3 text-sm text-slate-600 dark:text-slate-400"
                        questionClassName="text-sm text-slate-800 font-medium whitespace-pre-line"
                        figureFrameClassName="rounded-lg border border-slate-200 bg-white p-3 dark:bg-slate-900 dark:border-slate-700"
                        appearance={defaultQuestionAppearance}
                      />
                      <QuestionOptions
                        options={[
                          { key: 'a', label: 'A', text_ar: q.option_a },
                          { key: 'b', label: 'B', text_ar: q.option_b },
                          { key: 'c', label: 'C', text_ar: q.option_c },
                          { key: 'd', label: 'D', text_ar: q.option_d },
                        ]}
                        contentFormat={q.content_format}
                        selectedKey={q.correct_option}
                        correctOption={q.correct_option}
                        disabled
                        onSelect={() => {}}
                        testIdPrefix={`admin-question-options-${q.id}`}
                        appearance={defaultQuestionAppearance}
                      />
                      {q.explanation_ar && (
                        <div className="bg-amber-50 border border-amber-200 rounded-lg p-3 text-sm text-amber-700">
                          <p className="font-bold mb-1">Explanation:</p>
                          <p className="whitespace-pre-line">{q.explanation_ar}</p>
                        </div>
                      )}
                      {q.tags && (
                        <div className="flex flex-wrap gap-1">
                          {q.tags.split(',').map((tag, i) => (
                            <span key={i} className="bg-slate-100 text-slate-500 text-xs px-2 py-0.5 rounded-full dark:bg-slate-800 dark:text-slate-400">{tag.trim()}</span>
                          ))}
                        </div>
                      )}
                      <div className="grid grid-cols-1 lg:grid-cols-2 gap-3 text-xs">
                        <div className="rounded-lg border border-slate-200 bg-white p-3 dark:bg-slate-900 dark:border-slate-700">
                          <p className="font-bold text-slate-700 mb-2 dark:text-slate-200">Content Queue</p>
                          <div className="space-y-1 text-slate-600 dark:text-slate-400">
                            <p>Source key: <span className="font-mono">{q.source_key || 'admin question'}</span></p>
                            <p>Batch: {q.batch_id || 'Unbatched'}</p>
                            <p>Source: {q.authoring_source || 'human'}</p>
                            <p>Prompt version: {q.generation_prompt_version || '—'}</p>
                            <p>Variant group: {q.variant_group || '—'}</p>
                            <p>Classification: {contentClassificationLabels[q.content_classification || 'ready'] || q.content_classification || 'Ready'}</p>
                            <p>Recommended action: {recommendedActionLabels[q.recommended_action || 'keep-active'] || q.recommended_action || 'Keep Active'}</p>
                            <p>Issue counts: {q.content_issue_counts?.error || 0} error, {q.content_issue_counts?.warning || 0} warning</p>
                            <p>Ratings complete: {q.ratings_complete ? 'Yes' : 'No'}</p>
                          </div>
                        </div>
                        <div className="rounded-lg border border-slate-200 bg-white p-3 dark:bg-slate-900 dark:border-slate-700">
                          <p className="font-bold text-slate-700 mb-2 dark:text-slate-200">Review State</p>
                          <div className="space-y-1 text-slate-600 dark:text-slate-400">
                            <p>Review passes: {q.rating_passes_done || 0}</p>
                            <p>Missing ratings: {q.missing_review_ratings?.length ? q.missing_review_ratings.join(', ') : 'None'}</p>
                            <p>Analytics flags: {q.analytics_flags?.length ? q.analytics_flags.join(', ') : 'None'}</p>
                          </div>
                          {q.rating_notes && (
                            <p className="mt-2 rounded-md bg-slate-50 dark:bg-slate-800 px-2 py-1 text-slate-600 dark:text-slate-400">{q.rating_notes}</p>
                          )}
                        </div>
                      </div>
                      {!!q.content_issues?.length && (
                        <div className="rounded-lg border border-amber-200 bg-amber-50 p-3 text-xs text-amber-800">
                          <p className="font-bold mb-1">Content checks</p>
                          <div className="space-y-1">
                            {q.content_issues.map((issue) => (
                              <p key={`${issue.code}-${issue.field}`}>{issue.field}: {issue.message}</p>
                            ))}
                          </div>
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
                <h3 className="font-bold text-slate-800 dark:text-slate-100">Final Mock Exam</h3>
                <p className="text-xs text-slate-500">65 questions • 70 minutes • Verbal + Quant</p>
              </div>
              <a href="/mock?preview=true"
                className="flex items-center gap-2 bg-amber-500 hover:bg-amber-600 text-white text-sm font-bold px-5 py-2.5 rounded-lg transition">
                <Trophy className="w-4 h-4" />
                Preview Exam
              </a>
            </div>

            {/* Config */}
            <div className="bg-white border border-slate-200 rounded-xl p-4 flex items-center justify-between dark:bg-slate-900 dark:border-slate-800">
              <div>
                <p className="font-bold text-slate-700 text-sm dark:text-slate-200">Max Attempts</p>
                <p className="text-xs text-slate-500">Number of attempts allowed per student</p>
              </div>
              <div className="flex items-center gap-2">
                <input type="number" min="1" max="10" value={mockMaxAttempts} onChange={e => setMockMaxAttempts(Number(e.target.value))}
                  className="w-16 border border-slate-200 rounded-lg px-2 py-1.5 text-center text-sm dark:bg-slate-950 dark:border-slate-700 dark:text-slate-100" />
                <button onClick={saveMockConfig} className="bg-amber-500 hover:bg-amber-600 text-white text-xs font-bold px-3 py-1.5 rounded-lg">
                  Save
                </button>
              </div>
            </div>

            {/* Mock Stats */}
            <div className="grid grid-cols-2 lg:grid-cols-4 gap-3">
              <div className="bg-white border border-slate-200 rounded-xl p-4 dark:bg-slate-900 dark:border-slate-800">
                <div className="flex items-center gap-3">
                  <div className="w-10 h-10 rounded-lg flex items-center justify-center bg-amber-50 text-amber-600">
                    <Trophy className="w-5 h-5" />
                  </div>
                  <div>
                    <p className="text-2xl font-black text-slate-800 dark:text-slate-100">{users.mock_taken}</p>
                    <p className="text-xs text-slate-500">Completed Exam</p>
                  </div>
                </div>
              </div>
              <div className="bg-white border border-slate-200 rounded-xl p-4 dark:bg-slate-900 dark:border-slate-800">
                <div className="flex items-center gap-3">
                  <div className="w-10 h-10 rounded-lg flex items-center justify-center bg-blue-50 text-blue-600">
                    <Star className="w-5 h-5" />
                  </div>
                  <div>
                    <p className="text-2xl font-black text-slate-800 dark:text-slate-100">{users.mock_avg_score || '—'}</p>
                    <p className="text-xs text-slate-500">Average Score</p>
                  </div>
                </div>
              </div>
              <div className="bg-white border border-slate-200 rounded-xl p-4 dark:bg-slate-900 dark:border-slate-800">
                <div className="flex items-center gap-3">
                  <div className="w-10 h-10 rounded-lg flex items-center justify-center bg-emerald-50 text-emerald-600">
                    <Users className="w-5 h-5" />
                  </div>
                  <div>
                    <p className="text-2xl font-black text-slate-800 dark:text-slate-100">{users.users.filter(u => u.mock_attempts > 0 && u.mock_score >= 65).length}</p>
                    <p className="text-xs text-slate-500">Passed (65+)</p>
                  </div>
                </div>
              </div>
              <div className="bg-white border border-slate-200 rounded-xl p-4 dark:bg-slate-900 dark:border-slate-800">
                <div className="flex items-center gap-3">
                  <div className="w-10 h-10 rounded-lg flex items-center justify-center bg-violet-50 text-violet-600">
                    <Users className="w-5 h-5" />
                  </div>
                  <div>
                    <p className="text-2xl font-black text-slate-800 dark:text-slate-100">{users.users.filter(u => u.mock_attempts > 0 && u.mock_score >= 80).length}</p>
                    <p className="text-xs text-slate-500">Excellent (80+)</p>
                  </div>
                </div>
              </div>
            </div>

            {/* Score distribution */}
            {users.mock_taken > 0 && (
              <div className="bg-white border border-slate-200 rounded-2xl p-5 dark:bg-slate-900 dark:border-slate-800">
                <h3 className="text-sm font-bold text-slate-700 mb-3 dark:text-slate-200">Score Distribution</h3>
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
            <div className="bg-white border border-slate-200 rounded-xl overflow-hidden dark:bg-slate-900 dark:border-slate-800">
              <div className="px-4 py-3 border-b border-slate-100 dark:border-slate-800">
                <h3 className="font-bold text-slate-700 text-sm dark:text-slate-200">Student Results</h3>
              </div>
              <div className="overflow-x-auto">
                <table className="w-full">
                  <thead>
                    <tr className="bg-slate-50 text-xs text-slate-500 uppercase dark:bg-slate-800 dark:text-slate-400">
                      <th className="px-4 py-3 text-left">Student</th>
                      <th className="px-4 py-3 text-left">Day</th>
                      <th className="px-4 py-3 text-left">Status</th>
                      <th className="px-4 py-3 text-left">Score</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-slate-100 dark:divide-slate-800">
                    {users.users.filter(u => u.current_day >= 25).map((u, i) => (
                      <tr key={u.id} className={`hover:bg-slate-50 dark:hover:bg-slate-800 ${i % 2 === 1 ? 'bg-slate-50/50 dark:bg-slate-950/50' : ''}`}>
                        <td className="px-4 py-3">
                          <p className="font-medium text-sm text-slate-800 dark:text-slate-100">{u.name}</p>
                          <p className="text-xs text-slate-400">{u.email}</p>
                        </td>
                        <td className="px-4 py-3 text-sm text-slate-600 dark:text-slate-400">{u.current_day}/30</td>
                        <td className="px-4 py-3">
                          {u.mock_attempts > 0 ? (
                            <span className="text-xs bg-emerald-100 text-emerald-700 px-2 py-1 rounded-full font-medium">Completed ({u.mock_attempts} attempts)</span>
                          ) : (
                            <span className="text-xs bg-slate-100 text-slate-500 px-2 py-1 rounded-full dark:bg-slate-800 dark:text-slate-400">Not Started</span>
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
  const [tableEditorValue, setTableEditorValue] = useState(
    question?.table_ar ? JSON.stringify(question.table_ar, null, 2) : '',
  );
  const [form, setForm] = useState<QuestionPayload>({
    skill_id: question?.skill_id || skills[0]?.id || '',
    question_type: question?.question_type || 'reading',
    difficulty: question?.difficulty || 0.5,
    text_ar: question?.text_ar || '',
    passage_ar: question?.passage_ar || null,
    content_format: question?.content_format || ((question?.skill_id || skills[0]?.id || '').startsWith('quant_') ? 'markdown_math' : 'plain'),
    comparison_columns: question?.comparison_columns || null,
    figure_svg: question?.figure_svg || null,
    figure_alt: question?.figure_alt || null,
    table_ar: question?.table_ar || null,
    table_caption: question?.table_caption || null,
    option_a: question?.option_a || '', option_b: question?.option_b || '',
    option_c: question?.option_c || '', option_d: question?.option_d || '',
    correct_option: question?.correct_option || 'a',
    explanation_ar: question?.explanation_ar || null,
    solution_steps_ar: question?.solution_steps_ar ? JSON.stringify(question.solution_steps_ar) : null,
    tags: question?.tags || '',
    stage: question?.stage || 'general',
    status: question?.status || 'active',
    rating_clarity: question?.rating_clarity ?? null,
    rating_cognitive: question?.rating_cognitive ?? null,
    rating_distractors: question?.rating_distractors ?? null,
    rating_difficulty_align: question?.rating_difficulty_align ?? null,
    rating_explanation: question?.rating_explanation ?? null,
    rating_fairness: question?.rating_fairness ?? null,
    rating_discrimination: question?.rating_discrimination ?? null,
    rating_overall: question?.rating_overall ?? null,
    rating_passes_done: question?.rating_passes_done || 0,
    rating_notes: question?.rating_notes || null,
  });

  const update = (field: string, value: unknown) => setForm(prev => ({ ...prev, [field]: value }));
  const parsedTable = parseTableEditorValue(tableEditorValue);
  const safePreviewSvg = sanitizeInlineSvg(form.figure_svg);
  const comparisonColumns = form.comparison_columns || { a: '', b: '' };
  const reviewScores = questionRatingMetrics.map(metric => form[metric.field]).filter((value): value is number => typeof value === 'number');
  const computedOverallRating = reviewScores.length === questionRatingMetrics.length
    ? +(reviewScores.reduce((sum, value) => sum + value, 0) / questionRatingMetrics.length).toFixed(2)
    : null;

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setSaving(true); setError('');
    if (tableEditorValue.trim() && parsedTable.error) {
      setSaving(false);
      setError(parsedTable.error);
      return;
    }
    if (form.figure_svg?.trim() && !form.figure_alt?.trim()) {
      setSaving(false);
      setError('Figure alt text is required when a figure is provided.');
      return;
    }
    if (form.content_format === 'markdown_math') {
      const mathIssues = validateMarkdownMathFields([
        { label: 'Passage text', value: form.passage_ar },
        { label: 'Question text', value: form.text_ar },
        { label: 'Option A', value: form.option_a },
        { label: 'Option B', value: form.option_b },
        { label: 'Option C', value: form.option_c },
        { label: 'Option D', value: form.option_d },
        { label: 'Explanation', value: form.explanation_ar },
        { label: 'Solution steps', value: form.solution_steps_ar },
        { label: 'Column A', value: form.comparison_columns?.a },
        { label: 'Column B', value: form.comparison_columns?.b },
      ]);
      if (mathIssues.length) {
        setSaving(false);
        setError(mathIssues[0]);
        return;
      }
    }
    if (form.question_type === 'comparison' && (!comparisonColumns.a.trim() || !comparisonColumns.b.trim())) {
      setSaving(false);
      setError('Comparison questions require both Column A and Column B.');
      return;
    }
    const payload: QuestionPayload = {
      ...form,
      figure_svg: form.figure_svg?.trim() ? form.figure_svg : null,
      figure_alt: form.figure_alt?.trim() ? form.figure_alt : null,
      table_ar: parsedTable.value,
      table_caption: form.table_caption?.trim() ? form.table_caption : null,
      comparison_columns: form.question_type === 'comparison'
        ? { a: comparisonColumns.a.trim(), b: comparisonColumns.b.trim() }
        : null,
      rating_overall: computedOverallRating,
      rating_notes: form.rating_notes?.trim() ? form.rating_notes : null,
    };
    try { await onSave(payload); }
    catch (err: unknown) { setError(err instanceof Error ? err.message : 'An error occurred'); }
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
      <div className="bg-white rounded-2xl shadow-2xl w-full max-w-2xl my-8 dark:bg-slate-900">
        <div className="flex items-center justify-between p-5 border-b border-slate-100 dark:border-slate-800">
          <h3 className="font-bold text-slate-800 dark:text-slate-100">{question ? 'Edit Question' : 'Add New Question'}</h3>
          <button onClick={onClose} className="text-slate-400 hover:text-slate-600"><X className="w-5 h-5" /></button>
        </div>
        <form onSubmit={handleSubmit} className="p-5 space-y-4">
          <div className="grid grid-cols-2 gap-3">
            <div>
              <label className="text-xs font-medium text-slate-600 mb-1 block dark:text-slate-400">Skill</label>
              <select value={form.skill_id} onChange={e => {
                const nextSkill = e.target.value;
                update('skill_id', nextSkill);
                if (!question && nextSkill.startsWith('quant_')) {
                  update('content_format', 'markdown_math');
                }
              }}
                aria-label="Skill"
                className="w-full border border-slate-200 rounded-lg px-3 py-2 text-sm dark:bg-slate-950 dark:border-slate-700 dark:text-slate-100">
                {skills.map(s => <option key={s.id} value={s.id}>{s.icon} {s.name_ar}</option>)}
              </select>
            </div>
            <div>
              <label className="text-xs font-medium text-slate-600 mb-1 block dark:text-slate-400">Question Type</label>
              <select value={form.question_type} onChange={e => update('question_type', e.target.value)}
                aria-label="Question Type"
                className="w-full border border-slate-200 rounded-lg px-3 py-2 text-sm dark:bg-slate-950 dark:border-slate-700 dark:text-slate-100">
                {qTypes.map(t => <option key={t.v} value={t.v}>{t.l}</option>)}
              </select>
            </div>
          </div>
          <div className="grid grid-cols-2 lg:grid-cols-4 gap-3">
            <div>
              <label className="text-xs font-medium text-slate-600 mb-1 block dark:text-slate-400">Content Format</label>
              <select value={form.content_format || 'plain'} onChange={e => update('content_format', e.target.value)}
                aria-label="Content Format"
                className="w-full border border-slate-200 rounded-lg px-3 py-2 text-sm dark:bg-slate-950 dark:border-slate-700 dark:text-slate-100">
                <option value="plain">Plain Text</option>
                <option value="markdown_math">Markdown + TeX</option>
              </select>
            </div>
            <div>
              <label className="text-xs font-medium text-slate-600 mb-1 block dark:text-slate-400">Stage</label>
              <select value={form.stage || 'general'} onChange={e => update('stage', e.target.value)}
                aria-label="Stage"
                className="w-full border border-slate-200 rounded-lg px-3 py-2 text-sm dark:bg-slate-950 dark:border-slate-700 dark:text-slate-100">
                {['diagnostic', 'foundation', 'building', 'peak', 'mock', 'general'].map(stage => (
                  <option key={stage} value={stage}>{stage}</option>
                ))}
              </select>
            </div>
            <div>
              <label className="text-xs font-medium text-slate-600 mb-1 block dark:text-slate-400">Status</label>
              <select value={form.status || 'active'} onChange={e => update('status', e.target.value)}
                aria-label="Status"
                className="w-full border border-slate-200 rounded-lg px-3 py-2 text-sm dark:bg-slate-950 dark:border-slate-700 dark:text-slate-100">
                {['active', 'review', 'disabled'].map(status => (
                  <option key={status} value={status}>{status}</option>
                ))}
              </select>
            </div>
            <div>
              <label className="text-xs font-medium text-slate-600 mb-1 block dark:text-slate-400">Tags</label>
              <input value={form.tags || ''} onChange={e => update('tags', e.target.value)}
                aria-label="Tags"
                className="w-full border border-slate-200 rounded-lg px-3 py-2 text-sm dark:bg-slate-950 dark:border-slate-700 dark:text-slate-100"
                placeholder="fractions, percentages" />
            </div>
          </div>
          <div>
            <label className="text-xs font-medium text-slate-600 mb-1 block dark:text-slate-400">Difficulty: {form.difficulty}</label>
            <input type="range" min="0" max="1" step="0.1" value={form.difficulty}
              aria-label="Difficulty"
              onChange={e => update('difficulty', parseFloat(e.target.value))} className="w-full accent-amber-500" />
            <div className="flex justify-between text-xs text-slate-400"><span>Easy</span><span>Medium</span><span>Hard</span></div>
          </div>
          <div className="rounded-xl border border-slate-200 bg-slate-50 p-4 space-y-3 dark:bg-slate-950 dark:border-slate-700">
            <div className="flex items-center justify-between">
              <p className="text-sm font-bold text-slate-700 dark:text-slate-200">Editorial Review</p>
              <span className="text-xs text-slate-500">
                Overall: {computedOverallRating != null ? computedOverallRating.toFixed(2) : 'Pending'}
              </span>
            </div>
            <div className="grid grid-cols-2 lg:grid-cols-4 gap-3">
              {questionRatingMetrics.map((metric) => (
                <div key={metric.field}>
                  <label className="text-xs font-medium text-slate-600 mb-1 block dark:text-slate-400">{metric.subject}</label>
                  <select
                    value={form[metric.field] ?? ''}
                    onChange={(e) => update(metric.field, e.target.value ? Number(e.target.value) : null)}
                    className="w-full border border-slate-200 rounded-lg px-3 py-2 text-sm dark:bg-slate-950 dark:border-slate-700 dark:text-slate-100"
                  >
                    <option value="">Not rated</option>
                    {[1, 2, 3, 4, 5].map((score) => (
                      <option key={score} value={score}>{score}</option>
                    ))}
                  </select>
                </div>
              ))}
            </div>
            <div className="grid grid-cols-1 lg:grid-cols-3 gap-3">
              <div>
                <label className="text-xs font-medium text-slate-600 mb-1 block dark:text-slate-400">Review Passes</label>
                <input
                  type="number"
                  min="0"
                  max="3"
                  value={form.rating_passes_done ?? 0}
                  onChange={(e) => update('rating_passes_done', Number(e.target.value))}
                  aria-label="Review Passes"
                  className="w-full border border-slate-200 rounded-lg px-3 py-2 text-sm dark:bg-slate-950 dark:border-slate-700 dark:text-slate-100"
                />
              </div>
              <div className="lg:col-span-2">
                <label className="text-xs font-medium text-slate-600 mb-1 block dark:text-slate-400">Review Notes</label>
                <input
                  value={form.rating_notes || ''}
                  onChange={(e) => update('rating_notes', e.target.value || null)}
                  aria-label="Review Notes"
                  className="w-full border border-slate-200 rounded-lg px-3 py-2 text-sm dark:bg-slate-950 dark:border-slate-700 dark:text-slate-100"
                  placeholder="Key clarity fixes, answer-key checks, or editorial notes"
                />
              </div>
            </div>
            <p className="text-xs text-slate-500">
              Active questions now require all seven review ratings and at least one review pass.
            </p>
          </div>
          {form.content_format === 'markdown_math' && (
            <div className="rounded-xl border border-teal-200 bg-teal-50 p-3 text-xs text-teal-700">
              Use Markdown plus TeX like <code>$\\frac{'{1}'}{'{2}'}$</code>, <code>$\\sqrt{'{50}'}$</code>, and display blocks with <code>$$...$$</code>.
            </div>
          )}
          <div>
            <label className="text-xs font-medium text-slate-600 mb-1 block dark:text-slate-400">Passage Text (optional)</label>
            <textarea value={form.passage_ar || ''} onChange={e => update('passage_ar', e.target.value || null)}
              aria-label="Passage Text (optional)"
              rows={2} className="w-full border border-slate-200 rounded-lg px-3 py-2 text-sm resize-none dark:bg-slate-950 dark:border-slate-700 dark:text-slate-100" />
          </div>
          <div>
            <label className="text-xs font-medium text-slate-600 mb-1 block dark:text-slate-400">Question Text *</label>
            <textarea value={form.text_ar} onChange={e => update('text_ar', e.target.value)}
              aria-label="Question Text *"
              rows={3} className="w-full border border-slate-200 rounded-lg px-3 py-2 text-sm resize-none dark:bg-slate-950 dark:border-slate-700 dark:text-slate-100" required />
          </div>
          {form.question_type === 'comparison' && (
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-3">
              <div>
                <label className="text-xs font-medium text-slate-600 mb-1 block dark:text-slate-400">Column A *</label>
                <textarea
                  value={comparisonColumns.a}
                  onChange={e => update('comparison_columns', { ...comparisonColumns, a: e.target.value })}
                  rows={3}
                  className="w-full border border-slate-200 rounded-lg px-3 py-2 text-sm resize-none dark:bg-slate-950 dark:border-slate-700 dark:text-slate-100"
                />
              </div>
              <div>
                <label className="text-xs font-medium text-slate-600 mb-1 block dark:text-slate-400">Column B *</label>
                <textarea
                  value={comparisonColumns.b}
                  onChange={e => update('comparison_columns', { ...comparisonColumns, b: e.target.value })}
                  rows={3}
                  className="w-full border border-slate-200 rounded-lg px-3 py-2 text-sm resize-none dark:bg-slate-950 dark:border-slate-700 dark:text-slate-100"
                />
              </div>
            </div>
          )}
          <div>
            <label className="text-xs font-medium text-slate-600 mb-1 block dark:text-slate-400">Figure SVG (optional)</label>
            <textarea value={form.figure_svg || ''} onChange={e => update('figure_svg', e.target.value || null)}
              aria-label="Figure SVG (optional)"
              rows={6} className="w-full border border-slate-200 rounded-lg px-3 py-2 text-xs font-mono resize-y dark:bg-slate-950 dark:border-slate-700 dark:text-slate-100" placeholder="<svg ...>...</svg>" />
            {form.figure_svg && !safePreviewSvg && (
              <p className="mt-1 text-xs text-amber-600">Preview is hidden because the SVG markup is invalid or unsafe.</p>
            )}
          </div>
          <div>
            <label className="text-xs font-medium text-slate-600 mb-1 block dark:text-slate-400">Figure Alt Text</label>
            <input value={form.figure_alt || ''} onChange={e => update('figure_alt', e.target.value || null)}
              aria-label="Figure Alt Text"
              className="w-full border border-slate-200 rounded-lg px-3 py-2 text-sm dark:bg-slate-950 dark:border-slate-700 dark:text-slate-100"
              placeholder="Describe the figure for learners using assistive tech" />
          </div>
          <div>
            <label className="text-xs font-medium text-slate-600 mb-1 block dark:text-slate-400">Table JSON (optional)</label>
            <textarea value={tableEditorValue} onChange={e => setTableEditorValue(e.target.value)}
              aria-label="Table JSON (optional)"
              rows={6} className="w-full border border-slate-200 rounded-lg px-3 py-2 text-xs font-mono resize-y dark:bg-slate-950 dark:border-slate-700 dark:text-slate-100" placeholder={'{"headers":["Column","Value"],"rows":[["A","10"],["B","12"]]}'}
            />
            {tableEditorValue.trim() && parsedTable.error && (
              <p className="mt-1 text-xs text-amber-600">{parsedTable.error}</p>
            )}
          </div>
          <div>
            <label className="text-xs font-medium text-slate-600 mb-1 block dark:text-slate-400">Table Caption (optional)</label>
            <input value={form.table_caption || ''} onChange={e => update('table_caption', e.target.value || null)}
              aria-label="Table Caption (optional)"
              className="w-full border border-slate-200 rounded-lg px-3 py-2 text-sm dark:bg-slate-950 dark:border-slate-700 dark:text-slate-100"
              placeholder="Short summary of what the table shows" />
          </div>
          <div className="grid grid-cols-2 gap-3">
            {[{ k: 'option_a', l: 'A' }, { k: 'option_b', l: 'B' }, { k: 'option_c', l: 'C' }, { k: 'option_d', l: 'D' }].map(opt => (
              <div key={opt.k}>
                <label className="text-xs font-medium text-slate-600 mb-1 flex items-center gap-1">
                  <input type="radio" name="correct" value={opt.k.slice(-1)}
                    checked={form.correct_option === opt.k.slice(-1)}
                    onChange={() => update('correct_option', opt.k.slice(-1))} className="accent-emerald-500" />
                  Option {opt.l} {form.correct_option === opt.k.slice(-1) && <span className="text-emerald-500 text-[10px]">(Correct)</span>}
                </label>
                <input value={(form as unknown as Record<string, string>)[opt.k] || ''}
                  aria-label={`Option ${opt.l}`}
                  onChange={e => update(opt.k, e.target.value)}
                  className="w-full border border-slate-200 rounded-lg px-3 py-2 text-sm dark:bg-slate-950 dark:border-slate-700 dark:text-slate-100" required />
              </div>
            ))}
          </div>
          <div>
            <label className="text-xs font-medium text-slate-600 mb-1 block dark:text-slate-400">Explanation (optional)</label>
            <textarea value={form.explanation_ar || ''} onChange={e => update('explanation_ar', e.target.value || null)}
              aria-label="Explanation (optional)"
              rows={2} className="w-full border border-slate-200 rounded-lg px-3 py-2 text-sm resize-none dark:bg-slate-950 dark:border-slate-700 dark:text-slate-100" />
          </div>
          <div>
            <label className="text-xs font-medium text-slate-600 mb-1 block dark:text-slate-400">Solution Steps JSON (optional)</label>
            <textarea value={form.solution_steps_ar || ''} onChange={e => update('solution_steps_ar', e.target.value || null)}
              aria-label="Solution Steps JSON (optional)"
              rows={3} className="w-full border border-slate-200 rounded-lg px-3 py-2 text-xs font-mono resize-y dark:bg-slate-950 dark:border-slate-700 dark:text-slate-100"
              placeholder='["First simplify the fraction.", "Then compare the two values."]' />
          </div>
          {(form.passage_ar || form.text_ar || form.figure_svg || parsedTable.value) && (
            <div className="rounded-xl border border-slate-200 bg-slate-50 p-4 dark:bg-slate-950 dark:border-slate-700" data-testid="admin-question-preview">
              <p className="mb-3 text-xs font-bold uppercase tracking-wide text-slate-500">Live Preview</p>
              <QuestionPrompt
                passage_ar={form.passage_ar}
                table_ar={parsedTable.value}
                table_caption={form.table_caption}
                figure_svg={safePreviewSvg}
                figure_alt={form.figure_alt}
                text_ar={form.text_ar}
                content_format={form.content_format}
                comparison_columns={form.comparison_columns}
                testIdPrefix="admin-question-preview"
                compact
                passageClassName="bg-white border border-slate-200 rounded-lg p-3 mb-3 text-sm text-slate-600 dark:text-slate-400"
                questionClassName="text-sm text-slate-800 font-medium whitespace-pre-line"
                figureFrameClassName="mb-3 rounded-lg border border-slate-200 bg-white p-3 dark:bg-slate-900 dark:border-slate-700"
                appearance={defaultQuestionAppearance}
              />
              <div className="mt-4">
                <QuestionOptions
                  options={[
                    { key: 'a', label: 'A', text_ar: form.option_a },
                    { key: 'b', label: 'B', text_ar: form.option_b },
                    { key: 'c', label: 'C', text_ar: form.option_c },
                    { key: 'd', label: 'D', text_ar: form.option_d },
                  ]}
                  contentFormat={form.content_format}
                  selectedKey={form.correct_option}
                  correctOption={form.correct_option}
                  disabled
                  onSelect={() => {}}
                  testIdPrefix="admin-preview"
                  appearance={defaultQuestionAppearance}
                />
              </div>
            </div>
          )}
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
