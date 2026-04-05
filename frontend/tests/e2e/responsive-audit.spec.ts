import { expect, test, type Page, type TestInfo } from '@playwright/test';

import {
  expectNoHorizontalOverflow,
  goToAdmin,
  goToAnalytics,
  goToPlan,
  goToPractice,
  loginAsAdmin,
  loginAsSara,
  loginAsStudent,
  setTheme,
  visitLanding,
} from './helpers';

const mockAuditQuestion = {
  id: 88001,
  skill_id: 'quant_geometry',
  question_type: 'geometry',
  difficulty: 0.52,
  text_ar: 'The diagram shows a circle with radius 7 cm. What is its circumference?',
  passage_ar: null,
  figure_svg:
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 160"><circle cx="110" cy="80" r="56" fill="#fef3c7" stroke="#0f172a" stroke-width="5"/><line x1="110" y1="80" x2="166" y2="80" stroke="#0f172a" stroke-width="5"/><text x="140" y="68" font-size="18" font-family="Arial">7 cm</text></svg>',
  figure_alt: 'Circle diagram with a radius of 7 centimeters',
  table_ar: null,
  table_caption: null,
  content_format: 'markdown_math',
  comparison_columns: null,
  options: [
    { key: 'a', label: 'A', text_ar: '22 cm' },
    { key: 'b', label: 'B', text_ar: '44 cm' },
    { key: 'c', label: 'C', text_ar: '154 cm' },
    { key: 'd', label: 'D', text_ar: '308 cm' },
  ],
  paper_only: false,
};

async function expectPrimaryContentWithinViewport(page: Page, testId: string) {
  const viewport = page.viewportSize();
  expect(viewport).toBeTruthy();

  const rect = await page.getByTestId(testId).evaluate((element) => {
    const bounds = (element as HTMLElement).getBoundingClientRect();
    return {
      left: bounds.left,
      right: bounds.right,
      width: bounds.width,
    };
  });

  expect(rect.left).toBeGreaterThanOrEqual(-1);
  expect(rect.right).toBeLessThanOrEqual((viewport?.width ?? 0) + 1);
  expect(rect.width).toBeGreaterThan(0);
}

async function captureAudit(
  page: Page,
  testInfo: TestInfo,
  label: string,
  testId: string,
  theme: 'light' | 'dark',
) {
  await setTheme(page, theme);
  await expectNoHorizontalOverflow(page);
  await expectPrimaryContentWithinViewport(page, testId);
  await page.screenshot({
    path: testInfo.outputPath(`${label}-${theme}.png`),
    fullPage: true,
  });
}

async function resetClientSession(page: Page) {
  await page.evaluate(() => {
    localStorage.removeItem('gat_token');
    localStorage.removeItem('diagnostic_session');
    localStorage.removeItem('practice_session');
  });
  await page.goto('/');
}

