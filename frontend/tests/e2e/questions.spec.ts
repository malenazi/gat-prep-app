import { expect, test } from '@playwright/test';
import { goToPractice, loginAsSara } from './helpers';

const arabicPattern = /[\u0600-\u06FF]/;

test.describe('Question Content', () => {
  test.beforeEach(async ({ page }) => {
    await loginAsSara(page);
    await goToPractice(page);
  });

  test('renders English question text and answer options', async ({ page }) => {
    const questionText = await page.getByTestId('practice-question-text').textContent();
    expect(arabicPattern.test(questionText ?? '')).toBe(false);

    for (const key of ['a', 'b', 'c', 'd'] as const) {
      const optionText = await page.getByTestId(`practice-option-${key}`).textContent();
      expect(optionText?.length ?? 0).toBeGreaterThan(0);
      expect(arabicPattern.test(optionText ?? '')).toBe(false);
    }
  });
});
