import { test, expect, chromium, Page } from '@playwright/test';

const BASE_URL = 'https://gat-prep-prod-production.up.railway.app';

// Helper function to login
async function login(page: Page, email: string = 'student@gat.sa', password: string = 'password') {
  await page.goto(`${BASE_URL}/index.html`);
  await page.waitForSelector('text=Register Now', { timeout: 10000 });
  await page.click('text=Register Now');
  await page.waitForTimeout(1000);
  
  // Fill login form
  await page.fill('input[type="email"]', email);
  await page.fill('input[type="password"]', password);
  await page.click('button[type="submit"]');
  await page.waitForTimeout(3000);
}

// Helper to check for Arabic text
async function hasArabicText(page: Page): Promise<boolean> {
  const text = await page.locator('body').textContent() || '';
  return /[\u0600-\u06FF]/.test(text);
}

test.describe('Qudra Academy - Full E2E Test Suite', () => {
  
  test.describe('Landing Page', () => {
    test('displays FREE pricing correctly', async () => {
      const browser = await chromium.launch();
      const page = await browser.newPage();
      
      await page.goto(`${BASE_URL}/index.html`);
      await page.waitForLoadState('networkidle');
      
      // Verify FREE text is visible
      await expect(page.locator('text=FREE').first()).toBeVisible();
      
      // Verify no Arabic text
      expect(await hasArabicText(page)).toBe(false);
      
      await page.screenshot({ path: 'e2e-results/01-landing-free.png', fullPage: true });
      await browser.close();
    });

    test('shows all course features in English', async () => {
      const browser = await chromium.launch();
      const page = await browser.newPage();
      
      await page.goto(`${BASE_URL}/index.html`);
      
      // Check all major sections
      await expect(page.locator('text=General Aptitude Test Preparation Course')).toBeVisible();
      await expect(page.locator('text=30 Days of Intensive Adaptive Training')).toBeVisible();
      await expect(page.locator('text=What Will You Learn in This Course?')).toBeVisible();
      await expect(page.locator('text=Course Curriculum')).toBeVisible();
      await expect(page.locator('text=Student Reviews')).toBeVisible();
      
      await browser.close();
    });
  });

  test.describe('Authentication', () => {
    test('login with demo account works', async () => {
      const browser = await chromium.launch();
      const page = await browser.newPage();
      
      await login(page);
      
      // Verify dashboard loaded
      await expect(page.locator('text=Dashboard').first()).toBeVisible();
      
      await page.screenshot({ path: 'e2e-results/02-dashboard.png' });
      await browser.close();
    });

    test('register new student account', async () => {
      const browser = await chromium.launch();
      const page = await browser.newPage();
      
      await page.goto(`${BASE_URL}/index.html`);
      await page.click('text=Register Now');
      await page.waitForTimeout(1000);
      
      const timestamp = Date.now();
      
      // Create new account
      await page.fill('input[type="text"]', `TestUser${timestamp}`);
      await page.fill('input[type="email"]', `test${timestamp}@test.com`);
      await page.fill('input[type="password"]', 'password123');
      await page.click('button[type="submit"]');
      
      await page.waitForTimeout(3000);
      
      // Should redirect to dashboard or diagnostic
      const url = page.url();
      expect(url.includes('dashboard') || url.includes('diagnostic')).toBe(true);
      
      await page.screenshot({ path: 'e2e-results/03-after-register.png' });
      await browser.close();
    });
  });

  test.describe('Practice - All 9 Skills', () => {
    const skills = [
      { id: 'verbal_reading', name: 'Reading Comprehension' },
      { id: 'verbal_analogy', name: 'Verbal Analogy' },
      { id: 'verbal_completion', name: 'Sentence Completion' },
      { id: 'verbal_error', name: 'Contextual Error' },
      { id: 'verbal_oddword', name: 'Odd Word Out' },
      { id: 'quant_arithmetic', name: 'Arithmetic' },
      { id: 'quant_algebra', name: 'Algebra' },
      { id: 'quant_geometry', name: 'Geometry' },
      { id: 'quant_statistics', name: 'Statistics' },
    ];

    for (const skill of skills) {
      test(`Practice: ${skill.name} - Questions in English`, async () => {
        const browser = await chromium.launch();
        const page = await browser.newPage();
        
        await login(page);
        
        // Navigate to practice
        await page.click('text=Practice');
        await page.waitForTimeout(1500);
        
        // Click on skill
        await page.click(`text=${skill.name}`);
        await page.waitForTimeout(2000);
        
        // Take screenshot
        await page.screenshot({ path: `e2e-results/skill-${skill.id}.png` });
        
        // Verify no Arabic text
        expect(await hasArabicText(page)).toBe(false);
        
        // Verify options A, B, C, D exist
        const buttons = await page.locator('button').allTextContents();
        const hasOptions = buttons.some(t => /\bA\b/.test(t)) && 
                          buttons.some(t => /\bB\b/.test(t)) &&
                          buttons.some(t => /\bC\b/.test(t)) &&
                          buttons.some(t => /\bD\b/.test(t));
        expect(hasOptions).toBe(true);
        
        await browser.close();
      });
    }
  });

  test.describe('Answer Submission & Feedback', () => {
    test('submit answer and verify English feedback', async () => {
      const browser = await chromium.launch();
      const page = await browser.newPage();
      
      await login(page);
      
      // Go to practice
      await page.click('text=Practice');
      await page.waitForTimeout(1500);
      await page.click('text=Algebra');
      await page.waitForTimeout(2000);
      
      // Click option A
      const optionA = page.locator('button:has-text("A")').first();
      await optionA.click();
      await page.waitForTimeout(500);
      
      // Submit
      await page.click('button:has-text("Submit")');
      await page.waitForTimeout(2000);
      
      // Screenshot feedback
      await page.screenshot({ path: 'e2e-results/04-answer-feedback.png' });
      
      // Verify no Arabic in feedback
      expect(await hasArabicText(page)).toBe(false);
      
      await browser.close();
    });
  });

  test.describe('Study Plan', () => {
    test('view study plan page', async () => {
      const browser = await chromium.launch();
      const page = await browser.newPage();
      
      await login(page);
      
      // Navigate to plan
      await page.click('text=Plan');
      await page.waitForTimeout(2000);
      
      await page.screenshot({ path: 'e2e-results/05-study-plan.png', fullPage: true });
      
      // Verify no Arabic
      expect(await hasArabicText(page)).toBe(false);
      
      // Check for English labels
      await expect(page.locator('text=Day').first()).toBeVisible();
      
      await browser.close();
    });
  });

  test.describe('Analytics', () => {
    test('view analytics dashboard', async () => {
      const browser = await chromium.launch();
      const page = await browser.newPage();
      
      await login(page);
      
      // Navigate to analytics
      await page.click('text=Analytics');
      await page.waitForTimeout(2000);
      
      await page.screenshot({ path: 'e2e-results/06-analytics.png', fullPage: true });
      
      // Verify no Arabic
      expect(await hasArabicText(page)).toBe(false);
      
      // Check for English labels
      await expect(page.locator('text=Predicted Score').first()).toBeVisible();
      
      await browser.close();
    });
  });

  test.describe('Mock Exam', () => {
    test('view mock exam page', async () => {
      const browser = await chromium.launch();
      const page = await browser.newPage();
      
      await login(page, 'lujain@gat.sa', 'password'); // Use advanced student
      
      // Navigate to mock exam
      await page.click('text=Mock Exam');
      await page.waitForTimeout(2000);
      
      await page.screenshot({ path: 'e2e-results/07-mock-exam.png' });
      
      // Verify no Arabic
      expect(await hasArabicText(page)).toBe(false);
      
      await browser.close();
    });
  });

  test.describe('Admin Panel', () => {
    test('admin login and view questions', async () => {
      const browser = await chromium.launch();
      const page = await browser.newPage();
      
      await login(page, 'admin@gat.sa', 'admin123');
      
      // Navigate to admin
      await page.click('text=Admin');
      await page.waitForTimeout(2000);
      
      await page.screenshot({ path: 'e2e-results/08-admin-panel.png' });
      
      // Verify no Arabic
      expect(await hasArabicText(page)).toBe(false);
      
      await browser.close();
    });
  });

  test.describe('Navigation & UI', () => {
    test('all navigation links work', async () => {
      const browser = await chromium.launch();
      const page = await browser.newPage();
      
      await login(page);
      
      const pages = [
        { name: 'Dashboard', selector: 'text=Dashboard' },
        { name: 'Practice', selector: 'text=Practice' },
        { name: 'Plan', selector: 'text=Plan' },
        { name: 'Analytics', selector: 'text=Analytics' },
      ];
      
      for (const p of pages) {
        await page.click(p.selector);
        await page.waitForTimeout(1500);
        
        // Verify page loaded (no error)
        const errorVisible = await page.locator('text=Error').isVisible().catch(() => false);
        expect(errorVisible).toBe(false);
        
        // Verify no Arabic
        expect(await hasArabicText(page)).toBe(false);
      }
      
      await browser.close();
    });
  });

  test.describe('Error Handling', () => {
    test('error messages are in English', async () => {
      const browser = await chromium.launch();
      const page = await browser.newPage();
      
      // Try to access protected route without login
      await page.goto(`${BASE_URL}/dashboard`);
      await page.waitForTimeout(2000);
      
      await page.screenshot({ path: 'e2e-results/09-error-page.png' });
      
      // Should redirect or show error in English
      expect(await hasArabicText(page)).toBe(false);
      
      await browser.close();
    });
  });

  test.describe('Complete User Journey', () => {
    test('full student journey', async () => {
      const browser = await chromium.launch();
      const page = await browser.newPage();
      
      // 1. Visit landing page
      await page.goto(`${BASE_URL}/index.html`);
      await page.waitForLoadState('networkidle');
      expect(await hasArabicText(page)).toBe(false);
      
      // 2. Login
      await page.click('text=Register Now');
      await page.waitForTimeout(1000);
      await page.fill('input[type="email"]', 'student@gat.sa');
      await page.fill('input[type="password"]', 'password');
      await page.click('button[type="submit"]');
      await page.waitForTimeout(3000);
      
      // 3. Dashboard
      await expect(page.locator('text=Dashboard').first()).toBeVisible();
      
      // 4. Practice one question
      await page.click('text=Practice');
      await page.waitForTimeout(1500);
      await page.click('text=Verbal Analogy');
      await page.waitForTimeout(2000);
      
      // Answer and submit
      await page.click('button:has-text("A")').catch(() => page.click('text=A').first());
      await page.waitForTimeout(500);
      await page.click('button:has-text("Submit")');
      await page.waitForTimeout(2000);
      
      // 5. Check analytics
      await page.click('text=Analytics');
      await page.waitForTimeout(2000);
      
      // 6. Check study plan
      await page.click('text=Plan');
      await page.waitForTimeout(2000);
      
      // Final screenshot
      await page.screenshot({ path: 'e2e-results/10-full-journey.png', fullPage: true });
      
      // Verify no Arabic throughout journey
      expect(await hasArabicText(page)).toBe(false);
      
      await browser.close();
    });
  });
});