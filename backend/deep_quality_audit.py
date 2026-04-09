"""Deep quality audit for the entire question bank.

Goes beyond basic structural checks to detect:
1. Explanation/answer mismatches
2. Near-duplicate questions (cross-question)
3. Difficulty distribution gaps
4. Option plausibility issues
5. Questions where correct answer text appears in explanation but references wrong option
6. Skill coverage imbalance
7. Questions too short or too long
"""

import json
import re
import sys
import os
from collections import Counter, defaultdict
from difflib import SequenceMatcher
from typing import Any

sys.path.insert(0, os.path.dirname(__file__))

from questions import load_all_questions
from question_content import (
    collect_question_content_issues,
    classify_question_content,
    RATING_FIELDS,
)


def run_audit():
    questions = load_all_questions()
    print(f"Loaded {len(questions)} questions\n")

    results = {
        "total": len(questions),
        "issues": [],
        "stats": {},
    }

    # ── 1. Explanation references wrong answer ──────────────────────────
    answer_ref_pattern = re.compile(
        r"(?:correct answer|answer is|therefore|the answer)\s*(?:is|:)?\s*[\(\[]?([a-d])[\)\]]?",
        re.IGNORECASE,
    )
    explanation_mismatches = []
    for q in questions:
        explanation = getattr(q, "explanation_ar", "") or ""
        correct = (getattr(q, "correct_option", "") or "").lower()
        matches = answer_ref_pattern.findall(explanation)
        for m in matches:
            if m.lower() != correct:
                explanation_mismatches.append({
                    "source_key": getattr(q, "source_key", "?"),
                    "skill_id": q.skill_id,
                    "correct_option": correct,
                    "explanation_says": m.lower(),
                    "text_preview": q.text_ar[:80],
                })
    print(f"[1] Explanation/answer mismatches: {len(explanation_mismatches)}")
    for m in explanation_mismatches[:10]:
        print(f"    {m['source_key']}: correct={m['correct_option']} but explanation says {m['explanation_says']}")
    results["issues"].append({"type": "explanation_mismatch", "count": len(explanation_mismatches), "items": explanation_mismatches})

    # ── 2. Cross-question near-duplicates ──────────────────────────────
    print("\n[2] Cross-question near-duplicates...")
    by_skill = defaultdict(list)
    for q in questions:
        by_skill[q.skill_id].append(q)

    cross_dupes = []
    for skill_id, skill_qs in by_skill.items():
        # Use question text + correct option + option_a as signature (not passage)
        def q_signature(q):
            text = (q.text_ar or "").strip().lower()
            opts = f"|{getattr(q,'option_a','')}" f"|{getattr(q,'option_b','')}" f"|{getattr(q,'correct_option','')}"
            return (text + opts)[:300]

        sigs = [(i, q_signature(q)) for i, q in enumerate(skill_qs)]
        for i in range(len(sigs)):
            for j in range(i + 1, len(sigs)):
                sim = SequenceMatcher(None, sigs[i][1], sigs[j][1]).ratio()
                if sim >= 0.90:
                    q1 = skill_qs[sigs[i][0]]
                    q2 = skill_qs[sigs[j][0]]
                    cross_dupes.append({
                        "skill_id": skill_id,
                        "q1_key": getattr(q1, "source_key", "?"),
                        "q2_key": getattr(q2, "source_key", "?"),
                        "similarity": round(sim, 3),
                        "q1_text": q1.text_ar[:60],
                        "q2_text": q2.text_ar[:60],
                    })
    print(f"    Found {len(cross_dupes)} near-duplicate pairs")
    for d in cross_dupes[:10]:
        print(f"    {d['q1_key']} <-> {d['q2_key']} ({d['similarity']:.0%})")
    results["issues"].append({"type": "cross_duplicates", "count": len(cross_dupes), "items": cross_dupes})

    # ── 3. Difficulty distribution analysis ────────────────────────────
    print("\n[3] Difficulty distribution:")
    diff_buckets = Counter()
    diff_by_skill = defaultdict(lambda: Counter())
    for q in questions:
        bucket = round(q.difficulty, 1)
        diff_buckets[bucket] += 1
        diff_by_skill[q.skill_id][bucket] += 1

    for bucket in sorted(diff_buckets):
        bar = "#" * (diff_buckets[bucket] // 5)
        print(f"    {bucket:.1f}: {diff_buckets[bucket]:>4} {bar}")

    # Identify gaps
    gaps = []
    for skill_id in sorted(diff_by_skill):
        skill_diffs = diff_by_skill[skill_id]
        easy = sum(v for k, v in skill_diffs.items() if k <= 0.3)
        hard = sum(v for k, v in skill_diffs.items() if k >= 0.7)
        total = sum(skill_diffs.values())
        if easy < total * 0.15:
            gaps.append({"skill_id": skill_id, "issue": "too_few_easy", "easy_count": easy, "total": total, "easy_pct": round(easy / total * 100, 1)})
        if hard < total * 0.15:
            gaps.append({"skill_id": skill_id, "issue": "too_few_hard", "hard_count": hard, "total": total, "hard_pct": round(hard / total * 100, 1)})

    print(f"\n    Difficulty gaps: {len(gaps)}")
    for g in gaps:
        if g["issue"] == "too_few_easy":
            print(f"    {g['skill_id']}: only {g['easy_count']}/{g['total']} easy (≤0.3) = {g['easy_pct']}%")
        else:
            print(f"    {g['skill_id']}: only {g['hard_count']}/{g['total']} hard (≥0.7) = {g['hard_pct']}%")
    results["issues"].append({"type": "difficulty_gaps", "count": len(gaps), "items": gaps})

    # ── 4. Option quality checks ───────────────────────────────────────
    print("\n[4] Option quality issues:")
    option_issues = []

    for q in questions:
        opts = {
            "a": getattr(q, "option_a", ""),
            "b": getattr(q, "option_b", ""),
            "c": getattr(q, "option_c", ""),
            "d": getattr(q, "option_d", ""),
        }
        correct = getattr(q, "correct_option", "").lower()

        # Check if correct answer is obviously longest (common bad pattern)
        correct_len = len(opts.get(correct, ""))
        other_lens = [len(v) for k, v in opts.items() if k != correct]
        avg_other = sum(other_lens) / max(len(other_lens), 1)
        if correct_len > 0 and avg_other > 0 and correct_len > avg_other * 2.5:
            option_issues.append({
                "source_key": getattr(q, "source_key", "?"),
                "skill_id": q.skill_id,
                "issue": "correct_answer_much_longer",
                "correct_len": correct_len,
                "avg_other_len": round(avg_other, 1),
            })

        # Check all options are same type (all numeric or all text)
        numeric_count = sum(1 for v in opts.values() if re.match(r'^[\d\s\.\-\+/,]+$', v.strip()))
        if 0 < numeric_count < 4:
            option_issues.append({
                "source_key": getattr(q, "source_key", "?"),
                "skill_id": q.skill_id,
                "issue": "mixed_option_types",
                "numeric_count": numeric_count,
            })

    print(f"    Found {len(option_issues)} option quality issues")
    by_issue_type = Counter(i["issue"] for i in option_issues)
    for issue_type, count in by_issue_type.most_common():
        print(f"    {issue_type}: {count}")
    results["issues"].append({"type": "option_quality", "count": len(option_issues), "items": option_issues[:50]})

    # ── 5. Question text quality ───────────────────────────────────────
    print("\n[5] Text quality issues:")
    text_issues = []
    for q in questions:
        text = q.text_ar or ""
        # Very short questions (< 15 chars) might be incomplete
        if len(text.strip()) < 15:
            text_issues.append({
                "source_key": getattr(q, "source_key", "?"),
                "skill_id": q.skill_id,
                "issue": "very_short_text",
                "length": len(text.strip()),
                "text": text.strip(),
            })
        # Very long questions (> 500 chars without passage) might be confusing
        if len(text.strip()) > 500 and not getattr(q, "passage_ar", None):
            text_issues.append({
                "source_key": getattr(q, "source_key", "?"),
                "skill_id": q.skill_id,
                "issue": "very_long_text",
                "length": len(text.strip()),
            })

    print(f"    Found {len(text_issues)} text quality issues")
    for t in text_issues[:10]:
        if t["issue"] == "very_short_text":
            print(f"    {t['source_key']}: {t['issue']} ({t['length']} chars) \"{t['text']}\"")
        else:
            print(f"    {t['source_key']}: {t['issue']} ({t['length']} chars)")
    results["issues"].append({"type": "text_quality", "count": len(text_issues), "items": text_issues})

    # ── 6. Skill coverage balance ──────────────────────────────────────
    print("\n[6] Skill coverage:")
    skill_counts = Counter(q.skill_id for q in questions)
    avg_count = sum(skill_counts.values()) / len(skill_counts)
    for skill_id, count in sorted(skill_counts.items(), key=lambda x: x[1]):
        bar = "#" * (count // 5)
        deviation = "LOW" if count < avg_count * 0.7 else ("HIGH" if count > avg_count * 1.3 else "")
        print(f"    {skill_id:25s}: {count:>4} {bar} {deviation}")
    results["stats"]["skill_counts"] = dict(skill_counts)

    # ── 7. Rating coverage ─────────────────────────────────────────────
    print("\n[7] Rating coverage:")
    rated = sum(1 for q in questions if all(getattr(q, f, None) is not None for f in RATING_FIELDS))
    unrated = len(questions) - rated
    print(f"    Rated: {rated} ({rated/len(questions)*100:.1f}%)")
    print(f"    Unrated: {unrated} ({unrated/len(questions)*100:.1f}%)")
    results["stats"]["rated"] = rated
    results["stats"]["unrated"] = unrated

    # ── 8. Content format usage ────────────────────────────────────────
    print("\n[8] Content format:")
    format_counts = Counter(getattr(q, "content_format", "plain") or "plain" for q in questions)
    for fmt, count in format_counts.most_common():
        print(f"    {fmt}: {count}")

    # ── Summary ────────────────────────────────────────────────────────
    total_issues = sum(item["count"] for item in results["issues"])
    print(f"\n{'='*60}")
    print(f"AUDIT SUMMARY")
    print(f"{'='*60}")
    print(f"Total questions: {len(questions)}")
    print(f"Total issues found: {total_issues}")
    print(f"  Explanation mismatches: {len(explanation_mismatches)}")
    print(f"  Cross-question duplicates: {len(cross_dupes)}")
    print(f"  Difficulty gaps: {len(gaps)}")
    print(f"  Option quality issues: {len(option_issues)}")
    print(f"  Text quality issues: {len(text_issues)}")
    print(f"  Unrated questions: {unrated}")

    # Write JSON report
    report_path = os.path.join(os.path.dirname(__file__), "quality_audit_report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\nFull report saved to: {report_path}")


if __name__ == "__main__":
    run_audit()
