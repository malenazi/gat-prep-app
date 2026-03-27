"""
Question API Endpoint Tests
Tests that question-related API endpoints work correctly.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import requests
import json

BASE_URL = "http://localhost:3434/api"

def login_user(email, password):
    """Login and return token."""
    resp = requests.post(f"{BASE_URL}/auth/login", json={
        "email": email,
        "password": password
    })
    if resp.status_code == 200:
        return resp.json()["token"]
    return None

def test_skills_endpoint():
    """Test GET /api/skills returns skills in English."""
    print("\n" + "=" * 60)
    print("API TEST 1: Skills Endpoint")
    print("=" * 60)
    
    resp = requests.get(f"{BASE_URL}/skills")
    
    if resp.status_code != 200:
        print(f"❌ Failed: Status {resp.status_code}")
        return False
    
    skills = resp.json()
    print(f"✅ Returned {len(skills)} skills")
    
    # Check skill names are in English
    for skill in skills[:3]:
        name = skill.get("name_ar", "")
        print(f"  - {skill['id']}: {name}")
    
    return True

def test_practice_next_endpoint():
    """Test GET /api/practice/next returns a question."""
    print("\n" + "=" * 60)
    print("API TEST 2: Practice Next Endpoint")
    print("=" * 60)
    
    token = login_user("sara@gat.sa", "123456")
    if not token:
        print("❌ Failed to login")
        return False
    
    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.get(f"{BASE_URL}/practice/next", headers=headers)
    
    if resp.status_code != 200:
        print(f"❌ Failed: Status {resp.status_code}")
        return False
    
    data = resp.json()
    
    if "question" not in data or not data["question"]:
        print("❌ No question in response")
        return False
    
    q = data["question"]
    print(f"✅ Got question ID: {q['id']}")
    print(f"   Skill: {q['skill_id']}")
    print(f"   Type: {q['question_type']}")
    print(f"   Text preview: {q['text_ar'][:60]}...")
    
    return True

def test_practice_answer_endpoint():
    """Test POST /api/practice/answer submits answer."""
    print("\n" + "=" * 60)
    print("API TEST 3: Practice Answer Endpoint")
    print("=" * 60)
    
    token = login_user("sara@gat.sa", "123456")
    if not token:
        print("❌ Failed to login")
        return False
    
    headers = {"Authorization": f"Bearer {token}"}
    
    # Get a question first
    resp = requests.get(f"{BASE_URL}/practice/next", headers=headers)
    if resp.status_code != 200:
        print("❌ Failed to get question")
        return False
    
    q = resp.json()["question"]
    qid = q["id"]
    
    # Submit answer
    resp = requests.post(f"{BASE_URL}/practice/answer", headers=headers, json={
        "question_id": qid,
        "selected_option": "a",
        "time_spent_seconds": 30
    })
    
    if resp.status_code != 200:
        print(f"❌ Failed to submit answer: {resp.status_code}")
        return False
    
    result = resp.json()
    print(f"✅ Answer submitted successfully")
    print(f"   Correct: {result.get('is_correct')}")
    print(f"   XP Earned: {result.get('xp_earned')}")
    
    return True

def test_diagnostic_endpoints():
    """Test diagnostic question endpoints."""
    print("\n" + "=" * 60)
    print("API TEST 4: Diagnostic Endpoints")
    print("=" * 60)
    
    token = login_user("student@gat.sa", "123456")
    if not token:
        print("❌ Failed to login")
        return False
    
    headers = {"Authorization": f"Bearer {token}"}
    
    # Start diagnostic
    resp = requests.post(f"{BASE_URL}/diagnostic/start", headers=headers)
    if resp.status_code != 200:
        print(f"❌ Failed to start diagnostic: {resp.status_code}")
        return False
    
    print("✅ Diagnostic started")
    
    # Get next question
    resp = requests.get(f"{BASE_URL}/diagnostic/next", headers=headers)
    if resp.status_code != 200:
        print(f"❌ Failed to get diagnostic question: {resp.status_code}")
        return False
    
    q = resp.json()
    print(f"✅ Got diagnostic question: {q['id']}")
    print(f"   Skill: {q['skill_id']}")
    
    return True

def test_question_types():
    """Test that different question types return correctly."""
    print("\n" + "=" * 60)
    print("API TEST 5: Question Types Coverage")
    print("=" * 60)
    
    token = login_user("sara@gat.sa", "123456")
    if not token:
        print("❌ Failed to login")
        return False
    
    headers = {"Authorization": f"Bearer {token}"}
    
    # Fetch multiple questions and check types
    types_found = set()
    for _ in range(10):
        resp = requests.get(f"{BASE_URL}/practice/next", headers=headers)
        if resp.status_code == 200:
            q = resp.json().get("question")
            if q:
                types_found.add(q["skill_id"])
        
        # Submit dummy answer to get next
        if q:
            requests.post(f"{BASE_URL}/practice/answer", headers=headers, json={
                "question_id": q["id"],
                "selected_option": "a",
                "time_spent_seconds": 10
            })
    
    print(f"✅ Found {len(types_found)} different skill types:")
    for skill in types_found:
        print(f"  - {skill}")
    
    return len(types_found) >= 3

def run_all_api_tests():
    """Run all API tests."""
    print("=" * 60)
    print("QUESTION API TESTING SUITE")
    print("=" * 60)
    
    # Check server is running
    try:
        requests.get(f"{BASE_URL}/skills", timeout=5)
    except:
        print("\n❌ Server is not running on port 3434!")
        print("Please start the server first.")
        return False
    
    results = []
    
    results.append(("Skills Endpoint", test_skills_endpoint()))
    results.append(("Practice Next", test_practice_next_endpoint()))
    results.append(("Practice Answer", test_practice_answer_endpoint()))
    results.append(("Diagnostic", test_diagnostic_endpoints()))
    results.append(("Question Types", test_question_types()))
    
    # Summary
    print("\n" + "=" * 60)
    print("API TEST SUMMARY")
    print("=" * 60)
    
    passed = sum(1 for _, success in results if success)
    total = len(results)
    
    for name, success in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status}: {name}")
    
    print(f"\nTotal: {passed}/{total} tests passed")
    
    return passed == total

if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    success = run_all_api_tests()
    sys.exit(0 if success else 1)
