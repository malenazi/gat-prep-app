import { test, expect } from '@playwright/test';
import { TEST_USERS, EXPECTED_TEXT } from '../fixtures/test-data';

test.describe('Dashboard', () => {
  test.beforeEach(async ({ page }) => {
    // Login as Sara
    await page.goto('/');
    await page.getByText('Register Now').first().click();
    await page.getByText(TEST_USERS.sara.name).click();
    
    // Wait for dashboard to load
    await expect(page.getByText(`Hello, ${TEST_USERS.sara.name}`)).toBeVisible();
  });

  test('dashboard loads with correct user info', async ({ page }) => {
    // Check user name
    await expect(page.getByText(`Hello, ${TEST_USERS.sara.name}`)).toBeVisible();
    
    // Check day progress
    await expect(page.getByText(`Day ${TEST_USERS.sara.day} of 30`)).toBeVisible();
    
    // Check XP is displayed
    await expect(page.locator('text=/\\d+ XP/')).toBeVisible();
    
    // Check streak
    await expect(page.locator('text=/\\d+ day/')).toBeVisible();
  });

  test('predicted score is visible', async ({ page }) => {
    await expect(page.getByText(/Predicted Score/i)).toBeVisible();
    await expect(page.locator('text=/\\d+–\\d+/')).toBeVisible();
  });

  test('badges section loads', async ({ page }) => {
    await expect(page.getByText(/Badges|First Step/i)).toBeVisible();
  });

  test('skill progress bars are visible', async ({ page }) => {
    // Check for skill section
    await expect(page.getByText('Verbal')).toBeVisible();
    await expect(page.getByText('Quant')).toBeVisible();
  });

  test('weekly league section is visible', async ({ page }) => {
    await expect(page.getByText(/Bronze|Silver|Gold|Weekly League/i)).toBeVisible();
  });

  test('accomplishment stats are visible', async ({ page }) => {
    await expect(page.getByText(/Days Completed|Questions Answered/i)).toBeVisible();
  });

  test('navigation to Practice works', async ({ page }) => {
    await page.getByText('Practice', { exact: true }).click();
    await expect(page).toHaveURL(/.*practice.*/);
    await expect(page.getByText(/Question|Practice Session/i)).toBeVisible();
  });

  test('navigation to Plan works', async ({ page }) => {
    await page.getByText('Plan', { exact: true }).click();
    await expect(page).toHaveURL(/.*plan.*/);
    await expect(page.getByText(/Study Plan|Day \d+/i)).toBeVisible();
  });

  test('navigation to Analytics works', async ({ page }) => {
    await page.getByText('Analytics', { exact: true }).click();
    await expect(page).toHaveURL(/.*analytics.*/);
    await expect(page.getByText(/Analytics|Performance|Accuracy/i)).toBeVisible();
  });

  test('sidebar navigation is on the left (LTR)', async ({ page }) => {
    const sidebar = page.locator('aside');
    await expect(sidebar).toBeVisible();
    
    // Check sidebar is positioned on the left
    const box = await sidebar.boundingBox();
    expect(box?.x).toBeLessThan(100); // Should be near left edge
  });

  test('main content has left margin for sidebar', async ({ page }) => {
    const main = page.locator('main');
    const box = await main.boundingBox();
    
    // In LTR layout, main content should have left margin for sidebar
    expect(box?.x).toBeGreaterThan(200);
  });

  test('mobile navigation works', async ({ page }) => {
    // Set mobile viewport
    await page.setViewportSize({ width: 375, height: 667 });
    
    // Mobile nav should be at bottom
    const mobileNav = page.locator('nav').filter({ has: page.getByText('Home') });
    await expect(mobileNav).toBeVisible();
  });
});
