import argparse
import ast
import json
from pathlib import Path
from typing import Optional

from question_content import (
    extract_comparison_columns,
    is_quant_skill,
    normalize_math_markdown,
    suggest_figure_alt,
    suggest_table_caption,
)
from questions import QUESTION_MODULES


QUESTIONS_DIR = Path(__file__).resolve().parent / "questions"
QUESTION_MODULE_PATHS = {
    skill_id: QUESTIONS_DIR / f"{skill_id}.py" for skill_id, _loader in QUESTION_MODULES
}

TEXT_FIELDS = (
    "text_ar",
    "passage_ar",
    "option_a",
    "option_b",
    "option_c",
    "option_d",
    "explanation_ar",
)


def _string_value(node: Optional[ast.AST]) -> Optional[str]:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    return None


def _set_keyword(node: ast.Call, name: str, value: ast.expr) -> bool:
    for keyword in node.keywords:
        if keyword.arg == name:
            if ast.dump(keyword.value) != ast.dump(value):
                keyword.value = value
                return True
            return False
    node.keywords.append(ast.keyword(arg=name, value=value))
    return True


def _normalized_solution_steps(raw_value: str) -> str:
    try:
        parsed = json.loads(raw_value)
    except json.JSONDecodeError:
        return normalize_math_markdown(raw_value) or raw_value

    if isinstance(parsed, list):
        normalized = [normalize_math_markdown(str(step)) or str(step) for step in parsed]
        return json.dumps(normalized, ensure_ascii=False)
    if isinstance(parsed, str):
        return normalize_math_markdown(parsed) or parsed
    return raw_value


class QuestionModuleAutoFixer(ast.NodeTransformer):
    def __init__(self, skill_id: str):
        self.skill_id = skill_id
        self.counter = 0
        self.changed_questions = 0

    def visit_Call(self, node: ast.Call) -> ast.AST:
        self.generic_visit(node)
        if not isinstance(node.func, ast.Name) or node.func.id != "Question":
            return node

        self.counter += 1
        changed = False
        question_keywords = {keyword.arg: keyword for keyword in node.keywords if keyword.arg}
        source_key = f"{self.skill_id}:{self.counter:04d}"
        changed |= _set_keyword(node, "source_key", ast.Constant(source_key))

        if is_quant_skill(self.skill_id):
            for field in TEXT_FIELDS:
                current = _string_value(question_keywords.get(field).value) if question_keywords.get(field) else None
                if current is None:
                    continue
                normalized = normalize_math_markdown(current) or current
                if normalized != current:
                    changed |= _set_keyword(node, field, ast.Constant(normalized))

            solution_steps_node = question_keywords.get("solution_steps_ar")
            current_steps = _string_value(solution_steps_node.value) if solution_steps_node else None
            if current_steps:
                normalized_steps = _normalized_solution_steps(current_steps)
                if normalized_steps != current_steps:
                    changed |= _set_keyword(node, "solution_steps_ar", ast.Constant(normalized_steps))

            changed |= _set_keyword(node, "content_format", ast.Constant("markdown_math"))

        question_type = _string_value(question_keywords.get("question_type").value) if question_keywords.get("question_type") else None
        text_value = _string_value(question_keywords.get("text_ar").value) if question_keywords.get("text_ar") else None

        if question_type == "comparison" and text_value and "comparison_columns" not in question_keywords:
            normalized_text, columns = extract_comparison_columns(text_value)
            if columns:
                changed |= _set_keyword(node, "text_ar", ast.Constant(normalized_text or "Compare the two columns."))
                changed |= _set_keyword(
                    node,
                    "comparison_columns",
                    ast.Dict(
                        keys=[ast.Constant("a"), ast.Constant("b")],
                        values=[ast.Constant(columns["a"]), ast.Constant(columns["b"])],
                    ),
                )

        figure_svg = _string_value(question_keywords.get("figure_svg").value) if question_keywords.get("figure_svg") else None
        figure_alt = _string_value(question_keywords.get("figure_alt").value) if question_keywords.get("figure_alt") else None
        if figure_svg and not figure_alt:
            changed |= _set_keyword(
                node,
                "figure_alt",
                ast.Constant(
                    suggest_figure_alt(
                        self.skill_id,
                        question_type or "question",
                        text_value or "",
                    )
                ),
            )

        table_present = question_keywords.get("table_ar") is not None
        table_caption = _string_value(question_keywords.get("table_caption").value) if question_keywords.get("table_caption") else None
        if table_present and not table_caption:
            changed |= _set_keyword(
                node,
                "table_caption",
                ast.Constant(suggest_table_caption(self.skill_id, question_type or "question")),
            )

        if changed:
            self.changed_questions += 1
        return node


def auto_fix_module(skill_id: str, *, dry_run: bool = False) -> dict[str, int | str]:
    path = QUESTION_MODULE_PATHS[skill_id]
    source = path.read_text(encoding="utf-8")
    tree = ast.parse(source)
    fixer = QuestionModuleAutoFixer(skill_id)
    updated_tree = fixer.visit(tree)
    ast.fix_missing_locations(updated_tree)
    rewritten = ast.unparse(updated_tree) + "\n"

    if not dry_run and rewritten != source:
        path.write_text(rewritten, encoding="utf-8")

    return {
        "skill_id": skill_id,
        "questions_seen": fixer.counter,
        "questions_changed": fixer.changed_questions,
        "file_changed": int(rewritten != source),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Apply deterministic safe auto-fixes to question seed modules.")
    parser.add_argument("--dry-run", action="store_true", help="Report changes without writing files.")
    parser.add_argument(
        "--skills",
        nargs="*",
        default=None,
        help="Limit the auto-fix pass to specific skills, e.g. quant_algebra quant_statistics.",
    )
    parser.add_argument("--json", action="store_true", help="Print the auto-fix report as JSON.")
    args = parser.parse_args()

    skill_ids = args.skills or list(QUESTION_MODULE_PATHS.keys())
    report = [auto_fix_module(skill_id, dry_run=args.dry_run) for skill_id in skill_ids]

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return

    print("Question bank auto-fix")
    for item in report:
        print(
            f"  - {item['skill_id']}: {item['questions_changed']} changed / "
            f"{item['questions_seen']} scanned"
        )


if __name__ == "__main__":
    main()
