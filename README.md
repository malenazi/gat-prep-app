# Qudra Academy

English-language GAT prep platform with adaptive 30-day study plan.

- **Backend:** FastAPI + SQLAlchemy (Python)
- **Frontend:** React 19 + TypeScript + Vite
- **Question Bank:** 1,503 questions across 9 skills
- **Features:** Adaptive practice, diagnostic assessment, mock exams, analytics, admin dashboard
- **Deployment:** Railway (Nixpacks)

## Quick Start

```bash
bash start.sh
```

## Manual Setup

Backend:

```bash
pip install -r backend/requirements.txt
cd backend
python -m uvicorn main:app --reload --port 8000
```

Frontend:

```bash
cd frontend
npm install
npm run dev
```

The frontend proxies `/api` to `http://localhost:8000` in development.

## Question Bank

| Skill | Questions |
|-------|-----------|
| Quant Algebra | 167 |
| Quant Arithmetic | 167 |
| Quant Geometry | 167 |
| Quant Statistics | 167 |
| Verbal Analogy | 167 |
| Verbal Completion | 167 |
| Verbal Error | 167 |
| Verbal Oddword | 167 |
| Verbal Reading | 167 |
| **Total** | **1,503** |

Questions are organized by difficulty (0.2-0.8) and stage (diagnostic, foundation, building, peak, mock).

## Bootstrap Admin

```bash
export BOOTSTRAP_ADMIN_EMAIL=admin@qudra.academy
export BOOTSTRAP_ADMIN_PASSWORD='replace-with-a-strong-password'
python backend/bootstrap_admin.py
```

Admin panel: https://gat-prep-prod-production.up.railway.app/admin

## Testing

### Backend Tests

```bash
# All unit tests
python -m pytest backend/tests/ -q

# API integration tests (requires running server)
cd backend && python run_test_server.py &
API_BASE_URL=http://127.0.0.1:8000/api python -m pytest backend/tests/test_api_questions.py backend/tests/test_api_auth_reset.py -q
```

### Frontend Tests

```bash
cd frontend
npm run lint
npm run build

# E2E tests (auto-starts backend + frontend)
npx playwright test

# Full 30-day journey test
npx playwright test tests/e2e/new-user-full-journey.spec.ts

# Responsive audit (7 viewports + webkit)
PW_ENABLE_RESPONSIVE_AUDIT=1 npx playwright test tests/e2e/responsive-audit.spec.ts
```

### Production Smoke Tests

```bash
# Quick health check
python production_check.py

# Full smoke check (auto-registers test learner)
python smoke_check.py --base-url https://gat-prep-prod-production.up.railway.app

# Live E2E against production
cd frontend && E2E_BASE_URL=https://gat-prep-prod-production.up.railway.app \
  npx playwright test tests/e2e/new-user-full-journey.spec.ts
```

## Deployment

Before every deploy:

```bash
python sqlite_backup.py --label railway-predeploy
```

After every deploy:

```bash
python smoke_check.py --base-url https://gat-prep-prod-production.up.railway.app
```

## Project Structure

```
backend/
  main.py              # FastAPI app with all API endpoints
  models.py            # SQLAlchemy models
  database.py          # DB connection
  auth_utils.py        # JWT auth, rate limiting
  adaptive.py          # IRT-based adaptive algorithm
  seed.py              # Question bank loader
  questions/           # 9 skill modules (167 questions each)
  tests/               # pytest test suite
frontend/
  src/
    pages/             # Dashboard, Practice, Plan, Analytics, Admin, etc.
    components/        # Shared UI components
    hooks/useAuth.tsx  # Auth context
    lib/api.ts         # API client
  tests/e2e/           # Playwright E2E tests (13 test files)
```
