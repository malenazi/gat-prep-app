/**
 * Shared display text and generic selectors for E2E tests.
 */

export const INVALID_USER = {
  email: 'invalid@example.com',
  password: 'wrongpassword',
};

export const EXPECTED_TEXT = {
  landing: {
    title: 'Master the GAT Exam',
    subtitle: 'AI-powered adaptive learning with 1,318+ practice questions.',
    ctaButton: 'Get Started Free',
  },
  navigation: {
    home: 'Home',
    practice: 'Practice',
    plan: 'Plan',
    analytics: 'Analytics',
    admin: 'Admin Panel',
  },
  skills: [
    'Reading Comprehension',
    'Verbal Analogy',
    'Sentence Completion',
    'Contextual Error',
    'Odd Word Out',
    'Arithmetic',
    'Geometry',
    'Algebra',
    'Statistics & Analysis',
  ],
};

export const SELECTORS = {
  // Landing page
  landing: {
    navCourse: 'text=Course',
    navCurriculum: 'text=Curriculum',
    navReviews: 'text=Reviews',
    loginButton: 'text=Login',
    registerButton: 'text=Get Started Free',
    mobileMenuButton: 'button:has(svg)',
  },
  // Auth
  auth: {
    emailInput: 'input[type="email"]',
    passwordInput: 'input[type="password"]',
    nameInput: 'input[type="text"]',
    submitButton: 'button[type="submit"]',
    createAccountButton: 'text=Create New Account',
  },
  // Dashboard
  dashboard: {
    welcomeText: (name: string) => `text=Hello, ${name}`,
    dayProgress: 'text=Day',
    xpCounter: 'text=XP',
    streakCounter: 'text=day',
    practiceButton: 'text=Start Session',
    mockExamButton: 'text=Mock Exam',
  },
  // Navigation
  nav: {
    sidebar: 'aside',
    homeLink: 'text=Home',
    practiceLink: 'text=Practice',
    planLink: 'text=Plan',
    analyticsLink: 'text=Analytics',
    logoutButton: 'text=Logout',
  },
  // Practice
  practice: {
    questionCard: '[data-testid="question-card"]',
    optionA: 'text=A',
    optionB: 'text=B',
    optionC: 'text=C',
    optionD: 'text=D',
    submitButton: 'text=Submit',
    nextButton: 'text=Next',
    timer: '[data-testid="timer"]',
  },
};
