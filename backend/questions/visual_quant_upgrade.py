import json

from models import Question


def _steps(*items: str) -> str:
    return json.dumps(list(items))


def _find_by_key(questions: list[Question], source_key: str) -> Question:
    for question in questions:
        if getattr(question, "source_key", None) == source_key:
            return question
    raise ValueError(f"Could not find question with source_key: {source_key}")


def _find_question(questions: list[Question], skill_id: str, prefix: str) -> Question:
    for question in questions:
        if question.skill_id == skill_id and question.text_ar.startswith(prefix):
            return question
    raise ValueError(f"Could not find seeded question for {skill_id}: {prefix}")


def _find_question_containing(questions: list[Question], skill_id: str, fragment: str) -> Question:
    for question in questions:
        if question.skill_id == skill_id and fragment in question.text_ar:
            return question
    raise ValueError(f"Could not find seeded question for {skill_id} containing: {fragment}")


def _apply_updates(question: Question, **updates) -> None:
    for field, value in updates.items():
        setattr(question, field, value)


_SVG_STYLE = (
    '<style>'
    '.shape{fill:#dbeafe;stroke:#1e293b;stroke-width:3}'
    '.shape-alt{fill:#e0e7ff;stroke:#1e293b;stroke-width:3}'
    '.shape-warm{fill:#fef3c7;stroke:#1e293b;stroke-width:3}'
    '.shape-green{fill:#dcfce7;stroke:#1e293b;stroke-width:3}'
    '.shape-red{fill:#fee2e2;stroke:#1e293b;stroke-width:3}'
    '.shape-purple{fill:#ede9fe;stroke:#1e293b;stroke-width:3}'
    '.shape-cyan{fill:#cffafe;stroke:#1e293b;stroke-width:3}'
    '.shape-pink{fill:#fce7f3;stroke:#1e293b;stroke-width:3}'
    '.shape-white{fill:#ffffff;stroke:#1e293b;stroke-width:3}'
    '.shape-highlight{fill:#bfdbfe;stroke:#1e293b;stroke-width:2}'
    '.shape-highlight-pink{fill:#fecdd3;stroke:#1e293b;stroke-width:2}'
    '.line{stroke:#1e293b;stroke-width:3}'
    '.line-thin{stroke:#1e293b;stroke-width:2}'
    '.line-dash{stroke:#1e293b;stroke-width:2;stroke-dasharray:6 4}'
    '.label{font-size:14px;font-family:Arial,sans-serif;fill:#1e293b}'
    '.right-angle{fill:none;stroke:#1e293b;stroke-width:2}'
    '</style>'
)


def _svg(content: str, view_box: str = "0 0 220 140") -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{view_box}" '
        'width="220" height="140" preserveAspectRatio="xMidYMid meet">'
        f"{_SVG_STYLE}{content}</svg>"
    )


