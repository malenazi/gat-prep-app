import json
import xml.etree.ElementTree as ET
from typing import Any, Optional

from sqlalchemy import inspect, text


ALLOWED_SVG_TAGS = {
    "svg",
    "g",
    "line",
    "rect",
    "circle",
    "ellipse",
    "polygon",
    "polyline",
    "path",
    "text",
    "tspan",
}

ALLOWED_SVG_ATTRS = {
    "xmlns",
    "viewBox",
    "width",
    "height",
    "x",
    "y",
    "x1",
    "x2",
    "y1",
    "y2",
    "cx",
    "cy",
    "r",
    "rx",
    "ry",
    "d",
    "points",
    "fill",
    "stroke",
    "stroke-width",
    "stroke-linecap",
    "stroke-linejoin",
    "stroke-dasharray",
    "opacity",
    "fill-opacity",
    "stroke-opacity",
    "transform",
    "font-size",
    "font-family",
    "font-weight",
    "text-anchor",
    "dominant-baseline",
    "preserveAspectRatio",
}

DISALLOWED_SVG_VALUE_SNIPPETS = ("javascript:", "data:", "url(")


def _local_name(name: str) -> str:
    if "}" in name:
        return name.split("}", 1)[1]
    if ":" in name:
        return name.split(":", 1)[1]
    return name


def validate_svg_markup(svg_markup: Optional[str]) -> Optional[str]:
    if svg_markup is None:
        return None

    normalized = svg_markup.strip()
    if not normalized:
        return None

    try:
        root = ET.fromstring(normalized)
    except ET.ParseError as exc:
        raise ValueError(f"Invalid SVG markup: {exc}") from exc

    if _local_name(root.tag) != "svg":
        raise ValueError("SVG markup must have an <svg> root element")

    for element in root.iter():
        tag = _local_name(element.tag)
        if tag not in ALLOWED_SVG_TAGS:
            raise ValueError(f"SVG tag '{tag}' is not allowed")

        for raw_attr, raw_value in element.attrib.items():
            attr = _local_name(raw_attr)
            value = str(raw_value)
            lowered = value.lower()

            if attr.startswith("on"):
                raise ValueError(f"Event handler attribute '{attr}' is not allowed")
            if attr not in ALLOWED_SVG_ATTRS:
                raise ValueError(f"SVG attribute '{attr}' is not allowed")
            if any(snippet in lowered for snippet in DISALLOWED_SVG_VALUE_SNIPPETS):
                raise ValueError(f"SVG attribute '{attr}' contains a blocked reference")

    return normalized


def validate_table_payload(table_payload: Any) -> Optional[dict[str, list[list[str]] | list[str]]]:
    if table_payload is None:
        return None

    if not isinstance(table_payload, dict):
        raise ValueError("Table payload must be an object with headers and rows")

    headers = table_payload.get("headers")
    rows = table_payload.get("rows")

    if not isinstance(headers, list) or not headers:
        raise ValueError("Table headers must be a non-empty list")
    if not isinstance(rows, list) or not rows:
        raise ValueError("Table rows must be a non-empty list")

    normalized_headers: list[str] = []
    for header in headers:
        if not isinstance(header, str) or not header.strip():
            raise ValueError("Each table header must be a non-empty string")
        normalized_headers.append(header.strip())

    normalized_rows: list[list[str]] = []
    expected_width = len(normalized_headers)
    for row in rows:
        if not isinstance(row, list) or len(row) != expected_width:
            raise ValueError("Each table row must match the number of headers")
        normalized_row: list[str] = []
        for cell in row:
            if not isinstance(cell, str):
                raise ValueError("Each table cell must be a string")
            normalized_row.append(cell.strip())
        normalized_rows.append(normalized_row)

    return {"headers": normalized_headers, "rows": normalized_rows}


def serialize_table_payload(table_payload: Any) -> Optional[str]:
    normalized = validate_table_payload(table_payload)
    if normalized is None:
        return None
    return json.dumps(normalized, ensure_ascii=False)


def deserialize_table_payload(raw_payload: Optional[str]) -> Optional[dict[str, list[list[str]] | list[str]]]:
    if raw_payload is None:
        return None
    if isinstance(raw_payload, str) and not raw_payload.strip():
        return None

    try:
        parsed = json.loads(raw_payload)
    except (TypeError, json.JSONDecodeError) as exc:
        raise ValueError("Stored table payload is not valid JSON") from exc

    return validate_table_payload(parsed)


def normalize_question_visual_fields(question: Any):
    question.figure_svg = validate_svg_markup(getattr(question, "figure_svg", None))
    question.table_ar = serialize_table_payload(getattr(question, "table_ar", None))
    return question


def prepare_question_visual_fields(
    figure_svg: Optional[str],
    table_ar: Any,
) -> tuple[Optional[str], Optional[str]]:
    return validate_svg_markup(figure_svg), serialize_table_payload(table_ar)


def ensure_question_visual_columns(engine) -> None:
    inspector = inspect(engine)
    if "questions" not in inspector.get_table_names():
        return

    existing_columns = {column["name"] for column in inspector.get_columns("questions")}
    statements: list[str] = []

    if "figure_svg" not in existing_columns:
        statements.append("ALTER TABLE questions ADD COLUMN figure_svg TEXT")
    if "table_ar" not in existing_columns:
        statements.append("ALTER TABLE questions ADD COLUMN table_ar TEXT")

    if not statements:
        return

    with engine.begin() as connection:
        for statement in statements:
            connection.execute(text(statement))
