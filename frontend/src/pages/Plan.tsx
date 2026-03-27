import { useState, useEffect } from 'react';
import { api } from '@/lib/api';
import { useAuth } from '@/hooks/useAuth';
import type { StudyPlanDay, FocusSkill } from '@/types';

const skillTopics: Record<string, { icon: string; topics: string }> = {
  verbal_reading: { icon: '📖', topics: 'Text comprehension, extracting main ideas, inference' },
  verbal_analogy: { icon: '🔗', topics: 'Word relationships, logical analogies' },
  verbal_completion: { icon: '✏️', topics: 'Sentence completion, context understanding, vocabulary' },
  verbal_error: { icon: '🔍', topics: 'Identifying linguistic and grammatical errors in sentences' },
  verbal_oddword: { icon: '🎯', topics: 'Identifying the different word in a group' },
  quant_arithmetic: { icon: '🔢', topics: 'Arithmetic operations, ratios, fractions, equations' },
  quant_geometry: { icon: '📐', topics: 'Areas, perimeters, angles, geometric shapes' },
  quant_algebra: { icon: '📊', topics: 'Variables, equations, inequalities, functions' },
  quant_statistics: { icon: '📈', topics: 'Mean, median, mode, probability' },
};

function SkillDetailCard({ skill }: { skill: FocusSkill }) {
  const info = skillTopics[skill.id] || { icon: '📚', topics: '' };
  const isVerbal = skill.id?.startsWith('verbal');
  return (
    <div className={`rounded-xl p-3 border ${isVerbal ? 'bg-blue-50/50 border-blue-100' : 'bg-purple-50/50 border-purple-100'}`}>
      <div className="flex items-center gap-2 mb-1">
        <span className="text-base">{info.icon}</span>
        <span className={`text-sm font-bold ${isVerbal ? 'text-blue-700' : 'text-purple-700'}`}>{skill.name_ar}</span>
      </div>
      {info.topics && (
        <p className="text-slate-500 text-sm leading-relaxed mr-7">{info.topics}</p>
      )}
    </div>
  );
}

function SkeletonCard({ className = '' }: { className?: string }) {
  return <div className={`animate-pulse rounded-2xl ${className}`} />;
}