def _revise_geometry_questions(questions: list[Question]) -> int:
    revised = 0

    q = _find_by_key(questions, "quant_geometry:0001")
    _apply_updates(
        q,
        text_ar="The diagram shows a rectangle. What is its area?",
        figure_svg=_svg(
            '<rect x="35" y="30" width="150" height="80" class="shape"/>'
            '<text x="110" y="20" text-anchor="middle" class="label">8 cm</text>'
            '<text x="192" y="75" class="label">5 cm</text>'
        ),
        explanation_ar="From the diagram, the rectangle has length 8 cm and width 5 cm. Area = length x width = 8 x 5 = 40 square cm.",
        solution_steps_ar=_steps("Read the two side lengths from the diagram: 8 cm and 5 cm.", "Use rectangle area = length x width.", "8 x 5 = 40."),
        tags="rectangle,figure",
    )
    revised += 1

    q = _find_by_key(questions, "quant_geometry:0002")
    _apply_updates(
        q,
        text_ar="The diagram shows a right triangle with side lengths 3 cm and 4 cm. What is the hypotenuse?",
        figure_svg=_svg(
            '<path d="M40 105 L40 35 L150 105 Z" class="shape-green"/>'
            '<path d="M40 90 L55 90 L55 105" fill="none" class="line-thin"/>'
            '<text x="18" y="72" class="label">3 cm</text>'
            '<text x="88" y="126" class="label">4 cm</text>'
            '<text x="100" y="58" class="label">?</text>'
        ),
        explanation_ar="The diagram gives the two legs of a right triangle: 3 cm and 4 cm. By the Pythagorean theorem, $c^2 = 3^2 + 4^2 = 9 + 16 = 25$, so $c = 5$.",
        solution_steps_ar=_steps("Use $c^2 = a^2 + b^2$.", "$c^2 = 3^2 + 4^2 = 25$.", "$c = 5$."),
        tags="triangle,pythagorean,figure",
    )
    revised += 1

    q = _find_by_key(questions, "quant_geometry:0003")
    _apply_updates(
        q,
        text_ar="The diagram shows a circle with radius 7 cm. What is its circumference? (Use pi = 22/7.)",
        figure_svg=_svg(
            '<circle cx="95" cy="70" r="44" class="shape-warm"/>'
            '<line x1="95" y1="70" x2="139" y2="70" class="line"/>'
            '<text x="110" y="62" text-anchor="middle" class="label">7 cm</text>'
        ),
        explanation_ar="The radius shown is 7 cm. Circumference = $2 \\times \\pi \\times r = 2 \\times \\frac{22}{7} \\times 7 = 44$ cm.",
        solution_steps_ar=_steps("Use circumference = $2\\pi r$.", "Substitute $r = 7$ and $\\pi = \\frac{22}{7}$.", "$2 \\times 22 = 44$."),
        tags="circle,circumference,figure",
    )
    revised += 1

    q = _find_by_key(questions, "quant_geometry:0004")
    _apply_updates(
        q,
        text_ar="A square is shown with total perimeter 24 cm. What is its area?",
        figure_svg=_svg(
            '<rect x="55" y="25" width="90" height="90" class="shape-purple"/>'
            '<text x="100" y="18" text-anchor="middle" class="label">Perimeter = 24 cm</text>'
            '<text x="154" y="74" class="label">side = ?</text>'
        ),
        explanation_ar="A square has 4 equal sides, so each side is 24 / 4 = 6 cm. Area = side^2 = 6 x 6 = 36 square cm.",
        solution_steps_ar=_steps("Find one side: 24 / 4 = 6.", "Use square area = side x side.", "6 x 6 = 36."),
        tags="square,area,figure",
    )
    revised += 1

    q = _find_by_key(questions, "quant_geometry:0006")
    _apply_updates(
        q,
        text_ar="The diagram shows a triangle with base 10 cm and height 6 cm. What is its area?",
        figure_svg=_svg(
            '<path d="M35 110 L180 110 L80 35 Z" class="shape-red"/>'
            '<line x1="80" y1="35" x2="80" y2="110" class="line-dash"/>'
            '<text x="102" y="126" class="label">10 cm</text>'
            '<text x="84" y="74" class="label">6 cm</text>'
        ),
        explanation_ar="Use triangle area = $\\frac{1}{2} \\times$ base $\\times$ height. From the diagram, area = $\\frac{1}{2} \\times 10 \\times 6 = 30$ square cm.",
        solution_steps_ar=_steps("Read base = 10 cm and height = 6 cm.", "Apply triangle area = $\\frac{1}{2} \\times$ base $\\times$ height.", "Area = 30."),
        tags="triangle,area,figure",
    )
    revised += 1

    q = _find_by_key(questions, "quant_geometry:0007")
    _apply_updates(
        q,
        text_ar="The rectangle in the diagram has side lengths 12 cm and 4 cm. What is its perimeter?",
        figure_svg=_svg(
            '<rect x="30" y="38" width="160" height="64" class="shape-cyan"/>'
            '<text x="110" y="28" text-anchor="middle" class="label">12 cm</text>'
            '<text x="194" y="74" class="label">4 cm</text>'
        ),
        explanation_ar="Perimeter of a rectangle is 2 x (length + width). With 12 cm and 4 cm, perimeter = 2 x (12 + 4) = 32 cm.",
        solution_steps_ar=_steps("Add the two side lengths: 12 + 4 = 16.", "Double the sum for perimeter.", "2 x 16 = 32."),
        tags="rectangle,perimeter,figure",
    )
    revised += 1

    q = _find_by_key(questions, "quant_geometry:0008")
    _apply_updates(
        q,
        text_ar="The diagram shows a circle with radius 14 cm. What is its area? (Use pi = 22/7.)",
        figure_svg=_svg(
            '<circle cx="95" cy="72" r="46" class="shape-warm"/>'
            '<line x1="95" y1="72" x2="141" y2="72" class="line"/>'
            '<text x="112" y="64" text-anchor="middle" class="label">14 cm</text>'
        ),
        explanation_ar="Area = $\\pi r^2 = \\frac{22}{7} \\times 14^2 = \\frac{22}{7} \\times 196 = 616$ square cm.",
        solution_steps_ar=_steps("Use area = $\\pi r^2$.", "Square the radius: $14^2 = 196$.", "Multiply by $\\frac{22}{7}$ to get 616."),
        tags="circle,area,figure",
    )
    revised += 1

    q = _find_by_key(questions, "quant_geometry:0011")
    _apply_updates(
        q,
        text_ar="The right triangle shows hypotenuse 13 cm and one leg 5 cm. Find the missing leg.",
        figure_svg=_svg(
            '<path d="M40 105 L40 45 L150 105 Z" class="shape-alt"/>'
            '<path d="M40 90 L55 90 L55 105" fill="none" class="line-thin"/>'
            '<text x="14" y="78" class="label">5 cm</text>'
            '<text x="94" y="52" class="label">13 cm</text>'
            '<text x="88" y="126" class="label">?</text>'
        ),
        explanation_ar="Use the Pythagorean theorem. The missing leg satisfies x^2 = 13^2 - 5^2 = 169 - 25 = 144, so x = 12 cm.",
        solution_steps_ar=_steps("Use x^2 = 13^2 - 5^2.", "x^2 = 169 - 25 = 144.", "x = 12."),
        tags="triangle,pythagorean,figure",
    )
    revised += 1

    return revised


