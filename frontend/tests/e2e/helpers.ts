import { expect, type Page } from '@playwright/test';

function requiredEnv(name: string) {
  const value = process.env[name]?.trim();
  if (!value) {
    throw new Error(`Missing required test environment variable: ${name}`);
  }
  return value;
}

export const TEST_USERS = {
  get newStudent() {
    return {
      email: requiredEnv('E2E_NEW_STUDENT_EMAIL'),
      password: requiredEnv('E2E_NEW_STUDENT_PASSWORD'),
      name: requiredEnv('E2E_NEW_STUDENT_NAME'),
    };
  },
  get progress() {
    return {
      email: requiredEnv('E2E_PROGRESS_EMAIL'),
      password: requiredEnv('E2E_PROGRESS_PASSWORD'),
      name: requiredEnv('E2E_PROGRESS_NAME'),
    };
  },
  get admin() {
    return {
      email: requiredEnv('E2E_ADMIN_EMAIL'),
      password: requiredEnv('E2E_ADMIN_PASSWORD'),
      name: requiredEnv('E2E_ADMIN_NAME'),
    };
  },
};

export async function visitLanding(page: Page) {
  await page.goto('/');
  await expect(page.getByTestId('landing-page')).toBeVisible();
}

export async function openAuth(page: Page) {
  await visitLanding(page);
  await page.getByTestId('landing-start').click();
  await expect(page.getByTestId('auth-page')).toBeVisible();
}

export async function loginWithCredentials(page: Page, email: string, password: string) {
  await openAuth(page);
  await page.getByTestId('auth-email').fill(email);
  await page.getByTestId('auth-password').fill(password);
  await page.getByTestId('auth-submit').click();
}

export async function registerFreshLearner(
  page: Page,
  {
    email = `qa-${Date.now()}@example.com`,
    password = 'LearnerPass123!',
    name = 'QA Learner',
  }: { email?: string; password?: string; name?: string } = {},
) {
  await openAuth(page);
  await page.getByTestId('auth-create-account-shortcut').click();
  await page.getByTestId('auth-name').fill(name);
  await page.getByTestId('auth-email').fill(email);
  await page.getByTestId('auth-password').fill(password);
  await page.getByTestId('auth-submit').click();
  return { email, password, name };
}

export async function loginAsStudent(page: Page) {
  await loginWithCredentials(page, TEST_USERS.newStudent.email, TEST_USERS.newStudent.password);
  await expect(page.getByTestId('diagnostic-page')).toBeVisible();
}

export async function loginAsSara(page: Page) {
  await loginWithCredentials(page, TEST_USERS.progress.email, TEST_USERS.progress.password);
  await expect(page.getByTestId('dashboard-page')).toBeVisible();
}

export async function loginAsAdmin(page: Page) {
  await loginWithCredentials(page, TEST_USERS.admin.email, TEST_USERS.admin.password);
  await page.waitForURL(/\/admin$/, { timeout: 15000 });
  await expect(page.getByTestId('admin-page')).toBeVisible({ timeout: 15000 });
}

export async function completeDiagnostic(page: Page, option: 'a' | 'b' | 'c' | 'd' = 'a') {
  await expect(page.getByTestId('diagnostic-page')).toBeVisible();
  await page.getByTestId('diagnostic-start').click();

  for (let index = 0; index < 9; index += 1) {
    await expect(page.getByTestId('diagnostic-question-card')).toBeVisible();
    const progressBefore = await page.getByTestId('diagnostic-progress').textContent();
    await page.getByTestId(`diagnostic-option-${option}`).click();

    if (index < 8) {
      await expect(page.getByTestId('diagnostic-progress')).not.toHaveText(progressBefore ?? '', { timeout: 10000 });
    }
  }

  await expect(page.getByTestId('diagnostic-results')).toBeVisible();
}

export async function logout(page: Page) {
  const desktopLogout = page.getByTestId('logout-desktop');
  if (await desktopLogout.isVisible().catch(() => false)) {
    await desktopLogout.click();
  } else {
    const mobileLogout = page.getByTestId('logout-mobile');
    if (!(await mobileLogout.isVisible().catch(() => false))) {
      await clickResponsiveNav(page, 'nav-home', 'mobile-nav-home');
      await expect(page.getByTestId('dashboard-page')).toBeVisible();
    }
    await page.getByTestId('logout-mobile').click();
  }
}

export async function getStoredToken(page: Page) {
  return page.evaluate(() => localStorage.getItem('gat_token'));
}

async function clickResponsiveNav(page: Page, desktopTestId: string, mobileTestId: string) {
  const desktopTarget = page.getByTestId(desktopTestId);
  if (await desktopTarget.isVisible().catch(() => false)) {
    await desktopTarget.click();
    return;
  }

  await page.getByTestId(mobileTestId).click();
}

export async function goToPractice(page: Page) {
  await clickResponsiveNav(page, 'nav-practice', 'mobile-nav-practice');
  await expect(page).toHaveURL(/\/practice$/);
  await expect(page.getByTestId('practice-page')).toBeVisible();
  await expect(page.getByTestId('practice-question-card')).toBeVisible();
}

export async function goToPlan(page: Page) {
  await clickResponsiveNav(page, 'nav-plan', 'mobile-nav-plan');
  await expect(page).toHaveURL(/\/plan$/);
  await expect(page.getByTestId('plan-page')).toBeVisible();
}

export async function goToAnalytics(page: Page) {
  await clickResponsiveNav(page, 'nav-analytics', 'mobile-nav-analytics');
  await expect(page).toHaveURL(/\/analytics$/);
  await expect(page.getByTestId('analytics-page')).toBeVisible();
}

export async function goToAdmin(page: Page) {
  const adminPage = page.getByTestId('admin-page');
  if (await adminPage.isVisible().catch(() => false)) {
    await expect(adminPage).toBeVisible();
    return;
  }

  await clickResponsiveNav(page, 'nav-admin', 'mobile-nav-admin');
  await expect(page).toHaveURL(/\/admin$/);
  await expect(page.getByTestId('admin-page')).toBeVisible();
}

export async function goToSettings(page: Page) {
  await clickResponsiveNav(page, 'nav-settings', 'mobile-nav-settings');
  await expect(page).toHaveURL(/\/settings$/);
  await expect(page.getByTestId('settings-page')).toBeVisible();
}

export async function goToDashboard(page: Page) {
  await clickResponsiveNav(page, 'nav-home', 'mobile-nav-home');
  await expect(page).toHaveURL(/\/$/);
  await expect(page.getByTestId('dashboard-page')).toBeVisible();
}

export async function setTheme(page: Page, theme: 'light' | 'dark') {
  const button = page.getByTestId('theme-toggle-button');
  await expect(button).toBeVisible();
  const pressed = await button.getAttribute('aria-pressed');
  const isDark = pressed === 'true';

  if ((theme === 'dark' && !isDark) || (theme === 'light' && isDark)) {
    await button.click();
  }
}

export async function expectNoHorizontalOverflow(page: Page) {
  const overflow = await page.evaluate(() => {
    const root = document.documentElement;
    return Math.max(root.scrollWidth - root.clientWidth, 0);
  });

  expect(overflow).toBeLessThanOrEqual(1);
}

export async function answerPracticeQuestion(page: Page, option: 'a' | 'b' | 'c' | 'd' = 'a') {
  const questionBefore = await page.getByTestId('practice-question-text').textContent();
  await page.getByTestId(`practice-option-${option}`).click();
  await expect(page.getByTestId('practice-feedback')).toBeVisible();
  return questionBefore;
}
