/**
 * Test data for E2E tests
 */

export const TEST_USERS = {
  newStudent: {
    email: 'student@gat.sa',
    password: '123456',
    name: 'New Student',
  },
  sara: {
    email: 'sara@gat.sa',
    password: '123456',
    name: 'Sara Al-Mutairi',
    day: 5,
    phase: 'Foundation',
  },
  mohammed: {
    email: 'mohammed@gat.sa',
    password: '123456',
    name: 'Mohammed Al-Ghamdi',
    day: 15,
    phase: 'Enhancement',
  },
  lujain: {
    email: 'lujain@gat.sa',
    password: '123456',
    name: 'Lujain Al-Harbi',
    day: 25,
    phase: 'Mastery',
  },
  admin: {
    email: 'admin@gat.sa',
    password: 'admin123',
    name: 'System Admin',
  },
};

export const INVALID_USER = {
  email: 'invalid@example.com',
  password: 'wrongpassword',
};

export const EXPECTED_TEXT = {
  landing: {
    title: 'General Aptitude Test Preparation Course',
    subtitle: '30 Days of Intensive Adaptive Training',
    ctaButton: 'Register Now',
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
    registerButton: 'text=Register Now',
    mobileMenuButton: 'button:has(svg)',
  },
  // Auth
  auth: {
    emailInput: 'input[type="email"]',
    passwordInput: 'input[type="password"]',
    nameInput: 'input[type="text"]',
    submitButton: 'button[type="submit"]',
    demoAccount: (name: string) => `text=${name}`,
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
