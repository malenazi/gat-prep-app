import { expect, request as playwrightRequest, test, type APIRequestContext, type Page } from '@playwright/test';
import { completeDiagnostic, getStoredToken, loginWithCredentials, logout, registerFreshLearner } from './helpers';

interface TodayPlan {
  day: number;
  target_questions: number;
  completed_questions: number;
  is_mock_day: boolean;
  is_rest_day: boolean;
  remaining: number;
}

interface ApiUser {
  current_day: number;
}

interface StudyPlanDay {
  day: number;
  completed: boolean;
  is_mock_day: boolean;
  is_rest_day: boolean;
}

interface MockStartResponse {
  attempt_id: number;
  question_ids: number[];
}

function resolveApiBaseUrl() {
  const explicitApiUrl = process.env.E2E_API_URL?.trim();
  if (explicitApiUrl) {
    return explicitApiUrl.replace(/\/$/, '');
  }

  const externalBaseUrl = process.env.E2E_BASE_URL?.trim();
  if (externalBaseUrl) {
    return new URL('/', externalBaseUrl).toString().replace(/\/$/, '');
  }

  const backendPort = process.env.E2E_BACKEND_PORT ?? '38100';
  return `http://127.0.0.1:${backendPort}`;
}

async function apiJson<T>(api: APIRequestContext, path: string, options: Parameters<APIRequestContext['fetch']>[1] = {}) {
  const response = await api.fetch(`/api${path}`, {
    ...options,
    failOnStatusCode: false,
  });

  if (!response.ok()) {
    throw new Error(`${path} failed with ${response.status()}: ${await response.text()}`);
  }

  return response.json() as Promise<T>;
}

async function getToday(api: APIRequestContext) {
  return apiJson<TodayPlan>(api, '/study-plan/today');
}

async function getMe(api: APIRequestContext) {
  return apiJson<ApiUser>(api, '/me');
}

async function completePracticeGoalViaUi(page: Page, totalQuestions: number) {
  for (let index = 0; index < totalQuestions; index += 1) {
    await expect(page.getByTestId('practice-question-card')).toBeVisible();
    await page.getByTestId('practice-option-a').click();
    await expect(page.getByTestId('practice-feedback')).toBeVisible();

    if (index < totalQuestions - 1) {
      await page.getByTestId('practice-next').click();
    }
  }

  await page.getByTestId('practice-end').click();
  await expect(page.getByTestId('practice-exit-confirm')).toBeVisible();
  await page.getByTestId('practice-exit-end').click();
  await expect(page.getByTestId('dashboard-page')).toBeVisible();
}

async function completeNormalDay(api: APIRequestContext) {
  const today = await getToday(api);
  const remainingQuestions = Math.max(0, today.target_questions - today.completed_questions);

  for (let index = 0; index < remainingQuestions; index += 1) {
    const next = await apiJson<{ done: boolean; question?: { id: number } }>(api, '/practice/next');
    expect(next.done).toBe(false);
    expect(next.question).toBeTruthy();

    await apiJson(api, '/practice/answer', {
      method: 'POST',
      data: {
        question_id: next.question!.id,
        selected_option: 'a',
        time_spent_seconds: 1,
      },
    });
  }
}

async function completeMockDay(api: APIRequestContext) {
  const start = await apiJson<MockStartResponse>(api, '/mock/start', { method: 'POST' });

  for (const questionId of start.question_ids) {
    await apiJson(api, '/mock/answer', {
      method: 'POST',
      data: {
        question_id: questionId,
        selected_option: 'a',
        time_spent_seconds: 1,
        attempt_id: start.attempt_id,
      },
    });
  }

  await apiJson(api, '/mock/complete', {
    method: 'POST',
    data: { attempt_id: start.attempt_id },
  });
}

