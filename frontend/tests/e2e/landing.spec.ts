import { expect, test } from '@playwright/test';
import { openAuth, visitLanding } from './helpers';

test.describe('Landing Page', () => {
  test('shows the main CTA and navigation', async ({ page }) => {
    await visitLanding(page);

    await expect(page.getByTestId('landing-logo')).toBeVisible();
    await expect(page.getByTestId('landing-nav-course')).toBeVisible();
    await expect(page.getByTestId('landing-nav-curriculum')).toBeVisible();
    await expect(page.getByTestId('landing-nav-features')).toBeVisible();
    await expect(page.getByTestId('landing-nav-reviews')).toBeVisible();
    await expect(page.getByTestId('landing-hero-start')).toBeVisible();
    await expect(page.getByTestId('landing-faq')).toBeVisible();
  });

  test('opens the auth flow from the landing CTA', async ({ page }) => {
    await openAuth(page);
    await expect(page.getByTestId('auth-submit')).toBeVisible();
  });
});
