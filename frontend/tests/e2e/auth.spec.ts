import { expect, test } from '@playwright/test';
import { TEST_USERS, loginAsAdmin, loginAsSara, openAuth } from './helpers';

test.describe('Auth Flow', () => {
  test('logs in with a bootstrapped learner account', async ({ page }) => {
    await loginAsSara(page);
    await expect(page.getByTestId('topbar-greeting')).toContainText(TEST_USERS.progress.name);
  });

  test('redirects admins straight to the admin page after sign-in', async ({ page }) => {
    await loginAsAdmin(page);
    await expect(page).toHaveURL(/\/admin$/);
    await expect(page.getByTestId('admin-page')).toBeVisible();
  });

  test('shows an inline error for invalid credentials', async ({ page }) => {
    await openAuth(page);
    await page.getByTestId('auth-email').fill('invalid@example.com');
    await page.getByTestId('auth-password').fill('wrongpassword');
    await page.getByTestId('auth-submit').click();

    await expect(page.getByTestId('auth-error')).toBeVisible();
  });

  test('registers a fresh learner and sends them to diagnostic', async ({ page }) => {
    const email = `qa-${Date.now()}@example.com`;

    await openAuth(page);
    await page.getByTestId('auth-create-account-shortcut').click();
    await page.getByTestId('auth-name').fill('QA Learner');
    await page.getByTestId('auth-email').fill(email);
    await page.getByTestId('auth-password').fill('LearnerPass123!');
    await page.getByTestId('auth-submit').click();

    await expect(page.getByTestId('diagnostic-page')).toBeVisible();
    await expect(page.getByTestId('diagnostic-start')).toBeVisible();
  });

  test('signs the learner in when registration is retried with an existing email and the same password', async ({ page, request }) => {
    const email = `dup-${Date.now()}@example.com`;
    const password = 'LearnerPass123!';

    const registerResponse = await request.post('/api/auth/register', {
      data: {
        name: 'Duplicate Retry Learner',
        email,
        password,
      },
      headers: {
        'x-forwarded-for': '203.0.113.81',
      },
    });
    expect(registerResponse.ok()).toBeTruthy();

    await openAuth(page);
    await page.getByTestId('auth-create-account-shortcut').click();
    await page.getByTestId('auth-name').fill('Duplicate Retry Learner');
    await page.getByTestId('auth-email').fill(email);
    await page.getByTestId('auth-password').fill(password);
    await page.getByTestId('auth-submit').click();

    await expect(page.getByTestId('diagnostic-page')).toBeVisible();
    await expect(page.getByTestId('diagnostic-start')).toBeVisible();
  });

  test('guides the learner back to sign in when registration is retried with an existing email and a different password', async ({ page, request }) => {
    const email = `dup-guidance-${Date.now()}@example.com`;
    const originalPassword = 'LearnerPass123!';

    const registerResponse = await request.post('/api/auth/register', {
      data: {
        name: 'Duplicate Guidance Learner',
        email,
        password: originalPassword,
      },
      headers: {
        'x-forwarded-for': '203.0.113.82',
      },
    });
    expect(registerResponse.ok()).toBeTruthy();

    await openAuth(page);
    await page.getByTestId('auth-create-account-shortcut').click();
    await page.getByTestId('auth-name').fill('Duplicate Guidance Learner');
    await page.getByTestId('auth-email').fill(email);
    await page.getByTestId('auth-password').fill('DifferentPass456!');
    await page.getByTestId('auth-submit').click();

    await expect(page.getByTestId('auth-error')).toContainText('This email already has an account');
    await expect(page.getByTestId('auth-submit')).toContainText('Sign In');
    await expect(page.getByTestId('auth-email')).toHaveValue(email);
    await expect(page.getByTestId('auth-password')).toHaveValue('');
    await expect(page.getByTestId('auth-forgot-password')).toBeVisible();
  });

  test('resets a learner password from the forgot-password flow', async ({ page, request }) => {
    const email = `reset-ui-${Date.now()}@example.com`;
    const originalPassword = 'LearnerPass123!';
    const updatedPassword = 'ResetPass456!';

    const registerResponse = await request.post('/api/auth/register', {
      data: {
        name: 'Reset Flow Learner',
        email,
        password: originalPassword,
      },
      headers: {
        'x-forwarded-for': '203.0.113.77',
      },
    });
    expect(registerResponse.ok()).toBeTruthy();

    await openAuth(page);
    await page.getByTestId('auth-forgot-password').click();
    await expect(page.getByTestId('forgot-password-form')).toBeVisible();

    await page.getByTestId('forgot-email').fill(email);
    await page.getByTestId('forgot-request-submit').click();

    await expect(page.getByTestId('forgot-request-message')).toBeVisible();
    const resetToken = await page.getByTestId('forgot-preview-token').textContent();
    expect(resetToken).toBeTruthy();

    await page.getByTestId('forgot-reset-token').fill(resetToken ?? '');
    await page.getByTestId('forgot-new-password').fill(updatedPassword);
    await page.getByTestId('forgot-confirm-password').fill(updatedPassword);
    await page.getByTestId('forgot-reset-submit').click();

    await expect(page.getByTestId('auth-success')).toContainText('Password updated');
    await page.getByTestId('auth-submit').click();

    await expect(page.getByTestId('diagnostic-page')).toBeVisible();
  });
});
