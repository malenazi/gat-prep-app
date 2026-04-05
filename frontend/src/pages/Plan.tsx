import { useEffect, useMemo, useState } from 'react';
import type { LucideIcon } from 'lucide-react';
import {
  ArrowRight,
  BarChart3,
  BookOpen,
  Calculator,
  CalendarDays,
  CheckCircle2,
  Clock3,
  Coffee,
  DraftingCompass,
  Link2,
  PenTool,
  Search,
  Sigma,
  Target,
  Trophy,
} from 'lucide-react';

import { api } from '@/lib/api';
import { useAuth } from '@/hooks/useAuth';
import { pageShell, pageStack } from '@/lib/layout';
import type { FocusSkill, StudyPlanDay } from '@/types';

type PhaseKey = StudyPlanDay['phase'];

const phaseMeta: Record<
  PhaseKey,
  {
    label: string;
    range: string;
    description: string;
    surface: string;
    text: string;
    progress: string;
    accent: string;
  }
> = {
  foundation: {
    label: 'Foundation',
    range: 'Days 1-7',
    description: 'Build consistency around your weakest skills first.',
    surface: 'bg-sky-50 border-sky-200 dark:bg-sky-950/30 dark:border-sky-800',
    text: 'text-sky-700 dark:text-sky-300',
    progress: 'from-sky-400 to-blue-500',
    accent: 'bg-sky-500',
  },
  building: {
    label: 'Building',
    range: 'Days 8-22',
    description: 'Expand across all sections with steady daily practice.',
    surface: 'bg-teal-50 border-teal-200 dark:bg-teal-950/30 dark:border-teal-800',
    text: 'text-teal-700 dark:text-teal-300',
    progress: 'from-teal-400 to-emerald-500',
    accent: 'bg-teal-500',
  },
  peak: {
    label: 'Peak + Review',
    range: 'Days 23-30',
    description: 'Mix final sharpening, mock checkpoints, and recovery days.',
    surface: 'bg-amber-50 border-amber-200 dark:bg-amber-950/30 dark:border-amber-800',
    text: 'text-amber-700 dark:text-amber-300',
    progress: 'from-amber-400 to-orange-500',
    accent: 'bg-amber-500',
  },
};

const skillTopics: Record<
  string,
  {
    icon: LucideIcon;
    topics: string;
    tone: 'sky' | 'violet';
  }
> = {
  verbal_reading: {
    icon: BookOpen,
    topics: 'Text comprehension, extracting main ideas, inference.',
    tone: 'sky',
  },
  verbal_analogy: {
    icon: Link2,
    topics: 'Word relationships, analogies, and pattern matching.',
    tone: 'sky',
  },
  verbal_completion: {
    icon: PenTool,
    topics: 'Sentence completion, context clues, and vocabulary.',
    tone: 'sky',
  },
  verbal_error: {
    icon: Search,
    topics: 'Sentence accuracy, grammar, and contextual error spotting.',
    tone: 'sky',
  },
  verbal_oddword: {
    icon: Target,
    topics: 'Choosing the word that does not fit the group.',
    tone: 'sky',
  },
  quant_arithmetic: {
    icon: Calculator,
    topics: 'Operations, ratios, fractions, percentages, and equations.',
    tone: 'violet',
  },
  quant_geometry: {
    icon: DraftingCompass,
    topics: 'Areas, perimeters, angles, and geometric relationships.',
    tone: 'violet',
  },
  quant_algebra: {
    icon: Sigma,
    topics: 'Variables, equations, inequalities, and functions.',
    tone: 'violet',
  },
  quant_statistics: {
    icon: BarChart3,
    topics: 'Mean, median, probability, tables, and data interpretation.',
    tone: 'violet',
  },
};

function getRemainingQuestions(day: StudyPlanDay): number {
  return Math.max(0, day.target_questions - day.completed_questions);
}

function formatMinutes(minutes: number): string {
  if (minutes <= 0) return 'No timed session';
  if (minutes < 60) return `About ${minutes} min`;

  const hours = Math.floor(minutes / 60);
  const remainder = minutes % 60;
  return remainder > 0 ? `About ${hours} hr ${remainder} min` : `About ${hours} hr`;
}

function getEstimatedMinutes(day: StudyPlanDay, mode: 'assigned' | 'remaining' = 'assigned'): number {
  if (day.is_rest_day) return 0;
  if (day.is_mock_day) return 70;

  const questionCount = mode === 'remaining' ? getRemainingQuestions(day) : day.target_questions;
  return Math.max(15, Math.ceil(questionCount * 1.5));
}

