import { test, expect, chromium } from '@playwright/test';

const BASE_URL = 'https://gat-prep-prod-production.up.railway.app';

// Test 1: Landing Page - Check pricing is FREE
 test('Landing page shows FREE pricing', async () => {
  const browser = await chromium.launch({ headless: false });
  const page = await browser.newPage();
  
  await page.goto(`${BASE_URL}/index.html`);
  await page.waitForLoadState('networkidle');
  await page.screenshot({ path: 'test-results/01-landing-page.png', fullPage: true });
  
  // Check for FREE text
  const freeText = await page.locator('text=FREE').first();
  await expect(freeText).toBeVisible();
  
  console.log('✓ Landing page shows FREE pricing');
  await browser.close();
});

// Test 2: Register new student
 test('Register new student account', async () => {
  const browser = await chromium.launch({ headless: false });
  const page = await browser.newPage();
  
  await page.goto(`${BASE_URL}/index.html`);
  await page.click('text=Register Now');
  await page.waitForTimeout(1000);
  
  // Fill registration form
  const timestamp = Date.now();
  await page.fill('input[type="text"]', `TestStudent${timestamp}`);
  await page.fill('input[type="email"]', `test${timestamp}@example.com`);
  await page.fill('input[type="password"]', 'password123');
  
  await page.screenshot({ path: 'test-results/02-registration-form.png' });
  
  // Submit form
  await page.click('button[type="submit"]');
  await page.waitForTimeout(3000);
  
  await page.screenshot({ path: 'test-results/03-after-register.png', fullPage: true });
  
  console.log('✓ Registration completed');
  await browser.close();
});

// Test 3: Login and check dashboard
 test('Login and view dashboard', async () => {
  const browser = await chromium.launch({ headless: false });
  const page = await browser.newPage();
  
  await page.goto(`${BASE_URL}/index.html`);
  await page.click('text=Register Now');
  await page.waitForTimeout(1000);
  
  // Switch to login
  await page.click('text=Already have an account?');
  await page.fill('input[type="email"]', 'student@gat.sa');
  await page.fill('input[type="password"]', 'password');
  
  await page.click('button[type="submit"]');
  await page.waitForTimeout(3000);
  
  await page.screenshot({ path: 'test-results/04-dashboard.png', fullPage: true });
  
  // Check dashboard loaded
  await expect(page.locator('text=Dashboard')).toBeVisible();
  
  console.log('✓ Dashboard loaded');
  await browser.close();
});

// Test 4: Test all 9 skills show English questions
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
   test(`Skill: ${skill.name} - Questions in English`, async () => {
    const browser = await chromium.launch({ headless: false });
    const page = await browser.newPage();
    
    // Login first
    await page.goto(`${BASE_URL}/index.html`);
    await page.click('text=Register Now');
    await page.waitForTimeout(500);
    await page.click('text=Already have an account?');
    await page.fill('input[type="email"]', 'student@gat.sa');
    await page.fill('input[type="password"]', 'password');
    await page.click('button[type="submit"]');
    await page.waitForTimeout(2000);
    
    // Navigate to practice
    await page.click('text=Practice');
    await page.waitForTimeout(1000);
    
    // Select skill
    await page.click(`text=${skill.name}`);
    await page.waitForTimeout(2000);
    
    // Screenshot the question
    await page.screenshot({ path: `test-results/skill-${skill.id}.png`, fullPage: true });
    
    // Check question text is visible and in English
    const questionText = await page.locator('[class*="question"]').first();
    const text = await questionText.textContent() || '';
    
    // Check for no Arabic characters
    const hasArabic = /[\u0600-\u06FF]/.test(text);
    expect(hasArabic).toBe(false);
    
    // Check options are A, B, C, D
    await expect(page.locator('text=A')).toBeVisible();
    await expect(page.locator('text=B')).toBeVisible();
    await expect(page.locator('text=C')).toBeVisible();
    await expect(page.locator('text=D')).toBeVisible();
    
    console.log(`✓ ${skill.name}: Question in English, Options A/B/C/D`);
    await browser.close();
  });
}

// Test 5: Answer a question and check feedback
 test('Submit answer and check feedback in English', async () => {
  const browser = await chromium.launch({ headless: false });
  const page = await browser.newPage();
  
  // Login
  await page.goto(`${BASE_URL}/index.html`);
  await page.click('text=Register Now');
  await page.waitForTimeout(500);
  await page.click('text=Already have an account?');
  await page.fill('input[type="email"]', 'student@gat.sa');
  await page.fill('input[type="password"]', 'password');
  await page.click('button[type="submit"]');
  await page.waitForTimeout(2000);
  
  // Navigate to practice
  await page.click('text=Practice');
  await page.waitForTimeout(1000);
  await page.click('text=Algebra');
  await page.waitForTimeout(2000);
  
  // Select option A
  await page.click('text=A');
  await page.waitForTimeout(500);
  
  // Submit
  await page.click('text=Submit');
  await page.waitForTimeout(2000);
  
  await page.screenshot({ path: 'test-results/05-answer-feedback.png', fullPage: true });
  
  // Check feedback is in English
  const feedbackText = await page.locator('body').textContent() || '';
  const hasArabic = /[\u0600-\u06FF]/.test(feedbackText);
  expect(hasArabic).toBe(false);
  
  console.log('✓ Answer feedback in English');
  await browser.close();
});

// Test 6: Check all error messages are in English
 test('Error messages in English', async () => {
  const browser = await chromium.launch({ headless: false });
  const page = await browser.newPage();
  
  // Try to access dashboard without login
  await page.goto(`${BASE_URL}/dashboard`);
  await page.waitForTimeout(2000);
  
  await page.screenshot({ path: 'test-results/06-error-message.png' });
  
  // Check error is in English
  const pageText = await page.locator('body').textContent() || '';
  const hasArabic = /[\u0600-\u06FF]/.test(pageText);
  expect(hasArabic).toBe(false);
  
  console.log('✓ Error messages in English');
  await browser.close();
});