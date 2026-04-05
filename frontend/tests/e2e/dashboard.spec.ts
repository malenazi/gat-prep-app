import { expect, test } from '@playwright/test';
import { TEST_USERS, loginAsSara } from './helpers';

test.describe('Dashboard', () => {
  test.beforeEach(async ({ page }) => {
    await loginAsSara(page);
  });

  test('renders the main learner dashboard cards', async ({ page }) => {
    await expect(page.getByTestId('dashboard-page')).toBeVisible();
    await expect(page.getByTestId('dashboard-session-card')).toBeVisible();
    await expect(page.getByTestId('dashboard-score-card')).toBeVisible();
    await expect(page.getByTestId('dashboard-plan-card')).toBeVisible();
    await expect(page.getByTestId('dashboard-mastery-map')).toBeVisible();
    await expect(page.getByTestId('dashboard-league')).toBeVisible();
  });

  test('shows the authenticated learner in the top bar', async ({ page }) => {
    await expect(page.getByTestId('topbar-greeting')).toContainText(TEST_USERS.progress.name);
    await expect(page.getByTestId('topbar-day')).toContainText('Day');
  });
});
