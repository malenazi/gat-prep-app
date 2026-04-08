---
name: Deployment Configuration
description: How to deploy Qudra Academy — Railpack on Railway with GitHub auto-deploy
type: reference
---

## Deployment Method: Railpack + GitHub Auto-Deploy

### How it works
1. Push to `master` branch on GitHub
2. Railway auto-deploys via GitHub integration (connected to `malenazi/gat-prep-app`)
3. Railpack builds: installs Python, copies pre-built frontend, starts uvicorn
4. Deploy time: ~90 seconds

### Deploy steps
```bash
# 1. Build frontend locally
cd frontend && npm run build

# 2. Commit dist + code changes
git add -A && git commit -m "description"

# 3. Push — Railway auto-deploys
git push origin master

# 4. Verify (~2 min later)
python smoke_check.py --base-url https://gat-prep-prod-production.up.railway.app --skip-admin
```

### Configuration files
- `railway.json` — builder=RAILPACK, buildCommand, startCommand (4 workers)
- `frontend/dist/` — pre-built, committed to git (no Node.js on Railway)
- No nixpacks.toml, no Dockerfile

### Key settings
- Builder: RAILPACK (set in Railway dashboard → Settings → Build)
- Build command: `mkdir -p backend/static && cp -r frontend/dist/* backend/static/`
- Start command: `cd backend && python -m uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000} --workers 4`
- Auto-deploy: GitHub repo `malenazi/gat-prep-app`, branch `master`

### Railway CLI (if needed)
- `railway login` then `railway up` for manual deploy
- CLI token auth doesn't work well — use GitHub auto-deploy instead

### Important
- Always run `npm run build` locally before pushing (dist is committed)
- The `.gitignore` has `dist/` commented out so it gets included
- `frontend/dist/` must be force-added with `git add -f frontend/dist/` if ever re-ignored
