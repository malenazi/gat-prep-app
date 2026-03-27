import { test, expect } from '@playwright/test';
import { TEST_USERS } from '../fixtures/test-data';

test.describe('Study Plan', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/');
    await page.getByText('Register Now').first().click();
    await page.getByText(TEST_USERS.sara.name).click();
    await page.getByText('Plan', { exact: true }).click();
    await expect(page).toHaveURL(/.*plan.*/);
  });

  test('plan page loads with 30-day plan', async ({ page }) => {
    await expect(page.getByText(/Study Plan|30 Day/i)).toBeVisible();
    
    // Should show multiple days
    const dayElements = page.locator('text=/Day \\d+/');
    await expect(dayElements).toHaveCount(30);
  });

  test('current day is highlighted', async ({ page }) => {
    // Current day should have special styling
    const currentDay = page.locator('[class*="current"], [class*="active"], [class*="today"]').first();
    await expect(currentDay).toBeVisible();
  });

  test('phase labels are visible', async ({ page }) => {
    await expect(page.getByText(/Foundation|Building|Mastery/i)).toBeVisible();
  });

  test('day details panel works', async ({ page }) => {
    // Click on a day
    await page.locator('text=/Day \\d+/').first().click();
    
    // Details should appear
    await expect(page.getByText(/Target|Questions|Completed/i)).toBeVisible();
  });
});
