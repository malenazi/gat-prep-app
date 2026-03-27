from models import Question

def get_questions():
    return [

        # ══════════════════════════════════════════════════════════════
        # Existing Questions (14 questions)
        # ══════════════════════════════════════════════════════════════

        # 1 - Linear equation - diff 0.3
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.3,
            text_ar="If:\n3x + 7 = 22\nWhat is the value of x?",
            option_a="3", option_b="5", option_c="7", option_d="10",
            correct_option="b",
            explanation_ar="Solution:\n  3x + 7 = 22\n  3x = 22 - 7 = 15\n  x = 15 / 3 = 5\n\nWhy other options are wrong:\n  - 3: forgetting to subtract/add constant before dividing\n  - 7: sign error when transferring terms\n  - 10: dividing by wrong coefficient",
            solution_steps_ar='["3x + 7 = 22","Subtract 7 from both sides: 3x = 15","Divide by 3: x = 5"]',
    tags="linear-equation", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 2 - Geometric sequence - diff 0.4
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.4,
            text_ar="What is the next term in the geometric sequence:\n2, 6, 18, 54, ?",
            option_a="72", option_b="108", option_c="162", option_d="216",
            correct_option="c",
            explanation_ar="Pattern identification:\n  6 / 2 = 3\n  18 / 6 = 3\n  54 / 18 = 3\nTherefore, common ratio = 3\n\nNext term = 54 * 3 = 162\n\nWhy other options are wrong:\n  - 72: using wrong common ratio\n  - 108: confusing arithmetic and geometric sequences\n  - 216: error in applying general term formula",
            solution_steps_ar='["Find common ratio: 6 / 2 = 3","Verify: 18 / 6 = 3, 54 / 18 = 3","Next term = 54 * 3 = 162"]',
    tags="sequence", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 3 - Quadratic equation - diff 0.5
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.5,
            text_ar="If:\nx^2 = 49\nWhat are the possible values of x?",
            option_a="7 only", option_b="-7 only", option_c="+7 or -7", option_d="49",
            correct_option="c",
            explanation_ar="Solution:\n  x^2 = 49\n  x = +/- sqrt(49)\n  x = +7 or x = -7\n\nWhy other options are wrong:\n  - 7 only: sign error when factoring\n  - -7 only: forgetting the negative root\n  - 49: error in factorization",
            solution_steps_ar='["x^2 = 49","Take square root of both sides","x = +/- sqrt(49) = +/- 7"]',
    tags="quadratic", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 4 - Exponents - diff 0.6
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.6,
            text_ar="If:\n2^n = 32\nWhat is the value of n?",
            option_a="3", option_b="4", option_c="5", option_d="6",
            correct_option="c",
            explanation_ar="Solution:\n  2^n = 32\n  2^5 = 32\n  Therefore n = 5\n\nWhy other options are wrong:\n  - 3: multiplying exponents instead of adding\n  - 4: adding exponents instead of subtracting\n  - 6: multiplying base by exponent",
            solution_steps_ar='["2^n = 32","Factor 32 as power of 2: 2^5 = 32","Therefore n = 5"]',
    tags="exponent", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 5 - Simple linear equation - diff 0.2
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.2,
            text_ar="If:\nx - 9 = 15\nWhat is the value of x?",
            option_a="6", option_b="15", option_c="24", option_d="35",
            correct_option="c",
            explanation_ar="Solution:\n  x - 9 = 15\n  x = 15 + 9 = 24\n\nWhy other options are wrong:\n  - 6: forgetting to add constant\n  - 15: sign error when transferring terms\n  - 35: dividing by wrong coefficient",
            solution_steps_ar='["x - 9 = 15","Add 9 to both sides: x = 15 + 9","x = 24"]',
    tags="linear-equation", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 6 - Arithmetic sequence - diff 0.3
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.3,
            text_ar="What is the next term in the arithmetic sequence:\n3, 7, 11, 15, ?",
            option_a="17", option_b="18", option_c="19", option_d="20",
            correct_option="c",
            explanation_ar="Solution:\n  Common difference = 7 - 3 = 4\n  Next term = 15 + 4 = 19\n\nWhy other options are wrong:\n  - 17: using wrong common difference\n  - 18: confusing arithmetic and geometric sequences\n  - 20: error in applying general term formula",
            solution_steps_ar='["Difference between consecutive terms = 4","Common difference = 4","Next term = 15 + 4 = 19"]',
    tags="sequence", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # 7 - Functions - diff 0.3
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.3,
            text_ar="If y = 2x + 1\nWhat is the value of y when x = 4?",
            option_a="5", option_b="7", option_c="9", option_d="11",
            correct_option="c",
            explanation_ar="Solution:\n  y = 2 * 4 + 1 = 8 + 1 = 9\n\nWhy other options are wrong:\n  - 5: calculation error\n  - 7: sign error\n  - 11: wrong coefficient",
            solution_steps_ar='["y = 2x + 1","Substitute x = 4: y = 2 * 4 + 1","y = 8 + 1 = 9"]',
    tags="linear-equation,function", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # 8 - Inequality - diff 0.4
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.4,
            text_ar="Solve the inequality:\n2x + 3 < 11",
            option_a="x < 2", option_b="x < 4", option_c="x < 7", option_d="x > 4",
            correct_option="b",
            explanation_ar="Solution:\n  2x + 3 < 11\n  2x < 8\n  x < 4\n\nWhy other options are wrong:\n  - x < 2: forgetting to reverse sign\n  - x < 7: wrong inequality direction\n  - x > 4: treating inequality as equation",
            solution_steps_ar='["2x + 3 < 11","Subtract 3 from both sides: 2x < 8","Divide by 2: x < 4"]',
    tags="inequality", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 9 - Factoring difference of squares - diff 0.5
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.5,
            text_ar="Factor the expression:\nx^2 - 9",
            option_a="(x - 3)(x - 3)", option_b="(x + 3)(x - 3)", option_c="(x + 9)(x - 1)", option_d="(x - 9)(x + 1)",
            correct_option="b",
            explanation_ar="Solution:\n  x^2 - 9 = x^2 - 3^2\n  Difference of squares: (x + 3)(x - 3)\n\nWhy other options are wrong:\n  - (x-3)(x-3): sign error when factoring\n  - (x+9)(x-1): confusing difference of squares with perfect square\n  - (x-9)(x+1): swapping sign in one factor",
            solution_steps_ar='["Note that 9 = 3^2","Formula: a^2 - b^2 = (a + b)(a - b)","Therefore x^2 - 9 = (x + 3)(x - 3)"]',
    tags="factoring", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 10 - System of equations - diff 0.5
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.5,
            text_ar="If:\nx + y = 10\nx - y = 4\nWhat is the value of x?",
            option_a="3", option_b="5", option_c="7", option_d="10",
            correct_option="c",
            explanation_ar="Solution:\n  Adding equations: 2x = 14\n  x = 7\n\nWhy other options are wrong:\n  - 3: calculation error\n  - 5: sign error\n  - 10: wrong coefficient",
            solution_steps_ar='["Add the equations: 2x = 14","Divide by 2: x = 7"]',
    tags="linear-equation,function", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 11 - Exponents - diff 0.6
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.6,
            text_ar="What is the result:\n2^3 * 2^4 = ?",
            option_a="2^7", option_b="2^12", option_c="4^7", option_d="4^12",
            correct_option="a",
            explanation_ar="Rule:\n  a^m * a^n = a^(m + n)\n  2^3 * 2^4 = 2^7 = 128\n\nWhy other options are wrong:\n  - 2^12: multiplying exponents instead of adding\n  - 4^7: wrong base\n  - 4^12: both errors combined",
            solution_steps_ar='["Rule: a^m * a^n = a^(m + n)","2^3 * 2^4 = 2^(3+4)","= 2^7 = 128"]',
    tags="exponent", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 12 - Quadratic equation by factoring - diff 0.7
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.7,
            text_ar="If:\nx^2 - 5x + 6 = 0\nWhat are the values of x?",
            option_a="2, 3", option_b="-2, -3", option_c="1, 6", option_d="-1, 6",
            correct_option="a",
            explanation_ar="Solution:\n  (x - 2)(x - 3) = 0\n  x = 2 or x = 3\n\nWhy other options are wrong:\n  - -2,-3: sign error in roots\n  - 1,6: wrong factor pair\n  - -1,6: incorrect factoring",
            solution_steps_ar='["x^2 - 5x + 6 = 0","Find two numbers with product = 6 and sum = 5","Factor: (x - 2)(x - 3) = 0","Therefore x = 2 or x = 3"]',
    tags="quadratic", stage="foundation",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # 13 - Sum of sequence - diff 0.8
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.8,
            text_ar="The general term of an arithmetic sequence is:\na_n = 3n + 2\nWhat is the sum of the first 10 terms?",
            option_a="165", option_b="185", option_c="195", option_d="205",
            correct_option="b",
            explanation_ar="Solution:\n  a_1 = 3(1) + 2 = 5\n  a_10 = 3(10) + 2 = 32\n  Sum = 10/2 * (5 + 32) = 5 * 37 = 185\n\nWhy other options are wrong:\n  - 165: using wrong common difference\n  - 195: confusing arithmetic and geometric sequences\n  - 205: error in formula",
            solution_steps_ar='["a_1 = 3(1) + 2 = 5","a_10 = 3(10) + 2 = 32","Sum = (n/2) * (a_1 + a_n) = 5 * 37 = 185"]',
    tags="sequence", stage="foundation",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # 14 - System of equations - diff 0.8
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.8,
            text_ar="If:\nx + 2y = 8\n3x - 2y = 4\nWhat is the value of y?",
            option_a="1", option_b="2.5", option_c="3", option_d="4",
            correct_option="b",
            explanation_ar="Solution:\n  Adding equations: 4x = 12, so x = 3\n  Substitute: 3 + 2y = 8, so 2y = 5, so y = 2.5\n\nWhy other options are wrong:\n  - 1: calculation error\n  - 3: sign error\n  - 4: wrong coefficient",
            solution_steps_ar='["Add equations: 4x = 12, x = 3","Substitute: 3 + 2y = 8, 2y = 5","y = 2.5"]',
    tags="linear-equation,function", stage="foundation",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),


        # ══════════════════════════════════════════════════════════════
        # New Questions (97 questions) - Numbers 15 to 111
        # ══════════════════════════════════════════════════════════════

        # --- Difficulty 0.2 (need 11 total, have 1, adding 10) ---

        # 15 - Simple linear equation
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.2,
            text_ar="If:\nx + 5 = 12\nWhat is the value of x?",
            option_a="5", option_b="7", option_c="12", option_d="17",
            correct_option="b",
            explanation_ar="Solution:\n  x + 5 = 12\n  x = 12 - 5 = 7\n\nWhy other options are wrong:\n  - 5: forgetting to subtract constant\n  - 12: sign error\n  - 17: wrong operation",
            solution_steps_ar='["x + 5 = 12","Subtract 5 from both sides","x = 7"]',
    tags="linear-equation", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # 16 - Simple linear equation
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.2,
            text_ar="If:\n2x = 14\nWhat is the value of x?",
            option_a="2", option_b="5", option_c="7", option_d="14",
            correct_option="c",
            explanation_ar="Solution:\n  2x = 14\n  x = 14 / 2 = 7\n\nWhy other options are wrong:\n  - 2: using coefficient as answer\n  - 5: random error\n  - 14: forgetting to divide",
            solution_steps_ar='["2x = 14","Divide by 2","x = 7"]',
    tags="linear-equation", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # 17
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.2,
            text_ar="If:\nx + 8 = 20\nWhat is the value of x?",
            option_a="8", option_b="10", option_c="12", option_d="28",
            correct_option="c",
            explanation_ar="Solution:\n  x = 20 - 8 = 12\n\nWhy other options are wrong:\n  - 8: using the constant\n  - 10: incorrect subtraction\n  - 28: adding instead of subtracting",
            solution_steps_ar='["x + 8 = 20","Subtract 8 from both sides","x = 12"]',
    tags="linear-equation", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # 18
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.2,
            text_ar="If:\nx / 3 = 6\nWhat is the value of x?",
            option_a="2", option_b="9", option_c="18", option_d="36",
            correct_option="c",
            explanation_ar="Solution:\n  x = 6 * 3 = 18\n\nWhy other options are wrong:\n  - 2: dividing instead of multiplying\n  - 9: using 6+3\n  - 36: squaring instead of multiplying",
            solution_steps_ar='["x / 3 = 6","Multiply both sides by 3","x = 18"]',
    tags="linear-equation", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # 19
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.2,
            text_ar="If:\nx - 4 = 11\nWhat is the value of x?",
            option_a="7", option_b="11", option_c="15", option_d="44",
            correct_option="c",
            explanation_ar="Solution:\n  x = 11 + 4 = 15\n\nWhy other options are wrong:\n  - 7: subtracting 4 instead of adding\n  - 11: ignoring the constant\n  - 44: multiplying instead of adding",
            solution_steps_ar='["x - 4 = 11","Add 4 to both sides","x = 15"]',
    tags="linear-equation", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # 20
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.2,
            text_ar="If x = 3, what is the value of 4x?",
            option_a="7", option_b="12", option_c="16", option_d="34",
            correct_option="b",
            explanation_ar="Solution:\n  4x = 4 * 3 = 12\n\nWhy other options are wrong:\n  - 7: adding instead of multiplying\n  - 16: wrong calculation\n  - 34: concatenation error",
            solution_steps_ar='["Substitute x = 3","4 * 3 = 12"]',
    tags="linear-equation", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # 21
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.2,
            text_ar="If:\n5x = 35\nWhat is the value of x?",
            option_a="5", option_b="7", option_c="30", option_d="40",
            correct_option="b",
            explanation_ar="Solution:\n  x = 35 / 5 = 7\n\nWhy other options are wrong:\n  - 5: using coefficient\n  - 30: subtracting instead of dividing\n  - 40: adding instead of dividing",
            solution_steps_ar='["5x = 35","Divide by 5","x = 7"]',
    tags="linear-equation", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # 22
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.2,
            text_ar="What is the next term in the sequence:\n2, 4, 6, 8, ?",
            option_a="9", option_b="10", option_c="11", option_d="12",
            correct_option="b",
            explanation_ar="Solution:\n  Difference between terms = 2\n  Next term = 8 + 2 = 10\n\nWhy other options are wrong:\n  - 9: odd number pattern\n  - 11: adding 3\n  - 12: multiplying by 1.5",
            solution_steps_ar='["Difference between terms = 2","Next term = 8 + 2 = 10"]',
    tags="sequence", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # 23
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.2,
            text_ar="If we substitute x = 5 in the expression 2x + 1, which value do we get?",
            option_a="7", option_b="9", option_c="11", option_d="13",
            correct_option="c",
            explanation_ar="Solution:\n  2 * 5 + 1 = 10 + 1 = 11\n\nWhy other options are wrong:\n  - 7: calculating 2+5\n  - 9: calculating 2*5-1\n  - 13: calculating 2*5+3",
            solution_steps_ar='["Substitute x = 5","2 * 5 + 1 = 11"]',
    tags="linear-equation", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # 24
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.2,
            text_ar="If:\nx + 10 = 25\nWhat is the value of x?",
            option_a="10", option_b="15", option_c="25", option_d="35",
            correct_option="b",
            explanation_ar="Solution:\n  x = 25 - 10 = 15\n\nWhy other options are wrong:\n  - 10: using the constant\n  - 25: ignoring the operation\n  - 35: adding instead of subtracting",
            solution_steps_ar='["x + 10 = 25","Subtract 10 from both sides","x = 15"]',
    tags="linear-equation", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # --- Difficulty 0.3 (need 17 total, have 3, adding 14) ---

        # 25
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.3,
            text_ar="If:\n4x - 3 = 13\nWhat is the value of x?",
            option_a="2", option_b="3", option_c="4", option_d="5",
            correct_option="c",
            explanation_ar="Solution:\n  4x = 13 + 3 = 16\n  x = 4\n\nWhy other options are wrong:\n  - 2: division error\n  - 3: wrong addition\n  - 5: sign error",
            solution_steps_ar='["4x - 3 = 13","Add 3: 4x = 16","Divide by 4: x = 4"]',
    tags="linear-equation", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # 26
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.3,
            text_ar="If f(x) = 3x - 2\nWhat is the value of f(5)?",
            option_a="7", option_b="10", option_c="13", option_d="17",
            correct_option="c",
            explanation_ar="Solution:\n  f(5) = 3 * 5 - 2 = 15 - 2 = 13\n\nWhy other options are wrong:\n  - 7: calculation error\n  - 10: missing subtraction\n  - 17: sign error",
            solution_steps_ar='["f(5) = 3 * 5 - 2","= 15 - 2 = 13"]',
    tags="function", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # 27
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.3,
            text_ar="What is the next term in the arithmetic sequence:\n5, 9, 13, 17, ?",
            option_a="19", option_b="20", option_c="21", option_d="22",
            correct_option="c",
            explanation_ar="Solution:\n  Common difference = 4\n  Next term = 17 + 4 = 21\n\nWhy other options are wrong:\n  - 19: using difference of 2\n  - 20: confusing patterns\n  - 22: adding 5",
            solution_steps_ar='["Common difference = 9 - 5 = 4","Next term = 17 + 4 = 21"]',
    tags="sequence", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 28
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.3,
            text_ar="If:\n2x + 5 = 17\nWhat is the value of x?",
            option_a="4", option_b="6", option_c="8", option_d="11",
            correct_option="b",
            explanation_ar="Solution:\n  2x = 17 - 5 = 12\n  x = 6\n\nWhy other options are wrong:\n  - 4: not subtracting first\n  - 8: wrong calculation\n  - 11: adding 5 instead of subtracting",
            solution_steps_ar='["2x + 5 = 17","Subtract 5: 2x = 12","Divide by 2: x = 6"]',
    tags="linear-equation", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 29
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.3,
            text_ar="What number multiplied by itself gives 64?",
            option_a="6", option_b="7", option_c="8", option_d="9",
            correct_option="c",
            explanation_ar="Solution:\n  8 * 8 = 64\n  Therefore sqrt(64) = 8\n\nWhy other options are wrong:\n  - 6: wrong square\n  - 7: close but incorrect\n  - 9: wrong square",
            solution_steps_ar='["Find the number whose square = 64","8 * 8 = 64","Therefore sqrt(64) = 8"]',
    tags="radical", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 30
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.3,
            text_ar="What is the result of multiplying the number 3 by itself three times?",
            option_a="9", option_b="12", option_c="27", option_d="81",
            correct_option="c",
            explanation_ar="Solution:\n  3 * 3 * 3 = 27\n\nWhy other options are wrong:\n  - 9: only multiplying twice\n  - 12: adding instead\n  - 81: multiplying four times",
            solution_steps_ar='["3^3 = 3 * 3 * 3","= 9 * 3 = 27"]',
    tags="exponent", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),


        # 31
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.3,
            text_ar="What is the sum of numbers from 1 to 10?",
            option_a="45", option_b="50", option_c="55", option_d="60",
            correct_option="c",
            explanation_ar="Formula:\n  Sum = n(n + 1) / 2 = 10 * 11 / 2 = 55\n\nWhy other options are wrong:\n  - 45: wrong calculation\n  - 50: using n^2\n  - 60: wrong formula",
            solution_steps_ar='["Sum = n(n + 1) / 2","= 10 * 11 / 2","= 55"]',
    tags="sequence", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 32
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.3,
            text_ar="If y is directly proportional to x, and y = 6 when x = 2.\nWhat is the value of y when x = 5?",
            option_a="10", option_b="15", option_c="20", option_d="30",
            correct_option="b",
            explanation_ar="Solution:\n  k = 6 / 2 = 3\n  y = 3 * 5 = 15\n\nWhy other options are wrong:\n  - 10: confusing direct/inverse\n  - 20: wrong constant\n  - 30: wrong calculation",
            solution_steps_ar='["y = k * x, so k = 6 / 2 = 3","When x = 5: y = 3 * 5 = 15"]',
    tags="proportion", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 33
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.3,
            text_ar="If x = 2 and y = 3\nWhat is the value of 2x + y?",
            option_a="5", option_b="7", option_c="8", option_d="10",
            correct_option="b",
            explanation_ar="Solution:\n  2 * 2 + 3 = 4 + 3 = 7\n\nWhy other options are wrong:\n  - 5: wrong substitution\n  - 8: adding 2+3+3\n  - 10: multiplying all",
            solution_steps_ar='["Substitute: 2 * 2 + 3","= 4 + 3 = 7"]',
    tags="linear-equation,function", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 34
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.3,
            text_ar="If:\n5x - 10 = 30\nWhat is the value of x?",
            option_a="4", option_b="6", option_c="8", option_d="10",
            correct_option="c",
            explanation_ar="Solution:\n  5x = 30 + 10 = 40\n  x = 8\n\nWhy other options are wrong:\n  - 4: wrong division\n  - 6: sign error\n  - 10: ignoring division",
            solution_steps_ar='["5x - 10 = 30","Add 10: 5x = 40","Divide by 5: x = 8"]',
    tags="linear-equation", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 35
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.3,
            text_ar="What is the next term in the sequence:\n10, 15, 20, 25, ?",
            option_a="28", option_b="29", option_c="30", option_d="35",
            correct_option="c",
            explanation_ar="Solution:\n  Common difference = 5\n  Next term = 25 + 5 = 30\n\nWhy other options are wrong:\n  - 28: wrong pattern\n  - 29: odd number added\n  - 35: adding 10",
            solution_steps_ar='["Common difference = 5","Next term = 25 + 5 = 30"]',
    tags="sequence", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 36
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.3,
            text_ar="What is the integer whose square equals 121?",
            option_a="9", option_b="10", option_c="11", option_d="12",
            correct_option="c",
            explanation_ar="Solution:\n  11 * 11 = 121\n  Therefore sqrt(121) = 11\n\nWhy other options are wrong:\n  - 9: 81 is 9 squared\n  - 10: 100 is 10 squared\n  - 12: 144 is 12 squared",
            solution_steps_ar='["Find the number whose square = 121","11 * 11 = 121","Therefore sqrt(121) = 11"]',
    tags="radical", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 37
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.3,
            text_ar="If:\nx / 4 + 3 = 7\nWhat is the value of x?",
            option_a="4", option_b="10", option_c="16", option_d="28",
            correct_option="c",
            explanation_ar="Solution:\n  x / 4 = 7 - 3 = 4\n  x = 4 * 4 = 16\n\nWhy other options are wrong:\n  - 4: incomplete solution\n  - 10: wrong calculation\n  - 28: wrong operation",
            solution_steps_ar='["x / 4 + 3 = 7","Subtract 3: x / 4 = 4","Multiply by 4: x = 16"]',
    tags="linear-equation", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 38
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.3,
            text_ar="What is the distance of the number -8 from zero on the number line?",
            option_a="-8", option_b="0", option_c="8", option_d="16",
            correct_option="c",
            explanation_ar="Solution:\n  Absolute value = distance from zero\n  |-8| = 8\n\nWhy other options are wrong:\n  - -8: ignoring absolute value\n  - 0: incorrect\n  - 16: doubling error",
            solution_steps_ar='["Absolute value = distance from zero","Distance between -8 and zero = 8","Therefore |-8| = 8"]',
    tags="absolute-value", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- Difficulty 0.4 (need 22 total, have 2, adding 20) ---

        # 39
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.4,
            text_ar="Solve the inequality:\n3x - 5 >= 10",
            option_a="x >= 3", option_b="x >= 5", option_c="x >= 15", option_d="x <= 5",
            correct_option="b",
            explanation_ar="Solution:\n  3x >= 15\n  x >= 5\n\nWhy other options are wrong:\n  - x >= 3: wrong division\n  - x >= 15: not dividing\n  - x <= 5: wrong direction",
            solution_steps_ar='["3x - 5 >= 10","Add 5: 3x >= 15","Divide by 3: x >= 5"]',
    tags="inequality", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 40
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.4,
            text_ar="Factor the expression:\n6x + 12",
            option_a="6(x + 2)", option_b="3(2x + 4)", option_c="2(3x + 6)", option_d="12(x + 1)",
            correct_option="a",
            explanation_ar="Solution:\n  GCF = 6\n  6x + 12 = 6(x + 2)\n\nWhy other options are wrong:\n  - B and C: not fully factored\n  - D: wrong GCF",
            solution_steps_ar='["Greatest Common Factor = 6","6x + 12 = 6(x + 2)"]',
    tags="factoring", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 41
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.4,
            text_ar="What is the next term in the geometric sequence:\n3, 9, 27, 81, ?",
            option_a="108", option_b="162", option_c="243", option_d="324",
            correct_option="c",
            explanation_ar="Solution:\n  Common ratio = 3\n  Next term = 81 * 3 = 243\n\nWhy other options are wrong:\n  - 108: adding 27\n  - 162: wrong ratio\n  - 324: wrong calculation",
            solution_steps_ar='["Common ratio = 9 / 3 = 3","Next term = 81 * 3 = 243"]',
    tags="sequence", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 42
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.4,
            text_ar="If:\nx + y = 8\nand x = 3\nWhat is the value of y?",
            option_a="3", option_b="5", option_c="8", option_d="11",
            correct_option="b",
            explanation_ar="Solution:\n  y = 8 - 3 = 5\n\nWhy other options are wrong:\n  - 3: using x value\n  - 8: total value\n  - 11: adding instead of subtracting",
            solution_steps_ar='["Substitute x = 3","y = 8 - 3 = 5"]',
    tags="linear-equation,function", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 43
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.4,
            text_ar="Solve the equation:\n|x| = 5\nWhat are the possible values of x?",
            option_a="5 only", option_b="-5 only", option_c="5 or -5", option_d="0",
            correct_option="c",
            explanation_ar="Solution:\n  |x| = 5\n  x = 5 or x = -5\n\nWhy other options are wrong:\n  - 5 only: missing negative\n  - -5 only: missing positive\n  - 0: incorrect",
            solution_steps_ar='["|x| = 5","Case 1: x = 5","Case 2: x = -5"]',
    tags="absolute-value", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 44
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.4,
            text_ar="If f(x) = 4x - 7\nWhat is the value of f(3)?",
            option_a="3", option_b="5", option_c="7", option_d="12",
            correct_option="b",
            explanation_ar="Solution:\n  f(3) = 4 * 3 - 7 = 12 - 7 = 5\n\nWhy other options are wrong:\n  - 3: using input\n  - 7: using constant\n  - 12: forgetting subtraction",
            solution_steps_ar='["f(3) = 4 * 3 - 7","= 12 - 7 = 5"]',
    tags="function", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 45
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.4,
            text_ar="Simplify:\n(x^3)^2",
            option_a="x^5", option_b="x^6", option_c="x^9", option_d="2x^3",
            correct_option="b",
            explanation_ar="Rule:\n  (a^m)^n = a^(m * n)\n  = x^6\n\nWhy other options are wrong:\n  - x^5: adding exponents\n  - x^9: multiplying wrong\n  - 2x^3: wrong operation",
            solution_steps_ar='["Rule: (a^m)^n = a^(m * n)","(x^3)^2 = x^6"]',
    tags="exponent", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 46
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.4,
            text_ar="If:\n7x + 3 = 31\nWhat is the value of x?",
            option_a="2", option_b="4", option_c="5", option_d="7",
            correct_option="b",
            explanation_ar="Solution:\n  7x = 28\n  x = 4\n\nWhy other options are wrong:\n  - 2: wrong division\n  - 5: miscalculation\n  - 7: using coefficient",
            solution_steps_ar='["7x + 3 = 31","Subtract 3: 7x = 28","Divide by 7: x = 4"]',
    tags="linear-equation", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 47
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.4,
            text_ar="If y is inversely proportional to x, and y = 6 when x = 4.\nWhat is the value of y when x = 8?",
            option_a="2", option_b="3", option_c="4", option_d="12",
            correct_option="b",
            explanation_ar="Solution:\n  k = y * x = 6 * 4 = 24\n  When x = 8: y = 24 / 8 = 3\n\nWhy other options are wrong:\n  - 2: wrong calculation\n  - 4: direct proportion\n  - 12: wrong formula",
            solution_steps_ar='["k = y * x = 6 * 4 = 24","When x = 8: y = 24 / 8 = 3"]',
    tags="proportion", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 48
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.4,
            text_ar="An arithmetic sequence has first term 3 and common difference 4.\nWhat is the 5th term?",
            option_a="15", option_b="19", option_c="23", option_d="27",
            correct_option="b",
            explanation_ar="Solution:\n  a_5 = 3 + (5 - 1) * 4 = 3 + 16 = 19\n\nWhy other options are wrong:\n  - 15: wrong formula\n  - 23: wrong calculation\n  - 27: adding first term 3 times",
            solution_steps_ar='["a_n = a_1 + (n - 1) * d","a_5 = 3 + 4 * 4 = 19"]',
    tags="sequence", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 49
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.4,
            text_ar="Simplify:\nsqrt(50)",
            option_a="5sqrt(2)", option_b="2sqrt(5)", option_c="10sqrt(5)", option_d="25sqrt(2)",
            correct_option="a",
            explanation_ar="Solution:\n  sqrt(50) = sqrt(25 * 2) = 5sqrt(2)\n\nWhy other options are wrong:\n  - B: wrong factors\n  - C: not simplifying\n  - D: wrong extraction",
            solution_steps_ar='["sqrt(50) = sqrt(25 * 2)","= sqrt(25) * sqrt(2) = 5sqrt(2)"]',
    tags="radical", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 50
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.4,
            text_ar="Solve the inequality:\n-2x > 8",
            option_a="x > -4", option_b="x < -4", option_c="x > 4", option_d="x < 4",
            correct_option="b",
            explanation_ar="Solution:\n  Divide by -2 and reverse the sign:\n  x < -4\n\nWhy other options are wrong:\n  - x > -4: not reversing sign\n  - x > 4: wrong direction\n  - x < 4: wrong calculation",
            solution_steps_ar='["-2x > 8","Divide by -2 (reverse sign)","x < -4"]',
    tags="inequality", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),


        # 51
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.4,
            text_ar="If:\n6 - 2x = 0\nWhat is the value of x?",
            option_a="0", option_b="2", option_c="3", option_d="6",
            correct_option="c",
            explanation_ar="Solution:\n  2x = 6\n  x = 3\n\nWhy other options are wrong:\n  - 0: setting term to zero\n  - 2: wrong division\n  - 6: not dividing",
            solution_steps_ar='["6 - 2x = 0","2x = 6","x = 3"]',
    tags="linear-equation", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 52
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.4,
            text_ar="If f(x) = x^2 + 1\nWhat is the value of f(3)?",
            option_a="4", option_b="7", option_c="10", option_d="12",
            correct_option="c",
            explanation_ar="Solution:\n  f(3) = 9 + 1 = 10\n\nWhy other options are wrong:\n  - 4: wrong squaring\n  - 7: adding before squaring\n  - 12: wrong addition",
            solution_steps_ar='["f(3) = 3^2 + 1","= 9 + 1 = 10"]',
    tags="quadratic,function", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 53
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.4,
            text_ar="Using exponent rules, what is any number (non-zero) raised to the power of zero? Find 5^0",
            option_a="0", option_b="1", option_c="5", option_d="undefined",
            correct_option="b",
            explanation_ar="Rule:\n  Any non-zero number to the power of 0 = 1\n\nWhy other options are wrong:\n  - 0: common misconception\n  - 5: returning base\n  - undefined: incorrect rule",
            solution_steps_ar='["Rule: a^0 = 1 (for any a != 0)","5^0 = 1"]',
    tags="exponent", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 54
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.4,
            text_ar="If:\n3(x + 2) = 21\nWhat is the value of x?",
            option_a="3", option_b="5", option_c="7", option_d="9",
            correct_option="b",
            explanation_ar="Solution:\n  x + 2 = 7\n  x = 5\n\nWhy other options are wrong:\n  - 3: dividing wrong\n  - 7: forgetting to subtract\n  - 9: wrong operation",
            solution_steps_ar='["3(x + 2) = 21","Divide by 3: x + 2 = 7","x = 5"]',
    tags="linear-equation", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 55
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.4,
            text_ar="Factor the expression:\nx^2 - 4",
            option_a="(x - 2)^2", option_b="(x + 2)(x - 2)", option_c="(x + 4)(x - 1)", option_d="(x - 4)(x + 1)",
            correct_option="b",
            explanation_ar="Solution:\n  Difference of squares: x^2 - 2^2 = (x + 2)(x - 2)\n\nWhy other options are wrong:\n  - A: perfect square error\n  - C and D: wrong factors",
            solution_steps_ar='["x^2 - 4 = x^2 - 2^2","Difference of squares: (x + 2)(x - 2)"]',
    tags="factoring", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 56
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.4,
            text_ar="An arithmetic sequence has first term 2 and common difference 3.\nWhat is the 7th term?",
            option_a="18", option_b="20", option_c="21", option_d="23",
            correct_option="b",
            explanation_ar="Solution:\n  a_7 = 2 + (7 - 1) * 3 = 2 + 18 = 20\n\nWhy other options are wrong:\n  - 18: wrong calculation\n  - 21: off-by-one error\n  - 23: adding 7*3",
            solution_steps_ar='["a_7 = 2 + 6 * 3","= 2 + 18 = 20"]',
    tags="sequence", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 57
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.4,
            text_ar="Simplify:\nsqrt(18)",
            option_a="3sqrt(2)", option_b="2sqrt(3)", option_c="6sqrt(3)", option_d="9sqrt(2)",
            correct_option="a",
            explanation_ar="Solution:\n  sqrt(18) = sqrt(9 * 2) = 3sqrt(2)\n\nWhy other options are wrong:\n  - B: wrong factors\n  - C: incomplete\n  - D: wrong extraction",
            solution_steps_ar='["sqrt(18) = sqrt(9 * 2)","= sqrt(9) * sqrt(2) = 3sqrt(2)"]',
    tags="radical", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 58
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.4,
            text_ar="If x = -2\nWhat is the value of x^2 + 3x?",
            option_a="-10", option_b="-2", option_c="2", option_d="10",
            correct_option="b",
            explanation_ar="Solution:\n  (-2)^2 + 3(-2) = 4 - 6 = -2\n\nWhy other options are wrong:\n  - -10: sign errors\n  - 2: wrong calculation\n  - 10: ignoring negative",
            solution_steps_ar='["Substitute x = -2","(-2)^2 + 3 * (-2) = 4 - 6 = -2"]',
    tags="quadratic", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- Difficulty 0.5 (need 22 total, have 3, adding 19) ---

        # 59
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.5,
            text_ar="If:\n2x + y = 10\nx - y = 2\nWhat is the value of x?",
            option_a="3", option_b="4", option_c="5", option_d="6",
            correct_option="b",
            explanation_ar="Solution:\n  Adding equations: 3x = 12\n  x = 4\n\nWhy other options are wrong:\n  - 3: division error\n  - 5: wrong addition\n  - 6: wrong coefficient",
            solution_steps_ar='["Add equations: 3x = 12","x = 4"]',
    tags="linear-equation,function", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 60
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.5,
            text_ar="Solve the equation:\nx^2 - 4x = 0",
            option_a="0, 4", option_b="0, -4", option_c="2, -2", option_d="4 only",
            correct_option="a",
            explanation_ar="Solution:\n  x(x - 4) = 0\n  x = 0 or x = 4\n\nWhy other options are wrong:\n  - B: sign error\n  - C: wrong equation\n  - D: missing root",
            solution_steps_ar='["Factor out x: x(x - 4) = 0","x = 0 or x = 4"]',
    tags="quadratic", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 61
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.5,
            text_ar="Factor the expression:\nx^2 + 5x + 6",
            option_a="(x + 1)(x + 6)", option_b="(x + 2)(x + 3)", option_c="(x + 3)(x + 3)", option_d="(x - 2)(x - 3)",
            correct_option="b",
            explanation_ar="Solution:\n  Two numbers with product 6 and sum 5: 2 and 3\n  (x + 2)(x + 3)\n\nWhy other options are wrong:\n  - A: wrong pair\n  - C: perfect square error\n  - D: sign error",
            solution_steps_ar='["Find two numbers with product = 6 and sum = 5","The numbers: 2 and 3","Therefore (x + 2)(x + 3)"]',
    tags="factoring", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 62
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.5,
            text_ar="What is the value of 2^(-3)?",
            option_a="-8", option_b="-6", option_c="1/8", option_d="8",
            correct_option="c",
            explanation_ar="Rule:\n  a^(-n) = 1 / a^n\n  2^(-3) = 1 / 8 = 1/8\n\nWhy other options are wrong:\n  - -8: treating exponent as multiplier\n  - -6: wrong operation\n  - 8: ignoring negative sign",
            solution_steps_ar='["Rule: a^(-n) = 1 / a^n","2^(-3) = 1 / 2^3 = 1/8"]',
    tags="exponent", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 63
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.5,
            text_ar="If y is directly proportional to x, and y = 12 when x = 4.\nWhat is the value of y when x = 7?",
            option_a="18", option_b="21", option_c="24", option_d="28",
            correct_option="b",
            explanation_ar="Solution:\n  k = 12 / 4 = 3\n  y = 3 * 7 = 21\n\nWhy other options are wrong:\n  - 18: wrong constant\n  - 24: doubling error\n  - 28: wrong formula",
            solution_steps_ar='["k = 12 / 4 = 3","When x = 7: y = 3 * 7 = 21"]',
    tags="proportion", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 64
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.5,
            text_ar="Solve the equation:\n|2x - 5| = 9\nWhat is the sum of the two values of x?",
            option_a="3", option_b="5", option_c="7", option_d="9",
            correct_option="b",
            explanation_ar="Solution:\n  Case 1: 2x - 5 = 9, so x = 7\n  Case 2: 2x - 5 = -9, so x = -2\n  Sum = 7 + (-2) = 5\n\nWhy other options are wrong:\n  - 3: calculation error\n  - 7: using one value\n  - 9: wrong cases",
            solution_steps_ar='["Case 1: 2x - 5 = 9, x = 7","Case 2: 2x - 5 = -9, x = -2","Sum = 7 + (-2) = 5"]',
    tags="absolute-value", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 65
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.5,
            text_ar="In the equation x^2 - 5x + 6 = 0\nWhat is the product of the roots?",
            option_a="5", option_b="6", option_c="-6", option_d="-5",
            correct_option="b",
            explanation_ar="Solution:\n  Product of roots = c/a = 6/1 = 6\n  (Or: roots are 2 and 3, 2*3 = 6)\n\nWhy other options are wrong:\n  - 5: using sum\n  - -6: sign error\n  - -5: using -b/a",
            solution_steps_ar='["Product of roots = constant term / coefficient of x^2","= 6 / 1 = 6"]',
    tags="quadratic,radical", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 66
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.5,
            text_ar="Simplify:\nx^7 / x^3",
            option_a="x^4", option_b="x^10", option_c="x^21", option_d="1",
            correct_option="a",
            explanation_ar="Rule:\n  a^m / a^n = a^(m - n)\n  = x^4\n\nWhy other options are wrong:\n  - x^10: adding exponents\n  - x^21: multiplying exponents\n  - 1: wrong operation",
            solution_steps_ar='["Rule: a^m / a^n = a^(m - n)","x^(7-3) = x^4"]',
    tags="exponent", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 67
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.5,
            text_ar="Factor the expression:\nx^2 - 25",
            option_a="(x - 5)^2", option_b="(x + 5)(x - 5)", option_c="(x - 25)(x + 1)", option_d="(x + 1)(x - 25)",
            correct_option="b",
            explanation_ar="Solution:\n  Difference of squares: x^2 - 5^2 = (x + 5)(x - 5)\n\nWhy other options are wrong:\n  - A: perfect square error\n  - C and D: wrong factors",
            solution_steps_ar='["x^2 - 25 = x^2 - 5^2","Difference of squares: (x + 5)(x - 5)"]',
    tags="factoring", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 68
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.5,
            text_ar="If:\nx + 3y = 14\nx - y = 2\nWhat is the value of y?",
            option_a="2", option_b="3", option_c="4", option_d="5",
            correct_option="b",
            explanation_ar="Solution:\n  Subtract eq2 from eq1: 4y = 12, so y = 3\n\nWhy other options are wrong:\n  - 2: wrong subtraction\n  - 4: calculation error\n  - 5: wrong equation",
            solution_steps_ar='["(x + 3y) - (x - y) = 14 - 2","4y = 12","y = 3"]',
    tags="linear-equation,function", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 69
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.5,
            text_ar="If:\nx^2 = 81\nWhat are the possible values of x?",
            option_a="9 only", option_b="-9 only", option_c="+9 or -9", option_d="81",
            correct_option="c",
            explanation_ar="Solution:\n  x = +/- sqrt(81) = +/- 9\n\nWhy other options are wrong:\n  - 9 only: missing negative\n  - -9 only: missing positive\n  - 81: wrong interpretation",
            solution_steps_ar='["x^2 = 81","x = +/- sqrt(81)","x = 9 or x = -9"]',
    tags="quadratic", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 70
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.5,
            text_ar="Solve the inequality:\n4x + 1 <= 17",
            option_a="x <= 3", option_b="x <= 4", option_c="x <= 5", option_d="x >= 4",
            correct_option="b",
            explanation_ar="Solution:\n  4x <= 16, so x <= 4\n\nWhy other options are wrong:\n  - x <= 3: wrong division\n  - x <= 5: wrong calculation\n  - x >= 4: wrong direction",
            solution_steps_ar='["4x + 1 <= 17","Subtract 1: 4x <= 16","Divide by 4: x <= 4"]',
    tags="inequality", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 71
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.5,
            text_ar="If y is inversely proportional to x, and y = 10 when x = 3.\nWhat is the value of y when x = 6?",
            option_a="3", option_b="5", option_c="15", option_d="20",
            correct_option="b",
            explanation_ar="Solution:\n  k = 10 * 3 = 30\n  y = 30 / 6 = 5\n\nWhy other options are wrong:\n  - 3: wrong operation\n  - 15: wrong constant\n  - 20: wrong formula",
            solution_steps_ar='["k = y * x = 10 * 3 = 30","When x = 6: y = 30 / 6 = 5"]',
    tags="proportion", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 72
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.5,
            text_ar="If f(x) = 2x^2 - 3\nWhat is the value of f(4)?",
            option_a="29", option_b="31", option_c="32", option_d="35",
            correct_option="a",
            explanation_ar="Solution:\n  f(4) = 2 * 16 - 3 = 32 - 3 = 29\n\nWhy other options are wrong:\n  - 31: calculation error\n  - 32: forgetting subtraction\n  - 35: wrong operation",
            solution_steps_ar='["f(4) = 2 * 4^2 - 3","= 32 - 3 = 29"]',
    tags="quadratic,function", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 73
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.5,
            text_ar="What is the sum of numbers from 1 to 20?",
            option_a="190", option_b="200", option_c="210", option_d="220",
            correct_option="c",
            explanation_ar="Formula:\n  Sum = 20 * 21 / 2 = 210\n\nWhy other options are wrong:\n  - 190: wrong calculation\n  - 200: using n^2\n  - 220: wrong formula",
            solution_steps_ar='["Sum = n(n + 1) / 2","= 20 * 21 / 2 = 210"]',
    tags="sequence", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 74
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.5,
            text_ar="Factor the expression:\nx^2 - 7x + 12",
            option_a="(x - 2)(x - 6)", option_b="(x - 3)(x - 4)", option_c="(x - 1)(x - 12)", option_d="(x + 3)(x + 4)",
            correct_option="b",
            explanation_ar="Solution:\n  Two numbers with product 12 and sum 7: 3 and 4\n  (x - 3)(x - 4)\n\nWhy other options are wrong:\n  - A: wrong pair\n  - C: wrong sum\n  - D: sign error",
            solution_steps_ar='["Find two numbers with product = 12 and sum = 7","The numbers: 3 and 4","Therefore (x - 3)(x - 4)"]',
    tags="factoring", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 75
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.5,
            text_ar="If:\nx/2 + 3 = 7\nWhat is the value of x?",
            option_a="2", option_b="4", option_c="8", option_d="14",
            correct_option="c",
            explanation_ar="Solution:\n  x/2 = 4, so x = 8\n\nWhy other options are wrong:\n  - 2: wrong operation\n  - 4: incomplete solution\n  - 14: wrong addition",
            solution_steps_ar='["x/2 + 3 = 7","Subtract 3: x/2 = 4","Multiply by 2: x = 8"]',
    tags="linear-equation", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 76
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.5,
            text_ar="Simplify:\nsqrt(72)",
            option_a="6sqrt(2)", option_b="3sqrt(8)", option_c="2sqrt(18)", option_d="9sqrt(2)",
            correct_option="a",
            explanation_ar="Solution:\n  sqrt(72) = sqrt(36 * 2) = 6sqrt(2)\n\nWhy other options are wrong:\n  - B: not simplified\n  - C: not fully simplified\n  - D: wrong extraction",
            solution_steps_ar='["sqrt(72) = sqrt(36 * 2)","= 6sqrt(2)"]',
    tags="radical", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 77
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.5,
            text_ar="If:\n2x + 3y = 12\nand x = 3\nWhat is the value of y?",
            option_a="1", option_b="2", option_c="3", option_d="4",
            correct_option="b",
            explanation_ar="Solution:\n  6 + 3y = 12, so 3y = 6, so y = 2\n\nWhy other options are wrong:\n  - 1: wrong calculation\n  - 3: using x value\n  - 4: wrong operation",
            solution_steps_ar='["Substitute x = 3: 6 + 3y = 12","3y = 6","y = 2"]',
    tags="linear-equation,function", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),


        # --- Difficulty 0.6 (need 22 total, have 2, adding 20) ---

        # 78
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.6,
            text_ar="Simplify:\n(3^2 * 3^5) / 3^4",
            option_a="3^3", option_b="3^7", option_c="3^11", option_d="9",
            correct_option="a",
            explanation_ar="Solution:\n  3^(2+5) / 3^4 = 3^7 / 3^4 = 3^3 = 27\n\nWhy other options are wrong:\n  - 3^7: partial calculation\n  - 3^11: wrong operation\n  - 9: wrong base",
            solution_steps_ar='["3^2 * 3^5 = 3^7","3^7 / 3^4 = 3^3","= 27"]',
    tags="exponent", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 79
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.6,
            text_ar="Solve the equation:\nx^2 + 2x - 8 = 0",
            option_a="2, -4", option_b="-2, 4", option_c="2, 4", option_d="-2, -4",
            correct_option="a",
            explanation_ar="Solution:\n  (x + 4)(x - 2) = 0\n  x = 2 or x = -4\n\nWhy other options are wrong:\n  - B: sign error\n  - C: missing negative\n  - D: both signs wrong",
            solution_steps_ar='["Product = -8, Sum = 2, so 4 and -2","(x + 4)(x - 2) = 0","x = 2 or x = -4"]',
    tags="quadratic", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 80
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.6,
            text_ar="A geometric sequence has first term 2 and common ratio 3.\nWhat is the 5th term?",
            option_a="54", option_b="122", option_c="162", option_d="243",
            correct_option="c",
            explanation_ar="Solution:\n  a_5 = 2 * 3^4 = 2 * 81 = 162\n\nWhy other options are wrong:\n  - 54: using 3^3\n  - 122: wrong formula\n  - 243: forgetting to multiply by a_1",
            solution_steps_ar='["a_n = a_1 * r^(n-1)","a_5 = 2 * 3^4 = 2 * 81 = 162"]',
    tags="sequence", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # 81
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.6,
            text_ar="If:\n2x - y = 5\nx + y = 7\nWhat is the value of x?",
            option_a="3", option_b="4", option_c="5", option_d="6",
            correct_option="b",
            explanation_ar="Solution:\n  Adding equations: 3x = 12, so x = 4\n\nWhy other options are wrong:\n  - 3: wrong addition\n  - 5: wrong coefficient\n  - 6: calculation error",
            solution_steps_ar='["Add equations: 3x = 12","x = 4"]',
    tags="linear-equation,function", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # 82
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.6,
            text_ar="Factor the expression:\nx^2 - 8x + 16",
            option_a="(x - 4)^2", option_b="(x - 8)(x - 2)", option_c="(x + 4)^2", option_d="(x - 1)(x - 16)",
            correct_option="a",
            explanation_ar="Solution:\n  16 = 4^2 and 2*4 = 8\n  Perfect square: (x - 4)^2\n\nWhy other options are wrong:\n  - B: wrong factors\n  - C: wrong sign\n  - D: wrong pair",
            solution_steps_ar='["16 = 4^2","2 * 4 = 8 (middle coefficient)","Therefore perfect square: (x - 4)^2"]',
    tags="factoring", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # 83
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.6,
            text_ar="What is the value of 27^(1/3)?",
            option_a="3", option_b="9", option_c="27", option_d="81",
            correct_option="a",
            explanation_ar="Solution:\n  27^(1/3) = cube root of 27 = 3\n\nWhy other options are wrong:\n  - 9: squaring\n  - 27: not taking root\n  - 81: wrong operation",
            solution_steps_ar='["a^(1/n) = the nth root of a","27^(1/3) = cube root of 27 = 3"]',
    tags="exponent", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # 84
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.6,
            text_ar="Solve the equation:\n|x - 4| = 6\nWhat is the product of the two solutions?",
            option_a="-20", option_b="-10", option_c="10", option_d="20",
            correct_option="a",
            explanation_ar="Solution:\n  Case 1: x - 4 = 6, so x = 10\n  Case 2: x - 4 = -6, so x = -2\n  Product = 10 * (-2) = -20\n\nWhy other options are wrong:\n  - -10: wrong calculation\n  - 10: ignoring negative\n  - 20: wrong product",
            solution_steps_ar='["Case 1: x - 4 = 6, x = 10","Case 2: x - 4 = -6, x = -2","Product = 10 * (-2) = -20"]',
    tags="absolute-value", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # 85
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.6,
            text_ar="Solve the inequality:\n-3 < 2x + 1 < 9",
            option_a="-1 < x < 5", option_b="-2 < x < 4", option_c="0 < x < 4", option_d="-1 < x < 4",
            correct_option="b",
            explanation_ar="Solution:\n  Subtract 1: -4 < 2x < 8\n  Divide by 2: -2 < x < 4\n\nWhy other options are wrong:\n  - A: wrong subtraction\n  - C: missing negative\n  - D: wrong calculation",
            solution_steps_ar='["-3 < 2x + 1 < 9","Subtract 1: -4 < 2x < 8","Divide by 2: -2 < x < 4"]',
    tags="inequality", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # 86
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.6,
            text_ar="If:\n(x + 3)/4 = (x - 1)/2\nWhat is the value of x?",
            option_a="3", option_b="5", option_c="7", option_d="9",
            correct_option="b",
            explanation_ar="Solution:\n  Multiply by 4: x + 3 = 2(x - 1)\n  x + 3 = 2x - 2\n  5 = x\n\nWhy other options are wrong:\n  - 3: wrong distribution\n  - 7: sign error\n  - 9: wrong multiplication",
            solution_steps_ar='["Multiply by 4: x + 3 = 2(x - 1)","x + 3 = 2x - 2","5 = x"]',
    tags="linear-equation", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # 87
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.6,
            text_ar="What is the domain of the function:\nf(x) = 1 / (x - 3)?",
            option_a="All real numbers", option_b="All real numbers except 3", option_c="x > 3", option_d="x >= 3",
            correct_option="b",
            explanation_ar="Solution:\n  Denominator != 0: x - 3 != 0, so x != 3\n\nWhy other options are wrong:\n  - A: ignoring denominator restriction\n  - C: incomplete domain\n  - D: including boundary",
            solution_steps_ar='["Condition: Denominator != 0","x - 3 != 0, so x != 3","Domain: All real numbers except 3"]',
    tags="function", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # 88
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.6,
            text_ar="Simplify:\nsqrt(48) + sqrt(27)",
            option_a="5sqrt(3)", option_b="7sqrt(3)", option_c="9sqrt(3)", option_d="12sqrt(3)",
            correct_option="b",
            explanation_ar="Solution:\n  sqrt(48) = 4sqrt(3)\n  sqrt(27) = 3sqrt(3)\n  Sum = 7sqrt(3)\n\nWhy other options are wrong:\n  - A: wrong simplification\n  - C: wrong addition\n  - D: adding coefficients incorrectly",
            solution_steps_ar='["sqrt(48) = 4sqrt(3)","sqrt(27) = 3sqrt(3)","Sum = 4sqrt(3) + 3sqrt(3) = 7sqrt(3)"]',
    tags="radical", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # 89
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.6,
            text_ar="If:\n3x + 2y = 16\nx - y = 1\nWhat is the value of x?",
            option_a="2", option_b="3.6", option_c="4", option_d="5",
            correct_option="b",
            explanation_ar="Solution:\n  From eq2: x = y + 1\n  Substitute: 3(y + 1) + 2y = 16\n  5y + 3 = 16, so 5y = 13, so y = 2.6\n  x = 2.6 + 1 = 3.6\n\nWhy other options are wrong:\n  - 2: wrong calculation\n  - 4: approximation error\n  - 5: wrong equation",
            solution_steps_ar='["From eq2: x = y + 1","Substitute: 3(y + 1) + 2y = 16","5y = 13, y = 2.6, x = 3.6"]',
    tags="linear-equation,function", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # 90
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.6,
            text_ar="If 3^n = 81\nWhat is the value of n?",
            option_a="2", option_b="3", option_c="4", option_d="5",
            correct_option="c",
            explanation_ar="Solution:\n  3^4 = 81\n  Therefore n = 4\n\nWhy other options are wrong:\n  - 2: wrong power\n  - 3: 3^3 = 27\n  - 5: too high",
            solution_steps_ar='["3^n = 81","3^4 = 81","Therefore n = 4"]',
    tags="exponent", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # 91
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.6,
            text_ar="Solve the equation:\nx^2 - 9x + 20 = 0",
            option_a="4, 5", option_b="-4, -5", option_c="2, 10", option_d="-4, 5",
            correct_option="a",
            explanation_ar="Solution:\n  (x - 4)(x - 5) = 0\n  x = 4 or x = 5\n\nWhy other options are wrong:\n  - B: sign error\n  - C: wrong factors\n  - D: mixed signs",
            solution_steps_ar='["Product = 20, Sum = 9, so 4 and 5","(x - 4)(x - 5) = 0","x = 4 or x = 5"]',
    tags="quadratic", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # 92
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.6,
            text_ar="If y is directly proportional to the square of x, and y = 20 when x = 2.\nWhat is the value of y when x = 3?",
            option_a="30", option_b="45", option_c="60", option_d="90",
            correct_option="b",
            explanation_ar="Solution:\n  k = 20 / 4 = 5\n  y = 5 * 9 = 45\n\nWhy other options are wrong:\n  - 30: wrong formula\n  - 60: wrong constant\n  - 90: doubling error",
            solution_steps_ar='["y = k * x^2, so k = 20 / 4 = 5","When x = 3: y = 5 * 9 = 45"]',
    tags="proportion", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # 93
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.6,
            text_ar="Solve the equation:\nsqrt(x + 5) = 4\nWhat is the value of x?",
            option_a="9", option_b="11", option_c="16", option_d="21",
            correct_option="b",
            explanation_ar="Solution:\n  Square both sides: x + 5 = 16\n  x = 11\n\nWhy other options are wrong:\n  - 9: wrong subtraction\n  - 16: using squared value\n  - 21: adding instead of subtracting",
            solution_steps_ar='["Square both sides: x + 5 = 16","x = 16 - 5 = 11"]',
    tags="linear-equation,radical", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # 94
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.6,
            text_ar="Factor the expression:\n4x^2 - 1",
            option_a="(2x - 1)^2", option_b="(2x + 1)(2x - 1)", option_c="(4x + 1)(x - 1)", option_d="2(2x^2 - 1)",
            correct_option="b",
            explanation_ar="Solution:\n  Difference of squares: (2x)^2 - 1^2 = (2x + 1)(2x - 1)\n\nWhy other options are wrong:\n  - A: perfect square error\n  - C: wrong factors\n  - D: incomplete factoring",
            solution_steps_ar='["4x^2 - 1 = (2x)^2 - 1^2","Difference of squares","Therefore (2x + 1)(2x - 1)"]',
    tags="factoring", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # 95
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.6,
            text_ar="An arithmetic sequence has 3rd term 11 and 7th term 23.\nWhat is the common difference?",
            option_a="2", option_b="3", option_c="4", option_d="5",
            correct_option="b",
            explanation_ar="Solution:\n  a_7 - a_3 = 4d\n  23 - 11 = 12, so d = 3\n\nWhy other options are wrong:\n  - 2: wrong calculation\n  - 4: off-by-one\n  - 5: wrong formula",
            solution_steps_ar='["a_7 - a_3 = (7 - 3) * d","12 = 4d, so d = 3"]',
    tags="sequence", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # 96
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.6,
            text_ar="If f(x) = 2x + 1 and g(x) = x^2\nWhat is the value of f(g(3))?",
            option_a="19", option_b="37", option_c="49", option_d="63",
            correct_option="a",
            explanation_ar="Solution:\n  g(3) = 9\n  f(9) = 19\n\nWhy other options are wrong:\n  - 37: wrong order\n  - 49: g(7)\n  - 63: wrong calculation",
            solution_steps_ar='["g(3) = 3^2 = 9","f(9) = 2 * 9 + 1 = 19"]',
    tags="quadratic,function", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # 97
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.6,
            text_ar="Simplify:\n(2^5 * 2^3) / 2^6",
            option_a="2^2", option_b="2^4", option_c="2^14", option_d="4",
            correct_option="a",
            explanation_ar="Solution:\n  2^8 / 2^6 = 2^2 = 4\n\nWhy other options are wrong:\n  - 2^4: wrong subtraction\n  - 2^14: adding all\n  - 4: correct value but wrong form",
            solution_steps_ar='["2^5 * 2^3 = 2^8","2^8 / 2^6 = 2^2 = 4"]',
    tags="exponent", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),


        # --- Difficulty 0.7 (need 11 total, have 1, adding 10) ---

        # 98
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.7,
            text_ar="Solve the equation:\n2x^2 - 7x + 3 = 0",
            option_a="3, 1/2", option_b="3, -1/2", option_c="-3, 1/2", option_d="-3, -1/2",
            correct_option="a",
            explanation_ar="Solution:\n  (2x - 1)(x - 3) = 0\n  x = 1/2 or x = 3\n\nWhy other options are wrong:\n  - B: sign error\n  - C: wrong signs\n  - D: both signs wrong",
            solution_steps_ar='["2x^2 - 7x + 3 = 0","(2x - 1)(x - 3) = 0","x = 1/2 or x = 3"]',
    tags="quadratic", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # 99
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.7,
            text_ar="If:\n2x + 3y = 19\n3x - y = 1\nWhat is the value of x + y?",
            option_a="5", option_b="7", option_c="9", option_d="11",
            correct_option="b",
            explanation_ar="Solution:\n  From eq2: y = 3x - 1\n  Substitute: 2x + 3(3x - 1) = 19\n  11x - 3 = 19, so 11x = 22, so x = 2\n  y = 3(2) - 1 = 5\n  x + y = 7\n\nWhy other options are wrong:\n  - 5: using y value\n  - 9: wrong addition\n  - 11: wrong sum",
            solution_steps_ar='["From eq2: y = 3x - 1","Substitute: 11x - 3 = 19, x = 2","y = 5, x + y = 7"]',
    tags="linear-equation,function", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # 100
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.7,
            text_ar="An arithmetic sequence has first term 5 and common difference 3.\nHow many terms are needed for the last term to be 38?",
            option_a="10", option_b="11", option_c="12", option_d="13",
            correct_option="c",
            explanation_ar="Solution:\n  38 = 5 + (n - 1) * 3\n  33 = 3(n - 1)\n  n = 12\n\nWhy other options are wrong:\n  - 10: wrong calculation\n  - 11: off-by-one\n  - 13: wrong formula",
            solution_steps_ar='["38 = 5 + (n - 1) * 3","33 = 3(n - 1)","n - 1 = 11, n = 12"]',
    tags="sequence", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # 101
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.7,
            text_ar="If 4^x = 64\nWhat is the value of 2^x?",
            option_a="4", option_b="8", option_c="16", option_d="32",
            correct_option="b",
            explanation_ar="Solution:\n  (2^2)^x = 2^6, so 2x = 6, so x = 3\n  2^3 = 8\n\nWhy other options are wrong:\n  - 4: wrong power\n  - 16: wrong calculation\n  - 32: wrong base",
            solution_steps_ar='["4^x = 64, so (2^2)^x = 2^6","2x = 6, x = 3","2^3 = 8"]',
    tags="exponent", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # 102
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.7,
            text_ar="Solve the equation:\nx^2 + 3x - 10 = 0",
            option_a="2, -5", option_b="-2, 5", option_c="5, -2", option_d="-5, -2",
            correct_option="a",
            explanation_ar="Solution:\n  (x + 5)(x - 2) = 0\n  x = 2 or x = -5\n\nWhy other options are wrong:\n  - B: sign error\n  - C: wrong order\n  - D: both negative",
            solution_steps_ar='["Product = -10, Sum = 3, so 5 and -2","(x + 5)(x - 2) = 0","x = 2 or x = -5"]',
    tags="quadratic", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # 103
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.7,
            text_ar="What is the domain of the function:\nf(x) = sqrt(2x - 6)?",
            option_a="x >= 3", option_b="x > 3", option_c="x >= 6", option_d="All real numbers",
            correct_option="a",
            explanation_ar="Solution:\n  2x - 6 >= 0, so 2x >= 6, so x >= 3\n\nWhy other options are wrong:\n  - x > 3: excluding boundary\n  - x >= 6: wrong coefficient\n  - All real: ignoring restriction",
            solution_steps_ar='["Condition: 2x - 6 >= 0","2x >= 6, x >= 3"]',
    tags="function,radical", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # 104
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.7,
            text_ar="Sum of first 4 terms of a geometric sequence with first term 2 and common ratio 3.\nWhat is the sum?",
            option_a="40", option_b="62", option_c="80", option_d="120",
            correct_option="c",
            explanation_ar="Solution:\n  Terms: 2, 6, 18, 54\n  Sum = 80\n\nWhy other options are wrong:\n  - 40: wrong calculation\n  - 62: using arithmetic\n  - 120: wrong formula",
            solution_steps_ar='["Terms: 2, 6, 18, 54","Sum = 2 + 6 + 18 + 54 = 80"]',
    tags="sequence", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # 105
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.7,
            text_ar="Simplify:\n(x^2 - 4) / (x + 2)",
            option_a="x - 4", option_b="x - 2", option_c="x + 2", option_d="x^2 - 2",
            correct_option="b",
            explanation_ar="Solution:\n  (x + 2)(x - 2) / (x + 2) = x - 2\n\nWhy other options are wrong:\n  - x - 4: wrong factoring\n  - x + 2: not simplifying\n  - x^2 - 2: wrong division",
            solution_steps_ar='["Factor: x^2 - 4 = (x + 2)(x - 2)","Cancel (x + 2)","= x - 2"]',
    tags="quadratic,factoring", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # 106
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.7,
            text_ar="Solve the inequality:\n|x - 3| < 5",
            option_a="-2 < x < 8", option_b="-5 < x < 5", option_c="x > 8 or x < -2", option_d="-8 < x < 2",
            correct_option="a",
            explanation_ar="Solution:\n  -5 < x - 3 < 5\n  -2 < x < 8\n\nWhy other options are wrong:\n  - B: wrong range\n  - C: OR instead of AND\n  - D: wrong calculation",
            solution_steps_ar='["|x - 3| < 5","-5 < x - 3 < 5","Add 3: -2 < x < 8"]',
    tags="inequality,absolute-value", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # 107
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.7,
            text_ar="If f(x) = x^2 - 4x + 3\nWhat is the value of f(0) + f(1)?",
            option_a="3", option_b="4", option_c="5", option_d="6",
            correct_option="a",
            explanation_ar="Solution:\n  f(0) = 0 - 0 + 3 = 3\n  f(1) = 1 - 4 + 3 = 0\n  Sum = 3\n\nWhy other options are wrong:\n  - 4: wrong calculation\n  - 5: sign error\n  - 6: wrong addition",
            solution_steps_ar='["f(0) = 0 - 0 + 3 = 3","f(1) = 1 - 4 + 3 = 0","Sum = 3 + 0 = 3"]',
    tags="quadratic,function", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # --- Difficulty 0.8 (need 6 total, have 2, adding 4) ---

        # 108
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.8,
            text_ar="Solve the equation:\nx^2 - 6x + 5 = 0\nWhat is the difference between the roots?",
            option_a="2", option_b="4", option_c="5", option_d="6",
            correct_option="b",
            explanation_ar="Solution:\n  (x - 1)(x - 5) = 0\n  Difference = 5 - 1 = 4\n\nWhy other options are wrong:\n  - 2: wrong calculation\n  - 5: using larger root\n  - 6: sum of roots",
            solution_steps_ar='["(x - 1)(x - 5) = 0","x = 1 or x = 5","Difference = 5 - 1 = 4"]',
    tags="quadratic,radical", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # 109
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.8,
            text_ar="If:\nx + 3y = 11\n2x - y = 1\nWhat is the value of 2x + y?",
            option_a="7", option_b="9", option_c="10", option_d="11",
            correct_option="a",
            explanation_ar="Solution:\n  From eq2: y = 2x - 1\n  Substitute in eq1: x + 3(2x - 1) = 11\n  7x - 3 = 11, so 7x = 14, so x = 2\n  y = 2(2) - 1 = 3\n  2x + y = 4 + 3 = 7\n\nWhy other options are wrong:\n  - 9: wrong calculation\n  - 10: sign error\n  - 11: using total",
            solution_steps_ar='["From eq2: y = 2x - 1","Substitute: 7x - 3 = 11, x = 2","y = 3, 2x + y = 4 + 3 = 7"]',
    tags="linear-equation,function", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # 110
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.8,
            text_ar="Sum of an infinite decreasing geometric series:\nFirst term 12 and common ratio 1/3.\nWhat is the sum?",
            option_a="15", option_b="18", option_c="24", option_d="36",
            correct_option="b",
            explanation_ar="Formula:\n  Sum = a_1 / (1 - r) = 12 / (2/3) = 18\n\nWhy other options are wrong:\n  - 15: wrong ratio\n  - 24: using arithmetic\n  - 36: wrong formula",
            solution_steps_ar='["Sum = a_1 / (1 - r)","= 12 / (1 - 1/3) = 12 / (2/3)","= 12 * 3/2 = 18"]',
    tags="sequence", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        # 111
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.8,
            text_ar="If:\n9^x = 27\nWhat is the value of x?",
            option_a="1.5", option_b="2", option_c="2.5", option_d="3",
            correct_option="a",
            explanation_ar="Solution:\n  (3^2)^x = 3^3\n  3^(2x) = 3^3\n  2x = 3, so x = 1.5\n\nWhy other options are wrong:\n  - 2: wrong power\n  - 2.5: wrong calculation\n  - 3: wrong base",
            solution_steps_ar='["9 = 3^2, 27 = 3^3","3^(2x) = 3^3","2x = 3, x = 1.5"]',
    tags="exponent", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        # ══════════════════════════════════════════════════════════════
        # New Questions (112 - 167)
        # ══════════════════════════════════════════════════════════════

        # 112 - Completing the square - diff 0.2 - diagnostic
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.2,
            text_ar="What number do we add to both sides to complete the square in:\nx^2 + 4x = 5?",
            option_a="2", option_b="4", option_c="8", option_d="16",
            correct_option="b",
            explanation_ar="Solution:\n  Take half the coefficient of x, then square it:\n  (4 / 2)^2 = 4\n  Add 4 to both sides\n\nWhy other options are wrong:\n  - 2: not squared\n  - 8: wrong calculation\n  - 16: squared coefficient",
            solution_steps_ar='["Coefficient of x = 4","Half of it = 2","Square of half = 4","Add 4 to both sides"]',
    tags="quadratic", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # 113 - Simple linear equation - diff 0.2 - diagnostic
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.2,
            text_ar="If:\nx + 9 = 15\nWhat is the value of x?",
            option_a="4", option_b="5", option_c="6", option_d="7",
            correct_option="c",
            explanation_ar="Solution:\n  x = 15 - 9 = 6\n\nWhy other options are wrong:\n  - 4: wrong subtraction\n  - 5: using 14-9\n  - 7: adding instead",
            solution_steps_ar='["x + 9 = 15","Subtract 9 from both sides","x = 6"]',
    tags="linear-equation", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # 114 - Simple arithmetic sequence - diff 0.2 - diagnostic
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.2,
            text_ar="In the arithmetic sequence:\n3, 7, 11, 15, ...\nWhat is the next term?",
            option_a="17", option_b="18", option_c="19", option_d="20",
            correct_option="c",
            explanation_ar="Solution:\n  Common difference = 7 - 3 = 4\n  Next term = 15 + 4 = 19\n\nWhy other options are wrong:\n  - 17: wrong difference\n  - 18: wrong pattern\n  - 20: wrong difference",
            solution_steps_ar='["Common difference = 7 - 3 = 4","Next term = 15 + 4 = 19"]',
    tags="sequence", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # 115 - Basic logarithm - diff 0.3 - foundation
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.3,
            text_ar="What is the value of:\nlog_2(8)?",
            option_a="2", option_b="3", option_c="4", option_d="8",
            correct_option="b",
            explanation_ar="Solution:\n  log_2(8) = ? means 2^? = 8\n  2^3 = 8\n  Therefore log_2(8) = 3\n\nWhy other options are wrong:\n  - 2: confusing base and result\n  - 4: wrong power\n  - 8: returning argument",
            solution_steps_ar='["log_2(8) = x means 2^x = 8","2^3 = 8","Therefore log_2(8) = 3"]',
    tags="logarithm", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # 116 - Logarithm - diff 0.3 - foundation
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.3,
            text_ar="What is the value of:\nlog_10(1000)?",
            option_a="2", option_b="3", option_c="4", option_d="10",
            correct_option="b",
            explanation_ar="Solution:\n  log_10(1000) = ? means 10^? = 1000\n  10^3 = 1000\n  Therefore log_10(1000) = 3\n\nWhy other options are wrong:\n  - 2: 10^2 = 100\n  - 4: wrong power\n  - 10: returning base",
            solution_steps_ar='["10^x = 1000","10^3 = 1000","Therefore log_10(1000) = 3"]',
    tags="logarithm", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # 117 - Domain of function - diff 0.3 - foundation
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.3,
            text_ar="What is the domain of the function:\nf(x) = 1 / (x - 3)?",
            option_a="All real numbers", option_b="R - {0}", option_c="R - {3}", option_d="R - {-3}",
            correct_option="c",
            explanation_ar="Solution:\n  Denominator cannot be zero:\n  x - 3 != 0, so x != 3\n  Domain = R - {3}\n\nWhy other options are wrong:\n  - A: ignoring restriction\n  - B: wrong value\n  - D: sign error",
            solution_steps_ar='["Denominator != 0","x - 3 != 0","x != 3","Domain = R - {3}"]',
    tags="function", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),


        # 118 - Simplifying radical expression - diff 0.3 - foundation
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.3,
            text_ar="Simplify:\nsqrt(50)",
            option_a="5sqrt(2)", option_b="2sqrt(5)", option_c="10sqrt(5)", option_d="25sqrt(2)",
            correct_option="a",
            explanation_ar="Solution:\n  sqrt(50) = sqrt(25 * 2) = 5sqrt(2)\n\nWhy other options are wrong:\n  - B: wrong factors\n  - C: not simplifying\n  - D: wrong extraction",
            solution_steps_ar='["50 = 25 * 2","sqrt(50) = sqrt(25) * sqrt(2)","= 5sqrt(2)"]',
    tags="radical", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 119 - Simple word problem - diff 0.3 - foundation
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.3,
            text_ar="Ahmed bought 5 pens at a price of x riyals per pen.\nIf he paid 40 riyals, what is the price of one pen?",
            option_a="5", option_b="7", option_c="8", option_d="10",
            correct_option="c",
            explanation_ar="Solution:\n  5x = 40\n  x = 40 / 5 = 8 riyals\n\nWhy other options are wrong:\n  - 5: using quantity\n  - 7: wrong calculation\n  - 10: wrong division",
            solution_steps_ar='["5x = 40","x = 40 / 5","x = 8 riyals"]',
    tags="linear-equation", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 120 - Function composition - diff 0.4 - foundation
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.4,
            text_ar="If:\nf(x) = 2x + 1\ng(x) = x^2\nWhat is the value of f(g(2))?",
            option_a="5", option_b="9", option_c="10", option_d="25",
            correct_option="b",
            explanation_ar="Solution:\n  g(2) = 2^2 = 4\n  f(4) = 2 * 4 + 1 = 9\n\nWhy other options are wrong:\n  - 5: wrong order\n  - 10: calculation error\n  - 25: g(5)",
            solution_steps_ar='["g(2) = 2^2 = 4","f(4) = 2(4) + 1 = 9"]',
    tags="function", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 121 - Function composition - diff 0.4 - foundation
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.4,
            text_ar="If:\nf(x) = x + 3\ng(x) = 2x\nWhat is the value of g(f(5))?",
            option_a="13", option_b="16", option_c="10", option_d="8",
            correct_option="b",
            explanation_ar="Solution:\n  f(5) = 5 + 3 = 8\n  g(8) = 2 * 8 = 16\n\nWhy other options are wrong:\n  - 13: wrong order\n  - 10: f(5) * 2\n  - 8: stopping at f(5)",
            solution_steps_ar='["f(5) = 5 + 3 = 8","g(8) = 2 * 8 = 16"]',
    tags="function", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 122 - Domain of function - diff 0.4 - foundation
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.4,
            text_ar="What is the domain of the function:\nf(x) = sqrt(x - 2)?",
            option_a="x >= 0", option_b="x > 2", option_c="x >= 2", option_d="All real numbers",
            correct_option="c",
            explanation_ar="Solution:\n  Expression under square root >= 0\n  x - 2 >= 0, so x >= 2\n\nWhy other options are wrong:\n  - x >= 0: wrong shift\n  - x > 2: excluding boundary\n  - All real: ignoring restriction",
            solution_steps_ar='["Condition: x - 2 >= 0","x >= 2","Domain = [2, infinity)"]',
    tags="function,radical", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 123 - Simplifying rational expression - diff 0.4 - building
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.4,
            text_ar="Simplify:\n(x^2 - 9) / (x + 3)",
            option_a="x - 3", option_b="x + 3", option_c="x^2 - 3", option_d="x - 9",
            correct_option="a",
            explanation_ar="Solution:\n  x^2 - 9 = (x + 3)(x - 3)\n  (x + 3)(x - 3) / (x + 3) = x - 3\n\nWhy other options are wrong:\n  - x + 3: not factoring\n  - x^2 - 3: wrong division\n  - x - 9: wrong factoring",
            solution_steps_ar='["Factor numerator: x^2 - 9 = (x + 3)(x - 3)","Cancel (x + 3)","Result = x - 3"]',
    tags="factoring", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 124 - Sum and product of roots - diff 0.4 - building
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.4,
            text_ar="In the equation:\nx^2 - 7x + 10 = 0\nWhat is the sum of the roots?",
            option_a="5", option_b="7", option_c="10", option_d="-7",
            correct_option="b",
            explanation_ar="Solution:\n  Using Vieta's formulas:\n  Sum of roots = -(-7)/1 = 7\n\nWhy other options are wrong:\n  - 5: product of roots\n  - 10: constant term\n  - -7: sign error",
            solution_steps_ar='["Equation: x^2 - 7x + 10 = 0","Sum of roots = -b/a","= -(-7)/1 = 7"]',
    tags="quadratic", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 125 - Product of roots - diff 0.4 - building
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.4,
            text_ar="In the equation:\nx^2 - 7x + 10 = 0\nWhat is the product of the roots?",
            option_a="5", option_b="7", option_c="10", option_d="-10",
            correct_option="c",
            explanation_ar="Solution:\n  Using Vieta's formulas:\n  Product of roots = c/a = 10/1 = 10\n\nWhy other options are wrong:\n  - 5: wrong calculation\n  - 7: sum of roots\n  - -10: sign error",
            solution_steps_ar='["Equation: x^2 - 7x + 10 = 0","Product of roots = c/a","= 10/1 = 10"]',
    tags="quadratic", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 126 - Sum of arithmetic sequence - diff 0.4 - building
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.4,
            text_ar="Find the sum of the first 10 terms of the arithmetic sequence:\n2, 5, 8, 11, ...",
            option_a="145", option_b="155", option_c="160", option_d="170",
            correct_option="b",
            explanation_ar="Solution:\n  a_1 = 2, d = 3, n = 10\n  a_10 = 2 + 9 * 3 = 29\n  Sum = n/2 * (a_1 + a_n) = 10/2 * (2 + 29) = 5 * 31 = 155\n\nWhy other options are wrong:\n  - 145: wrong formula\n  - 160: calculation error\n  - 170: wrong common difference",
            solution_steps_ar='["a_10 = 2 + 9 * 3 = 29","Sum = n/2 * (a_1 + a_n)","= 5 * (2 + 29) = 155"]',
    tags="sequence", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 127 - Simplifying rational expression - diff 0.4 - building
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.4,
            text_ar="Simplify:\n(2x) / (4x^2)",
            option_a="1 / (2x)", option_b="2 / x", option_c="x / 2", option_d="1 / (4x)",
            correct_option="a",
            explanation_ar="Solution:\n  2x / 4x^2 = 2 / (4x) = 1 / (2x)\n\nWhy other options are wrong:\n  - 2/x: wrong cancellation\n  - x/2: wrong operation\n  - 1/(4x): not simplifying fully",
            solution_steps_ar='["Cancel 2x from numerator and denominator","2x / 4x^2 = 1 / (2x)"]',
    tags="proportion", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 128 - Word problem - diff 0.5 - building
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.5,
            text_ar="Ahmed's age is twice Sarah's age.\nIf the sum of their ages is 36 years, what is Sarah's age?",
            option_a="9", option_b="12", option_c="18", option_d="24",
            correct_option="b",
            explanation_ar="Solution:\n  Sarah's age = x, Ahmed's age = 2x\n  x + 2x = 36, so 3x = 36, so x = 12\n\nWhy other options are wrong:\n  - 9: wrong division\n  - 18: Ahmed's age\n  - 24: wrong calculation",
            solution_steps_ar='["Let Sarah age = x","Ahmed age = 2x","x + 2x = 36, 3x = 36","x = 12 years"]',
    tags="linear-equation", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 129 - Completing the square - diff 0.5 - building
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.5,
            text_ar="Solve by completing the square:\nx^2 + 6x + 5 = 0",
            option_a="x = -1 or x = -5", option_b="x = 1 or x = 5", option_c="x = -1 or x = 5", option_d="x = 1 or x = -5",
            correct_option="a",
            explanation_ar="Solution:\n  x^2 + 6x = -5\n  (half of 6)^2 = 9, add it\n  (x + 3)^2 = 4\n  x + 3 = +/- 2\n  x = -1 or x = -5\n\nWhy other options are wrong:\n  - B: sign error\n  - C: one wrong sign\n  - D: sign error",
            solution_steps_ar='["x^2 + 6x = -5","Add (6/2)^2 = 9 to both sides","(x + 3)^2 = 4","x + 3 = 2, x = -1","x + 3 = -2, x = -5"]',
    tags="quadratic", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 130 - Sum of geometric sequence - diff 0.5 - building
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.5,
            text_ar="Find the sum of the first 4 terms of the geometric sequence:\n3, 6, 12, 24",
            option_a="39", option_b="42", option_c="45", option_d="48",
            correct_option="c",
            explanation_ar="Solution:\n  a_1 = 3, r = 2, n = 4\n  Sum = a_1 * (r^n - 1) / (r - 1)\n  = 3 * (16 - 1) / 1 = 3 * 15 = 45\n\nWhy other options are wrong:\n  - 39: wrong formula\n  - 42: calculation error\n  - 48: adding wrong",
            solution_steps_ar='["a_1 = 3, r = 2, n = 4","Sum = 3 * (2^4 - 1) / (2 - 1)","= 3 * 15 / 1 = 45"]',
    tags="sequence", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 131 - Vieta: finding equation - diff 0.5 - building
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.5,
            text_ar="If the roots of a quadratic equation are 3 and -2\nWhat is the equation?",
            option_a="x^2 - x - 6 = 0", option_b="x^2 + x - 6 = 0", option_c="x^2 - 5x + 6 = 0", option_d="x^2 + 5x + 6 = 0",
            correct_option="a",
            explanation_ar="Solution:\n  Sum of roots = 3 + (-2) = 1\n  Product = 3 * (-2) = -6\n  Equation: x^2 - 1x + (-6) = 0, so x^2 - x - 6 = 0\n\nWhy other options are wrong:\n  - B: sign error\n  - C: wrong roots\n  - D: wrong roots",
            solution_steps_ar='["Sum of roots = 3 + (-2) = 1","Product = 3 * (-2) = -6","Equation: x^2 - (sum)x + (product) = 0","x^2 - x - 6 = 0"]',
    tags="quadratic", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 132 - Function composition - diff 0.5 - building
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.5,
            text_ar="If:\nf(x) = x^2 - 1\ng(x) = x + 2\nFind f(g(1))",
            option_a="4", option_b="8", option_c="2", option_d="6",
            correct_option="b",
            explanation_ar="Solution:\n  g(1) = 1 + 2 = 3\n  f(3) = 3^2 - 1 = 9 - 1 = 8\n\nWhy other options are wrong:\n  - 4: wrong calculation\n  - 2: wrong order\n  - 6: wrong operation",
            solution_steps_ar='["g(1) = 1 + 2 = 3","f(3) = 9 - 1 = 8"]',
    tags="function", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 133 - Polynomial division - diff 0.5 - building
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.5,
            text_ar="The result of dividing:\n(x^2 + 5x + 6) / (x + 2)",
            option_a="x + 2", option_b="x + 3", option_c="x + 4", option_d="x - 3",
            correct_option="b",
            explanation_ar="Solution:\n  x^2 + 5x + 6 = (x + 2)(x + 3)\n  / (x + 2) = x + 3\n\nWhy other options are wrong:\n  - x + 2: wrong division\n  - x + 4: wrong factors\n  - x - 3: sign error",
            solution_steps_ar='["Factor: x^2 + 5x + 6 = (x + 2)(x + 3)","Divide by (x + 2)","Result = x + 3"]',
    tags="polynomial", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 134 - Word problem - diff 0.5 - building
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.5,
            text_ar="Price of 3 books and 2 notebooks = 26 riyals.\nIf the price of a book is 6 riyals, what is the price of a notebook?",
            option_a="2", option_b="3", option_c="4", option_d="5",
            correct_option="c",
            explanation_ar="Solution:\n  3 * 6 + 2y = 26\n  18 + 2y = 26\n  2y = 8, so y = 4\n\nWhy other options are wrong:\n  - 2: wrong calculation\n  - 3: wrong division\n  - 5: wrong addition",
            solution_steps_ar='["3(6) + 2y = 26","18 + 2y = 26","2y = 8","y = 4 riyals"]',
    tags="linear-equation", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 135 - Logarithm - diff 0.5 - building
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.5,
            text_ar="What is the value of:\nlog_3(81)?",
            option_a="2", option_b="3", option_c="4", option_d="5",
            correct_option="c",
            explanation_ar="Solution:\n  3^? = 81\n  3^4 = 81\n  Therefore log_3(81) = 4\n\nWhy other options are wrong:\n  - 2: 3^2 = 9\n  - 3: 3^3 = 27\n  - 5: too high",
            solution_steps_ar='["log_3(81) = x means 3^x = 81","3^4 = 81","Therefore log_3(81) = 4"]',
    tags="logarithm", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 136 - Arithmetic sequence application - diff 0.6 - building
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.6,
            text_ar="Khalid saves 50 riyals in the first week and increases by 20 riyals each week.\nHow much has he saved after 8 weeks?",
            option_a="840", option_b="960", option_c="1000", option_d="920",
            correct_option="b",
            explanation_ar="Solution:\n  Arithmetic sequence: a_1 = 50, d = 20, n = 8\n  a_8 = 50 + 7 * 20 = 190\n  Sum = 8/2 * (50 + 190) = 4 * 240 = 960\n\nWhy other options are wrong:\n  - 840: wrong formula\n  - 1000: wrong calculation\n  - 920: wrong common difference",
            solution_steps_ar='["a_1 = 50, d = 20, n = 8","a_8 = 50 + 7(20) = 190","Sum = 4(50 + 190) = 960 riyals"]',
    tags="sequence", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 137 - Simplifying rational expression - diff 0.6 - peak
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.6,
            text_ar="Simplify:\n(x^2 - 4) / (x^2 + 4x + 4)",
            option_a="(x - 2) / (x + 2)", option_b="(x + 2) / (x - 2)", option_c="1 / (x + 2)", option_d="(x - 4) / (x + 4)",
            correct_option="a",
            explanation_ar="Solution:\n  Numerator: x^2 - 4 = (x - 2)(x + 2)\n  Denominator: x^2 + 4x + 4 = (x + 2)^2\n  = (x - 2)(x + 2) / (x + 2)^2 = (x - 2) / (x + 2)\n\nWhy other options are wrong:\n  - B: inverted\n  - C: incomplete\n  - D: wrong factors",
            solution_steps_ar='["Numerator = (x - 2)(x + 2)","Denominator = (x + 2)^2","Cancel (x + 2)","= (x - 2) / (x + 2)"]',
    tags="factoring,proportion", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # 138 - Completing the square - diff 0.6 - peak
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.6,
            text_ar="Write the function f(x) = x^2 - 8x + 10 in vertex form by completing the square.",
            option_a="(x - 4)^2 - 6", option_b="(x - 4)^2 + 6", option_c="(x - 8)^2 - 6", option_d="(x + 4)^2 - 6",
            correct_option="a",
            explanation_ar="Solution:\n  x^2 - 8x + 10\n  = (x^2 - 8x + 16) - 16 + 10\n  = (x - 4)^2 - 6\n\nWhy other options are wrong:\n  - B: sign error\n  - C: wrong shift\n  - D: wrong sign",
            solution_steps_ar='["(-8/2)^2 = 16","Add and subtract 16","(x^2 - 8x + 16) - 16 + 10","= (x - 4)^2 - 6"]',
    tags="quadratic", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),


        # 139 - Polynomial division - diff 0.6 - peak
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.6,
            text_ar="The result of dividing:\n(2x^3 + 5x^2 - 4x - 3) / (x + 3)\nWhat is the remainder?",
            option_a="0", option_b="3", option_c="6", option_d="36",
            correct_option="a",
            explanation_ar="Solution using Remainder Theorem:\n  f(-3) = 2(-27) + 5(9) - 4(-3) - 3\n  = -54 + 45 + 12 - 3 = 0\n  Therefore remainder = 0\n\nWhy other options are wrong:\n  - 3: calculation error\n  - 6: wrong substitution\n  - 36: sign error",
            solution_steps_ar='["Using Remainder Theorem: f(-3)","= 2(-27) + 5(9) - 4(-3) - 3","= -54 + 45 + 12 - 3 = 0"]',
    tags="polynomial", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # 140 - Sum and product of roots - diff 0.6 - peak
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.6,
            text_ar="If the roots of equation 2x^2 - 10x + 8 = 0 are p and q\nWhat is the value of p^2 + q^2?",
            option_a="9", option_b="17", option_c="21", option_d="25",
            correct_option="b",
            explanation_ar="Solution:\n  p + q = 10/2 = 5\n  pq = 8/2 = 4\n  p^2 + q^2 = (p + q)^2 - 2pq = 25 - 8 = 17\n\nWhy other options are wrong:\n  - 9: wrong formula\n  - 21: calculation error\n  - 25: forgetting subtraction",
            solution_steps_ar='["p + q = -b/a = 10/2 = 5","pq = c/a = 8/2 = 4","p^2 + q^2 = (p + q)^2 - 2pq","= 25 - 8 = 17"]',
    tags="quadratic", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # 141 - Word problem to system of equations - diff 0.6 - peak
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.6,
            text_ar="The sum of two numbers is 20 and the difference between them is 4.\nWhat is the larger number?",
            option_a="8", option_b="10", option_c="12", option_d="14",
            correct_option="c",
            explanation_ar="Solution:\n  x + y = 20\n  x - y = 4\n  Adding: 2x = 24, so x = 12\n\nWhy other options are wrong:\n  - 8: smaller number\n  - 10: average\n  - 14: wrong calculation",
            solution_steps_ar='["x + y = 20","x - y = 4","Adding: 2x = 24","x = 12"]',
    tags="system-of-equations", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # 142 - Function composition - diff 0.6 - peak
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.6,
            text_ar="If:\nf(x) = 3x - 2\ng(x) = x^2 + 1\nFind g(f(1))",
            option_a="2", option_b="4", option_c="10", option_d="26",
            correct_option="a",
            explanation_ar="Solution:\n  f(1) = 3(1) - 2 = 1\n  g(1) = 1^2 + 1 = 2\n\nWhy other options are wrong:\n  - 4: wrong calculation\n  - 10: wrong order\n  - 26: f(3) in g",
            solution_steps_ar='["f(1) = 3 - 2 = 1","g(1) = 1 + 1 = 2"]',
    tags="function", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # 143 - Domain of rational function - diff 0.6 - mock
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.6,
            text_ar="What is the domain of the function:\nf(x) = (x + 1) / (x^2 - 4)?",
            option_a="R - {4}", option_b="R - {2}", option_c="R - {2, -2}", option_d="R - {-4}",
            correct_option="c",
            explanation_ar="Solution:\n  Denominator != 0:\n  x^2 - 4 != 0\n  (x - 2)(x + 2) != 0\n  x != 2 and x != -2\n\nWhy other options are wrong:\n  - A: wrong value\n  - B: missing one value\n  - D: wrong value",
            solution_steps_ar='["Denominator != 0","x^2 - 4 != 0","(x - 2)(x + 2) != 0","Domain = R - {2, -2}"]',
    tags="function", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # 144 - Logarithm properties - diff 0.6 - mock
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.6,
            text_ar="What is the value of:\nlog_2(4) + log_2(8)?",
            option_a="3", option_b="5", option_c="7", option_d="12",
            correct_option="b",
            explanation_ar="Solution:\n  log_2(4) = 2\n  log_2(8) = 3\n  Sum = 2 + 3 = 5\n\nWhy other options are wrong:\n  - 3: wrong calculation\n  - 7: adding arguments\n  - 12: multiplying arguments",
            solution_steps_ar='["log_2(4) = 2 (since 2^2 = 4)","log_2(8) = 3 (since 2^3 = 8)","Sum = 2 + 3 = 5"]',
    tags="logarithm", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # 145 - Polynomial division - diff 0.6 - mock
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.6,
            text_ar="The result of dividing:\n(x^3 - 8) / (x - 2)",
            option_a="x^2 + 2x + 4", option_b="x^2 - 2x + 4", option_c="x^2 + 4", option_d="x^2 - 4",
            correct_option="a",
            explanation_ar="Solution:\n  x^3 - 8 = (x - 2)(x^2 + 2x + 4) (difference of cubes)\n  / (x - 2) = x^2 + 2x + 4\n\nWhy other options are wrong:\n  - B: sign error\n  - C: incomplete\n  - D: wrong formula",
            solution_steps_ar='["a^3 - b^3 = (a - b)(a^2 + ab + b^2)","x^3 - 8 = (x - 2)(x^2 + 2x + 4)","/ (x - 2) = x^2 + 2x + 4"]',
    tags="polynomial,factoring", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # 146 - Arithmetic sequence application - diff 0.6 - mock
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.6,
            text_ar="A theater has 15 rows.\nThe first row has 20 seats and each row has 3 more seats than the previous.\nHow many seats are in the theater?",
            option_a="555", option_b="615", option_c="450", option_d="600",
            correct_option="b",
            explanation_ar="Solution:\n  a_1 = 20, d = 3, n = 15\n  a_15 = 20 + 14 * 3 = 62\n  Sum = 15/2 * (20 + 62) = 7.5 * 82 = 615\n\nWhy other options are wrong:\n  - 555: wrong formula\n  - 450: wrong calculation\n  - 600: approximation",
            solution_steps_ar='["a_15 = 20 + 14 * 3 = 62","Sum = 15/2 * (20 + 62)","= 7.5 * 82 = 615 seats"]',
    tags="sequence", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # 147 - Simplifying rational expression - diff 0.6 - mock
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.6,
            text_ar="Simplify:\n(x^2 + 3x) / (x^2 - 9)",
            option_a="x / (x + 3)", option_b="x / (x - 3)", option_c="3 / (x - 3)", option_d="(x + 3) / x",
            correct_option="b",
            explanation_ar="Solution:\n  Numerator: x(x + 3)\n  Denominator: (x + 3)(x - 3)\n  = x / (x - 3)\n\nWhy other options are wrong:\n  - A: wrong denominator\n  - C: wrong numerator\n  - D: inverted",
            solution_steps_ar='["Numerator = x(x + 3)","Denominator = (x + 3)(x - 3)","Cancel (x + 3)","= x / (x - 3)"]',
    tags="factoring,proportion", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # 148 - Word problem to quadratic - diff 0.7 - mock
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.7,
            text_ar="A rectangular garden has length 3 meters more than its width.\nIf its area is 70 m^2, what is the width?",
            option_a="5", option_b="7", option_c="8", option_d="10",
            correct_option="b",
            explanation_ar="Solution:\n  Width = x, Length = x + 3\n  x(x + 3) = 70\n  x^2 + 3x - 70 = 0\n  (x + 10)(x - 7) = 0\n  x = 7 (positive value)\n\nWhy other options are wrong:\n  - 5: wrong factoring\n  - 8: wrong calculation\n  - 10: using length",
            solution_steps_ar='["Width = x, Length = x + 3","x(x + 3) = 70","x^2 + 3x - 70 = 0","(x + 10)(x - 7) = 0","x = 7 meters"]',
    tags="quadratic", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # 149 - Sum of geometric sequence - diff 0.7 - mock
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.7,
            text_ar="Find the sum of the first 5 terms:\n1, 3, 9, 27, ...",
            option_a="91", option_b="121", option_c="13", option_d="40",
            correct_option="b",
            explanation_ar="Solution:\n  a_1 = 1, r = 3, n = 5\n  Sum = a_1 * (r^n - 1) / (r - 1)\n  = 1 * (243 - 1) / 2 = 242 / 2 = 121\n\nWhy other options are wrong:\n  - 91: wrong formula\n  - 13: wrong calculation\n  - 40: using arithmetic",
            solution_steps_ar='["a_1 = 1, r = 3, n = 5","Sum = 1 * (3^5 - 1) / (3 - 1)","= (243 - 1) / 2 = 121"]',
    tags="sequence", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # 150 - Advanced completing the square - diff 0.7 - mock
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.7,
            text_ar="Find the minimum value of the function:\nf(x) = 2x^2 - 12x + 20",
            option_a="-2", option_b="2", option_c="3", option_d="8",
            correct_option="b",
            explanation_ar="Solution:\n  f(x) = 2(x^2 - 6x) + 20\n  = 2(x^2 - 6x + 9 - 9) + 20\n  = 2(x - 3)^2 - 18 + 20\n  = 2(x - 3)^2 + 2\n  Minimum value = 2 when x = 3\n\nWhy other options are wrong:\n  - -2: sign error\n  - 3: wrong value\n  - 8: wrong calculation",
            solution_steps_ar='["f(x) = 2(x^2 - 6x) + 20","= 2(x - 3)^2 - 18 + 20","= 2(x - 3)^2 + 2","Minimum value = 2"]',
    tags="quadratic", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # 151 - Function composition - diff 0.7 - mock
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.7,
            text_ar="If:\nf(x) = 2x + 1\ng(x) = x - 3\nFind (f o g)(x)",
            option_a="2x - 5", option_b="2x - 2", option_c="2x + 4", option_d="2x - 1",
            correct_option="a",
            explanation_ar="Solution:\n  (f o g)(x) = f(g(x)) = f(x - 3)\n  = 2(x - 3) + 1 = 2x - 6 + 1 = 2x - 5\n\nWhy other options are wrong:\n  - 2x - 2: wrong calculation\n  - 2x + 4: sign error\n  - 2x - 1: wrong constant",
            solution_steps_ar='["(f o g)(x) = f(g(x))","= f(x - 3)","= 2(x - 3) + 1","= 2x - 5"]',
    tags="function", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # 152 - Advanced logarithm - diff 0.7 - peak
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.7,
            text_ar="If:\nlog_5(x) = 2\nWhat is the value of log_5(25x)?",
            option_a="3", option_b="4", option_c="5", option_d="7",
            correct_option="b",
            explanation_ar="Solution:\n  log_5(25x) = log_5(25) + log_5(x)\n  = 2 + 2 = 4\n\nWhy other options are wrong:\n  - 3: wrong calculation\n  - 5: wrong property\n  - 7: adding 25",
            solution_steps_ar='["log_5(25x) = log_5(25) + log_5(x)","log_5(25) = 2 (since 5^2 = 25)","= 2 + 2 = 4"]',
    tags="logarithm", stage="peak",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # 153 - Polynomial division by synthetic - diff 0.7 - peak
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.7,
            text_ar="If (x - 1) is a factor of:\nx^3 - 3x^2 + kx + 2\nWhat is the value of k?",
            option_a="0", option_b="1", option_c="2", option_d="-2",
            correct_option="a",
            explanation_ar="Solution:\n  If (x - 1) is a factor then f(1) = 0\n  1 - 3 + k + 2 = 0\n  k = 0\n\nWhy other options are wrong:\n  - 1: calculation error\n  - 2: wrong substitution\n  - -2: sign error",
            solution_steps_ar='["f(1) = 0","1 - 3 + k + 2 = 0","k = 0"]',
    tags="polynomial", stage="peak",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # 154 - Word problem to system - diff 0.7 - peak
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.7,
            text_ar="Adult tickets cost 30 riyals and children tickets cost 15 riyals.\n200 tickets were sold for a total of 4500 riyals.\nHow many children tickets were sold?",
            option_a="80", option_b="100", option_c="120", option_d="150",
            correct_option="b",
            explanation_ar="Solution:\n  a + c = 200 (adults + children)\n  30a + 15c = 4500\n  From eq1: a = 200 - c\n  30(200 - c) + 15c = 4500\n  6000 - 30c + 15c = 4500\n  -15c = -1500, so c = 100\n\nWhy other options are wrong:\n  - 80: calculation error\n  - 120: wrong equation\n  - 150: wrong substitution",
            solution_steps_ar='["a + c = 200","30a + 15c = 4500","Substitute: 30(200 - c) + 15c = 4500","-15c = -1500, c = 100 children tickets"]',
    tags="system-of-equations", stage="peak",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # 155 - Advanced Vieta - diff 0.7 - mock
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.7,
            text_ar="If the roots of the equation x^2 - 6x + k = 0 are equal\nWhat is the value of k?",
            option_a="3", option_b="6", option_c="9", option_d="12",
            correct_option="c",
            explanation_ar="Solution:\n  Roots are equal when discriminant = 0\n  b^2 - 4ac = 0\n  36 - 4k = 0, so k = 9\n\nWhy other options are wrong:\n  - 3: wrong formula\n  - 6: using b\n  - 12: wrong calculation",
            solution_steps_ar='["Discriminant = 0 for equal roots","b^2 - 4ac = 0","36 - 4k = 0","k = 9"]',
    tags="quadratic", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # 156 - Domain of composite function - diff 0.7 - mock
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.7,
            text_ar="What is the domain of the function:\nf(x) = sqrt(6 - 2x)?",
            option_a="x <= 3", option_b="x >= 3", option_c="x < 3", option_d="x > 3",
            correct_option="a",
            explanation_ar="Solution:\n  6 - 2x >= 0\n  -2x >= -6\n  x <= 3 (dividing by negative reverses sign)\n\nWhy other options are wrong:\n  - x >= 3: wrong direction\n  - x < 3: excluding boundary\n  - x > 3: wrong direction and excluding",
            solution_steps_ar='["6 - 2x >= 0","-2x >= -6","Divide by -2 and reverse sign","x <= 3"]',
    tags="function,inequality", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # 157 - Simplifying complex rational expression - diff 0.7 - mock
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.7,
            text_ar="Simplify:\n(1/x - 1/y) / (1/x + 1/y)",
            option_a="(y - x) / (y + x)", option_b="(x - y) / (x + y)", option_c="xy", option_d="1",
            correct_option="a",
            explanation_ar="Solution:\n  Numerator: (y - x) / (xy)\n  Denominator: (y + x) / (xy)\n  Divide: (y - x) / (y + x)\n\nWhy other options are wrong:\n  - B: inverted\n  - C: wrong operation\n  - D: wrong simplification",
            solution_steps_ar='["Numerator = (y - x) / (xy)","Denominator = (y + x) / (xy)","Division = (y-x)/(xy) * (xy)/(y+x)","= (y - x) / (y + x)"]',
    tags="proportion", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # 158 - Infinite geometric sequence - diff 0.7 - mock
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.7,
            text_ar="Sum of an infinite geometric series:\nFirst term 10 and common ratio 1/5.\nWhat is the sum?",
            option_a="10", option_b="12.5", option_c="15", option_d="50",
            correct_option="b",
            explanation_ar="Solution:\n  Sum = a_1 / (1 - r)\n  = 10 / (1 - 1/5) = 10 / (4/5)\n  = 10 * 5/4 = 50/4 = 12.5\n\nWhy other options are wrong:\n  - 10: wrong formula\n  - 15: wrong calculation\n  - 50: forgetting division",
            solution_steps_ar='["Sum = a_1 / (1 - r)","= 10 / (1 - 1/5) = 10 / (4/5)","= 10 * 5/4 = 12.5"]',
    tags="sequence", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),


        # 159 - Completing the square with coefficient - diff 0.8 - mock
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.8,
            text_ar="Solve the equation by completing the square:\n2x^2 + 8x - 10 = 0",
            option_a="x = 1 or x = -5", option_b="x = -1 or x = 5", option_c="x = 2 or x = -5", option_d="x = -2 or x = 5",
            correct_option="a",
            explanation_ar="Solution:\n  Divide by 2: x^2 + 4x - 5 = 0\n  x^2 + 4x = 5\n  (4/2)^2 = 4, add it\n  (x + 2)^2 = 9\n  x + 2 = +/- 3\n  x = 1 or x = -5\n\nWhy other options are wrong:\n  - B: sign error\n  - C: one wrong root\n  - D: sign error",
            solution_steps_ar='["Divide by 2: x^2 + 4x - 5 = 0","x^2 + 4x = 5","Add 4: (x + 2)^2 = 9","x + 2 = 3, x = 1","x + 2 = -3, x = -5"]',
    tags="quadratic", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # 160 - Function composition and finding inverse - diff 0.8 - mock
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.8,
            text_ar="If f(x) = 3x + 6\nWhat is f^(-1)(15)?",
            option_a="2", option_b="3", option_c="4", option_d="7",
            correct_option="b",
            explanation_ar="Solution:\n  f(x) = 15, so 3x + 6 = 15\n  3x = 9, so x = 3\n  Therefore f^(-1)(15) = 3\n\nWhy other options are wrong:\n  - 2: wrong calculation\n  - 4: wrong formula\n  - 7: adding 15+6",
            solution_steps_ar='["f(x) = 15","3x + 6 = 15","3x = 9","x = 3, so f^(-1)(15) = 3"]',
    tags="function", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # 161 - Logarithm equation - diff 0.8 - mock
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.8,
            text_ar="Solve:\nlog_3(x + 5) = 3",
            option_a="14", option_b="22", option_c="27", option_d="32",
            correct_option="b",
            explanation_ar="Solution:\n  log_3(x + 5) = 3\n  x + 5 = 3^3 = 27\n  x = 27 - 5 = 22\n\nWhy other options are wrong:\n  - 14: wrong calculation\n  - 27: forgetting to subtract\n  - 32: adding 27+5",
            solution_steps_ar='["log_3(x + 5) = 3","x + 5 = 3^3 = 27","x = 22"]',
    tags="logarithm", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        # 162 - Word problem to quadratic - diff 0.8 - mock
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.8,
            text_ar="The product of two consecutive integers equals 132.\nWhat is the larger number?",
            option_a="11", option_b="12", option_c="13", option_d="14",
            correct_option="b",
            explanation_ar="Solution:\n  n(n + 1) = 132\n  n^2 + n - 132 = 0\n  (n + 12)(n - 11) = 0\n  n = 11 (positive)\n  Larger number = 12\n\nWhy other options are wrong:\n  - 11: the smaller number\n  - 13: wrong roots\n  - 14: wrong calculation",
            solution_steps_ar='["n(n + 1) = 132","n^2 + n - 132 = 0","(n + 12)(n - 11) = 0","n = 11, larger number = 12"]',
    tags="quadratic", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        # 163 - Synthetic division - diff 0.8 - mock
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.8,
            text_ar="When dividing:\nx^4 - 1\nby (x - 1), what is the result?",
            option_a="x^3 + x^2 + x + 1", option_b="x^3 - x^2 + x - 1", option_c="x^3 + 1", option_d="x^2 + 1",
            correct_option="a",
            explanation_ar="Solution:\n  x^4 - 1 = (x - 1)(x^3 + x^2 + x + 1)\n  (factorization of difference of powers)\n  / (x - 1) = x^3 + x^2 + x + 1\n\nWhy other options are wrong:\n  - B: sign error\n  - C: incomplete\n  - D: wrong degree",
            solution_steps_ar='["x^4 - 1 = (x^2 - 1)(x^2 + 1)","= (x - 1)(x + 1)(x^2 + 1)","Or use: a^4 - 1 = (a - 1)(a^3 + a^2 + a + 1)","Result = x^3 + x^2 + x + 1"]',
    tags="polynomial,factoring", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        # 164 - Vieta with fractions - diff 0.8 - mock
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.8,
            text_ar="If p and q are roots of:\nx^2 - 5x + 3 = 0\nWhat is the value of 1/p + 1/q?",
            option_a="3/5", option_b="5/3", option_c="5", option_d="3",
            correct_option="b",
            explanation_ar="Solution:\n  1/p + 1/q = (p + q) / (pq)\n  p + q = 5, pq = 3\n  = 5/3\n\nWhy other options are wrong:\n  - 3/5: inverted\n  - 5: sum only\n  - 3: product only",
            solution_steps_ar='["1/p + 1/q = (p + q) / (pq)","p + q = 5 (Vieta)","pq = 3 (Vieta)","= 5/3"]',
    tags="quadratic", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        # 165 - Word problem speed - diff 0.6 - building
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.6,
            text_ar="A car travels 240 km.\nIf its speed increased by 20 km/h, the time would decrease by 1 hour.\nWhat is the original speed?",
            option_a="40", option_b="60", option_c="80", option_d="100",
            correct_option="b",
            explanation_ar="Solution:\n  240/s - 240/(s + 20) = 1\n  Testing: 240/60 - 240/80 = 4 - 3 = 1\n  Original speed = 60 km/h\n\nWhy other options are wrong:\n  - 40: wrong calculation\n  - 80: wrong speed\n  - 100: wrong formula",
            solution_steps_ar='["Time = Distance / Speed","240/s - 240/(s + 20) = 1","Testing: 240/60 = 4, 240/80 = 3","4 - 3 = 1, so speed = 60 km/h"]',
    tags="linear-equation", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # 166 - Sum of arithmetic sequence - diff 0.5 - building
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.5,
            text_ar="Find the sum of even numbers from 2 to 20",
            option_a="90", option_b="100", option_c="110", option_d="120",
            correct_option="c",
            explanation_ar="Solution:\n  Sequence: 2, 4, 6, ..., 20\n  a_1 = 2, a_n = 20, n = 10\n  Sum = 10/2 * (2 + 20) = 5 * 22 = 110\n\nWhy other options are wrong:\n  - 90: wrong formula\n  - 100: using n^2\n  - 120: wrong calculation",
            solution_steps_ar='["Number of terms = (20 - 2)/2 + 1 = 10","Sum = n/2 * (a_1 + a_n)","= 5 * (2 + 20) = 110"]',
    tags="sequence", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # 167 - Domain of composite function - diff 0.5 - building
        Question(skill_id="quant_algebra", question_type="algebra", difficulty=0.5,
            text_ar="What is the domain of the function:\nf(x) = 1 / sqrt(x - 1)?",
            option_a="x > 0", option_b="x >= 1", option_c="x > 1", option_d="All real numbers",
            correct_option="c",
            explanation_ar="Solution:\n  Condition 1: expression under sqrt > 0 (not >= because it's in denominator)\n  x - 1 > 0, so x > 1\n\nWhy other options are wrong:\n  - x > 0: wrong shift\n  - x >= 1: including boundary\n  - All real: ignoring restrictions",
            solution_steps_ar='["Expression under sqrt > 0 (cannot equal 0 in denominator)","x - 1 > 0","x > 1","Domain = (1, infinity)"]',
    tags="function,radical", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),
    ]
