# Soft Launch Runbook

Last updated: 2026-04-04

## Scope

This app is soft-launch ready on Railway with SQLite only if we keep the rollout disciplined:

- Run a single Railway instance only.
- Do not horizontally scale during the SQLite beta.
- Create a SQLite backup before every deploy or restart that could replace the runtime filesystem.
- Run the post-deploy smoke check before inviting users back in.

## Required Production Config

- `SECRET_KEY` must be explicitly set to a non-default value.
- `CORS_ORIGINS` must list the allowed frontend origins.
- `BOOTSTRAP_ADMIN_EMAIL` and `BOOTSTRAP_ADMIN_PASSWORD` are recommended for controlled admin access.

## Before Every Deploy

1. Freeze non-essential changes.
2. Create a SQLite backup:

```bash
python sqlite_backup.py --label railway-predeploy
```

3. Copy the generated backup file off the host or attach it to the release notes.
4. Record the deploy time and the commit you are shipping.

## After Every Deploy

Run the public checks first:

```bash
python production_check.py
```

Then run the full smoke check:

```bash
python smoke_check.py \
  --base-url https://gat-prep-prod-production.up.railway.app \
  --admin-email admin@qudra.academy \
  --admin-password '<secure-admin-password>'
```

Notes:

- If `SMOKE_EMAIL` and `SMOKE_PASSWORD` are not supplied, `smoke_check.py` will auto-register a fresh learner.
- If admin credentials are omitted, the script still runs the learner flow and skips admin-only checks.

## Expected Smoke Results

- `GET /health` returns `{"status": "ok"}`
- `GET /api/skills` returns at least 9 skills
- learner registration or login succeeds
- `GET /api/me` returns the authenticated learner profile
- learner can start diagnostic or reach practice, depending on account state
- admin login succeeds
- admin can read `/api/admin/config`

## If Smoke Fails

1. Stop rollout and pause tester invites.
2. Restore from the most recent SQLite backup if user data is at risk.
3. Fix the issue in a narrow patch.
4. Re-run the backup and smoke flow before reopening access.

## Beta Operating Rules

- Only ship fixes for auth, registration, content, analytics, or production incidents.
- Keep backup files outside the repo history.
- Migrate to PostgreSQL before any scale-out or broader public launch.
