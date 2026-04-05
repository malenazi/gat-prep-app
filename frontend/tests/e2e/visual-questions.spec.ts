import { expect, test } from '@playwright/test';
import { goToPractice, loginAsAdmin, loginAsSara, loginAsStudent } from './helpers';

const svgQuestion = {
  id: 9001,
  skill_id: 'quant_geometry',
  question_type: 'geometry',
  difficulty: 0.5,
  text_ar: 'The diagram shows a rectangle. What is its area?',
  passage_ar: null,
  figure_svg:
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 140"><rect x="35" y="30" width="150" height="80" fill="#dbeafe" stroke="#0f172a" stroke-width="3"/><text x="110" y="20" text-anchor="middle" font-size="14" font-family="Arial">8 cm</text><text x="196" y="75" font-size="14" font-family="Arial">5 cm</text></svg>',
  table_ar: null,
  options: [
    { key: 'a', label: 'A', text_ar: '26 square cm' },
    { key: 'b', label: 'B', text_ar: '40 square cm' },
    { key: 'c', label: 'C', text_ar: '45 square cm' },
    { key: 'd', label: 'D', text_ar: '80 square cm' },
  ],
  paper_only: false,
};

const tableQuestion = {
  id: 9002,
  skill_id: 'quant_statistics',
  question_type: 'statistics',
  difficulty: 0.4,
  text_ar: 'Use the table to find the arithmetic mean.',
  passage_ar: null,
  figure_svg: null,
  table_ar: {
    headers: ['Student', 'Score'],
    rows: [['A', '70'], ['B', '80'], ['C', '90'], ['D', '60']],
  },
  options: [
    { key: 'a', label: 'A', text_ar: '70' },
    { key: 'b', label: 'B', text_ar: '75' },
    { key: 'c', label: 'C', text_ar: '80' },
    { key: 'd', label: 'D', text_ar: '85' },
  ],
  paper_only: false,
};

