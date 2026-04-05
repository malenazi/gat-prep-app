import argparse
import json
from collections import Counter, defaultdict
from typing import Any

from question_content import (
    collect_question_content_issues,
    collect_question_quality_metadata,
)
from questions import load_all_questions


def _summarize_questions(questions: list[Any]) -> dict[str, Any]:
    classifications = Counter()
    status_counts = Counter()
    by_skill: dict[str, Counter[str]] = defaultdict(Counter)
    queue_by_skill: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    flagged_examples: list[dict[str, Any]] = []

    for question in questions:
        issues = collect_question_content_issues(question)
        quality = collect_question_quality_metadata(question, issues)
        classification = quality["content_classification"]
        recommended_action = quality["recommended_action"]
        status = getattr(question, "status", "active") or "active"

        classifications[classification] += 1
        status_counts[status] += 1
        by_skill[question.skill_id][classification] += 1
        queue_by_skill[question.skill_id][recommended_action] += 1

        if issues and len(flagged_examples) < 40:
            flagged_examples.append(
                {
                    "id": getattr(question, "id", None),
                    "source_key": quality["source_key"],
                    "skill_id": question.skill_id,
                    "question_type": question.question_type,
                    "status": status,
                    "classification": classification,
                    "recommended_action": recommended_action,
                    "ratings_complete": quality["ratings_complete"],
                    "content_issue_counts": quality["content_issue_counts"],
                    "issues": [
                        {
                            "severity": issue.severity,
                            "code": issue.code,
                            "field": issue.field,
                            "message": issue.message,
                        }
                        for issue in issues
                    ],
                }
            )

    return {
        "total_questions": len(questions),
        "classifications": dict(classifications),
        "status_counts": dict(status_counts),
        "by_skill": {skill: dict(counter) for skill, counter in sorted(by_skill.items())},
        "queue_by_skill": {
            skill: dict(counter) for skill, counter in sorted(queue_by_skill.items())
        },
        "flagged_examples": flagged_examples,
    }


def build_report() -> dict[str, Any]:
    before = _summarize_questions(load_all_questions(apply_refresh=False))
    after = _summarize_questions(load_all_questions(apply_refresh=True))

    before_classes = Counter(before["classifications"])
    after_classes = Counter(after["classifications"])
    delta = {
        key: after_classes.get(key, 0) - before_classes.get(key, 0)
        for key in sorted(set(before_classes) | set(after_classes))
    }

    return {
        "before_refresh": before,
        "after_refresh": after,
        "before_after_summary": {
            "classification_delta": delta,
            "status_delta": {
                key: Counter(after["status_counts"]).get(key, 0)
                - Counter(before["status_counts"]).get(key, 0)
                for key in sorted(
                    set(before["status_counts"]) | set(after["status_counts"])
                )
            },
        },
        "total_questions": after["total_questions"],
        "classifications": after["classifications"],
        "status_counts": after["status_counts"],
        "by_skill": after["by_skill"],
        "queue_by_skill": after["queue_by_skill"],
        "flagged_examples": after["flagged_examples"],
    }


def print_report(report: dict[str, Any], *, mode: str, skill: str | None) -> None:
    if mode == "dry-run":
        print("Question content audit dry run")
        print(f"Total questions: {report['total_questions']}")
        print("Classification delta after refresh:")
        for key, value in report["before_after_summary"]["classification_delta"].items():
            print(f"  - {key}: {value:+}")
        print("Status delta after refresh:")
        for key, value in report["before_after_summary"]["status_delta"].items():
            print(f"  - {key}: {value:+}")
        return

    if mode == "queues":
        print("Question content queues")
        queue_source = report["queue_by_skill"]
        for skill_id, actions in queue_source.items():
            if skill and skill_id != skill:
                continue
            print(f"- {skill_id}")
            for action, count in sorted(actions.items()):
                print(f"    {action}: {count}")
        return

    print(f"Total questions: {report['total_questions']}")
    print("Classifications:")
    for key, value in sorted(report["classifications"].items()):
        print(f"  - {key}: {value}")
    print("Status counts:")
    for key, value in sorted(report["status_counts"].items()):
        print(f"  - {key}: {value}")
    print("Flagged examples:")
    for item in report["flagged_examples"][:10]:
        print(
            f"  - {item['source_key']} {item['skill_id']} "
            f"({item['classification']}, {item['recommended_action']}): "
            + ", ".join(issue["code"] for issue in item["issues"])
        )


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit question content formatting and QA status.")
    parser.add_argument("--json", action="store_true", help="Print the full audit report as JSON.")
    parser.add_argument(
        "--mode",
        choices=("report", "queues", "dry-run"),
        default="report",
        help="Choose the report mode.",
    )
    parser.add_argument("--skill", help="Limit queue output to a specific skill.")
    args = parser.parse_args()

    report = build_report()
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return

    print_report(report, mode=args.mode, skill=args.skill)


if __name__ == "__main__":
    main()