function getFocusSummary(day: StudyPlanDay): string {
  if (!day.focus_skills?.length) {
    return day.is_mock_day
      ? 'Covers verbal and quantitative sections in one timed checkpoint.'
      : 'Balanced review across the current phase.';
  }

  return day.focus_skills.map((skill) => skill.name_ar).join(', ');
}

function getShortFocusSummary(day: StudyPlanDay): string {
  if (!day.focus_skills?.length) {
    return day.is_mock_day
      ? 'Timed verbal + quantitative simulation.'
      : 'Adaptive mixed-skill practice.';
  }

  const names = day.focus_skills.map((skill) => skill.name_ar);
  if (names.length <= 2) {
    return `Focus: ${names.join(' + ')}`;
  }

  return `Focus: ${names.slice(0, 2).join(' + ')} + ${names.length - 2} more`;
}

function getRoadmapTaskLabel(day: StudyPlanDay): string {
  if (day.is_rest_day) return 'Rest day';
  if (day.is_mock_day) return 'Mock checkpoint';
  return 'Practice session';
}

function getRoadmapPrimaryValue(day: StudyPlanDay, task: ReturnType<typeof getDayTaskMeta>): string {
  if (day.is_rest_day) return 'Recovery';
  if (day.is_mock_day) return task.estimate;
  return `${day.target_questions} questions`;
}

function getRoadmapSecondaryValue(day: StudyPlanDay, task: ReturnType<typeof getDayTaskMeta>): string {
  if (day.is_rest_day) return 'Reset, recover, and review lightly.';
  if (day.is_mock_day) return task.detail;
  return getShortFocusSummary(day);
}

function getRoadmapFooter(day: StudyPlanDay, remainingQuestions: number, task: ReturnType<typeof getDayTaskMeta>): string {
  if (day.is_rest_day) {
    return day.completed ? 'Recovery complete' : 'Recovery scheduled';
  }

  if (day.completed) {
    return day.is_mock_day ? 'Mock completed' : 'Completed';
  }

  if (day.is_today) {
    return day.is_mock_day ? 'Ready to start today' : `${remainingQuestions} left today`;
  }

  return day.is_mock_day ? task.estimate : task.estimate;
}

function getDayTaskMeta(day: StudyPlanDay): {
  eyebrow: string;
  title: string;
  detail: string;
  estimate: string;
  icon: LucideIcon;
} {
  if (day.is_rest_day) {
    return {
      eyebrow: 'Recovery',
      title: 'Rest day',
      detail: 'Recharge, review lightly, and return with a fresh mind.',
      estimate: 'No timed work',
      icon: Coffee,
    };
  }

  if (day.is_mock_day) {
    return {
      eyebrow: 'Checkpoint',
      title: 'Full mock exam',
      detail: 'Timed verbal and quantitative simulation.',
      estimate: 'About 70 min',
      icon: Trophy,
    };
  }

  return {
    eyebrow: 'Practice block',
    title: `${day.target_questions} practice questions`,
    detail: day.focus_skills?.length
      ? `Focus on ${getFocusSummary(day)}`
      : 'Targeted skills selected from your study phase.',
    estimate: formatMinutes(getEstimatedMinutes(day)),
    icon: Target,
  };
}

function getDayState(day: StudyPlanDay): {
  label: string;
  chipClass: string;
  cardClass: string;
  borderClass: string;
} {
  if (day.completed) {
    return {
      label: 'Completed',
      chipClass: 'bg-emerald-100 text-emerald-700 dark:bg-emerald-900/40 dark:text-emerald-300',
      cardClass: 'bg-emerald-50/70 dark:bg-emerald-950/30',
      borderClass: 'border-emerald-300 dark:border-emerald-800',
    };
  }

  if (day.is_today) {
    return {
      label: 'Today',
      chipClass: 'bg-teal-100 text-teal-700 dark:bg-teal-900/40 dark:text-teal-300',
      cardClass: 'bg-teal-50/80 dark:bg-teal-950/30',
      borderClass: 'border-teal-400 dark:border-teal-600',
    };
  }

  return {
    label: 'Upcoming',
    chipClass: 'bg-slate-100 text-slate-600 dark:bg-slate-800 dark:text-slate-400',
    cardClass: 'bg-white dark:bg-slate-900 hover:bg-slate-50 dark:hover:bg-slate-800',
    borderClass: 'border-slate-200 dark:border-slate-800',
  };
}

