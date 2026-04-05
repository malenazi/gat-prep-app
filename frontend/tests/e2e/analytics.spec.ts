import { expect, test } from '@playwright/test';
import { goToAnalytics, loginAsSara } from './helpers';

test.describe('Analytics', () => {
  test.beforeEach(async ({ page }) => {
    await loginAsSara(page);
    await goToAnalytics(page);
  });

  test('renders the analytics overview cards', async ({ page }) => {
    await expect(page.getByTestId('analytics-stats')).toBeVisible();
    await expect(page.getByTestId('analytics-score-card')).toBeVisible();
    await expect(page.getByTestId('analytics-verbal')).toBeVisible();
    await expect(page.getByTestId('analytics-quant')).toBeVisible();
  });
});
