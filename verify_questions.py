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

# Test all 9 skills
skills = ['verbal_reading', 'verbal_analogy', 'verbal_completion', 
          'verbal_error', 'verbal_oddword', 'quant_arithmetic', 
          'quant_algebra', 'quant_geometry', 'quant_statistics']

print('\n=== TESTING ALL 9 SKILLS ===')
for skill in skills:
    try:
        req = urllib.request.Request(
            f'{BASE}/api/practice/next?skill_id={skill}',
            headers={'Authorization': f'Bearer {token}'}
        )
        r = urllib.request.urlopen(req, timeout=10)
        q = json.loads(r.read().decode())
        
        text = q.get('text_ar', 'N/A')[:50]
        labels = [o.get('label') for o in q.get('options', [])]
        print(f'{skill:25s}: {text:50s} | Options: {labels}')
    except Exception as e:
        print(f'{skill:25s}: ERROR - {e}')

print('\n=== VERIFICATION COMPLETE ===')
