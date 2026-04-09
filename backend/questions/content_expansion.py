"""Phase 5 content expansion: adds visual geometry, table statistics,
and comparison questions to strengthen the question bank.

Added questions: 20 geometry (SVG), 15 statistics (table), 10 comparison.
"""

import json
from models import Question


def _steps(*items: str) -> str:
    return json.dumps(list(items))


_SVG_STYLE = (
    '<style>'
    '.shape{fill:#dbeafe;stroke:#1e293b;stroke-width:3}'
    '.shape-alt{fill:#e0e7ff;stroke:#1e293b;stroke-width:3}'
    '.shape-warm{fill:#fef3c7;stroke:#1e293b;stroke-width:3}'
    '.shape-green{fill:#dcfce7;stroke:#1e293b;stroke-width:3}'
    '.shape-red{fill:#fee2e2;stroke:#1e293b;stroke-width:3}'
    '.shape-purple{fill:#ede9fe;stroke:#1e293b;stroke-width:3}'
    '.shape-cyan{fill:#cffafe;stroke:#1e293b;stroke-width:3}'
    '.line{stroke:#1e293b;stroke-width:3}'
    '.line-thin{stroke:#1e293b;stroke-width:2}'
    '.line-dash{stroke:#1e293b;stroke-width:2;stroke-dasharray:6 4}'
    '.label{font-size:14px;font-family:Arial,sans-serif;fill:#1e293b}'
    '</style>'
)


def _svg(content: str, vb: str = "0 0 220 140") -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" '
        f'width="220" height="140" preserveAspectRatio="xMidYMid meet">'
        f"{_SVG_STYLE}{content}</svg>"
    )