def _revise_statistics_questions(questions: list[Question]) -> int:
    revised = 0

    q = _find_by_key(questions, "quant_statistics:0001")
    _apply_updates(
        q,
        text_ar="Use the table to find the arithmetic mean of the four scores.",
        table_ar={"headers": ["Student", "Score"], "rows": [["A", "70"], ["B", "80"], ["C", "90"], ["D", "60"]]},
        explanation_ar="Add the four scores from the table: 70 + 80 + 90 + 60 = 300. Divide by 4 students, so the mean is 75.",
        solution_steps_ar=_steps("Sum the scores in the table to get 300.", "Count 4 scores.", "300 / 4 = 75."),
        tags="mean,table",
    )
    revised += 1

    q = _find_by_key(questions, "quant_statistics:0002")
    _apply_updates(
        q,
        text_ar="The table lists quiz scores and their frequencies. What is the mode?",
        table_ar={
            "headers": ["Score", "Frequency"],
            "rows": [["5", "1"], ["6", "1"], ["7", "3"], ["8", "2"], ["9", "1"]],
        },
        explanation_ar="The mode is the score with the highest frequency in the table. Score 7 appears 3 times, more than any other value.",
        solution_steps_ar=_steps("Read the frequency column.", "Identify the largest frequency: 3.", "The score with frequency 3 is 7."),
        tags="mode,table",
    )
    revised += 1

    q = _find_by_key(questions, "quant_statistics:0012")
    _apply_updates(
        q,
        text_ar="Use the values in the table to find the median.",
        table_ar={"headers": ["Value"], "rows": [["3"], ["7"], ["2"], ["9"], ["5"]]},
        explanation_ar="Order the values from the table: 2, 3, 5, 7, 9. With 5 values, the middle one is 5.",
        solution_steps_ar=_steps("Sort the listed values.", "There are 5 values, so choose the middle one.", "The median is 5."),
        tags="median,table",
    )
    revised += 1

    q = _find_by_key(questions, "quant_statistics:0013")
    _apply_updates(
        q,
        text_ar="Use the table to find the range of the data set.",
        table_ar={"headers": ["Value"], "rows": [["15"], ["8"], ["23"], ["11"], ["4"]]},
        explanation_ar="From the table, the maximum value is 23 and the minimum is 4. Range = 23 - 4 = 19.",
        solution_steps_ar=_steps("Find the largest and smallest values in the table.", "Largest = 23 and smallest = 4.", "23 - 4 = 19."),
        tags="range,table",
    )
    revised += 1

    q = _find_by_key(questions, "quant_statistics:0014")
    _apply_updates(
        q,
        text_ar="The table summarizes the class. What is the probability of selecting a football player?",
        table_ar={
            "headers": ["Category", "Count"],
            "rows": [["Football players", "12"], ["Other students", "18"], ["Total students", "30"]],
        },
        explanation_ar="Probability = favorable outcomes / total outcomes. The table shows 12 football players out of 30 students, so 12/30 = 2/5.",
        solution_steps_ar=_steps("Use football players as the favorable count: 12.", "Use total students as the denominator: 30.", "12/30 simplifies to 2/5."),
        tags="probability,table",
    )
    revised += 1

    q = _find_by_key(questions, "quant_statistics:0015")
    _apply_updates(
        q,
        text_ar="A school has the five students listed in the table. How many different 2-student teams can be formed?",
        table_ar={"headers": ["Student"], "rows": [["A"], ["B"], ["C"], ["D"], ["E"]]},
        explanation_ar="The order does not matter, so use combinations: C(5,2) = 5! / (2! x 3!) = 10.",
        solution_steps_ar=_steps("Choose 2 from 5 without order.", "Use combinations: C(5,2).", "C(5,2) = 10."),
        tags="combination,table",
    )
    revised += 1

    q = _find_by_key(questions, "quant_statistics:0016")
    _apply_updates(
        q,
        text_ar="Use the weighted-score table to find the weighted average.",
        table_ar={
            "headers": ["Subject", "Score", "Weight"],
            "rows": [["Subject 1", "80", "3"], ["Subject 2", "90", "2"]],
        },
        explanation_ar="Weighted average = (80 x 3 + 90 x 2) / (3 + 2) = (240 + 180) / 5 = 84.",
        solution_steps_ar=_steps("Multiply each score by its weight.", "Add weighted scores: 240 + 180 = 420.", "Divide by total weight 5 to get 84."),
        tags="mean,weighted-average,table",
    )
    revised += 1

    return revised


