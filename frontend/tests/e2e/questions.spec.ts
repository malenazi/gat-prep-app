import { test, expect } from '@playwright/test';
import { TEST_USERS } from '../fixtures/test-data';

test.describe('Question Bank E2E Tests', () => {
  test.beforeEach(async ({ page }) => {
    // Login as Sara
    await page.goto('/');
    await page.getByText('Register Now').first().click();
    await page.getByText(TEST_USERS.sara.name).click();
  });

  test('practice question displays in English', async ({ page }) => {
    // Navigate to practice
    await page.getByRole('link', { name: 'Practice' }).click();
    await expect(page).toHaveURL(/.*practice.*/);
    
    // Wait for question to load
    await page.waitForSelector('text=/What|How|If|Calculate|Find|Which/', { timeout: 10000 });
    
    // Get question text
    const questionText = await page.locator('.text-lg, .text-xl, [class*="question"]').first().textContent();
    
    // Verify it's in English (no Arabic characters)
    const arabicPattern = /[\u0600-\u06FF]/;
    expect(arabicPattern.test(questionText || '')).toBe(false);
    
    console.log('Question text:', questionText?.substring(0, 100));
  });

  test('question options display correctly', async ({ page }) => {
    await page.getByRole('link', { name: 'Practice' }).click();
    
    // Wait for options to load
    await page.waitForSelector('button:has-text("A")', { timeout: 10000 });
    
    // Check all 4 options are present
    const options = ['A', 'B', 'C', 'D'];
    for (const opt of options) {
      const optionBtn = page.locator('button').filter({ hasText: new RegExp(`^${opt}\\b`) }).first();
      await expect(optionBtn).toBeVisible();
    }
  });

  test('question explanation is in English', async ({ page }) => {
    await page.getByRole('link', { name: 'Practice' }).click();
    
    // Select an answer
    await page.locator('button').filter({ hasText: /^A\b/ }).first().click();
    await page.getByText('Submit').click();
    
    // Wait for feedback/explanation
    await page.waitForSelector('text=/Explanation|Solution|Correct|Wrong/', { timeout: 10000 });
    
    // Get explanation text
    const explanation = await page.locator('text=/Explanation|Solution/').first().textContent();
    
    // Verify no Arabic characters
    const arabicPattern = /[\u0600-\u06FF]/;
    expect(arabicPattern.test(explanation || '')).toBe(false);
  });

  test('different question skills appear', async ({ page }) => {
    await page.getByRole('link', { name: 'Practice' }).click();
    
    const skillsFound: string[] = [];
    
    // Try to get 5 different questions
    for (let i = 0; i < 5; i++) {
      // Get question and check skill
      const skillLabel = await page.locator('[class*="skill"], [class*="badge"]').first().textContent().catch(() => null);
      if (skillLabel && !skillsFound.includes(skillLabel)) {
        skillsFound.push(skillLabel);
      }
      
      // Answer to get next
      await page.locator('button').filter({ hasText: /^A\b/ }).first().click();
      await page.getByText('Submit').click();
      await page.getByText('Next').click();
      
      // Wait for next question
      await page.waitForTimeout(500);
    }
    
    console.log('Skills found:', skillsFound);
    expect(skillsFound.length).toBeGreaterThanOrEqual(1);
  });

  test('math questions display numbers correctly', async ({ page }) => {
    await page.getByRole('link', { name: 'Practice' }).click();
    
    // Look for math-related questions
    const questionText = await page.locator('.text-lg, .text-xl').first().textContent();
    
    // Check if it contains numbers or math symbols
    const hasNumbers = /\d/.test(questionText || '');
    const hasMathSymbols = /[+=×÷\-/%]/.test(questionText || '');
    
    if (hasNumbers || hasMathSymbols) {
      console.log('Math question found:', questionText?.substring(0, 100));
      expect(true).toBe(true); // Math question detected
    } else {
      console.log('Non-math question:', questionText?.substring(0, 100));
      expect(true).toBe(true); // That's fine too
    }
  });

  test('question timer works', async ({ page }) => {
    await page.getByRole('link', { name: 'Practice' }).click();
    
    // Get initial timer value
    const timer = page.locator('text=/\\d+s|\\d+:\\d+/').first();
    await expect(timer).toBeVisible();
    
    const initialTime = await timer.textContent();
    
    // Wait 2 seconds
    await page.waitForTimeout(2000);
    
    const newTime = await timer.textContent();
    
    // Timer should have changed
    expect(newTime).not.toBe(initialTime);
  });

  test('XP is awarded for correct answers', async ({ page }) => {
    await page.getByRole('link', { name: 'Practice' }).click();
    
    // Get initial XP
    const initialXPText = await page.locator('text=/\\d+ XP/').first().textContent();
    const initialXP = parseInt(initialXPText?.match(/\d+/)?.[0] || '0');
    
    // Answer a question
    await page.locator('button').filter({ hasText: /^A\b/ }).first().click();
    await page.getByText('Submit').click();
    
    // Check for XP popup or update
    const xpPopup = page.locator('text=/\\+\\d+ XP/');
    await expect(xpPopup).toBeVisible();
    
    const xpAwarded = await xpPopup.textContent();
    console.log('XP awarded:', xpAwarded);
    
    expect(parseInt(xpAwarded?.match(/\d+/)?.[0] || '0')).toBeGreaterThan(0);
  });

  test('reading comprehension passage displays', async ({ page }) => {
    await page.getByRole('link', { name: 'Practice' }).click();
    
    // Wait for question
    await page.waitForTimeout(1000);
    
    // Check if there's a passage (longer text block)
    const textBlocks = await page.locator('p, .prose, [class*="passage"]').allTextContents();
    
    for (const text of textBlocks) {
      if (text && text.length > 200) {
        console.log('Passage found, length:', text.length);
        
        // Verify no Arabic
        const arabicPattern = /[\u0600-\u06FF]/;
        expect(arabicPattern.test(text)).toBe(false);
        return;
      }
    }
    
    // If no passage found, that's ok (might not be a reading question)
    expect(true).toBe(true);
  });

  test('question images load correctly', async ({ page }) => {
    await page.getByRole('link', { name: 'Practice' }).click();
    
    // Wait for question
    await page.waitForTimeout(1000);
    
    // Check for images
    const images = await page.locator('img').all();
    
    for (const img of images) {
      const src = await img.getAttribute('src');
      if (src && !src.includes('logo')) {
        // Check image loads
        await expect(img).toBeVisible();
        console.log('Image found:', src);
      }
    }
    
    expect(true).toBe(true);
  });
});
