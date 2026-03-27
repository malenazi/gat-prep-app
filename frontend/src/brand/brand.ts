// Brand Identity for قدرة أكاديمي — Qudra Academy
// Complete brand guidelines and design tokens

export const brand = {
  // Brand Name
  name: {
    ar: 'قدرة أكاديمي',
    en: 'Qudra Academy',
    tagline: {
      ar: 'طريقك نحو النجاح',
      en: 'Your Path to Success'
    }
  },

  // Color Palette
  colors: {
    // Primary Colors
    primary: {
      50: '#E8FDF7',
      100: '#C0F8E8',
      200: '#88F0D0',
      300: '#50E8B8',
      400: '#20DCA4',
      500: '#00C8A0', // Main brand color
      600: '#00A888',
      700: '#00A080',
      800: '#007860',
      900: '#006050',
    },
    
    // Secondary Colors (Cyan)
    secondary: {
      50: '#ecfeff',
      100: '#cffafe',
      200: '#a5f3fc',
      300: '#67e8f9',
      400: '#22d3ee',
      500: '#06b6d4',
      600: '#0891b2',
      700: '#0e7490',
    },
    
    // Accent Colors
    accent: {
      gold: '#FFC107',
      amber: '#f59e0b',
      orange: '#f97316',
      violet: '#8b5cf6',
      purple: '#a855f7',
      rose: '#f43f5e',
      pink: '#ec4899',
    },
    
    // Semantic Colors
    semantic: {
      success: '#22c55e',
      warning: '#f59e0b',
      error: '#ef4444',
      info: '#3b82f6',
    },
    
    // Neutral Colors
    neutral: {
      white: '#ffffff',
      50: '#f8fafc',
      100: '#f1f5f9',
      200: '#e2e8f0',
      300: '#cbd5e1',
      400: '#94a3b8',
      500: '#64748b',
      600: '#475569',
      700: '#334155',
      800: '#1e293b',
      900: '#0f172a',
      black: '#000000',
    },
  },

  // Typography
  typography: {
    fontFamily: {
      primary: "'Tajawal', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif",
      arabic: "'Tajawal', sans-serif",
      mono: "'JetBrains Mono', 'Fira Code', monospace",
    },
    fontWeights: {
      light: 300,
      regular: 400,
      medium: 500,
      bold: 700,
      black: 800,
      heavy: 900,
    },
    sizes: {
      xs: '0.75rem',    // 12px
      sm: '0.875rem',   // 14px
      base: '1rem',     // 16px
      lg: '1.125rem',   // 18px
      xl: '1.25rem',    // 20px
      '2xl': '1.5rem',  // 24px
      '3xl': '1.875rem',// 30px
      '4xl': '2.25rem', // 36px
      '5xl': '3rem',    // 48px
      '6xl': '3.75rem', // 60px
      '7xl': '4.5rem',  // 72px
    },
  },

  // Spacing
  spacing: {
    xs: '0.25rem',   // 4px
    sm: '0.5rem',    // 8px
    md: '1rem',      // 16px
    lg: '1.5rem',    // 24px
    xl: '2rem',      // 32px
    '2xl': '2.5rem', // 40px
    '3xl': '3rem',   // 48px
    '4xl': '4rem',   // 64px
    '5xl': '5rem',   // 80px
  },

  // Border Radius
  radius: {
    none: '0',
    sm: '0.25rem',   // 4px
    md: '0.5rem',    // 8px
    lg: '0.75rem',   // 12px
    xl: '1rem',      // 16px
    '2xl': '1.5rem', // 24px
    '3xl': '2rem',   // 32px
    full: '9999px',
  },

  // Shadows
  shadows: {
    sm: '0 1px 2px 0 rgba(0, 0, 0, 0.05)',
    md: '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -2px rgba(0, 0, 0, 0.1)',
    lg: '0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.1)',
    xl: '0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1)',
    '2xl': '0 25px 50px -12px rgba(0, 0, 0, 0.25)',
    brand: '0 4px 20px rgba(0, 200, 160, 0.3)',
    glow: '0 0 30px rgba(0, 200, 160, 0.2)',
    inner: 'inset 0 2px 4px 0 rgba(0, 0, 0, 0.05)',
  },

  // Transitions
  transitions: {
    fast: '150ms ease-in-out',
    base: '200ms ease-in-out',
    slow: '300ms ease-in-out',
    slower: '500ms ease-in-out',
    spring: '300ms cubic-bezier(0.16, 1, 0.3, 1)',
  },

  // Z-Index Scale
  zIndex: {
    hide: -1,
    base: 0,
    docked: 10,
    dropdown: 1000,
    sticky: 1100,
    banner: 1200,
    overlay: 1300,
    modal: 1400,
    popover: 1500,
    skipLink: 1600,
    toast: 1700,
    tooltip: 1800,
  },

  // Breakpoints
  breakpoints: {
    sm: '640px',
    md: '768px',
    lg: '1024px',
    xl: '1280px',
    '2xl': '1536px',
  },

  // Animation Durations
  animation: {
    fast: '150ms',
    base: '200ms',
    slow: '300ms',
    slower: '500ms',
    slowest: '1000ms',
  },
} as const;

// Brand messaging
export const brandMessages = {
  hero: {
    title: 'قدرة أكاديمي',
    subtitle: 'طريقك نحو النجاح',
    description: 'تدرب بذكاء، تعلم بفعالية، وحقق درجات عالية في اختبار القدرات العامة',
  },
  features: {
    diagnostic: {
      title: 'اختبار تشخيصي ذكي',
      description: 'اكتشف مستواك الحالي واحصل على خطة دراسية مخصصة',
    },
    practice: {
      title: 'أسئلة مشابهة للاختبار',
      description: 'تدرب على أسئلة بنفس مستوى صعوبة اختبار القدرات',
    },
    progress: {
      title: 'تتبع تقدمك',
      description: 'راقب تحسنك مع إحصائيات مفصلة وشارات إنجاز',
    },
    explanation: {
      title: 'شرح مفصل',
      description: 'افهم أخطاءك مع شروحات واضحة لكل سؤال',
    },
  },
  cta: {
    primary: 'ابدأ رحلتك الآن',
    secondary: 'شاهد كيف تعمل',
    startFree: 'ابدأ مجاناً',
  },
  stats: {
    students: '10K+ طالب',
    questions: '50K+ سؤال',
    success: '95% نسبة النجاح',
  },
  feedback: {
    excellent: 'أداء ممتاز! استمر في التقدم 🎉',
    good: 'أداء جيد! واصل التدرب 👏',
    keepTrying: 'لا تيأس! استمر في التدرب لتحسين أدائك 💪',
  },
  errors: {
    generic: 'حدث خطأ، يرجى المحاولة مرة أخرى',
    unauthorized: 'يجب تسجيل الدخول أولاً',
    network: 'مشكلة في الاتصال، تحقق من إنترنتك',
  },
  success: {
    login: 'تم تسجيل الدخول بنجاح!',
    logout: 'تم تسجيل الخروج',
    quizStart: 'بدأ الاختبار',
    quizComplete: 'أكملت الاختبار بنجاح!',
  },
} as const;

// Export type for TypeScript support
export type Brand = typeof brand;
export type BrandColors = typeof brand.colors;
export type BrandTypography = typeof brand.typography;

export default brand;
