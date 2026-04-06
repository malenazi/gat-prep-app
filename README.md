# Qudra Academy

English-language GAT prep platform with adaptive 30-day study plan.

- **Backend:** Python 3.12, FastAPI, SQLAlchemy
- **Frontend:** React 19, TypeScript, Vite 7, Tailwind CSS 4
- **Database:** PostgreSQL (Railway) / SQLite (local dev)
- **Question Bank:** 1,503 questions across 9 skills
- **Deployment:** Railway (Railpack), ~90 second deploys

**Live:** https://gat-prep-prod-production.up.railway.app

## Quick Start

Backend:
```bash
pip install -r requirements.txt
cd backend && python -m uvicorn main:app --reload --port 8000
```

Frontend:
```bash
cd frontend && npm install && npm run dev
```

The frontend proxies `/api` to `http://localhost:8000` in development.

## Question Bank

| Skill | Count |
|-------|-------|
| Quant: Algebra, Arithmetic, Geometry, Statistics | 167 each |
| Verbal: Reading, Analogy, Completion, Error, Oddword | 167 each |
| **Total** | **1,503** |

Organized by difficulty (0.2-0.8) and stage (diagnostic, foundation, building, peak, mock).

## Testing

```bash
# Backend unit tests
python -m pytest backend/tests/ -q

# Frontend lint + build
cd frontend && npm run lint && npm run build

# Quality audits
npm run dark:audit        # Dark mode coverage (15 rules, strict)
npm run svg:audit         # Hardcoded color check

# E2E tests (28 tests, auto-starts servers)
npx playwright test

# Visual regression (dark mode contrast)
npx playwright test tests/e2e/dark-mode-visual.spec.ts
```

## Deployment

```bash
# 1. Build frontend locally
cd frontend && npm run build

# 2. Deploy (~90 seconds with Railpack)
railway up

# 3. Verify
python smoke_check.py --base-url https://gat-prep-prod-production.up.railway.app --skip-admin
```

## Admin

```bash
# Bootstrap admin (first time only — set in Railway env vars)
BOOTSTRAP_ADMIN_EMAIL=admin@qudra.academy
BOOTSTRAP_ADMIN_PASSWORD='...'
```

Admin panel: https://gat-prep-prod-production.up.railway.app/admin

## Project Structure

```
backend/
  main.py              # FastAPI app — all API endpoints
  models.py            # SQLAlchemy models (User, Question, StudyPlan, etc.)
  database.py          # DB connection (PostgreSQL/SQLite auto-detect)
  adaptive.py          # IRT-based adaptive question selection
  auth_utils.py        # JWT auth, password hashing, rate limiting
  seed.py              # Question bank sync on startup
  questions/           # 9 skill modules (167 questions each)
  tests/               # pytest suite (35+ tests)
frontend/
  dist/                # Pre-built static files (committed for fast deploys)
  src/
    pages/             # Dashboard, Practice, Plan, Analytics, Admin, MockExam, Diagnostic
    components/        # UI components, question rendering, auth form
    hooks/useAuth.tsx  # Auth context provider
    lib/api.ts         # API client
  scripts/             # Quality audit tools (dark mode, SVG colors)
  tests/e2e/           # Playwright E2E tests (15 spec files, 28+ tests)
```

## Architecture

```
Browser → Railway (HTTPS)
  ├── Static files (frontend/dist → backend/static)
  ├── /api/* → FastAPI (Python)
  └── PostgreSQL (persistent user data)
```

## Quality Tools

| Tool | Command | What it checks |
|------|---------|---------------|
| Dark mode audit | `npm run dark:audit` | 15 rules — bg, text, border dark variants |
| SVG color audit | `npm run svg:audit` | Hardcoded hex colors in TSX |
| Visual regression | `npx playwright test dark-mode-visual` | Screenshots + contrast check |
| Question quality | `pytest tests/test_question_quality.py` | Duplicates, empty fields, SVG fills |
| Pre-commit hooks | Husky + lint-staged | ESLint fix + Prettier on commit |
