import { expect, test } from '@playwright/test';
import { goToAnalytics, goToPlan, goToPractice, loginAsSara } from './helpers';

const arabicPattern = /[\u0600-\u06FF]/;

test.describe('English UI Check', () => {
  test('keeps the main authenticated flow in English', async ({ page }) => {
    await loginAsSara(page);

    const dashboardText = await page.getByTestId('dashboard-page').textContent();
    expect(arabicPattern.test(dashboardText ?? '')).toBe(false);

    await goToPractice(page);
    const practiceText = await page.getByTestId('practice-question-card').textContent();
    expect(arabicPattern.test(practiceText ?? '')).toBe(false);

    await goToPlan(page);
    const planText = await page.getByTestId('plan-detail').textContent();
    expect(arabicPattern.test(planText ?? '')).toBe(false);

    await goToAnalytics(page);
    const analyticsText = await page.getByTestId('analytics-page').textContent();
    expect(arabicPattern.test(analyticsText ?? '')).toBe(false);
  });
});
