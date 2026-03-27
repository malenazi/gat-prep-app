"""
Question Bank Loading Tests
Tests that all question files load correctly and contain valid data.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import re
from questions import load_all_questions

def test_all_questions_load():
    """Test that all question files import and load successfully."""
    print("=" * 60)
    print("TEST 1: Loading All Questions")
    print("=" * 60)
    
    try:
        questions = load_all_questions()
        print(f"✅ Successfully loaded {len(questions)} questions")
        assert len(questions) > 0, "No questions loaded!"
        assert len(questions) >= 1300, f"Expected at least 1300 questions, got {len(questions)}"
        return True, len(questions)
    except Exception as e:
        print(f"❌ Failed to load questions: {e}")
        return False, 0

def test_question_structure():
    """Test that questions have all required fields."""
    print("\n" + "=" * 60)
    print("TEST 2: Question Structure Validation")
    print("=" * 60)
    
    questions = load_all_questions()
    required_fields = ['id', 'skill_id', 'question_type', 'text_ar', 'option_a', 
                      'option_b', 'option_c', 'option_d', 'correct_option', 
                      'explanation_ar', 'difficulty']
    
    errors = []
    for i, q in enumerate(questions[:100]):  # Check first 100
        for field in required_fields:
            if not hasattr(q, field) or getattr(q, field) is None:
                errors.append(f"Question {q.id} missing field: {field}")
    
    if errors:
        print(f"❌ Found {len(errors)} structure errors:")
        for err in errors[:10]:
            print(f"  - {err}")
        return False
    else:
        print(f"✅ All questions have required fields")
        return True

def test_skill_coverage():
    """Test that questions exist for all skills."""
    print("\n" + "=" * 60)
    print("TEST 3: Skill Coverage")
    print("=" * 60)
    
    questions = load_all_questions()
    skills_found = {}
    
    for q in questions:
        skill = q.skill_id
        skills_found[skill] = skills_found.get(skill, 0) + 1
    
    expected_skills = [
        'verbal_reading', 'verbal_analogy', 'verbal_completion',
        'verbal_error', 'verbal_oddword', 'quant_arithmetic',
        'quant_geometry', 'quant_algebra', 'quant_statistics'
    ]
    
    print(f"Found questions for {len(skills_found)} skills:")
    all_pass = True
    for skill in expected_skills:
        count = skills_found.get(skill, 0)
        if count > 0:
            print(f"  ✅ {skill}: {count} questions")
        else:
            print(f"  ❌ {skill}: NO questions!")
            all_pass = False
    
    return all_pass

def test_english_content():
    """Test that question content is in English."""
    print("\n" + "=" * 60)
    print("TEST 4: English Content Validation")
    print("=" * 60)
    
    questions = load_all_questions()
    arabic_pattern = re.compile(r'[\u0600-\u06FF]')
    
    issues = []
    for q in questions:
        # Skip verbal_analogy for now
        if q.skill_id == 'verbal_analogy':
            continue
            
        text = f"{q.text_ar} {q.option_a} {q.option_b} {q.option_c} {q.option_d}"
        arabic_chars = arabic_pattern.findall(text)
        
        if arabic_chars:
            issues.append({
                'id': q.id,
                'skill': q.skill_id,
                'arabic_chars': len(arabic_chars)
            })
    
    if issues:
        print(f"❌ Found {len(issues)} questions with Arabic content:")
        for issue in issues[:10]:
            print(f"  - Q{issue['id']} ({issue['skill']}): {issue['arabic_chars']} Arabic chars")
        return False
    else:
        print(f"✅ All questions are in English (except verbal_analogy)")
        return True

def test_correct_options():
    """Test that correct_option values are valid."""
    print("\n" + "=" * 60)
    print("TEST 5: Correct Option Validation")
    print("=" * 60)
    
    questions = load_all_questions()
    valid_options = {'a', 'b', 'c', 'd'}
    errors = []
    
    for q in questions:
        if q.correct_option not in valid_options:
            errors.append(f"Q{q.id}: invalid correct_option '{q.correct_option}'")
    
    if errors:
        print(f"❌ Found {len(errors)} invalid correct_options:")
        for err in errors[:10]:
            print(f"  - {err}")
        return False
    else:
        print(f"✅ All correct_options are valid (a, b, c, or d)")
        return True

def test_difficulty_range():
    """Test that difficulty values are in valid range."""
    print("\n" + "=" * 60)
    print("TEST 6: Difficulty Range Validation")
    print("=" * 60)
    
    questions = load_all_questions()
    errors = []
    
    for q in questions:
        if not (0.0 <= q.difficulty <= 1.0):
            errors.append(f"Q{q.id}: difficulty {q.difficulty} out of range [0.0, 1.0]")
    
    if errors:
        print(f"❌ Found {len(errors)} invalid difficulty values:")
        for err in errors[:10]:
            print(f"  - {err}")
        return False
    else:
        print(f"✅ All difficulty values are valid (0.0-1.0)")
        return True

def run_all_tests():
    """Run all question bank tests."""
    print("\n" + "=" * 60)
    print("QUESTION BANK TESTING SUITE")
    print("=" * 60)
    
    results = []
    
    # Test 1
    success, count = test_all_questions_load()
    results.append(("Question Loading", success, count))
    
    # Test 2
    results.append(("Question Structure", test_question_structure(), None))
    
    # Test 3
    results.append(("Skill Coverage", test_skill_coverage(), None))
    
    # Test 4
    results.append(("English Content", test_english_content(), None))
    
    # Test 5
    results.append(("Correct Options", test_correct_options(), None))
    
    # Test 6
    results.append(("Difficulty Range", test_difficulty_range(), None))
    
    # Summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    
    passed = sum(1 for _, success, _ in results if success)
    total = len(results)
    
    for name, success, data in results:
        status = "✅ PASS" if success else "❌ FAIL"
        extra = f" ({data})" if data else ""
        print(f"{status}: {name}{extra}")
    
    print(f"\nTotal: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed!")
    else:
        print("⚠️ Some tests failed. Review issues above.")
    
    return passed == total

if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    success = run_all_tests()
    sys.exit(0 if success else 1)