test.describe('New User Full Journey', () => {
  test('registers, re-logs in, and completes the full 30-day course', async ({ page }) => {
    test.setTimeout(10 * 60 * 1000);

    const learner = await registerFreshLearner(page);
    await expect(page.getByTestId('diagnostic-page')).toBeVisible();

    await completeDiagnostic(page);
    await page.getByTestId('diagnostic-finish').click();
    await expect(page.getByTestId('dashboard-page')).toBeVisible();
    await expect(page.getByTestId('topbar-day')).toContainText('Day 1');

    const token = await getStoredToken(page);
    expect(token).toBeTruthy();

    const api = await playwrightRequest.newContext({
      baseURL: resolveApiBaseUrl(),
      extraHTTPHeaders: {
        Authorization: `Bearer ${token}`,
        'Content-Type': 'application/json',
      },
    });

    try {
      const earlyAdvance = await api.fetch('/api/advance-day', {
        method: 'POST',
        failOnStatusCode: false,
      });
      expect(earlyAdvance.status()).toBe(400);
      await expect(earlyAdvance.text()).resolves.toContain("Complete today's questions first");

      const dayOnePlan = await getToday(api);
      expect(dayOnePlan.day).toBe(1);
      expect(dayOnePlan.is_mock_day).toBe(false);
      expect(dayOnePlan.is_rest_day).toBe(false);

      await logout(page);
      await expect(page.getByTestId('auth-page')).toBeVisible();

      await loginWithCredentials(page, learner.email, learner.password);
      await expect(page.getByTestId('dashboard-page')).toBeVisible();
      await expect(page.getByTestId('topbar-day')).toContainText('Day 1');

      await page.getByTestId('dashboard-session-link').click();
      await expect(page).toHaveURL(/\/practice$/);
      await completePracticeGoalViaUi(page, dayOnePlan.target_questions - dayOnePlan.completed_questions);

      await expect(page.getByTestId('dashboard-session-complete')).toBeVisible();
      const laterButton = page.getByRole('button', { name: 'Later' });
      if (await laterButton.isVisible().catch(() => false)) {
        await laterButton.click();
      }
      await page.getByTestId('dashboard-advance-day').click();
      await expect(page.getByTestId('topbar-day')).toContainText('Day 2');

      let firstMockRouteVerified = false;

      while (true) {
        const me = await getMe(api);
        const today = await getToday(api);

        if (me.current_day === 30) {
          expect(today.is_rest_day).toBe(true);
          expect(today.completed_questions).toBe(today.target_questions);
          break;
        }

        if (today.is_mock_day) {
          if (!firstMockRouteVerified) {
            await page.goto('/');
            await expect(page.getByTestId('dashboard-page')).toBeVisible();
            await page.getByTestId('dashboard-session-link').click();
            await expect(page).toHaveURL(/\/mock$/);
            await expect(page.getByTestId('mock-page')).toBeVisible();
            firstMockRouteVerified = true;
          }

          await completeMockDay(api);
        } else {
          await completeNormalDay(api);
        }

        const completedToday = await getToday(api);
        expect(completedToday.completed_questions).toBeGreaterThanOrEqual(completedToday.target_questions);
        expect(completedToday.remaining).toBe(0);

        const advanceResponse = await api.fetch('/api/advance-day', {
          method: 'POST',
          failOnStatusCode: false,
        });
        expect(advanceResponse.ok()).toBe(true);
      }

      const finalPlan = await apiJson<StudyPlanDay[]>(api, '/study-plan');
      expect(finalPlan).toHaveLength(30);
      expect(finalPlan.every((day) => day.completed)).toBe(true);
      expect(finalPlan.filter((day) => day.is_mock_day)).toHaveLength(4);
      expect(finalPlan.find((day) => day.day === 30)?.is_rest_day).toBe(true);

      await page.goto('/');
      await expect(page.getByTestId('dashboard-page')).toBeVisible();
      await expect(page.getByTestId('topbar-day')).toContainText('Day 30');
      await page.getByTestId('nav-plan').click();
      await expect(page.getByTestId('plan-page')).toBeVisible();
      for (let day = 1; day <= 30; day += 1) {
        const card = page.getByTestId(`plan-day-${day}`);
        await card.scrollIntoViewIfNeeded();
        await expect(card).toBeVisible();
        await card.click();
        await expect(page.getByTestId('plan-detail')).toContainText(`Day ${day}`);
      }
    } finally {
      await api.dispose();
    }
  });
});
