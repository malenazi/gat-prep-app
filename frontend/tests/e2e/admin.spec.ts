import { test, expect } from '@playwright/test';
import { TEST_USERS } from '../fixtures/test-data';

test.describe('Admin Panel', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/');
    await page.getByText('Register Now').first().click();
    await page.getByText(TEST_USERS.admin.name).click();
  });

  test('admin dashboard loads', async ({ page }) => {
    await expect(page.getByText('Admin Panel')).toBeVisible();
    await expect(page.getByText(/Overview|Dashboard/i)).toBeVisible();
  });

  test('users table is visible', async ({ page }) => {
    await page.getByText(/Users|Students/i).click();
    await expect(page.locator('table')).toBeVisible();
    await expect(page.getByText(/Name|Email|Day/i)).toBeVisible();
  });

  test('questions table is visible', async ({ page }) => {
    await page.getByText(/Questions|Question Bank/i).click();
    await expect(page.locator('table')).toBeVisible();
  });

  test('feedback section is visible', async ({ page }) => {
    await page.getByText(/Feedback|Reviews/i).click();
    await expect(page.getByText(/Rating|Comment/i)).toBeVisible();
  });
});