def _revise_arithmetic_questions(questions: list[Question]) -> int:
    revised = 0

    q = _find_by_key(questions, "quant_arithmetic:0001")
    _apply_updates(
        q,
        text_ar="Use the table to find the final amount paid after the discount.",
        table_ar={"headers": ["Item", "Value"], "rows": [["Original price", "120"], ["Discount", "25%"]]},
        explanation_ar="The table shows an original price of 120 and a discount of 25%. Discount value = 120 x 0.25 = 30, so the amount paid is 120 - 30 = 90.",
        solution_steps_ar=_steps("Find 25% of 120 to get the discount.", "Discount = 30.", "Subtract 30 from 120 to get 90."),
        tags="percentage,discount,table",
    )
    revised += 1

    q = _find_by_key(questions, "quant_arithmetic:0002")
    _apply_updates(
        q,
        text_ar="The class information is summarized in the table. How many girls are there?",
        table_ar={
            "headers": ["Item", "Value"],
            "rows": [["Boys : Girls", "3 : 2"], ["Total students", "35"]],
        },
        explanation_ar="The ratio has 5 total parts. Girls take 2 of those 5 parts, so girls = (2/5) x 35 = 14.",
        solution_steps_ar=_steps("Add ratio parts: 3 + 2 = 5.", "Girls take 2 of the 5 parts.", "Compute (2/5) x 35 = 14."),
        tags="ratio,table",
    )
    revised += 1

    q = _find_by_key(questions, "quant_arithmetic:0005")
    _apply_updates(
        q,
        text_ar="Use the summary table to find the new average after one more student joins.",
        table_ar={
            "headers": ["Item", "Value"],
            "rows": [["Current students", "5"], ["Current average", "80"], ["New score", "92"]],
        },
        explanation_ar="Current total = 5 x 80 = 400. Add the new score to get 492, then divide by 6 students, giving a new average of 82.",
        solution_steps_ar=_steps("Convert the old average into a total: 5 x 80 = 400.", "Add the new score: 400 + 92 = 492.", "Divide by 6 to get 82."),
        tags="average,table",
    )
    revised += 1

    q = _find_by_key(questions, "quant_arithmetic:0007")
    _apply_updates(
        q,
        text_ar="Use the comparison table, then choose the correct relationship.",
        table_ar={
            "headers": ["Column", "Expression"],
            "rows": [["A", "25% of 200"], ["B", "50% of 100"]],
        },
        explanation_ar="Column A = 0.25 x 200 = 50 and Column B = 0.50 x 100 = 50. The two values are equal.",
        solution_steps_ar=_steps("Compute Column A: 50.", "Compute Column B: 50.", "Since both are 50, the values are equal."),
        tags="comparison,percentage,table",
    )
    revised += 1

    q = _find_by_key(questions, "quant_arithmetic:0015")
    _apply_updates(
        q,
        text_ar="Use the comparison table, then choose the correct relationship.",
        table_ar={
            "headers": ["Column", "Value"],
            "rows": [["A", "Average of 4, 6, 8, 10"], ["B", "7.5"]],
        },
        explanation_ar="Column A has average (4 + 6 + 8 + 10) / 4 = 28 / 4 = 7. Column B is 7.5, so Column B is greater.",
        solution_steps_ar=_steps("Find Column A average: 28 / 4 = 7.", "Read Column B: 7.5.", "Because 7 < 7.5, Column B is greater."),
        tags="comparison,average,table",
    )
    revised += 1

    return revised


