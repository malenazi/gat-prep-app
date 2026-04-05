import path from 'node:path';
import { randomBytes, randomUUID } from 'node:crypto';
import { fileURLToPath } from 'node:url';
import { defineConfig, devices } from '@playwright/test';

const currentDir = path.dirname(fileURLToPath(import.meta.url));
const frontendPort = Number.parseInt(process.env.E2E_FRONTEND_PORT ?? '34134', 10);
const backendPort = Number.parseInt(process.env.E2E_BACKEND_PORT ?? '38100', 10);
const externalBaseUrl = process.env.E2E_BASE_URL?.trim();
const isExternalRun = Boolean(externalBaseUrl);
const enableResponsiveAudit = process.env.PW_ENABLE_RESPONSIVE_AUDIT === '1';
const databaseUrl =
  process.env.E2E_DATABASE_URL ??
  `sqlite:///${path.resolve(currentDir, '../backend/gat_prep.e2e.db').replace(/\\/g, '/')}`;

function ensureEnv(name: string, valueFactory: () => string) {
  if (!process.env[name]?.trim()) {
    process.env[name] = valueFactory();
  }
  return process.env[name] as string;
}

function strongPassword(prefix: string) {
  return `${prefix}!${randomBytes(12).toString('base64url')}9aA`;
}

ensureEnv('E2E_NEW_STUDENT_NAME', () => 'QA New Learner');
ensureEnv('E2E_NEW_STUDENT_EMAIL', () => `qa-new-${randomUUID()}@example.com`);
ensureEnv('E2E_NEW_STUDENT_PASSWORD', () => strongPassword('NewLearner'));

ensureEnv('E2E_PROGRESS_NAME', () => 'QA Progress Learner');
ensureEnv('E2E_PROGRESS_EMAIL', () => `qa-progress-${randomUUID()}@example.com`);
ensureEnv('E2E_PROGRESS_PASSWORD', () => strongPassword('ProgressLearner'));

ensureEnv('E2E_ADMIN_NAME', () => 'QA Admin');
ensureEnv('E2E_ADMIN_EMAIL', () => `qa-admin-${randomUUID()}@example.com`);
ensureEnv('E2E_ADMIN_PASSWORD', () => strongPassword('AdminBootstrap'));

const inheritedEnv = Object.fromEntries(
  Object.entries(process.env).filter((entry): entry is [string, string] => typeof entry[1] === 'string'),
);

export default defineConfig({
  testDir: './tests/e2e',
  fullyParallel: false,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: 1,
  reporter: [['html', { open: 'never' }]],
  use: {
    baseURL: externalBaseUrl ?? `http://127.0.0.1:${frontendPort}`,
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
    video: 'on-first-retry',
    headless: true,
    viewport: { width: 1280, height: 720 },
    actionTimeout: 15000,
    navigationTimeout: 15000,
  },
  projects: [
    {
      name: 'chromium',
      testIgnore: /responsive-audit\.spec\.ts$/,
      use: { ...devices['Desktop Chrome'] },
    },
    ...(enableResponsiveAudit
      ? [
          {
            name: 'audit-chromium-390',
            testMatch: /responsive-audit\.spec\.ts$/,
            use: {
              ...devices['Desktop Chrome'],
              viewport: { width: 390, height: 844 },
              screen: { width: 390, height: 844 },
              isMobile: true,
              hasTouch: true,
            },
          },
          {
            name: 'audit-chromium-768',
            testMatch: /responsive-audit\.spec\.ts$/,
            use: {
              ...devices['Desktop Chrome'],
              viewport: { width: 768, height: 1024 },
              screen: { width: 768, height: 1024 },
            },
          },
          {
            name: 'audit-chromium-1024',
            testMatch: /responsive-audit\.spec\.ts$/,
            use: {
              ...devices['Desktop Chrome'],
              viewport: { width: 1024, height: 768 },
              screen: { width: 1024, height: 768 },
            },
          },
          {
            name: 'audit-chromium-1280',
            testMatch: /(responsive-audit|plan)\.spec\.ts$/,
            use: {
              ...devices['Desktop Chrome'],
              viewport: { width: 1280, height: 800 },
              screen: { width: 1280, height: 800 },
            },
          },
          {
            name: 'audit-chromium-1440',
            testMatch: /(responsive-audit|plan)\.spec\.ts$/,
            use: {
              ...devices['Desktop Chrome'],
              viewport: { width: 1440, height: 900 },
              screen: { width: 1440, height: 900 },
            },
          },
          {
            name: 'audit-chromium-1920',
            testMatch: /(responsive-audit|plan)\.spec\.ts$/,
            use: {
              ...devices['Desktop Chrome'],
              viewport: { width: 1920, height: 1080 },
              screen: { width: 1920, height: 1080 },
            },
          },
          {
            name: 'audit-chromium-2560',
            testMatch: /(responsive-audit|plan)\.spec\.ts$/,
            use: {
              ...devices['Desktop Chrome'],
              viewport: { width: 2560, height: 1440 },
              screen: { width: 2560, height: 1440 },
            },
          },
          {
            name: 'audit-webkit-390',
            testMatch: /responsive-audit\.spec\.ts$/,
            use: {
              browserName: 'webkit',
              viewport: { width: 390, height: 844 },
              screen: { width: 390, height: 844 },
              isMobile: true,
              hasTouch: true,
            },
          },
          {
            name: 'audit-webkit-1280',
            testMatch: /responsive-audit\.spec\.ts$/,
            use: {
              browserName: 'webkit',
              viewport: { width: 1280, height: 800 },
              screen: { width: 1280, height: 800 },
            },
          },
        ]
      : []),
  ],
  webServer: isExternalRun
    ? undefined
    : [
        {
          command: 'python run_test_server.py',
          cwd: '../backend',
          env: {
            ...inheritedEnv,
            E2E_BACKEND_PORT: String(backendPort),
            E2E_DATABASE_URL: databaseUrl,
          },
          url: `http://127.0.0.1:${backendPort}/health`,
          reuseExistingServer: false,
          timeout: 120000,
        },
        {
          command: `npm run dev -- --host 127.0.0.1 --port ${frontendPort} --strictPort`,
          cwd: '.',
          env: {
            ...inheritedEnv,
            E2E_API_URL: `http://127.0.0.1:${backendPort}`,
          },
          url: `http://127.0.0.1:${frontendPort}/`,
          reuseExistingServer: false,
          timeout: 120000,
        },
      ],
});