test.describe('Visual Questions', () => {
  test('practice renders an SVG question and submits normally', async ({ page }) => {
    await loginAsSara(page);
    await page.route('**/api/practice/next', async (route) => {
      await route.fulfill({
        json: {
          done: false,
          question: svgQuestion,
          adaptive: {
            skill_name: 'Geometry',
            skill_section: 'quant',
            difficulty_score: 55,
            difficulty_label: 'Target',
            skill_mastery: 0,
            challenge_band: 'Calibrating',
            selection_reason: 'Chosen to establish your starting level in Geometry.',
          },
          assistment: {
            hints_available: true,
            hints: [
              { index: 1, title: 'Hint 1: What to notice', text_ar: 'Notice which dimensions the figure gives you.' },
              { index: 2, title: 'Hint 2: How to set it up', text_ar: 'Choose the formula that matches area, then substitute the side lengths.' },
            ],
          },
        },
      });
    });
    await page.route('**/api/practice/answer', async (route) => {
      await route.fulfill({
        json: {
          is_correct: true,
          correct_option: 'b',
          explanation_ar: 'Area = 8 x 5 = 40.',
          solution_steps_ar: ['Read the side lengths.', 'Multiply 8 by 5.'],
          xp_earned: 10,
        },
      });
    });

    await goToPractice(page);
    await expect(page.getByTestId('practice-challenge-chip')).toContainText('Calibrating');
    await expect(page.getByTestId('practice-skill-mastery')).toContainText('Starting level');
    await page.getByTestId('practice-hint-reveal').click();
    await expect(page.getByTestId('practice-hint-1')).toBeVisible();
    await expect(page.getByTestId('practice-question-figure')).toBeVisible();
    await page.getByTestId('practice-option-b').click();
    await expect(page.getByTestId('practice-feedback')).toBeVisible();
  });

  test('diagnostic renders a table question without layout breakage', async ({ page }) => {
    await loginAsStudent(page);
    await page.route('**/api/diagnostic/start', async (route) => {
      await route.fulfill({ json: { message: 'Start diagnostic test', total_questions: 9 } });
    });
    let diagnosticNextCallCount = 0;
    await page.route('**/api/diagnostic/next', async (route) => {
      diagnosticNextCallCount += 1;
      await route.fulfill({
        json: {
          done: false,
          progress: diagnosticNextCallCount - 1,
          total: 9,
          question: {
            ...tableQuestion,
            id: tableQuestion.id + diagnosticNextCallCount,
            text_ar: diagnosticNextCallCount === 1
              ? tableQuestion.text_ar
              : `Question ${diagnosticNextCallCount}: keep moving through the diagnostic`,
          },
        },
      });
    });
    await page.route('**/api/diagnostic/answer', async (route) => {
      await route.fulfill({
        json: {
          is_correct: true,
          correct_option: 'b',
          explanation_ar: 'This should not appear during the diagnostic session.',
          solution_steps_ar: ['Step 1', 'Step 2'],
        },
      });
    });

    await page.getByTestId('diagnostic-start').click();
    await expect(page.getByTestId('diagnostic-question-table')).toBeVisible();
    await expect(page.getByTestId('diagnostic-question-text')).toContainText('arithmetic mean');
    await expect(page.getByTestId('diagnostic-testing-note')).toBeVisible();

    await page.getByTestId('diagnostic-option-b').click();
    await expect(page.getByTestId('diagnostic-progress')).toContainText('Question 2 of 9');
    await expect(page.getByText('Quick diagnostic review')).toHaveCount(0);
    await expect(page.getByText('Correct answer:')).toHaveCount(0);
  });

  test('mock exam renders a visual question in preview mode', async ({ page }) => {
    await loginAsAdmin(page);
    await page.route('**/api/mock/start?preview=true', async (route) => {
      await route.fulfill({
        json: {
          attempt_id: 101,
          attempt_number: 1,
          total_questions: 1,
          verbal_count: 1,
          quant_count: 0,
          verbal_minutes: 35,
          quant_minutes: 35,
          question_ids: [svgQuestion.id],
        },
      });
    });
    await page.route(`**/api/mock/question/${svgQuestion.id}`, async (route) => {
      await route.fulfill({ json: svgQuestion });
    });
    await page.route('**/api/mock/answer', async (route) => {
      await route.fulfill({ json: { is_correct: true } });
    });
    await page.route('**/api/mock/complete', async (route) => {
      await route.fulfill({
        json: {
          attempt_id: 101,
          attempt_number: 1,
          score: 88,
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
    await page.route('**/api/mock/attempts/101', async (route) => {
      await route.fulfill({
        json: {
          attempt_number: 1,
          score: 88,
          total: 1,
          correct: 1,
          verbal_correct: 1,
          verbal_total: 1,
          quant_correct: 0,
          quant_total: 0,
          completed_at: new Date().toISOString(),
          skill_breakdown: [],
          questions: [
            {
              question_id: svgQuestion.id,
              text_ar: svgQuestion.text_ar,
              passage_ar: svgQuestion.passage_ar,
              content_format: 'plain',
              comparison_columns: null,
              figure_svg: svgQuestion.figure_svg,
              figure_alt: 'Rectangle diagram',
              table_ar: null,
              table_caption: null,
              options: svgQuestion.options.map((option) => ({ key: option.key, text_ar: option.text_ar })),
              selected_option: 'b',
              correct_option: 'b',
              is_correct: true,
              time_spent_seconds: 12,
              explanation_ar: 'Area = 8 x 5 = 40.',
              solution_steps_ar: ['Read the side lengths.', 'Multiply 8 by 5.'],
              skill_id: svgQuestion.skill_id,
              skill_name_ar: 'Geometry',
              section: 'quantitative',
            },
          ],
        },
      });
    });

    await page.goto('/mock?preview=true');
    await page.getByTestId('mock-start').click();
    await expect(page.getByTestId('mock-question-figure')).toBeVisible();
    await expect(page.getByText('Correct answer:')).toHaveCount(0);
    await page.getByTestId('mock-option-b').click();
    await expect(page.getByTestId('mock-results')).toBeVisible();
    await expect(page.getByTestId('mock-review-attempt')).toBeVisible();
    await page.getByTestId('mock-review-attempt').click();
    await expect(page.getByText('Question Review (1)')).toBeVisible();
  });
});
