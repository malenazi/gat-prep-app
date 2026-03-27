import { test, expect } from '@playwright/test';
import { TEST_USERS, INVALID_USER } from '../fixtures/test-data';

test.describe('Authentication', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/');
    // Wait for page to load
    await page.waitForLoadState('networkidle');
  });

  test('login with demo account - Sara', async ({ page }) => {
    // Click login/register to go to auth page
    await page.getByText('Register Now').first().click();
    
    // Wait for auth form
    await expect(page.getByText('Demo Accounts')).toBeVisible();
    
    // Click on Sara's demo account
    await page.getByText(TEST_USERS.sara.name).click();
    
    // Should redirect to dashboard
    await expect(page).toHaveURL(/\//);
    
    // Verify logged in as Sara
    await expect(page.getByText(`Hello, ${TEST_USERS.sara.name}`)).toBeVisible();
    await expect(page.getByText(`Day ${TEST_USERS.sara.day}`)).toBeVisible();
  });

  test('login with demo account - Mohammed', async ({ page }) => {
    await page.getByText('Register Now').first().click();
    await page.getByText(TEST_USERS.mohammed.name).click();
    
    await expect(page.getByText(`Hello, ${TEST_USERS.mohammed.name}`)).toBeVisible();
    await expect(page.getByText(`Day ${TEST_USERS.mohammed.day}`)).toBeVisible();
  });

  test('login with new student account', async ({ page }) => {
    await page.getByText('Register Now').first().click();
    await page.getByText(TEST_USERS.newStudent.name).click();
    
    await expect(page.getByText(`Hello, ${TEST_USERS.newStudent.name}`)).toBeVisible();
    // New student should be on diagnostic
    await expect(page.getByText(/Diagnostic|Question/)).toBeVisible();
  });

  test('login with admin account', async ({ page }) => {
    await page.getByText('Register Now').first().click();
    await page.getByText(TEST_USERS.admin.name).click();
    
    // Admin should see admin panel
    await expect(page.getByText('Admin Panel')).toBeVisible();
    await expect(page.getByText(/Overview|Users|Questions/)).toBeVisible();
  });

  test('manual login with credentials', async ({ page }) => {
    await page.getByText('Register Now').first().click();
    
    // Click "Create New Account" to show register form, then toggle to login
    await page.getByText('Create New Account').click();
    
    // Toggle to login
    await page.getByText('Already have an account?').click();
    
    // Fill credentials
    await page.fill('input[type="email"]', TEST_USERS.sara.email);
    await page.fill('input[type="password"]', TEST_USERS.sara.password);
    
    // Submit
    await page.click('button[type="submit"]');
    
    // Should be logged in
    await expect(page.getByText(`Hello, ${TEST_USERS.sara.name}`)).toBeVisible();
  });

  test('invalid credentials show error', async ({ page }) => {
    await page.getByText('Register Now').first().click();
    await page.getByText('Create New Account').click();
    await page.getByText('Already have an account?').click();
    
    // Fill invalid credentials
    await page.fill('input[type="email"]', INVALID_USER.email);
    await page.fill('input[type="password"]', INVALID_USER.password);
    
    // Submit
    await page.click('button[type="submit"]');
    
    // Should show error
    await expect(page.getByText(/Invalid|Error|incorrect/i)).toBeVisible();
  });

  test('logout works', async ({ page }) => {
    // Login first
    await page.getByText('Register Now').first().click();
    await page.getByText(TEST_USERS.sara.name).click();
    
    // Wait for dashboard
    await expect(page.getByText(`Hello, ${TEST_USERS.sara.name}`)).toBeVisible();
    
    // Click logout
    await page.getByText('Logout').click();
    
    // Should be back to landing page
    await expect(page.getByText(EXPECTED_TEXT.landing.title)).toBeVisible();
  });

  test('session persists after refresh', async ({ page }) => {
    // Login
    await page.getByText('Register Now').first().click();
    await page.getByText(TEST_USERS.sara.name).click();
    
    // Wait for dashboard
    await expect(page.getByText(`Hello, ${TEST_USERS.sara.name}`)).toBeVisible();
    
    // Refresh page
    await page.reload();
    
    // Should still be logged in
    await expect(page.getByText(`Hello, ${TEST_USERS.sara.name}`)).toBeVisible();
  });
});