def _new_geometry_questions() -> list[Question]:
    return [
        Question(
            skill_id="quant_geometry",
            question_type="geometry",
            difficulty=0.45,
            text_ar="The diagram shows a parallelogram. What is its area?",
            figure_svg=_svg(
                '<polygon points="50,110 155,110 185,45 80,45" class="shape"/>'
                '<line x1="80" y1="45" x2="80" y2="110" class="line-dash"/>'
                '<text x="103" y="128" class="label">12 cm</text>'
                '<text x="88" y="82" class="label">5 cm</text>'
            ),
            option_a="17 square cm",
            option_b="30 square cm",
            option_c="60 square cm",
            option_d="120 square cm",
            correct_option="c",
            explanation_ar="Area of a parallelogram = base x height. The diagram shows base 12 cm and height 5 cm, so area = 60 square cm.",
            solution_steps_ar=_steps("Use base x height.", "12 x 5 = 60."),
            tags="parallelogram,area,figure",
            stage="building",
        ),
        Question(
            skill_id="quant_geometry",
            question_type="geometry",
            difficulty=0.55,
            text_ar="The diagram shows a trapezoid. What is its area?",
            figure_svg=_svg(
                '<polygon points="45,110 185,110 155,50 80,50" class="shape-pink"/>'
                '<line x1="80" y1="50" x2="80" y2="110" class="line-dash"/>'
                '<text x="110" y="42" text-anchor="middle" class="label">6 cm</text>'
                '<text x="115" y="128" class="label">10 cm</text>'
                '<text x="88" y="84" class="label">4 cm</text>'
            ),
            option_a="28 square cm",
            option_b="30 square cm",
            option_c="32 square cm",
            option_d="40 square cm",
            correct_option="c",
            explanation_ar="Use trapezoid area = $\\frac{1}{2} \\times$ (sum of parallel sides) $\\times$ height = $\\frac{1}{2} \\times (10 + 6) \\times 4 = 32$.",
            solution_steps_ar=_steps("Add the parallel sides: 10 + 6 = 16.", "Multiply by the height: 16 x 4 = 64.", "Take half: 64 / 2 = 32."),
            tags="trapezoid,area,figure",
            stage="building",
        ),
        Question(
            skill_id="quant_geometry",
            question_type="geometry",
            difficulty=0.4,
            text_ar="The diagram shows a right triangle with legs 6 cm and 8 cm. What is the hypotenuse?",
            figure_svg=_svg(
                '<path d="M40 105 L40 45 L160 105 Z" class="shape-green"/>'
                '<path d="M40 90 L55 90 L55 105" fill="none" class="line-thin"/>'
                '<text x="20" y="78" class="label">6 cm</text>'
                '<text x="92" y="124" class="label">8 cm</text>'
                '<text x="110" y="64" class="label">?</text>'
            ),
            option_a="9 cm",
            option_b="10 cm",
            option_c="12 cm",
            option_d="14 cm",
            correct_option="b",
            explanation_ar="By the Pythagorean theorem, $c^2 = 6^2 + 8^2 = 36 + 64 = 100$, so $c = 10$.",
            solution_steps_ar=_steps("Compute 6^2 + 8^2 = 100.", "Take the square root.", "The hypotenuse is 10."),
            tags="triangle,pythagorean,figure",
            stage="foundation",
        ),
        Question(
            skill_id="quant_geometry",
            question_type="geometry",
            difficulty=0.35,
            text_ar="The diagram shows two angles of a triangle. What is the third angle?",
            figure_svg=_svg(
                '<path d="M40 110 L180 110 L105 35 Z" class="shape-warm"/>'
                '<text x="62" y="102" class="label">35 deg</text>'
                '<text x="140" y="102" class="label">65 deg</text>'
                '<text x="100" y="58" class="label">?</text>'
            ),
            option_a="70 deg",
            option_b="75 deg",
            option_c="80 deg",
            option_d="100 deg",
            correct_option="c",
            explanation_ar="Angles in a triangle sum to 180 deg. The missing angle is 180 - 35 - 65 = 80 deg.",
            solution_steps_ar=_steps("Add the given angles: 35 + 65 = 100.", "Subtract from 180.", "180 - 100 = 80."),
            tags="triangle,angles,figure",
            stage="foundation",
        ),
        Question(
            skill_id="quant_geometry",
            question_type="geometry",
            difficulty=0.5,
            text_ar="The diagram shows a rectangle with side lengths 6 cm and 8 cm. What is the diagonal?",
            figure_svg=_svg(
                '<rect x="40" y="30" width="140" height="80" class="shape-cyan"/>'
                '<line x1="40" y1="110" x2="180" y2="30" class="line-thin"/>'
                '<text x="110" y="22" text-anchor="middle" class="label">8 cm</text>'
                '<text x="188" y="74" class="label">6 cm</text>'
                '<text x="110" y="78" class="label">?</text>'
            ),
            option_a="9 cm",
            option_b="10 cm",
            option_c="11 cm",
            option_d="14 cm",
            correct_option="b",
            explanation_ar="The diagonal is the hypotenuse of a right triangle with legs 6 and 8. d^2 = 6^2 + 8^2 = 100, so d = 10.",
            solution_steps_ar=_steps("Use 6^2 + 8^2 = d^2.", "d^2 = 36 + 64 = 100.", "d = 10."),
            tags="rectangle,diagonal,figure",
            stage="building",
        ),
        Question(
            skill_id="quant_geometry",
            question_type="geometry",
            difficulty=0.6,
            text_ar="The diagram shows a semicircle of radius 7 cm. What is its perimeter? (Use pi = 22/7.)",
            figure_svg=_svg(
                '<path d="M40 100 A60 60 0 0 1 160 100 L40 100 Z" class="shape-purple"/>'
                '<line x1="100" y1="100" x2="160" y2="100" class="line"/>'
                '<text x="116" y="92" class="label">7 cm</text>'
            ),
            option_a="22 cm",
            option_b="29 cm",
            option_c="36 cm",
            option_d="44 cm",
            correct_option="c",
            explanation_ar="Perimeter of a semicircle = half the circumference + the diameter = $\\pi r + 2r = 22 + 14 = 36$ cm.",
            solution_steps_ar=_steps("Half circumference = $\\pi r = 22$.", "Diameter = 14.", "$22 + 14 = 36$."),
            tags="circle,semicircle,perimeter,figure",
            stage="building",
        ),
        Question(
            skill_id="quant_geometry",
            question_type="geometry",
            difficulty=0.45,
            text_ar="A rectangle is cut by a diagonal as shown. What is the area of the shaded triangle?",
            figure_svg=_svg(
                '<rect x="40" y="30" width="150" height="90" class="shape-white"/>'
                '<path d="M40 120 L40 30 L190 120 Z" class="shape-highlight"/>'
                '<text x="115" y="22" text-anchor="middle" class="label">8 cm</text>'
                '<text x="198" y="80" class="label">6 cm</text>'
            ),
            option_a="20 square cm",
            option_b="24 square cm",
            option_c="48 square cm",
            option_d="56 square cm",
            correct_option="b",
            explanation_ar="Rectangle area = 8 x 6 = 48. A diagonal splits a rectangle into two equal triangles, so the shaded triangle area is 48 / 2 = 24.",
            solution_steps_ar=_steps("Find the rectangle area: 8 x 6 = 48.", "A diagonal halves the rectangle into two equal triangles.", "48 / 2 = 24."),
            tags="rectangle,triangle,area,figure",
            stage="building",
        ),
        Question(
            skill_id="quant_geometry",
            question_type="geometry",
            difficulty=0.4,
            text_ar="The diagonal of the square is shown. What is the area of one triangular half?",
            figure_svg=_svg(
                '<rect x="55" y="25" width="110" height="110" class="shape-white"/>'
                '<path d="M55 135 L55 25 L165 135 Z" class="shape-highlight-pink"/>'
                '<text x="172" y="84" class="label">10 cm</text>'
            ),
            option_a="25 square cm",
            option_b="40 square cm",
            option_c="50 square cm",
            option_d="100 square cm",
            correct_option="c",
            explanation_ar="Square area = 10 x 10 = 100. The diagonal divides the square into two equal triangles, so one half has area 50.",
            solution_steps_ar=_steps("Compute square area: 10 x 10 = 100.", "The diagonal splits the square into two equal parts.", "100 / 2 = 50."),
            tags="square,diagonal,area,figure",
            stage="foundation",
        ),
    ]


