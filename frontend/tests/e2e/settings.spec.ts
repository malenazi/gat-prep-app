import { expect, test } from '@playwright/test';
import { loginAsSara, goToSettings, setTheme } from './helpers';

test.describe('Settings Page', () => {
  test.beforeEach(async ({ page }) => {
    await loginAsSara(page);
  });

  test('navigates to settings and shows account tab by default', async ({ page }) => {
    await goToSettings(page);
    await expect(page.getByTestId('settings-tab-account')).toBeVisible();
    await expect(page.getByTestId('settings-tab-appearance')).toBeVisible();
    await expect(page.getByTestId('settings-tab-support')).toBeVisible();
    // Account tab is active by default — profile info visible
    await expect(page.getByText('Profile Information')).toBeVisible();
  });

  test('switches between tabs', async ({ page }) => {
    await goToSettings(page);

    // Switch to Appearance
    await page.getByTestId('settings-tab-appearance').click();
    await expect(page.getByText('Theme')).toBeVisible();
    await expect(page.getByText('Light')).toBeVisible();
    await expect(page.getByText('Dark')).toBeVisible();

    // Switch to Support
    await page.getByTestId('settings-tab-support').click();
    await expect(page.getByText('Help & Resources')).toBeVisible();
    await expect(page.getByText('Contact Support')).toBeVisible();
    await expect(page.getByText('Report a Problem')).toBeVisible();

    // Switch back to Account
    await page.getByTestId('settings-tab-account').click();
    await expect(page.getByText('Profile Information')).toBeVisible();
  });

  test('shows user profile information on account tab', async ({ page }) => {
    await goToSettings(page);
    await expect(page.getByText('Email', { exact: true }).first()).toBeVisible();
    await expect(page.getByText('Password & Security')).toBeVisible();
    await expect(page.getByRole('button', { name: 'Reset Password via Email' })).toBeVisible();
  });

  test('appearance tab theme buttons are visible', async ({ page }) => {
    await goToSettings(page);
    await page.getByTestId('settings-tab-appearance').click();
    const settingsPage = page.getByTestId('settings-page');
    const lightBtn = settingsPage.getByRole('button', { name: 'Light' });
    const darkBtn = settingsPage.getByRole('button', { name: 'Dark' });
    await expect(lightBtn).toBeVisible();
    await expect(darkBtn).toBeVisible();
  });

  test('support tab opens feedback form', async ({ page }) => {
    await goToSettings(page);
    await page.getByTestId('settings-tab-support').click();
    await page.getByText('Contact Support').click();
    await expect(page.getByText('Send us a message')).toBeVisible();
    await expect(page.getByPlaceholder('Describe your issue or suggestion...')).toBeVisible();
  });

  test('shows study preferences with time presets', async ({ page }) => {
    await goToSettings(page);
    const prefs = page.getByTestId('settings-study-prefs');
    await expect(prefs).toBeVisible();
    await expect(prefs.getByText('Study Preferences')).toBeVisible();
    // Check preset buttons exist
    await expect(page.getByTestId('study-preset-15')).toBeVisible();
    await expect(page.getByTestId('study-preset-30')).toBeVisible();
    await expect(page.getByTestId('study-preset-60')).toBeVisible();
    await expect(page.getByTestId('study-preset-120')).toBeVisible();
    // Check estimated load is shown
    await expect(prefs.getByText(/questions \/ day/)).toBeVisible();
  });

  test('selecting a study preset shows save button and updates estimate', async ({ page }) => {
    await goToSettings(page);
    // Click a different preset
    await page.getByTestId('study-preset-30').click();
    // Save button should appear
    const saveBtn = page.getByTestId('study-save-btn');
    await expect(saveBtn).toBeVisible();
    // Estimate should show ~10 questions (max(10, 30/4) = 10)
    await expect(page.getByTestId('settings-study-prefs').getByText('~10 questions / day')).toBeVisible();
  });

  test('saving study preferences calls API and shows success', async ({ page }) => {
    await goToSettings(page);
    // Pick 15 min first (unlikely to be current), then save
    await page.getByTestId('study-preset-15').click();
    const saveBtn = page.getByTestId('study-save-btn');
    // If save button not visible, the user was already at 15 — pick 30 instead
    if (!(await saveBtn.isVisible().catch(() => false))) {
      await page.getByTestId('study-preset-30').click();
    }
    await expect(saveBtn).toBeVisible({ timeout: 5000 });
    await saveBtn.click();
    await expect(page.getByText('Study plan updated!')).toBeVisible({ timeout: 10000 });
  });

  test('settings page renders correctly in dark mode', async ({ page }) => {
    await setTheme(page, 'dark');
    await goToSettings(page);

    // Take screenshot for visual verification
    await page.screenshot({ path: 'e2e-results/settings-dark.png', fullPage: true });

    // Check all 3 tabs in dark mode
    await page.getByTestId('settings-tab-appearance').click();
    await page.screenshot({ path: 'e2e-results/settings-appearance-dark.png', fullPage: true });

    await page.getByTestId('settings-tab-support').click();
    await page.getByText('Contact Support').click();
    await page.screenshot({ path: 'e2e-results/settings-support-dark.png', fullPage: true });
  });

  test('settings page renders correctly in light mode', async ({ page }) => {
    await setTheme(page, 'light');
    await goToSettings(page);

    await page.screenshot({ path: 'e2e-results/settings-light.png', fullPage: true });

    await page.getByTestId('settings-tab-appearance').click();
    await page.screenshot({ path: 'e2e-results/settings-appearance-light.png', fullPage: true });

    await page.getByTestId('settings-tab-support').click();
    await page.getByText('Contact Support').click();
    await page.screenshot({ path: 'e2e-results/settings-support-light.png', fullPage: true });
  });
});
