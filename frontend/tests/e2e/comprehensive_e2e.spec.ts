import { expect, test } from '@playwright/test';
import { answerPracticeQuestion, goToAnalytics, goToPlan, goToPractice, loginAsSara } from './helpers';

test.describe('Learner Journey', () => {
  test('completes a realistic cross-page flow', async ({ page }) => {
    await loginAsSara(page);

    await goToPractice(page);
    await answerPracticeQuestion(page, 'a');
    await page.getByTestId('practice-next').click();

    await goToPlan(page);
    await expect(page.getByTestId('plan-detail')).toBeVisible();

    await goToAnalytics(page);
    await expect(page.getByTestId('analytics-score-card')).toBeVisible();

    await page.getByTestId('nav-home').click();
    await expect(page.getByTestId('dashboard-page')).toBeVisible();
  });
});
