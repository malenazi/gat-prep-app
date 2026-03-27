"""
Question Bank Test Summary
Generates a comprehensive report of question testing.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import re
from questions import load_all_questions
from database import SessionLocal
from models import Skill, Question

def generate_report():
    """Generate comprehensive test report."""
    print("=" * 70)
    print("QUESTION BANK TESTING - FINAL REPORT")
    print("=" * 70)
    
    # Load all questions
    questions = load_all_questions()
    
    print(f"\n📊 OVERALL STATISTICS")
    print("-" * 70)
    print(f"Total Questions: {len(questions)}")
    
    # Count by skill
    skill_counts = {}
    arabic_counts = {}
    arabic_pattern = re.compile(r'[\u0600-\u06FF]')
    
    for q in questions:
        skill = q.skill_id
        skill_counts[skill] = skill_counts.get(skill, 0) + 1
        
        # Check for Arabic
        text = f"{q.text_ar} {q.option_a} {q.option_b} {q.option_c} {q.option_d}"
        arabic_chars = len(arabic_pattern.findall(text))
        if arabic_chars > 0:
            arabic_counts[skill] = arabic_counts.get(skill, 0) + arabic_chars
    
    print(f"\n📚 QUESTIONS BY SKILL")
    print("-" * 70)
    for skill, count in sorted(skill_counts.items()):
        arabic = arabic_counts.get(skill, 0)
        status = "⚠️  Has Arabic" if arabic > 0 else "✅ English"
        print(f"  {skill:25s}: {count:4d} questions {status}")
    
    print(f"\n🔤 ENGLISH TRANSLATION STATUS")
    print("-" * 70)
    total_arabic = sum(arabic_counts.values())
    if total_arabic == 0:
        print("✅ All questions are in English")
    else:
        print(f"⚠️  Found {total_arabic} Arabic characters:")
        for skill, count in arabic_counts.items():
            print(f"  - {skill}: {count} Arabic characters")
    
    print(f"\n✅ STRUCTURE VALIDATION")
    print("-" * 70)
    
    # Check difficulty distribution
    diff_ranges = {"0.0-0.2": 0, "0.2-0.4": 0, "0.4-0.6": 0, "0.6-0.8": 0, "0.8-1.0": 0}
    for q in questions:
        d = q.difficulty
        if d <= 0.2:
            diff_ranges["0.0-0.2"] += 1
        elif d <= 0.4:
            diff_ranges["0.2-0.4"] += 1
        elif d <= 0.6:
            diff_ranges["0.4-0.6"] += 1
        elif d <= 0.8:
            diff_ranges["0.6-0.8"] += 1
        else:
            diff_ranges["0.8-1.0"] += 1
    
    print("Difficulty Distribution:")
    for range_name, count in diff_ranges.items():
        pct = count / len(questions) * 100
        bar = "█" * int(pct / 2)
        print(f"  {range_name}: {count:4d} ({pct:5.1f}%) {bar}")
    
    print(f"\n🎯 CORRECT ANSWER DISTRIBUTION")
    print("-" * 70)
    answer_counts = {"a": 0, "b": 0, "c": 0, "d": 0}
    for q in questions:
        opt = q.correct_option
        if opt in answer_counts:
            answer_counts[opt] += 1
    
    for opt, count in answer_counts.items():
        pct = count / len(questions) * 100
        print(f"  Option {opt}: {count:4d} ({pct:5.1f}%)")
    
    # Sample questions
    print(f"\n📝 SAMPLE QUESTIONS (First from each skill)")
    print("-" * 70)
    seen_skills = set()
    for q in questions:
        if q.skill_id not in seen_skills:
            seen_skills.add(q.skill_id)
            print(f"\n{q.skill_id}:")
            print(f"  Q: {q.text_ar[:80]}...")
            print(f"  A: {q.option_a[:40]}...")
            print(f"  Correct: {q.correct_option}")
    
    print(f"\n" + "=" * 70)
    print("TESTING SUMMARY")
    print("=" * 70)
    
    tests_passed = 0
    tests_total = 5
    
    # Test 1: Questions load
    if len(questions) > 1300:
        print("✅ Questions load successfully")
        tests_passed += 1
    else:
        print("❌ Question loading issue")
    
    # Test 2: All skills present
    if len(skill_counts) == 9:
        print("✅ All 9 skills present")
        tests_passed += 1
    else:
        print(f"❌ Only {len(skill_counts)} skills found")
    
    # Test 3: Translation (exclude verbal_analogy)
    non_analogy_arabic = sum(c for s, c in arabic_counts.items() if s != 'verbal_analogy')
    if non_analogy_arabic == 0:
        print("✅ 8/8 translated skills are in English")
        tests_passed += 1
    else:
        print(f"⚠️  {non_analogy_arabic} Arabic chars in non-analogy questions")
    
    # Test 4: Difficulty range
    if all(0.0 <= q.difficulty <= 1.0 for q in questions):
        print("✅ All difficulty values valid")
        tests_passed += 1
    else:
        print("❌ Some difficulty values out of range")
    
    # Test 5: Answer options
    if all(q.correct_option in 'abcd' for q in questions):
        print("✅ All answer options valid")
        tests_passed += 1
    else:
        print("❌ Some answer options invalid")
    
    print(f"\nPassed: {tests_passed}/{tests_total} tests")
    
    if tests_passed == tests_total:
        print("\n🎉 Question bank is fully operational!")
    elif tests_passed >= 4:
        print("\n✅ Question bank is mostly operational (minor issues)")
    else:
        print("\n⚠️ Question bank has issues that need attention")
    
    print("=" * 70)

if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    generate_report()
