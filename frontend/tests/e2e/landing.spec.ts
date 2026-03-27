import { test, expect } from '@playwright/test';
import { EXPECTED_TEXT } from '../fixtures/test-data';

test.describe('Landing Page', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/');
  });

  test('page loads with correct title and content', async ({ page }) => {
    // Check page title
    await expect(page).toHaveTitle(/Qudra Academy/);
    
    // Check main heading
    await expect(page.getByText(EXPECTED_TEXT.landing.title)).toBeVisible();
    
    // Check subtitle
    await expect(page.getByText(EXPECTED_TEXT.landing.subtitle)).toBeVisible();
    
    // Check CTA button
    await expect(page.getByText(EXPECTED_TEXT.landing.ctaButton).first()).toBeVisible();
  });

  test('navigation links are visible', async ({ page }) => {
    await expect(page.getByText('Course')).toBeVisible();
    await expect(page.getByText('Curriculum')).toBeVisible();
    await expect(page.getByText('Reviews')).toBeVisible();
  });

  test('login and register buttons are visible', async ({ page }) => {
    await expect(page.getByText('Login').first()).toBeVisible();
    await expect(page.getByText('Register Now').first()).toBeVisible();
  });

  test('pricing information is displayed', async ({ page }) => {
    await expect(page.getByText('199')).toBeVisible();
    await expect(page.getByText('50%')).toBeVisible();
  });

  test('course features section is visible', async ({ page }) => {
    await expect(page.getByText('Smart Diagnostic Test')).toBeVisible();
    await expect(page.getByText('Adaptive Questions')).toBeVisible();
    await expect(page.getByText('Detailed Analytics')).toBeVisible();
  });

  test('FAQ section works', async ({ page }) => {
    // Scroll to FAQ
    await page.getByText('Frequently Asked Questions').scrollIntoViewIfNeeded();
    
    // Click on first FAQ
    await page.getByText('How long is the course?').click();
    
    // Check answer is visible
    await expect(page.getByText(/30 days/)).toBeVisible();
  });

  test('mobile menu works on small viewport', async ({ page }) => {
    // Set mobile viewport
    await page.setViewportSize({ width: 375, height: 667 });
    
    // Mobile menu button should be visible
    const menuButton = page.locator('button').filter({ has: page.locator('svg') }).first();
    await expect(menuButton).toBeVisible();
    
    // Click to open menu
    await menuButton.click();
    
    // Check menu items are visible
    await expect(page.getByText('Course')).toBeVisible();
    await expect(page.getByText('Login')).toBeVisible();
  });

  test('page has correct LTR direction', async ({ page }) => {
    const html = page.locator('html');
    await expect(html).toHaveAttribute('dir', 'ltr');
    await expect(html).toHaveAttribute('lang', 'en');
  });

  test('sidebar is on the left side (LTR layout)', async ({ page }) => {
    // This test will run after login
    // For now, just verify the HTML direction
    const body = page.locator('body');
    const direction = await body.evaluate(el => getComputedStyle(el).direction);
    expect(direction).toBe('ltr');
  });
});
