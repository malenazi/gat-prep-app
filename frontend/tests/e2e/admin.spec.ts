import { expect, test } from '@playwright/test';
import { goToAdmin, loginAsAdmin } from './helpers';

test.describe('Admin Dashboard', () => {
  test.beforeEach(async ({ page }) => {
    await loginAsAdmin(page);
    await goToAdmin(page);
  });

  test('opens the admin overview and tab bar', async ({ page }) => {
    await expect(page.getByTestId('admin-page')).toBeVisible();
    await expect(page.getByTestId('admin-tab-overview')).toBeVisible();
    await expect(page.getByTestId('admin-tab-feedback')).toBeVisible();
    await expect(page.getByTestId('admin-tab-users')).toBeVisible();
    await expect(page.getByTestId('admin-tab-questions')).toBeVisible();
    await expect(page.getByTestId('admin-tab-mock')).toBeVisible();
  });

  test('switches between admin tabs', async ({ page }) => {
    await page.getByTestId('admin-tab-questions').click();
    await expect(page.getByText('Question Bank')).toBeVisible();

    await page.getByTestId('admin-tab-mock').click();
    await expect(page.getByText('Final Mock Exam')).toBeVisible();
  });

  test('shows live SVG and table previews in the question modal', async ({ page }) => {
    await page.getByTestId('admin-tab-questions').click();
    await page.getByRole('button', { name: 'Add Question' }).click();

    await page.getByLabel('Question Text *').fill('Preview visual question');
    await page.getByLabel('Figure SVG (optional)').fill(
      '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 80"><rect x="10" y="10" width="80" height="40" fill="#dbeafe" stroke="#0f172a" stroke-width="2"/></svg>',
    );
    await page.getByLabel('Table JSON (optional)').fill(
      '{"headers":["Column","Value"],"rows":[["A","12"],["B","18"]]}',
    );
    await page.getByRole('textbox', { name: 'Option A' }).fill('10');
    await page.getByRole('textbox', { name: 'Option B' }).fill('12');
    await page.getByRole('textbox', { name: 'Option C' }).fill('18');
    await page.getByRole('textbox', { name: 'Option D' }).fill('24');

    await expect(page.getByTestId('admin-question-preview-figure')).toBeVisible();
    await expect(page.getByTestId('admin-question-preview-table')).toBeVisible();
  });

  test('shows review controls for question activation', async ({ page }) => {
    await page.getByTestId('admin-tab-questions').click();
    await page.getByRole('button', { name: 'Add Question' }).click();

    await expect(page.getByText('Editorial Review')).toBeVisible();
    await expect(page.getByLabel('Status')).toBeVisible();
    await expect(page.getByLabel('Review Passes')).toBeVisible();
    await expect(page.getByLabel('Review Notes')).toBeVisible();
  });
});
