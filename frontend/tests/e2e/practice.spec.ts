import { expect, test } from '@playwright/test';
import { answerPracticeQuestion, goToPractice, loginAsSara } from './helpers';

test.describe('Practice Session', () => {
  test.beforeEach(async ({ page }) => {
    await loginAsSara(page);
    await goToPractice(page);
  });

  test('loads a question with options and timer', async ({ page }) => {
    await expect(page.getByTestId('practice-question-text')).toBeVisible();
    await expect(page.getByTestId('practice-adaptive-panel')).toBeVisible();
    await expect(page.getByTestId('practice-level-chip')).toBeVisible();
    await expect(page.getByTestId('practice-challenge-chip')).toBeVisible();
    await expect(page.getByTestId('practice-skill-mastery')).toBeVisible();
    await expect(page.getByTestId('practice-timer')).toBeVisible();
    await expect(page.getByTestId('practice-option-a')).toBeVisible();
    await expect(page.getByTestId('practice-option-b')).toBeVisible();
    await expect(page.getByTestId('practice-option-c')).toBeVisible();
    await expect(page.getByTestId('practice-option-d')).toBeVisible();
  });

  test('reveals hints on demand without auto-opening the reason panel', async ({ page }) => {
    await expect(page.getByTestId('practice-selection-reason')).toHaveCount(0);
    await expect(page.getByTestId('practice-hint-panel')).toBeVisible();
    await expect(page.getByTestId('practice-hint-1')).toHaveCount(0);

    await page.getByTestId('practice-hint-reveal').click();
    await expect(page.getByTestId('practice-hint-1')).toBeVisible();

    await page.getByTestId('practice-selection-reason-toggle').click();
    await expect(page.getByTestId('practice-selection-reason')).toBeVisible();
  });

  test('submits an answer and advances to a new question', async ({ page }) => {
    const questionBefore = await answerPracticeQuestion(page, 'a');
    await expect(page.getByTestId('practice-adaptive-recap')).toBeVisible();
    await page.getByTestId('practice-next').click();

    await expect(page.getByTestId('practice-question-card')).toBeVisible();
    await expect(page.getByTestId('practice-question-text')).not.toHaveText(questionBefore ?? '');
  });
});
