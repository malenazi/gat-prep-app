import json
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models import Question


def get_questions():
    return [

        # ══════════════════════════════════════════════════════════════
        # ██  Existing Questions (28 questions)  ██
        # ══════════════════════════════════════════════════════════════

        # ── Q1: Discount ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.2,
            text_ar="If the price of a book = 120 riyals, and you got a 25% discount, how much do you pay?",
            option_a="30 riyals", option_b="90 riyals", option_c="95 riyals", option_d="100 riyals",
            correct_option="b",
            explanation_ar="Given:\n  Price = 120 riyals\n  Discount rate = 25%\n\nSolution:\n  Discount value = 120 × 0.25 = 30 riyals\n  Amount paid = 120 − 30 = 90 riyals\n\nWhy other options are wrong:\n  • (a) 30 riyals: This is only the discount value, not the amount paid\n  • (c) 95 riyals: Result of calculating 20% discount instead of 25%\n  • (d) 100 riyals: Result of subtracting the percentage (25) instead of discount value (30)",
            solution_steps_ar='["Given: Price = 120 riyals, Discount = 25%","Discount value = 120 × 0.25 = 30 riyals","Amount paid = 120 − 30 = 90 riyals"]',
    tags="percentage,discount", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ── Q2: Ratio ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.3,
            text_ar="The ratio of boys to girls in a class = 3 : 2\nIf the total number of students = 35, how many girls are there?",
            option_a="10", option_b="14", option_c="20", option_d="21",
            correct_option="b",
            explanation_ar="Given:\n  Ratio: boys : girls = 3 : 2\n  Total number = 35\n\nSolution:\n  Sum of ratio parts = 3 + 2 = 5\n  Girls' share = (2 ÷ 5) × 35 = 14\n\nWhy other options are wrong:\n  • (a) 10: Result of dividing 35 ÷ 3.5 or error in ratio estimation\n  • (c) 20: Result of calculating girls' share as 35 − 15 with wrong estimation for boys\n  • (d) 21: Result of calculating boys' share (3 parts) instead of girls' (2 parts)",
            solution_steps_ar='["Given: Ratio 3 : 2, Total = 35","Sum of parts = 3 + 2 = 5","Number of girls = (2 ÷ 5) × 35 = 14"]',
    tags="ratio", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ── Q3: Fractions ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.4,
            text_ar="Ahmed walked ¾ of the distance to school.\nIf the total distance = 12 km, how much remains?",
            option_a="3 km", option_b="4 km", option_c="8 km", option_d="9 km",
            correct_option="a",
            explanation_ar="Given:\n  Total distance = 12 km\n  Fraction covered = ¾\n\nSolution:\n  Distance covered = ¾ × 12 = 9 km\n  Remaining = 12 − 9 = 3 km\n\nWhy other options are wrong:\n  • (b) 4 km: Result of calculating ¼ × 12 = 3 then confusing with 12 ÷ 3\n  • (c) 8 km: Result of calculating ⅔ × 12 instead of ¼ × 12\n  • (d) 9 km: This is the distance covered, not the remaining (forgot to subtract from total)",
            solution_steps_ar='["Distance covered = ¾ × 12 = 9 km","Remaining = 12 − 9 = 3 km"]',
    tags="fraction", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q4: Work Rate ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.5,
            text_ar="A worker completed ⅓ of the work in 4 hours.\nHow many hours does he need to complete the entire work?",
            option_a="8", option_b="10", option_c="12", option_d="16",
            correct_option="c",
            explanation_ar="Given:\n  Completed part = ⅓\n  Time = 4 hours\n\nSolution:\n  If ⅓ of work = 4 hours\n  Then full work (1) = 4 × 3 = 12 hours\n\nWhy other options are wrong:\n  • (a) 8: Result of doubling time (4 × 2) instead of multiplying by 3\n  • (b) 10: Wrong estimate not based on correct inverse relationship\n  • (d) 16: Result of multiplying 4 × 4 confusing denominator with multiplier",
            solution_steps_ar='["Given: ⅓ of work = 4 hours","Full work = 4 × 3 = 12 hours"]',
    tags="fraction,work-rate", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q5: Average ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.6,
            text_ar="The average score of 5 students = 80\nA sixth student joined with a score of 92\nWhat is the new average?",
            option_a="82", option_b="84", option_c="86", option_d="88",
            correct_option="a",
            explanation_ar="Given:\n  Original number of students = 5, Average = 80\n  New student: score = 92\n\nSolution:\n  Original total = 5 × 80 = 400\n  New total = 400 + 92 = 492\n  New average = 492 ÷ 6 = 82\n\nWhy other options are wrong:\n  • (b) 84: Result of calculating average of 80 and 92 directly without considering counts\n  • (c) 86: Result of calculating (80 + 92) ÷ 2 = 86 (average of only two values)\n  • (d) 88: Result of dividing by 5 instead of 6 after adding the student",
            solution_steps_ar='["Original total = number of students × average = 5 × 80 = 400","New total = 400 + 92 = 492","New average = 492 ÷ 6 = 82"]',
    tags="average", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q6: Speed ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.7,
            text_ar="A car travels a distance = 360 km in time = 4 hours.\nIf its speed increased by 30 km/h, how many hours does it need to cover the same distance?",
            option_a="2", option_b="3", option_c="4", option_d="5",
            correct_option="b",
            explanation_ar="Given:\n  Distance = 360 km, Time = 4 h\n  Speed increase = 30 km/h\n\nSolution:\n  Original speed = Distance ÷ Time = 360 ÷ 4 = 90 km/h\n  New speed = 90 + 30 = 120 km/h\n  New time = Distance ÷ Speed = 360 ÷ 120 = 3 hours\n\nWhy other options are wrong:\n  • (a) 2: Result of dividing 360 ÷ 180 incorrectly doubling the speed\n  • (c) 4: This is the original time before speed increase\n  • (d) 5: Result of using original speed minus 30 instead of increase",
            solution_steps_ar='["Original speed = 360 ÷ 4 = 90 km/h","New speed = 90 + 30 = 120 km/h","Time = 360 ÷ 120 = 3 hours"]',
    tags="speed", stage="foundation",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # ── Q7: Comparison — Percentages ──
        Question(skill_id="quant_arithmetic", question_type="comparison", difficulty=0.5,
            text_ar="Compare:\n\n▸ Column (A): 25% of 200\n▸ Column (B): 50% of 100",
            option_a="Column (A) is greater", option_b="Column (B) is greater", option_c="The two values are equal", option_d="The relationship cannot be determined",
            correct_option="c",
            explanation_ar="Calculate each column:\n  Column (A) = 200 × 0.25 = 50\n  Column (B) = 100 × 0.5 = 50\n\n∴ The two values are equal (50 = 50)\n\nWhy other options are wrong:\n  • (a) Column (A) is greater: Wrong because both values = 50\n  • (b) Column (B) is greater: Wrong because 50 = 50\n  • (d) Cannot be determined: Can be determined because values are fixed and calculable",
            solution_steps_ar='["Column (A) = 200 × 0.25 = 50","Column (B) = 100 × 0.5 = 50","50 = 50 ∴ The two values are equal"]',
    tags="comparison,percentage", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ── Q8: Comparison — Roots ──
        Question(skill_id="quant_arithmetic", question_type="comparison", difficulty=0.6,
            text_ar="Compare:\n\n▸ Column (A): ∛27 (cube root of 27)\n▸ Column (B): √9 (square root of 9)",
            option_a="Column (A) is greater", option_b="Column (B) is greater", option_c="The two values are equal", option_d="The relationship cannot be determined",
            correct_option="c",
            explanation_ar="Calculate each column:\n  Column (A): ∛27 = 3 (because 3 × 3 × 3 = 27)\n  Column (B): √9 = 3 (because 3 × 3 = 9)\n\n∴ The two values are equal (3 = 3)\n\nWhy other options are wrong:\n  • (a) Column (A) is greater: Wrong because ∛27 = 3 = √9\n  • (b) Column (B) is greater: Wrong for the same reason\n  • (d) Cannot be determined: Both values can be calculated precisely",
            solution_steps_ar='["Column (A) = ∛27 = 3","Column (B) = √9 = 3","3 = 3 ∴ The two values are equal"]',
    tags="comparison,profit", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q9: Simple Multiplication ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.2,
            text_ar="Khaled bought 5 notebooks, price of each notebook = 8 riyals.\nWhat is the total amount?",
            option_a="13 riyals", option_b="40 riyals", option_c="35 riyals", option_d="45 riyals",
            correct_option="b",
            explanation_ar="Given:\n  Number of notebooks = 5\n  Price per notebook = 8 riyals\n\nSolution:\n  Total amount = 5 × 8 = 40 riyals\n\nWhy other options are wrong:\n  • (a) 13 riyals: Result of addition (5 + 8) instead of multiplication\n  • (c) 35 riyals: Result of multiplying 5 × 7 (error in notebook price)\n  • (d) 45 riyals: Result of multiplying 5 × 9 (error in notebook price)",
            solution_steps_ar='["Given: Number of notebooks = 5, Price per notebook = 8 riyals","Total amount = 5 × 8 = 40 riyals"]',
    tags="ratio", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ── Q10: Percentage ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.3,
            text_ar="Which of the following values equals 20% of 150?",
            option_a="15", option_b="20", option_c="30", option_d="35",
            correct_option="c",
            explanation_ar="Given:\n  Percentage = 20%\n  Number = 150\n\nSolution:\n  20% of 150 = 150 × 0.20 = 30\n\nWhy other options are wrong:\n  • (a) 15: Result of calculating 10% of 150 instead of 20%\n  • (b) 20: Confusing between percentage (20) and calculated value\n  • (d) 35: Result of calculating 150 × 0.25 approximately (error in percentage)",
            solution_steps_ar='["Given: Percentage = 20%, Number = 150","20% of 150 = 150 × 0.20 = 30"]',
    tags="percentage", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ── Q11: Fraction Conversion ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.3,
            text_ar="The fraction ⅗ equals what percentage?",
            option_a="35%", option_b="53%", option_c="60%", option_d="75%",
            correct_option="c",
            explanation_ar="Given:\n  Fraction = ⅗\n\nSolution:\n  ⅗ = 3 ÷ 5 = 0.6\n  0.6 × 100 = 60%\n\nWhy other options are wrong:\n  • (a) 35%: Result of writing numerator and denominator as number (35) instead of division\n  • (b) 53%: Result of reversing numerator and denominator (5/3) and writing as number\n  • (d) 75%: Result of confusing with fraction ¾ instead of ⅗",
            solution_steps_ar='["Fraction = ⅗","Divide: 3 ÷ 5 = 0.6","Multiply by 100: 0.6 × 100 = 60%"]',
    tags="percentage,fraction", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ── Q12: Profit ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.4,
            text_ar="A merchant bought goods for 400 riyals and sold them for 520 riyals.\nWhat is the profit percentage?",
            option_a="20%", option_b="25%", option_c="30%", option_d="35%",
            correct_option="c",
            explanation_ar="Given:\n  Purchase price = 400 riyals\n  Selling price = 520 riyals\n\nSolution:\n  Profit = 520 − 400 = 120 riyals\n  Profit percentage = (120 ÷ 400) × 100 = 30%\n\nWhy other options are wrong:\n  • (a) 20%: Result of calculating profit percentage from selling price (120 ÷ 600) incorrectly\n  • (b) 25%: Result of calculating (120 ÷ 480) or confusion in division\n  • (d) 35%: Result of calculating (140 ÷ 400) with error in finding profit",
            solution_steps_ar='["Profit = Selling price − Purchase price = 520 − 400 = 120 riyals","Profit percentage = (Profit ÷ Purchase price) × 100","= (120 ÷ 400) × 100 = 30%"]',
    tags="percentage,profit", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q13: Ratio and Proportion ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.5,
            text_ar="The ratio of water to juice in a mixture = 3 : 2\nIf the amount of water = 9 liters, what is the total quantity of the mixture?",
            option_a="12 liters", option_b="15 liters", option_c="18 liters", option_d="6 liters",
            correct_option="b",
            explanation_ar="Given:\n  Ratio: water : juice = 3 : 2\n  Water quantity = 9 liters\n\nSolution:\n  One part = 9 ÷ 3 = 3 liters\n  Juice quantity = 2 × 3 = 6 liters\n  Total quantity = 9 + 6 = 15 liters\n\nWhy other options are wrong:\n  • (a) 12 liters: Result of adding only 3 (one part) to water\n  • (c) 18 liters: Result of doubling water quantity (9 × 2) instead of calculating ratio\n  • (d) 6 liters: This is only the juice quantity, not the total mixture",
            solution_steps_ar='["One part = Water quantity ÷ Water parts = 9 ÷ 3 = 3 liters","Juice quantity = 2 × 3 = 6 liters","Total quantity = 9 + 6 = 15 liters"]',
    tags="ratio,mixture", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q14: Comparison — Fractions ──
        Question(skill_id="quant_arithmetic", question_type="comparison", difficulty=0.5,
            text_ar="Compare:\n\n▸ Column (A): ³⁄₈ + ¹⁄₈\n▸ Column (B): ½",
            option_a="Column (A) is greater", option_b="Column (B) is greater", option_c="The two values are equal", option_d="The relationship cannot be determined",
            correct_option="c",
            explanation_ar="Calculate each column:\n  Column (A) = ³⁄₈ + ¹⁄₈ = ⁴⁄₈ = ½\n  Column (B) = ½\n\n∴ The two values are equal (½ = ½)\n\nWhy other options are wrong:\n  • (a) Column (A) is greater: Wrong because ³⁄₈ + ¹⁄₈ = ⁴⁄₈ = ½ exactly\n  • (b) Column (B) is greater: Wrong for the same reason\n  • (d) Cannot be determined: Can calculate the addition and simplify fraction",
            solution_steps_ar='["Column (A) = ³⁄₈ + ¹⁄₈ = ⁴⁄₈ = ½","Column (B) = ½","½ = ½ ∴ The two values are equal"]',
    tags="comparison,fraction", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q15: Comparison — Average ──
        Question(skill_id="quant_arithmetic", question_type="comparison", difficulty=0.6,
            text_ar="Compare:\n\n▸ Column (A): Average of numbers 4, 6, 8, 10\n▸ Column (B): 7.5",
            option_a="Column (A) is greater", option_b="Column (B) is greater", option_c="The two values are equal", option_d="The relationship cannot be determined",
            correct_option="b",
            explanation_ar="Calculate each column:\n  Column (A): Sum = 4 + 6 + 8 + 10 = 28\n  Average = 28 ÷ 4 = 7\n  Column (B) = 7.5\n\n∴ 7 < 7.5 ← Column (B) is greater\n\nWhy other options are wrong:\n  • (a) Column (A) is greater: Wrong because 7 < 7.5\n  • (c) The two values are equal: Wrong because 7 ≠ 7.5\n  • (d) Cannot be determined: Can calculate average precisely",
            solution_steps_ar='["Column (A): Sum = 4 + 6 + 8 + 10 = 28","Average = 28 ÷ 4 = 7","Column (B) = 7.5 ← Column (B) is greater"]',
    tags="comparison,average", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q16: Train and Minutes ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.7,
            text_ar="A train travels at 90 km/h.\nHow many minutes does it need to cover 60 km?",
            option_a="30 minutes", option_b="40 minutes", option_c="45 minutes", option_d="50 minutes",
            correct_option="b",
            explanation_ar="Given:\n  Speed = 90 km/h\n  Distance = 60 km\n\nSolution:\n  Time = Distance ÷ Speed = 60 ÷ 90 = ⅔ hour\n  ⅔ hour = ⅔ × 60 = 40 minutes\n\nWhy other options are wrong:\n  • (a) 30 minutes: Result of calculating 60 ÷ 90 = ⅔ then multiplying ⅔ × 45 incorrectly\n  • (c) 45 minutes: Result of calculating ¾ hour instead of ⅔ hour\n  • (d) 50 minutes: Result of forgetting correct conversion from hours to minutes",
            solution_steps_ar='["Time = Distance ÷ Speed = 60 ÷ 90 = ⅔ hour","Convert to minutes: ⅔ × 60 = 40 minutes"]',
    tags="speed", stage="foundation",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # ── Q17: Increase and Discount ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.8,
            text_ar="The price of a product increased by 20% then decreased by 20%.\nIf the original price = 500 riyals, what is the final price?",
            option_a="450 riyals", option_b="480 riyals", option_c="500 riyals", option_d="520 riyals",
            correct_option="b",
            explanation_ar="Given:\n  Original price = 500 riyals\n  Increase 20% then decrease 20%\n\nSolution:\n  After increase = 500 × 1.20 = 600 riyals\n  After decrease = 600 × 0.80 = 480 riyals\n\nWhy other options are wrong:\n  • (a) 450 riyals: Result of subtracting 10% instead of calculating increase then decrease\n  • (c) 500 riyals: Wrong belief that 20% increase then 20% decrease returns original price\n  • (d) 520 riyals: Result of calculating increase only 500 + 20 = 520 without percentage",
            solution_steps_ar='["Price after increase = 500 × 1.20 = 600 riyals","Price after decrease = 600 × 0.80 = 480 riyals","Note: Increase and decrease by same percentage do not return original price"]',
    tags="percentage", stage="foundation",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # ── Q18: Workers ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.8,
            text_ar="6 workers can complete a project in 10 days.\nIf 2 workers leave after 4 days, how many additional days do the remaining workers need to finish the work?",
            option_a="6 days", option_b="8 days", option_c="9 days", option_d="10 days",
            correct_option="c",
            explanation_ar="Given:\n  6 workers → 10 days\n  After 4 days 2 left → 4 workers remain\n\nSolution:\n  Total work = 6 × 10 = 60 work units\n  Completed in 4 days = 6 × 4 = 24 units\n  Remaining = 60 − 24 = 36 units\n  Days needed = 36 ÷ 4 = 9 days\n\nWhy other options are wrong:\n  • (a) 6 days: Result of calculating 10 − 4 = 6 (remaining days without considering worker change)\n  • (b) 8 days: Result of calculating 36 ÷ 4 ≈ 8 with wrong approximation\n  • (d) 10 days: Original full time without considering what was completed",
            solution_steps_ar='["Total work = 6 workers × 10 days = 60 work units","Completed = 6 × 4 = 24 units","Remaining = 60 − 24 = 36 units","Additional days = 36 ÷ 4 workers = 9 days"]',
    tags="work-rate", stage="foundation",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        # ── Q19: Compound Interest ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.2,
            text_ar="Khaled deposited 10,000 riyals in a bank with compound interest of 10% annually for 2 years.\nWhat is the total amount after 2 years?",
            option_a="12,000 riyals", option_b="12,100 riyals", option_c="11,000 riyals", option_d="11,100 riyals",
            correct_option="b",
            explanation_ar="Given:\n  Principal = 10,000 riyals\n  Interest rate = 10% annually\n  Duration = 2 years\n\nSolution:\n  After Year 1 = 10,000 × 1.1 = 11,000\n  After Year 2 = 11,000 × 1.1 = 12,100 riyals\n\nWhy other options are wrong:\n  • (a) 12,000 riyals: This is simple interest (10,000 + 1,000 × 2), not compound\n  • (c) 11,000 riyals: Amount after one year only, not two\n  • (d) 11,100 riyals: Result of adding one year interest + 100 approximately",
            solution_steps_ar='["Given: Principal = 10,000, Interest = 10%, Duration = 2 years","After Year 1 = 10,000 × 1.1 = 11,000","After Year 2 = 11,000 × 1.1 = 12,100 riyals"]',
    tags="percentage,compound-interest", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # ── Q20: LCM ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.25,
            text_ar="What is the smallest number divisible by both 4 and 6?",
            option_a="8", option_b="12", option_c="24", option_d="36",
            correct_option="b",
            explanation_ar="Given:\n  Numbers: 4 and 6\n\nSolution:\n  4 = 2²\n  6 = 2 × 3\n  LCM = 2² × 3 = 12\n\nWhy other options are wrong:\n  • (a) 8: Divisible by 4 but not by 6\n  • (c) 24: Divisible by both but not the smallest (multiple of 12)\n  • (d) 36: Common multiple but not the smallest",
            solution_steps_ar='["Factorization: 4 = 2², 6 = 2 × 3","LCM = 2² × 3 = 4 × 3 = 12","So smallest common number = 12"]',
    tags="lcm-gcd", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ── Q21: Ages ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.3,
            text_ar="Ahmed's age now is twice his son's age.\nIf the son's age = 12 years, how old will Ahmed be after 5 years?",
            option_a="24", option_b="27", option_c="29", option_d="34",
            correct_option="c",
            explanation_ar="Given:\n  Son's age = 12 years\n  Father's age = 2 × Son's age\n\nSolution:\n  Father's current age = 2 × 12 = 24 years\n  After 5 years = 24 + 5 = 29 years\n\nWhy other options are wrong:\n  • (a) 24: This is father's current age, not after 5 years\n  • (b) 27: Result of adding 5 to son's age then doubling (12 + 5) × incorrect\n  • (d) 34: Result of multiplying 12 × 2 + 10 or error in addition",
            solution_steps_ar='["Father\'s current age = 2 × 12 = 24 years","After 5 years = 24 + 5 = 29 years"]',
    tags="age", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ── Q22: Mixing Solutions ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.45,
            text_ar="3 liters of juice with 20% concentration were mixed with 7 liters of juice with 40% concentration.\nWhat is the concentration of the resulting mixture?",
            option_a="28%", option_b="30%", option_c="34%", option_d="36%",
            correct_option="c",
            explanation_ar="Given:\n  Solution 1: 3 liters at 20% concentration\n  Solution 2: 7 liters at 40% concentration\n\nSolution:\n  Substance quantity = (3 × 0.2) + (7 × 0.4) = 0.6 + 2.8 = 3.4 liters\n  Total volume = 3 + 7 = 10 liters\n  Concentration = 3.4 ÷ 10 = 0.34 = 34%\n\nWhy other options are wrong:\n  • (a) 28%: Result of calculating (20 + 40) ÷ 2 − 2 with wrong estimate\n  • (b) 30%: Result of calculating arithmetic average (20 + 40) ÷ 2 without considering quantities\n  • (d) 36%: Result of adding extra weight to the more concentrated solution",
            solution_steps_ar='["Substance from Solution 1 = 3 × 0.2 = 0.6","Substance from Solution 2 = 7 × 0.4 = 2.8","Total = 0.6 + 2.8 = 3.4, Volume = 10","Concentration = 3.4 ÷ 10 = 34%"]',
    tags="percentage,mixture", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q23: Joint Work ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.5,
            text_ar="A worker can complete work in 6 days, and another worker can complete it in 12 days.\nIf they work together, how many days do they need to complete the work?",
            option_a="3 days", option_b="4 days", option_c="5 days", option_d="9 days",
            correct_option="b",
            explanation_ar="Given:\n  Worker 1: completes work in 6 days\n  Worker 2: completes work in 12 days\n\nSolution:\n  First worker's daily output = ¹⁄₆\n  Second worker's daily output = ¹⁄₁₂\n  Combined output = ¹⁄₆ + ¹⁄₁₂ = ²⁄₁₂ + ¹⁄₁₂ = ³⁄₁₂ = ¼\n  Time = 1 ÷ ¼ = 4 days\n\nWhy other options are wrong:\n  • (a) 3 days: Result of wrong estimate assuming work is done faster\n  • (c) 5 days: Result of calculating (6 + 12) ÷ 2 − 4 approximately\n  • (d) 9 days: Result of adding times 6 + 12 = 18 ÷ 2 = 9 instead of adding rates",
            solution_steps_ar='["First worker daily = ¹⁄₆, Second = ¹⁄₁₂","Combined = ¹⁄₆ + ¹⁄₁₂ = ³⁄₁₂ = ¼","Time = 1 ÷ ¼ = 4 days"]',
    tags="work-rate", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q24: Profit by Percentage ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.5,
            text_ar="A merchant bought goods for 800 riyals and sold them at 35% profit.\nWhat is the selling price?",
            option_a="920 riyals", option_b="1,000 riyals", option_c="1,080 riyals", option_d="1,120 riyals",
            correct_option="c",
            explanation_ar="Given:\n  Purchase price = 800 riyals\n  Profit percentage = 35%\n\nSolution:\n  Profit value = 800 × 0.35 = 280 riyals\n  Selling price = 800 + 280 = 1,080 riyals\n\nWhy other options are wrong:\n  • (a) 920 riyals: Result of calculating 15% profit instead of 35%\n  • (b) 1,000 riyals: Result of calculating 25% profit instead of 35%\n  • (d) 1,120 riyals: Result of calculating 40% profit instead of 35%",
            solution_steps_ar='["Profit value = 800 × 0.35 = 280 riyals","Selling price = 800 + 280 = 1,080 riyals"]',
    tags="percentage,profit", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q25: Currency Conversion ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.55,
            text_ar="If the exchange rate of dollar = 3.75 riyals.\nHow many riyals does a traveler need to buy 240 dollars?",
            option_a="750 riyals", option_b="840 riyals", option_c="900 riyals", option_d="64 riyals",
            correct_option="c",
            explanation_ar="Given:\n  Exchange rate = 1 dollar = 3.75 riyals\n  Required amount = 240 dollars\n\nSolution:\n  Amount in riyals = 240 × 3.75 = 900 riyals\n\nWhy other options are wrong:\n  • (a) 750 riyals: Result of multiplying 240 × 3 approximately (ignoring 0.75)\n  • (b) 840 riyals: Result of multiplying 240 × 3.5 instead of 3.75\n  • (d) 64 riyals: Result of dividing 240 ÷ 3.75 instead of multiplying",
            solution_steps_ar='["Given: 1 dollar = 3.75 riyals, Required = 240 dollars","Amount = 240 × 3.75 = 900 riyals"]',
    tags="currency", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q26: Train and Bridge ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.7,
            text_ar="A train 150 meters long travels at 72 km/h.\nHow many seconds does it need to cross a bridge 350 meters long?",
            option_a="18 seconds", option_b="20 seconds", option_c="25 seconds", option_d="30 seconds",
            correct_option="c",
            explanation_ar="Given:\n  Train length = 150 m, Bridge length = 350 m\n  Speed = 72 km/h\n\nSolution:\n  Total distance = 150 + 350 = 500 m\n  Speed in m/s = 72 × ¹⁰⁰⁰⁄₃₆₀₀ = 20 m/s\n  Time = 500 ÷ 20 = 25 seconds\n\nWhy other options are wrong:\n  • (a) 18 seconds: Result of calculating 350 ÷ 20 (forgot to add train length)\n  • (b) 20 seconds: Result of wrong speed conversion or forgetting part of distance\n  • (d) 30 seconds: Result of using distance 600 m or wrong speed",
            solution_steps_ar='["Total distance = train length + bridge length = 150 + 350 = 500 m","Convert speed: 72 km/h = 72 × (1000 ÷ 3600) = 20 m/s","Time = 500 ÷ 20 = 25 seconds"]',
    tags="speed", stage="foundation",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # ── Q27: GCD Application ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.75,
            text_ar="A farmer wanted to divide a rectangular field with dimensions 120 m × 84 m into equal largest possible square pieces.\nWhat is the side length of each square?",
            option_a="6 m", option_b="12 m", option_c="14 m", option_d="21 m",
            correct_option="b",
            explanation_ar="Given:\n  Dimensions: 120 m × 84 m\n\nSolution:\n  We need GCD (120, 84)\n  120 = 2³ × 3 × 5\n  84 = 2² × 3 × 7\n  GCD = 2² × 3 = 12\n  Side length = 12 m\n\nWhy other options are wrong:\n  • (a) 6 m: Common divisor but not the largest\n  • (c) 14 m: Divides 84 but not 120\n  • (d) 21 m: Divides 84 but not 120",
            solution_steps_ar='["Factorization: 120 = 2³ × 3 × 5, 84 = 2² × 3 × 7","GCD = 2² × 3 = 4 × 3 = 12","Largest square side length = 12 m"]',
    tags="ratio", stage="foundation",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # ── Q28: Compound Work ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.8,
            text_ar="5 workers can complete a project in 18 days working 8 hours daily.\nHow many workers are needed to complete the same project in 10 days working 6 hours daily?",
            option_a="9", option_b="10", option_c="12", option_d="15",
            correct_option="c",
            explanation_ar="Given:\n  Case 1: 5 workers × 18 days × 8 hours\n  Case 2: x workers × 10 days × 6 hours\n\nSolution:\n  Work amount is constant:\n  5 × 18 × 8 = x × 10 × 6\n  720 = 60x\n  x = 720 ÷ 60 = 12 workers\n\nWhy other options are wrong:\n  • (a) 9: Result of calculating 720 ÷ 80 (using 8 hours instead of 6)\n  • (b) 10: Result of calculating 720 ÷ 72 or error in multiplying days × hours\n  • (d) 15: Result of calculating 720 ÷ 48 (error in product 10 × 6)",
            solution_steps_ar='["Work amount = workers × days × hours","Case 1: 5 × 18 × 8 = 720 work units","Case 2: x × 10 × 6 = 60x","60x = 720 → x = 12 workers"]',
    tags="work-rate", stage="foundation",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        # ══════════════════════════════════════════════════════════════
        # ██  New Questions (83 questions) — from Q29 to Q111  ██
        # ══════════════════════════════════════════════════════════════

        # ════════════════════════════════════════
        # Difficulty 0.2 — Very Easy Arithmetic Questions
        # ════════════════════════════════════════

        # ── Q29 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.2,
            text_ar="If the price of 3 pens = 15 riyals, what is the price of one pen?",
            option_a="3 riyals", option_b="5 riyals", option_c="8 riyals", option_d="12 riyals",
            correct_option="b",
            explanation_ar="Given:\n  Price of 3 pens = 15 riyals\n\nSolution:\n  Price of one pen = 15 ÷ 3 = 5 riyals\n\nWhy other options are wrong:\n  • (a) 28: Result of division by wrong sum of parts\n  • (c) 36: Result of confusing larger and smaller part shares\n  • (d) 128: Result of multiplication instead of division or vice versa",
            solution_steps_ar='["Given: 3 pens = 15 riyals","Price per pen = 15 ÷ 3 = 5 riyals"]',
    tags="ratio", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # ── Q30 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.2,
            text_ar="What is the value of ½ of 64?",
            option_a="28", option_b="32", option_c="36", option_d="128",
            correct_option="b",
            explanation_ar="Solution:\n  ½ × 64 = 32\n\nWhy other options are wrong:\n  • (a) 70 riyals: Result of forgetting to unify denominators\n  • (c) 75 riyals: Result of calculating covered part instead of remaining or vice versa\n  • (d) 88 riyals: Result of error in multiplying or dividing fractions",
            solution_steps_ar='["½ × 64 = 64 ÷ 2 = 32"]',
    tags="fraction", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ── Q31 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.2,
            text_ar="Saad bought a shirt for 80 riyals and got a 10% discount.\nHow much did he pay?",
            option_a="70 riyals", option_b="72 riyals", option_c="75 riyals", option_d="88 riyals",
            correct_option="b",
            explanation_ar="Given:\n  Price = 80 riyals, Discount = 10%\n\nSolution:\n  Discount value = 80 × 0.1 = 8 riyals\n  Amount paid = 80 − 8 = 72 riyals\n\nWhy other options are wrong:\n  • (a) 6: Result of calculating percentage from wrong number\n  • (b) 7: Result of forgetting to subtract or add percentage to original number\n  • (d) 9: Result of confusing between percentage value and percentage itself",
            solution_steps_ar='["Discount value = 80 × 0.1 = 8 riyals","Amount paid = 80 − 8 = 72 riyals"]',
    tags="percentage,discount", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ── Q32 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.2,
            text_ar="If the number of apples in a basket = 48 apples, and they were distributed equally among 6 children.\nHow many apples does each child get?",
            option_a="6", option_b="7", option_c="8", option_d="9",
            correct_option="c",
            explanation_ar="Solution:\n  Apples per child = 48 ÷ 6 = 8 apples\n\nWhy other options are wrong:\n  • (a) 20: Result of division by wrong sum of parts\n  • (c) 40: Result of confusing larger and smaller part shares\n  • (d) 50: Result of multiplication instead of division or vice versa",
            solution_steps_ar='["Apples per child = 48 ÷ 6 = 8"]',
    tags="ratio", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ── Q33 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.2,
            text_ar="What is the value of ¼ of 100?",
            option_a="20", option_b="25", option_c="40", option_d="50",
            correct_option="b",
            explanation_ar="Solution:\n  ¼ × 100 = 100 ÷ 4 = 25\n\nWhy other options are wrong:\n  • (a) 24 riyals: Result of forgetting to unify denominators\n  • (c) 30 riyals: Result of calculating covered part instead of remaining or vice versa\n  • (d) 32 riyals: Result of error in multiplying or dividing fractions",
            solution_steps_ar='["¼ × 100 = 100 ÷ 4 = 25"]',
    tags="fraction", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ── Q34 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.2,
            text_ar="Price of 1 kg of rice = 7 riyals.\nHow much does one pay for buying 4 kilograms?",
            option_a="24 riyals", option_b="28 riyals", option_c="30 riyals", option_d="32 riyals",
            correct_option="b",
            explanation_ar="Solution:\n  Amount = 4 × 7 = 28 riyals\n\nWhy other options are wrong:\n  • (a) 24 riyals: Result of division by wrong sum of parts\n  • (c) 30 riyals: Result of confusing larger and smaller part shares\n  • (d) 32 riyals: Result of multiplication instead of division or vice versa",
            solution_steps_ar='["Amount = number of kg × price per kg = 4 × 7 = 28 riyals"]',
    tags="ratio", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.14),

        # ════════════════════════════════════════
        # Difficulty 0.3 — Easy Arithmetic Questions
        # ════════════════════════════════════════

        # ── Q35 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.3,
            text_ar="In a class of 40 students, the pass rate is 75%.\nHow many students passed?",
            option_a="25", option_b="30", option_c="32", option_d="35",
            correct_option="b",
            explanation_ar="Solution:\n  Number of passing students = 40 × 0.75 = 30 students\n\nWhy other options are wrong:\n  • (a) 15: Result of calculating percentage from wrong number\n  • (c) 25: Result of forgetting to subtract or add percentage to original number\n  • (d) 30: Result of confusing between percentage value and percentage itself",
            solution_steps_ar='["Number of passing students = 40 × 75% = 40 × 0.75 = 30"]',
    tags="percentage", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ── Q36 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.3,
            text_ar="What is the arithmetic mean of numbers: 10, 20, 30?",
            option_a="15", option_b="20", option_c="25", option_d="30",
            correct_option="b",
            explanation_ar="Solution:\n  Sum = 10 + 20 + 30 = 60\n  Average = 60 ÷ 3 = 20\n\nWhy other options are wrong:\n  • (a) 4: Result of division by wrong number of values\n  • (c) 10: Result of forgetting to add new value to sum\n  • (d) 16: Result of calculating sum without dividing by number of elements",
            solution_steps_ar='["Sum = 10 + 20 + 30 = 60","Average = 60 ÷ 3 = 20"]',
    tags="average", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ── Q37 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.3,
            text_ar="The ratio of males to females in an office = 4 : 1.\nIf the number of males is 20, how many females are there?",
            option_a="4", option_b="5", option_c="10", option_d="16",
            correct_option="b",
            explanation_ar="Given:\n  Ratio: males : females = 4 : 1\n  Number of males = 20\n\nSolution:\n  One part = 20 ÷ 4 = 5\n  Number of females = 1 × 5 = 5\n\nWhy other options are wrong:\n  • (a) 25%: Result of division by wrong sum of parts\n  • (b) 30%: Result of confusing larger and smaller part shares\n  • (d) 45%: Result of multiplication instead of division or vice versa",
            solution_steps_ar='["One part = 20 ÷ 4 = 5","Number of females = 1 × 5 = 5"]',
    tags="ratio", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q38 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.3,
            text_ar="Sami completed ⅖ of his project.\nWhat percentage did he complete?",
            option_a="25%", option_b="30%", option_c="40%", option_d="45%",
            correct_option="c",
            explanation_ar="Solution:\n  ⅖ = 2 ÷ 5 = 0.4\n  0.4 × 100 = 40%\n\nWhy other options are wrong:\n  • (a) 45 km/h: Result of calculating percentage from wrong number\n  • (b) 50 km/h: Result of forgetting to subtract or add percentage to original number\n  • (d) 90 km/h: Result of confusing between percentage value and percentage itself",
            solution_steps_ar='["⅖ = 2 ÷ 5 = 0.4","0.4 × 100 = 40%"]',
    tags="percentage,fraction,work-rate", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q39 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.3,
            text_ar="Majed traveled 180 km in 3 hours.\nWhat is his speed in km/h?",
            option_a="45 km/h", option_b="50 km/h", option_c="60 km/h", option_d="90 km/h",
            correct_option="c",
            explanation_ar="Solution:\n  Speed = Distance ÷ Time = 180 ÷ 3 = 60 km/h\n\nWhy other options are wrong:\n  • (a) 25 riyals: Result of division by wrong sum of parts\n  • (c) 75 riyals: Result of confusing larger and smaller part shares\n  • (d) 100 riyals: Result of multiplication instead of division or vice versa",
            solution_steps_ar='["Speed = Distance ÷ Time","Speed = 180 ÷ 3 = 60 km/h"]',
    tags="ratio", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q40 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.3,
            text_ar="Ali bought an item for 200 riyals and sold it for 250 riyals.\nHow many riyals did he profit?",
            option_a="25 riyals", option_b="50 riyals", option_c="75 riyals", option_d="100 riyals",
            correct_option="b",
            explanation_ar="Solution:\n  Profit = Selling price − Purchase price = 250 − 200 = 50 riyals\n\nWhy other options are wrong:\n  • (a) 2 riyals: Result of calculating profit percentage from selling price instead of purchase\n  • (c) 4 riyals: Result of calculating profit amount only without adding to price\n  • (d) 6 riyals: Result of confusing between profit and total revenue",
            solution_steps_ar='["Profit = 250 − 200 = 50 riyals"]',
    tags="profit", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q41 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.3,
            text_ar="If the price of 12 eggs = 9 riyals.\nWhat is the price of 4 eggs?",
            option_a="2 riyals", option_b="3 riyals", option_c="4 riyals", option_d="6 riyals",
            correct_option="b",
            explanation_ar="Solution:\n  Price per egg = 9 ÷ 12 = 0.75 riyal\n  Price of 4 eggs = 4 × 0.75 = 3 riyals\n\nWhy other options are wrong:\n  • (a) 0.5: Result of division by wrong sum of parts\n  • (b) 0.75: Result of confusing larger and smaller part shares\n  • (d) 1.5: Result of multiplication instead of division or vice versa",
            solution_steps_ar='["Price per egg = 9 ÷ 12 = 0.75 riyal","Price of 4 eggs = 4 × 0.75 = 3 riyals"]',
    tags="ratio", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q42 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.3,
            text_ar="What is the result of: 0.5 + 0.25 + 0.25 ?",
            option_a="0.5", option_b="0.75", option_c="1", option_d="1.5",
            correct_option="c",
            explanation_ar="Solution:\n  0.5 + 0.25 = 0.75\n  0.75 + 0.25 = 1\n\nWhy other options are wrong:\n  • (a) 0.5: Result of forgetting to unify denominators\n  • (b) 0.75: Result of calculating covered part instead of remaining or vice versa\n  • (d) 1.5: Result of error in multiplying or dividing fractions",
            solution_steps_ar='["0.5 + 0.25 = 0.75","0.75 + 0.25 = 1"]',
    tags="fraction", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ════════════════════════════════════════
        # Difficulty 0.4 — Medium Arithmetic Questions
        # ════════════════════════════════════════

        # ── Q43 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.4,
            text_ar="If an employee's salary = 6,000 riyals monthly, and he saves 15% of it.\nHow much does he save monthly?",
            option_a="750 riyals", option_b="800 riyals", option_c="900 riyals", option_d="1,000 riyals",
            correct_option="c",
            explanation_ar="Solution:\n  Savings = 6,000 × 0.15 = 900 riyals\n\nWhy other options are wrong:\n  • (a) 25: Result of calculating percentage from wrong number\n  • (c) 35: Result of forgetting to subtract or add percentage to original number\n  • (d) 40: Result of confusing between percentage value and percentage itself",
            solution_steps_ar='["Savings = Salary × savings rate","= 6,000 × 0.15 = 900 riyals"]',
    tags="percentage", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q44 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.4,
            text_ar="What is the arithmetic mean of numbers: 15, 25, 30, 35, 45?",
            option_a="25", option_b="30", option_c="35", option_d="40",
            correct_option="b",
            explanation_ar="Solution:\n  Sum = 15 + 25 + 30 + 35 + 45 = 150\n  Average = 150 ÷ 5 = 30\n\nWhy other options are wrong:\n  • (a) 160 km: Result of division by wrong number of values\n  • (b) 180 km: Result of forgetting to add new value to sum\n  • (d) 240 km: Result of calculating sum without dividing by number of elements",
            solution_steps_ar='["Sum = 15 + 25 + 30 + 35 + 45 = 150","Average = 150 ÷ 5 = 30"]',
    tags="average", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q45 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.4,
            text_ar="A car travels at 80 km/h.\nHow many kilometers does it cover in two and a half hours?",
            option_a="160 km", option_b="180 km", option_c="200 km", option_d="240 km",
            correct_option="c",
            explanation_ar="Solution:\n  Distance = Speed × Time = 80 × 2.5 = 200 km\n\nWhy other options are wrong:\n  • (a) 3: Result of forgetting to convert units between hours and minutes or km/h and m/s\n  • (b) 6: Result of using distance instead of time in equation\n  • (c) 8: Result of error in calculating average speed",
            solution_steps_ar='["Distance = Speed × Time","= 80 × 2.5 = 200 km"]',
    tags="speed", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q46 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.4,
            text_ar="Fahd ate ⅜ of a cake.\nIf the cake contains 24 pieces, how many pieces did he eat?",
            option_a="3", option_b="6", option_c="8", option_d="9",
            correct_option="d",
            explanation_ar="Solution:\n  Number of pieces = ⅜ × 24 = 3 × 24 ÷ 8 = 72 ÷ 8 = 9 pieces\n\nWhy other options are wrong:\n  • (a) 15%: Result of forgetting to unify denominators\n  • (c) 25%: Result of calculating covered part instead of remaining or vice versa\n  • (d) 30%: Result of error in multiplying or dividing fractions",
            solution_steps_ar='["Number of pieces = ⅜ × 24","= (3 × 24) ÷ 8 = 72 ÷ 8 = 9 pieces"]',
    tags="fraction", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q47 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.4,
            text_ar="The price of a mobile phone was reduced from 2,000 riyals to 1,600 riyals.\nWhat is the discount percentage?",
            option_a="15%", option_b="20%", option_c="25%", option_d="30%",
            correct_option="b",
            explanation_ar="Solution:\n  Discount amount = 2,000 − 1,600 = 400 riyals\n  Discount percentage = (400 ÷ 2,000) × 100 = 20%\n\nWhy other options are wrong:\n  • (a) 0.25 liter: Result of calculating percentage from wrong number\n  • (c) 1 liter: Result of forgetting to subtract or add percentage to original number\n  • (d) 1.5 liters: Result of confusing between percentage value and percentage itself",
            solution_steps_ar='["Discount amount = 2,000 − 1,600 = 400 riyals","Discount percentage = (400 ÷ 2,000) × 100 = 20%"]',
    tags="percentage,discount", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q48 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.4,
            text_ar="The ratio of salt to water in a solution = 1 : 9.\nIf the total volume is 5 liters, how many liters of salt?",
            option_a="0.25 liter", option_b="0.5 liter", option_c="1 liter", option_d="1.5 liters",
            correct_option="b",
            explanation_ar="Solution:\n  Sum of parts = 1 + 9 = 10\n  Salt quantity = (1 ÷ 10) × 5 = 0.5 liter\n\nWhy other options are wrong:\n  • (a) 81 riyals: Result of division by wrong sum of parts\n  • (c) 95 riyals: Result of confusing larger and smaller part shares\n  • (d) 100 riyals: Result of multiplication instead of division or vice versa",
            solution_steps_ar='["Sum of parts = 1 + 9 = 10","Salt quantity = (1 ÷ 10) × 5 = 0.5 liter"]',
    tags="ratio,mixture", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q49 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.4,
            text_ar="Mohammed bought 3 books at prices: 45, 35, and 20 riyals.\nHe got a 10% discount on the total.\nHow much did he pay?",
            option_a="81 riyals", option_b="90 riyals", option_c="95 riyals", option_d="100 riyals",
            correct_option="b",
            explanation_ar="Solution:\n  Total = 45 + 35 + 20 = 100 riyals\n  Discount = 100 × 0.1 = 10 riyals\n  Amount paid = 100 − 10 = 90 riyals\n\nWhy other options are wrong:\n  • (a) ¹⁄₁₂: Result of calculating percentage from wrong number\n  • (c) ⁷⁄₁₂: Result of forgetting to subtract or add percentage to original number\n  • (d) ½: Result of confusing between percentage value and percentage itself",
            solution_steps_ar='["Total = 45 + 35 + 20 = 100 riyals","Discount = 100 × 0.1 = 10","Amount paid = 100 − 10 = 90 riyals"]',
    tags="percentage,discount", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q50 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.4,
            text_ar="A student spent ⅓ of his allowance on food, and ¼ on transportation.\nWhat is the remaining fraction?",
            option_a="¹⁄₁₂", option_b="⁵⁄₁₂", option_c="⁷⁄₁₂", option_d="½",
            correct_option="b",
            explanation_ar="Solution:\n  Spent = ⅓ + ¼ = ⁴⁄₁₂ + ³⁄₁₂ = ⁷⁄₁₂\n  Remaining = 1 − ⁷⁄₁₂ = ⁵⁄₁₂\n\nWhy other options are wrong:\n  • (a) 45 euros: Result of forgetting to unify denominators\n  • (c) 84 euros: Result of calculating covered part instead of remaining or vice versa\n  • (d) 882 euros: Result of error in multiplying or dividing fractions",
            solution_steps_ar='["Spent = ⅓ + ¼ = ⁴⁄₁₂ + ³⁄₁₂ = ⁷⁄₁₂","Remaining = 1 − ⁷⁄₁₂ = ⁵⁄₁₂"]',
    tags="fraction", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q51 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.4,
            text_ar="If the exchange rate of euro = 4.20 riyals.\nHow many euros does one get when exchanging 210 riyals?",
            option_a="45 euros", option_b="50 euros", option_c="84 euros", option_d="882 euros",
            correct_option="b",
            explanation_ar="Solution:\n  Number of euros = 210 ÷ 4.20 = 50 euros\n\nWhy other options are wrong:\n  • (a) 320: Result of division instead of multiplication or vice versa\n  • (b) 350: Result of using approximate exchange rate\n  • (d) 380: Result of error in decimal calculation",
            solution_steps_ar='["Number of euros = Amount in riyals ÷ Euro price","= 210 ÷ 4.20 = 50 euros"]',
    tags="currency", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q52 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.4,
            text_ar="The number of club members = 300.\nThe number increased by 20%.\nWhat is the new number of members?",
            option_a="320", option_b="350", option_c="360", option_d="380",
            correct_option="c",
            explanation_ar="Solution:\n  Increase = 300 × 0.2 = 60\n  New number = 300 + 60 = 360\n\nWhy other options are wrong:\n  • (a) 320: Result of calculating percentage from wrong number\n  • (b) 350: Result of forgetting to subtract or add percentage to original number\n  • (d) 380: Result of confusing between percentage value and percentage itself",
            solution_steps_ar='["Increase = 300 × 0.2 = 60","New number = 300 + 60 = 360"]',
    tags="percentage", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ════════════════════════════════════════
        # Difficulty 0.5 — Medium Arithmetic Questions
        # ════════════════════════════════════════

        # ── Q53 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.5,
            text_ar="Weighted average of two grades:\n  Math = 80 (weight 3)\n  Science = 90 (weight 2)\nWhat is the weighted average?",
            option_a="82", option_b="84", option_c="85", option_d="86",
            correct_option="b",
            explanation_ar="Solution:\n  Average = (80 × 3 + 90 × 2) ÷ (3 + 2)\n  = (240 + 180) ÷ 5 = 420 ÷ 5 = 84\n\nWhy other options are wrong:\n  • (a) 6 hours: Result of division by wrong number of values\n  • (c) 8 hours: Result of forgetting to add new value to sum\n  • (d) 9 hours: Result of calculating sum without dividing by number of elements",
            solution_steps_ar='["Average = (80 × 3 + 90 × 2) ÷ (3 + 2)","= (240 + 180) ÷ 5 = 420 ÷ 5 = 84"]',
    tags="average", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q54 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.5,
            text_ar="A car covers 300 km.\nIt went at 100 km/h and returned at 75 km/h.\nWhat is the total time for the round trip?",
            option_a="6 hours", option_b="7 hours", option_c="8 hours", option_d="9 hours",
            correct_option="b",
            explanation_ar="Solution:\n  Going time = 300 ÷ 100 = 3 hours\n  Return time = 300 ÷ 75 = 4 hours\n  Total time = 3 + 4 = 7 hours\n\nWhy other options are wrong:\n  • (a) 6 years: Result of forgetting to convert units between hours and minutes or km/h and m/s\n  • (c) 10 years: Result of using distance instead of time in equation\n  • (d) 12 years: Result of error in calculating average speed",
            solution_steps_ar='["Going time = 300 ÷ 100 = 3 hours","Return time = 300 ÷ 75 = 4 hours","Total time = 3 + 4 = 7 hours"]',
    tags="speed", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q55 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.5,
            text_ar="If the father's age is 4 times his son's age, and the difference between their ages is 24 years.\nWhat is the son's age?",
            option_a="6 years", option_b="8 years", option_c="10 years", option_d="12 years",
            correct_option="b",
            explanation_ar="Solution:\n  Father's age = 4 × Son's age\n  Difference = 4x − x = 3x = 24\n  x = 24 ÷ 3 = 8 years\n\nWhy other options are wrong:\n  • (a) Profit 50 riyals: Result of forgetting to add future years to both ages\n  • (c) Loss 50 riyals: Result of calculating current age only without required addition\n  • (d) Profit 100 riyals: Result of confusion in forming age equation",
            solution_steps_ar='["Let son\'s age = x, father\'s age = 4x","Difference: 4x − x = 3x = 24","x = 24 ÷ 3 = 8 years"]',
    tags="age", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q56 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.5,
            text_ar="A merchant bought 50 items at 20 riyals each.\n10 items were damaged, and he sold the rest at 25 riyals each.\nDid he profit or lose and how much?",
            option_a="Profit 50 riyals", option_b="No profit or loss", option_c="Loss 50 riyals", option_d="Profit 100 riyals",
            correct_option="b",
            explanation_ar="Solution:\n  Purchase cost = 50 × 20 = 1,000 riyals\n  Items sold = 50 − 10 = 40 items\n  Sales revenue = 40 × 25 = 1,000 riyals\n  Profit = 1,000 − 1,000 = 0 (no profit or loss)\n\nWhy other options are wrong:\n  • (a) 4: Result of calculating profit percentage from selling price instead of purchase\n  • (c) 48: Result of calculating profit amount only without adding to price\n  • (d) 96: Result of confusing between profit and total revenue",
            solution_steps_ar='["Purchase cost = 50 × 20 = 1,000 riyals","Sold = 40 items, Revenue = 40 × 25 = 1,000","Difference = zero → no profit or loss"]',
    tags="profit", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q57 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.5,
            text_ar="LCM of numbers 8 and 12 equals:",
            option_a="4", option_b="24", option_c="48", option_d="96",
            correct_option="b",
            explanation_ar="Solution:\n  8 = 2³\n  12 = 2² × 3\n  LCM = 2³ × 3 = 24\n\nWhy other options are wrong:\n  • (a) 6.2 riyals: This is GCD instead of LCM or vice versa\n  • (b) 6.5 riyals: Result of multiplying numbers directly\n  • (d) 7 riyals: Result of error in prime factorization",
            solution_steps_ar='["8 = 2³, 12 = 2² × 3","LCM = 2³ × 3 = 8 × 3 = 24"]',
    tags="lcm-gcd", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q58 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.5,
            text_ar="Mixing 4 liters of milk at 5 riyals/liter with 6 liters at 8 riyals/liter.\nWhat is the price per liter of the mixture?",
            option_a="6.2 riyals", option_b="6.5 riyals", option_c="6.8 riyals", option_d="7 riyals",
            correct_option="c",
            explanation_ar="Solution:\n  Total cost = (4 × 5) + (6 × 8) = 20 + 48 = 68 riyals\n  Total volume = 4 + 6 = 10 liters\n  Price per liter = 68 ÷ 10 = 6.8 riyals\n\nWhy other options are wrong:\n  • (a) 20 km: Result of calculating arithmetic average instead of weighted average by quantity\n  • (c) 30 km: Result of forgetting to weight different quantities when mixing\n  • (d) 35 km: Result of dividing by number of solutions instead of total volume",
            solution_steps_ar='["Cost = (4 × 5) + (6 × 8) = 20 + 48 = 68","Volume = 10 liters","Price per liter = 68 ÷ 10 = 6.8 riyals"]',
    tags="mixture", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.43),

        # ── Q59 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.5,
            text_ar="A cyclist covered ⅗ of the distance in one hour.\nIf his speed was 15 km/h, what is the total distance?",
            option_a="20 km", option_b="25 km", option_c="30 km", option_d="35 km",
            correct_option="b",
            explanation_ar="Solution:\n  Distance covered in one hour = 15 km\n  This equals ⅗ of total distance\n  Total distance = 15 ÷ ⅗ = 15 × ⁵⁄₃ = 25 km\n\nWhy other options are wrong:\n  • (a) 100 riyals: Result of forgetting to unify denominators\n  • (b) 200 riyals: Result of calculating covered part instead of remaining or vice versa\n  • (d) 400 riyals: Result of error in multiplying or dividing fractions",
            solution_steps_ar='["Covered = 15 km = ⅗ of total distance","Total distance = 15 ÷ (3/5) = 15 × (5/3) = 25 km"]',
    tags="fraction,speed", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q60 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.5,
            text_ar="An amount of 600 riyals was distributed among three people in ratio 1 : 2 : 3.\nWhat is the share of the person with the largest share?",
            option_a="100 riyals", option_b="200 riyals", option_c="300 riyals", option_d="400 riyals",
            correct_option="c",
            explanation_ar="Solution:\n  Sum of parts = 1 + 2 + 3 = 6\n  Value of one part = 600 ÷ 6 = 100 riyals\n  Largest share (3 parts) = 3 × 100 = 300 riyals\n\nWhy other options are wrong:\n  • (a) 100 riyals: Result of calculating percentage from wrong number\n  • (b) 200 riyals: Result of forgetting to subtract or add percentage to original number\n  • (d) 400 riyals: Result of confusing between percentage value and percentage itself",
            solution_steps_ar='["Sum of parts = 1 + 2 + 3 = 6","Value of part = 600 ÷ 6 = 100","Largest share = 3 × 100 = 300 riyals"]',
    tags="percentage", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

    ]
