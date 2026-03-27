import { useState, useEffect } from 'react';
import {
  CheckCircle, BookOpen, Brain, BarChart3, Zap, Calendar,
  Star, Clock, ChevronDown, ChevronUp, Globe, Layers,
  Shield, MessageCircle, Award
} from 'lucide-react';
import { Button } from '@/components/ui/button';

interface LandingPageProps {
  onStart: () => void;
  onTrial?: () => void;
}

export function LandingPage({ onStart, onTrial }: LandingPageProps) {
  const [scrolled, setScrolled] = useState(false);
  const [openPhase, setOpenPhase] = useState<number | null>(0);
  const [openFaq, setOpenFaq] = useState<number | null>(null);
  const [showPolicy, setShowPolicy] = useState<'privacy' | 'terms' | 'refund' | null>(null);
  const [mobileMenu, setMobileMenu] = useState(false);

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 20);
    window.addEventListener('scroll', onScroll);
    return () => window.removeEventListener('scroll', onScroll);
  }, []);

  const scrollTo = (id: string) => {
    document.getElementById(id)?.scrollIntoView({ behavior: 'smooth' });
  };

  /* ─── Data ─── */

  const learningOutcomes = [
    'Identify strengths and weaknesses in 9 verbal and quantitative skills',
    'Master strategies for solving aptitude questions at the required speed',
    'Practice questions with difficulty that adapts to your actual level',
    'Understand recurring question patterns in the real test',
    'Improve expected score through organized daily training',
    'Take a full simulation test under the same conditions as the real exam',
  ];

  const phases = [
    {
      title: 'Foundation',
      days: 'Day 1–7',
      icon: Layers,
      color: 'bg-blue-50 text-blue-700 border-blue-200',
      bullets: [
        'Comprehensive diagnostic test to determine your level in all skills',
        'Build a customized study plan based on diagnostic results',
        'Practice fundamentals of verbal and quantitative skills (300+ questions)',
      ],
      questions: '300+',
      focus: 'Diagnosis + Basics',
    },
    {
      title: 'Enhancement',
      days: 'Day 8–22',
      icon: Brain,
      color: 'bg-teal-50 text-teal-700 border-teal-200',
      bullets: [
        'Intensive daily training on questions that adapt to your current level',
        'Focus on weaker skills while gradually increasing difficulty',
        'Review weekly analytics and update plan based on your progress (500+ questions)',
      ],
      questions: '500+',
      focus: 'Intensive Adaptive Training',
    },
    {
      title: 'Mastery',
      days: 'Day 23–30',
      icon: Award,
      color: 'bg-amber-50 text-amber-700 border-amber-200',
      bullets: [
        'Comprehensive review of all skills with focus on remaining weak points',
        'High difficulty level questions to achieve the maximum possible score',
        'Full simulation test (200+ questions) under real exam conditions with final report',
      ],
      questions: '200+',
      focus: 'Review + Simulation',
    },
  ];

  const features = [
    {
      icon: Brain,
      title: 'Smart Diagnostic Test',
      desc: 'Determines your level in 9 skills within minutes and builds your study plan automatically',
    },
    {
      icon: Zap,
      title: 'Adaptive Questions',
      desc: 'Elo system raises or lowers question difficulty based on your actual performance',
    },
    {
      icon: BarChart3,
      title: 'Detailed Analytics',
      desc: 'Charts to track your progress in each skill with prediction of your final score',
    },
    {
      icon: MessageCircle,
      title: 'Instant Explanation',
      desc: 'After each answer, get a detailed explanation of the correct solution and optimal strategy',
    },
  ];

  const reviews = [
    {
      name: 'Sarah Al-Mutairi',
      score: 'Scored 95%',
      quote: 'The adaptive questions helped me focus on my weak points. Every day I felt clear improvement in my level.',
      avatar: 'S',
    },
    {
      name: 'Mohammed Al-Ghamdi',
      score: 'Scored 92%',
      quote: 'The daily plan kept me committed for 30 days without interruption. The analytics showed me where to focus.',
      avatar: 'M',
    },
    {
      name: 'Lujain Al-Harbi',
      score: 'Scored 98%',
      quote: 'The simulation test was very close to the real exam. I entered the test with complete confidence.',
      avatar: 'L',
    },
  ];

  const ratingDistribution = [
    { stars: 5, pct: 78 },
    { stars: 4, pct: 15 },
    { stars: 3, pct: 5 },
    { stars: 2, pct: 1 },
    { stars: 1, pct: 1 },
  ];

  const includedItems = [
    'Comprehensive Diagnostic Test',
    '30-Day Customized Study Plan',
    '+1500 Adaptive Questions',
    'Detailed Analytics & Reports',
    'Full Simulation Test',
    'Detailed Explanation for Each Question',
  ];

  const faqs = [
    {
      q: 'How long is the course?',
      a: '30 days of intensive training. Each day includes a set of questions that adapt to your level, with a clear study plan divided into 3 phases: Foundation, Enhancement, and Mastery.',
    },
    {
      q: 'Is the course suitable for my level?',
      a: 'Yes, the course starts with a smart diagnostic test that determines your current level in 9 skills, then builds a customized plan for you. Questions automatically adapt to your performance whether you are a beginner or advanced.',
    },
    {
      q: 'What happens after 30 days?',
      a: 'You can review detailed analytics, the final performance report, and simulation test results. All your data is saved for reference at any time.',
    },
    {
      q: 'Can I get a refund?',
      a: 'Yes, we offer a full refund guarantee within 7 days of registration if you are not satisfied with the course for any reason.',
    },
    {
      q: 'Are the questions similar to the real test?',
      a: 'Yes, more than 1500 questions designed with the same patterns and difficulty as the real General Aptitude Test, covering all required verbal and quantitative skills.',
    },
    {
      q: 'Do I need prior knowledge?',
      a: 'No, the course starts from scratch with a diagnostic test that determines the appropriate starting point for you. Even if you have not studied for the aptitude test before, you will find the course suitable and helpful.',
    },
  ];

  return (
    <div className="min-h-screen overflow-x-hidden bg-slate-50" >

      {/* ═══════════════════════════════════════════════
          1. Fixed Navbar
          ═══════════════════════════════════════════════ */}
      <header
        className={`fixed top-0 inset-x-0 z-50 transition-all duration-300 ${
          scrolled
            ? 'bg-white/95 backdrop-blur-md shadow-sm border-b border-slate-100'
            : 'bg-white/70 backdrop-blur-sm'
        }`}
      >
        <div className="max-w-7xl mx-auto px-4 lg:px-6 h-16 lg:h-18 flex items-center justify-between">
          {/* Logo */}
          <a href="#" className="flex items-center gap-2.5 group">
            <img src="/logo-icon.png" alt="Qudra Academy" className="w-9 h-9" />
            <span className="font-black text-lg text-slate-800">Qudra Academy</span>
          </a>

          {/* Nav Links (desktop) */}
          <nav className="hidden md:flex items-center gap-6 text-sm font-medium text-slate-600">
            <button onClick={() => scrollTo('course')} className="hover:text-teal-600 transition">Course</button>
            <button onClick={() => scrollTo('curriculum')} className="hover:text-teal-600 transition">Curriculum</button>
            <button onClick={() => scrollTo('reviews')} className="hover:text-teal-600 transition">Reviews</button>
          </nav>

          {/* Auth + Mobile Menu */}
          <div className="flex items-center gap-3">
            <button onClick={onStart} className="text-sm font-medium text-slate-600 hover:text-teal-600 transition hidden sm:block">
              Login
            </button>
            <Button onClick={onStart} className="btn-primary h-10 px-5 text-sm">Register Now</Button>
            {/* Hamburger (mobile only) */}
            <button onClick={() => setMobileMenu(!mobileMenu)} className="md:hidden p-2 text-slate-600 hover:text-teal-600">
              <svg className="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                {mobileMenu
                  ? <path strokeLinecap="round" strokeLinejoin="round" d="M6 18L18 6M6 6l12 12" />
                  : <path strokeLinecap="round" strokeLinejoin="round" d="M4 6h16M4 12h16M4 18h16" />}
              </svg>
            </button>
          </div>
        </div>

        {/* Mobile Menu Dropdown */}
        {mobileMenu && (
          <div className="md:hidden border-t border-slate-100 bg-white/95 backdrop-blur-sm px-6 py-4 space-y-3 animate-slide-up">
            <button onClick={() => { scrollTo('course'); setMobileMenu(false); }} className="block w-full text-left text-sm font-medium text-slate-600 hover:text-teal-600 py-2">Course</button>
            <button onClick={() => { scrollTo('curriculum'); setMobileMenu(false); }} className="block w-full text-left text-sm font-medium text-slate-600 hover:text-teal-600 py-2">Curriculum</button>
            <button onClick={() => { scrollTo('reviews'); setMobileMenu(false); }} className="block w-full text-left text-sm font-medium text-slate-600 hover:text-teal-600 py-2">Reviews</button>
            <button onClick={() => { onStart(); setMobileMenu(false); }} className="block w-full text-left text-sm font-medium text-teal-600 hover:text-teal-700 py-2">Login</button>
          </div>
        )}
      </header>

      {/* ═══════════════════════════════════════════════
          2. Hero Section
          ═══════════════════════════════════════════════ */}
      <section className="relative pt-28 lg:pt-32 pb-16 lg:pb-24 overflow-hidden">
        {/* Background Decoration */}
        <div className="absolute inset-0 bg-gradient-to-br from-teal-50/50 via-white to-cyan-50/30" />
        <div className="absolute top-20 right-0 w-[500px] h-[500px] bg-teal-200/15 rounded-full blur-[120px]" />
        <div className="absolute bottom-0 left-0 w-[400px] h-[400px] bg-cyan-200/15 rounded-full blur-[100px]" />

        <div className="relative z-10 max-w-7xl mx-auto px-4 lg:px-6">
          <div className="flex flex-col lg:flex-row gap-10 lg:gap-14">

            {/* Left: Text Content */}
            <div className="flex-1 text-center lg:text-left">
              {/* Rating Badge */}
              <div className="inline-flex items-center gap-2 bg-amber-50 border border-amber-200/60 text-amber-700 text-xs lg:text-sm font-bold px-4 py-2 rounded-full mb-6">
                <Star className="w-4 h-4 fill-amber-400 text-amber-400" />
                <span>4.8 (2,450 ratings) &bull; +10,000 students</span>
              </div>

              <h1 className="text-3xl sm:text-4xl lg:text-5xl font-black text-slate-900 mb-3 leading-tight">
                General Aptitude Test{' '}
                <span className="brand-gradient-text">Preparation Course</span>
              </h1>

              <h2 className="text-xl lg:text-2xl font-bold text-slate-600 mb-3">
                30 Days of Intensive Adaptive Training
              </h2>

              <p className="text-sm text-slate-500 mb-5">
                By <span className="font-bold text-teal-600">Qudra Academy</span>
              </p>

              {/* Meta Tags */}
              <div className="flex flex-wrap gap-3 justify-center lg:justify-start mb-6 text-xs text-slate-500">
                <span className="flex items-center gap-1.5">
                  <Calendar className="w-3.5 h-3.5" /> Last updated: March 2026
                </span>
                <span className="text-slate-300">|</span>
                <span className="flex items-center gap-1.5">
                  <Globe className="w-3.5 h-3.5" /> Arabic
                </span>
                <span className="text-slate-300">|</span>
                <span className="flex items-center gap-1.5">
                  <BookOpen className="w-3.5 h-3.5" /> 9 Skills
                </span>
                <span className="text-slate-300">|</span>
                <span className="flex items-center gap-1.5">
                  <Clock className="w-3.5 h-3.5" /> 30 Days
                </span>
              </div>

              {/* Price */}
              <div className="flex items-center gap-3 justify-center lg:justify-start mb-6">
                <span className="text-3xl lg:text-4xl font-black text-emerald-600">FREE</span>
                <span className="bg-emerald-100 text-emerald-700 text-xs font-bold px-2.5 py-1 rounded-full">
                  LIMITED TIME
                </span>
              </div>

              {/* Buttons */}
              <div className="flex flex-col sm:flex-row gap-3 justify-center lg:justify-start mb-4">
                <Button
                  onClick={onStart}
                  className="h-12 lg:h-14 px-8 lg:px-10 text-base lg:text-lg font-bold bg-gradient-to-l from-emerald-500 to-emerald-600 hover:from-emerald-600 hover:to-emerald-700 text-white rounded-xl shadow-lg hover:shadow-xl transition-all hover:-translate-y-0.5"
                >
                  Register Now — Free
                </Button>
                <Button
                  variant="outline"
                  onClick={onTrial || onStart}
                  className="h-12 lg:h-14 px-6 text-base border-slate-300 text-slate-600 hover:bg-slate-50 rounded-xl"
                >
                  Try Free
                </Button>
              </div>
            </div>

            {/* Right: Course Overview Card */}
            <div className="w-full lg:w-[380px] flex-shrink-0">
              <div className="bg-white rounded-2xl border border-slate-200 shadow-card-lg p-6 lg:sticky lg:top-24">
                <h3 className="text-lg font-black text-slate-800 mb-5 text-center">Course Overview</h3>

                <div className="space-y-4 mb-6">
                  <div className="flex items-center justify-between text-sm">
                    <span className="text-slate-500">Price</span>
                    <span className="font-bold text-emerald-600">FREE</span>
                  </div>
                  <div className="border-b border-slate-100" />
                  <div className="flex items-center justify-between text-sm">
                    <span className="text-slate-500">Duration</span>
                    <span className="font-bold text-slate-800">30 Days</span>
                  </div>
                  <div className="border-b border-slate-100" />
                  <div className="flex items-center justify-between text-sm">
                    <span className="text-slate-500">Level</span>
                    <span className="font-bold text-slate-800">All Levels</span>
                  </div>
                  <div className="border-b border-slate-100" />
                </div>

                <p className="text-sm font-bold text-slate-700 mb-3">Includes:</p>
                <ul className="space-y-2.5 mb-6">
                  {includedItems.map((item, i) => (
                    <li key={i} className="flex items-start gap-2 text-sm text-slate-600">
                      <CheckCircle className="w-4.5 h-4.5 text-teal-500 mt-0.5 flex-shrink-0" />
                      <span>{item}</span>
                    </li>
                  ))}
                </ul>

                <Button
                  onClick={onStart}
                  className="w-full h-12 text-base font-bold bg-gradient-to-l from-amber-500 to-amber-600 hover:from-amber-600 hover:to-amber-700 text-white rounded-xl shadow-lg hover:shadow-xl transition-all"
                >
                  Register Now
                </Button>
              </div>
            </div>

          </div>
        </div>
      </section>

      {/* ═══════════════════════════════════════════════
          3. What You'll Learn
          ═══════════════════════════════════════════════ */}
      <section id="course" className="py-16 lg:py-24 bg-white">
        <div className="max-w-5xl mx-auto px-4 lg:px-6">
          <h2 className="text-2xl lg:text-3xl font-black text-slate-800 text-center mb-10">
            What Will You Learn in This Course?
          </h2>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-4 lg:gap-5">
            {learningOutcomes.map((item, i) => (
              <div
                key={i}
                className="flex items-start gap-3 bg-white border border-slate-200 rounded-2xl p-4 lg:p-5"
              >
                <CheckCircle className="w-5 h-5 text-teal-500 mt-0.5 flex-shrink-0" />
                <span className="text-sm lg:text-base text-slate-700 leading-relaxed">{item}</span>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* ═══════════════════════════════════════════════
          4. Course Curriculum
          ═══════════════════════════════════════════════ */}
      <section id="curriculum" className="py-16 lg:py-24 bg-slate-50">
        <div className="max-w-4xl mx-auto px-4 lg:px-6">
          <h2 className="text-2xl lg:text-3xl font-black text-slate-800 text-center mb-3">
            Course Curriculum — <span className="text-teal-600">3 Phases</span>
          </h2>
          <p className="text-slate-500 text-center mb-10 text-sm">
            A progressive learning path from diagnosis to mastery
          </p>

          <div className="space-y-4">
            {phases.map((phase, i) => {
              const Icon = phase.icon;
              const isOpen = openPhase === i;
              return (
                <div
                  key={i}
                  className={`bg-white border border-slate-200 rounded-2xl overflow-hidden transition-all ${
                    isOpen ? 'shadow-card-lg' : ''
                  }`}
                >
                  <button
                    onClick={() => setOpenPhase(isOpen ? null : i)}
                    className="w-full flex items-center gap-4 p-5 lg:p-6 text-right hover:bg-slate-50/50 transition"
                  >
                    <div
                      className={`w-10 h-10 rounded-xl flex items-center justify-center flex-shrink-0 border ${phase.color}`}
                    >
                      <Icon className="w-5 h-5" />
                    </div>
                    <div className="flex-1 min-w-0">
                      <div className="flex items-center gap-2 mb-0.5">
                        <h3 className="text-base lg:text-lg font-bold text-slate-800">
                          Phase {i + 1}: {phase.title}
                        </h3>
                        <span className="text-xs text-slate-400 font-medium">({phase.days})</span>
                      </div>
                      <div className="flex items-center gap-3 text-xs text-slate-500">
                        <span>{phase.focus}</span>
                        <span className="text-slate-300">|</span>
                        <span>{phase.questions} Questions</span>
                      </div>
                    </div>
                    {isOpen ? (
                      <ChevronUp className="w-5 h-5 text-slate-400 flex-shrink-0" />
                    ) : (
                      <ChevronDown className="w-5 h-5 text-slate-400 flex-shrink-0" />
                    )}
                  </button>

                  {isOpen && (
                    <div className="px-5 lg:px-6 pb-5 lg:pb-6 pt-0">
                      <div className="border-t border-slate-100 pt-4">
                        <ul className="space-y-3">
                          {phase.bullets.map((bullet, j) => (
                            <li key={j} className="flex items-start gap-2.5 text-sm text-slate-600">
                              <CheckCircle className="w-4 h-4 text-teal-500 mt-0.5 flex-shrink-0" />
                              <span className="leading-relaxed">{bullet}</span>
                            </li>
                          ))}
                        </ul>
                      </div>
                    </div>
                  )}
                </div>
              );
            })}
          </div>
        </div>
      </section>

      {/* ═══════════════════════════════════════════════
          5. Course Features
          ═══════════════════════════════════════════════ */}
      <section className="py-16 lg:py-24 bg-white">
        <div className="max-w-5xl mx-auto px-4 lg:px-6">
          <h2 className="text-2xl lg:text-3xl font-black text-slate-800 text-center mb-10">
            What Makes This Course Special?
          </h2>

          <div className="grid grid-cols-1 sm:grid-cols-2 gap-5 lg:gap-6">
            {features.map((f, i) => {
              const Icon = f.icon;
              return (
                <div
                  key={i}
                  className="bg-white border border-slate-200 rounded-2xl p-6 hover:shadow-card-lg hover:-translate-y-1 transition-all duration-300"
                >
                  <div className="w-12 h-12 bg-teal-50 rounded-xl flex items-center justify-center mb-4">
                    <Icon className="w-6 h-6 text-teal-600" />
                  </div>
                  <h3 className="text-base lg:text-lg font-bold text-slate-800 mb-2">{f.title}</h3>
                  <p className="text-sm text-slate-500 leading-relaxed">{f.desc}</p>
                </div>
              );
            })}
          </div>
        </div>
      </section>

      {/* ═══════════════════════════════════════════════
          6. Student Ratings & Reviews
          ═══════════════════════════════════════════════ */}
      <section id="reviews" className="py-16 lg:py-24 bg-slate-50">
        <div className="max-w-5xl mx-auto px-4 lg:px-6">
          <h2 className="text-2xl lg:text-3xl font-black text-slate-800 text-center mb-10">
            Student Reviews
          </h2>

          {/* Rating Overview */}
          <div className="bg-white border border-slate-200 rounded-2xl p-6 lg:p-8 mb-8">
            <div className="flex flex-col md:flex-row items-center gap-8">
              {/* Overall Score */}
              <div className="text-center flex-shrink-0">
                <div className="text-5xl lg:text-6xl font-black text-slate-900 mb-1">4.8</div>
                <div className="flex items-center justify-center gap-1 mb-2">
                  {[1, 2, 3, 4, 5].map((s) => (
                    <Star
                      key={s}
                      className={`w-5 h-5 ${
                        s <= 4 ? 'fill-amber-400 text-amber-400' : 'fill-amber-400/70 text-amber-400/70'
                      }`}
                    />
                  ))}
                </div>
                <p className="text-sm text-slate-500">2,450 ratings</p>
              </div>

              {/* Distribution Bars */}
              <div className="flex-1 w-full space-y-2">
                {ratingDistribution.map((r) => (
                  <div key={r.stars} className="flex items-center gap-3">
                    <div className="flex items-center gap-0.5 w-20 justify-end flex-shrink-0">
                      {Array.from({ length: r.stars }).map((_, j) => (
                        <Star key={j} className="w-3 h-3 fill-amber-400 text-amber-400" />
                      ))}
                    </div>
                    <div className="flex-1 h-2.5 bg-slate-100 rounded-full overflow-hidden">
                      <div
                        className="h-full bg-amber-400 rounded-full transition-all"
                        style={{ width: `${r.pct}%` }}
                      />
                    </div>
                    <span className="text-xs text-slate-500 w-10 text-left flex-shrink-0">{r.pct}%</span>
                  </div>
                ))}
              </div>
            </div>
          </div>

          {/* Review Cards */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-5">
            {reviews.map((r, i) => (
              <div
                key={i}
                className="bg-white border border-slate-200 rounded-2xl p-5 lg:p-6"
              >
                <div className="flex items-center gap-3 mb-3">
                  <div className="w-10 h-10 bg-gradient-to-br from-teal-500 to-teal-700 rounded-full flex items-center justify-center text-white font-bold text-sm">
                    {r.avatar}
                  </div>
                  <div>
                    <p className="font-bold text-slate-800 text-sm">{r.name}</p>
                    <div className="flex items-center gap-0.5">
                      {[1, 2, 3, 4, 5].map((s) => (
                        <Star key={s} className="w-3 h-3 fill-amber-400 text-amber-400" />
                      ))}
                    </div>
                  </div>
                </div>
                <p className="text-sm text-slate-600 leading-relaxed mb-3">"{r.quote}"</p>
                <p className="text-xs font-bold text-teal-600">{r.score}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* ═══════════════════════════════════════════════
          7. Academy Info
          ═══════════════════════════════════════════════ */}
      <section className="py-16 lg:py-20 bg-white">
        <div className="max-w-3xl mx-auto px-4 lg:px-6">
          <div className="bg-gradient-to-br from-teal-50 to-cyan-50 border border-teal-200/50 rounded-2xl p-6 lg:p-8 text-center">
            <img src="/logo-icon.png" alt="Qudra Academy" className="w-14 h-14 mx-auto mb-4" />
            <h3 className="text-lg lg:text-xl font-black text-slate-800 mb-2">By Qudra Academy</h3>
            <p className="text-sm text-slate-500 mb-6 max-w-md mx-auto">
              An educational platform specialized in preparing for the General Aptitude Test
            </p>

            <div className="flex flex-wrap items-center justify-center gap-6 lg:gap-10">
              <div className="text-center">
                <p className="text-xl lg:text-2xl font-black text-slate-800">+10,000</p>
                <p className="text-xs text-slate-500">Students</p>
              </div>
              <div className="w-px h-10 bg-teal-200/60 hidden sm:block" />
              <div className="text-center">
                <p className="text-xl lg:text-2xl font-black text-slate-800">93%</p>
                <p className="text-xs text-slate-500">Improvement Rate</p>
              </div>
              <div className="w-px h-10 bg-teal-200/60 hidden sm:block" />
              <div className="text-center">
                <p className="text-xl lg:text-2xl font-black text-slate-800">+1500</p>
                <p className="text-xs text-slate-500">Questions</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* ═══════════════════════════════════════════════
          8. Pricing Card
          ═══════════════════════════════════════════════ */}
      <section className="py-16 lg:py-24 bg-slate-50">
        <div className="max-w-lg mx-auto px-4 lg:px-6">
          <div className="relative bg-white rounded-2xl border-2 border-transparent shadow-card-lg overflow-hidden">
            {/* Gradient Border Effect */}
            <div className="absolute inset-0 rounded-2xl bg-gradient-to-br from-teal-400 via-amber-400 to-teal-500 -z-10 m-[-2px]" />
            <div className="absolute inset-0 rounded-2xl bg-white m-0" />

            <div className="relative p-6 lg:p-8 text-center">
              <h3 className="text-lg lg:text-xl font-black text-slate-800 mb-1">
                Aptitude Test Course — 30 Days
              </h3>

              {/* Price */}
              <div className="flex items-center justify-center gap-3 my-5">
                <span className="text-4xl lg:text-5xl font-black text-emerald-600">FREE</span>
              </div>

              <span className="inline-block bg-emerald-100 text-emerald-700 text-sm font-bold px-4 py-1.5 rounded-full mb-6">
                LIMITED TIME — Register Now
              </span>

              {/* Included Items */}
              <ul className="space-y-3 mb-6 text-right">
                {includedItems.map((item, i) => (
                  <li key={i} className="flex items-center gap-2.5 text-sm text-slate-600">
                    <CheckCircle className="w-4.5 h-4.5 text-teal-500 flex-shrink-0" />
                    <span>{item}</span>
                  </li>
                ))}
              </ul>

              {/* CTA */}
              <Button
                onClick={onStart}
                className="w-full h-14 text-lg font-bold bg-gradient-to-l from-emerald-500 to-emerald-600 hover:from-emerald-600 hover:to-emerald-700 text-white rounded-xl shadow-lg hover:shadow-xl transition-all hover:-translate-y-0.5 mb-4"
              >
                Register Now — Free Access
              </Button>

              <p className="text-xs text-slate-400 mb-3 flex items-center justify-center gap-1.5">
                <Shield className="w-3.5 h-3.5" />
                Free for All Students — No Credit Card Required
              </p>

              <div className="border-t border-slate-100 pt-4 mt-2">
                <p className="text-xs text-slate-400">
                  Demo account: <span className="font-mono text-slate-500">student@gat.sa</span> /{' '}
                  <span className="font-mono text-slate-500">123456</span>
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* ═══════════════════════════════════════════════
          9. FAQ
          ═══════════════════════════════════════════════ */}
      <section className="py-16 lg:py-24 bg-white">
        <div className="max-w-3xl mx-auto px-4 lg:px-6">
          <h2 className="text-2xl lg:text-3xl font-black text-slate-800 text-center mb-10">
            Frequently Asked Questions
          </h2>

          <div className="space-y-3">
            {faqs.map((faq, i) => {
              const isOpen = openFaq === i;
              return (
                <div
                  key={i}
                  className={`bg-white border border-slate-200 rounded-2xl overflow-hidden transition-all ${
                    isOpen ? 'shadow-card' : ''
                  }`}
                >
                  <button
                    onClick={() => setOpenFaq(isOpen ? null : i)}
                    className="w-full flex items-center justify-between gap-4 p-5 text-right hover:bg-slate-50/50 transition"
                  >
                    <span className="text-sm lg:text-base font-bold text-slate-800">{faq.q}</span>
                    {isOpen ? (
                      <ChevronUp className="w-5 h-5 text-slate-400 flex-shrink-0" />
                    ) : (
                      <ChevronDown className="w-5 h-5 text-slate-400 flex-shrink-0" />
                    )}
                  </button>

                  {isOpen && (
                    <div className="px-5 pb-5 pt-0">
                      <div className="border-t border-slate-100 pt-4">
                        <p className="text-sm text-slate-600 leading-relaxed">{faq.a}</p>
                      </div>
                    </div>
                  )}
                </div>
              );
            })}
          </div>
        </div>
      </section>

      {/* ═══════════════════════════════════════════════
          10. Footer
          ═══════════════════════════════════════════════ */}
      <footer className="py-10 lg:py-14 bg-slate-900 text-white">
        <div className="max-w-5xl mx-auto px-4 lg:px-6">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mb-8">
            {/* Brand */}
            <div className="text-center">
              <div className="flex items-center justify-center gap-2.5 mb-3">
                <img src="/logo-icon.png" alt="Qudra Academy" className="w-9 h-9" />
                <span className="font-black text-lg">Qudra Academy</span>
              </div>
              <p className="text-sm text-slate-400 leading-relaxed">
                An educational platform specialized in preparing for the General Aptitude Test with an intelligent adaptive approach.
              </p>
              <div className="flex flex-wrap gap-2 justify-center mt-4">
                {['Verbal', 'Quantitative', 'CAT', '30 Days'].map((tag) => (
                  <span key={tag} className="bg-slate-800 text-slate-500 text-xs px-2.5 py-1 rounded-full border border-slate-700">{tag}</span>
                ))}
              </div>
            </div>

            {/* Quick Links */}
            <div className="text-center">
              <h4 className="font-bold text-sm mb-3 text-slate-300">Quick Links</h4>
              <div className="space-y-2 text-sm">
                <button onClick={() => document.getElementById('course')?.scrollIntoView({ behavior: 'smooth' })} className="block mx-auto text-slate-400 hover:text-white transition">Course Content</button>
                <button onClick={() => document.getElementById('curriculum')?.scrollIntoView({ behavior: 'smooth' })} className="block mx-auto text-slate-400 hover:text-white transition">Curriculum</button>
                <button onClick={() => document.getElementById('reviews')?.scrollIntoView({ behavior: 'smooth' })} className="block mx-auto text-slate-400 hover:text-white transition">Student Reviews</button>
                <button onClick={onStart} className="block mx-auto text-slate-400 hover:text-white transition">Login</button>
              </div>
            </div>

            {/* Legal Links */}
            <div className="text-center">
              <h4 className="font-bold text-sm mb-3 text-slate-300">Legal Information</h4>
              <div className="space-y-2 text-sm">
                <button onClick={() => setShowPolicy('privacy')} className="block mx-auto text-slate-400 hover:text-white transition">Privacy Policy</button>
                <button onClick={() => setShowPolicy('terms')} className="block mx-auto text-slate-400 hover:text-white transition">Terms & Conditions</button>
                <button onClick={() => setShowPolicy('refund')} className="block mx-auto text-slate-400 hover:text-white transition">Refund Policy</button>
                <button onClick={() => window.location.href = 'mailto:info@qudra.academy'} className="block mx-auto text-slate-400 hover:text-white transition">Contact Us</button>
              </div>
            </div>
          </div>

          <div className="border-t border-slate-800 pt-6 text-center">
            <p className="text-xs text-slate-500">
              &copy; 2026 Qudra Academy. All rights reserved.
            </p>
          </div>
        </div>
      </footer>

      {/* ═══ Policy Modal ═══ */}
      {showPolicy && (
        <div className="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-50 flex items-center justify-center p-4 overflow-y-auto">
          <div className="bg-white rounded-2xl max-w-2xl w-full max-h-[80vh] overflow-y-auto p-6 lg:p-8 my-8">
            <div className="flex items-center justify-between mb-6">
              <h2 className="text-xl font-black text-slate-800">
                {showPolicy === 'privacy' ? 'Privacy Policy' : showPolicy === 'terms' ? 'Terms & Conditions' : 'Refund Policy'}
              </h2>
              <button onClick={() => setShowPolicy(null)} className="text-slate-400 hover:text-slate-600 text-2xl">&times;</button>
            </div>
            <div className="prose prose-sm text-slate-600 leading-relaxed space-y-4">
              {showPolicy === 'privacy' && (<>
                <p className="font-bold text-slate-800">Last Updated: March 2026</p>
                <p>At Qudra Academy, we are committed to protecting our users' privacy. This policy explains how we collect, use, and protect your data.</p>
                <h3 className="font-bold text-slate-800">Data We Collect</h3>
                <p>• Name and email upon registration<br/>• Your answers to questions and test results<br/>• Course progress data (current day, points, streaks)</p>
                <h3 className="font-bold text-slate-800">How We Use Your Data</h3>
                <p>• Personalize study plans and adapt questions to your level<br/>• Improve platform experience and develop content<br/>• Send course-related notifications (optional)</p>
                <h3 className="font-bold text-slate-800">Data Protection</h3>
                <p>We use SSL encryption to protect data during transmission, and we do not share your data with third parties for marketing purposes.</p>
              </>)}
              {showPolicy === 'terms' && (<>
                <p className="font-bold text-slate-800">Last Updated: March 2026</p>
                <p>By using the Qudra Academy platform, you agree to the following terms and conditions.</p>
                <h3 className="font-bold text-slate-800">Account & Registration</h3>
                <p>• Information provided during registration must be accurate<br/>• You are responsible for maintaining your account credentials<br/>• Account sharing with others is not allowed</p>
                <h3 className="font-bold text-slate-800">Content Usage</h3>
                <p>• Educational content is for personal use only<br/>• Copying or redistributing questions or educational materials is prohibited<br/>• All intellectual property rights are reserved to Qudra Academy</p>
                <h3 className="font-bold text-slate-800">Limitation of Liability</h3>
                <p>The course is a preparation tool and does not guarantee a specific score on the General Aptitude Test. Results depend on the student's level of commitment.</p>
              </>)}
              {showPolicy === 'refund' && (<>
                <p className="font-bold text-slate-800">Last Updated: March 2026</p>
                <p>We strive for your complete satisfaction with our course. If you are not satisfied, you can request a refund according to the following terms.</p>
                <h3 className="font-bold text-slate-800">Refund Period</h3>
                <p>• You are entitled to a full refund within <strong>7 days</strong> of registration<br/>• Refund is accepted if you have not exceeded Day 5 of the study plan</p>
                <h3 className="font-bold text-slate-800">How to Request a Refund</h3>
                <p>• Send refund request to: info@qudra.academy<br/>• Include your registered email and reason for refund<br/>• Request will be processed within 3-5 business days</p>
                <h3 className="font-bold text-slate-800">Cases Where Refund Is Not Accepted</h3>
                <p>• After 7 days from registration<br/>• If you have exceeded Day 5 of the study plan<br/>• If you have completed the final simulation test</p>
              </>)}
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
