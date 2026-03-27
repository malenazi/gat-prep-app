import { useState, useEffect, useRef } from 'react';
import {
  CheckCircle, BookOpen, Brain, BarChart3, Zap,
  Star, Clock, ChevronDown, ChevronUp, Layers,
  Shield, MessageCircle, Award, Users, Target, Trophy,
  PlayCircle, ArrowRight, Sparkles, CheckSquare
} from 'lucide-react';
import { Button } from '@/components/ui/button';

interface LandingPageProps {
  onStart: () => void;
  onTrial?: () => void;
}

// Animated counter hook
function useCountUp(end: number, duration: number = 2000) {
  const [count, setCount] = useState(0);
  const countRef = useRef(0);
  const [isVisible, setIsVisible] = useState(false);
  const ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting && !isVisible) {
          setIsVisible(true);
        }
      },
      { threshold: 0.5 }
    );

    if (ref.current) {
      observer.observe(ref.current);
    }

    return () => observer.disconnect();
  }, [isVisible]);

  useEffect(() => {
    if (!isVisible) return;

    const startTime = Date.now();
    const timer = setInterval(() => {
      const elapsed = Date.now() - startTime;
      const progress = Math.min(elapsed / duration, 1);
      const easeOutQuart = 1 - Math.pow(1 - progress, 4);
      countRef.current = Math.floor(easeOutQuart * end);
      setCount(countRef.current);

      if (progress === 1) {
        clearInterval(timer);
      }
    }, 16);

    return () => clearInterval(timer);
  }, [isVisible, end, duration]);

  return { count, ref };
}

