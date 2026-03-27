import urllib.request
import json

BASE = 'https://gat-prep-prod-production.up.railway.app'

# Login
login_data = json.dumps({'email': 'student@gat.sa', 'password': '123456'}).encode()
req = urllib.request.Request(
    f'{BASE}/api/auth/login',
    data=login_data,
    headers={'Content-Type': 'application/json'}
)
r = urllib.request.urlopen(req, timeout=10)
data = json.loads(r.read().decode())
token = data.get('token')
print(f'Login successful!')

# Get question
req = urllib.request.Request(
    f'{BASE}/api/practice/next?skill_id=verbal_analogy',
    headers={'Authorization': f'Bearer {token}'}
)
r = urllib.request.urlopen(req, timeout=10)
response_text = r.read().decode()
print(f'\nRaw response:')
print(response_text[:500])

q = json.loads(response_text)
print(f'\nParsed keys: {q.keys()}')
print(f'id: {q.get("id")}')
print(f'text_ar: {q.get("text_ar")}')
print(f'options type: {type(q.get("options"))}')
