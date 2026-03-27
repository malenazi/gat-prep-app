# قدرة أكاديمي — Qudra Academy

Arabic-only adaptive learning platform for the Saudi GAT — Science track.

## Quick Start

```bash
bash start.sh
```

### Manual Setup

**Backend:**
```bash
cd backend
pip install fastapi uvicorn sqlalchemy "python-jose[cryptography]" pydantic
uvicorn main:app --reload --port 8000
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

Frontend proxies `/api` to `localhost:8000` in dev mode.

## Files
- `backend/main.py` — FastAPI server (19 endpoints)
- `backend/models.py` — Database models (8 tables)
- `backend/adaptive.py` — Elo tracking + item selection + study plan
- `backend/seed.py` — 35 Arabic GAT questions + 9 badges
- `frontend/src/` — React 19 + TypeScript + shadcn/ui (Auth, Diagnostic, Dashboard, Practice, Plan, Analytics, Admin)