export default function Plan() {
  const { user } = useAuth();
  const [plan, setPlan] = useState<StudyPlanDay[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [selectedDay, setSelectedDay] = useState<StudyPlanDay | null>(null);

  const loadData = async () => {
    setLoading(true); setError('');
    try { setPlan(await api.studyPlan()); }
    catch (e: unknown) { setError(e instanceof Error ? e.message : 'Error occurred'); }
    setLoading(false);
  };

  useEffect(() => { loadData(); }, []);

  // Auto-select today
  useEffect(() => {
    if (plan.length > 0) {
      const today = plan.find(d => d.is_today);
      if (today && (!selectedDay || selectedDay.day !== today.day)) {
        setSelectedDay(today);
      }
    }
  }, [plan]);

  if (loading) return (
    <div className="p-6 lg:p-10 max-w-6xl mx-auto space-y-6">
      <SkeletonCard className="bg-white shadow-card h-20" />
      <SkeletonCard className="bg-white shadow-card h-64" />
    </div>
  );

  if (error) return (
    <div className="min-h-[60vh] flex flex-col items-center justify-center p-6 text-center">
      <div className="text-5xl mb-4">⚠️</div>
      <p className="text-red-500 text-sm mb-4">{error}</p>
      <button onClick={loadData} className="bg-teal-600 text-white font-bold py-2.5 px-8 rounded-xl shadow-brand">Retry</button>
    </div>
  );

  const completedDays = plan.filter(d => d.completed).length;
  const phases = [
    { key: 'foundation' as const, label: 'Foundation', range: '1-7', color: 'from-blue-400 to-blue-500', bg: 'bg-blue-400', days: 7 },
    { key: 'building' as const, label: 'Building', range: '8-22', color: 'from-teal-400 to-teal-500', bg: 'bg-teal-400', days: 15 },
    { key: 'peak' as const, label: 'Mastery', range: '23-30', color: 'from-amber-400 to-amber-500', bg: 'bg-amber-400', days: 8 },
  ];

  return (
    <div className="p-3 lg:p-10 max-w-6xl mx-auto page-enter">
      <div className="flex items-center justify-between mb-4 lg:mb-6">
        <div>
          <h1 className="text-2xl lg:text-3xl font-black text-slate-800">Study Plan</h1>
          <p className="text-slate-500 text-sm mt-1">30 Days • Scientific Track • Day {user?.current_day || 0}</p>
        </div>
        <div className="bg-white shadow-card rounded-xl px-4 py-2 text-sm">
          <span className="text-teal-600 font-bold">{completedDays}</span>
          <span className="text-slate-500">/{plan.length} days</span>
        </div>
      </div>

      {/* Phase Progress Bar */}
      <div className="bg-white shadow-card rounded-2xl p-5 mb-4 lg:mb-6">
        <div className="flex gap-1 lg:gap-2 items-center">
          {phases.map((ph) => {
            const phDays = plan.filter(d => d.phase === ph.key);
            const phCompleted = phDays.filter(d => d.completed).length;
            const phPct = phDays.length > 0 ? (phCompleted / phDays.length) * 100 : 0;
            const isCurrent = plan.find(d => d.is_today)?.phase === ph.key;
            return (
              <div key={ph.key} className="flex-1">
                <div className="flex items-center justify-between mb-1.5">
                  <span className={`text-sm font-bold ${isCurrent ? 'text-slate-700' : 'text-slate-500'}`}>{ph.label}</span>
                  <span className="text-sm text-slate-500">{ph.range}</span>
                </div>
                <div className="h-2.5 bg-slate-100 rounded-full overflow-hidden">
                  <div className={`h-full bg-gradient-to-l ${ph.color} rounded-full transition-all duration-700`} style={{ width: `${phPct}%` }} />
                </div>
              </div>
            );
          })}
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-[1fr_320px] gap-3 lg:gap-6">
        {/* Calendar Grid */}
        <div className="bg-white shadow-card rounded-2xl p-5 lg:p-6">
          <div className="grid grid-cols-6 md:grid-cols-6 lg:grid-cols-10 gap-2">
            {plan.map(day => {
              const isCurrent = day.is_today;
              const isSelected = selectedDay?.day === day.day;
              const pct = day.target_questions > 0 ? Math.min(1, day.completed_questions / day.target_questions) : 0;

              let bgColor = 'bg-white hover:bg-slate-50';
              if (day.completed) bgColor = 'bg-emerald-50 hover:bg-emerald-100';
              else if (isCurrent) bgColor = 'bg-teal-50 hover:bg-teal-100';

              let borderColor = 'border-slate-200';
              if (isSelected) borderColor = 'border-teal-500 ring-2 ring-teal-500/20';
              else if (isCurrent) borderColor = 'border-teal-400';
              else if (day.completed) borderColor = 'border-emerald-300';

              const phaseColor = day.phase === 'foundation' ? 'bg-blue-400' : day.phase === 'building' ? 'bg-teal-400' : 'bg-amber-400';

              return (
                <button key={day.day} onClick={() => setSelectedDay(day)}
                  className={`${bgColor} border ${borderColor} rounded-xl p-1.5 lg:p-2.5 text-center relative overflow-hidden transition-all cursor-pointer`}>
                  <div className={`absolute top-1 left-1 w-1.5 h-1.5 rounded-full ${phaseColor}`} />
                  <div className={`font-bold text-sm ${isCurrent ? 'text-teal-600' : day.completed ? 'text-emerald-500' : 'text-slate-500'}`}>
                    {day.day}
                  </div>
                  {day.is_mock_day && <div className="text-sm text-amber-500 font-medium">Mock</div>}
                  {day.is_rest_day && <div className="text-sm text-slate-500">Rest</div>}
                  {!day.is_mock_day && !day.is_rest_day && (
                    <div className="mt-1">
                      {day.completed ? (
                        <span className="text-emerald-500 text-sm">✓</span>
                      ) : isCurrent && pct > 0 ? (
                        <div className="h-1 bg-slate-200 rounded-full overflow-hidden">
                          <div className="h-full bg-teal-400 rounded-full" style={{ width: `${pct * 100}%` }} />
                        </div>
                      ) : (
                        <span className="text-slate-500 text-sm">{day.target_questions}Q</span>
                      )}
                    </div>
                  )}
                </button>
              );
            })}
          </div>
        </div>

        {/* Day Detail Panel */}
        <div className="lg:sticky lg:top-24">
          {selectedDay ? (
            <div className="bg-white shadow-card rounded-2xl p-6 animate-fade-in">
              <div className="flex items-center justify-between mb-4">
                <h3 className="text-slate-800 font-bold text-lg">Day {selectedDay.day}</h3>
                <span className={`text-sm font-bold px-3 py-1 rounded-full
                  ${selectedDay.phase === 'foundation' ? 'bg-blue-50 text-blue-600' :
                    selectedDay.phase === 'building' ? 'bg-teal-50 text-teal-600' : 'bg-amber-50 text-amber-600'}`}>
                  {selectedDay.phase === 'foundation' ? 'التأسيس' : selectedDay.phase === 'building' ? 'التعزيز' : 'الإتقان'}
                </span>
              </div>

              {selectedDay.is_rest_day ? (
                <div className="text-center py-6">
                  <div className="text-4xl mb-2">😴</div>
                  <p className="text-slate-500">Rest Day</p>
                </div>
              ) : selectedDay.is_mock_day ? (
                <div className="text-center py-4">
                  <div className="text-4xl mb-2">📝</div>
                  <p className="text-slate-700 font-bold">Mock Exam</p>
                  <p className="text-slate-500 text-sm mt-1">{selectedDay.target_questions} questions</p>
                  <p className="text-slate-500 text-sm mt-2 flex items-center justify-center gap-1">
                    <svg className="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}><path strokeLinecap="round" strokeLinejoin="round" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                    ~{Math.ceil(selectedDay.target_questions * 1.5)} minutes
                  </p>
                  <div className="mt-4 text-left">
                    <p className="text-slate-500 text-sm mb-2 font-medium">Covers all skills:</p>
                    <p className="text-slate-500 text-sm leading-relaxed">Verbal (comprehension, analogy, completion, contextual error) + Quant (arithmetic, geometry, algebra, statistics)</p>
                  </div>
                </div>
              ) : (
                <>
                  <div className="space-y-3 mb-4">
                    <div className="flex justify-between text-sm">
                      <span className="text-slate-500">Required</span>
                      <span className="text-slate-800 font-bold">{selectedDay.target_questions} questions</span>
                    </div>
                    <div className="flex justify-between text-sm">
                      <span className="text-slate-500">Completed</span>
                      <span className="text-teal-600 font-bold">{selectedDay.completed_questions}</span>
                    </div>
                    <div className="flex justify-between text-sm">
                      <span className="text-slate-500">Remaining</span>
                      <span className="text-slate-800 font-bold">{Math.max(0, selectedDay.target_questions - selectedDay.completed_questions)}</span>
                    </div>
                    {/* Estimated time */}
                    <div className="flex justify-between text-sm">
                      <span className="text-slate-500 flex items-center gap-1">
                        <svg className="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}><path strokeLinecap="round" strokeLinejoin="round" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                        Estimated Time
                      </span>
                      <span className="text-slate-600 font-bold">~{Math.ceil(Math.max(0, selectedDay.target_questions - selectedDay.completed_questions) * 1.5)} minutes</span>
                    </div>
                    {/* Progress bar */}
                    <div className="h-2 bg-slate-100 rounded-full overflow-hidden">
                      <div className="h-full bg-gradient-to-l from-teal-400 to-teal-600 rounded-full transition-all"
                        style={{ width: `${Math.min(100, (selectedDay.completed_questions / Math.max(1, selectedDay.target_questions)) * 100)}%` }} />
                    </div>
                  </div>

                  {/* Required Skills with descriptions */}
                  {selectedDay.focus_skills?.length > 0 && (
                    <div className="border-t border-slate-100 pt-4 mb-4">
                      <p className="text-slate-500 text-sm mb-3 font-bold">Required Skills</p>
                      <div className="space-y-2.5">
                        {selectedDay.focus_skills.map(s => (
                          <SkillDetailCard key={s.id} skill={s} />
                        ))}
                      </div>
                    </div>
                  )}

                  {/* Phase description */}
                  <div className="border-t border-slate-100 pt-4">
                    <p className="text-slate-500 text-sm mb-1 font-medium">Phase: {selectedDay.phase === 'foundation' ? 'Foundation' : selectedDay.phase === 'building' ? 'Building' : 'Mastery'}</p>
                    <p className="text-slate-500 text-sm leading-relaxed">
                      {selectedDay.phase === 'foundation' ? 'Foundation Phase — Focus on your 3 weakest skills and strengthen them.' :
                       selectedDay.phase === 'building' ? 'Building Phase — Comprehensive training on all skills alternately.' :
                       'Mastery Phase — Final review and mock exams for full preparation.'}
                    </p>
                  </div>

                  {selectedDay.completed && (
                    <div className="mt-4 bg-emerald-50 rounded-xl p-3 text-center">
                      <span className="text-emerald-600 text-sm font-bold">✓ Completed</span>
                    </div>
                  )}
                </>
              )}
            </div>
          ) : (
            <div className="bg-white shadow-card rounded-2xl p-6 text-center text-slate-500">
              <p className="text-sm">Select a day to view details</p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