export function LandingPage({ onStart, onTrial }: LandingPageProps) {
  const [scrolled, setScrolled] = useState(false);
  const [openPhase, setOpenPhase] = useState<number | null>(0);
  const [openFaq, setOpenFaq] = useState<number | null>(null);
  const [mobileMenu, setMobileMenu] = useState(false);
  const [activeTestimonial, setActiveTestimonial] = useState(0);

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 20);
    window.addEventListener('scroll', onScroll);
    return () => window.removeEventListener('scroll', onScroll);
  }, []);

  // Auto-rotate testimonials
  useEffect(() => {
    const timer = setInterval(() => {
      setActiveTestimonial((prev) => (prev + 1) % testimonials.length);
    }, 5000);
    return () => clearInterval(timer);
  }, []);

  const scrollTo = (id: string) => {
    document.getElementById(id)?.scrollIntoView({ behavior: 'smooth' });
  };

  // Statistics with animated counters
  const StatsSection = () => {
    const students = useCountUp(10000);
    const questions = useCountUp(1318);
    const successRate = useCountUp(95);
    const rating = useCountUp(48, 1000); // 4.8 * 10 for animation

    return (
      <div className="grid grid-cols-2 md:grid-cols-4 gap-6 max-w-4xl mx-auto">
        <div ref={students.ref} className="text-center p-6 bg-white rounded-2xl shadow-lg border border-slate-100">
          <div className="text-3xl md:text-4xl font-black text-teal-600 mb-1">
            {students.count.toLocaleString()}+
          </div>
          <div className="text-sm text-slate-600 font-medium">Students Enrolled</div>
        </div>
        <div ref={questions.ref} className="text-center p-6 bg-white rounded-2xl shadow-lg border border-slate-100">
          <div className="text-3xl md:text-4xl font-black text-teal-600 mb-1">
            {questions.count.toLocaleString()}
          </div>
          <div className="text-sm text-slate-600 font-medium">Practice Questions</div>
        </div>
        <div ref={successRate.ref} className="text-center p-6 bg-white rounded-2xl shadow-lg border border-slate-100">
          <div className="text-3xl md:text-4xl font-black text-teal-600 mb-1">
            {successRate.count}%
          </div>
          <div className="text-sm text-slate-600 font-medium">Success Rate</div>
        </div>
        <div ref={rating.ref} className="text-center p-6 bg-white rounded-2xl shadow-lg border border-slate-100">
          <div className="text-3xl md:text-4xl font-black text-teal-600 mb-1">
            {(rating.count / 10).toFixed(1)}
          </div>
          <div className="text-sm text-slate-600 font-medium">User Rating</div>
        </div>
      </div>
    );
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
      title: 'Smart Diagnostic',
      desc: 'AI-powered assessment identifies your strengths and weaknesses across all 9 skills in minutes.',
    },
    {
      icon: Zap,
      title: 'Adaptive Learning',
      desc: 'Elo-based system automatically adjusts question difficulty to match your evolving skill level.',
    },
    {
      icon: BarChart3,
      title: 'Progress Analytics',
      desc: 'Detailed charts track your improvement and predict your final exam score with accuracy.',
    },
    {
      icon: Target,
      title: 'Personalized Plan',
      desc: 'Custom 30-day study schedule tailored to your diagnostic results and daily availability.',
    },
  ];

  const includedItems = [
    'Comprehensive Diagnostic Test',
    '30-Day Customized Study Plan',
    '1,318+ Adaptive Questions',
    'Detailed Analytics & Reports',
    'Full Simulation Test',
    'Detailed Explanation for Each Question',
  ];

  const testimonials = [
    {
      name: 'Sarah Al-Mutairi',
      role: 'University Student',
      score: 'Scored 95%',
      text: 'The adaptive questions helped me focus on my weak points. Every day I felt clear improvement in my level. The analytics showed exactly where I needed to improve.',
      avatar: 'S',
    },
    {
      name: 'Mohammed Al-Ghamdi',
      role: 'Engineering Major',
      score: 'Scored 92%',
      text: 'The daily plan kept me committed for 30 days without interruption. The analytics showed me where to focus. Best investment in my academic career!',
      avatar: 'M',
    },
    {
      name: 'Lujain Al-Harbi',
      role: 'Medical Student',
      score: 'Scored 98%',
      text: 'The simulation test was very close to the real exam. I entered the test with complete confidence. Highly recommend to anyone preparing for GAT!',
      avatar: 'L',
    },
  ];

  const faqs = [
    {
      q: 'How long is the course?',
      a: 'The course is designed for 30 days of intensive study, but you can adjust the pace based on your schedule. Each day requires 60-90 minutes of focused practice.',
    },
    {
      q: 'Is the course suitable for my level?',
      a: 'Yes! Our smart diagnostic test identifies your current level and creates a personalized plan. Whether you\'re a beginner or advanced, the adaptive system ensures optimal challenge.',
    },
    {
      q: 'What happens after 30 days?',
      a: 'You\'ll have full access to all practice questions and can continue using the platform. Many students use it for ongoing practice until their exam date.',
    },
    {
      q: 'Can I get a refund?',
      a: 'Since this is a free course during the launch period, no payment is required. Enjoy full access to all features at no cost!',
    },
    {
      q: 'Are the questions similar to the real test?',
      a: 'Yes, our question bank is developed by GAT experts and closely mirrors the actual exam format, difficulty, and question types.',
    },
    {
      q: 'Do I need prior knowledge?',
      a: 'No prior knowledge is required. Our Foundation phase covers all basics, and the adaptive system ensures you start at the right level for you.',
    },
  ];

  const trustBadges = [
    { icon: Shield, text: 'Bank-Level Security' },
    { icon: CheckSquare, text: 'Expert-Crafted Questions' },
    { icon: Users, text: '10,000+ Students' },
    { icon: Trophy, text: '95% Success Rate' },
  ];

  return (
    <div className="min-h-screen bg-white font-sans text-slate-800">
      {/* ═══════════════════════════════════════════════
          1. Floating Header
          ═══════════════════════════════════════════════ */}
      <header
        className={`fixed top-0 left-0 right-0 z-50 transition-all duration-300 ${
          scrolled ? 'bg-white/95 backdrop-blur-md shadow-sm border-b border-slate-100' : 'bg-transparent'
        }`}
      >
        <div className="max-w-7xl mx-auto px-4 lg:px-6">
          <div className="flex items-center justify-between h-16 lg:h-18">
            {/* Logo */}
            <div className="flex items-center gap-2">
              <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-teal-500 to-cyan-600 flex items-center justify-center text-white font-black text-lg shadow-lg">
                Q
              </div>
              <span className="font-black text-lg text-slate-800 hidden sm:block">Qudra Academy</span>
            </div>

            {/* Nav Links (desktop) */}
            <nav className="hidden md:flex items-center gap-6 text-sm font-medium text-slate-600">
              <button onClick={() => scrollTo('course')} className="hover:text-teal-600 transition">Course</button>
              <button onClick={() => scrollTo('curriculum')} className="hover:text-teal-600 transition">Curriculum</button>
              <button onClick={() => scrollTo('features')} className="hover:text-teal-600 transition">Features</button>
              <button onClick={() => scrollTo('reviews')} className="hover:text-teal-600 transition">Reviews</button>
            </nav>

            {/* CTA */}
            <div className="flex items-center gap-3">
              <button onClick={onStart} className="text-sm font-medium text-slate-600 hover:text-teal-600 transition hidden sm:block">
                Login
              </button>
              <Button onClick={onStart} className="btn-primary h-10 px-5 text-sm">Get Started Free</Button>
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
              <button onClick={() => { scrollTo('features'); setMobileMenu(false); }} className="block w-full text-left text-sm font-medium text-slate-600 hover:text-teal-600 py-2">Features</button>
              <button onClick={() => { scrollTo('reviews'); setMobileMenu(false); }} className="block w-full text-left text-sm font-medium text-slate-600 hover:text-teal-600 py-2">Reviews</button>
              <button onClick={() => { onStart(); setMobileMenu(false); }} className="block w-full text-left text-sm font-medium text-teal-600 hover:text-teal-700 py-2">Get Started</button>
            </div>
          )}
        </div>
      </header>

      {/* ═══════════════════════════════════════════════
          2. Enhanced Hero Section
          ═══════════════════════════════════════════════ */}
      <section className="relative pt-28 lg:pt-36 pb-20 lg:pb-28 overflow-hidden">
        {/* Animated Background */}
        <div className="absolute inset-0 bg-gradient-to-br from-teal-50/80 via-white to-cyan-50/60" />
        <div className="absolute top-20 right-0 w-[600px] h-[600px] bg-teal-200/20 rounded-full blur-[150px] animate-pulse" />
        <div className="absolute bottom-0 left-0 w-[500px] h-[500px] bg-cyan-200/20 rounded-full blur-[120px] animate-pulse" style={{ animationDelay: '1s' }} />
        
        {/* Grid Pattern Overlay */}
        <div className="absolute inset-0 bg-[url('data:image/svg+xml,%3Csvg%20width%3D%2260%22%20height%3D%2260%22%20viewBox%3D%220%200%2060%2060%22%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%3E%3Cg%20fill%3D%22none%22%20fill-rule%3D%22evenodd%22%3E%3Cg%20fill%3D%22%239C92AC%22%20fill-opacity%3D%220.03%22%3E%3Cpath%20d%3D%22M36%2034v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6%2034v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6%204V0H4v4H0v2h4v4h2V6h4V4H6z%22/%3E%3C/g%3E%3C/g%3E%3C/svg%3E')] opacity-50" />

        <div className="relative z-10 max-w-7xl mx-auto px-4 lg:px-6">
          <div className="flex flex-col lg:flex-row gap-12 lg:gap-16 items-center">

            {/* Left: Text Content */}
            <div className="flex-1 text-center lg:text-left">
              {/* Trust Badge */}
              <div className="inline-flex items-center gap-2 bg-gradient-to-r from-amber-50 to-orange-50 border border-amber-200/60 text-amber-700 text-xs lg:text-sm font-bold px-4 py-2 rounded-full mb-6 shadow-sm">
                <Sparkles className="w-4 h-4 text-amber-500" />
                <span>Limited Time: 100% FREE Access</span>
              </div>

              <h1 className="text-4xl sm:text-5xl lg:text-6xl font-black text-slate-900 mb-4 leading-tight">
                Master the{' '}
                <span className="bg-gradient-to-r from-teal-600 to-cyan-600 bg-clip-text text-transparent">GAT Exam</span>
                <br />in 30 Days
              </h1>

              <h2 className="text-xl lg:text-2xl font-medium text-slate-600 mb-6 max-w-2xl">
                AI-powered adaptive learning with 1,318+ practice questions. 
                Personalized study plan that evolves with you.
              </h2>

              {/* Trust Indicators */}
              <div className="flex flex-wrap gap-4 justify-center lg:justify-start mb-8">
                <div className="flex items-center gap-1.5 text-sm text-slate-600">
                  <div className="flex -space-x-1">
                    {[...Array(5)].map((_, i) => (
                      <Star key={i} className="w-4 h-4 fill-amber-400 text-amber-400" />
                    ))}
                  </div>
                  <span className="font-semibold">4.8</span>
                  <span className="text-slate-400">(2,450+ reviews)</span>
                </div>
                <span className="text-slate-300 hidden sm:inline">|</span>
                <div className="flex items-center gap-1.5 text-sm text-slate-600">
                  <Users className="w-4 h-4 text-teal-500" />
                  <span className="font-semibold">10,000+</span>
                  <span className="text-slate-400">students</span>
                </div>
              </div>

              {/* CTA Buttons */}
              <div className="flex flex-col sm:flex-row gap-4 justify-center lg:justify-start mb-8">
                <Button
                  onClick={onStart}
                  className="h-14 lg:h-16 px-8 lg:px-12 text-base lg:text-lg font-bold bg-gradient-to-r from-teal-500 to-cyan-600 hover:from-teal-600 hover:to-cyan-700 text-white rounded-2xl shadow-xl shadow-teal-500/25 hover:shadow-2xl hover:shadow-teal-500/30 transition-all hover:-translate-y-1 flex items-center gap-2"
                >
                  Start Free Today
                  <ArrowRight className="w-5 h-5" />
                </Button>
                <Button
                  variant="outline"
                  onClick={onTrial || onStart}
                  className="h-14 lg:h-16 px-8 text-base border-2 border-slate-200 text-slate-700 hover:bg-slate-50 hover:border-slate-300 rounded-2xl flex items-center gap-2"
                >
                  <PlayCircle className="w-5 h-5" />
                  Watch Demo
                </Button>
              </div>

              {/* Trust Badges */}
              <div className="flex flex-wrap gap-3 justify-center lg:justify-start">
                {trustBadges.map((badge, i) => (
                  <div key={i} className="flex items-center gap-1.5 text-xs text-slate-500 bg-slate-50 px-3 py-1.5 rounded-full">
                    <badge.icon className="w-3.5 h-3.5 text-teal-500" />
                    <span>{badge.text}</span>
                  </div>
                ))}
              </div>
            </div>

            {/* Right: Enhanced Course Card */}
            <div className="w-full lg:w-[420px] flex-shrink-0">
              <div className="bg-white rounded-3xl border border-slate-200 shadow-2xl shadow-slate-200/50 p-8 relative overflow-hidden">
                {/* Decorative Elements */}
                <div className="absolute top-0 right-0 w-32 h-32 bg-gradient-to-br from-teal-100 to-cyan-100 rounded-bl-full opacity-50" />
                
                {/* Price Tag */}
                <div className="absolute -top-1 -right-1">
                  <div className="bg-gradient-to-r from-emerald-500 to-teal-500 text-white text-xs font-bold px-4 py-2 rounded-bl-2xl rounded-tr-2xl shadow-lg">
                    100% FREE
                  </div>
                </div>

                <h3 className="text-xl font-black text-slate-800 mb-2">Complete GAT Course</h3>
                <p className="text-sm text-slate-500 mb-6">Everything you need to ace the exam</p>

                <div className="space-y-4 mb-6">
                  <div className="flex items-center justify-between text-sm py-2 border-b border-slate-100">
                    <span className="text-slate-500 flex items-center gap-2">
                      <Clock className="w-4 h-4" /> Duration
                    </span>
                    <span className="font-bold text-slate-800">30 Days</span>
                  </div>
                  <div className="flex items-center justify-between text-sm py-2 border-b border-slate-100">
                    <span className="text-slate-500 flex items-center gap-2">
                      <BookOpen className="w-4 h-4" /> Questions
                    </span>
                    <span className="font-bold text-slate-800">1,318+</span>
                  </div>
                  <div className="flex items-center justify-between text-sm py-2 border-b border-slate-100">
                    <span className="text-slate-500 flex items-center gap-2">
                      <Award className="w-4 h-4" /> Skills
                    </span>
                    <span className="font-bold text-slate-800">9 Total</span>
                  </div>
                </div>

                <ul className="space-y-3 mb-8">
                  {includedItems.slice(0, 4).map((item, i) => (
                    <li key={i} className="flex items-center gap-3 text-sm text-slate-600">
                      <div className="w-5 h-5 rounded-full bg-teal-100 flex items-center justify-center flex-shrink-0">
                        <CheckCircle className="w-3 h-3 text-teal-600" />
                      </div>
                      <span>{item}</span>
                    </li>
                  ))}
                </ul>

                <Button
                  onClick={onStart}
                  className="w-full h-14 text-base font-bold bg-gradient-to-r from-amber-500 to-orange-500 hover:from-amber-600 hover:to-orange-600 text-white rounded-xl shadow-lg shadow-amber-500/25 hover:shadow-xl transition-all"
                >
                  Get Instant Access
                </Button>
                
                <p className="text-xs text-slate-400 text-center mt-4">
                  No credit card required • Cancel anytime
                </p>
              </div>
            </div>

          </div>
        </div>
      </section>

      {/* ═══════════════════════════════════════════════
          3. Stats Section
          ═══════════════════════════════════════════════ */}
      <section className="py-16 bg-gradient-to-b from-white to-slate-50">
        <div className="max-w-6xl mx-auto px-4 lg:px-6">
          <StatsSection />
        </div>
      </section>

      {/* ═══════════════════════════════════════════════
          4. What You'll Learn
          ═══════════════════════════════════════════════ */}
      <section id="course" className="py-20 lg:py-28 bg-white">
        <div className="max-w-5xl mx-auto px-4 lg:px-6">
          <div className="text-center mb-14">
            <span className="inline-block text-sm font-bold text-teal-600 bg-teal-50 px-4 py-1.5 rounded-full mb-4">
              LEARNING OUTCOMES
            </span>
            <h2 className="text-3xl lg:text-4xl font-black text-slate-900 mb-4">
              What Will You Learn?
            </h2>
            <p className="text-lg text-slate-600 max-w-2xl mx-auto">
              Master all the skills needed to excel in the General Aptitude Test
            </p>
          </div>

          <div className="grid md:grid-cols-2 gap-5">
            {learningOutcomes.map((item, i) => (
              <div 
                key={i} 
                className="flex items-start gap-4 p-5 bg-slate-50 rounded-xl hover:bg-teal-50 transition-colors group"
              >
                <div className="w-8 h-8 rounded-lg bg-teal-100 text-teal-600 flex items-center justify-center flex-shrink-0 group-hover:bg-teal-500 group-hover:text-white transition-all">
                  <CheckCircle className="w-5 h-5" />
                </div>
                <span className="text-slate-700 font-medium">{item}</span>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* ═══════════════════════════════════════════════
          5. Enhanced Features Grid
          ═══════════════════════════════════════════════ */}
      <section id="features" className="py-20 lg:py-28 bg-slate-50">
        <div className="max-w-6xl mx-auto px-4 lg:px-6">
          <div className="text-center mb-14">
            <span className="inline-block text-sm font-bold text-teal-600 bg-white px-4 py-1.5 rounded-full mb-4 shadow-sm">
              WHY CHOOSE US
            </span>
            <h2 className="text-3xl lg:text-4xl font-black text-slate-900 mb-4">
              Powerful Features for Better Learning
            </h2>
            <p className="text-lg text-slate-600 max-w-2xl mx-auto">
              Our AI-powered platform adapts to your unique learning style
            </p>
          </div>

          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
            {features.map((f, i) => (
              <div 
                key={i} 
                className="group bg-white rounded-2xl p-6 border border-slate-100 shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300"
              >
                <div className="w-14 h-14 rounded-2xl bg-gradient-to-br from-teal-100 to-cyan-100 text-teal-600 flex items-center justify-center mb-5 group-hover:from-teal-500 group-hover:to-cyan-500 group-hover:text-white transition-all">
                  <f.icon className="w-7 h-7" />
                </div>
                <h3 className="text-lg font-bold text-slate-800 mb-2">{f.title}</h3>
                <p className="text-sm text-slate-600 leading-relaxed">{f.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* ═══════════════════════════════════════════════
          6. 3-Phase Curriculum
          ═══════════════════════════════════════════════ */}
      <section id="curriculum" className="py-20 lg:py-28 bg-white">
        <div className="max-w-5xl mx-auto px-4 lg:px-6">
          <div className="text-center mb-14">
            <span className="inline-block text-sm font-bold text-teal-600 bg-teal-50 px-4 py-1.5 rounded-full mb-4">
              30-DAY CURRICULUM
            </span>
            <h2 className="text-3xl lg:text-4xl font-black text-slate-900 mb-4">
              Your Path to GAT Success
            </h2>
            <p className="text-lg text-slate-600 max-w-2xl mx-auto">
              A progressive learning journey from diagnosis to mastery
            </p>
          </div>

          <div className="space-y-4">
            {phases.map((phase, i) => (
              <div
                key={i}
                className={`rounded-2xl border-2 transition-all ${
                  openPhase === i ? 'border-teal-200 shadow-lg' : 'border-slate-100 hover:border-slate-200'
                }`}
              >
                <button
                  onClick={() => setOpenPhase(openPhase === i ? null : i)}
                  className="w-full p-6 flex items-center justify-between text-left"
                >
                  <div className="flex items-center gap-4">
                    <div className={`w-14 h-14 rounded-xl flex items-center justify-center ${phase.color}`}>
                      <phase.icon className="w-7 h-7" />
                    </div>
                    <div>
                      <h3 className="text-xl font-bold text-slate-800">Phase {i + 1}: {phase.title}</h3>
                      <p className="text-sm text-slate-500">{phase.days} • {phase.focus}</p>
                    </div>
                  </div>
                  <div className="flex items-center gap-4">
                    <span className="text-sm font-bold text-teal-600 bg-teal-50 px-3 py-1 rounded-full hidden sm:block">
                      {phase.questions} Questions
                    </span>
                    {openPhase === i ? <ChevronUp className="w-5 h-5 text-slate-400" /> : <ChevronDown className="w-5 h-5 text-slate-400" />}
                  </div>
                </button>
                
                {openPhase === i && (
                  <div className="px-6 pb-6 pt-2 border-t border-slate-100">
                    <ul className="space-y-3 mt-4">
                      {phase.bullets.map((bullet, j) => (
                        <li key={j} className="flex items-start gap-3 text-slate-600">
                          <CheckCircle className="w-5 h-5 text-teal-500 mt-0.5 flex-shrink-0" />
                          <span>{bullet}</span>
                        </li>
                      ))}
                    </ul>
                  </div>
                )}
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* ═══════════════════════════════════════════════
          7. Testimonials Carousel
          ═══════════════════════════════════════════════ */}
      <section id="reviews" className="py-20 lg:py-28 bg-gradient-to-b from-slate-50 to-white">
        <div className="max-w-5xl mx-auto px-4 lg:px-6">
          <div className="text-center mb-14">
            <span className="inline-block text-sm font-bold text-teal-600 bg-white px-4 py-1.5 rounded-full mb-4 shadow-sm">
              STUDENT SUCCESS STORIES
            </span>
            <h2 className="text-3xl lg:text-4xl font-black text-slate-900 mb-4">
              Join 10,000+ Successful Students
            </h2>
          </div>

          <div className="relative">
            <div className="bg-white rounded-3xl p-8 lg:p-12 shadow-xl shadow-slate-200/50 border border-slate-100">
              <div className="flex flex-col lg:flex-row gap-8 items-center">
                {/* Avatar */}
                <div className="w-20 h-20 rounded-full bg-gradient-to-br from-teal-400 to-cyan-500 flex items-center justify-center text-white text-3xl font-bold shadow-lg">
                  {testimonials[activeTestimonial].avatar}
                </div>
                
                {/* Content */}
                <div className="flex-1 text-center lg:text-left">
                  <div className="flex items-center gap-1 justify-center lg:justify-start mb-4">
                    {[...Array(5)].map((_, i) => (
                      <Star key={i} className="w-5 h-5 fill-amber-400 text-amber-400" />
                    ))}
                  </div>
                  <p className="text-lg lg:text-xl text-slate-700 mb-6 leading-relaxed">
                    "{testimonials[activeTestimonial].text}"
                  </p>
                  <div>
                    <div className="font-bold text-slate-800">{testimonials[activeTestimonial].name}</div>
                    <div className="text-sm text-slate-500">{testimonials[activeTestimonial].role}</div>
                    <div className="inline-block mt-2 text-sm font-bold text-teal-600 bg-teal-50 px-3 py-1 rounded-full">
                      {testimonials[activeTestimonial].score}
                    </div>
                  </div>
                </div>
              </div>
            </div>

            {/* Navigation Dots */}
            <div className="flex justify-center gap-2 mt-6">
              {testimonials.map((_, i) => (
                <button
                  key={i}
                  onClick={() => setActiveTestimonial(i)}
                  className={`w-3 h-3 rounded-full transition-all ${
                    activeTestimonial === i ? 'bg-teal-500 w-8' : 'bg-slate-300 hover:bg-slate-400'
                  }`}
                />
              ))}
            </div>
          </div>
        </div>
      </section>

      {/* ═══════════════════════════════════════════════
          8. CTA Section
          ═══════════════════════════════════════════════ */}
      <section className="py-20 lg:py-28 bg-gradient-to-br from-teal-600 to-cyan-700 relative overflow-hidden">
        {/* Decorative Elements */}
        <div className="absolute top-0 right-0 w-96 h-96 bg-white/5 rounded-full blur-3xl" />
        <div className="absolute bottom-0 left-0 w-96 h-96 bg-white/5 rounded-full blur-3xl" />
        
        <div className="relative z-10 max-w-4xl mx-auto px-4 lg:px-6 text-center">
          <h2 className="text-3xl lg:text-5xl font-black text-white mb-6">
            Ready to Ace Your GAT Exam?
          </h2>
          <p className="text-xl text-teal-100 mb-8 max-w-2xl mx-auto">
            Join thousands of students who achieved their dream scores. 
            Start your free 30-day journey today.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Button
              onClick={onStart}
              className="h-16 px-10 text-lg font-bold bg-white text-teal-600 hover:bg-teal-50 rounded-2xl shadow-xl transition-all hover:-translate-y-1"
            >
              Start Free Today
              <ArrowRight className="w-5 h-5 ml-2" />
            </Button>
          </div>
          <p className="text-teal-200 mt-6 text-sm">
            No credit card required • Instant access • Cancel anytime
          </p>
        </div>
      </section>

      {/* ═══════════════════════════════════════════════
          9. FAQ
          ═══════════════════════════════════════════════ */}
      <section className="py-20 lg:py-28 bg-white">
        <div className="max-w-3xl mx-auto px-4 lg:px-6">
          <div className="text-center mb-14">
            <span className="inline-block text-sm font-bold text-teal-600 bg-teal-50 px-4 py-1.5 rounded-full mb-4">
              FAQ
            </span>
            <h2 className="text-3xl lg:text-4xl font-black text-slate-900 mb-4">
              Frequently Asked Questions
            </h2>
          </div>

          <div className="space-y-3">
            {faqs.map((faq, i) => (
              <div
                key={i}
                className={`rounded-xl border transition-all ${
                  openFaq === i ? 'border-teal-200 bg-teal-50/30' : 'border-slate-200 hover:border-slate-300'
                }`}
              >
                <button
                  onClick={() => setOpenFaq(openFaq === i ? null : i)}
                  className="w-full p-5 flex items-center justify-between text-left"
                >
                  <span className="font-bold text-slate-800 pr-4">{faq.q}</span>
                  {openFaq === i ? <ChevronUp className="w-5 h-5 text-teal-500 flex-shrink-0" /> : <ChevronDown className="w-5 h-5 text-slate-400 flex-shrink-0" />}
                </button>
                {openFaq === i && (
                  <div className="px-5 pb-5">
                    <p className="text-slate-600 leading-relaxed">{faq.a}</p>
                  </div>
                )}
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* ═══════════════════════════════════════════════
          10. Compliance Section
          ═══════════════════════════════════════════════ */}
      <section className="bg-slate-50 py-16 lg:py-20">
        <div className="max-w-6xl mx-auto px-4 lg:px-6">
          <div className="text-center mb-12">
            <h2 className="text-2xl lg:text-3xl font-bold text-slate-900 mb-3">Compliant With National Standards</h2>
            <p className="text-slate-600 max-w-2xl mx-auto">
              This platform meets the highest standards set by Saudi Arabia's leading education authorities
            </p>
          </div>

          <div className="grid md:grid-cols-2 gap-6 lg:gap-8">
            {/* ETEC Card */}
            <div className="bg-white rounded-2xl p-8 lg:p-10 shadow-lg shadow-slate-200/50 border border-slate-100 hover:shadow-xl hover:shadow-slate-200/60 transition-all duration-300 hover:-translate-y-1">
              <div className="flex flex-col items-center text-center">
                <div className="mb-6 p-6 bg-slate-50 rounded-2xl w-full max-w-xs">
                  <img 
                    src="/logos/etec.png" 
                    alt="ETEC - Education and Training Evaluation Commission" 
                    className="w-full h-auto object-contain" 
                  />
                </div>
                <h3 className="text-xl font-bold text-slate-900 mb-2">ETEC</h3>
                <p className="text-sm font-medium text-teal-600 mb-4">Education and Training Evaluation Commission</p>
                <p className="text-slate-600 text-sm leading-relaxed">
                  Our exam preparation content aligns with ETEC standards for academic assessment 
                  and evaluation, ensuring you practice with questions that meet official quality benchmarks.
                </p>
              </div>
            </div>

            {/* NELC Card */}
            <div className="bg-white rounded-2xl p-8 lg:p-10 shadow-lg shadow-slate-200/50 border border-slate-100 hover:shadow-xl hover:shadow-slate-200/60 transition-all duration-300 hover:-translate-y-1">
              <div className="flex flex-col items-center text-center">
                <div className="mb-6 p-6 bg-slate-50 rounded-2xl w-full max-w-xs">
                  <img 
                    src="/logos/nelc.png" 
                    alt="NELC - National eLearning Center" 
                    className="w-full h-auto object-contain" 
                  />
                </div>
                <h3 className="text-xl font-bold text-slate-900 mb-2">NELC</h3>
                <p className="text-sm font-medium text-teal-600 mb-4">National eLearning Center</p>
                <p className="text-slate-600 text-sm leading-relaxed">
                  Our digital learning platform adheres to NELC national e-learning standards, 
                  providing a compliant and quality-assured online education experience.
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* ═══════════════════════════════════════════════
          11. Footer
          ═══════════════════════════════════════════════ */}
      <footer className="bg-slate-900 text-slate-300 py-16">
        <div className="max-w-6xl mx-auto px-4 lg:px-6">
          <div className="grid md:grid-cols-4 gap-10 mb-10">
            {/* Brand */}
            <div className="md:col-span-1">
              <div className="flex items-center gap-2 mb-4">
                <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-teal-500 to-cyan-600 flex items-center justify-center text-white font-black text-lg">
                  Q
                </div>
                <span className="font-black text-lg text-white">Qudra Academy</span>
              </div>
              <p className="text-sm text-slate-400 leading-relaxed">
                Empowering students to achieve their best GAT scores through adaptive learning technology.
              </p>
            </div>

            {/* Quick Links */}
            <div>
              <h4 className="font-bold text-white mb-4">Quick Links</h4>
              <ul className="space-y-2 text-sm">
                <li><button onClick={() => scrollTo('course')} className="hover:text-teal-400 transition">Course</button></li>
                <li><button onClick={() => scrollTo('curriculum')} className="hover:text-teal-400 transition">Curriculum</button></li>
                <li><button onClick={() => scrollTo('features')} className="hover:text-teal-400 transition">Features</button></li>
                <li><button onClick={() => scrollTo('reviews')} className="hover:text-teal-400 transition">Reviews</button></li>
              </ul>
            </div>

            {/* Legal */}
            <div>
              <h4 className="font-bold text-white mb-4">Legal</h4>
              <ul className="space-y-2 text-sm">
                <li><button className="hover:text-teal-400 transition">Privacy Policy</button></li>
                <li><button className="hover:text-teal-400 transition">Terms of Service</button></li>
                <li><button className="hover:text-teal-400 transition">Refund Policy</button></li>
              </ul>
            </div>

            {/* Contact */}
            <div>
              <h4 className="font-bold text-white mb-4">Contact</h4>
              <ul className="space-y-2 text-sm">
                <li className="flex items-center gap-2">
                  <MessageCircle className="w-4 h-4" />
                  <span>support@qudra.academy</span>
                </li>
              </ul>
            </div>
          </div>

          <div className="border-t border-slate-800 pt-8 text-center text-sm text-slate-500">
            <p>&copy; 2026 Qudra Academy. All rights reserved.</p>
          </div>
        </div>
      </footer>
    </div>
  );
}
