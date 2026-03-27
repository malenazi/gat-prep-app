import { test, expect } from '@playwright/test';
import { TEST_USERS } from '../fixtures/test-data';

test.describe('Analytics', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/');
    await page.getByText('Register Now').first().click();
    await page.getByText(TEST_USERS.sara.name).click();
    await page.getByText('Analytics', { exact: true }).click();
    await expect(page).toHaveURL(/.*analytics.*/);
  });

  test('analytics page loads', async ({ page }) => {
    await expect(page.getByText(/Analytics|Performance/i)).toBeVisible();
  });

  test('skill breakdown is visible', async ({ page }) => {
    await expect(page.getByText('Verbal')).toBeVisible();
    await expect(page.getByText('Quant')).toBeVisible();
  });

  test('stats cards are visible', async ({ page }) => {
    await expect(page.getByText(/Questions|Correct|Accuracy/i)).toBeVisible();
  });
});
