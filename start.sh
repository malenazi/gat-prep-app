#!/bin/bash
echo "🎯 قدرة أكاديمي — Qudra Academy"
echo ""
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
python3 -m pip install fastapi uvicorn sqlalchemy "python-jose[cryptography]" "passlib[bcrypt]" "bcrypt==4.0.1" --break-system-packages -q 2>/dev/null
cd "$SCRIPT_DIR/frontend" && npm install -q 2>/dev/null && npm run build 2>/dev/null
cd "$SCRIPT_DIR/backend"
# Database is persistent — do NOT delete it on startup
# Use 'python reset_db.py' manually if you need a fresh database
echo "🚀 Server: http://localhost:8000"
python3 -m uvicorn main:app --host 0.0.0.0 --port 8000
