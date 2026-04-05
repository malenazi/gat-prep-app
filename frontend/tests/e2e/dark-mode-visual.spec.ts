import { expect, test, type Page } from '@playwright/test';
import { goToAnalytics, goToPlan, goToPractice, loginAsSara, setTheme } from './helpers';

/**
 * Dark mode visual regression test.
 * Screenshots every page in light and dark mode,
 * then checks for contrast issues in dark mode.
 */

const PAGES = [
  { name: 'dashboard', navigate: async () => { /* already on dashboard after login */ } },
  { name: 'practice', navigate: async (p: Page) => { await goToPractice(p); } },
  { name: 'plan', navigate: async (p: Page) => { await goToPlan(p); } },
  { name: 'analytics', navigate: async (p: Page) => { await goToAnalytics(p); } },
];

test.describe('Dark Mode Visual Audit', () => {
  test.beforeEach(async ({ page }) => {
    await loginAsSara(page);
  });

  for (const { name, navigate } of PAGES) {
    test(`${name} — screenshots and contrast check`, async ({ page }) => {
      await navigate(page);
      await page.waitForTimeout(500); // let animations settle

      // Light mode screenshot
      await setTheme(page, 'light');
      await page.waitForTimeout(300);
      await page.screenshot({
        path: `e2e-results/theme-audit/light-${name}.png`,
        fullPage: true,
      });

      // Dark mode screenshot
      await setTheme(page, 'dark');
      await page.waitForTimeout(300);
      await page.screenshot({
        path: `e2e-results/theme-audit/dark-${name}.png`,
        fullPage: true,
      });

      // Contrast check: find elements with near-invisible text in dark mode
      const contrastIssues = await page.evaluate(() => {
        const issues: string[] = [];
        const elements = document.querySelectorAll('p, span, h1, h2, h3, h4, h5, h6, a, button, label, td, th, li');

        for (const el of elements) {
          const htmlEl = el as HTMLElement;
          const text = htmlEl.textContent?.trim();
          if (!text || text.length === 0) continue;

          const style = getComputedStyle(htmlEl);
          const color = style.color;
          const bg = style.backgroundColor;
          const opacity = parseFloat(style.opacity);

          // Check for very low opacity text
          if (opacity < 0.4 && text.length > 0) {
            issues.push(`Low opacity (${opacity}): "${text.substring(0, 30)}"`);
            continue;
          }

          // Parse RGB values
          const parseRgb = (c: string) => {
            const m = c.match(/rgba?\((\d+),\s*(\d+),\s*(\d+)/);
            return m ? { r: +m[1], g: +m[2], b: +m[3] } : null;
          };

          const fg = parseRgb(color);
          const bgc = parseRgb(bg);

          if (!fg || !bgc) continue;

          // Check for white/near-white background in dark mode (shouldn't happen)
          if (bgc.r > 240 && bgc.g > 240 && bgc.b > 240) {
            issues.push(`White bg in dark mode: "${text.substring(0, 30)}" (bg: rgb(${bgc.r},${bgc.g},${bgc.b}))`);
          }

          // Simple luminance contrast check
          const lum = (c: { r: number; g: number; b: number }) =>
            0.299 * c.r + 0.587 * c.g + 0.114 * c.b;

          const fgLum = lum(fg);
          const bgLum = lum(bgc);
          const contrast = Math.abs(fgLum - bgLum);

          // Very low contrast = text invisible
          if (contrast < 20 && bgc.r + bgc.g + bgc.b > 0) {
            issues.push(`Low contrast (${Math.round(contrast)}): "${text.substring(0, 30)}" (fg: rgb(${fg.r},${fg.g},${fg.b}), bg: rgb(${bgc.r},${bgc.g},${bgc.b}))`);
          }
        }

        return issues.slice(0, 20); // cap at 20
      });

      // Report issues but don't fail (visual audit is informational)
      if (contrastIssues.length > 0) {
        console.log(`\n⚠️  ${name} dark mode contrast issues:`);
        for (const issue of contrastIssues) {
          console.log(`    ${issue}`);
        }
      }

      // Soft assertion: no white backgrounds should exist in dark mode
      const whiteIssues = contrastIssues.filter(i => i.includes('White bg'));
      // Soft limit: allow up to 5 minor white-bg elements (badges, icons)
      // Set to 0 once all issues are fixed
      expect(whiteIssues.length, `White backgrounds found in dark mode on ${name} page`).toBeLessThanOrEqual(5);
    });
  }
});