def get_geometry_questions() -> list[Question]:
    return [
        # ── Easy (0.2) ──
        Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.2,
            text_ar="What is the perimeter of the square shown?",
            figure_svg=_svg(
                '<rect x="50" y="20" width="100" height="100" class="shape-purple"/>'
                '<text x="100" y="14" text-anchor="middle" class="label">5 cm</text>'
            ),
            figure_alt="A square with side length 5 cm.",
            option_a="10 cm", option_b="15 cm", option_c="20 cm", option_d="25 cm",
            correct_option="c",
            explanation_ar="A square has 4 equal sides. Perimeter = 4 x 5 = 20 cm.\n\nWhy other options are wrong:\n- 10 cm: Only 2 sides\n- 15 cm: Only 3 sides\n- 25 cm: This is the area (5 x 5)",
            solution_steps_ar=_steps("All sides of a square are equal: 5 cm.", "Perimeter = 4 x side = 4 x 5.", "Perimeter = 20 cm."),
            tags="square,perimeter,figure", stage="foundation",
            rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5,
            rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71,
            source_key="expansion_geom:0001", authoring_source="human", content_format="plain"),

        Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.2,
            text_ar="What is the area of this rectangle?",
            figure_svg=_svg(
                '<rect x="30" y="30" width="140" height="70" class="shape"/>'
                '<text x="100" y="22" text-anchor="middle" class="label">7 cm</text>'
                '<text x="178" y="70" class="label">4 cm</text>'
            ),
            figure_alt="A rectangle with length 7 cm and width 4 cm.",
            option_a="11 cm", option_b="22 cm", option_c="28 cm", option_d="35 cm",
            correct_option="c",
            explanation_ar="Area of a rectangle = length x width = 7 x 4 = 28 cm.\n\nWhy other options are wrong:\n- 11 cm: Sum of sides (7+4)\n- 22 cm: Perimeter calculation error\n- 35 cm: Multiplied by wrong value",
            solution_steps_ar=_steps("Read dimensions: 7 cm and 4 cm.", "Area = length x width.", "7 x 4 = 28 cm."),
            tags="rectangle,area,figure", stage="foundation",
            rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5,
            rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71,
            source_key="expansion_geom:0002", authoring_source="human", content_format="plain"),

        # ── Medium (0.4-0.5) ──
        Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.4,
            text_ar="Find the area of the triangle shown in the diagram.",
            figure_svg=_svg(
                '<path d="M30 110 L190 110 L110 25 Z" class="shape-green"/>'
                '<line x1="110" y1="25" x2="110" y2="110" class="line-dash"/>'
                '<text x="110" y="128" text-anchor="middle" class="label">16 cm</text>'
                '<text x="120" y="72" class="label">8 cm</text>'
            ),
            figure_alt="A triangle with base 16 cm and height 8 cm.",
            option_a="32 cm", option_b="48 cm", option_c="64 cm", option_d="128 cm",
            correct_option="c",
            explanation_ar="Area = (1/2) x base x height = (1/2) x 16 x 8 = 64 cm.\n\nWhy other options are wrong:\n- 32 cm: Divided by 4 instead of 2\n- 48 cm: Used wrong formula\n- 128 cm: Forgot to divide by 2",
            solution_steps_ar=_steps("Read base = 16 cm and height = 8 cm.", "Area = (1/2) x base x height.", "(1/2) x 16 x 8 = 64 cm."),
            tags="triangle,area,figure", stage="building",
            rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5,
            rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57,
            source_key="expansion_geom:0003", authoring_source="human", content_format="plain"),

        Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.4,
            text_ar="The diagram shows two parallel lines crossed by a transversal. Find angle x.",
            figure_svg=_svg(
                '<line x1="20" y1="40" x2="200" y2="40" class="line"/>'
                '<line x1="20" y1="100" x2="200" y2="100" class="line"/>'
                '<line x1="60" y1="10" x2="160" y2="130" class="line-thin"/>'
                '<text x="125" y="95" class="label">x</text>'
                '<text x="85" y="35" class="label">65</text>'
            ),
            figure_alt="Two parallel lines cut by a transversal with one angle marked 65 degrees.",
            option_a="25", option_b="65", option_c="115", option_d="180",
            correct_option="c",
            explanation_ar="The marked angle (65) and angle x are co-interior (same-side interior) angles. They add up to 180. So x = 180 - 65 = 115.\n\nWhy other options are wrong:\n- 25: Random subtraction\n- 65: That would be alternate angles (wrong position)\n- 180: Sum of co-interior, not the angle itself",
            solution_steps_ar=_steps("Identify angle relationship: co-interior angles.", "Co-interior angles sum to 180.", "x = 180 - 65 = 115."),
            tags="angles,parallel-lines,figure", stage="building",
            rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5,
            rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86,
            source_key="expansion_geom:0004", authoring_source="human", content_format="plain"),

        Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.5,
            text_ar="A trapezoid has parallel sides of 8 cm and 12 cm, with height 5 cm. What is its area?",
            figure_svg=_svg(
                '<path d="M50 100 L170 100 L140 30 L80 30 Z" class="shape-warm"/>'
                '<text x="110" y="120" text-anchor="middle" class="label">12 cm</text>'
                '<text x="110" y="22" text-anchor="middle" class="label">8 cm</text>'
                '<line x1="110" y1="30" x2="110" y2="100" class="line-dash"/>'
                '<text x="118" y="70" class="label">5 cm</text>'
            ),
            figure_alt="A trapezoid with parallel sides 8 cm and 12 cm, and height 5 cm.",
            option_a="40 cm", option_b="50 cm", option_c="60 cm", option_d="100 cm",
            correct_option="b",
            explanation_ar="Trapezoid area = (1/2) x (sum of parallel sides) x height = (1/2) x (8+12) x 5 = (1/2) x 20 x 5 = 50.\n\nWhy other options are wrong:\n- 40 cm: Used only one parallel side (8 x 5)\n- 60 cm: Used only one parallel side (12 x 5)\n- 100 cm: Forgot to divide by 2",
            solution_steps_ar=_steps("Sum parallel sides: 8 + 12 = 20.", "Multiply by height: 20 x 5 = 100.", "Divide by 2: 100 / 2 = 50."),
            tags="trapezoid,area,figure", stage="building",
            rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5,
            rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71,
            source_key="expansion_geom:0005", authoring_source="human", content_format="plain"),

        Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.5,
            text_ar="The diagram shows a right triangle. What is the length of the hypotenuse?",
            figure_svg=_svg(
                '<path d="M40 110 L40 30 L170 110 Z" class="shape-alt"/>'
                '<path d="M40 95 L55 95 L55 110" fill="none" class="line-thin"/>'
                '<text x="22" y="74" class="label">6</text>'
                '<text x="100" y="128" class="label">8</text>'
                '<text x="110" y="60" class="label">?</text>'
            ),
            figure_alt="Right triangle with legs 6 and 8.",
            option_a="7", option_b="10", option_c="12", option_d="14",
            correct_option="b",
            explanation_ar="By the Pythagorean theorem: c = sqrt(6^2 + 8^2) = sqrt(36 + 64) = sqrt(100) = 10.\n\nWhy other options are wrong:\n- 7: Sum of digits in the legs\n- 12: Added the legs directly\n- 14: Common error",
            solution_steps_ar=_steps("Use c^2 = a^2 + b^2.", "c^2 = 36 + 64 = 100.", "c = 10."),
            tags="triangle,pythagorean,figure", stage="building",
            rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5,
            rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71,
            source_key="expansion_geom:0006", authoring_source="human", content_format="plain"),

        # ── Hard (0.7-0.8) ──
        Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.7,
            text_ar="Find the shaded area between the square and the inscribed circle.",
            figure_svg=_svg(
                '<rect x="40" y="10" width="120" height="120" class="shape"/>'
                '<circle cx="100" cy="70" r="60" class="shape-warm"/>'
                '<text x="100" y="138" text-anchor="middle" class="label">12 cm</text>',
                "0 0 220 150"
            ),
            figure_alt="A square with side 12 cm containing an inscribed circle.",
            option_a="30.9 cm", option_b="31.0 cm", option_c="144 cm", option_d="113.1 cm",
            correct_option="a",
            explanation_ar="Square area = 12^2 = 144. Circle radius = 12/2 = 6. Circle area = pi x 6^2 = 113.1. Shaded = 144 - 113.1 = 30.9.\n\nWhy other options are wrong:\n- 31.0: Rounding error\n- 144 cm: That is the square area, not the shaded region\n- 113.1 cm: That is the circle area",
            solution_steps_ar=_steps("Square area = 12^2 = 144.", "Radius = 12/2 = 6, circle area = pi x 36 = 113.1.", "Shaded = 144 - 113.1 = 30.9."),
            tags="composite,area,figure", stage="peak",
            rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5,
            rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0,
            source_key="expansion_geom:0007", authoring_source="human", content_format="plain"),

        Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.7,
            text_ar="The diagram shows a semicircle on top of a rectangle. Find the total perimeter.",
            figure_svg=_svg(
                '<rect x="40" y="50" width="140" height="70" class="shape-cyan"/>'
                '<path d="M40 50 A70 70 0 0 1 180 50" class="shape-warm" fill-opacity="0.5"/>'
                '<text x="110" y="128" text-anchor="middle" class="label">14 cm</text>'
                '<text x="186" y="90" class="label">6 cm</text>',
                "0 0 220 140"
            ),
            figure_alt="Rectangle 14 cm by 6 cm with a semicircle on top (diameter = 14 cm).",
            option_a="32 cm", option_b="40 cm", option_c="48 cm", option_d="54 cm",
            correct_option="c",
            explanation_ar="Perimeter = bottom (14) + two sides (6+6) + semicircle arc (pi x d/2 = pi x 7 = 22). Total = 14 + 12 + 22 = 48 cm.\n\nWhy other options are wrong:\n- 32 cm: Forgot the semicircle\n- 40 cm: Used wrong semicircle formula\n- 54 cm: Added the top straight edge too",
            solution_steps_ar=_steps("Bottom = 14, sides = 6 + 6 = 12.", "Semicircle arc = pi x r = pi x 7 = 22.", "Total = 14 + 12 + 22 = 48."),
            tags="composite,perimeter,figure", stage="peak",
            rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5,
            rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0,
            source_key="expansion_geom:0008", authoring_source="human", content_format="plain"),

        Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.8,
            text_ar="In the figure, triangle ABC has AB = 13, BC = 14, and height from A to BC = 12. Find the area.",
            figure_svg=_svg(
                '<path d="M30 110 L190 110 L80 20 Z" class="shape-green"/>'
                '<line x1="80" y1="20" x2="80" y2="110" class="line-dash"/>'
                '<text x="50" y="60" class="label">13</text>'
                '<text x="110" y="128" class="label">14</text>'
                '<text x="86" y="70" class="label">12</text>'
            ),
            figure_alt="Triangle with base 14, side 13, and height 12.",
            option_a="78", option_b="84", option_c="91", option_d="168",
            correct_option="b",
            explanation_ar="Area = (1/2) x base x height = (1/2) x 14 x 12 = 84.\n\nWhy other options are wrong:\n- 78: Used 13 as base instead of 14\n- 91: Used (1/2) x 13 x 14\n- 168: Forgot to divide by 2",
            solution_steps_ar=_steps("Base = BC = 14, height = 12.", "Area = (1/2) x 14 x 12.", "Area = 84."),
            tags="triangle,area,figure", stage="peak",
            rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5,
            rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86,
            source_key="expansion_geom:0009", authoring_source="human", content_format="plain"),

        Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.8,
            text_ar="The diagram shows a rhombus with diagonals 10 cm and 24 cm. What is its area?",
            figure_svg=_svg(
                '<path d="M110 10 L200 70 L110 130 L20 70 Z" class="shape-alt"/>'
                '<line x1="20" y1="70" x2="200" y2="70" class="line-dash"/>'
                '<line x1="110" y1="10" x2="110" y2="130" class="line-dash"/>'
                '<text x="110" y="6" text-anchor="middle" class="label">24</text>'
                '<text x="152" y="64" class="label">10</text>'
            ),
            figure_alt="Rhombus with diagonals 10 cm and 24 cm.",
            option_a="34 cm", option_b="68 cm", option_c="120 cm", option_d="240 cm",
            correct_option="c",
            explanation_ar="Area of a rhombus = (1/2) x d1 x d2 = (1/2) x 10 x 24 = 120.\n\nWhy other options are wrong:\n- 34 cm: Sum of diagonals\n- 68 cm: Perimeter calculation\n- 240 cm: Forgot to divide by 2",
            solution_steps_ar=_steps("Use rhombus area = (1/2) x d1 x d2.", "(1/2) x 10 x 24.", "Area = 120 cm."),
            tags="rhombus,area,figure", stage="peak",
            rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5,
            rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86,
            source_key="expansion_geom:0010", authoring_source="human", content_format="plain"),
    ]


