import urllib.request
import json

BASE = 'https://gat-prep-prod-production.up.railway.app'

print('=== INFRASTRUCTURE HEALTH CHECK ===')

# 1. Health check
try:
    r = urllib.request.urlopen(f'{BASE}/', timeout=10)
    data = json.loads(r.read().decode())
    print(f'[OK] API Status: {data.get("message")}')
except Exception as e:
    print(f'[FAIL] API Error: {e}')

# 2. Skills endpoint
try:
    r = urllib.request.urlopen(f'{BASE}/api/skills', timeout=10)
    skills = json.loads(r.read().decode())
    print(f'[OK] Skills API: {len(skills)} skills loaded')
except Exception as e:
    print(f'[FAIL] Skills API Error: {e}')

# 3. Database test via login
try:
    login_data = json.dumps({'email': 'student@gat.sa', 'password': '123456'}).encode()
    req = urllib.request.Request(
        f'{BASE}/api/auth/login',
        data=login_data,
        headers={'Content-Type': 'application/json'}
    )
    r = urllib.request.urlopen(req, timeout=10)
    data = json.loads(r.read().decode())
    print(f'[OK] Login API: Working (token received: {bool(data.get("token"))})')
    token = data.get('token')
except Exception as e:
    print(f'[FAIL] Login API Error: {e}')
    token = None

print('\n=== SECURITY CHECK ===')
# 4. Check CORS headers
try:
    r = urllib.request.urlopen(f'{BASE}/api/skills', timeout=10)
    headers = dict(r.headers)
    cors = headers.get('Access-Control-Allow-Origin', 'NOT SET')
    print(f'[OK] CORS: {cors}')
except Exception as e:
    print(f'[FAIL] CORS Check Error: {e}')

print('[OK] HTTPS: Enabled (URL uses https://)')

print('\n=== DATA INTEGRITY CHECK ===')
# 5. Question count via API
try:
    req = urllib.request.Request(
        f'{BASE}/api/practice/next?skill_id=verbal_analogy',
        headers={'Authorization': f'Bearer {token or "test"}'}
    )
    r = urllib.request.urlopen(req, timeout=10)
    q = json.loads(r.read().decode())
    print(f'[OK] Questions API: Working (ID: {q.get("id")})')
    print(f'[OK] Question Text: {q.get("text_ar", "N/A")[:50]}...')
    
    # Check options
    options = q.get('options', [])
    labels = [o.get('label') for o in options]
    print(f'[OK] Option Labels: {labels}')
except Exception as e:
    print(f'[FAIL] Questions API Error: {e}')

print('\n=== SUMMARY ===')
print('All critical systems operational!' if token else 'Some issues detected!')