function SkillDetailCard({ skill }: { skill: FocusSkill }) {
  const info = skillTopics[skill.id] ?? {
    icon: Target,
    topics: 'Targeted revision from your personalized plan.',
    tone: skill.id.startsWith('verbal') ? 'sky' : 'violet',
  };
  const Icon = info.icon;
  const toneClasses =
    info.tone === 'sky'
      ? 'bg-sky-50 border-sky-200 text-sky-700'
      : 'bg-violet-50 border-violet-200 text-violet-700';

  return (
    <div className={`rounded-2xl border p-4 ${toneClasses}`}>
      <div className="flex items-start gap-3">
        <div className="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-white/80 shadow-sm">
          <Icon className="h-5 w-5" />
        </div>
        <div>
          <p className="text-sm font-bold">{skill.name_ar}</p>
          <p className="mt-1 text-sm leading-relaxed text-slate-600 dark:text-slate-300">{info.topics}</p>
        </div>
      </div>
    </div>
  );
}

function SkeletonCard({ className = '' }: { className?: string }) {
  return <div className={`animate-pulse rounded-3xl ${className}`} />;
}

export default function Plan() {
  const { user } = useAuth();
  const [plan, setPlan] = useState<StudyPlanDay[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [selectedDay, setSelectedDay] = useState<StudyPlanDay | null>(null);

  const loadData = async () => {
    setLoading(true);
    setError('');
    try {
      setPlan(await api.studyPlan());
    } catch (e: unknown) {
      setError(e instanceof Error ? e.message : 'Error occurred');
    }
    setLoading(false);
  };

  useEffect(() => {
    void loadData();
  }, []);

  useEffect(() => {
    if (!plan.length || selectedDay) return;
    const today = plan.find((day) => day.is_today) ?? plan[0];
    setSelectedDay(today);
  }, [plan, selectedDay]);

  const today = useMemo(() => plan.find((day) => day.is_today) ?? null, [plan]);
  const completedDays = useMemo(() => plan.filter((day) => day.completed).length, [plan]);
  const activePhase = today ? phaseMeta[today.phase] : phaseMeta.foundation;
  const todayTask = today ? getDayTaskMeta(today) : null;

  if (loading) {
    return (
      <div className={`${pageShell.wide} ${pageStack}`}>
        <SkeletonCard className="bg-white dark:bg-slate-900 shadow-card h-48" />
        <SkeletonCard className="bg-white dark:bg-slate-900 shadow-card h-52" />
        <SkeletonCard className="bg-white dark:bg-slate-900 shadow-card h-80" />
      </div>
    );
  }

  if (error) {
    return (
      <div className="min-h-[60vh] flex flex-col items-center justify-center p-6 text-center">
        <CalendarDays className="mb-4 h-12 w-12 text-red-400" />
        <p className="mb-4 text-sm text-red-500">{error}</p>
        <button
          onClick={() => {
            void loadData();
          }}
          className="rounded-2xl bg-teal-600 px-8 py-3 font-bold text-white shadow-brand"
        >
          Retry
        </button>
      </div>
    );
  }

  return (
    <div className={`${pageShell.wide} ${pageStack} page-enter text-slate-800 dark:text-slate-100`} data-testid="plan-page">
      <section className="overflow-hidden rounded-[2rem] border border-teal-100 dark:border-teal-900 bg-[radial-gradient(circle_at_top_left,_rgba(45,212,191,0.16),_transparent_48%),linear-gradient(135deg,_#f8fffe,_#eefaf8_45%,_#ffffff)] dark:bg-[radial-gradient(circle_at_top_left,_rgba(45,212,191,0.08),_transparent_48%),linear-gradient(135deg,_#0f172a,_#0f1e2a_45%,_#0f172a)] p-6 shadow-card-lg lg:p-8">
        <div className="flex flex-col gap-6 lg:flex-row lg:items-start lg:justify-between">
          <div className="max-w-2xl">
            <div className="inline-flex items-center gap-2 rounded-full bg-white/80 dark:bg-slate-950/80 px-3 py-1 text-xs font-black uppercase tracking-[0.18em] text-teal-700 dark:text-teal-300 shadow-sm">
              <CalendarDays className="h-3.5 w-3.5" />
              30-day roadmap
            </div>
            <h1 className="mt-4 text-3xl font-black tracking-tight text-slate-900 lg:text-5xl dark:text-slate-100">Study Plan</h1>
            <p className="mt-3 max-w-2xl text-sm leading-relaxed text-slate-600 dark:text-slate-300 lg:text-base">
              Follow a clearer daily roadmap with practice blocks, mock checkpoints, and recovery days. Select any day to see the workload, timing, and skills behind it.
            </p>
            <p className="mt-3 text-sm font-medium text-slate-500">
              Day {user?.current_day || 0} of 30 and currently in <span className={`font-bold ${activePhase.text}`}>{activePhase.label}</span>.
            </p>
          </div>

          <div className="grid gap-3 sm:grid-cols-2 xl:min-w-[460px] xl:grid-cols-3">
            <div className="rounded-3xl border border-white/80 bg-white/80 dark:bg-slate-950/80 dark:border-slate-800 p-4 shadow-sm stat-card-shine">
              <p className="text-xs font-bold uppercase tracking-[0.16em] text-slate-400">Progress</p>
              <p className="mt-2 text-2xl font-black text-slate-900 dark:text-slate-100">{completedDays}<span className="text-base text-slate-400"> / {plan.length}</span></p>
              <p className="mt-1 text-sm text-slate-500">Days completed</p>
            </div>

            <div className="rounded-3xl border border-white/80 bg-white/80 dark:bg-slate-950/80 dark:border-slate-800 p-4 shadow-sm stat-card-shine">
              <p className="text-xs font-bold uppercase tracking-[0.16em] text-slate-400">Today</p>
              <p className="mt-2 text-base font-black text-slate-900 dark:text-slate-100">{todayTask?.title ?? 'Roadmap ready'}</p>
              <p className="mt-1 text-sm text-slate-500">{todayTask?.estimate ?? 'Select a day to inspect the plan.'}</p>
            </div>

            <div className={`rounded-3xl border p-4 shadow-sm stat-card-shine ${activePhase.surface}`}>
              <p className="text-xs font-bold uppercase tracking-[0.16em] text-slate-400">Current phase</p>
              <p className={`mt-2 text-base font-black ${activePhase.text}`}>{activePhase.label}</p>
              <p className="mt-1 text-sm text-slate-500">{activePhase.range}</p>
            </div>
          </div>
        </div>
      </section>

      <section className="grid gap-4 xl:grid-cols-3" data-testid="plan-phase-progress">
        {Object.entries(phaseMeta).map(([phaseKey, info]) => {
          const phaseDays = plan.filter((day) => day.phase === phaseKey);
          const phaseCompleted = phaseDays.filter((day) => day.completed).length;
          const phasePercent = phaseDays.length ? (phaseCompleted / phaseDays.length) * 100 : 0;
          const isCurrent = today?.phase === phaseKey;

          return (
            <article
              key={phaseKey}
              className={`rounded-3xl border p-5 shadow-card ${info.surface}`}
            >
              <div className="flex items-start justify-between gap-4">
                <div>
                  <p className={`text-lg font-black ${info.text}`}>{info.label}</p>
                  <p className="mt-1 text-sm text-slate-500">{info.range}</p>
                </div>
                {isCurrent && (
                  <span className="rounded-full bg-white/90 dark:bg-slate-800 px-3 py-1 text-xs font-bold uppercase tracking-[0.16em] text-slate-700 dark:text-slate-300">
                    Current
                  </span>
                )}
              </div>

              <p className="mt-4 text-sm leading-relaxed text-slate-600 dark:text-slate-400">{info.description}</p>

              <div className="mt-5 flex items-end justify-between gap-4">
                <div>
                  <p className="text-2xl font-black text-slate-900 dark:text-slate-100">{phaseCompleted}<span className="text-base text-slate-400"> / {phaseDays.length}</span></p>
                  <p className="text-sm text-slate-500 dark:text-slate-400">days finished in this phase</p>
                </div>
                <p className={`text-sm font-bold ${info.text}`}>{Math.round(phasePercent)}%</p>
              </div>

              <div className="mt-3 h-2.5 overflow-hidden rounded-full bg-white/80 dark:bg-slate-800">
                <div
                  className={`h-full rounded-full bg-gradient-to-r ${info.progress} transition-all duration-700 animate-bar-fill`}
                  style={{ width: `${phasePercent}%` }}
                />
              </div>
            </article>
          );
        })}
      </section>

      <div className="plan-layout">
        <section className="rounded-[2rem] border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 p-5 shadow-card lg:p-6" data-testid="plan-roadmap">
          <div className="flex flex-col gap-4 xl:flex-row xl:items-start xl:justify-between">
            <div>
              <h2 className="text-xl font-black text-slate-900 dark:text-slate-100">Daily roadmap</h2>
              <p className="mt-1 text-sm text-slate-500">
                Scan the next few days quickly, then select any card for the full breakdown below or in the side panel on wider screens.
              </p>
            </div>

            <div className="min-w-0 xl:max-w-[22rem]">
              <div className="plan-legend-grid text-xs font-bold uppercase tracking-[0.14em]" data-testid="plan-legend">
                <span className="rounded-full bg-emerald-100 dark:bg-emerald-900/40 px-3 py-1 text-center text-emerald-700 dark:text-emerald-300">Completed</span>
                <span className="rounded-full bg-teal-100 dark:bg-teal-900/40 px-3 py-1 text-center text-teal-700 dark:text-teal-300">Today</span>
                <span className="rounded-full bg-white dark:bg-slate-900 px-3 py-1 text-center text-slate-600 dark:text-slate-400 ring-1 ring-slate-200 dark:ring-slate-700">Upcoming</span>
              </div>
              <p className="mt-2 text-xs leading-relaxed text-slate-500">
                Mock checkpoints and rest days are labeled directly on each card, so the roadmap stays easier to scan.
              </p>
            </div>
          </div>

          <div className="plan-roadmap-grid mt-6" data-testid="plan-roadmap-grid">
            {plan.map((day) => {
              const phaseInfo = phaseMeta[day.phase];
              const task = getDayTaskMeta(day);
              const dayState = getDayState(day);
              const isSelected = selectedDay?.day === day.day;
              const remainingQuestions = getRemainingQuestions(day);
              const completionPercent = day.target_questions > 0
                ? Math.min(100, (day.completed_questions / day.target_questions) * 100)
                : day.completed
                  ? 100
                  : 0;
              const cardLabel = getRoadmapTaskLabel(day);
              const primaryValue = getRoadmapPrimaryValue(day, task);
              const secondaryValue = getRoadmapSecondaryValue(day, task);
              const footerValue = getRoadmapFooter(day, remainingQuestions, task);

              return (
                <button
                  key={day.day}
                  onClick={() => setSelectedDay(day)}
                  data-testid={`plan-day-${day.day}`}
                  className={`group flex min-h-[18rem] flex-col rounded-3xl border p-4 text-left transition-all interactive-press ${day.is_today ? 'animate-glow-ring' : ''} ${dayState.cardClass} ${dayState.borderClass} ${isSelected ? 'ring-2 ring-teal-500/20 shadow-lg' : 'shadow-sm hover:-translate-y-0.5 hover:shadow-md'}`}
                >
                  <div className="flex items-start justify-between gap-3">
                    <div>
                      <p className="text-xs font-bold uppercase tracking-[0.16em] text-slate-400 dark:text-slate-500">Day</p>
                      <p className="mt-1 text-2xl font-black text-slate-900 dark:text-slate-100">{day.day}</p>
                    </div>
                    <span className={`rounded-full px-2.5 py-1 text-[11px] font-bold uppercase tracking-[0.14em] ${dayState.chipClass}`}>
                      {dayState.label}
                    </span>
                  </div>

                  <p className="mt-4 text-xs font-bold uppercase tracking-[0.14em] text-slate-500">
                    {cardLabel} • {phaseInfo.label}
                  </p>

                  <p className="mt-3 text-[1.75rem] font-black leading-tight text-slate-900 dark:text-slate-100">{primaryValue}</p>
                  <p className="mt-2 min-h-[2.8rem] text-sm leading-relaxed text-slate-500 dark:text-slate-400">
                    {secondaryValue}
                  </p>

                  {!day.is_rest_day ? (
                    <div className="mt-auto pt-5">
                      <div className="mb-2 flex items-center justify-between text-xs font-medium text-slate-500">
                        <span>{footerValue}</span>
                        <span>{day.completed ? '100%' : `${Math.round(completionPercent)}%`}</span>
                      </div>
                      <div className="h-2 overflow-hidden rounded-full bg-slate-100 dark:bg-slate-700">
                        <div
                          className={`h-full rounded-full bg-gradient-to-r ${phaseInfo.progress}`}
                          style={{ width: `${completionPercent}%` }}
                        />
                      </div>
                    </div>
                  ) : (
                    <div className="mt-auto pt-5">
                      <div className="rounded-2xl bg-slate-100 dark:bg-slate-800 px-3 py-2 text-xs font-semibold text-slate-500 dark:text-slate-400">
                        {footerValue}
                      </div>
                    </div>
                  )}
                </button>
              );
            })}
          </div>
        </section>

        <aside className="plan-roadmap-detail">
          {selectedDay ? (
            <div className="rounded-[2rem] border border-slate-200 bg-white dark:bg-slate-900 p-6 shadow-card-lg animate-fade-in" data-testid="plan-detail">
              {(() => {
                const phaseInfo = phaseMeta[selectedDay.phase];
                const dayState = getDayState(selectedDay);
                const task = getDayTaskMeta(selectedDay);
                const TaskIcon = task.icon;
                const remainingQuestions = getRemainingQuestions(selectedDay);
                const assignedMinutes = getEstimatedMinutes(selectedDay, 'assigned');
                const remainingMinutes = getEstimatedMinutes(selectedDay, 'remaining');
                const completionPercent = selectedDay.target_questions > 0
                  ? Math.min(100, (selectedDay.completed_questions / selectedDay.target_questions) * 100)
                  : selectedDay.completed
                    ? 100
                    : 0;

                return (
                  <>
                    <div className="flex items-start justify-between gap-4">
                      <div>
                        <p className="text-sm font-medium text-slate-400">Selected day</p>
                        <h3 className="mt-1 text-2xl font-black text-slate-900 dark:text-slate-100">Day {selectedDay.day}</h3>
                        <p className="mt-1 text-sm text-slate-500">{phaseInfo.label}</p>
                      </div>
                      <span className={`rounded-full px-3 py-1 text-xs font-bold uppercase tracking-[0.14em] ${dayState.chipClass}`}>
                        {dayState.label}
                      </span>
                    </div>

                    <div className={`mt-5 rounded-3xl border p-5 ${phaseInfo.surface}`}>
                      <div className="flex items-start gap-4">
                        <div className="flex h-14 w-14 shrink-0 items-center justify-center rounded-2xl bg-white/90 dark:bg-slate-800 shadow-sm">
                          <TaskIcon className={`h-6 w-6 ${phaseInfo.text}`} />
                        </div>
                        <div>
                          <p className="text-xs font-bold uppercase tracking-[0.16em] text-slate-400">{task.eyebrow}</p>
                          <p className="mt-1 text-xl font-black text-slate-900 dark:text-slate-100">{task.title}</p>
                          <p className="mt-2 text-sm leading-relaxed text-slate-600 dark:text-slate-300">{task.detail}</p>
                        </div>
                      </div>
                    </div>

                    <div className="mt-5 grid gap-3 sm:grid-cols-2">
                      <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-800/50 p-4">
                        <div className="flex items-center gap-2 text-slate-500">
                          <CalendarDays className="h-4 w-4" />
                          <p className="text-xs font-bold uppercase tracking-[0.14em]">Assigned work</p>
                        </div>
                        <p className="mt-3 text-lg font-black text-slate-900 dark:text-slate-100">
                          {selectedDay.is_mock_day ? 'Full mock exam' : selectedDay.is_rest_day ? 'Recovery day' : `${selectedDay.target_questions} questions`}
                        </p>
                        <p className="mt-1 text-sm text-slate-500">
                          {selectedDay.is_rest_day ? 'Use this day to recover and reset.' : formatMinutes(assignedMinutes)}
                        </p>
                      </div>

                      <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-800/50 p-4">
                        <div className="flex items-center gap-2 text-slate-500">
                          <Clock3 className="h-4 w-4" />
                          <p className="text-xs font-bold uppercase tracking-[0.14em]">Current status</p>
                        </div>
                        <p className="mt-3 text-lg font-black text-slate-900 dark:text-slate-100">
                          {selectedDay.is_rest_day
                            ? selectedDay.completed
                              ? 'Recovery complete'
                              : 'Recovery planned'
                            : selectedDay.completed
                              ? 'Session completed'
                              : `${remainingQuestions} questions left`}
                        </p>
                        <p className="mt-1 text-sm text-slate-500">
                          {selectedDay.is_rest_day ? 'No timed session required.' : formatMinutes(remainingMinutes)}
                        </p>
                      </div>
                    </div>

                    {!selectedDay.is_rest_day && (
                      <div className="mt-5 rounded-2xl border border-slate-200 bg-white dark:bg-slate-900 p-4">
                        <div className="mb-3 flex items-center justify-between text-sm">
                          <p className="font-bold text-slate-700">Completion</p>
                          <p className="font-semibold text-slate-500">
                            {selectedDay.is_mock_day
                              ? selectedDay.completed
                                ? 'Finished'
                                : 'Not started'
                              : `${selectedDay.completed_questions} of ${selectedDay.target_questions} completed`}
                          </p>
                        </div>
                        <div className="h-2.5 overflow-hidden rounded-full bg-slate-100">
                          <div
                            className={`h-full rounded-full bg-gradient-to-r ${phaseInfo.progress}`}
                            style={{ width: `${completionPercent}%` }}
                          />
                        </div>
                      </div>
                    )}

                    <div className="mt-5 rounded-2xl border border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-800/50 p-4">
                      <p className="text-xs font-bold uppercase tracking-[0.14em] text-slate-400">Why this day matters</p>
                      <p className="mt-2 text-sm leading-relaxed text-slate-600 dark:text-slate-300">
                        {selectedDay.is_rest_day
                          ? 'Recovery days keep your pace sustainable across the 30-day plan.'
                          : selectedDay.is_mock_day
                            ? 'Mock days simulate exam pressure and show whether your accuracy holds under time limits.'
                            : phaseInfo.description}
                      </p>
                    </div>

                    {selectedDay.focus_skills?.length > 0 && !selectedDay.is_mock_day && !selectedDay.is_rest_day && (
                      <div className="mt-5 border-t border-slate-100 dark:border-slate-800 pt-5">
                        <p className="text-sm font-black text-slate-900 dark:text-slate-100">Focus skills</p>
                        <p className="mt-1 text-sm text-slate-500">
                          This practice block concentrates on {getFocusSummary(selectedDay)}.
                        </p>
                        <div className="mt-4 space-y-3">
                          {selectedDay.focus_skills.map((skill) => (
                            <SkillDetailCard key={skill.id} skill={skill} />
                          ))}
                        </div>
                      </div>
                    )}

                    {selectedDay.is_mock_day && (
                      <div className="mt-5 rounded-2xl border border-amber-200 dark:border-amber-800 bg-amber-50 dark:bg-amber-950/30 p-4">
                        <div className="flex items-start gap-3">
                          <Trophy className="mt-0.5 h-5 w-5 shrink-0 text-amber-600" />
                          <div>
                            <p className="text-sm font-bold text-amber-800 dark:text-amber-200">What to expect</p>
                            <p className="mt-1 text-sm leading-relaxed text-amber-700">
                              A full timed simulation with verbal and quantitative sections, no live feedback during the exam, and review after the attempt finishes.
                            </p>
                          </div>
                        </div>
                      </div>
                    )}

                    {selectedDay.completed && (
                      <div className="mt-5 rounded-2xl border border-emerald-200 dark:border-emerald-800 bg-emerald-50 dark:bg-emerald-950/30 px-4 py-3 text-sm font-bold text-emerald-700 dark:text-emerald-300">
                        <div className="flex items-center gap-2">
                          <CheckCircle2 className="h-4 w-4" />
                          Day {selectedDay.day} is complete.
                        </div>
                      </div>
                    )}

                    {selectedDay.is_today && !selectedDay.completed && !selectedDay.is_rest_day && (
                      <a
                        href={selectedDay.is_mock_day ? '/mock' : '/practice'}
                        className="mt-5 inline-flex w-full items-center justify-center gap-2 rounded-2xl bg-gradient-to-r from-teal-600 to-teal-500 px-4 py-3 text-sm font-bold text-white shadow-brand transition-all hover:shadow-lg"
                      >
                        Open today&apos;s session
                        <ArrowRight className="h-4 w-4" />
                      </a>
                    )}
                  </>
                );
              })()}
            </div>
          ) : (
            <div className="rounded-[2rem] border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 p-6 text-center text-slate-500 dark:text-slate-400 shadow-card">
              <p className="text-sm">Select a day to view details.</p>
            </div>
          )}
        </aside>
      </div>
    </div>
  );
}