def _new_statistics_questions() -> list[Question]:
    return [
        Question(
            skill_id="quant_statistics",
            question_type="statistics",
            difficulty=0.35,
            text_ar="Use the table to find the mode of the weekly sales numbers.",
            table_ar={
                "headers": ["Day", "Sales"],
                "rows": [["Sun", "12"], ["Mon", "15"], ["Tue", "18"], ["Wed", "15"]],
            },
            option_a="12",
            option_b="15",
            option_c="16",
            option_d="18",
            correct_option="b",
            explanation_ar="The mode is the value that appears most often. In the table, 15 appears twice and every other value appears once.",
            solution_steps_ar=_steps("Read the sales numbers: 12, 15, 18, 15.", "Count repeats.", "15 appears most often."),
            tags="mode,table",
            stage="foundation",
        ),
        Question(
            skill_id="quant_statistics",
            question_type="statistics",
            difficulty=0.45,
            text_ar="Use the score table to find the range.",
            table_ar={
                "headers": ["Student", "Score"],
                "rows": [["A", "72"], ["B", "85"], ["C", "91"], ["D", "78"]],
            },
            option_a="13",
            option_b="16",
            option_c="19",
            option_d="21",
            correct_option="c",
            explanation_ar="The highest score in the table is 91 and the lowest is 72. Range = 91 - 72 = 19.",
            solution_steps_ar=_steps("Find the maximum score: 91.", "Find the minimum score: 72.", "Subtract to get 19."),
            tags="range,table",
            stage="foundation",
        ),
        Question(
            skill_id="quant_statistics",
            question_type="statistics",
            difficulty=0.5,
            text_ar="Use the frequency table to find the total number of observations.",
            table_ar={
                "headers": ["Value", "Frequency"],
                "rows": [["1", "2"], ["2", "3"], ["3", "4"], ["4", "1"]],
            },
            option_a="8",
            option_b="9",
            option_c="10",
            option_d="11",
            correct_option="c",
            explanation_ar="Add the frequencies in the table: 2 + 3 + 4 + 1 = 10 observations.",
            solution_steps_ar=_steps("Read the frequency column.", "Add 2 + 3 + 4 + 1.", "The total is 10."),
            tags="frequency,table",
            stage="building",
        ),
        Question(
            skill_id="quant_statistics",
            question_type="statistics",
            difficulty=0.4,
            text_ar="A bag contains the items listed in the table. What is the probability of choosing a blue card?",
            table_ar={
                "headers": ["Color", "Count"],
                "rows": [["Blue", "5"], ["Red", "3"], ["Green", "2"]],
            },
            option_a="1/5",
            option_b="1/2",
            option_c="3/5",
            option_d="5/10",
            correct_option="b",
            explanation_ar="There are 5 blue cards and 10 cards in total. Probability = 5/10 = 1/2.",
            solution_steps_ar=_steps("Count blue cards: 5.", "Count all cards: 5 + 3 + 2 = 10.", "5/10 simplifies to 1/2."),
            tags="probability,table",
            stage="foundation",
        ),
    ]


