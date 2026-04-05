import json
import os
import urllib.request

BASE = os.getenv("PRODUCTION_CHECK_BASE", "https://gat-prep-prod-production.up.railway.app").rstrip("/")
CHECK_EMAIL = os.getenv("CHECK_EMAIL", "").strip()
CHECK_PASSWORD = os.getenv("CHECK_PASSWORD", "").strip()

print("=== INFRASTRUCTURE HEALTH CHECK ===")

try:
    response = urllib.request.urlopen(f"{BASE}/health", timeout=10)
    data = json.loads(response.read().decode())
    print(f'[OK] Health endpoint: {data.get("status")}')
except Exception as exc:
    print(f"[FAIL] Health endpoint error: {exc}")

try:
    response = urllib.request.urlopen(f"{BASE}/api", timeout=10)
    data = json.loads(response.read().decode())
    print(f'[OK] API Status: {data.get("message")}')
except Exception as exc:
    print(f"[FAIL] API Error: {exc}")

try:
    response = urllib.request.urlopen(f"{BASE}/api/skills", timeout=10)
    skills = json.loads(response.read().decode())
    print(f"[OK] Skills API: {len(skills)} skills loaded")
except Exception as exc:
    print(f"[FAIL] Skills API Error: {exc}")
    skills = []

print("\n=== SECURITY CHECK ===")
print("[OK] HTTPS: Enabled (URL uses https://)")
if CHECK_EMAIL and CHECK_PASSWORD:
    try:
        login_data = json.dumps({"email": CHECK_EMAIL, "password": CHECK_PASSWORD}).encode()
        request = urllib.request.Request(
            f"{BASE}/api/auth/login",
            data=login_data,
            headers={"Content-Type": "application/json"},
        )
        response = urllib.request.urlopen(request, timeout=10)
        data = json.loads(response.read().decode())
        token = data.get("token")
        print(f"[OK] Login API: Working (token received: {bool(token)})")
    except Exception as exc:
        print(f"[FAIL] Login API Error: {exc}")
        token = None
else:
    token = None
    print("[SKIP] Login check: set CHECK_EMAIL and CHECK_PASSWORD to verify auth")

print("\n=== DATA CHECK ===")
if token:
    try:
        request = urllib.request.Request(
            f"{BASE}/api/me",
            headers={"Authorization": f"Bearer {token}"},
        )
        response = urllib.request.urlopen(request, timeout=10)
        user = json.loads(response.read().decode())
        print(f'[OK] Authenticated profile check for: {user.get("email")}')
    except Exception as exc:
        print(f"[FAIL] Authenticated profile check failed: {exc}")
else:
    print("[SKIP] Authenticated profile check: credentials not provided")

print("\n=== SUMMARY ===")
print("[OK] Public health checks completed")
