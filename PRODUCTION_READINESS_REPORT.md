# Qudra Academy - Production Readiness Report

Date: 2026-04-04
Environment: Railway soft launch
URL: https://gat-prep-prod-production.up.railway.app

## Executive Summary

Qudra Academy is ready for a controlled soft launch, not an unrestricted public scale-up.

The critical production items are now in place:

- shared demo, test, and seeded admin accounts removed from normal startup
- secure admin bootstrap added
- password hashing upgraded for production use
- registration and login hardened with normalization and throttling
- browser-saveable email and password fields enabled
- active landing page copy rewritten to avoid unsupported trust or endorsement claims

The remaining operational constraint is SQLite. This launch is safe only if every deploy follows the backup and smoke-check runbook in [SOFT_LAUNCH_RUNBOOK.md](SOFT_LAUNCH_RUNBOOK.md).

## Release Status

| Area | Status | Notes |
|------|--------|-------|
| Auth and registration | Complete | bcrypt, normalized email lookup, throttling |
| Admin access | Complete | bootstrap-only admin creation |
| Demo-account removal | Complete | no public demo login path |
| Browser credential saving | Complete | proper form semantics on login and register |
| Public launch copy | Complete | beta-safe messaging on active landing page |
| SQLite guardrails | Complete | backup script, smoke script, and runbook added |

## Production Controls

Required configuration:

- `SECRET_KEY`
- `CORS_ORIGINS`
- recommended: `BOOTSTRAP_ADMIN_EMAIL`
- recommended: `BOOTSTRAP_ADMIN_PASSWORD`

Operational rules:

- run one Railway instance only
- do not scale out while SQLite is the primary database
- create a SQLite backup before every deploy
- run smoke checks immediately after deploy
- limit releases during beta to bug fixes and essential content changes

## Deploy Workflow

Before deploy:

```bash
python sqlite_backup.py --label railway-predeploy
```

After deploy:

```bash
python production_check.py
python smoke_check.py --admin-email admin@qudra.academy --admin-password '<secure-admin-password>'
```

## Known Limitations

1. SQLite remains the highest operational risk.
   Use backups before deploys and keep the app on a single instance.

2. PostgreSQL migration is still required before broader launch or scale-out.

3. The frontend build still emits a large chunk warning.
   This is not a soft-launch blocker, but it should be addressed after beta stabilization.

## Soft Launch Recommendation

Approved for soft launch with guardrails.

Do not treat this as final-scale production until:

- PostgreSQL replaces SQLite
- deploy backup and restore flow is routine
- the team is comfortable with observed beta traffic and incident handling