test.describe('Responsive visual audit', () => {
  test('walks the public and learner journey with screenshots in both themes', async ({ page }, testInfo) => {
    test.setTimeout(8 * 60 * 1000);
    const isWebkitAudit = testInfo.project.name.includes('webkit');

    await visitLanding(page);
    await captureAudit(page, testInfo, 'landing', 'landing-page', 'light');
    await captureAudit(page, testInfo, 'landing', 'landing-page', 'dark');

    await page.getByTestId('landing-start').click();
    await expect(page.getByTestId('auth-page')).toBeVisible();
    await captureAudit(page, testInfo, 'auth', 'auth-page', 'light');
    await captureAudit(page, testInfo, 'auth', 'auth-page', 'dark');

    await loginAsStudent(page);
    await expect(page.getByTestId('diagnostic-page')).toBeVisible();
    await captureAudit(page, testInfo, 'diagnostic-intro', 'diagnostic-page', 'light');
    await captureAudit(page, testInfo, 'diagnostic-intro', 'diagnostic-page', 'dark');

    if (!isWebkitAudit) {
      let servedQuestion = false;
      await page.route('**/api/diagnostic/start', async (route) => {
        await route.fulfill({ json: { message: 'Start diagnostic test', total_questions: 9 } });
      });
      await page.route('**/api/diagnostic/next', async (route) => {
        if (!servedQuestion) {
          servedQuestion = true;
          await route.fulfill({
            json: {
              done: false,
              progress: 0,
              total: 9,
              question: mockAuditQuestion,
            },
          });
          return;
        }

        await route.fulfill({ json: { done: true, progress: 1, total: 9 } });
      });
      await page.route('**/api/diagnostic/answer', async (route) => {
        await route.fulfill({
          json: {
            is_correct: true,
            correct_option: 'b',
            explanation_ar: 'Use the circumference formula.',
            solution_steps_ar: ['Identify the radius.', 'Apply the circumference formula.'],
          },
        });
      });
      await page.route('**/api/diagnostic/complete', async (route) => {
        await route.fulfill({
          json: {
            predicted_score: {
              low: 72,
              mid: 79,
              high: 85,
              verbal_mastery: 0.74,
              quant_mastery: 0.83,
            },
          },
        });
      });

      await page.getByTestId('diagnostic-start').click();
      await expect(page.getByTestId('diagnostic-question-card')).toBeVisible();
      await captureAudit(page, testInfo, 'diagnostic-testing', 'diagnostic-page', 'light');
      await captureAudit(page, testInfo, 'diagnostic-testing', 'diagnostic-page', 'dark');

      await page.getByTestId('diagnostic-option-a').click();
      await expect(page.getByTestId('diagnostic-results')).toBeVisible();
      await captureAudit(page, testInfo, 'diagnostic-results', 'diagnostic-results', 'light');
      await captureAudit(page, testInfo, 'diagnostic-results', 'diagnostic-results', 'dark');
    }

    await resetClientSession(page);
    await loginAsSara(page);
    await captureAudit(page, testInfo, 'dashboard-progress', 'dashboard-page', 'light');
    await captureAudit(page, testInfo, 'dashboard-progress', 'dashboard-page', 'dark');

    await goToPractice(page);
    await captureAudit(page, testInfo, 'practice', 'practice-page', 'light');
    await captureAudit(page, testInfo, 'practice', 'practice-page', 'dark');

    await goToPlan(page);
    await page.getByTestId('plan-day-11').scrollIntoViewIfNeeded();
    await page.getByTestId('plan-day-11').click();
    await captureAudit(page, testInfo, 'plan', 'plan-page', 'light');
    await captureAudit(page, testInfo, 'plan', 'plan-page', 'dark');

    if (isWebkitAudit) {
      return;
    }

    await goToAnalytics(page);
    await captureAudit(page, testInfo, 'analytics', 'analytics-page', 'light');
    await captureAudit(page, testInfo, 'analytics', 'analytics-page', 'dark');

    await resetClientSession(page);
    await loginAsAdmin(page);
    await goToAdmin(page);
    await captureAudit(page, testInfo, 'admin-shell', 'admin-page', 'light');
    await captureAudit(page, testInfo, 'admin-shell', 'admin-page', 'dark');

    await page.route('**/api/mock/start?preview=true', async (route) => {
      await route.fulfill({
        json: {
          attempt_id: 601,
          attempt_number: 1,
          total_questions: 1,
          verbal_count: 1,
          quant_count: 0,
          verbal_minutes: 35,
          quant_minutes: 35,
          question_ids: [mockAuditQuestion.id],
        },
      });
    });
    await page.route(`**/api/mock/question/${mockAuditQuestion.id}`, async (route) => {
      await route.fulfill({ json: mockAuditQuestion });
    });
    await page.route('**/api/mock/answer', async (route) => {
      await route.fulfill({ json: { is_correct: true } });
    });
    await page.route('**/api/mock/complete', async (route) => {
      await route.fulfill({
        json: {
          attempt_id: 601,
          attempt_number: 1,
          score: 86,
          total: 1,
          correct: 1,
          verbal_correct: 1,
          verbal_total: 1,
          quant_correct: 0,
          quant_total: 0,
          verbal_pct: 1,
          quant_pct: 0,
        },
      });
    });

    await page.goto('/mock?preview=true');
    await expect(page.getByTestId('mock-page')).toBeVisible();
    await captureAudit(page, testInfo, 'mock-intro', 'mock-page', 'light');
    await captureAudit(page, testInfo, 'mock-intro', 'mock-page', 'dark');

    await page.getByTestId('mock-start').click();
    await expect(page.getByTestId('mock-page')).toBeVisible();
    await captureAudit(page, testInfo, 'mock-exam', 'mock-page', 'light');
    await captureAudit(page, testInfo, 'mock-exam', 'mock-page', 'dark');

    await page.getByTestId('mock-option-a').click();
    await expect(page.getByTestId('mock-results')).toBeVisible();
    await captureAudit(page, testInfo, 'mock-results', 'mock-results', 'light');
    await captureAudit(page, testInfo, 'mock-results', 'mock-results', 'dark');

    await page.goto('/admin');
    await expect(page.getByTestId('admin-page')).toBeVisible();
  });
});
