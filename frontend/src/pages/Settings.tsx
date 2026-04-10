import { useState, useEffect } from 'react';
import { useAuth } from '@/hooks/useAuth';
import { api } from '@/lib/api';
import type { SupportTicket } from '@/types';
import { useTheme } from 'next-themes';
import { pageShell, pageStack } from '@/lib/layout';
import { User, Mail, Lock, Sun, Moon, HelpCircle, MessageSquare, AlertTriangle, Clock } from 'lucide-react';
import { FAQAccordion } from '@/components/support/FAQAccordion';

const MINUTE_PRESETS = [15, 30, 45, 60, 90, 120] as const;

export default function Settings() {
  const { user, loadUser } = useAuth();
  const { theme, setTheme } = useTheme();
  const [activeTab, setActiveTab] = useState<'account' | 'appearance' | 'support'>('account');
  const [passwordMsg, setPasswordMsg] = useState<{ type: 'success' | 'error'; text: string } | null>(null);
  const [passwordLoading, setPasswordLoading] = useState(false);
  const [showFeedback, setShowFeedback] = useState(false);
  const [showFAQ, setShowFAQ] = useState(false);
  const [showTickets, setShowTickets] = useState(false);
  const [feedbackText, setFeedbackText] = useState('');
  const [feedbackMsg, setFeedbackMsg] = useState<string | null>(null);
  const [tickets, setTickets] = useState<SupportTicket[]>([]);
  const [dailyMinutes, setDailyMinutes] = useState(0);
  const [studyMsg, setStudyMsg] = useState<{ type: 'success' | 'error'; text: string } | null>(null);
  const [studySaving, setStudySaving] = useState(false);

  if (!user) return null;

  // Initialize dailyMinutes from user on first render (after user is available)
  if (dailyMinutes === 0 && user.daily_minutes > 0) {
    setDailyMinutes(user.daily_minutes);
  }

  const tabs = [
    { key: 'account' as const, label: 'Account', icon: User },
    { key: 'appearance' as const, label: 'Appearance', icon: Sun },
    { key: 'support' as const, label: 'Support', icon: HelpCircle },
  ];

  const questionsPerDay = Math.max(10, Math.floor(dailyMinutes / 4));
  const hasStudyChange = dailyMinutes !== user.daily_minutes;

  const handleStudySave = async () => {
    setStudyMsg(null);
    setStudySaving(true);
    try {
      await api.updateSettings({ daily_minutes: dailyMinutes });
      await loadUser();
      setStudyMsg({ type: 'success', text: 'Study plan updated! Your daily schedule has been regenerated.' });
      setTimeout(() => setStudyMsg(null), 4000);
    } catch {
      setStudyMsg({ type: 'error', text: 'Failed to save. Please try again.' });
    }
    setStudySaving(false);
  };

  const handlePasswordChange = async () => {
    setPasswordMsg(null);
    setPasswordLoading(true);
    try {
      await api.forgotPassword({ email: user.email });
      setPasswordMsg({ type: 'success', text: 'A password reset link has been sent to your email.' });
    } catch {
      setPasswordMsg({ type: 'error', text: 'Failed to initiate password reset. Please try again.' });
    }
    setPasswordLoading(false);
  };

  const loadTickets = async () => {
    try {
      const data = await api.myTickets();
      setTickets(data);
    } catch { /* ignore */ }
  };

  useEffect(() => {
    if (activeTab === 'support') loadTickets();
  }, [activeTab]);

  const handleFeedback = async () => {
    if (!feedbackText.trim()) return;
    try {
      const result = await api.submitFeedback({
        rating: 0,
        comment: feedbackText,
        trigger: 'settings_support',
      });
      setFeedbackMsg(`Message #${result.ticket_id} sent. We'll review it shortly.`);
      setFeedbackText('');
      loadTickets();
      setTimeout(() => setFeedbackMsg(null), 5000);
    } catch {
      setFeedbackMsg('Failed to send. Please try again.');
    }
  };

  return (
    <div className={`${pageShell.standard} ${pageStack} page-enter`} data-testid="settings-page">
      <h1 className="text-2xl font-black text-slate-800 dark:text-slate-100">Settings</h1>

      {/* Tabs */}
      <div className="flex gap-1 bg-slate-100 dark:bg-slate-800 rounded-xl p-1">
        {tabs.map(tab => {
          const Icon = tab.icon;
          const active = activeTab === tab.key;
          return (
            <button key={tab.key} onClick={() => setActiveTab(tab.key)}
              data-testid={`settings-tab-${tab.key}`}
              className={`flex-1 flex items-center justify-center gap-2 rounded-lg py-2.5 text-sm font-bold transition-all ${active ? 'bg-white dark:bg-slate-900 text-teal-600 dark:text-teal-400 shadow-sm' : 'text-slate-500 dark:text-slate-400 hover:text-slate-700 dark:hover:text-slate-200'}`}>
              <Icon className="h-4 w-4" />
              {tab.label}
            </button>
          );
        })}
      </div>

      {/* Account Tab */}
      {activeTab === 'account' && (
        <div className="space-y-5">
          {/* Profile Info */}
          <div className="bg-white dark:bg-slate-900 shadow-card rounded-2xl p-5">
            <h2 className="text-sm font-bold uppercase tracking-wider text-slate-400 dark:text-slate-500 mb-4">Profile Information</h2>
            <div className="space-y-4">
              <div className="flex items-center gap-4">
                <div className="flex h-14 w-14 items-center justify-center rounded-full bg-gradient-to-br from-teal-400 to-teal-600 text-xl font-bold text-white shadow-brand">
                  {user.name?.charAt(0)}
                </div>
                <div>
                  <p className="text-lg font-bold text-slate-800 dark:text-slate-100">{user.name}</p>
                  <p className="text-sm text-slate-500 dark:text-slate-400">Learner</p>
                </div>
              </div>
              <div className="grid gap-3">
                <div className="flex items-center gap-3 rounded-xl bg-slate-50 dark:bg-slate-800 px-4 py-3">
                  <Mail className="h-4 w-4 text-slate-400 dark:text-slate-500" />
                  <div>
                    <p className="text-xs text-slate-400 dark:text-slate-500">Email</p>
                    <p className="text-sm font-medium text-slate-700 dark:text-slate-200">{user.email}</p>
                  </div>
                </div>
                <div className="flex items-center gap-3 rounded-xl bg-slate-50 dark:bg-slate-800 px-4 py-3">
                  <User className="h-4 w-4 text-slate-400 dark:text-slate-500" />
                  <div>
                    <p className="text-xs text-slate-400 dark:text-slate-500">Member since</p>
                    <p className="text-sm font-medium text-slate-700 dark:text-slate-200">
                      {user.course_started_at
                        ? new Date(user.course_started_at).toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' })
                        : 'Recently joined'}
                      {' '}<span className="text-slate-400 dark:text-slate-500">(Day {user.current_day}/30)</span>
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Study Preferences */}
          <div className="bg-white dark:bg-slate-900 shadow-card rounded-2xl p-5" data-testid="settings-study-prefs">
            <h2 className="text-sm font-bold uppercase tracking-wider text-slate-400 dark:text-slate-500 mb-4">
              <Clock className="h-4 w-4 inline mr-1" />
              Study Preferences
            </h2>
            <p className="text-sm text-slate-500 dark:text-slate-400 mb-4">
              How much time can you study each day? This adjusts your daily question count and study plan.
            </p>
            <div className="grid grid-cols-3 gap-2 sm:grid-cols-6">
              {MINUTE_PRESETS.map(mins => (
                <button
                  key={mins}
                  type="button"
                  data-testid={`study-preset-${mins}`}
                  onClick={() => setDailyMinutes(mins)}
                  className={`rounded-xl border-2 py-3 text-center text-sm font-bold transition-all ${
                    dailyMinutes === mins
                      ? 'border-teal-500 bg-teal-50 text-teal-700 shadow-sm dark:bg-teal-900/20 dark:text-teal-300'
                      : 'border-slate-200 bg-white text-slate-600 hover:border-slate-300 dark:border-slate-700 dark:bg-slate-800 dark:text-slate-300 dark:hover:border-slate-600'
                  }`}
                >
                  {mins} min
                </button>
              ))}
            </div>
            <div className="mt-4 flex items-center justify-between rounded-xl bg-slate-50 dark:bg-slate-800 px-4 py-3">
              <div>
                <p className="text-xs text-slate-400 dark:text-slate-500">Estimated daily load</p>
                <p className="text-sm font-bold text-slate-700 dark:text-slate-200">
                  ~{questionsPerDay} questions / day
                </p>
              </div>
              <div className="text-right">
                <p className="text-xs text-slate-400 dark:text-slate-500">Study time</p>
                <p className="text-sm font-bold text-slate-700 dark:text-slate-200">
                  {dailyMinutes >= 60 ? `${Math.floor(dailyMinutes / 60)}h ${dailyMinutes % 60 > 0 ? `${dailyMinutes % 60}m` : ''}` : `${dailyMinutes}m`}
                </p>
              </div>
            </div>
            {studyMsg && (
              <div className={`mt-3 rounded-xl px-4 py-3 text-sm font-medium ${studyMsg.type === 'success' ? 'bg-emerald-50 dark:bg-emerald-900/30 text-emerald-700 dark:text-emerald-300' : 'bg-red-50 dark:bg-red-900/30 text-red-600 dark:text-red-300'}`}>
                {studyMsg.text}
              </div>
            )}
            {hasStudyChange && (
              <button
                onClick={handleStudySave}
                disabled={studySaving}
                data-testid="study-save-btn"
                className="mt-3 bg-teal-600 text-white font-bold py-2.5 px-6 rounded-xl text-sm hover:bg-teal-500 transition disabled:opacity-50"
              >
                {studySaving ? 'Saving...' : 'Save Study Plan'}
              </button>
            )}
          </div>

          {/* Password */}
          <div className="bg-white dark:bg-slate-900 shadow-card rounded-2xl p-5">
            <h2 className="text-sm font-bold uppercase tracking-wider text-slate-400 dark:text-slate-500 mb-4">
              <Lock className="h-4 w-4 inline mr-1" />
              Password & Security
            </h2>
            <p className="text-sm text-slate-500 dark:text-slate-400 mb-4">
              To change your password, use the password reset flow. We'll send a reset code to your email.
            </p>
            {passwordMsg && (
              <div className={`mb-4 rounded-xl px-4 py-3 text-sm font-medium ${passwordMsg.type === 'success' ? 'bg-emerald-50 dark:bg-emerald-900/30 text-emerald-700 dark:text-emerald-300' : 'bg-red-50 dark:bg-red-900/30 text-red-600 dark:text-red-300'}`}>
                {passwordMsg.text}
              </div>
            )}
            <button onClick={handlePasswordChange} disabled={passwordLoading}
              className="bg-teal-600 text-white font-bold py-2.5 px-6 rounded-xl text-sm hover:bg-teal-500 transition disabled:opacity-50">
              {passwordLoading ? 'Sending...' : 'Reset Password via Email'}
            </button>
          </div>
        </div>
      )}

      {/* Appearance Tab */}
      {activeTab === 'appearance' && (
        <div className="bg-white dark:bg-slate-900 shadow-card rounded-2xl p-5">
          <h2 className="text-sm font-bold uppercase tracking-wider text-slate-400 dark:text-slate-500 mb-4">Theme</h2>
          <div className="grid grid-cols-2 gap-3">
            <button onClick={() => setTheme('light')}
              className={`flex flex-col items-center gap-3 rounded-xl border-2 p-5 transition-all ${theme === 'light' ? 'border-teal-500 bg-teal-50 dark:bg-teal-900/20' : 'border-slate-200 dark:border-slate-700 hover:border-slate-300 dark:hover:border-slate-600'}`}>
              <Sun className={`h-8 w-8 ${theme === 'light' ? 'text-teal-600' : 'text-slate-400 dark:text-slate-500'}`} />
              <span className={`text-sm font-bold ${theme === 'light' ? 'text-teal-700 dark:text-teal-300' : 'text-slate-600 dark:text-slate-300'}`}>Light</span>
            </button>
            <button onClick={() => setTheme('dark')}
              className={`flex flex-col items-center gap-3 rounded-xl border-2 p-5 transition-all ${theme === 'dark' ? 'border-teal-500 bg-teal-50 dark:bg-teal-900/20' : 'border-slate-200 dark:border-slate-700 hover:border-slate-300 dark:hover:border-slate-600'}`}>
              <Moon className={`h-8 w-8 ${theme === 'dark' ? 'text-teal-600 dark:text-teal-400' : 'text-slate-400 dark:text-slate-500'}`} />
              <span className={`text-sm font-bold ${theme === 'dark' ? 'text-teal-700 dark:text-teal-300' : 'text-slate-600 dark:text-slate-300'}`}>Dark</span>
            </button>
          </div>
        </div>
      )}

      {/* Support Tab */}
      {activeTab === 'support' && (
        <div className="space-y-5">
          {/* Quick Links */}
          <div className="bg-white dark:bg-slate-900 shadow-card rounded-2xl p-5">
            <h2 className="text-sm font-bold uppercase tracking-wider text-slate-400 dark:text-slate-500 mb-4">Help & Resources</h2>
            <div className="grid gap-2">
              <button onClick={() => { setShowFAQ(!showFAQ); setShowFeedback(false); }}
                data-testid="support-faq-btn"
                className={`flex items-center justify-between rounded-xl px-4 py-3 transition w-full text-left ${showFAQ ? 'bg-teal-50 dark:bg-teal-900/20 ring-1 ring-teal-200 dark:ring-teal-800' : 'bg-slate-50 dark:bg-slate-800 hover:bg-slate-100 dark:hover:bg-slate-700'}`}>
                <div className="flex items-center gap-3">
                  <HelpCircle className="h-4 w-4 text-teal-500" />
                  <span className="text-sm font-medium text-slate-700 dark:text-slate-200">Frequently Asked Questions</span>
                </div>
                <svg className={`h-4 w-4 text-slate-400 transition-transform dark:text-slate-500 ${showFAQ ? 'rotate-180' : ''}`} fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                  <path strokeLinecap="round" strokeLinejoin="round" d="M19 9l-7 7-7-7" />
                </svg>
              </button>
              <button onClick={() => { setShowFeedback(!showFeedback); setShowFAQ(false); }}
                data-testid="support-contact-btn"
                className={`flex items-center justify-between rounded-xl px-4 py-3 transition w-full text-left ${showFeedback ? 'bg-teal-50 dark:bg-teal-900/20 ring-1 ring-teal-200 dark:ring-teal-800' : 'bg-slate-50 dark:bg-slate-800 hover:bg-slate-100 dark:hover:bg-slate-700'}`}>
                <div className="flex items-center gap-3">
                  <MessageSquare className="h-4 w-4 text-teal-500" />
                  <span className="text-sm font-medium text-slate-700 dark:text-slate-200">Contact Support</span>
                </div>
              </button>
              <button onClick={() => { setShowFeedback(!showFeedback); setShowFAQ(false); }}
                className="flex items-center justify-between rounded-xl bg-slate-50 dark:bg-slate-800 px-4 py-3 hover:bg-slate-100 dark:hover:bg-slate-700 transition w-full text-left">
                <div className="flex items-center gap-3">
                  <AlertTriangle className="h-4 w-4 text-amber-500" />
                  <span className="text-sm font-medium text-slate-700 dark:text-slate-200">Report a Problem</span>
                </div>
              </button>
            </div>
          </div>

          {/* FAQ Accordion */}
          {showFAQ && (
            <div className="bg-white dark:bg-slate-900 shadow-card rounded-2xl p-5 animate-slide-down">
              <h2 className="text-sm font-bold uppercase tracking-wider text-slate-400 dark:text-slate-500 mb-3">Frequently Asked Questions</h2>
              <FAQAccordion />
            </div>
          )}

          {/* Feedback Form */}
          {showFeedback && (
            <div className="bg-white dark:bg-slate-900 shadow-card rounded-2xl p-5 animate-slide-down" data-testid="support-form">
              <h2 className="text-sm font-bold uppercase tracking-wider text-slate-400 dark:text-slate-500 mb-3">Send us a message</h2>
              <textarea
                value={feedbackText}
                onChange={(e) => setFeedbackText(e.target.value)}
                placeholder="Describe your issue or suggestion..."
                className="w-full rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 px-4 py-3 text-sm text-slate-700 dark:text-slate-200 placeholder-slate-400 dark:placeholder-slate-500 resize-none h-28 focus:outline-none focus:ring-2 focus:ring-teal-500"
              />
              {feedbackMsg && (
                <p className="mt-2 text-sm font-medium text-teal-600 dark:text-teal-400">{feedbackMsg}</p>
              )}
              <button onClick={handleFeedback} disabled={!feedbackText.trim()}
                className="mt-3 bg-teal-600 text-white font-bold py-2.5 px-6 rounded-xl text-sm hover:bg-teal-500 transition disabled:opacity-50">
                Send Message
              </button>
            </div>
          )}

          {/* My Tickets History */}
          {tickets.length > 0 && (
            <div className="bg-white dark:bg-slate-900 shadow-card rounded-2xl p-5">
              <button onClick={() => setShowTickets(!showTickets)}
                className="w-full flex items-center justify-between">
                <h2 className="text-sm font-bold uppercase tracking-wider text-slate-400 dark:text-slate-500">
                  My Tickets ({tickets.length})
                </h2>
                <svg className={`h-4 w-4 text-slate-400 transition-transform dark:text-slate-500 ${showTickets ? 'rotate-180' : ''}`} fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                  <path strokeLinecap="round" strokeLinejoin="round" d="M19 9l-7 7-7-7" />
                </svg>
              </button>
              {showTickets && (
                <div className="mt-3 space-y-2" data-testid="support-tickets">
                  {tickets.map(t => (
                    <div key={t.id} className="rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 p-3">
                      <div className="flex items-center justify-between mb-1">
                        <div className="flex items-center gap-2">
                          <span className="text-xs font-mono text-slate-400 dark:text-slate-500">#{t.id}</span>
                          {t.category && (
                            <span className="rounded-full bg-slate-200 dark:bg-slate-700 px-2 py-0.5 text-[10px] font-bold text-slate-600 dark:text-slate-300">
                              {t.category}
                            </span>
                          )}
                          <span className={`rounded-full px-2 py-0.5 text-[10px] font-bold ${
                            t.status === 'resolved' ? 'bg-emerald-100 text-emerald-700 dark:bg-emerald-900/30 dark:text-emerald-300' :
                            t.status === 'in_review' ? 'bg-blue-100 text-blue-700 dark:bg-blue-900/30 dark:text-blue-300' :
                            'bg-amber-100 text-amber-700 dark:bg-amber-900/30 dark:text-amber-300'
                          }`}>
                            {t.status === 'in_review' ? 'In Review' : t.status === 'resolved' ? 'Resolved' : 'Open'}
                          </span>
                        </div>
                        <span className="text-[10px] text-slate-400 dark:text-slate-500">
                          {t.created_at ? new Date(t.created_at).toLocaleDateString() : ''}
                        </span>
                      </div>
                      <p className="text-sm text-slate-700 dark:text-slate-200 line-clamp-2">{t.comment}</p>
                      {t.admin_response && (
                        <div className="mt-2 rounded-lg bg-teal-50 dark:bg-teal-900/20 border border-teal-200 dark:border-teal-800 px-3 py-2">
                          <p className="text-[10px] font-bold text-teal-600 dark:text-teal-400 mb-0.5">Admin Response</p>
                          <p className="text-sm text-teal-800 dark:text-teal-200">{t.admin_response}</p>
                        </div>
                      )}
                    </div>
                  ))}
                </div>
              )}
            </div>
          )}
        </div>
      )}
    </div>
  );
}
