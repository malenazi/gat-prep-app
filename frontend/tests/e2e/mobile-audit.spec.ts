import { expect, test } from '@playwright/test';
import { loginAsSara, goToPractice, goToSettings, setTheme } from './helpers';

test.use({
  viewport: { width: 390, height: 844 },
  isMobile: true,
  hasTouch: true,
});

test.describe('Mobile UX Audit', () => {
  test.beforeEach(async ({ page }) => {
    await loginAsSara(page);
  });

  test('dashboard mobile layout', async ({ page }) => {
    await expect(page.getByTestId('dashboard-page')).toBeVisible();
    // Mobile nav should be visible
    await expect(page.getByTestId('mobile-nav')).toBeVisible();
    // Desktop sidebar should be hidden
    await expect(page.getByTestId('app-sidebar')).not.toBeVisible();
    await page.screenshot({ path: 'e2e-results/mobile-dashboard.png', fullPage: true });
  });

  test('practice mobile layout', async ({ page }) => {
    await goToPractice(page);
    await expect(page.getByTestId('practice-question-card')).toBeVisible();
    // Check question code badge
    await expect(page.getByTestId('practice-question-code')).toBeVisible();
    await page.screenshot({ path: 'e2e-results/mobile-practice.png', fullPage: true });
  });

  test('settings mobile layout', async ({ page }) => {
    await goToSettings(page);
    await expect(page.getByTestId('settings-page')).toBeVisible();
    // Study prefs visible
    await expect(page.getByTestId('settings-study-prefs')).toBeVisible();
    await page.screenshot({ path: 'e2e-results/mobile-settings.png', fullPage: true });
    // Switch tabs
    await page.getByTestId('settings-tab-appearance').click();
    await page.screenshot({ path: 'e2e-results/mobile-settings-appearance.png', fullPage: true });
    await page.getByTestId('settings-tab-support').click();
    await page.screenshot({ path: 'e2e-results/mobile-settings-support.png', fullPage: true });
  });

  test('plan mobile layout', async ({ page }) => {
    await page.getByTestId('mobile-nav-plan').click();
    await expect(page.getByTestId('plan-page')).toBeVisible();
    await page.screenshot({ path: 'e2e-results/mobile-plan.png', fullPage: true });
  });

  test('analytics mobile layout', async ({ page }) => {
    await page.getByTestId('mobile-nav-analytics').click();
    await expect(page.getByTestId('analytics-page')).toBeVisible();
    await page.screenshot({ path: 'e2e-results/mobile-analytics.png', fullPage: true });
  });

  test('mobile dark mode all pages', async ({ page }) => {
    await setTheme(page, 'dark');
    await page.screenshot({ path: 'e2e-results/mobile-dashboard-dark.png', fullPage: true });

    await goToPractice(page);
    await page.screenshot({ path: 'e2e-results/mobile-practice-dark.png', fullPage: true });

    await goToSettings(page);
    await page.screenshot({ path: 'e2e-results/mobile-settings-dark.png', fullPage: true });
  });

  test('mobile nav has all items including settings', async ({ page }) => {
    const nav = page.getByTestId('mobile-nav');
    await expect(nav.getByText('Home')).toBeVisible();
    await expect(nav.getByText('Practice')).toBeVisible();
    await expect(nav.getByText('Plan')).toBeVisible();
    await expect(nav.getByText('Analytics')).toBeVisible();
    await expect(nav.getByText('Settings')).toBeVisible();
  });

  test('touch targets are large enough', async ({ page }) => {
    // Check mobile nav button sizes (should be at least 44x44 for touch)
    const navItems = page.getByTestId('mobile-nav').locator('a');
    const count = await navItems.count();
    for (let i = 0; i < count; i++) {
      const box = await navItems.nth(i).boundingBox();
      if (box) {
        expect(box.height).toBeGreaterThanOrEqual(40);
        expect(box.width).toBeGreaterThanOrEqual(40);
      }
    }
  });

  test('no horizontal overflow on mobile', async ({ page }) => {
    // Dashboard
    const overflow = await page.evaluate(() => {
      return Math.max(document.documentElement.scrollWidth - document.documentElement.clientWidth, 0);
    });
    expect(overflow).toBeLessThanOrEqual(1);

    // Practice
    await goToPractice(page);
    const practiceOverflow = await page.evaluate(() => {
      return Math.max(document.documentElement.scrollWidth - document.documentElement.clientWidth, 0);
    });
    expect(practiceOverflow).toBeLessThanOrEqual(1);

    // Settings
    await goToSettings(page);
    const settingsOverflow = await page.evaluate(() => {
      return Math.max(document.documentElement.scrollWidth - document.documentElement.clientWidth, 0);
    });
    expect(settingsOverflow).toBeLessThanOrEqual(1);
  });
});