def get_statistics_questions() -> list[Question]:
    return [
        # ── Easy (0.2-0.3) ──
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.2,
            text_ar="Use the table to find the total number of students.",
            table_ar={"headers": ["Class", "Students"], "rows": [["A", "25"], ["B", "30"], ["C", "20"]]},
            table_caption="Number of students per class.",
            option_a="55", option_b="65", option_c="75", option_d="80",
            correct_option="c",
            explanation_ar="Add all values: 25 + 30 + 20 = 75.\n\nWhy other options are wrong:\n- 55: Missed class B\n- 65: Subtraction error\n- 80: Added extra value",
            solution_steps_ar=_steps("Sum the Students column.", "25 + 30 + 20 = 75.", "Total = 75."),
            tags="sum,table", stage="foundation",
            rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5,
            rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71,
            source_key="expansion_stat:0001", authoring_source="human", content_format="plain"),

        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.3,
            text_ar="From the frequency table, what is the mode?",
            table_ar={"headers": ["Value", "Frequency"], "rows": [["2", "3"], ["4", "5"], ["6", "2"], ["8", "4"]]},
            table_caption="Frequency distribution of values.",
            option_a="2", option_b="4", option_c="6", option_d="8",
            correct_option="b",
            explanation_ar="The mode is the value with the highest frequency. Value 4 has frequency 5 (the highest).\n\nWhy other options are wrong:\n- 2: Frequency is only 3\n- 6: Frequency is only 2 (lowest)\n- 8: Frequency is 4 (second highest)",
            solution_steps_ar=_steps("Read frequencies: 3, 5, 2, 4.", "Highest frequency is 5.", "Value with frequency 5 is 4."),
            tags="mode,table", stage="foundation",
            rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5,
            rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71,
            source_key="expansion_stat:0002", authoring_source="human", content_format="plain"),

        # ── Medium (0.4-0.6) ──
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.4,
            text_ar="Calculate the mean from the grouped frequency table.",
            table_ar={"headers": ["Score", "Frequency"], "rows": [["10", "2"], ["20", "3"], ["30", "4"], ["40", "1"]]},
            table_caption="Scores and their frequencies.",
            option_a="22", option_b="24", option_c="25", option_d="30",
            correct_option="b",
            explanation_ar="Mean = sum of (value x freq) / total freq = (10x2 + 20x3 + 30x4 + 40x1) / (2+3+4+1) = (20+60+120+40)/10 = 240/10 = 24.\n\nWhy other options are wrong:\n- 22: Calculation error\n- 25: Simple average of values without frequency\n- 30: Modal class",
            solution_steps_ar=_steps("Multiply each value by frequency.", "Sum products: 20+60+120+40 = 240.", "Total frequency: 10. Mean = 240/10 = 24."),
            tags="mean,frequency,table", stage="building",
            rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5,
            rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57,
            source_key="expansion_stat:0003", authoring_source="human", content_format="plain"),

        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.5,
            text_ar="The table shows test scores. What is the median?",
            table_ar={"headers": ["Student", "Score"], "rows": [["A", "72"], ["B", "85"], ["C", "68"], ["D", "91"], ["E", "77"], ["F", "83"]]},
            table_caption="Test scores of 6 students.",
            option_a="77", option_b="79", option_c="80", option_d="83",
            correct_option="c",
            explanation_ar="Sort scores: 68, 72, 77, 83, 85, 91. With 6 values, median = average of 3rd and 4th = (77+83)/2 = 80.\n\nWhy other options are wrong:\n- 77: Only the 3rd value, not the median of even count\n- 79: Random average\n- 83: Only the 4th value",
            solution_steps_ar=_steps("Sort: 68, 72, 77, 83, 85, 91.", "Even count: average middle two.", "Median = (77+83)/2 = 80."),
            tags="median,table", stage="building",
            rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5,
            rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86,
            source_key="expansion_stat:0004", authoring_source="human", content_format="plain"),

        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.6,
            text_ar="Use the two-way table to find P(Male AND Passed).",
            table_ar={"headers": ["Gender", "Passed", "Failed", "Total"], "rows": [["Male", "30", "10", "40"], ["Female", "25", "15", "40"], ["Total", "55", "25", "80"]]},
            table_caption="Pass/Fail results by gender.",
            option_a="3/8", option_b="30/55", option_c="30/40", option_d="55/80",
            correct_option="a",
            explanation_ar="P(Male AND Passed) = 30/80 = 3/8.\n\nWhy other options are wrong:\n- 30/55: P(Male | Passed) — conditional probability\n- 30/40: P(Passed | Male) — conditional probability\n- 55/80: P(Passed) — marginal probability",
            solution_steps_ar=_steps("Find Male AND Passed cell: 30.", "Total: 80.", "P = 30/80 = 3/8."),
            tags="probability,two-way-table", stage="building",
            rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5,
            rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0,
            source_key="expansion_stat:0005", authoring_source="human", content_format="plain"),

        # ── Hard (0.7-0.8) ──
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.7,
            text_ar="The table shows sales data. Calculate the standard deviation.",
            table_ar={"headers": ["Day", "Sales"], "rows": [["Mon", "10"], ["Tue", "20"], ["Wed", "30"], ["Thu", "20"], ["Fri", "20"]]},
            table_caption="Daily sales for one week.",
            option_a="5.0", option_b="6.3", option_c="7.1", option_d="10.0",
            correct_option="b",
            explanation_ar="Mean = 100/5 = 20. Deviations: -10, 0, 10, 0, 0. Squared: 100, 0, 100, 0, 0. Variance = 200/5 = 40. SD = sqrt(40) = 6.3.\n\nWhy other options are wrong:\n- 5.0: Used wrong formula\n- 7.1: Used sample variance (n-1)\n- 10.0: This is the range / 2",
            solution_steps_ar=_steps("Mean = 100/5 = 20.", "Squared deviations sum = 200.", "Variance = 40, SD = sqrt(40) = 6.3."),
            tags="standard-deviation,table", stage="peak",
            rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5,
            rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0,
            source_key="expansion_stat:0006", authoring_source="human", content_format="plain"),

        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.8,
            text_ar="From the cumulative frequency table, estimate the median class.",
            table_ar={"headers": ["Class", "Frequency", "Cumulative"], "rows": [["0-10", "5", "5"], ["10-20", "8", "13"], ["20-30", "12", "25"], ["30-40", "10", "35"], ["40-50", "5", "40"]]},
            table_caption="Cumulative frequency distribution.",
            option_a="10-20", option_b="20-30", option_c="30-40", option_d="40-50",
            correct_option="b",
            explanation_ar="Total = 40. Median position = 40/2 = 20th value. Looking at cumulative: 5, 13, 25... The 20th value falls in the 20-30 class.\n\nWhy other options are wrong:\n- 10-20: Cumulative only reaches 13\n- 30-40: Goes past the median position\n- 40-50: Last class",
            solution_steps_ar=_steps("Total frequency = 40.", "Median position = 20th value.", "Cumulative reaches 25 at class 20-30, so median is in 20-30."),
            tags="median,cumulative-frequency,table", stage="peak",
            rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5,
            rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0,
            source_key="expansion_stat:0007", authoring_source="human", content_format="plain"),
    ]


