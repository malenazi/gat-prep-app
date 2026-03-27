import { test, expect } from '@playwright/test';
import { TEST_USERS } from '../fixtures/test-data';

test.describe('Practice Session', () => {
  test.beforeEach(async ({ page }) => {
    // Login as Sara
    await page.goto('/');
    await page.getByText('Register Now').first().click();
    await page.getByText(TEST_USERS.sara.name).click();
    
    // Navigate to Practice
    await page.getByText('Practice', { exact: true }).click();
    await expect(page).toHaveURL(/.*practice.*/);
  });

  test('practice page loads with question', async ({ page }) => {
    // Check question is displayed
    await expect(page.locator('.text-lg, .text-xl').first()).toBeVisible();
    
    // Check options are visible (A, B, C, D)
    const options = page.locator('button').filter({ hasText: /^(A|B|C|D)\b/ });
    await expect(options).toHaveCount(4);
  });

  test('timer is visible and counts down', async ({ page }) => {
    // Look for timer element
    const timer = page.locator('text=/\\d+s|\\d+:\\d+/').first();
    await expect(timer).toBeVisible();
    
    // Get initial value
    const initialText = await timer.textContent();
    
    // Wait 2 seconds
    await page.waitForTimeout(2000);
    
    // Timer should have changed
    const newText = await timer.textContent();
    expect(newText).not.toBe(initialText);
  });

  test('select answer option', async ({ page }) => {
    // Click on option A
    const optionA = page.locator('button').filter({ hasText: /^A\b/ }).first();
    await optionA.click();
    
    // Option should be selected/highlighted
    await expect(optionA).toHaveClass(/selected|border-teal|bg-teal/);
  });

  test('submit answer and see feedback', async ({ page }) => {
    // Select an answer
    const optionA = page.locator('button').filter({ hasText: /^A\b/ }).first();
    await optionA.click();
    
    // Submit
    await page.getByText('Submit').click();
    
    // Feedback should appear
    await expect(page.getByText(/Correct|Wrong|✓|✗/)).toBeVisible();
  });

  test('next question loads after submitting', async ({ page }) => {
    // Get current question text
    const questionText = await page.locator('.text-lg, .text-xl').first().textContent();
    
    // Select and submit
    await page.locator('button').filter({ hasText: /^A\b/ }).first().click();
    await page.getByText('Submit').click();
    
    // Click next
    await page.getByText('Next').click();
    
    // New question should load (text changed)
    await page.waitForTimeout(500);
    const newQuestionText = await page.locator('.text-lg, .text-xl').first().textContent();
    expect(newQuestionText).not.toBe(questionText);
  });

  test('session stats update after answering', async ({ page }) => {
    // Check initial stats
    const statsBefore = await page.locator('text=/\\d+\/\\d+/').first().textContent();
    
    // Answer a question
    await page.locator('button').filter({ hasText: /^A\b/ }).first().click();
    await page.getByText('Submit').click();
    await page.getByText('Next').click();
    
    // Stats should update
    await page.waitForTimeout(500);
    const statsAfter = await page.locator('text=/\\d+\/\\d+/').first().textContent();
    expect(statsAfter).not.toBe(statsBefore);
  });

  test('XP earned is displayed', async ({ page }) => {
    // Answer a question
    await page.locator('button').filter({ hasText: /^A\b/ }).first().click();
    await page.getByText('Submit').click();
    
    // XP popup or text should appear
    await expect(page.locator('text=/\\+\\d+ XP/')).toBeVisible();
  });

  test('end session works', async ({ page }) => {
    // Look for end session button
    const endButton = page.getByText(/End|Exit|Stop/i).first();
    if (await endButton.isVisible().catch(() => false)) {
      await endButton.click();
      
      // Should show confirmation or return to dashboard
      await expect(page.getByText(/Confirm|Session Summary|Dashboard/i).first()).toBeVisible();
    }
  });
});
