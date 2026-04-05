import { expect, test, type Page } from '@playwright/test';
import { expectNoHorizontalOverflow, goToPlan, loginAsSara } from './helpers';

async function expectVisiblePlanCardsStable(page: Page) {
  await expectNoHorizontalOverflow(page);

  const evaluation = await page.locator('[data-testid^="plan-day-"]').evaluateAll((elements) => {
    const visibleRects = elements
      .map((element) => {
        const rect = (element as HTMLElement).getBoundingClientRect();
        return {
          top: rect.top,
          left: rect.left,
          right: rect.right,
          bottom: rect.bottom,
          scrollHeight: (element as HTMLElement).scrollHeight,
          clientHeight: (element as HTMLElement).clientHeight,
          visible: rect.width > 0 && rect.height > 0 && rect.bottom > 0,
        };
      })
      .filter((rect) => rect.visible);

    let hasOverlap = false;
    for (let index = 0; index < visibleRects.length; index += 1) {
      for (let next = index + 1; next < visibleRects.length; next += 1) {
        const current = visibleRects[index];
        const candidate = visibleRects[next];
        const intersectsX = current.left < candidate.right - 1 && current.right > candidate.left + 1;
        const intersectsY = current.top < candidate.bottom - 1 && current.bottom > candidate.top + 1;
        if (intersectsX && intersectsY) {
          hasOverlap = true;
        }
      }
    }

    const hasClipping = visibleRects.some((rect) => rect.scrollHeight - rect.clientHeight > 2);
    return { hasOverlap, hasClipping };
  });

  expect(evaluation.hasOverlap).toBe(false);
  expect(evaluation.hasClipping).toBe(false);
}

test.describe('Study Plan', () => {
  test.beforeEach(async ({ page }) => {
    await loginAsSara(page);
    await goToPlan(page);
  });

  test('shows phase progress and selected day details', async ({ page }) => {
    await expect(page.getByTestId('plan-phase-progress')).toBeVisible();
    await expect(page.getByTestId('plan-detail')).toBeVisible();
    await expect(page.getByTestId('plan-page')).not.toContainText('30Q');
    await expect(page.getByTestId('plan-page')).toContainText(/practice questions|mock exam|rest day/i);
    await expect(page.getByTestId('plan-roadmap-grid')).toBeVisible();
    await expectVisiblePlanCardsStable(page);
  });

  test('updates the detail panel across the full 30-day roadmap without crowding', async ({ page }) => {
    for (let day = 1; day <= 30; day += 1) {
      const card = page.getByTestId(`plan-day-${day}`);
      await card.scrollIntoViewIfNeeded();
      await expect(card).toBeVisible();
      await card.click();
      await expect(page.getByTestId('plan-detail')).toContainText(`Day ${day}`);
      await expectVisiblePlanCardsStable(page);
    }
  });
});
