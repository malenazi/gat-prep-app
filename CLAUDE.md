# Qudra Academy — AI Coding Rules

## Tech Stack
- **Backend:** Python 3.12, FastAPI, SQLAlchemy, SQLite
- **Frontend:** React 19, TypeScript, Vite 7, Tailwind CSS 4
- **Testing:** pytest (backend), Playwright (frontend E2E)
- **Deployment:** Railway (Nixpacks), deploy via `railway up`

## Dark Mode (CRITICAL)
- Every `bg-white` MUST have `dark:bg-slate-900` (or `dark:bg-slate-950` for nested)
- Every `text-slate-800` MUST have `dark:text-slate-100`
- Every `text-slate-700` MUST have `dark:text-slate-200`
- Every `text-slate-600` MUST have `dark:text-slate-300`
- Every `text-slate-500` MUST have `dark:text-slate-400`
- Every `border-slate-200` MUST have `dark:border-slate-800`
- Every `border-slate-100` MUST have `dark:border-slate-800`
- Every `bg-slate-50` MUST have `dark:bg-slate-800` or `dark:bg-slate-900`
- Every `bg-slate-100` MUST have `dark:bg-slate-800`
- Colored backgrounds (amber-50, emerald-50, etc.) need `dark:*-950/30` variants
- Never use hardcoded hex colors in SVGs — use `currentColor` with Tailwind classes
- Recharts: never use hardcoded `fill`/`stroke` — use Tailwind arbitrary variant classes like `className="[&_text]:fill-slate-500 dark:[&_text]:fill-slate-400"`

## Components
- Never remove or rename `data-testid` attributes
- All new components must work in both light and dark mode
- Use `rounded-2xl` for cards (not `rounded-[2rem]`)
- Use existing CSS utility classes from `index.css` (card-hover, animate-*, stagger-*, etc.)

## Questions
- All question options must be unique (no duplicates within a question)
- All text must be in English
- Explanations must reference actual option values, not generic placeholders
- Correct option must be in {a, b, c, d}

## Code Style
- Use straight quotes only (never smart/curly quotes)
- No unused variables or imports
- Prefer editing existing files over creating new ones

## Before Finishing
- Run `cd frontend && npm run lint` — must pass clean
- Run `cd frontend && npm run build` — must succeed
- Run `npx playwright test --grep-invert "full-journey"` — 27/27 must pass
- For backend changes: `python -m pytest backend/tests/ -q`

## Deployment
- Deploy via `railway up` (auto-deploy from git may be disabled)
- After deploy: `python smoke_check.py --base-url https://gat-prep-prod-production.up.railway.app --skip-admin`
- Always hard-refresh browser (Ctrl+Shift+R) to verify new bundle