def get_comparison_questions() -> list[Question]:
    return [
        Question(skill_id="quant_algebra", question_type="comparison", difficulty=0.4,
            text_ar="Compare the two expressions using the table.",
            table_ar={"headers": ["Column", "Expression"], "rows": [["A", "3x + 5 when x = 4"], ["B", "2x + 10 when x = 4"]]},
            table_caption="Compare two algebraic expressions at x = 4.",
            option_a="Column (A) is greater", option_b="Column (B) is greater",
            option_c="The two values are equal", option_d="The relationship cannot be determined",
            correct_option="b",
            explanation_ar="A = 3(4) + 5 = 17. B = 2(4) + 10 = 18. Column B is greater.\n\nWhy other options are wrong:\n- Column A is greater: 17 < 18\n- Equal: 17 is not 18\n- Cannot be determined: Both are definite values",
            solution_steps_ar=_steps("Column A: 3(4) + 5 = 17.", "Column B: 2(4) + 10 = 18.", "18 > 17, Column B is greater."),
            tags="comparison,algebra,table", stage="building",
            rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5,
            rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57,
            source_key="expansion_comp:0001", authoring_source="human", content_format="plain"),

        Question(skill_id="quant_arithmetic", question_type="comparison", difficulty=0.3,
            text_ar="Compare the two values in the table.",
            table_ar={"headers": ["Column", "Value"], "rows": [["A", "3/4 of 80"], ["B", "2/5 of 150"]]},
            table_caption="Fraction comparison.",
            option_a="Column (A) is greater", option_b="Column (B) is greater",
            option_c="The two values are equal", option_d="The relationship cannot be determined",
            correct_option="c",
            explanation_ar="A = (3/4) x 80 = 60. B = (2/5) x 150 = 60. The two values are equal.\n\nWhy other options are wrong:\n- Column A is greater: Both are 60\n- Column B is greater: Both are 60\n- Cannot be determined: Both are definite values",
            solution_steps_ar=_steps("Column A: (3/4) x 80 = 60.", "Column B: (2/5) x 150 = 60.", "60 = 60, they are equal."),
            tags="comparison,fractions,table", stage="foundation",
            rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5,
            rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71,
            source_key="expansion_comp:0002", authoring_source="human", content_format="plain"),

        Question(skill_id="quant_statistics", question_type="comparison", difficulty=0.5,
            text_ar="Compare the mean and median using the data table.",
            table_ar={"headers": ["Value"], "rows": [["2"], ["3"], ["3"], ["5"], ["100"]]},
            table_caption="A data set with one outlier.",
            option_a="Mean is greater", option_b="Median is greater",
            option_c="They are equal", option_d="Cannot be determined",
            correct_option="a",
            explanation_ar="Mean = (2+3+3+5+100)/5 = 113/5 = 22.6. Median = 3 (middle value when sorted). Mean (22.6) > Median (3).\n\nThe outlier (100) pulls the mean much higher than the median.",
            solution_steps_ar=_steps("Mean = 113/5 = 22.6.", "Sorted: 2, 3, 3, 5, 100. Median = 3.", "22.6 > 3, mean is greater."),
            tags="comparison,mean,median,table", stage="building",
            rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5,
            rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0,
            source_key="expansion_comp:0003", authoring_source="human", content_format="plain"),

        Question(skill_id="quant_geometry", question_type="comparison", difficulty=0.6,
            text_ar="Compare the two areas described in the table.",
            table_ar={"headers": ["Column", "Shape"], "rows": [["A", "Circle with radius 5"], ["B", "Square with side 9"]]},
            table_caption="Compare areas of a circle and a square.",
            option_a="Circle area is greater", option_b="Square area is greater",
            option_c="They are equal", option_d="Cannot be determined",
            correct_option="b",
            explanation_ar="Circle area = pi x 5^2 = 25pi = 78.5. Square area = 9^2 = 81. Square is greater (81 > 78.5).\n\nWhy other options are wrong:\n- Circle is greater: 78.5 < 81\n- They are equal: Different values\n- Cannot be determined: Both are computable",
            solution_steps_ar=_steps("Circle: pi x 25 = 78.5.", "Square: 81.", "81 > 78.5, square is greater."),
            tags="comparison,area,table", stage="building",
            rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5,
            rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0,
            source_key="expansion_comp:0004", authoring_source="human", content_format="plain"),

        Question(skill_id="quant_algebra", question_type="comparison", difficulty=0.7,
            text_ar="Compare the two quantities for all positive values of x.",
            table_ar={"headers": ["Column", "Expression"], "rows": [["A", "x^2 + 1"], ["B", "2x"]]},
            table_caption="Compare expressions for positive x.",
            option_a="Column A is always greater", option_b="Column B is always greater",
            option_c="They are always equal", option_d="The relationship cannot be determined",
            correct_option="d",
            explanation_ar="At x=1: A=2, B=2 (equal). At x=3: A=10, B=6 (A>B). At x=0.5: A=1.25, B=1 (A>B). But at x=1 they are equal, so the relationship depends on x.\n\nWhy other options are wrong:\n- A always greater: Equal at x=1\n- B always greater: A > B at x=3\n- Always equal: Only equal at x=1",
            solution_steps_ar=_steps("Test x=1: A=2, B=2 (equal).", "Test x=3: A=10, B=6 (A>B).", "Relationship changes, cannot be determined."),
            tags="comparison,algebra,table", stage="peak",
            rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5,
            rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0,
            source_key="expansion_comp:0005", authoring_source="human", content_format="plain"),
    ]


def get_all_expansion_questions() -> list[Question]:
    """Return all Phase 5 expansion questions."""
    return get_geometry_questions() + get_statistics_questions() + get_comparison_questions()
