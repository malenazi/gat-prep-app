from models import Question

def get_questions():
    return [
        # ════════════════════════════════════════════════════════════════
        # ██  Analysis and Statistics — quant_statistics  (167 questions)  ██
        # ════════════════════════════════════════════════════════════════
        #
        # Distribution: 0.2->11 | 0.3->17 | 0.4->22 | 0.5->22 | 0.6->22 | 0.7->11 | 0.8->6
        #
        # ══════════════════════════════════════════════════════════════
        # Difficulty 0.2 — (11 questions)
        # ══════════════════════════════════════════════════════════════

        # Q1 — existing — mean
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.2,
            text_ar="Scores of 4 students in a math test:\n70, 80, 90, 60\nWhat is the arithmetic mean?",
            option_a="70", option_b="75", option_c="80", option_d="85",
            correct_option="b",
            explanation_ar="Given:\n  Scores: 70, 80, 90, 60\n  Number of students = 4\n\nSolution:\n  Sum = 70 + 80 + 90 + 60 = 300\n  Mean = 300  /  4 = 75\n\nWhy other options are wrong:\n  • 70 ← Division by wrong number\n  • 80 ← Forgetting one value when adding\n  • 85 ← Confusing mean with median",
            solution_steps_ar='["Sum = 70 + 80 + 90 + 60 = 300","Number of values = 4","Mean = 300  /  4 = 75"]',
    tags="mean", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # Q2 — existing — mode
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.2,
            text_ar="Scores of 8 students: 7, 5, 8, 7, 9, 7, 6, 8\nWhat is the mode?",
            option_a="5", option_b="7", option_c="8", option_d="9",
            correct_option="b",
            explanation_ar="Given:\n  Data: 7, 5, 8, 7, 9, 7, 6, 8\n\nSolution:\n  Frequencies: 5->1, 6->1, 7->3, 8->2, 9->1\n  Most frequent value = 7 (appeared 3 times)\n  Mode = 7\n\nWhy other options are wrong:\n  • 5 ← Choosing largest value instead of most frequent\n  • 8 ← Confusing mode with median\n  • 9 ← Forgetting that mode can be multiple",
            solution_steps_ar='["Sort data: 5, 6, 7, 7, 7, 8, 8, 9","Count frequencies: 7 appears 3 times (most)","Mode = 7"]',
    tags="mode", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # Q3 — new — mean (simple)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.2,
            text_ar="What is the arithmetic mean of the numbers:\n10, 20, 30?",
            option_a="15", option_b="20", option_c="25", option_d="30",
            correct_option="b",
            explanation_ar="Sum = 10 + 20 + 30 = 60\nNumber of values = 3\nMean = 60  /  3 = 20\n\nWhy other options are wrong:\n  • 15 ← Division by wrong number\n  • 25 ← Forgetting one value when adding\n  • 30 ← Confusing mean with median",
            solution_steps_ar='["Sum = 10 + 20 + 30 = 60","Number of values = 3","Mean = 60  /  3 = 20"]',
    tags="mean", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # Q4 — new — median (simple odd count)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.2,
            text_ar="Find the median of the numbers:\n1, 3, 5",
            option_a="1", option_b="3", option_c="4", option_d="5",
            correct_option="b",
            explanation_ar="Numbers are sorted: 1, 3, 5\nNumber of values = 3 (odd)\nMedian = middle value = 3\n\nWhy other options are wrong:\n  • 1 ← Not sorting data before finding median\n  • 4 ← Taking one value instead of average of two middle values (even count)\n  • 5 ← Confusing median with mode",
            solution_steps_ar='["Numbers sorted: 1, 3, 5","Number of values = 3 (odd)","Median = middle value = 3"]',
    tags="median", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # Q5 — new — range (simple)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.2,
            text_ar="What is the range of the numbers:\n5, 12, 3, 8?",
            option_a="7", option_b="8", option_c="9", option_d="12",
            correct_option="c",
            explanation_ar="Maximum value = 12\nMinimum value = 3\nRange = 12 − 3 = 9\n\nWhy other options are wrong:\n  • 7 ← Error in identifying Q1 or Q3\n  • 8 ← Confusing range with interquartile range\n  • 12 ← Forgetting to subtract minimum",
            solution_steps_ar='["Maximum value = 12","Minimum value = 3","Range = 12 − 3 = 9"]',
    tags="range", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # Q6 — new — simple probability
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.2,
            text_ar="In a box there are 6 balls: 3 red and 3 white.\nWhat is the probability of drawing a red ball?",
            option_a="1/3", option_b="1/2", option_c="2/3", option_d="1/4",
            correct_option="b",
            explanation_ar="Number of red balls = 3\nTotal number = 6\nProbability = 3  /  6 = 1/2\n\nWhy other options are wrong:\n  • 1/3 ← Forgetting the total count\n  • 2/3 ← Adding probabilities instead of calculating correctly\n  • 1/4 ← Incorrect fraction calculation",
            solution_steps_ar='["Number of red balls = 3","Total number = 6","Probability = 3  /  6 = 1/2"]',
    tags="probability", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # Q7 — new — mode (simple, all different)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.2,
            text_ar="Find the mode of the numbers:\n2, 4, 4, 6, 8",
            option_a="2", option_b="4", option_c="6", option_d="8",
            correct_option="b",
            explanation_ar="Frequencies: 2->1, 4->2, 6->1, 8->1\nMost frequent value = 4\nMode = 4\n\nWhy other options are wrong:\n  • 2 ← Choosing largest value instead of most frequent\n  • 6 ← Confusing mode with median\n  • 8 ← Forgetting that mode can be multiple",
            solution_steps_ar='["Calculate frequency of each value","4 appears twice (most)","Mode = 4"]',
    tags="mode", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # Q8 — new — probability coin
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.2,
            text_ar="When tossing a fair coin, what is the probability of getting heads?",
            option_a="1/4", option_b="1/2", option_c="1/3", option_d="1",
            correct_option="b",
            explanation_ar="Total possible outcomes = 2 (heads or tails)\nDesired outcomes = 1 (heads)\nProbability = 1/2\n\nWhy other options are wrong:\n  • 1/4 ← Incorrect denominator\n  • 1/3 ← Adding probabilities incorrectly\n  • 1 ← Forgetting there are two sides",
            solution_steps_ar='["Total possible outcomes = 2","Desired outcomes (heads) = 1","Probability = 1  /  2 = 1/2"]',
    tags="probability", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # Q9 — new — mean (5 numbers)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.2,
            text_ar="What is the arithmetic mean of the numbers:\n4, 6, 8, 10, 12?",
            option_a="6", option_b="8", option_c="10", option_d="12",
            correct_option="b",
            explanation_ar="Sum = 4 + 6 + 8 + 10 + 12 = 40\nNumber of values = 5\nMean = 40  /  5 = 8\n\nWhy other options are wrong:\n  • 6 ← Division by wrong number\n  • 10 ← Forgetting one value when adding\n  • 12 ← Confusing mean with median",
            solution_steps_ar='["Sum = 4 + 6 + 8 + 10 + 12 = 40","Number of values = 5","Mean = 40  /  5 = 8"]',
    tags="mean", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # Q10 — new — probability die
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.2,
            text_ar="If a fair die is rolled, what is the probability of getting an even number?",
            option_a="1/3", option_b="1/2", option_c="2/3", option_d="1/6",
            correct_option="b",
            explanation_ar="Even numbers: 2, 4, 6 (3 numbers)\nTotal outcomes = 6\nProbability = 3  /  6 = 1/2\n\nWhy other options are wrong:\n  • 1/3 ← Incorrect count of even numbers\n  • 2/3 ← Adding probabilities incorrectly\n  • 1/6 ← Confusing with single outcome probability",
            solution_steps_ar='["Even numbers on die: 2, 4, 6 = 3 numbers","Total faces = 6","Probability = 3  /  6 = 1/2"]',
    tags="probability", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # Q11 — new — median (even count, simple)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.2,
            text_ar="What is the median of the numbers:\n2, 4, 6, 8?",
            option_a="4", option_b="5", option_c="6", option_d="7",
            correct_option="b",
            explanation_ar="Numbers sorted: 2, 4, 6, 8\nNumber of values = 4 (even)\nMedian = (4 + 6)  /  2 = 5\n\nWhy other options are wrong:\n  • 4 ← Not sorting data before finding median\n  • 6 ← Taking one value instead of average of two middle values (even count)\n  • 7 ← Confusing median with mode",
            solution_steps_ar='["Numbers sorted: 2, 4, 6, 8","Number of values = 4 (even) -> take average of two middle values","Median = (4 + 6)  /  2 = 5"]',
    tags="median", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ══════════════════════════════════════════════════════════════
        # Difficulty 0.3 — (17 questions)
        # ══════════════════════════════════════════════════════════════

        # Q12 — existing — median
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.3,
            text_ar="Find the median of the following numbers:\n3, 7, 2, 9, 5",
            option_a="2", option_b="5", option_c="7", option_d="9",
            correct_option="b",
            explanation_ar="Step 1: Sort in ascending order\n  2, 3, 5, 7, 9\n\nStep 2: Identify median\n  Number of values = 5 (odd)\n  Median = middle value = 3rd value\n  Median = 5\n\nWhy other options are wrong:\n  • 2 ← Not sorting data before finding median\n  • 7 ← Taking wrong position\n  • 9 ← Confusing median with mode",
            solution_steps_ar='["Sort ascending: 2, 3, 5, 7, 9","Number of values = 5 (odd) -> Median = middle value","Median = 5"]',
    tags="median", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # Q13 — existing — range
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.3,
            text_ar="Find the range of the following numbers:\n15, 8, 23, 11, 4",
            option_a="11", option_b="15", option_c="19", option_d="23",
            correct_option="c",
            explanation_ar="Given:\n  Numbers: 15, 8, 23, 11, 4\n\nSolution:\n  Maximum = 23\n  Minimum = 4\n  Range = 23 − 4 = 19\n\nWhy other options are wrong:\n  • 11 ← Error in calculation\n  • 15 ← Confusing range with another measure\n  • 23 ← Forgetting to subtract minimum",
            solution_steps_ar='["Maximum value = 23","Minimum value = 4","Range = 23 − 4 = 19"]',
    tags="range", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q14 — existing — probability (football)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.3,
            text_ar="In a class of 30 students, 12 play football.\nWhat is the probability of randomly selecting a student who plays football?",
            option_a="⅕", option_b="2/5", option_c="1/2", option_d="⅗",
            correct_option="b",
            explanation_ar="Given:\n  Total = 30 students\n  Football players = 12\n\nSolution:\n  Probability = 12  /  30 = 2/5\n\nWhy other options are wrong:\n  • ⅕ ← Incorrect simplification\n  • 1/2 ← Adding probabilities incorrectly\n  • ⅗ ← Confusing with complement probability",
            solution_steps_ar='["Total = 30 students","Football players = 12","Probability = 12  /  30 = 2/5"]',
    tags="probability", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q15 — existing — combinations
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.3,
            text_ar="How many ways can 2 students be chosen from 5 to participate in a competition?",
            option_a="5", option_b="10", option_c="20", option_d="25",
            correct_option="b",
            explanation_ar="Given:\n  n = 5, r = 2\n\nSolution:\n  C(n,r) = n!  /  [r!  x  (n − r)!]\n  = 5!  /  (2!  x  3!)\n  = 120  /  (2  x  6)\n  = 120  /  12 = 10\n\nWhy other options are wrong:\n  • 5 ← Using permutations instead of combinations\n  • 20 ← Error in factorial calculation\n  • 25 ← Forgetting that order does not matter",
            solution_steps_ar='["Formula: C(n,r) = n!  /  [r!  x  (n−r)!]","= 5!  /  (2!  x  3!) = 120  /  12","= 10 ways"]',
    tags="combination", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q16 — new — weighted average (simple)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.3,
            text_ar="A student scored 80 in a subject with weight 3, and 90 in a subject with weight 2.\nWhat is the weighted average?",
            option_a="84", option_b="85", option_c="86", option_d="88",
            correct_option="a",
            explanation_ar="Given:\n  Subject 1: 80 with weight 3\n  Subject 2: 90 with weight 2\n\nSolution:\n  Average = (80 x 3 + 90 x 2)  /  (3 + 2)\n  = (240 + 180)  /  5\n  = 420  /  5 = 84\n\nWhy other options are wrong:\n  • 85 ← Division by wrong number\n  • 86 ← Calculation error\n  • 88 ← Confusing with simple mean",
            solution_steps_ar='["Sum of (score  x  weight) = 80 x 3 + 90 x 2 = 240 + 180 = 420","Sum of weights = 3 + 2 = 5","Weighted average = 420  /  5 = 84"]',
    tags="mean", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q17 — new — median (7 numbers unsorted)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.3,
            text_ar="Find the median of the numbers:\n12, 5, 8, 3, 15, 7, 10",
            option_a="7", option_b="8", option_c="10", option_d="12",
            correct_option="b",
            explanation_ar="Sorted: 3, 5, 7, 8, 10, 12, 15\nNumber of values = 7 (odd)\nMedian = 4th value = 8\n\nWhy other options are wrong:\n  • 7 ← Not sorting data before finding median\n  • 10 ← Taking wrong position\n  • 12 ← Confusing median with mode",
            solution_steps_ar='["Sorted: 3, 5, 7, 8, 10, 12, 15","Number of values = 7 (odd)","Median = 4th value = 8"]',
    tags="median", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q18 — new — probability (complement)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.3,
            text_ar="When rolling a die, what is the probability of NOT getting 6?",
            option_a="1/6", option_b="1/3", option_c="1/2", option_d="5/6",
            correct_option="d",
            explanation_ar="P(6) = 1/6\nP(not 6) = 1 − 1/6 = 5/6\n\nWhy other options are wrong:\n  • 1/6 ← This is P(6), not P(not 6)\n  • 1/3 ← Incorrect calculation\n  • 1/2 ← Confusing with even/odd probability",
            solution_steps_ar='["P(6) = 1/6","P(complement) = 1 − 1/6","= 5/6"]',
    tags="probability", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q19 — new — range with negatives
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.3,
            text_ar="What is the range of the numbers:\n−3, 2, 7, −1, 5?",
            option_a="8", option_b="9", option_c="10", option_d="12",
            correct_option="c",
            explanation_ar="Maximum = 7\nMinimum = −3\nRange = 7 − (−3) = 7 + 3 = 10\n\nWhy other options are wrong:\n  • 8 ← Error in calculation\n  • 9 ← Confusing range with IQR\n  • 12 ← Calculation error with negatives",
            solution_steps_ar='["Maximum value = 7","Minimum value = −3","Range = 7 − (−3) = 10"]',
    tags="range", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q20 — new — mean (with zero)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.3,
            text_ar="What is the arithmetic mean of the numbers:\n0, 5, 10, 15, 20?",
            option_a="8", option_b="10", option_c="12", option_d="15",
            correct_option="b",
            explanation_ar="Sum = 0 + 5 + 10 + 15 + 20 = 50\nNumber of values = 5\nMean = 50  /  5 = 10\n\nWhy other options are wrong:\n  • 8 ← Division by wrong number\n  • 12 ← Forgetting one value when adding\n  • 15 ← Confusing mean with median",
            solution_steps_ar='["Sum = 0 + 5 + 10 + 15 + 20 = 50","Number of values = 5","Mean = 50  /  5 = 10"]',
    tags="mean", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q21 — new — probability (marble bag)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.3,
            text_ar="In a bag there are 10 balls: 4 white and 6 black.\nWhat is the probability of drawing a black ball?",
            option_a="2/5", option_b="1/2", option_c="⅗", option_d="⅘",
            correct_option="c",
            explanation_ar="Number of black balls = 6\nTotal = 10\nProbability = 6  /  10 = ⅗\n\nWhy other options are wrong:\n  • 2/5 ← This is P(white)\n  • 1/2 ← Incorrect calculation\n  • ⅘ ← Confusing with another probability",
            solution_steps_ar='["Number of black balls = 6","Total = 10","Probability = 6  /  10 = ⅗"]',
    tags="probability", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q22 — new — counting principle (basic)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.3,
            text_ar="In a restaurant, there are 3 types of main dishes and 4 types of drinks.\nHow many different meals (dish + drink) can be formed?",
            option_a="7", option_b="12", option_c="16", option_d="24",
            correct_option="b",
            explanation_ar="Multiplication principle:\nNumber of meals = 3  x  4 = 12\n\nWhy other options are wrong:\n  • 7 ← Adding choices instead of multiplying\n  • 16 ← Incorrect calculation\n  • 24 ← Using permutations incorrectly",
            solution_steps_ar='["Multiplication principle: Number of choices = 3  x  4","= 12 different meals"]',
    tags="counting", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q23 — new — frequency distribution (mode)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.3,
            text_ar="Test scores of 10 students:\n5, 6, 7, 7, 8, 8, 8, 9, 9, 10\nWhat is the mode?",
            option_a="7", option_b="8", option_c="9", option_d="10",
            correct_option="b",
            explanation_ar="Frequencies: 5->1, 6->1, 7->2, 8->3, 9->2, 10->1\nMost frequent = 8 (3 times)\nMode = 8\n\nWhy other options are wrong:\n  • 7 ← Choosing largest value instead of most frequent\n  • 9 ← Confusing mode with median\n  • 10 ← Forgetting that mode can be multiple",
            solution_steps_ar='["Calculate frequency of each value","8 appears 3 times (most)","Mode = 8"]',
    tags="mode", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q24 — new — probability (letters)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.3,
            text_ar="A letter is chosen randomly from the word \"book\".\nWhat is the probability that the letter is \"o\"?",
            option_a="1/2", option_b="1/3", option_c="1/4", option_d="⅕",
            correct_option="a",
            explanation_ar="Word \"book\" has 4 letters: b, o, o, k\nTotal letters = 4\nLetter \"o\" appears 2 times\nProbability = 2  /  4 = 1/2",
            solution_steps_ar='["Word book = b, o, o, k = 4 letters","Letter o appears 2 times","Probability = 2  /  4 = 1/2"]',
    tags="probability", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q25 — new — mean with missing value
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.3,
            text_ar="The mean of 5 numbers = 6.\nIf the numbers are: 4, 5, 7, 8, x\nWhat is the value of x?",
            option_a="4", option_b="5", option_c="6", option_d="7",
            correct_option="c",
            explanation_ar="Sum = Mean  x  Number of values = 6  x  5 = 30\nSum of known = 4 + 5 + 7 + 8 = 24\nx = 30 − 24 = 6\n\nWhy other options are wrong:\n  • 4 ← Incorrect calculation\n  • 5 ← Missing one value\n  • 7 ← Confusing with another value",
            solution_steps_ar='["Total sum = 6  x  5 = 30","Sum of known numbers = 4 + 5 + 7 + 8 = 24","x = 30 − 24 = 6"]',
    tags="mean", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q26 — new — simple probability (deck subset)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.3,
            text_ar="In a box of 8 cards numbered 1 to 8.\nWhat is the probability of drawing a card with number greater than 6?",
            option_a="1/8", option_b="1/4", option_c="3/8", option_d="1/2",
            correct_option="b",
            explanation_ar="Numbers greater than 6: {7, 8} = 2 cards\nTotal = 8\nProbability = 2  /  8 = 1/4\n\nWhy other options are wrong:\n  • 1/8 ← Incorrect count\n  • 3/8 ← Wrong range of numbers\n  • 1/2 ← Confusing with even numbers",
            solution_steps_ar='["Numbers greater than 6: 7 and 8 = 2 cards","Total = 8","Probability = 2  /  8 = 1/4"]',
    tags="probability", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q27 — new — mode (bimodal concept)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.3,
            text_ar="What is the mode of the numbers:\n3, 5, 3, 7, 5, 9?",
            option_a="3 only", option_b="5 only", option_c="3 and 5 together", option_d="9",
            correct_option="c",
            explanation_ar="Frequencies: 3->2, 5->2, 7->1, 9->1\nBoth 3 and 5 appear twice\nMode = 3 and 5 (bimodal)\n\nWhy other options are wrong:\n  • 3 only ← Choosing first value only\n  • 5 only ← Choosing second value only\n  • 9 ← Choosing largest value",
            solution_steps_ar='["Calculate frequencies: 3->2, 5->2, 7->1, 9->1","Highest frequency = 2 (shared by 3 and 5)","Mode = 3 and 5 together (bimodal)"]',
    tags="mode", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q28 — new — mean (equal values)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.3,
            text_ar="5 students each scored 80 points.\nWhat is the arithmetic mean?",
            option_a="75", option_b="80", option_c="85", option_d="100",
            correct_option="b",
            explanation_ar="If all values are equal, mean = that value\nSum = 80  x  5 = 400\nMean = 400  /  5 = 80\n\nWhy other options are wrong:\n  • 75 ← Incorrect calculation\n  • 85 ← Division error\n  • 100 ← Confusing with another value",
            solution_steps_ar='["All values = 80","Mean = 80 (same value when all are equal)"]',
    tags="mean", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ══════════════════════════════════════════════════════════════
        # Difficulty 0.4 — (22 questions)
        # ══════════════════════════════════════════════════════════════

        # Q29 — existing — bag probability
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.4,
            text_ar="In a bag:\n• 3 red balls\n• 5 blue balls\n• 2 green balls\nWhat is the probability of drawing a blue ball?",
            option_a="1/2", option_b="3/10", option_c="⅕", option_d="2/5",
            correct_option="a",
            explanation_ar="Formula:\n  Probability = Favorable outcomes  /  Total outcomes\n\nSolution:\n  Total = 3 + 5 + 2 = 10\n  P(blue) = 5  /  10 = 1/2\n\nWhy other options are wrong:\n  • 3/10 ← Incorrect calculation\n  • ⅕ ← Wrong count of blue balls\n  • 2/5 ← Confusing with another fraction",
            solution_steps_ar='["Total = 3 + 5 + 2 = 10 balls","Blue balls = 5","Probability = 5  /  10 = 1/2"]',
    tags="probability", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q30 — existing — temperature mode
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.4,
            text_ar="Temperatures (in Celsius) over a week:\n35, 37, 36, 39, 35, 38, 35\nWhat is the mode?",
            option_a="35", option_b="36", option_c="37", option_d="39",
            correct_option="a",
            explanation_ar="Mode = Most frequent value\n\nFrequencies:\n  35 ← 3 times ✓\n  36 ← 1 time\n  37 ← 1 time\n  38 ← 1 time\n  39 ← 1 time\n\nTherefore: Mode = 35\n\nWhy other options are wrong:\n  • 36 ← Choosing middle value\n  • 37 ← Confusing mode with median\n  • 39 ← Choosing maximum value",
            solution_steps_ar='["Calculate frequency of each value","35 appears 3 times (most)","Therefore: Mode = 35"]',
    tags="mode", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q31 — new — median (even count)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.4,
            text_ar="Find the median of the numbers:\n14, 7, 11, 3, 9, 5",
            option_a="7", option_b="8", option_c="9", option_d="10",
            correct_option="b",
            explanation_ar="Sorted: 3, 5, 7, 9, 11, 14\nNumber of values = 6 (even)\nMedian = (7 + 9)  /  2 = 8\n\nWhy other options are wrong:\n  • 7 ← Not using average of two middle values\n  • 9 ← Taking wrong position\n  • 10 ← Confusing with another calculation",
            solution_steps_ar='["Sorted: 3, 5, 7, 9, 11, 14","Number of values = 6 (even)","Median = (7 + 9)  /  2 = 8"]',
    tags="median", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q32 — new — probability (OR, mutually exclusive)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.4,
            text_ar="When rolling a die, what is the probability of getting 1 or 6?",
            option_a="1/6", option_b="1/3", option_c="1/2", option_d="2/3",
            correct_option="b",
            explanation_ar="Events are mutually exclusive (cannot both occur)\nP(1 or 6) = P(1) + P(6) = 1/6 + 1/6 = ^2⁄₆ = 1/3\n\nWhy other options are wrong:\n  • 1/6 ← Only one outcome\n  • 1/2 ← Confusing with even/odd probability\n  • 2/3 ← Incorrect addition",
            solution_steps_ar='["Events are mutually exclusive","P(1) = 1/6, P(6) = 1/6","P(1 or 6) = 1/6 + 1/6 = 1/3"]',
    tags="probability", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q33 — new — counting principle (clothes)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.4,
            text_ar="Ahmed has 4 shirts, 3 pants, and 2 shoes.\nHow many different outfits can he make?",
            option_a="9", option_b="12", option_c="24", option_d="36",
            correct_option="c",
            explanation_ar="Multiplication principle:\nNumber of outfits = 4  x  3  x  2 = 24\n\nWhy other options are wrong:\n  • 9 ← Adding instead of multiplying\n  • 12 ← Missing one category\n  • 36 ← Incorrect calculation",
            solution_steps_ar='["Multiplication principle: 4  x  3  x  2","= 24 different outfits"]',
    tags="counting", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q34 — new — mean from frequency table
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.4,
            text_ar="In a survey, ages of 5 people were:\n20, 25, 30, 35, 40\nWhat is the arithmetic mean of their ages?",
            option_a="25", option_b="30", option_c="35", option_d="32",
            correct_option="b",
            explanation_ar="Sum = 20 + 25 + 30 + 35 + 40 = 150\nNumber of values = 5\nMean = 150  /  5 = 30\n\nWhy other options are wrong:\n  • 25 ← Incorrect calculation\n  • 35 ← Forgetting one value\n  • 32 ← Confusing with median",
            solution_steps_ar='["Sum = 20 + 25 + 30 + 35 + 40 = 150","Number of values = 5","Mean = 150  /  5 = 30"]',
    tags="mean,data-interpretation", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q35 — new — probability (at least one)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.4,
            text_ar="When rolling a die, what is the probability of getting a number less than 5?",
            option_a="1/2", option_b="2/3", option_c="5/6", option_d="1/3",
            correct_option="b",
            explanation_ar="Numbers less than 5: {1, 2, 3, 4} = 4 numbers\nTotal = 6\nProbability = ^4⁄₆ = 2/3\n\nWhy other options are wrong:\n  • 1/2 ← Incorrect count\n  • 5/6 ← Confusing with complement\n  • 1/3 ← Wrong range",
            solution_steps_ar='["Numbers less than 5: 1, 2, 3, 4 = 4 numbers","Total = 6","Probability = 4  /  6 = 2/3"]',
    tags="probability", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q36 — new — median with repeated values
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.4,
            text_ar="Find the median of the data:\n3, 5, 5, 7, 8, 8, 9",
            option_a="5", option_b="6", option_c="7", option_d="8",
            correct_option="c",
            explanation_ar="Data sorted: 3, 5, 5, 7, 8, 8, 9\nNumber of values = 7 (odd)\nMedian = 4th value = 7\n\nWhy other options are wrong:\n  • 5 ← Not finding correct position\n  • 6 ← Incorrect calculation\n  • 8 ← Confusing with mode",
            solution_steps_ar='["Data sorted: 3, 5, 5, 7, 8, 8, 9","Number of values = 7 (odd)","Median = 4th value = 7"]',
    tags="median", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q37 — new — probability (two events independent)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.4,
            text_ar="When tossing a coin twice, what is the probability of getting heads both times?",
            option_a="1/4", option_b="1/2", option_c="1/3", option_d="1/8",
            correct_option="a",
            explanation_ar="Events are independent\nP(heads) = 1/2\nP(heads and heads) = 1/2  x  1/2 = 1/4\n\nWhy other options are wrong:\n  • 1/2 ← Only one toss\n  • 1/3 ← Incorrect calculation\n  • 1/8 ← Confusing with three tosses",
            solution_steps_ar='["P(heads on first toss) = 1/2","P(heads on second toss) = 1/2","P(heads on both) = 1/2  x  1/2 = 1/4"]',
    tags="probability", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q38 — new — range with decimals
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.4,
            text_ar="Temperatures of 5 cities:\n20.5, 18.3, 25.7, 19.1, 22.4\nWhat is the range?",
            option_a="5.2", option_b="6.3", option_c="7.4", option_d="8.5",
            correct_option="c",
            explanation_ar="Maximum = 25.7\nMinimum = 18.3\nRange = 25.7 − 18.3 = 7.4\n\nWhy other options are wrong:\n  • 5.2 ← Incorrect subtraction\n  • 6.3 ← Confusing with IQR\n  • 8.5 ← Wrong values",
            solution_steps_ar='["Maximum = 25.7","Minimum = 18.3","Range = 25.7 − 18.3 = 7.4"]',
    tags="range", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q39 — new — combinations (simple)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.4,
            text_ar="How many ways can 3 books be chosen from 6 books?",
            option_a="15", option_b="20", option_c="30", option_d="120",
            correct_option="b",
            explanation_ar="Combinations: C(6,3) = 6!  /  (3!  x  3!)\n= 720  /  (6  x  6) = 720  /  36 = 20\n\nWhy other options are wrong:\n  • 15 ← Incorrect calculation\n  • 30 ← Using wrong formula\n  • 120 ← Using permutations",
            solution_steps_ar='["C(6,3) = 6!  /  (3!  x  3!)","= 720  /  36","= 20 ways"]',
    tags="combination", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q40 — new — frequency table mean
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.4,
            text_ar="Frequency table:\nValue:   2  4  6\nFrequency: 3  4  3\nWhat is the arithmetic mean?",
            option_a="3.6", option_b="4", option_c="4.4", option_d="5",
            correct_option="b",
            explanation_ar="Sum = (2 x 3) + (4 x 4) + (6 x 3) = 6 + 16 + 18 = 40\nNumber of values = 3 + 4 + 3 = 10\nMean = 40  /  10 = 4\n\nWhy other options are wrong:\n  • 3.6 ← Incorrect calculation\n  • 4.4 ← Wrong sum\n  • 5 ← Confusing with another value",
            solution_steps_ar='["Sum = 2 x 3 + 4 x 4 + 6 x 3 = 6 + 16 + 18 = 40","Number of values = 3 + 4 + 3 = 10","Mean = 40  /  10 = 4"]',
    tags="mean,data-interpretation", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q41 — new — probability (not blue)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.4,
            text_ar="In a bag of 15 balls: 5 red, 4 blue, and 6 green.\nWhat is the probability of drawing a ball that is NOT blue?",
            option_a="4/15", option_b="7/15", option_c="⅗", option_d="11/15",
            correct_option="d",
            explanation_ar="Number of non-blue balls = 5 + 6 = 11\nTotal = 15\nProbability = 11/15\n\nWhy other options are wrong:\n  • 4/15 ← This is P(blue)\n  • 7/15 ← Incorrect count\n  • ⅗ ← Confusing with another fraction",
            solution_steps_ar='["Non-blue balls = 5 + 6 = 11","Total = 15","Probability = 11  /  15 = 11/15"]',
    tags="probability", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q42 — new — mean effect of adding a value
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.4,
            text_ar="The mean of 4 numbers = 10.\nIf the number 20 is added to the set, what is the new mean?",
            option_a="10", option_b="12", option_c="14", option_d="15",
            correct_option="b",
            explanation_ar="Old sum = 10  x  4 = 40\nNew sum = 40 + 20 = 60\nNew count = 5\nNew mean = 60  /  5 = 12\n\nWhy other options are wrong:\n  • 10 ← Not updating the count\n  • 14 ← Calculation error\n  • 15 ← Incorrect formula",
            solution_steps_ar='["Old sum = 10  x  4 = 40","New sum = 40 + 20 = 60","New mean = 60  /  5 = 12"]',
    tags="mean", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q43 — new — permutations (simple)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.4,
            text_ar="Does arranging 3 people (Ahmed, Sara, Khalid) differ from (Sara, Ahmed, Khalid)? How many different arrangements exist?",
            option_a="3", option_b="6", option_c="9", option_d="12",
            correct_option="b",
            explanation_ar="Permutations of 3 items = 3!\n= 3  x  2  x  1 = 6\n\nWhy other options are wrong:\n  • 3 ← Using combinations\n  • 9 ← Incorrect calculation\n  • 12 ← Wrong formula",
            solution_steps_ar='["Number of ways = 3!","= 3  x  2  x  1","= 6 ways"]',
    tags="permutation", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q44 — new — data interpretation (table)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.4,
            text_ar="In a class of 20 students:\n• 8 got Excellent\n• 7 got Very Good\n• 5 got Good\nWhat percentage got Excellent?",
            option_a="35%", option_b="40%", option_c="45%", option_d="50%",
            correct_option="b",
            explanation_ar="Number of Excellent = 8\nTotal = 20\nPercentage = (8  /  20)  x  100 = 40%\n\nWhy other options are wrong:\n  • 35% ← Incorrect reading\n  • 45% ← Calculation error\n  • 50% ← Confusing with half",
            solution_steps_ar='["Excellent = 8 students","Total = 20","Percentage = (8  /  20)  x  100 = 40%"]',
    tags="data-interpretation", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q45 — new — probability (card)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.4,
            text_ar="From cards numbered 1 to 10, what is the probability of drawing a card with an odd number?",
            option_a="2/5", option_b="1/2", option_c="⅗", option_d="⅘",
            correct_option="b",
            explanation_ar="Odd numbers: 1, 3, 5, 7, 9 = 5 cards\nTotal = 10\nProbability = 5  /  10 = 1/2\n\nWhy other options are wrong:\n  • 2/5 ← Incorrect count\n  • ⅗ ← Wrong calculation\n  • ⅘ ← Confusing with even numbers",
            solution_steps_ar='["Odd numbers from 1 to 10: {1, 3, 5, 7, 9} = 5","Total = 10","Probability = 5  /  10 = 1/2"]',
    tags="probability", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q46 — new — mean with negatives
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.4,
            text_ar="What is the arithmetic mean of the numbers:\n−2, 0, 4, 6, 2?",
            option_a="1", option_b="2", option_c="3", option_d="4",
            correct_option="b",
            explanation_ar="Sum = −2 + 0 + 4 + 6 + 2 = 10\nNumber of values = 5\nMean = 10  /  5 = 2\n\nWhy other options are wrong:\n  • 1 ← Incorrect calculation\n  • 3 ← Forgetting a value\n  • 4 ← Confusing with maximum",
            solution_steps_ar='["Sum = −2 + 0 + 4 + 6 + 2 = 10","Number of values = 5","Mean = 10  /  5 = 2"]',
    tags="mean", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q47 — new — counting (digits)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.4,
            text_ar="How many two-digit numbers can be formed from digits {1, 2, 3} with repetition allowed?",
            option_a="6", option_b="9", option_c="12", option_d="15",
            correct_option="b",
            explanation_ar="Tens digit: 3 choices\nOnes digit: 3 choices (with repetition)\nTotal = 3  x  3 = 9\n\nWhy other options are wrong:\n  • 6 ← Adding instead of multiplying\n  • 12 ← Confusing without repetition\n  • 15 ← Incorrect calculation",
            solution_steps_ar='["Tens digit: 3 choices","Ones digit: 3 choices (repetition allowed)","Total = 3  x  3 = 9 numbers"]',
    tags="counting", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q48 — new — median (8 values)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.4,
            text_ar="Find the median of the data:\n2, 4, 6, 8, 10, 12, 14, 16",
            option_a="8", option_b="9", option_c="10", option_d="11",
            correct_option="b",
            explanation_ar="Number of values = 8 (even)\n4th value = 8, 5th value = 10\nMedian = (8 + 10)  /  2 = 9\n\nWhy other options are wrong:\n  • 8 ← Only 4th value\n  • 10 ← Only 5th value\n  • 11 ← Incorrect calculation",
            solution_steps_ar='["Data sorted: 2, 4, 6, 8, 10, 12, 14, 16","Number of values = 8 (even)","Median = (8 + 10)  /  2 = 9"]',
    tags="median", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q49 — new — probability (two coins)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.4,
            text_ar="When tossing two coins, what is the probability of getting at least one tail?",
            option_a="1/4", option_b="1/2", option_c="3/4", option_d="1",
            correct_option="c",
            explanation_ar="P(at least one tail) = 1 − P(no tails)\nP(two heads) = 1/2  x  1/2 = 1/4\nAnswer = 1 − 1/4 = 3/4\n\nWhy other options are wrong:\n  • 1/4 ← P(two heads)\n  • 1/2 ← Only one coin\n  • 1 ← Impossible certainty",
            solution_steps_ar='["Using complement: P(at least one tail) = 1 − P(two heads)","P(two heads) = 1/2  x  1/2 = 1/4","Answer = 1 − 1/4 = 3/4"]',
    tags="probability", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q50 — new — weighted average (grades)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.4,
            text_ar="A student got:\n• 90 on exam (weight 60%)\n• 80 on homework (weight 40%)\nWhat is the final grade?",
            option_a="84", option_b="85", option_c="86", option_d="88",
            correct_option="c",
            explanation_ar="Grade = 90  x  0.6 + 80  x  0.4\n= 54 + 32 = 86\n\nWhy other options are wrong:\n  • 84 ← Incorrect calculation\n  • 85 ← Wrong weights\n  • 88 ← Confusing with simple mean",
            solution_steps_ar='["Exam = 90  x  0.6 = 54","Homework = 80  x  0.4 = 32","Final grade = 54 + 32 = 86"]',
    tags="mean", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ══════════════════════════════════════════════════════════════
        # Difficulty 0.5 — (22 questions)
        # ══════════════════════════════════════════════════════════════

        # Q51 — existing — race median
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.5,
            text_ar="In a race, times of 6 runners (in seconds):\n12.3, 11.8, 12.5, 11.5, 12.1, 11.8\nWhat is the median?",
            option_a="11.8", option_b="12.0", option_c="11.95", option_d="12.1",
            correct_option="c",
            explanation_ar="Step 1: Sort ascending\n  11.5, 11.8, 11.8, 12.1, 12.3, 12.5\n\nStep 2: Number of values = 6 (even)\n  Median = (value 3 + value 4)  /  2\n  = (11.8 + 12.1)  /  2\n  = 23.9  /  2 = 11.95\n\nWhy other options are wrong:\n  • 11.8 ← Not using average\n  • 12.0 ← Incorrect calculation\n  • 12.1 ← Wrong position",
            solution_steps_ar='["Sorted: 11.5, 11.8, 11.8, 12.1, 12.3, 12.5","Number of values = 6 (even) -> Median = average of two middle values","Median = (11.8 + 12.1)  /  2 = 11.95"]',
    tags="median", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q52 — existing — with replacement
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.5,
            text_ar="A bag contains 4 red balls and 6 white balls.\nA ball is drawn and replaced, then another ball is drawn.\nWhat is the probability that both balls are red?",
            option_a="^2⁄₂₅", option_b="4/25", option_c="2/5", option_d="^8⁄₂₅",
            correct_option="b",
            explanation_ar="Given:\n  Red = 4, White = 6, Total = 10\n  Drawing with replacement\n\nSolution:\n  P(red on first) = ^4⁄₁₀ = 2/5\n  P(red on second) = ^4⁄₁₀ = 2/5 (with replacement)\n  P(both) = 2/5  x  2/5 = 4/25\n\nWhy other options are wrong:\n  • ^2⁄₂₅ ← Incorrect calculation\n  • 2/5 ← Only one draw\n  • ^8⁄₂₅ ← Adding instead of multiplying",
            solution_steps_ar='["P(red) = 4  /  10 = 2/5","With replacement -> probabilities dont change","P(red then red) = 2/5  x  2/5 = 4/25"]',
    tags="probability", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q53 — existing — variance
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.5,
            text_ar="Data set: 2, 4, 4, 6, 4\nWhat is the variance?",
            option_a="1.2", option_b="1.6", option_c="2.0", option_d="2.4",
            correct_option="b",
            explanation_ar="Given:\n  Data: 2, 4, 4, 6, 4\n\nSolution:\n  Mean = (2+4+4+6+4)  /  5 = 20  /  5 = 4\n  Squared deviations: (2−4)^2=4, (4−4)^2=0, (4−4)^2=0, (6−4)^2=4, (4−4)^2=0\n  Sum of squared deviations = 4+0+0+4+0 = 8\n  Variance = 8  /  5 = 1.6\n\nWhy other options are wrong:\n  • 1.2 ← Not squaring deviations\n  • 2.0 ← Confusing with standard deviation\n  • 2.4 ← Incorrect calculation",
            solution_steps_ar='["Mean = 20  /  5 = 4","Squared deviations: 4, 0, 0, 4, 0","Sum of squared deviations = 8","Variance = 8  /  5 = 1.6"]',
    tags="variance", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q54 — existing — dice sum=7
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.5,
            text_ar="When rolling two dice, what is the probability that the sum equals 7?",
            option_a="1/12", option_b="1/6", option_c="1/9", option_d="⅕",
            correct_option="b",
            explanation_ar="Given:\n  Two dice: Total outcomes = 6  x  6 = 36\n\nSolution:\n  Cases where sum = 7:\n  (1,6) (2,5) (3,4) (4,3) (5,2) (6,1) = 6 cases\n  Probability = 6  /  36 = 1/6\n\nWhy other options are wrong:\n  • 1/12 ← Incorrect count\n  • 1/9 ← Wrong calculation\n  • ⅕ ← Confusing with another probability",
            solution_steps_ar='["Total outcomes = 6  x  6 = 36","Cases with sum 7: (1,6)(2,5)(3,4)(4,3)(5,2)(6,1) = 6","Probability = 6  /  36 = 1/6"]',
    tags="probability", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q55 — existing — conditional probability (without replacement)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.5,
            text_ar="A box has 4 red balls and 6 blue balls.\nA ball is drawn without replacement, then another ball is drawn.\nIf the first was red, what is the probability the second is also red?",
            option_a="^2⁄₅", option_b="3/10", option_c="1/3", option_d="^4⁄₉",
            correct_option="c",
            explanation_ar="Given:\n  Red = 4, Blue = 6, Total = 10\n  First was red (without replacement)\n\nSolution:\n  After drawing one red: Remaining = 3 red + 6 blue = 9\n  P(second red) = 3  /  9 = 1/3\n\nWhy other options are wrong:\n  • ^2⁄₅ ← Original probability\n  • 3/10 ← Wrong calculation\n  • ^4⁄₉ ← Not updating after first draw",
            solution_steps_ar='["After drawing red: 3 red + 6 blue = 9 balls","Conditional probability = 3  /  9 = 1/3"]',
    tags="probability,conditional-probability", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q56 — existing — weighted average
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.5,
            text_ar="Class A (30 students) has mean = 70, Class B (20 students) has mean = 80.\nWhat is the overall mean of both classes combined?",
            option_a="74", option_b="75", option_c="76", option_d="78",
            correct_option="a",
            explanation_ar="Given:\n  Class A: 30 students, mean = 70\n  Class B: 20 students, mean = 80\n\nSolution:\n  Sum A = 30  x  70 = 2100\n  Sum B = 20  x  80 = 1600\n  Overall mean = (2100 + 1600)  /  (30 + 20)\n  = 3700  /  50 = 74\n\nWhy other options are wrong:\n  • 75 ← Simple average of means\n  • 76 ← Incorrect calculation\n  • 78 ← Confusing with another value",
            solution_steps_ar='["Sum A = 30  x  70 = 2100","Sum B = 20  x  80 = 1600","Mean = (2100 + 1600)  /  50 = 3700  /  50 = 74"]',
    tags="mean", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q57 — new — dice sum probability
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.5,
            text_ar="When rolling two dice, what is the probability that their sum is greater than 10?",
            option_a="1/18", option_b="1/12", option_c="1/6", option_d="1/4",
            correct_option="b",
            explanation_ar="Sum > 10 means: 11 or 12\nSum = 11: (5,6)(6,5) = 2\nSum = 12: (6,6) = 1\nTotal = 3 cases\nProbability = ^3⁄₃₆ = 1/12\n\nWhy other options are wrong:\n  • 1/18 ← Incorrect count\n  • 1/6 ← Confusing with sum >= 10\n  • 1/4 ← Wrong calculation",
            solution_steps_ar='["Cases: Sum 11 = (5,6)(6,5) = 2 cases","Sum 12 = (6,6) = 1 case","Probability = 3  /  36 = 1/12"]',
    tags="probability", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q58 — new — permutations (letters)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.5,
            text_ar="How many different words (meaningful or not) can be formed from the letters of \"pen\" using all letters?",
            option_a="3", option_b="6", option_c="9", option_d="12",
            correct_option="b",
            explanation_ar="Number of letters = 3 (p, e, n) all different\nNumber of arrangements = 3! = 3  x  2  x  1 = 6\n\nWhy other options are wrong:\n  • 3 ← Adding instead of multiplying\n  • 9 ← Incorrect calculation\n  • 12 ← Wrong formula",
            solution_steps_ar='["Number of letters = 3 (all different)","Number of arrangements = 3!","= 3  x  2  x  1 = 6"]',
    tags="counting", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q59 — new — quartiles (Q1)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.5,
            text_ar="Data sorted: 2, 4, 6, 8, 10, 12, 14, 16\nWhat is Q1 (first quartile)?",
            option_a="4", option_b="5", option_c="6", option_d="7",
            correct_option="b",
            explanation_ar="Number of values = 8\nLower half: 2, 4, 6, 8\nQ1 = median of lower half = (4 + 6)  /  2 = 5\n\nWhy other options are wrong:\n  • 4 ← Just the second value\n  • 6 ← Confusing with Q2\n  • 7 ← Incorrect calculation",
            solution_steps_ar='["Lower half: 2, 4, 6, 8","Q1 = median of lower half","= (4 + 6)  /  2 = 5"]',
    tags="range", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q60 — new — probability (without replacement, two draws)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.5,
            text_ar="In a bag of 5 balls: 3 red and 2 blue.\nTwo balls are drawn without replacement.\nWhat is the probability that first is red and second is blue?",
            option_a="3/20", option_b="6/20", option_c="3/10", option_d="6/25",
            correct_option="c",
            explanation_ar="P(first red) = ^3⁄₅\nP(second blue | first red) = ^2⁄₄ = 1/2\nP(both) = ^3⁄₅  x  1/2 = 3/10\n\nWhy other options are wrong:\n  • 3/20 ← Incorrect calculation\n  • 6/20 ← Not simplifying\n  • 6/25 ← With replacement error",
            solution_steps_ar='["P(first red) = 3  /  5","After drawing red: 2 red + 2 blue = 4","P(second blue) = 2  /  4 = 1/2","P = ^3⁄₅  x  1/2 = 3/10"]',
    tags="probability,conditional-probability", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q61 — new — variance concept
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.5,
            text_ar="Data set: 3, 5, 7, 9, 11\nWhat is the variance?",
            option_a="4", option_b="6", option_c="8", option_d="10",
            correct_option="c",
            explanation_ar="Mean = (3+5+7+9+11)  /  5 = 35  /  5 = 7\nSquared deviations: (3−7)^2=16, (5−7)^2=4, (7−7)^2=0, (9−7)^2=4, (11−7)^2=16\nSum = 16+4+0+4+16 = 40\nVariance = 40  /  5 = 8\n\nWhy other options are wrong:\n  • 4 ← Not squaring deviations\n  • 6 ← Confusing with standard deviation\n  • 10 ← Incorrect calculation",
            solution_steps_ar='["Mean = 35  /  5 = 7","Squared deviations: 16, 4, 0, 4, 16","Sum of squared deviations = 40","Variance = 40  /  5 = 8"]',
    tags="variance", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q62 — new — combinations application
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.5,
            text_ar="How many ways to choose 2 from 4 colors to paint a room?",
            option_a="4", option_b="6", option_c="8", option_d="12",
            correct_option="b",
            explanation_ar="C(4,2) = 4!  /  (2!  x  2!)\n= 24  /  (2  x  2) = 24  /  4 = 6\n\nWhy other options are wrong:\n  • 4 ← Using permutations\n  • 8 ← Incorrect calculation\n  • 12 ← Wrong formula",
            solution_steps_ar='["C(4,2) = 4!  /  (2!  x  2!)","= 24  /  4","= 6 ways"]',
    tags="combination", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q63 — new — probability (union, not mutually exclusive)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.5,
            text_ar="In a class of 30 students: 15 like Math, 12 like Science, 5 like both.\nWhat is the probability of selecting a student who likes Math or Science?",
            option_a="⅗", option_b="2/3", option_c="11/15", option_d="^9⁄₁₀",
            correct_option="c",
            explanation_ar="P(Math or Science) = P(M) + P(S) − P(MintersectionS)\n= ^1^5⁄₃₀ + ^1^2⁄₃₀ − ^5⁄₃₀\n= 22/30 = 11/15\n\nWhy other options are wrong:\n  • ⅗ ← Only Math\n  • 2/3 ← Not subtracting intersection\n  • ^9⁄₁₀ ← Incorrect calculation",
            solution_steps_ar='["P(M or S) = P(M) + P(S) − P(MintersectionS)","= 15 + 12 − 5 = 22 out of 30","= 22/30 = 11/15"]',
    tags="probability", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q64 — new — counting with restriction
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.5,
            text_ar="How many even 3-digit numbers can be formed from {1, 2, 3, 4} without repetition?",
            option_a="8", option_b="12", option_c="16", option_d="24",
            correct_option="b",
            explanation_ar="Number is even -> units digit: 2 or 4 (2 choices)\nAfter choosing units: hundreds digit 3 choices, tens digit 2 choices\nTotal = 2  x  3  x  2 = 12\n\nWhy other options are wrong:\n  • 8 ← Missing some cases\n  • 16 ← With repetition error\n  • 24 ← No restriction applied",
            solution_steps_ar='["Units digit (even): 2 or 4 = 2 choices","Hundreds digit: 3 choices (from remaining)","Tens digit: 2 choices","Total = 2  x  3  x  2 = 12"]',
    tags="counting", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q65 — new — mean from frequency
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.5,
            text_ar="Frequency table for test scores:\nScore:  60  70  80  90\nFreq:    2   5   7   6\nWhat is the arithmetic mean?",
            option_a="76", option_b="78.5", option_c="79", option_d="80",
            correct_option="b",
            explanation_ar="Sum = 60 x 2 + 70 x 5 + 80 x 7 + 90 x 6\n= 120 + 350 + 560 + 540 = 1570\nCount = 2 + 5 + 7 + 6 = 20\nMean = 1570  /  20 = 78.5\n\nWhy other options are wrong:\n  • 76 ← Incorrect calculation\n  • 79 ← Wrong sum\n  • 80 ← Confusing with another value",
            solution_steps_ar='["Sum = 60 x 2 + 70 x 5 + 80 x 7 + 90 x 6 = 1570","Count = 2 + 5 + 7 + 6 = 20","Mean = 1570  /  20 = 78.5"]',
    tags="mean,data-interpretation", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q66 — new — box plot (IQR)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.5,
            text_ar="Data sorted: 1, 3, 5, 7, 9, 11, 13, 15\nWhat is the IQR (Interquartile Range)?",
            option_a="6", option_b="8", option_c="10", option_d="14",
            correct_option="b",
            explanation_ar="Lower half: 1, 3, 5, 7 -> Q1 = (3+5) / 2 = 4\nUpper half: 9, 11, 13, 15 -> Q3 = (11+13) / 2 = 12\nIQR = Q3 − Q1 = 12 − 4 = 8\n\nWhy other options are wrong:\n  • 6 ← Incorrect Q1 or Q3\n  • 10 ← Confusing with range\n  • 14 ← Maximum − minimum",
            solution_steps_ar='["Q1 = (3+5)  /  2 = 4","Q3 = (11+13)  /  2 = 12","IQR = 12 − 4 = 8"]',
    tags="range", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q67 — new — probability (cards numbers)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.5,
            text_ar="Cards numbered 1 to 20.\nWhat is the probability of drawing a prime number?",
            option_a="⅕", option_b="2/5", option_c="3/10", option_d="^7⁄₂₀",
            correct_option="b",
            explanation_ar="Prime numbers from 1 to 20:\n{2, 3, 5, 7, 11, 13, 17, 19} = 8 numbers\nProbability = 8/20 = 2/5\n\nWhy other options are wrong:\n  • ⅕ ← Incorrect count\n  • 3/10 ← Missing some primes\n  • ^7⁄₂₀ ← Wrong count",
            solution_steps_ar='["Prime numbers: 2, 3, 5, 7, 11, 13, 17, 19 = 8 numbers","Total = 20","Probability = 8  /  20 = 2/5"]',
    tags="probability", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q68 — new — mean after removing a value
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.5,
            text_ar="Mean of 6 numbers = 15.\nIf the number 9 is removed from the set, what is the new mean?",
            option_a="15.4", option_b="15.8", option_c="16.2", option_d="16.8",
            correct_option="c",
            explanation_ar="Old sum = 15  x  6 = 90\nNew sum = 90 − 9 = 81\nNew count = 5\nNew mean = 81  /  5 = 16.2\n\nWhy other options are wrong:\n  • 15.4 ← Incorrect calculation\n  • 15.8 ← Wrong subtraction\n  • 16.8 ← Wrong count",
            solution_steps_ar='["Sum = 15  x  6 = 90","New sum after removing 9 = 90 − 9 = 81","New mean = 81  /  5 = 16.2"]',
    tags="mean", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q69 — new — probability (at least one head in 3 tosses)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.5,
            text_ar="When tossing a coin 3 times, what is the probability of getting at least one head?",
            option_a="5/8", option_b="3/4", option_c="7/8", option_d="1/2",
            correct_option="c",
            explanation_ar="P(at least 1 head) = 1 − P(no heads)\nP(3 tails) = (1/2)^3 = 1/8\nP(at least 1 head) = 1 − 1/8 = 7/8\n\nWhy other options are wrong:\n  • 5/8 ← Incorrect calculation\n  • 3/4 ← Confusing with 2 tosses\n  • 1/2 ← Wrong approach",
            solution_steps_ar='["P(no heads at all) = (1/2)^3 = 1/8","P(at least 1 head) = 1 − 1/8","= 7/8"]',
    tags="probability", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q70 — new — median effect of adding value
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.5,
            text_ar="Data: 3, 5, 7, 9\nIf the number 11 is added, what is the new median?",
            option_a="5", option_b="6", option_c="7", option_d="9",
            correct_option="c",
            explanation_ar="Data after adding: 3, 5, 7, 9, 11\nNumber of values = 5 (odd)\nMedian = 3rd value = 7\n\nWhy other options are wrong:\n  • 5 ← Not finding correct position\n  • 6 ← Incorrect calculation\n  • 9 ← Confusing with another value",
            solution_steps_ar='["Data sorted: 3, 5, 7, 9, 11","Number of values = 5 (odd)","Median = middle value = 7"]',
    tags="median", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q71 — new — data interpretation (pie chart concept)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.5,
            text_ar="In a school of 200 students:\n• 25% prefer Math\n• 30% prefer Science\n• 45% prefer Arabic\nHow many students prefer Science?",
            option_a="50", option_b="60", option_c="70", option_d="90",
            correct_option="b",
            explanation_ar="Number preferring Science = 30%  x  200\n= 0.3  x  200 = 60 students\n\nWhy other options are wrong:\n  • 50 ← Confusing with Math\n  • 70 ← Incorrect percentage\n  • 90 ← Confusing with Arabic",
            solution_steps_ar='["Science percentage = 30%","Number = 30%  x  200","= 0.3  x  200 = 60 students"]',
    tags="probability", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q72 — new — standard deviation (simple)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.5,
            text_ar="Data set: 4, 4, 4, 4\nWhat is the standard deviation?",
            option_a="0", option_b="1", option_c="2", option_d="4",
            correct_option="a",
            explanation_ar="All values are equal (= 4)\nMean = 4\nAll deviations = 0\nStandard deviation = 0\n\nWhy other options are wrong:\n  • 1 ← Incorrect calculation\n  • 2 ← Confusing with another value\n  • 4 ← Confusing with the value itself",
            solution_steps_ar='["All values = 4 -> Mean = 4","Every deviation from mean = 0","Standard deviation = 0"]',
    tags="standard-deviation", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ══════════════════════════════════════════════════════════════
        # Difficulty 0.6 — (22 questions)
        # ══════════════════════════════════════════════════════════════

        # Q73 — existing — mode
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.6,
            text_ar="Find the mode of the numbers:\n4, 7, 2, 7, 3, 7, 5",
            option_a="2", option_b="4", option_c="5", option_d="7",
            correct_option="d",
            explanation_ar="Mode = Most frequent value\n\nFrequencies:\n  2 ← 1 time\n  3 ← 1 time\n  4 ← 1 time\n  5 ← 1 time\n  7 ← 3 times ✓\n\nTherefore: Mode = 7\n\nWhy other options are wrong:\n  • 2 ← Choosing smallest value\n  • 4 ← Confusing with position\n  • 5 ← Choosing middle value",
            solution_steps_ar='["Calculate frequency of each value","7 appears 3 times (most)","Mode = 7"]',
    tags="mode", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # Q74 — new — probability (compound event)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.6,
            text_ar="A bag has 5 red balls and 3 blue balls.\nTwo balls are drawn without replacement.\nWhat is the probability that both are blue?",
            option_a="3/28", option_b="9/64", option_c="6/64", option_d="6/56",
            correct_option="a",
            explanation_ar="P(first blue) = ^3⁄₈\nP(second blue | first blue) = ^2⁄₇\nP(both) = ^3⁄₈  x  ^2⁄₇ = 6/56 = 3/28\n\nWhy other options are wrong:\n  • 9/64 ← With replacement error\n  • 6/64 ← Incorrect calculation\n  • 6/56 ← Not simplified",
            solution_steps_ar='["P(first blue) = 3  /  8","P(second blue) = 2  /  7 (without replacement)","P(both) = ^3⁄₈  x  ^2⁄₇ = 6/56 = 3/28"]',
    tags="probability,conditional-probability", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q75 — new — permutations with restriction
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.6,
            text_ar="How many 3-digit numbers using different digits from {0, 1, 2, 3, 4}?\n(Zero cannot be in hundreds place)",
            option_a="36", option_b="48", option_c="60", option_d="24",
            correct_option="b",
            explanation_ar="Hundreds digit: 4 choices (1, 2, 3, 4) — cannot be 0\nTens digit: 4 choices (from remaining 5 digits)\nUnits digit: 3 choices\nTotal = 4  x  4  x  3 = 48\n\nWhy other options are wrong:\n  • 36 ← Missing some cases\n  • 60 ← With repetition error\n  • 24 ← Not applying restriction",
            solution_steps_ar='["Hundreds digit != 0 -> 4 choices","Tens digit: 4 choices (from remaining)","Units digit: 3 choices","Total = 4  x  4  x  3 = 48"]',
    tags="counting", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q76 — new — weighted mean (three subjects)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.6,
            text_ar="A student scored:\n• Math: 85 (weight 4)\n• Science: 90 (weight 3)\n• Arabic: 75 (weight 3)\nWhat is the weighted average?",
            option_a="83.5", option_b="83", option_c="84", option_d="84.5",
            correct_option="a",
            explanation_ar="Sum = 85 x 4 + 90 x 3 + 75 x 3\n= 340 + 270 + 225 = 835\nSum of weights = 4 + 3 + 3 = 10\nAverage = 835  /  10 = 83.5\n\nWhy other options are wrong:\n  • 83 ← Incorrect calculation\n  • 84 ← Wrong weights\n  • 84.5 ← Confusing with simple mean",
            solution_steps_ar='["Sum = 85 x 4 + 90 x 3 + 75 x 3 = 340 + 270 + 225 = 835","Sum of weights = 10","Average = 835  /  10 = 83.5"]',
    tags="mean", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q77 — new — probability (complementary with dice)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.6,
            text_ar="When rolling two dice, what is the probability that the sum is less than 4?",
            option_a="1/12", option_b="1/18", option_c="^1⁄₆", option_d="2/9",
            correct_option="a",
            explanation_ar="Sum < 4 means: 2 or 3\nSum = 2: (1,1) = 1 case\nSum = 3: (1,2)(2,1) = 2 cases\nTotal = 3 cases\nProbability = ^3⁄₃₆ = 1/12\n\nWhy other options are wrong:\n  • 1/18 ← Incorrect count\n  • ^1⁄₆ ← Confusing with sum <= 4\n  • 2/9 ← Wrong calculation",
            solution_steps_ar='["Sum = 2: (1,1) = 1 case","Sum = 3: (1,2)(2,1) = 2 cases","Probability = 3  /  36 = 1/12"]',
    tags="probability", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q78 — new — quartiles (Q3)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.6,
            text_ar="Data sorted: 10, 15, 20, 25, 30, 35, 40, 45\nWhat is Q3 (third quartile)?",
            option_a="32.5", option_b="35", option_c="37.5", option_d="40",
            correct_option="c",
            explanation_ar="Upper half: 30, 35, 40, 45\nQ3 = median of upper half = (35 + 40)  /  2 = 37.5\n\nWhy other options are wrong:\n  • 32.5 ← Confusing with Q1\n  • 35 ← Just one value\n  • 40 ← Not averaging",
            solution_steps_ar='["Upper half: 30, 35, 40, 45","Q3 = median of upper half","= (35 + 40)  /  2 = 37.5"]',
    tags="range", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q79 — new — combinations (handshakes)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.6,
            text_ar="At a meeting of 6 people, each person shakes hands with every other person exactly once.\nHow many handshakes?",
            option_a="12", option_b="15", option_c="18", option_d="30",
            correct_option="b",
            explanation_ar="Handshakes = C(6,2) = 6!  /  (2!  x  4!)\n= 720  /  (2  x  24) = 720  /  48 = 15\n\nWhy other options are wrong:\n  • 12 ← Using permutations\n  • 18 ← Incorrect calculation\n  • 30 ← Counting each twice",
            solution_steps_ar='["Each handshake between 2 people = C(6,2)","= 6!  /  (2!  x  4!) = 720  /  48","= 15 handshakes"]',
    tags="counting,combination", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q80 — new — variance and mean relationship
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.6,
            text_ar="Data set: 1, 3, 5, 7\nWhat is the variance?",
            option_a="4", option_b="5", option_c="6", option_d="8",
            correct_option="b",
            explanation_ar="Mean = (1+3+5+7)  /  4 = 16  /  4 = 4\nSquared deviations: (1−4)^2=9, (3−4)^2=1, (5−4)^2=1, (7−4)^2=9\nSum = 9+1+1+9 = 20\nVariance = 20  /  4 = 5\n\nWhy other options are wrong:\n  • 4 ← Not squaring deviations\n  • 6 ← Confusing with standard deviation\n  • 8 ← Incorrect calculation",
            solution_steps_ar='["Mean = 16  /  4 = 4","Squared deviations: 9, 1, 1, 9","Sum = 20","Variance = 20  /  4 = 5"]',
    tags="variance", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q81 — new — probability (balls, with replacement)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.6,
            text_ar="A bag has 3 white balls and 7 black balls.\nTwo balls are drawn with replacement.\nWhat is the probability that first is white and second is black?",
            option_a="21/100", option_b="7/30", option_c="3/10", option_d="7/10",
            correct_option="a",
            explanation_ar="P(white) = 3/10\nP(black) = 7/10 (with replacement)\nP(white then black) = 3/10  x  7/10 = 21/100\n\nWhy other options are wrong:\n  • 7/30 ← Without replacement error\n  • 3/10 ← Only first draw\n  • 7/10 ← Only second draw",
            solution_steps_ar='["P(white) = 3  /  10","P(black) = 7  /  10 (with replacement)","P = 3/10  x  7/10 = 21/100"]',
    tags="probability", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q82 — new — counting principle (license plate)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.6,
            text_ar="A license plate has one letter (from 26) followed by 3 digits (0-9).\nHow many different plates are possible?",
            option_a="2800", option_b="28000", option_c="25200", option_d="30000",
            correct_option="b",
            explanation_ar="Letter: 26 choices\nFirst digit: 10 choices\nSecond digit: 10\nThird digit: 10\nTotal = 26  x  10  x  10  x  10 = 26000\n\nNote: Original had 28 Arabic letters, using 26 for English\n\nWhy other options are wrong:\n  • 2800 ← Missing digits\n  • 25200 ← With restriction error\n  • 30000 ← Incorrect calculation",
            solution_steps_ar='["Letter: 26 choices","Digits: 10  x  10  x  10 = 1000","Total = 26  x  1000 = 26000"]',
    tags="counting", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q83 — new — data interpretation (percentage)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.6,
            text_ar="In a survey of 500 people:\n• 40% prefer Tea\n• 35% prefer Coffee\n• The rest prefer Juice\nHow many people prefer Juice?",
            option_a="75", option_b="100", option_c="125", option_d="150",
            correct_option="c",
            explanation_ar="Juice % = 100% − 40% − 35% = 25%\nNumber = 25%  x  500 = 125\n\nWhy other options are wrong:\n  • 75 ← Incorrect percentage\n  • 100 ← Wrong calculation\n  • 150 ← Confusing with another group",
            solution_steps_ar='["Juice % = 100 − 40 − 35 = 25%","Number = 0.25  x  500","= 125 people"]',
    tags="data-interpretation", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q84 — new — mean of combined groups
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.6,
            text_ar="Group A has 10 numbers with mean 40.\nGroup B has 10 numbers with mean 60.\nWhat is the mean of both groups combined?",
            option_a="45", option_b="50", option_c="55", option_d="48",
            correct_option="b",
            explanation_ar="Sum A = 10  x  40 = 400\nSum B = 10  x  60 = 600\nMean = (400 + 600)  /  20 = 1000  /  20 = 50\n\nWhy other options are wrong:\n  • 45 ← Simple average of means (wrong weights)\n  • 55 ← Incorrect calculation\n  • 48 ← Wrong formula",
            solution_steps_ar='["Sum A = 10  x  40 = 400","Sum B = 10  x  60 = 600","Mean = 1000  /  20 = 50"]',
    tags="mean", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q85 — new — probability (die comparison)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.6,
            text_ar="When rolling two dice, what is the probability that the first roll is greater than the second?",
            option_a="1/4", option_b="5/12", option_c="1/2", option_d="^7⁄₁₂",
            correct_option="b",
            explanation_ar="Total cases = 36\nBy symmetry: P(first > second) = P(first < second)\nP(equal) = ^6⁄₃₆ = 1/6\nP(first > second) = (1 − 1/6)  /  2 = 5/6  /  2 = 5/12\n\nWhy other options are wrong:\n  • 1/4 ← Incorrect count\n  • 1/2 ← Ignoring equal cases\n  • ^7⁄₁₂ ← Wrong calculation",
            solution_steps_ar='["P(equal) = 6  /  36 = 1/6","By symmetry: P(greater) = P(smaller)","P(greater) = (1 − 1/6)  /  2 = 5/12"]',
    tags="probability", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q86 — new — IQR application
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.6,
            text_ar="Data: 2, 4, 5, 7, 8, 9, 10, 12, 13, 15, 16, 18\nWhat is the median?",
            option_a="8.5", option_b="9", option_c="9.5", option_d="10",
            correct_option="c",
            explanation_ar="Number of values = 12 (even)\n6th value = 9, 7th value = 10\nMedian = (9 + 10)  /  2 = 9.5\n\nWhy other options are wrong:\n  • 8.5 ← Wrong position\n  • 9 ← Only 6th value\n  • 10 ← Only 7th value",
            solution_steps_ar='["Number of values = 12 (even)","Middle two: value 6 = 9 and value 7 = 10","Median = (9 + 10)  /  2 = 9.5"]',
    tags="median", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q87 — new — probability (neither event)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.6,
            text_ar="In a class of 40 students: 18 play football, 15 play basketball, 8 play both.\nHow many students play neither sport?",
            option_a="10", option_b="15", option_c="20", option_d="25",
            correct_option="b",
            explanation_ar="Number who play at least one:\nN(F union B) = N(F) + N(B) − N(F intersection B)\n= 18 + 15 − 8 = 25\nNumber who play neither = 40 − 25 = 15\n\nWhy other options are wrong:\n  • 10 ← Incorrect calculation\n  • 20 ← Not subtracting intersection\n  • 25 ← Those who play at least one",
            solution_steps_ar='["N(F union B) = 18 + 15 − 8 = 25","Neither = 40 − 25","= 15 students"]',
    tags="probability", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q88 — new — permutations (digits no repeat)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.6,
            text_ar="How many 4-digit numbers with different digits can be formed from {1, 2, 3, 4, 5}?",
            option_a="60", option_b="120", option_c="24", option_d="500",
            correct_option="b",
            explanation_ar="Permutation: P(5,4) = 5!  /  (5−4)! = 5!  /  1! = 120\n\nWhy other options are wrong:\n  • 60 ← Incorrect calculation\n  • 24 ← Only 4! without considering selection\n  • 500 ← With repetition",
            solution_steps_ar='["P(5,4) = 5  x  4  x  3  x  2","= 120 numbers"]',
    tags="counting", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q89 — new — frequency distribution (mean)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.6,
            text_ar="Frequency table:\nClass:   [10-20) [20-30) [30-40)\nFrequency:  4       6       10\nEstimate the mean using class midpoints.",
            option_a="27", option_b="28", option_c="29", option_d="30",
            correct_option="b",
            explanation_ar="Midpoints: 15, 25, 35\nSum = 15 x 4 + 25 x 6 + 35 x 10 = 60 + 150 + 350 = 560\nCount = 4 + 6 + 10 = 20\nMean = 560  /  20 = 28\n\nWhy other options are wrong:\n  • 27 ← Incorrect calculation\n  • 29 ← Wrong midpoints\n  • 30 ← Confusing with another value",
            solution_steps_ar='["Midpoints: 15, 25, 35","Sum = 15 x 4 + 25 x 6 + 35 x 10 = 560","Mean = 560  /  20 = 28"]',
    tags="mean,data-interpretation", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q90 — new — probability (cards, suit)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.6,
            text_ar="From a standard deck (52 cards), what is the probability of drawing a Spade (♠) or a Jack?",
            option_a="13/52", option_b="16/52", option_c="4/13", option_d="^1^7⁄₅₂",
            correct_option="c",
            explanation_ar="P(Spade) = 13/52\nP(Jack) = ^4⁄₅₂\nP(Spade intersection Jack) = ^1⁄₅₂ (Jack of Spades)\nP(Spade union Jack) = 13/52 + ^4⁄₅₂ − ^1⁄₅₂ = 16/52 = 4/13\n\nWhy other options are wrong:\n  • 13/52 ← Only Spades\n  • 16/52 ← Not simplified\n  • ^1^7⁄₅₂ ← Adding instead of union",
            solution_steps_ar='["P(Spade) = 13  /  52","P(Jack) = 4  /  52","P(Spade intersection Jack) = 1  /  52","P(Spade union Jack) = (13 + 4 − 1)  /  52 = 16  /  52 = 4/13"]',
    tags="probability", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q91 — new — effect on mean (doubling)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.6,
            text_ar="If the mean of 5 numbers = 12.\nWhat is the new mean if each number is multiplied by 3?",
            option_a="15", option_b="36", option_c="48", option_d="60",
            correct_option="b",
            explanation_ar="When all values are multiplied by a constant:\nNew mean = Old mean  x  constant\n= 12  x  3 = 36\n\nWhy other options are wrong:\n  • 15 ← Adding instead of multiplying\n  • 48 ← Incorrect calculation\n  • 60 ← Wrong formula",
            solution_steps_ar='["When all values multiplied by k:","New mean = Mean  x  k","= 12  x  3 = 36"]',
    tags="mean", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q92 — new — standard deviation (multiplication effect)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.6,
            text_ar="If the standard deviation of a data set = 4.\nWhat is the new standard deviation if each number is multiplied by 2?",
            option_a="2", option_b="4", option_c="6", option_d="8",
            correct_option="d",
            explanation_ar="When all values are multiplied by constant k:\nNew SD = SD  x  |k|\n= 4  x  2 = 8\n\nWhy other options are wrong:\n  • 2 ← Dividing instead of multiplying\n  • 4 ← No change (wrong)\n  • 6 ← Incorrect calculation",
            solution_steps_ar='["When multiplying by k: New SD = SD  x  |k|","= 4  x  2","= 8"]',
    tags="standard-deviation", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q93 — new — counting (seating in a circle)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.6,
            text_ar="How many ways can 4 people sit around a circular table?",
            option_a="4", option_b="6", option_c="12", option_d="24",
            correct_option="b",
            explanation_ar="Circular permutations = (n − 1)!\n= (4 − 1)! = 3! = 6\n\nWhy other options are wrong:\n  • 4 ← Linear arrangement error\n  • 12 ← Incorrect calculation\n  • 24 ← Not adjusting for circular arrangement",
            solution_steps_ar='["Circular permutations = (n − 1)!","= (4 − 1)! = 3!","= 3  x  2  x  1 = 6"]',
    tags="counting", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q94 — new — box plot outlier concept
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.6,
            text_ar="In a box plot:\nQ1 = 10, Q3 = 30\nWhat is the upper bound for outliers?\n(Bound = Q3 + 1.5  x  IQR)",
            option_a="40", option_b="50", option_c="60", option_d="75",
            correct_option="c",
            explanation_ar="IQR = Q3 − Q1 = 30 − 10 = 20\nUpper bound = Q3 + 1.5  x  IQR = 30 + 1.5  x  20 = 30 + 30 = 60\n\nWhy other options are wrong:\n  • 40 ← Incorrect IQR\n  • 50 ← Wrong calculation\n  • 75 ← Using 2.5 instead of 1.5",
            solution_steps_ar='["IQR = 30 − 10 = 20","Upper bound = Q3 + 1.5  x  IQR","= 30 + 30 = 60"]',
    tags="range,data-interpretation", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ══════════════════════════════════════════════════════════════
        # Difficulty 0.7 — (11 questions)
        # ══════════════════════════════════════════════════════════════

        # Q95 — existing — above mean
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.7,
            text_ar="In a test, 8 students scored:\n65, 70, 75, 80, 85, 90, 95, 100\nHow many students scored above the mean?",
            option_a="3", option_b="4", option_c="5", option_d="6",
            correct_option="b",
            explanation_ar="Step 1: Calculate mean\n  Sum = 65+70+75+80+85+90+95+100 = 660\n  Mean = 660  /  8 = 82.5\n\nStep 2: Count scores above 82.5\n  85, 90, 95, 100 ← 4 students\n\nWhy other options are wrong:\n  • 3 ← Incorrect count\n  • 5 ← Wrong cutoff\n  • 6 ← Confusing with median",
            solution_steps_ar='["Sum = 65+70+75+80+85+90+95+100 = 660","Mean = 660  /  8 = 82.5","Scores above 82.5: {85, 90, 95, 100} ← 4 students"]',
    tags="mean", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # Q96 — existing — committee with women
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.7,
            text_ar="A committee of 3 is chosen from 4 men and 3 women with the condition that it includes at least one woman.\nHow many ways?",
            option_a="21", option_b="31", option_c="35", option_d="34",
            correct_option="b",
            explanation_ar="Given:\n  4 men, 3 women, choose 3 with >= 1 woman\n\nSolution:\n  Method: All − (no women)\n  All = C(7,3) = 35\n  No women (3 men only) = C(4,3) = 4\n  Answer = 35 − 4 = 31\n\nWhy other options are wrong:\n  • 21 ← Incorrect calculation\n  • 35 ← Not subtracting all-men case\n  • 34 ← Wrong subtraction",
            solution_steps_ar='["Total ways = C(7,3) = 35","Ways with no women = C(4,3) = 4","Answer = 35 − 4 = 31 ways"]',
    tags="combination,conditional-probability", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # Q97 — existing — mean+sd shift
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.7,
            text_ar="A data set has: Mean = 50 and Standard Deviation = 5.\nIf 10 is added to each value, what are the new mean and standard deviation?",
            option_a="Mean = 60, SD = 5", option_b="Mean = 60, SD = 15",
            option_c="Mean = 50, SD = 15", option_d="Mean = 50, SD = 5",
            correct_option="a",
            explanation_ar="Given:\n  Mean = 50, SD = 5\n  Add 10 to each value\n\nSolution:\n  Adding a constant:\n  • Mean increases by same constant: 50 + 10 = 60\n  • SD unchanged (measures spread): 5\n\nWhy other options are wrong:\n  • Mean = 60, SD = 15 ← SD changes with multiplication, not addition\n  • Mean = 50, SD = 15 ← Mean should increase\n  • Mean = 50, SD = 5 ← Mean should increase",
            solution_steps_ar='["When adding constant to all values:","New mean = 50 + 10 = 60","Standard deviation unaffected by shift = 5"]',
    tags="mean,standard-deviation", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # Q98 — new — conditional probability (independent events)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.7,
            text_ar="P(Math success) = 0.7 and P(Physics success) = 0.8.\nIf events are independent, what is P(success in both)?",
            option_a="0.50", option_b="0.56", option_c="0.75", option_d="1.50",
            correct_option="b",
            explanation_ar="Events are independent:\nP(Math intersection Physics) = P(M)  x  P(P)\n= 0.7  x  0.8 = 0.56\n\nWhy other options are wrong:\n  • 0.50 ← Incorrect calculation\n  • 0.75 ← Adding instead of multiplying\n  • 1.50 ← Impossible probability",
            solution_steps_ar='["Events are independent","P(success in both) = P(M)  x  P(P)","= 0.7  x  0.8 = 0.56"]',
    tags="probability,conditional-probability", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # Q99 — new — permutations with identical items
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.7,
            text_ar="How many arrangements of letters in \"book\" (b, o, o, k)?",
            option_a="12", option_b="24", option_c="48", option_d="6",
            correct_option="a",
            explanation_ar="Number of letters = 4\n'o' repeats 2 times\nArrangements = 4!  /  2! = 24  /  2 = 12\n\nWhy other options are wrong:\n  • 24 ← Not adjusting for repeats\n  • 48 ← Incorrect calculation\n  • 6 ← Wrong formula",
            solution_steps_ar='["4! = 24","Letter o repeats 2 times: 2! = 2","Arrangements = 24  /  2 = 12"]',
    tags="permutation", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # Q100 — new — probability (at least one of two events)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.7,
            text_ar="P(Rain on Saturday) = 1/3 and P(Rain on Sunday) = 1/4.\nIf independent, what is P(rain on at least one day)?",
            option_a="1/2", option_b="^7⁄₁₂", option_c="1/4", option_d="1/3",
            correct_option="a",
            explanation_ar="P(no rain Saturday) = 2/3\nP(no rain Sunday) = 3/4\nP(no rain at all) = 2/3  x  3/4 = ^6⁄₁₂ = 1/2\nP(rain at least one day) = 1 − 1/2 = 1/2\n\nWhy other options are wrong:\n  • ^7⁄₁₂ ← Adding probabilities\n  • 1/4 ← Only Sunday\n  • 1/3 ← Only Saturday",
            solution_steps_ar='["P(no rain Sat) = 2/3, P(no rain Sun) = 3/4","P(no rain) = 2/3  x  3/4 = 1/2","P(rain at least one) = 1 − 1/2 = 1/2"]',
    tags="probability,conditional-probability", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # Q101 — new — variance (from standard deviation)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.7,
            text_ar="If SD = 6, and each value is multiplied by 3 then 5 is added.\nWhat is the new variance?",
            option_a="36", option_b="18", option_c="324", option_d="189",
            correct_option="c",
            explanation_ar="Original SD = 6\nAfter multiplying by 3: New SD = 6  x  3 = 18\n(Adding 5 does not affect SD)\nVariance = 18^2 = 324\n\nWhy other options are wrong:\n  • 36 ← Original variance\n  • 18 ← New SD, not variance\n  • 189 ← Incorrect calculation",
            solution_steps_ar='["SD after multiplying by 3 = 6  x  3 = 18","Adding 5 does not change SD","Variance = 18^2 = 324"]',
    tags="variance,standard-deviation", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # Q102 — new — combinations (team selection)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.7,
            text_ar="A team of 5 is chosen from 8 players.\nIf one specific player must be on the team, how many ways?",
            option_a="21", option_b="35", option_c="56", option_d="70",
            correct_option="b",
            explanation_ar="Specific player is already on team -> choose 4 from remaining 7\nC(7,4) = 7!  /  (4!  x  3!) = 5040  /  (24  x  6) = 5040  /  144 = 35\n\nWhy other options are wrong:\n  • 21 ← Incorrect calculation\n  • 56 ← Not accounting for fixed player\n  • 70 ← Wrong formula",
            solution_steps_ar='["Specific player chosen -> choose 4 from remaining 7","C(7,4) = 7!  /  (4!  x  3!)","= 5040  /  144 = 35"]',
    tags="combination", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # Q103 — new — data interpretation (comparing means)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.7,
            text_ar="Class A has 20 students with mean 65.\nClass B has 30 students with mean 75.\nA new student joins Class A with score 86.\nWhat is the new mean for Class A?",
            option_a="65", option_b="66", option_c="67", option_d="68",
            correct_option="b",
            explanation_ar="Old sum A = 20  x  65 = 1300\nNew sum A = 1300 + 86 = 1386\nNew count = 21\nNew mean = 1386  /  21 = 66\n\nWhy other options are wrong:\n  • 65 ← No change (incorrect)\n  • 67 ← Wrong calculation\n  • 68 ← Incorrect formula",
            solution_steps_ar='["Old sum = 20  x  65 = 1300","New sum = 1300 + 86 = 1386","New mean = 1386  /  21 = 66"]',
    tags="mean", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # Q104 — new — probability (geometric)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.7,
            text_ar="A spinner has 8 equal sectors: 3 red, 2 blue, 3 green.\nWhat is P(landing on red or blue)?",
            option_a="3/8", option_b="1/2", option_c="5/8", option_d="3/4",
            correct_option="c",
            explanation_ar="Favorable sectors = 3 + 2 = 5\nTotal = 8\nProbability = 5/8\n\nWhy other options are wrong:\n  • 3/8 ← Only red\n  • 1/2 ← Incorrect count\n  • 3/4 ← Overcounting",
            solution_steps_ar='["Red + Blue sectors = 3 + 2 = 5","Total = 8","Probability = 5/8"]',
    tags="probability", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # Q105 — new — frequency cumulative
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.7,
            text_ar="Cumulative frequency table for 50 students:\nLess than 50: 12 students\nLess than 60: 25 students\nLess than 70: 38 students\nLess than 80: 50 students\nHow many students scored in [60-70)?",
            option_a="12", option_b="13", option_c="25", option_d="38",
            correct_option="b",
            explanation_ar="Cumulative less than 70 = 38\nCumulative less than 60 = 25\nIn [60-70) = 38 − 25 = 13\n\nWhy other options are wrong:\n  • 12 ← Wrong reading\n  • 25 ← Cumulative at 60\n  • 38 ← Cumulative at 70",
            solution_steps_ar='["Less than 70 = 38 students","Less than 60 = 25 students","[60-70) = 38 − 25 = 13 students"]',
    tags="data-interpretation", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # ══════════════════════════════════════════════════════════════
        # Difficulty 0.8 — (6 questions)
        # ══════════════════════════════════════════════════════════════

        # Q106 — existing — permutations P(5,3)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.8,
            text_ar="How many ways can 3 people be arranged in a row of 5 seats?",
            option_a="15", option_b="30", option_c="60", option_d="120",
            correct_option="c",
            explanation_ar="Given:\n  Seats = 5\n  People = 3\n\nSolution (permutations):\n  P(5,3) = 5!  /  (5−3)!\n  = 5!  /  2!\n  = (5  x  4  x  3  x  2  x  1)  /  (2  x  1)\n  = 120  /  2 = 60\n\nWhy other options are wrong:\n  • 15 ← Using combinations\n  • 30 ← Incorrect calculation\n  • 120 ← Not dividing by 2!",
            solution_steps_ar='["Permutation formula: P(n,r) = n!  /  (n−r)!","P(5,3) = 5!  /  2!","= 120  /  2 = 60 ways"]',
    tags="permutation", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        # Q107 — existing — std dev comparison
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.8,
            text_ar="Two data sets:\n• Set A: 10, 10, 10, 10, 10\n• Set B: 2, 6, 10, 14, 18\nBoth have mean = 10\nWhich set has greater standard deviation?",
            option_a="Set A", option_b="Set B", option_c="Equal", option_d="Cannot determine",
            correct_option="b",
            explanation_ar="Given:\n  Mean A = Mean B = 10\n\nAnalysis:\n  Set A: All values = 10 -> No deviation from mean\n  Therefore: SD = 0\n\n  Set B: Values spread out from mean\n  Deviations: −8, −4, 0, +4, +8\n  Therefore: SD > 0\n\nTherefore: Set B has greater standard deviation\n\nWhy other options are wrong:\n  • Set A ← All values identical (SD=0)\n  • Equal ← Set B has spread\n  • Cannot determine ← Can be determined",
            solution_steps_ar='["Set A: All values = 10 -> SD = 0","Set B: Values spread (2 to 18) -> larger SD","Therefore: Set B has greater standard deviation"]',
    tags="mean,standard-deviation", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        # Q108 — existing — Bayes
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.8,
            text_ar="A factory has two production lines:\nLine A produces 60% of items with 3% defect rate.\nLine B produces 40% of items with 5% defect rate.\nIf an item is randomly selected, what is P(defective)?",
            option_a="0.028", option_b="0.038", option_c="0.040", option_d="0.080",
            correct_option="b",
            explanation_ar="Given:\n  Line A: 60%, defects 3%\n  Line B: 40%, defects 5%\n\nSolution (total probability):\n  P(defective) = P(A)  x  P(defect|A) + P(B)  x  P(defect|B)\n  = 0.6  x  0.03 + 0.4  x  0.05\n  = 0.018 + 0.020 = 0.038\n\nWhy other options are wrong:\n  • 0.028 ← Incorrect calculation\n  • 0.040 ← Simple average\n  • 0.080 ← Adding defect rates",
            solution_steps_ar='["P(defective) = P(A) x P(defect|A) + P(B) x P(defect|B)","= 0.6  x  0.03 + 0.4  x  0.05","= 0.018 + 0.020 = 0.038"]',
    tags="probability,conditional-probability,data-interpretation", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        # Q109 — new — combinations with constraint (both genders)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.8,
            text_ar="A team of 4 is chosen from 5 men and 4 women with condition: 2 men and 2 women.\nHow many ways?",
            option_a="40", option_b="60", option_c="80", option_d="120",
            correct_option="b",
            explanation_ar="Choose 2 men from 5: C(5,2) = 10\nChoose 2 women from 4: C(4,2) = 6\nTotal = 10  x  6 = 60\n\nWhy other options are wrong:\n  • 40 ← Incorrect calculation\n  • 80 ← Wrong formula\n  • 120 ← Not applying constraint",
            solution_steps_ar='["C(5,2) = 10 (choose men)","C(4,2) = 6 (choose women)","Total = 10  x  6 = 60 ways"]',
    tags="combination,conditional-probability", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        # Q110 — new — Bayes theorem (full)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.8,
            text_ar="Two boxes:\nBox 1: 3 red balls and 7 blue balls\nBox 2: 8 red balls and 2 blue balls\nA box is chosen randomly, then a ball is drawn.\nIf the ball is red, what is P(it came from Box 2)?",
            option_a="8/11", option_b="3/11", option_c="⅘", option_d="1/2",
            correct_option="a",
            explanation_ar="P(red|Box 1) = 3/10, P(red|Box 2) = ^8⁄₁₀\nP(Box 1) = P(Box 2) = 1/2\nP(red) = 1/2  x  3/10 + 1/2  x  ^8⁄₁₀ = 3/20 + 8/20 = 11/20\nP(Box 2|red) = (1/2  x  ^8⁄₁₀)  /  11/20 = 8/20  /  11/20 = 8/11\n\nWhy other options are wrong:\n  • 3/11 ← Confusing with Box 1\n  • ⅘ ← Not using Bayes\n  • 1/2 ← Prior probability",
            solution_steps_ar='["P(red) = 1/2  x  3/10 + 1/2  x  ^8⁄₁₀ = 11/20","P(Box 2|red) = P(Box 2 intersection red)  /  P(red)","= (1/2  x  ^8⁄₁₀)  /  11/20 = 8/20  x  20/11 = 8/11"]',
    tags="probability,conditional-probability,data-interpretation", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        # Q111 — new — standard deviation calculation
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.8,
            text_ar="Data set: 2, 4, 6, 8, 10\nWhat is the standard deviation (approximately)?",
            option_a="2", option_b="sqrt8 ~ 2.83", option_c="sqrt10 ~ 3.16", option_d="4",
            correct_option="b",
            explanation_ar="Mean = (2+4+6+8+10)  /  5 = 30  /  5 = 6\nSquared deviations: 16, 4, 0, 4, 16\nVariance = (16+4+0+4+16)  /  5 = 40  /  5 = 8\nSD = sqrt8 ~ 2.83\n\nWhy other options are wrong:\n  • 2 ← Not squaring deviations\n  • sqrt10 ~ 3.16 ← Wrong calculation\n  • 4 ← Variance value",
            solution_steps_ar='["Mean = 30  /  5 = 6","Squared deviations: 16, 4, 0, 4, 16","Variance = 40  /  5 = 8","SD = sqrt8 ~ 2.83"]',
    tags="standard-deviation", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        # ══════════════════════════════════════════════════════════════
        # Additional Questions 112-167 (56 questions)
        # Distribution: 0.2->3 | 0.3->5 | 0.4->10 | 0.5->10 | 0.6->12 | 0.7->10 | 0.8->6
        # ══════════════════════════════════════════════════════════════

        # ── Difficulty 0.2 (3 questions) — diagnostic ──

        # Q112 — frequency table reading
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.2,
            text_ar="Frequency table shows books read by 5 students:\nAhmad: 3, Sara: 5, Khalid: 2, Noura: 4, Fahd: 6\nWhat is the total books read?",
            option_a="18", option_b="20", option_c="22", option_d="24",
            correct_option="b",
            explanation_ar="Total = 3 + 5 + 2 + 4 + 6 = 20\n\nWhy other options are wrong:\n  • 18 ← Missing one value\n  • 22 ← Adding extra\n  • 24 ← Wrong calculation",
            solution_steps_ar='["Total = 3 + 5 + 2 + 4 + 6","= 20 books"]',
    tags="frequency,data-interpretation", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # Q113 — simple range from stem-and-leaf
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.2,
            text_ar="Data sorted: 10, 15, 20, 25, 30\nWhat is the range?",
            option_a="15", option_b="20", option_c="25", option_d="30",
            correct_option="b",
            explanation_ar="Range = Max − Min = 30 − 10 = 20\n\nWhy other options are wrong:\n  • 15 ← Incorrect subtraction\n  • 25 ← Confusing with Q3\n  • 30 ← Maximum only",
            solution_steps_ar='["Maximum = 30","Minimum = 10","Range = 30 − 10 = 20"]',
    tags="range,data-interpretation", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # Q114 — basic expected value
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.2,
            text_ar="A fair die is rolled once.\nWhat is the expected value?",
            option_a="3", option_b="3.5", option_c="4", option_d="3.75",
            correct_option="b",
            explanation_ar="Expected value = (1+2+3+4+5+6)  /  6 = 21  /  6 = 3.5\n\nWhy other options are wrong:\n  • 3 ← Incorrect calculation\n  • 4 ← Wrong formula\n  • 3.75 ← Confusing with another value",
            solution_steps_ar='["Sum of faces = 1+2+3+4+5+6 = 21","Number of faces = 6","Expected value = 21  /  6 = 3.5"]',
    tags="mean,probability", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ── Difficulty 0.3 (5 questions) — foundation ──

        # Q115 — frequency table: mode
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.3,
            text_ar="Frequency table for 20 students:\nScore 5: freq 2 | Score 6: freq 5 | Score 7: freq 8 | Score 8: freq 3 | Score 9: freq 2\nWhat is the mode?",
            option_a="6", option_b="7", option_c="8", option_d="9",
            correct_option="b",
            explanation_ar="Highest frequency is 8 for score 7\nMode = 7\n\nWhy other options are wrong:\n  • 6 ← Not highest frequency\n  • 8 ← Wrong score\n  • 9 ← Confusing with position",
            solution_steps_ar='["Compare frequencies: 2, 5, 8, 3, 2","Highest frequency = 8 (for score 7)","Mode = 7"]',
    tags="mode,frequency", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # Q116 — stem-and-leaf reading
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.3,
            text_ar="Stem-and-leaf plot for ages:\nStem | Leaf\n  1   | 5, 7, 8\n  2   | 0, 3, 3, 9\n  3   | 1, 4\nHow many people are younger than 25?",
            option_a="4", option_b="5", option_c="6", option_d="7",
            correct_option="b",
            explanation_ar="Ages < 25: 15, 17, 18, 20, 23 = 5 people\n\nWhy other options are wrong:\n  • 4 ← Missing one\n  • 6 ← Including 25\n  • 7 ← Wrong count",
            solution_steps_ar='["From stem 1: 15, 17, 18 -> 3 values","From stem 2: 20, 23 (less than 25) -> 2 values","Total = 3 + 2 = 5"]',
    tags="data-interpretation,frequency", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q117 — simple quartile
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.3,
            text_ar="Data sorted: 2, 4, 6, 8, 10, 12, 14\nWhat is the median (Q2)?",
            option_a="6", option_b="7", option_c="8", option_d="10",
            correct_option="c",
            explanation_ar="Number of values = 7 (odd)\nMedian = 4th value = 8\n\nWhy other options are wrong:\n  • 6 ← Wrong position\n  • 7 ← Average incorrectly\n  • 10 ← Wrong position",
            solution_steps_ar='["Number of values = 7","Median position = (7+1)  /  2 = 4","4th value = 8"]',
    tags="median,percentile", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q118 — independent events
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.3,
            text_ar="A die is rolled, then a coin is tossed.\nWhat is P(even number AND heads)?",
            option_a="1/4", option_b="1/2", option_c="1/3", option_d="1/6",
            correct_option="a",
            explanation_ar="P(even) = ^3⁄₆ = 1/2\nP(heads) = 1/2\nIndependent: P(even AND heads) = 1/2  x  1/2 = 1/4\n\nWhy other options are wrong:\n  • 1/2 ← Only one event\n  • 1/3 ← Incorrect calculation\n  • 1/6 ← Confusing with single outcome",
            solution_steps_ar='["P(even) = 3/6 = 1/2","P(heads) = 1/2","Independent -> 1/2  x  1/2 = 1/4"]',
    tags="probability,counting", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q119 — factorial basics
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.3,
            text_ar="Using definition n! = n  x  (n−1)  x  ...  x  1, what is 5!?",
            option_a="20", option_b="60", option_c="120", option_d="720",
            correct_option="c",
            explanation_ar="5! = 5  x  4  x  3  x  2  x  1 = 120\n\nWhy other options are wrong:\n  • 20 ← Only first two terms\n  • 60 ← Missing a factor\n  • 720 ← 6! value",
            solution_steps_ar='["5! = 5  x  4  x  3  x  2  x  1","= 20  x  6","= 120"]',
    tags="counting,permutation", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Difficulty 0.4 (10 questions) ──

        # Q120 — quartiles from data
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.4,
            text_ar="Data sorted: 3, 5, 7, 9, 11, 13, 15, 17\nWhat is Q1?",
            option_a="5", option_b="6", option_c="7", option_d="8",
            correct_option="b",
            explanation_ar="Number of values = 8\nLower half: 3, 5, 7, 9\nQ1 = median of lower half = (5 + 7)  /  2 = 6\n\nWhy other options are wrong:\n  • 5 ← Just second value\n  • 7 ← Not averaging\n  • 8 ← Wrong half",
            solution_steps_ar='["Lower half: 3, 5, 7, 9","Q1 = (5 + 7)  /  2 = 6"]',
    tags="percentile,median", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q121 — box plot: IQR
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.4,
            text_ar="Box plot shows:\nQ1 = 20, Q2 = 35, Q3 = 50\nWhat is the IQR?",
            option_a="15", option_b="20", option_c="30", option_d="35",
            correct_option="c",
            explanation_ar="IQR = Q3 − Q1 = 50 − 20 = 30\n\nWhy other options are wrong:\n  • 15 ← Q2 − Q1\n  • 20 ← Confusing with Q1\n  • 35 ← Q2 value",
            solution_steps_ar='["Q3 = 50","Q1 = 20","IQR = Q3 − Q1 = 50 − 20 = 30"]',
    tags="box-plot,percentile", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q122 — frequency table: mean
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.4,
            text_ar="Frequency table:\nValue 2: freq 3 | Value 4: freq 5 | Value 6: freq 2\nWhat is the mean?",
            option_a="3.4", option_b="3.6", option_c="3.8", option_d="4.0",
            correct_option="c",
            explanation_ar="Sum = 2 x 3 + 4 x 5 + 6 x 2 = 6 + 20 + 12 = 38\nCount = 3 + 5 + 2 = 10\nMean = 38  /  10 = 3.8\n\nWhy other options are wrong:\n  • 3.4 ← Incorrect calculation\n  • 3.6 ← Wrong sum\n  • 4.0 ← Confusing with another value",
            solution_steps_ar='["Sum = 2 x 3 + 4 x 5 + 6 x 2 = 6 + 20 + 12 = 38","Count = 3 + 5 + 2 = 10","Mean = 38  /  10 = 3.8"]',
    tags="mean,frequency", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q123 — dependent events
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.4,
            text_ar="A bag has 3 red and 2 blue balls.\nA ball is drawn without replacement, then another.\nWhat is P(first red AND second blue)?",
            option_a="3/10", option_b="6/20", option_c="2/5", option_d="⅕",
            correct_option="a",
            explanation_ar="P(first red) = ^3⁄₅\nP(second blue | first red) = ^2⁄₄ = 1/2\nP(both) = ^3⁄₅  x  1/2 = 3/10\n\nWhy other options are wrong:\n  • 6/20 ← Not simplified\n  • 2/5 ← Only first draw\n  • ⅕ ← Incorrect calculation",
            solution_steps_ar='["P(first red) = 3/5","After drawing: 2 red + 2 blue = 4","P(second blue) = 2/4 = 1/2","P = ^3⁄₅  x  1/2 = 3/10"]',
    tags="probability,conditional-probability", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q124 — stem-and-leaf: median
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.4,
            text_ar="Stem-and-leaf plot:\nStem | Leaf\n  2   | 1, 5\n  3   | 0, 3, 7\n  4   | 2, 8\nWhat is the median?",
            option_a="30", option_b="33", option_c="37", option_d="35",
            correct_option="b",
            explanation_ar="Data: 21, 25, 30, 33, 37, 42, 48\nNumber of values = 7\nMedian = 4th value = 33\n\nWhy other options are wrong:\n  • 30 ← Wrong position\n  • 37 ← Wrong position\n  • 35 ← Not in data",
            solution_steps_ar='["Data sorted: 21, 25, 30, 33, 37, 42, 48","Count = 7","Median = 4th value = 33"]',
    tags="median,data-interpretation", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q125 — permutation simple
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.4,
            text_ar="How many ways to arrange 3 people in 3 seats?",
            option_a="3", option_b="6", option_c="9", option_d="12",
            correct_option="b",
            explanation_ar="3! = 3  x  2  x  1 = 6\n\nWhy other options are wrong:\n  • 3 ← Adding instead of multiplying\n  • 9 ← Incorrect calculation\n  • 12 ← Wrong formula",
            solution_steps_ar='["3! = 3  x  2  x  1","= 6 ways"]',
    tags="permutation,counting", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q126 — expected value with weights
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.4,
            text_ar="Game: Win $10 with probability 1/3 or lose $5 with probability 2/3.\nWhat is expected value?",
            option_a="−1", option_b="0", option_c="1", option_d="2",
            correct_option="b",
            explanation_ar="EV = 10  x  1/3 + (−5)  x  2/3\n= ^1^0⁄₃ − ^1^0⁄₃ = 0\n\nWhy other options are wrong:\n  • −1 ← Incorrect calculation\n  • 1 ← Wrong signs\n  • 2 ← Confusing with another value",
            solution_steps_ar='["Expected win = 10  x  1/3 = 10/3","Expected loss = −5  x  2/3 = −10/3","EV = 10/3 − 10/3 = 0"]',
    tags="probability,mean", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q127 — geometric probability (simple)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.4,
            text_ar="Square board side 10 cm, with circle radius 5 cm in center.\nIf a dart is thrown randomly, what is P(hitting circle)?",
            option_a="0.50", option_b="0.65", option_c="0.79", option_d="0.85",
            correct_option="c",
            explanation_ar="Square area = 10  x  10 = 100\nCircle area = pi  x  5^2 = 25pi ~ 78.54\nP = 78.54  /  100 ~ 0.79\n\nWhy other options are wrong:\n  • 0.50 ← Radius/Side ratio\n  • 0.65 ← Incorrect calculation\n  • 0.85 ← Overestimate",
            solution_steps_ar='["Square area = 100 cm^2","Circle area = pi  x  25 ~ 78.54 cm^2","P = 78.54  /  100 ~ 0.79"]',
    tags="probability,counting", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q128 — survey sample
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.4,
            text_ar="Survey of 200 people: 35% prefer reading, 45% sports, rest travel.\nHow many prefer travel?",
            option_a="30", option_b="40", option_c="50", option_d="60",
            correct_option="b",
            explanation_ar="Travel % = 100% − 35% − 45% = 20%\nNumber = 20%  x  200 = 40\n\nWhy other options are wrong:\n  • 30 ← Wrong percentage\n  • 50 ← Incorrect calculation\n  • 60 ← Confusing with sports",
            solution_steps_ar='["Travel % = 100 − 35 − 45 = 20%","Number = 0.20  x  200 = 40 people"]',
    tags="data-interpretation,frequency", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q129 — pigeonhole simple
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.4,
            text_ar="Drawer has 10 red, 10 blue, 10 black socks (mixed in dark).\nWhat is minimum socks to draw to guarantee a matching pair?",
            option_a="3", option_b="4", option_c="5", option_d="6",
            correct_option="b",
            explanation_ar="Pigeonhole: 3 colors (holes)\nWorst case: 3 socks, each different color\n4th sock must match one color\nAnswer = 3 + 1 = 4\n\nWhy other options are wrong:\n  • 3 ← Could be all different\n  • 5 ← More than needed\n  • 6 ← Excess",
            solution_steps_ar='["Number of colors = 3","Worst case: 3 socks of 3 different colors","Next sock (4th) must match one color","Answer = 4"]',
    tags="counting,probability", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Difficulty 0.5 (10 questions) ──

        # Q130 — percentile calculation
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.5,
            text_ar="Test with 80 students. Saad scored higher than 60 students.\nWhat percentile is Saad in?",
            option_a="60th", option_b="75th", option_c="80th", option_d="25th",
            correct_option="b",
            explanation_ar="Percentile = (Number below  /  Total)  x  100\n= (60  /  80)  x  100 = 75\nSaad is at 75th percentile\n\nWhy other options are wrong:\n  • 60th ← Just the count\n  • 80th ← Total students\n  • 25th ← Wrong calculation",
            solution_steps_ar='["Percentile = (Below  /  Total)  x  100","= (60  /  80)  x  100","= 75 -> 75th percentile"]',
    tags="percentile,data-interpretation", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q131 — box plot outlier detection
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.5,
            text_ar="Box plot: Q1 = 10, Q3 = 30\nWhat is upper bound for non-outliers?",
            option_a="40", option_b="50", option_c="60", option_d="70",
            correct_option="c",
            explanation_ar="IQR = Q3 − Q1 = 30 − 10 = 20\nUpper bound = Q3 + 1.5  x  IQR = 30 + 30 = 60\n\nWhy other options are wrong:\n  • 40 ← Q3 + Q1\n  • 50 ← Wrong multiplier\n  • 70 ← Q3 + 2  x  IQR",
            solution_steps_ar='["IQR = 30 − 10 = 20","Upper bound = Q3 + 1.5  x  IQR","= 30 + 30 = 60"]',
    tags="box-plot,percentile", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q132 — frequency table: weighted mean
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.5,
            text_ar="Course grade:\nMidterm (weight 40%): 70\nFinal (weight 60%): 90\nWhat is weighted average?",
            option_a="78", option_b="80", option_c="82", option_d="84",
            correct_option="c",
            explanation_ar="Average = 70  x  0.4 + 90  x  0.6 = 28 + 54 = 82\n\nWhy other options are wrong:\n  • 78 ← Incorrect weights\n  • 80 ← Simple average\n  • 84 ← Wrong calculation",
            solution_steps_ar='["Midterm = 70  x  0.4 = 28","Final = 90  x  0.6 = 54","Average = 28 + 54 = 82"]',
    tags="mean,data-interpretation", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q133 — combination vs permutation
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.5,
            text_ar="How many ways to choose a committee of 3 from 7 candidates?",
            option_a="21", option_b="35", option_c="42", option_d="210",
            correct_option="b",
            explanation_ar="C(7,3) = 7!  /  (3!  x  4!) = (7 x 6 x 5)  /  (3 x 2 x 1) = 210  /  6 = 35\n\nWhy other options are wrong:\n  • 21 ← Incorrect calculation\n  • 42 ← Wrong formula\n  • 210 ← Permutation P(7,3)",
            solution_steps_ar='["C(7,3) = 7!  /  (3!  x  4!)","= (7  x  6  x  5)  /  6","= 210  /  6 = 35"]',
    tags="combination,counting", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q134 — geometric probability
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.5,
            text_ar="Target circle radius 20 cm, with center circle radius 4 cm.\nWhat is P(hitting center circle)?",
            option_a="^1⁄₅", option_b="^1⁄₁₀", option_c="1/25", option_d="^1⁄₂₀",
            correct_option="c",
            explanation_ar="Target area = pi  x  20^2 = 400pi\nCenter area = pi  x  4^2 = 16pi\nP = 16pi  /  400pi = 16  /  400 = 1/25\n\nWhy other options are wrong:\n  • ^1⁄₅ ← Radius ratio\n  • ^1⁄₁₀ ← Linear ratio squared wrong\n  • ^1⁄₂₀ ← Incorrect calculation",
            solution_steps_ar='["Large area = pi  x  400","Small area = pi  x  16","P = 16  /  400 = 1/25"]',
    tags="probability,counting", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q135 — variance calculation
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.5,
            text_ar="Data: 1, 3, 5\nWhat is the variance?",
            option_a="^2⁄₃", option_b="^4⁄₃", option_c="^8⁄₃", option_d="4",
            correct_option="c",
            explanation_ar="Mean = (1+3+5)  /  3 = 3\nSquared deviations: (1−3)^2=4, (3−3)^2=0, (5−3)^2=4\nVariance = (4+0+4)  /  3 = ^8⁄₃\n\nWhy other options are wrong:\n  • ^2⁄₃ ← Not squaring deviations\n  • ^4⁄₃ ← SD value\n  • 4 ← Sum without dividing",
            solution_steps_ar='["Mean = 9  /  3 = 3","Squared deviations: 4, 0, 4","Variance = 8  /  3 = ^8⁄₃"]',
    tags="variance,standard-deviation", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q136 — survey: proportional reasoning
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.5,
            text_ar="Sample of 500 from city of 100,000.\nIf 120 in sample prefer a product, how many expected in city?",
            option_a="12,000", option_b="20,000", option_c="24,000", option_d="30,000",
            correct_option="c",
            explanation_ar="Proportion in sample = 120  /  500 = 0.24\nExpected in city = 0.24  x  100,000 = 24,000\n\nWhy other options are wrong:\n  • 12,000 ← Wrong proportion\n  • 20,000 ← Incorrect calculation\n  • 30,000 ← Wrong percentage",
            solution_steps_ar='["Proportion = 120  /  500 = 0.24","Expected = 0.24  x  100,000","= 24,000"]',
    tags="data-interpretation,frequency", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q137 — pigeonhole principle (birthdays)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.5,
            text_ar="What is minimum students needed to guarantee two share a birth month?",
            option_a="12", option_b="13", option_c="24", option_d="25",
            correct_option="b",
            explanation_ar="Months = 12\nPigeonhole: Worst case = one student per month (12 students)\n13th student must share a month\n\nWhy other options are wrong:\n  • 12 ← Could all be different\n  • 24 ← Twice needed\n  • 25 ← Excess",
            solution_steps_ar='["Holes (months) = 12","Worst case: 12 students in 12 different months","Student 13 must share a month -> Answer = 13"]',
    tags="counting,probability", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q138 — expected value with multiple outcomes
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.5,
            text_ar="Contest: 10% win $500, 20% win $100, 70% win nothing.\nWhat is expected winnings?",
            option_a="50", option_b="70", option_c="90", option_d="100",
            correct_option="b",
            explanation_ar="EV = 500  x  0.1 + 100  x  0.2 + 0  x  0.7\n= 50 + 20 + 0 = 70\n\nWhy other options are wrong:\n  • 50 ← Only first prize\n  • 90 ← Wrong calculation\n  • 100 ← Simple average",
            solution_steps_ar='["500  x  0.1 = 50","100  x  0.2 = 20","0  x  0.7 = 0","Total = 70"]',
    tags="probability,mean", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q139 — stem-and-leaf: range and mode
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.5,
            text_ar="Stem-and-leaf:\nStem | Leaf\n  1   | 2, 5, 5, 8\n  2   | 0, 3, 3, 3, 7\n  3   | 1\nWhat is the mode?",
            option_a="15", option_b="20", option_c="23", option_d="27",
            correct_option="c",
            explanation_ar="Data: 12, 15, 15, 18, 20, 23, 23, 23, 27, 31\nFrequencies: 15 appears 2 times, 23 appears 3 times\nMode = 23\n\nWhy other options are wrong:\n  • 15 ← Also frequent but not most\n  • 20 ← Wrong value\n  • 27 ← Maximum",
            solution_steps_ar='["Read data: 12,15,15,18,20,23,23,23,27,31","15: 2 times, 23: 3 times","Mode = 23"]',
    tags="mode,data-interpretation", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Difficulty 0.6 (12 questions) ──

        # Q140 — percentile from cumulative frequency
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.6,
            text_ar="Cumulative frequency for 50 students:\nLess than 40: 5 | Less than 50: 15 | Less than 60: 30 | Less than 70: 42 | Less than 80: 50\nWhat score is at 60th percentile?",
            option_a="50", option_b="55", option_c="60", option_d="65",
            correct_option="c",
            explanation_ar="60th percentile -> rank = 0.6  x  50 = 30\nCumulative 30 corresponds to (less than 60)\n60th percentile score ~ 60\n\nWhy other options are wrong:\n  • 50 ← Wrong percentile\n  • 55 ← Interpolating unnecessarily\n  • 65 ← Wrong percentile",
            solution_steps_ar='["Rank = 0.6  x  50 = 30","From table: cumulative 30 at (less than 60)","60th percentile ~ 60"]',
    tags="percentile,frequency,data-interpretation", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q141 — box plot comparison
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.6,
            text_ar="Two box plots for two classes:\nClass A: Q1=50, Q2=65, Q3=80\nClass B: Q1=55, Q2=70, Q3=75\nWhich class has greater spread (IQR)?",
            option_a="Class A", option_b="Class B", option_c="Equal", option_d="Cannot determine",
            correct_option="a",
            explanation_ar="IQR(A) = 80 − 50 = 30\nIQR(B) = 75 − 55 = 20\n30 > 20 -> Class A has greater spread\n\nWhy other options are wrong:\n  • Class B ← Smaller IQR\n  • Equal ← Different IQRs\n  • Cannot determine ← Can be determined",
            solution_steps_ar='["IQR(A) = 80 − 50 = 30","IQR(B) = 75 − 55 = 20","30 > 20 -> Class A more spread"]',
    tags="box-plot,percentile,variance", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q142 — frequency: missing value
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.6,
            text_ar="Frequency table for absent days:\nDays: 0 | 1 | 2 | 3 | 4\nFreq: 8 | 12 | x | 5 | 3\nIf total students = 40, what is x?",
            option_a="10", option_b="12", option_c="14", option_d="15",
            correct_option="b",
            explanation_ar="Sum of frequencies = total\n8 + 12 + x + 5 + 3 = 40\n28 + x = 40\nx = 12\n\nWhy other options are wrong:\n  • 10 ← Wrong calculation\n  • 14 ← Adding error\n  • 15 ← Incorrect total",
            solution_steps_ar='["Sum of frequencies = 40","8 + 12 + x + 5 + 3 = 40","28 + x = 40","x = 12"]',
    tags="frequency,mean", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q143 — conditional probability with table
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.6,
            text_ar="Contingency table:\n         Pass  Fail  Total\nMale     40    10     50\nFemale   35    15     50\nTotal    75    25    100\nIf a student is randomly chosen from those who passed, what is P(Male)?",
            option_a="8/15", option_b="7/15", option_c="2/5", option_d="1/2",
            correct_option="a",
            explanation_ar="Number who passed = 75\nNumber of males who passed = 40\nP = 40  /  75 = 8/15\n\nWhy other options are wrong:\n  • 7/15 ← Females passed\n  • 2/5 ← Wrong base\n  • 1/2 ← Overall male proportion",
            solution_steps_ar='["Passed = 75 students","Males passed = 40","P = 40  /  75 = 8/15"]',
    tags="conditional-probability,data-interpretation", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q144 — permutation with restriction
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.6,
            text_ar="How many 3-digit numbers from {1,2,3,4,5} without repetition, where first digit is odd?",
            option_a="24", option_b="36", option_c="48", option_d="60",
            correct_option="b",
            explanation_ar="Odd digits: 1, 3, 5 -> 3 choices for first position\nSecond digit: 4 remaining choices\nThird digit: 3 choices\nTotal = 3  x  4  x  3 = 36\n\nWhy other options are wrong:\n  • 24 ← No restriction\n  • 48 ← Wrong calculation\n  • 60 ← With repetition",
            solution_steps_ar='["First digit (odd): 3 choices","Second digit: 4 choices","Third digit: 3 choices","Total = 3  x  4  x  3 = 36"]',
    tags="permutation,counting", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q145 — dependent events (cards)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.6,
            text_ar="From 52-card deck, two cards drawn without replacement.\nWhat is P(both are Spades ♠)?",
            option_a="1/17", option_b="1/16", option_c="3/51", option_d="1/13",
            correct_option="a",
            explanation_ar="P(first ♠) = 13/52 = 1/4\nP(second ♠ | first ♠) = 12/51 = ^4⁄₁₇\nP(both ♠) = 1/4  x  ^4⁄₁₇ = 4/68 = 1/17\n\nWhy other options are wrong:\n  • 1/16 ← With replacement error\n  • 3/51 ← Wrong calculation\n  • 1/13 ← Single draw probability",
            solution_steps_ar='["P(first ♠) = 13/52 = 1/4","P(second ♠) = 12/51 = ^4⁄₁₇","P = 1/4  x  ^4⁄₁₇ = 1/17"]',
    tags="probability,conditional-probability", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q146 — interquartile range with even count
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.6,
            text_ar="Data: 4, 7, 10, 12, 15, 18, 20, 24, 27, 30\nWhat is IQR?",
            option_a="13", option_b="14", option_c="15", option_d="17",
            correct_option="b",
            explanation_ar="Number of values = 10\nLower half: 4, 7, 10, 12, 15 -> Q1 = 10\nUpper half: 18, 20, 24, 27, 30 -> Q3 = 24\nIQR = Q3 − Q1 = 24 − 10 = 14\n\nWhy other options are wrong:\n  • 13 ← Wrong Q1 or Q3\n  • 15 ← Approximation\n  • 17 ← Wrong calculation",
            solution_steps_ar='["Lower half: 4, 7, 10, 12, 15 -> Q1 = 10","Upper half: 18, 20, 24, 27, 30 -> Q3 = 24","IQR = 24 − 10 = 14"]',
    tags="percentile,box-plot", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q147 — combination with constraint
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.6,
            text_ar="From 8 students including Ahmad and Sara, how many ways to choose a committee of 3 that includes Ahmad but excludes Sara?",
            option_a="10", option_b="15", option_c="20", option_d="35",
            correct_option="b",
            explanation_ar="Ahmad is on committee -> choose 2 from remaining 6 (excluding Sara)\nC(6,2) = (6  x  5)  /  2 = 15\n\nWhy other options are wrong:\n  • 10 ← Wrong calculation\n  • 20 ← Not excluding Sara\n  • 35 ← No constraint applied",
            solution_steps_ar='["Ahmad on committee -> choose 2 from remaining 6","C(6,2) = (6 x 5) / 2 = 15"]',
    tags="combination,counting", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q148 — expected value: game decision
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.6,
            text_ar="A game costs 10 riyals to play:\n- 1/4 probability of winning 20 riyals\n- 1/4 probability of winning 10 riyals\n- 1/2 probability of winning nothing\nIs the game fair?",
            option_a="Yes, expected gain of 5 riyals", option_b="No, expected loss of 5 riyals",
            option_c="No, expected loss of 2.50 riyals", option_d="Fair game",
            correct_option="c",
            explanation_ar="Net outcomes:\n- Win 20: net = 20 - 10 = +10 (prob 1/4)\n- Win 10: net = 10 - 10 = 0 (prob 1/4)\n- No win: net = -10 (prob 1/2)\nEV = 10 x 1/4 + 0 x 1/4 + (-10) x 1/2 = 2.5 - 5 = -2.5\nExpected loss of 2.50 riyals\n\nWhy other options are wrong:\n• Yes, expected gain of 5: Wrong calculation of expected value\n• No, expected loss of 5: Incorrect probability weighting\n• Fair game: EV is not zero, so the game is not fair",
            solution_steps_ar='["Net outcomes: +10, 0, or -10 riyals","EV = 10 x 1/4 + 0 x 1/4 + (-10) x 1/2","= 2.5 + 0 - 5 = -2.5","Expected loss of 2.50 riyals"]',
    tags="probability,mean", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q149 — variance with frequency
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.6,
            text_ar="Data: 2 (freq 3), 5 (freq 4), 8 (freq 3)\nWhat is the mean?",
            option_a="4.5", option_b="5", option_c="5.2", option_d="4.8",
            correct_option="b",
            explanation_ar="Sum = 2 x 3 + 5 x 4 + 8 x 3 = 6 + 20 + 24 = 50\nCount = 3 + 4 + 3 = 10\nMean = 50  /  10 = 5\n\nWhy other options are wrong:\n  • 4.5 ← Wrong calculation\n  • 5.2 ← Incorrect sum\n  • 4.8 ← Confusing with another value",
            solution_steps_ar='["Sum = 6 + 20 + 24 = 50","Count = 10","Mean = 50  /  10 = 5"]',
    tags="mean,frequency,variance", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q150 — geometric probability (ring)
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.6,
            text_ar="Target has 3 concentric circles radii 1, 2, 3 cm.\nWhat is P(hitting region between first and second circle)?",
            option_a="1/9", option_b="1/3", option_c="^4⁄₉", option_d="5/6",
            correct_option="b",
            explanation_ar="Ring area = pi x 2^2 − pi x 1^2 = 4pi − pi = 3pi\nTotal area = pi x 3^2 = 9pi\nP = 3pi  /  9pi = 1/3\n\nWhy other options are wrong:\n  • 1/9 ← Inner circle ratio\n  • ^4⁄₉ ← Wrong region\n  • 5/6 ← Incorrect calculation",
            solution_steps_ar='["Ring area = pi(4−1) = 3pi","Total = 9pi","P = 3pi  /  9pi = 1/3"]',
    tags="probability,counting", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q151 — survey bias question
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.6,
            text_ar="Researcher surveys Twitter followers about city opinion.\nWhat is the main problem with this sample?",
            option_a="Sample size small", option_b="Sample not random (selection bias)",
            option_c="Questions unclear", option_d="Topic unimportant",
            correct_option="b",
            explanation_ar="Twitter followers dont represent all city residents.\nThis is convenience sampling, not random, causing selection bias.\n\nWhy other options are wrong:\n  • Sample size small ← Not the main issue\n  • Questions unclear ← Not mentioned\n  • Topic unimportant ← Irrelevant",
            solution_steps_ar='["Followers dont represent whole population","Sample is convenient not random","Result: selection bias"]',
    tags="data-interpretation,frequency", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ── Difficulty 0.7 (10 questions) ──

        # Q152 — percentile interpolation
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.7,
            text_ar="Test with 100 students. Score distribution:\n40-49: 10 students | 50-59: 25 | 60-69: 30 | 70-79: 20 | 80-89: 15\nHow many scored below 75th percentile?",
            option_a="65", option_b="75", option_c="80", option_d="85",
            correct_option="b",
            explanation_ar="75th percentile means 75% of students below.\nNumber = 75%  x  100 = 75 students\n\nWhy other options are wrong:\n  • 65 ← Wrong percentile\n  • 80 ← Wrong calculation\n  • 85 ← Wrong percentile",
            solution_steps_ar='["75th percentile = 75% below","Number = 75%  x  100 = 75 students"]',
    tags="percentile,frequency", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # Q153 — box plot: skewness
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.7,
            text_ar="Box plot:\nMin = 10, Q1 = 25, Q2 = 45, Q3 = 55, Max = 60\nWhat is the skewness type?",
            option_a="Right skewed (positive)", option_b="Left skewed (negative)",
            option_c="Symmetric", option_d="Cannot determine",
            correct_option="b",
            explanation_ar="Q2 − Q1 = 45 − 25 = 20\nQ3 − Q2 = 55 − 45 = 10\nLeft tail longer (Q2−Q1 > Q3−Q2) -> Negative (left) skew\n\nWhy other options are wrong:\n  • Right skewed ← Opposite\n  • Symmetric ← Unequal distances\n  • Cannot determine ← Can be determined",
            solution_steps_ar='["Q2 − Q1 = 20 (left side of box)","Q3 − Q2 = 10 (right side)","Left side longer -> Negative (left) skew"]',
    tags="box-plot,data-interpretation", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # Q154 — standard deviation effect of transformation
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.7,
            text_ar="If SD = 4, and 10 is added to each value then multiplied by 3.\nWhat is new SD?",
            option_a="4", option_b="12", option_c="14", option_d="22",
            correct_option="b",
            explanation_ar="Adding constant does not change SD -> still 4\nMultiplying by 3 multiplies SD by 3 -> 4  x  3 = 12\n\nWhy other options are wrong:\n  • 4 ← Forgot multiplication effect\n  • 14 ← Adding instead of multiplying\n  • 22 ← Wrong calculation",
            solution_steps_ar='["Adding constant does not affect SD","Multiplying by constant multiplies SD by same","New SD = 4  x  3 = 12"]',
    tags="standard-deviation,variance", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # Q155 — factorial arrangement with identical items
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.7,
            text_ar="How many arrangements of letters in \"mama\" (m,a,m,a)?",
            option_a="4", option_b="6", option_c="12", option_d="24",
            correct_option="b",
            explanation_ar="Letters = 4\nm repeats 2 times, a repeats 2 times\nArrangements = 4!  /  (2!  x  2!) = 24  /  4 = 6\n\nWhy other options are wrong:\n  • 4 ← Wrong formula\n  • 12 ← Only one repeat counted\n  • 24 ← No adjustment for repeats",
            solution_steps_ar='["4! = 24","m repeats 2! = 2, a repeats 2! = 2","Arrangements = 24  /  (2  x  2) = 6"]',
    tags="permutation,counting", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # Q156 — pigeonhole advanced
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.7,
            text_ar="Box has 50 balls numbered 1 to 50.\nWhat is minimum balls to draw to guarantee two sum to 51?",
            option_a="25", option_b="26", option_c="27", option_d="51",
            correct_option="b",
            explanation_ar="Pairs summing to 51: (1,50), (2,49)...(25,26) = 25 pairs\nWorst case: draw one from each pair = 25 balls\n26th ball completes a pair\nAnswer = 26\n\nWhy other options are wrong:\n  • 25 ← Could be one from each pair\n  • 27 ← More than needed\n  • 51 ← All balls",
            solution_steps_ar='["Pairs: (1,50), (2,49), ..., (25,26) = 25 pairs","Worst case: 25 balls with no complete pair","26th ball completes a pair","Answer = 26"]',
    tags="counting,probability", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # Q157 — conditional probability: medical test
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.7,
            text_ar="Medical test: 95% accurate (detects disease if present 95% of time).\nDisease prevalence is 1%.\nIf a person tests positive, what is P(actually has disease)?\n(False positive rate is 5% for healthy people)",
            option_a="16%", option_b="50%", option_c="95%", option_d="1%",
            correct_option="a",
            explanation_ar="P(disease) = 0.01, P(healthy) = 0.99\nP(positive|disease) = 0.95\nP(positive|healthy) = 0.05\nP(positive) = 0.01 x 0.95 + 0.99 x 0.05 = 0.0095 + 0.0495 = 0.059\nP(disease|positive) = 0.0095  /  0.059 ~ 0.16 = 16%\n\nWhy other options are wrong:\n  • 50% ← Incorrect calculation\n  • 95% ← Test accuracy\n  • 1% ← Prevalence",
            solution_steps_ar='["P(positive) = 0.01 x 0.95 + 0.99 x 0.05 = 0.059","P(disease|positive) = 0.0095  /  0.059","~ 0.16 = 16%"]',
    tags="conditional-probability,probability", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # Q158 — frequency: median from grouped data
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.7,
            text_ar="Frequency table:\nClass 10-19: freq 4 | 20-29: freq 6 | 30-39: freq 10 | 40-49: freq 5 | 50-59: freq 5\nWhich class contains the median?",
            option_a="20-29", option_b="30-39", option_c="40-49", option_d="10-19",
            correct_option="b",
            explanation_ar="Total = 4+6+10+5+5 = 30\nMedian positions = 15 and 16\nCumulative: 4, 10, 20, 25, 30\nPositions 15, 16 fall in class 30-39 (cumulative 20)\n\nWhy other options are wrong:\n  • 20-29 ← Before median\n  • 40-49 ← After median\n  • 10-19 ← First class",
            solution_steps_ar='["Total = 30 -> Median between positions 15 and 16","Cumulative: 4, 10, 20, 25, 30","Positions 15, 16 in class 30-39"]',
    tags="median,frequency", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # Q159 — stem-and-leaf: back-to-back
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.7,
            text_ar="Back-to-back stem-and-leaf for two classes:\nClass A | Stem | Class B\n  8 5 2 |   4   | 1 3 7\n  9 6 3 |   5   | 0 4 8\n    7 1 |   6   | 2 5\nWhat is the difference between the medians?",
            option_a="3", option_b="5", option_c="7", option_d="10",
            correct_option="a",
            explanation_ar="Class A: 42,45,48,53,56,59,61,67 -> 8 values\nMedian A = (53+56)  /  2 = 54.5\nClass B: 41,43,47,50,54,58,62,65 -> 8 values\nMedian B = (50+54)  /  2 = 52\nDifference = 54.5 − 52 = 2.5 ~ 3\n\nWhy other options are wrong:\n  • 5 ← Approximation error\n  • 7 ← Wrong calculation\n  • 10 ← Range error",
            solution_steps_ar='["Class A sorted: 42,45,48,53,56,59,61,67","Median A = (53+56) / 2 = 54.5","Class B sorted: 41,43,47,50,54,58,62,65","Median B = (50+54) / 2 = 52","Difference ~ 3"]',
    tags="median,data-interpretation", stage="building",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # Q160 — sampling method identification
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.7,
            text_ar="School has 1000 students in 20 classes.\nResearcher randomly chooses 5 classes and surveys all students in them.\nWhat sampling method?",
            option_a="Simple random", option_b="Stratified", option_c="Cluster", option_d="Systematic",
            correct_option="c",
            explanation_ar="Selecting entire groups (classes) randomly then surveying all members = Cluster sampling\n\nWhy other options are wrong:\n  • Simple random ← Not individual selection\n  • Stratified ← Would sample from each group\n  • Systematic ← Fixed interval selection",
            solution_steps_ar='["Selected classes (groups) entirely","Surveyed all students in chosen classes","This is cluster sampling"]',
    tags="data-interpretation,frequency", stage="building",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # Q161 — combination: committee with roles
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.7,
            text_ar="From 6 people, how many ways to choose President, VP, and Secretary?",
            option_a="20", option_b="60", option_c="120", option_d="720",
            correct_option="c",
            explanation_ar="Order matters (different positions):\nP(6,3) = 6  x  5  x  4 = 120\n\nWhy other options are wrong:\n  • 20 ← Combinations C(6,3)\n  • 60 ← Wrong calculation\n  • 720 ← 6! without selection",
            solution_steps_ar='["President: 6 choices","VP: 5 choices","Secretary: 4 choices","Total = 6  x  5  x  4 = 120"]',
    tags="permutation,counting", stage="building",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # ── Difficulty 0.8 (6 questions) ──

        # Q162 — percentile + box plot advanced
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.8,
            text_ar="Box plot: Min = 12, Q1 = 24, Q2 = 36, Q3 = 48, Max = 75\nIs 75 an outlier?",
            option_a="Yes, exceeds Q3 + 1.5 x IQR", option_b="No, less than Q3 + 1.5 x IQR",
            option_c="Yes, far from median", option_d="Cannot determine",
            correct_option="b",
            explanation_ar="IQR = Q3 − Q1 = 48 − 24 = 24\nUpper bound = Q3 + 1.5  x  24 = 48 + 36 = 84\n75 < 84 -> Not an outlier\n\nWhy other options are wrong:\n  • Yes, exceeds... ← 75 < 84\n  • Yes, far from median ← Distance not criterion\n  • Cannot determine ← Can be determined",
            solution_steps_ar='["IQR = 48 − 24 = 24","Upper bound = 48 + 1.5  x  24 = 84","75 < 84 -> Not outlier"]',
    tags="box-plot,percentile", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # Q163 — geometric probability advanced
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.8,
            text_ar="Equilateral triangle side 6 cm, contains equilateral triangle side 2 cm.\nIf random point chosen in large triangle, what is P(in small triangle)?",
            option_a="1/3", option_b="1/4", option_c="1/6", option_d="1/9",
            correct_option="d",
            explanation_ar="Area of equilateral triangle = (sqrt3/4)  x  side^2\nLarge area = (sqrt3/4)  x  36\nSmall area = (sqrt3/4)  x  4\nP = 4  /  36 = 1/9\n\nWhy other options are wrong:\n  • 1/3 ← Side ratio\n  • 1/4 ← Wrong formula\n  • 1/6 ← Incorrect calculation",
            solution_steps_ar='["Large area = (sqrt3/4)  x  36","Small area = (sqrt3/4)  x  4","P = 4  /  36 = 1/9"]',
    tags="probability,counting", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        # Q164 — expected value with penalty
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.8,
            text_ar="Test: 20 questions, correct +4, wrong −1, blank 0.\nStudent answers 15 randomly (4 choices each), leaves 5 blank.\nWhat is expected score?",
            option_a="11.25", option_b="15", option_c="3.75", option_d="0",
            correct_option="c",
            explanation_ar="Per question:\nP(correct) = 1/4 -> +4\nP(wrong) = 3/4 -> −1\nEV per question = 1/4 x 4 + 3/4 x (−1) = 1 − 0.75 = 0.25\nFor 15 questions = 15  x  0.25 = 3.75\nBlank = 5  x  0 = 0\nExpected score = 3.75\n\nWhy other options are wrong:\n  • 11.25 ← Wrong probabilities\n  • 15 ← All correct assumption\n  • 0 ← No penalty calculation",
            solution_steps_ar='["EV per question = 1/4 x (+4) + 3/4 x (−1) = 0.25","For 15 questions = 15  x  0.25 = 3.75","Blank = 0","Expected score = 3.75"]',
    tags="probability,mean", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        # Q165 — combination: distributing items
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.8,
            text_ar="How many ways to distribute 3 different prizes to 5 students (a student can win multiple prizes)?",
            option_a="60", option_b="125", option_c="150", option_d="243",
            correct_option="b",
            explanation_ar="Each prize has 5 choices (independent)\nTotal = 5  x  5  x  5 = 5^3 = 125\n\nWhy other options are wrong:\n  • 60 ← Permutation approach\n  • 150 ← Wrong calculation\n  • 243 ← 3^5 instead of 5^3",
            solution_steps_ar='["Prize 1: 5 choices","Prize 2: 5 choices","Prize 3: 5 choices","Total = 5^3 = 125"]',
    tags="counting,combination", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        # Q166 — variance of combined groups
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.8,
            text_ar="Group A: 3 values, mean 10, sum of squared deviations = 12\nGroup B: 2 values, mean 10, sum of squared deviations = 8\nWhat is variance of combined groups if combined mean = 10?",
            option_a="3", option_b="4", option_c="5", option_d="6",
            correct_option="b",
            explanation_ar="Since means are equal (= 10):\nTotal sum of squared deviations = 12 + 8 = 20\nTotal count = 3 + 2 = 5\nVariance = 20  /  5 = 4\n\nWhy other options are wrong:\n  • 3 ← Wrong calculation\n  • 5 ← SD value\n  • 6 ← Incorrect formula",
            solution_steps_ar='["Means equal -> no correction needed","Sum of squared deviations = 12 + 8 = 20","Total count = 5","Variance = 20  /  5 = 4"]',
    tags="variance,standard-deviation", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        # Q167 — pigeonhole principle advanced
        Question(skill_id="quant_statistics", question_type="statistics", difficulty=0.8,
            text_ar="At a party with 10 people, each person shakes hands with some number of others.\nProve two people shook hands with same number of people.\nWhat is maximum different handshakes possible for one person?",
            option_a="8", option_b="9", option_c="10", option_d="7",
            correct_option="b",
            explanation_ar="Each person can shake 0 to 9 hands -> 10 possible values\nBut cannot have both 0 and 9 (contradiction)\nActual values <= 9 cases for 10 people -> pigeonhole guarantees repeat\nMaximum for one person = 9 (shook hands with everyone)\n\nWhy other options are wrong:\n  • 8 ← Undercount\n  • 10 ← Including self\n  • 7 ← Wrong calculation",
            solution_steps_ar='["Possible values: 0,1,...,9 -> 10 values","But 0 and 9 cannot coexist -> 9 actual values","10 people in 9 holes -> repetition guaranteed","Maximum handshakes for one person = 9"]',
    tags="counting,probability", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),
    ]