def _new_arithmetic_questions() -> list[Question]:
    return [
        Question(
            skill_id="quant_arithmetic",
            question_type="comparison",
            difficulty=0.45,
            text_ar="Use the table, then choose the correct relationship.",
            table_ar={
                "headers": ["Column", "Expression"],
                "rows": [["A", "18 x 4"], ["B", "24 x 3"]],
            },
            option_a="Column (A) is greater",
            option_b="Column (B) is greater",
            option_c="The two values are equal",
            option_d="The relationship cannot be determined",
            correct_option="c",
            explanation_ar="Column A = 72 and Column B = 72, so the two values are equal.",
            solution_steps_ar=_steps("Compute Column A: 18 x 4 = 72.", "Compute Column B: 24 x 3 = 72.", "Both columns are equal."),
            tags="comparison,table",
            stage="building",
        ),
        Question(
            skill_id="quant_arithmetic",
            question_type="comparison",
            difficulty=0.55,
            text_ar="Use the table, then choose the correct relationship.",
            table_ar={
                "headers": ["Column", "Expression"],
                "rows": [["A", "30% of 250"], ["B", "20% of 360"]],
            },
            option_a="Column (A) is greater",
            option_b="Column (B) is greater",
            option_c="The two values are equal",
            option_d="The relationship cannot be determined",
            correct_option="a",
            explanation_ar="Column A = 0.30 x 250 = 75. Column B = 0.20 x 360 = 72. Therefore Column A is greater.",
            solution_steps_ar=_steps("Find Column A: 75.", "Find Column B: 72.", "75 is greater than 72."),
            tags="comparison,percentage,table",
            stage="building",
        ),
        Question(
            skill_id="quant_arithmetic",
            question_type="arithmetic",
            difficulty=0.4,
            text_ar="The store offers in the table apply to the same shirt. Which statement is correct?",
            table_ar={
                "headers": ["Offer", "Rule"],
                "rows": [["Store A", "80 riyals with 10% discount"], ["Store B", "72 riyals with no discount"]],
            },
            option_a="Store A final price is 72 riyals",
            option_b="Store A final price is 74 riyals",
            option_c="Store B final price is 68 riyals",
            option_d="Store A is more expensive than Store B",
            correct_option="a",
            explanation_ar="Store A final price = 80 - 8 = 72. Store B final price is already 72. So the correct statement is that Store A ends at 72 riyals.",
            solution_steps_ar=_steps("Find 10% of 80 = 8.", "Store A final price = 80 - 8 = 72.", "Store B is already 72."),
            tags="discount,table",
            stage="foundation",
        ),
        Question(
            skill_id="quant_arithmetic",
            question_type="comparison",
            difficulty=0.6,
            text_ar="Use the travel table, then choose the correct relationship.",
            table_ar={
                "headers": ["Column", "Value"],
                "rows": [["A", "Speed when 180 km is covered in 3 hours"], ["B", "55 km/h"]],
            },
            option_a="Column (A) is greater",
            option_b="Column (B) is greater",
            option_c="The two values are equal",
            option_d="The relationship cannot be determined",
            correct_option="a",
            explanation_ar="Column A speed = 180 / 3 = 60 km/h. Since 60 is greater than 55, Column A is greater.",
            solution_steps_ar=_steps("Compute speed in Column A: 180 / 3 = 60.", "Read Column B: 55.", "60 > 55, so Column A is greater."),
            tags="comparison,speed,table",
            stage="building",
        ),
    ]


def apply_visual_refresh(questions: list[Question]) -> list[Question]:
    revised_count = 0
    revised_count += _revise_geometry_questions(questions)
    revised_count += _revise_statistics_questions(questions)
    revised_count += _revise_arithmetic_questions(questions)

    new_questions = _new_geometry_questions() + _new_statistics_questions() + _new_arithmetic_questions()

    if revised_count != 20:
        raise ValueError(f"Expected to revise 20 questions, revised {revised_count}")
    if len(new_questions) != 16:
        raise ValueError(f"Expected 16 new visual questions, found {len(new_questions)}")

    questions.extend(new_questions)
    return questions
