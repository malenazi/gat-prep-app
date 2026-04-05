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

        # ── Q61 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.2,
            text_ar="What is 25% of 200?",
            option_a="50", option_b="25", option_c="75", option_d="100",
            correct_option="a",
            explanation_ar="Given:\n  25% of 200\n\nSolution:\n  25% × 200 = (25/100) × 200 = 50\n\nWhy other options are wrong:\n  • (b) 25: Confuses the percentage number with the result\n  • (c) 75: Computes 75% instead of 25%\n  • (d) 100: Computes 50% instead of 25%",
            solution_steps_ar='["25% of 200 = (25/100) × 200","= 0.25 × 200","= 50"]',
    tags="percentage", stage="diagnostic",
    rating_clarity=5, rating_cognitive=3, rating_fairness=5, rating_distractors=4, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=3, rating_overall=4.29),

        # ── Q62 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.2,
            text_ar="A store sells an item for 80 riyals after a 20% discount. What was the original price?",
            option_a="96 riyals", option_b="100 riyals", option_c="90 riyals", option_d="110 riyals",
            correct_option="b",
            explanation_ar="Given:\n  Sale price = 80 riyals, discount = 20%\n\nSolution:\n  Original × (1 − 0.20) = 80\n  Original × 0.80 = 80\n  Original = 80 ÷ 0.80 = 100 riyals\n\nWhy other options are wrong:\n  • (a) 96 riyals: Adds 20% of 80 to 80 (80 + 16 = 96)\n  • (c) 90 riyals: Adds a flat 10 instead of computing the percentage\n  • (d) 110 riyals: Adds a flat 30 instead of computing the percentage",
            solution_steps_ar='["Original × (1 − 0.20) = 80","Original × 0.80 = 80","Original = 80 ÷ 0.80 = 100 riyals"]',
    tags="percentage,discount", stage="diagnostic",
    rating_clarity=5, rating_cognitive=3, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q63 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.3,
            text_ar="If the ratio of boys to girls in a class is 3:5, and there are 40 students total, how many boys are there?",
            option_a="12", option_b="15", option_c="20", option_d="25",
            correct_option="b",
            explanation_ar="Given:\n  Ratio boys:girls = 3:5, total = 40\n\nSolution:\n  Total parts = 3 + 5 = 8\n  One part = 40 ÷ 8 = 5\n  Boys = 3 × 5 = 15\n\nWhy other options are wrong:\n  • (a) 12: Computes 3/10 of 40 instead of 3/8\n  • (c) 20: Divides total in half instead of using the ratio\n  • (d) 25: Computes the number of girls (5 × 5) instead of boys",
            solution_steps_ar='["Total parts = 3 + 5 = 8","One part = 40 ÷ 8 = 5","Boys = 3 × 5 = 15"]',
    tags="ratio", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q64 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.3,
            text_ar="What is 3/4 + 1/6?",
            option_a="4/10", option_b="5/6", option_c="7/12", option_d="11/12",
            correct_option="d",
            explanation_ar="Given:\n  3/4 + 1/6\n\nSolution:\n  LCM of 4 and 6 = 12\n  3/4 = 9/12\n  1/6 = 2/12\n  9/12 + 2/12 = 11/12\n\nWhy other options are wrong:\n  • (a) 4/10: Adds numerators and denominators separately (3+1)/(4+6)\n  • (c) 7/12: Uses wrong conversion for 1/6 (gets 1/12 instead of 2/12)\n  • (b) 5/6: Computes 3/4 as 8/12 instead of 9/12",
            solution_steps_ar='["LCM of 4 and 6 = 12","3/4 = 9/12, 1/6 = 2/12","9/12 + 2/12 = 11/12"]',
    tags="fraction", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q65 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.3,
            text_ar="A car travels 180 km in 3 hours. What is its average speed?",
            option_a="60 km/h", option_b="540 km/h", option_c="90 km/h", option_d="50 km/h",
            correct_option="a",
            explanation_ar="Given:\n  Distance = 180 km, Time = 3 hours\n\nSolution:\n  Speed = Distance ÷ Time = 180 ÷ 3 = 60 km/h\n\nWhy other options are wrong:\n  • (d) 50 km/h: Divides 180 by 3.6 instead of 3\n  • (b) 540 km/h: Multiplies distance by time instead of dividing\n  • (c) 90 km/h: Divides 180 by 2 instead of 3",
            solution_steps_ar='["Speed = Distance ÷ Time","Speed = 180 ÷ 3","Speed = 60 km/h"]',
    tags="speed", stage="diagnostic",
    rating_clarity=5, rating_cognitive=3, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.43),

        # ── Q66 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.4,
            text_ar="If 6 workers can complete a job in 12 days, how many days will it take 9 workers to complete the same job?",
            option_a="8 days", option_b="6 days", option_c="10 days", option_d="18 days",
            correct_option="a",
            explanation_ar="Given:\n  6 workers → 12 days\n\nSolution:\n  Total work = 6 × 12 = 72 worker-days\n  Days for 9 workers = 72 ÷ 9 = 8 days\n\nWhy other options are wrong:\n  • (b) 6 days: Divides 12 by 2 instead of using inverse proportion\n  • (c) 10 days: Subtracts 2 from 12 days\n  • (d) 18 days: Multiplies 12 by 9/6 instead of dividing",
            solution_steps_ar='["Total work = 6 × 12 = 72 worker-days","Days for 9 workers = 72 ÷ 9","= 8 days"]',
    tags="work-rate", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q67 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.4,
            text_ar="The average of 5 numbers is 24. If a sixth number is added and the average becomes 25, what is the sixth number?",
            option_a="30", option_b="26", option_c="25", option_d="29",
            correct_option="a",
            explanation_ar="Given:\n  Average of 5 numbers = 24, new average with 6 numbers = 25\n\nSolution:\n  Sum of 5 numbers = 5 × 24 = 120\n  Sum of 6 numbers = 6 × 25 = 150\n  Sixth number = 150 − 120 = 30\n\nWhy other options are wrong:\n  • (c) 25: Uses the new average directly as the sixth number\n  • (b) 26: Adds 1 to the new average\n  • (d) 29: Subtracts incorrectly (150 − 120 = 29)",
            solution_steps_ar='["Sum of 5 numbers = 5 × 24 = 120","Sum of 6 numbers = 6 × 25 = 150","Sixth number = 150 − 120 = 30"]',
    tags="average", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q68 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.4,
            text_ar="A merchant buys goods for 500 riyals and sells them for 650 riyals. What is the profit percentage?",
            option_a="15%", option_b="23%", option_c="35%", option_d="30%",
            correct_option="d",
            explanation_ar="Given:\n  Cost = 500, Selling price = 650\n\nSolution:\n  Profit = 650 − 500 = 150\n  Profit % = (150/500) × 100 = 30%\n\nWhy other options are wrong:\n  • (a) 15%: Divides profit by selling price instead of cost price\n  • (b) 23%: Computes 150/650 × 100 ≈ 23%\n  • (c) 35%: Adds 5% to the correct answer",
            solution_steps_ar='["Profit = 650 − 500 = 150","Profit % = (150/500) × 100","= 30%"]',
    tags="profit", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q69 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.5,
            text_ar="A shirt is marked at 400 riyals. It is first discounted by 20%, then an additional 10% discount is applied on the new price. What is the final price?",
            option_a="288 riyals", option_b="280 riyals", option_c="300 riyals", option_d="270 riyals",
            correct_option="a",
            explanation_ar="Given:\n  Marked price = 400, first discount = 20%, second discount = 10%\n\nSolution:\n  After first discount: 400 × 0.80 = 320\n  After second discount: 320 × 0.90 = 288\n\nWhy other options are wrong:\n  • (b) 280 riyals: Applies 30% discount directly (400 × 0.70)\n  • (c) 300 riyals: Applies only the first 20% discount plus an error\n  • (d) 270 riyals: Applies 10% then 20% on the wrong base",
            solution_steps_ar='["After 20% discount: 400 × 0.80 = 320","After 10% discount: 320 × 0.90 = 288","Final price = 288 riyals"]',
    tags="discount,percentage", stage="diagnostic",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.86),

        # ── Q70 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.5,
            text_ar="What is the LCM of 12 and 18?",
            option_a="36", option_b="24", option_c="6", option_d="72",
            correct_option="a",
            explanation_ar="Given:\n  Find LCM of 12 and 18\n\nSolution:\n  12 = 2² × 3\n  18 = 2 × 3²\n  LCM = 2² × 3² = 4 × 9 = 36\n\nWhy other options are wrong:\n  • (c) 6: This is the GCD, not the LCM\n  • (b) 24: Uses 2³ × 3 instead of 2² × 3²\n  • (d) 72: Multiplies 12 × 18 ÷ 3 instead of finding LCM properly",
            solution_steps_ar='["12 = 2² × 3","18 = 2 × 3²","LCM = 2² × 3² = 36"]',
    tags="lcm-gcd", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ── Q71 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.5,
            text_ar="A father is 40 years old and his son is 10 years old. In how many years will the father be twice as old as his son?",
            option_a="20 years", option_b="15 years", option_c="25 years", option_d="10 years",
            correct_option="a",
            explanation_ar="Given:\n  Father = 40, Son = 10\n\nSolution:\n  In x years: 40 + x = 2(10 + x)\n  40 + x = 20 + 2x\n  20 = x\n  In 20 years: Father = 60, Son = 30, and 60 = 2 × 30 ✓\n\nWhy other options are wrong:\n  • (d) 10 years: Father=50, Son=20, ratio=2.5 not 2\n  • (b) 15 years: Father=55, Son=25, ratio=2.2 not 2\n  • (c) 25 years: Father=65, Son=35, ratio≈1.86 not 2",
            solution_steps_ar='["Let x = years from now","40 + x = 2(10 + x)","40 + x = 20 + 2x","x = 20 years"]',
    tags="age", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ── Q72 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.6,
            text_ar="If 1 USD = 3.75 SAR, how many US dollars can you get for 1,500 SAR?",
            option_a="375 USD", option_b="562.50 USD", option_c="450 USD", option_d="400 USD",
            correct_option="d",
            explanation_ar="Given:\n  1 USD = 3.75 SAR, amount = 1,500 SAR\n\nSolution:\n  USD = 1,500 ÷ 3.75 = 400 USD\n\nWhy other options are wrong:\n  • (a) 375 USD: Divides 1,500 by 4 instead of 3.75\n  • (c) 450 USD: Divides 1,500 by 3.33 instead of 3.75\n  • (b) 562.50 USD: Multiplies 1,500 by 0.375 (misplaces decimal)",
            solution_steps_ar='["USD = SAR ÷ exchange rate","USD = 1,500 ÷ 3.75","= 400 USD"]',
    tags="currency", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ── Q73 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.6,
            text_ar="If 10,000 riyals is invested at 5% annual compound interest, what is the amount after 2 years?",
            option_a="10,500 riyals", option_b="11,025 riyals", option_c="11,050 riyals", option_d="11,000 riyals",
            correct_option="b",
            explanation_ar="Given:\n  Principal = 10,000, Rate = 5%, Time = 2 years\n\nSolution:\n  A = P(1 + r)^t = 10,000 × (1.05)² = 10,000 × 1.1025 = 11,025\n\nWhy other options are wrong:\n  • (a) 10,500 riyals: Computes simple interest for 1 year only\n  • (d) 11,000 riyals: Computes simple interest for 2 years (no compounding)\n  • (c) 11,050 riyals: Adds an extra 25 to the simple interest result",
            solution_steps_ar='["A = P(1 + r)^t","A = 10,000 × (1.05)²","A = 10,000 × 1.1025 = 11,025 riyals"]',
    tags="compound-interest", stage="diagnostic",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        # ── Q74 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.6,
            text_ar="A 60-litre mixture contains milk and water in the ratio 2:1. How much water must be added to make the ratio 1:1?",
            option_a="10 litres", option_b="15 litres", option_c="30 litres", option_d="20 litres",
            correct_option="d",
            explanation_ar="Given:\n  Total = 60 litres, Milk:Water = 2:1\n\nSolution:\n  Milk = 60 × 2/3 = 40 litres\n  Water = 60 × 1/3 = 20 litres\n  For 1:1 ratio, water must equal milk = 40\n  Water to add = 40 − 20 = 20 litres\n\nWhy other options are wrong:\n  • (a) 10 litres: Adds half the needed amount\n  • (b) 15 litres: Computes 60/4 = 15 incorrectly\n  • (c) 30 litres: Adds the current amount of water instead of the difference",
            solution_steps_ar='["Milk = 40 litres, Water = 20 litres","For 1:1, need water = milk = 40","Add 40 − 20 = 20 litres"]',
    tags="mixture,ratio", stage="diagnostic",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        # ── Q75 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.7,
            text_ar="The sum of three consecutive even numbers is 78. What is the largest number?",
            option_a="28", option_b="26", option_c="24", option_d="30",
            correct_option="a",
            explanation_ar="Given:\n  Sum of 3 consecutive even numbers = 78\n\nSolution:\n  Let the numbers be n, n+2, n+4\n  n + n+2 + n+4 = 78\n  3n + 6 = 78\n  3n = 72, n = 24\n  Largest = 24 + 4 = 28\n\nWhy other options are wrong:\n  • (c) 24: This is the smallest of the three, not the largest\n  • (b) 26: This is the middle number\n  • (d) 30: Adds 6 to 24 instead of 4",
            solution_steps_ar='["n + (n+2) + (n+4) = 78","3n + 6 = 78, so n = 24","Largest = 24 + 4 = 28"]',
    tags="number-properties,sequences", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q76 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.2,
            text_ar="Convert 2.5 hours to minutes.",
            option_a="150 minutes", option_b="140 minutes", option_c="160 minutes", option_d="130 minutes",
            correct_option="a",
            explanation_ar="Given:\n  2.5 hours\n\nSolution:\n  2.5 × 60 = 150 minutes\n\nWhy other options are wrong:\n  • (d) 130 minutes: Computes 2 × 60 + 10 instead of 2 × 60 + 30\n  • (b) 140 minutes: Computes 2 × 60 + 20 instead of 2 × 60 + 30\n  • (c) 160 minutes: Computes 2 × 60 + 40 instead of 2 × 60 + 30",
            solution_steps_ar='["1 hour = 60 minutes","2.5 hours = 2.5 × 60","= 150 minutes"]',
    tags="unit-conversion,time", stage="foundation",
    rating_clarity=5, rating_cognitive=3, rating_fairness=5, rating_distractors=4, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=3, rating_overall=4.29),

        # ── Q77 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.2,
            text_ar="What is the next number in the sequence: 2, 6, 18, 54, ...?",
            option_a="108", option_b="216", option_c="72", option_d="162",
            correct_option="d",
            explanation_ar="Given:\n  Sequence: 2, 6, 18, 54, ...\n\nSolution:\n  Each term is multiplied by 3\n  Next = 54 × 3 = 162\n\nWhy other options are wrong:\n  • (a) 108: Multiplies 54 by 2 instead of 3\n  • (c) 72: Adds 18 to 54 instead of multiplying\n  • (b) 216: Multiplies 54 by 4 instead of 3",
            solution_steps_ar='["Pattern: each term × 3","6/2 = 3, 18/6 = 3, 54/18 = 3","Next = 54 × 3 = 162"]',
    tags="sequences", stage="foundation",
    rating_clarity=5, rating_cognitive=3, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=3, rating_overall=4.43),

        # ── Q78 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.3,
            text_ar="If 4 kg of apples cost 36 riyals, how much do 7 kg cost?",
            option_a="63 riyals", option_b="56 riyals", option_c="72 riyals", option_d="84 riyals",
            correct_option="a",
            explanation_ar="Given:\n  4 kg = 36 riyals\n\nSolution:\n  Price per kg = 36 ÷ 4 = 9 riyals\n  7 kg = 7 × 9 = 63 riyals\n\nWhy other options are wrong:\n  • (b) 56 riyals: Uses 8 riyals per kg instead of 9\n  • (c) 72 riyals: Doubles 36 instead of computing proportionally\n  • (d) 84 riyals: Uses 12 riyals per kg instead of 9",
            solution_steps_ar='["Price per kg = 36 ÷ 4 = 9 riyals","7 kg = 7 × 9","= 63 riyals"]',
    tags="proportion", stage="foundation",
    rating_clarity=5, rating_cognitive=3, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.43),

        # ── Q79 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.3,
            text_ar="What is the GCD (Greatest Common Divisor) of 36 and 48?",
            option_a="6", option_b="12", option_c="24", option_d="8",
            correct_option="b",
            explanation_ar="Given:\n  Find GCD of 36 and 48\n\nSolution:\n  36 = 2² × 3²\n  48 = 2⁴ × 3\n  GCD = 2² × 3 = 12\n\nWhy other options are wrong:\n  • (a) 6: Uses only 2 × 3 = 6, missing a factor of 2\n  • (d) 8: Uses 2³ instead of 2² × 3\n  • (c) 24: Uses 2³ × 3, but 36 has only 2²",
            solution_steps_ar='["36 = 2² × 3²","48 = 2⁴ × 3","GCD = 2² × 3 = 12"]',
    tags="lcm-gcd", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q80 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.3,
            text_ar="A number increased by 40% becomes 70. What is the original number?",
            option_a="42", option_b="45", option_c="48", option_d="50",
            correct_option="d",
            explanation_ar="Given:\n  Number × 1.40 = 70\n\nSolution:\n  Number = 70 ÷ 1.40 = 50\n\nWhy other options are wrong:\n  • (a) 42: Computes 70 × 0.60 = 42 (subtracts 40% of 70)\n  • (b) 45: Subtracts a flat 25 from 70\n  • (c) 48: Computes 70 − 70 × 0.40 × 0.80 or similar error",
            solution_steps_ar='["Original × 1.40 = 70","Original = 70 ÷ 1.40","= 50"]',
    tags="percentage", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=4, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.43),

        # ── Q81 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.4,
            text_ar="A train 150 meters long passes a pole in 10 seconds. What is the speed of the train in km/h?",
            option_a="15 km/h", option_b="45 km/h", option_c="60 km/h", option_d="54 km/h",
            correct_option="d",
            explanation_ar="Given:\n  Length = 150 m, Time = 10 s\n\nSolution:\n  Speed = 150 ÷ 10 = 15 m/s\n  Convert: 15 × (3600/1000) = 15 × 3.6 = 54 km/h\n\nWhy other options are wrong:\n  • (a) 15 km/h: Gives speed in m/s without converting to km/h\n  • (b) 45 km/h: Multiplies 15 by 3 instead of 3.6\n  • (c) 60 km/h: Multiplies 15 by 4 instead of 3.6",
            solution_steps_ar='["Speed = 150 ÷ 10 = 15 m/s","Convert to km/h: 15 × 3.6","= 54 km/h"]',
    tags="speed,unit-conversion", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q82 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.4,
            text_ar="If a pipe can fill a tank in 6 hours and another pipe can fill it in 3 hours, how long will both pipes take together?",
            option_a="2 hours", option_b="1.5 hours", option_c="3 hours", option_d="4.5 hours",
            correct_option="a",
            explanation_ar="Given:\n  Pipe A fills in 6 hours, Pipe B fills in 3 hours\n\nSolution:\n  Rate of A = 1/6, Rate of B = 1/3\n  Combined rate = 1/6 + 1/3 = 1/6 + 2/6 = 3/6 = 1/2\n  Time = 1 ÷ (1/2) = 2 hours\n\nWhy other options are wrong:\n  • (b) 1.5 hours: Divides 3 by 2 without considering both rates\n  • (c) 3 hours: Uses only the faster pipe's time\n  • (d) 4.5 hours: Averages 6 and 3 as (6+3)/2",
            solution_steps_ar='["Rate A = 1/6, Rate B = 1/3","Combined = 1/6 + 2/6 = 3/6 = 1/2","Time = 2 hours"]',
    tags="work-rate", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q83 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.4,
            text_ar="Estimate the value of 49.7 × 20.3 to the nearest hundred.",
            option_a="900", option_b="1,200", option_c="1,100", option_d="1,000",
            correct_option="d",
            explanation_ar="Given:\n  49.7 × 20.3\n\nSolution:\n  Estimate: 50 × 20 = 1,000\n  Exact: 49.7 × 20.3 = 1,008.91\n  Nearest hundred = 1,000\n\nWhy other options are wrong:\n  • (a) 900: Underestimates by rounding both numbers down\n  • (c) 1,100: Overestimates by rounding 20.3 up to 22\n  • (b) 1,200: Significantly overestimates the product",
            solution_steps_ar='["Round: 49.7 ≈ 50, 20.3 ≈ 20","50 × 20 = 1,000","Nearest hundred = 1,000"]',
    tags="estimation", stage="foundation",
    rating_clarity=5, rating_cognitive=3, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.43),

        # ── Q84 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.4,
            text_ar="How many minutes are there in 3 days and 5 hours?",
            option_a="4,380 minutes", option_b="4,620 minutes", option_c="4,680 minutes", option_d="4,500 minutes",
            correct_option="b",
            explanation_ar="Given:\n  3 days and 5 hours\n\nSolution:\n  3 days = 3 × 24 = 72 hours\n  Total hours = 72 + 5 = 77 hours\n  Minutes = 77 × 60 = 4,620 minutes\n\nWhy other options are wrong:\n  • (a) 4,380 minutes: Uses 73 hours instead of 77\n  • (d) 4,500 minutes: Uses 75 hours (3 × 25)\n  • (c) 4,680 minutes: Uses 78 hours",
            solution_steps_ar='["3 days = 72 hours","72 + 5 = 77 hours","77 × 60 = 4,620 minutes"]',
    tags="time,unit-conversion", stage="foundation",
    rating_clarity=5, rating_cognitive=3, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.43),

        # ── Q85 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.5,
            text_ar="The ratio of two numbers is 5:3. If their difference is 24, what is the larger number?",
            option_a="36", option_b="60", option_c="48", option_d="72",
            correct_option="b",
            explanation_ar="Given:\n  Ratio = 5:3, difference = 24\n\nSolution:\n  Difference in parts = 5 − 3 = 2\n  One part = 24 ÷ 2 = 12\n  Larger number = 5 × 12 = 60\n\nWhy other options are wrong:\n  • (a) 36: Computes 3 × 12 = 36 (the smaller number)\n  • (c) 48: Computes 4 × 12 = 48 (wrong multiplier)\n  • (d) 72: Computes 6 × 12 = 72 (wrong multiplier)",
            solution_steps_ar='["Difference in parts = 5 − 3 = 2","One part = 24 ÷ 2 = 12","Larger = 5 × 12 = 60"]',
    tags="ratio", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ── Q86 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.5,
            text_ar="A shopkeeper marks an item 60% above the cost price, then gives a 25% discount. What is the profit percentage?",
            option_a="20%", option_b="15%", option_c="25%", option_d="35%",
            correct_option="a",
            explanation_ar="Given:\n  Markup = 60%, Discount = 25%\n\nSolution:\n  Let cost = 100\n  Marked price = 100 × 1.60 = 160\n  Selling price = 160 × 0.75 = 120\n  Profit = 120 − 100 = 20\n  Profit % = 20%\n\nWhy other options are wrong:\n  • (b) 15%: Subtracts 25% from 60% then subtracts more\n  • (c) 25%: Confuses discount percentage with profit\n  • (d) 35%: Subtracts 25 from 60 directly",
            solution_steps_ar='["Let cost = 100, Marked = 160","Selling = 160 × 0.75 = 120","Profit % = (120−100)/100 = 20%"]',
    tags="profit,discount,percentage", stage="foundation",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        # ── Q87 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.5,
            text_ar="If 3/5 of a number equals 45, what is 2/3 of the same number?",
            option_a="30", option_b="50", option_c="40", option_d="60",
            correct_option="b",
            explanation_ar="Given:\n  3/5 × N = 45\n\nSolution:\n  N = 45 × 5/3 = 75\n  2/3 × 75 = 50\n\nWhy other options are wrong:\n  • (a) 30: Computes 2/3 × 45 = 30 (uses 45 instead of 75)\n  • (c) 40: Computes 2/3 × 60 (wrong original number)\n  • (d) 60: Computes 4/5 × 75 = 60",
            solution_steps_ar='["3/5 × N = 45, so N = 45 × 5/3 = 75","2/3 × 75 = 50"]',
    tags="fraction", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ── Q88 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.5,
            text_ar="Two trains start at the same time from cities 600 km apart and travel toward each other. Train A travels at 70 km/h and Train B at 80 km/h. After how many hours will they meet?",
            option_a="4 hours", option_b="3 hours", option_c="5 hours", option_d="6 hours",
            correct_option="a",
            explanation_ar="Given:\n  Distance = 600 km, Speed A = 70 km/h, Speed B = 80 km/h\n\nSolution:\n  Combined speed = 70 + 80 = 150 km/h\n  Time = 600 ÷ 150 = 4 hours\n\nWhy other options are wrong:\n  • (b) 3 hours: Divides 600 by 200 (incorrect combined speed)\n  • (c) 5 hours: Divides 600 by 120\n  • (d) 6 hours: Divides 600 by 100",
            solution_steps_ar='["Combined speed = 70 + 80 = 150 km/h","Time = 600 ÷ 150","= 4 hours"]',
    tags="speed", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ── Q89 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.5,
            text_ar="What is the value of 2³ + 3² − 5?",
            option_a="10", option_b="16", option_c="14", option_d="12",
            correct_option="d",
            explanation_ar="Given:\n  2³ + 3² − 5\n\nSolution:\n  2³ = 8\n  3² = 9\n  8 + 9 − 5 = 12\n\nWhy other options are wrong:\n  • (a) 10: Computes 2³ as 6 instead of 8\n  • (c) 14: Computes 3² as 11 or forgets to subtract 5\n  • (b) 16: Computes 2³ + 3² without subtracting 5 (8+9=17, close error)",
            solution_steps_ar='["2³ = 8","3² = 9","8 + 9 − 5 = 12"]',
    tags="number-properties", stage="foundation",
    rating_clarity=5, rating_cognitive=3, rating_fairness=5, rating_distractors=4, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=3, rating_overall=4.29),

        # ── Q90 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.6,
            text_ar="A mixture of 40 litres of milk and water contains 10% water. How much water should be added to make water 20% of the new mixture?",
            option_a="5 litres", option_b="4 litres", option_c="6 litres", option_d="8 litres",
            correct_option="a",
            explanation_ar="Given:\n  Total = 40 litres, Water = 10% of 40 = 4 litres, Milk = 36 litres\n\nSolution:\n  Let x litres of water be added\n  (4 + x) / (40 + x) = 20/100 = 1/5\n  5(4 + x) = 40 + x\n  20 + 5x = 40 + x\n  4x = 20\n  x = 5 litres\n\nWhy other options are wrong:\n  • (b) 4 litres: Gets 8/44 ≈ 18.2%, not 20%\n  • (c) 6 litres: Gets 10/46 ≈ 21.7%, not 20%\n  • (d) 8 litres: Gets 12/48 = 25%, not 20%",
            solution_steps_ar='["Water = 10% of 40 = 4 litres","(4+x)/(40+x) = 1/5","5(4+x) = 40+x → x = 5 litres"]',
    tags="mixture,percentage", stage="foundation",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        # ── Q91 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.6,
            text_ar="If a map scale is 1:50,000, and two cities are 8 cm apart on the map, what is the actual distance between them in kilometers?",
            option_a="4 km", option_b="40 km", option_c="400 km", option_d="0.4 km",
            correct_option="a",
            explanation_ar="Given:\n  Scale = 1:50,000, Map distance = 8 cm\n\nSolution:\n  Actual distance = 8 × 50,000 = 400,000 cm\n  400,000 cm = 4,000 m = 4 km\n\nWhy other options are wrong:\n  • (b) 40 km: Multiplies by an extra factor of 10\n  • (c) 400 km: Forgets to convert cm to km properly\n  • (d) 0.4 km: Divides by an extra factor of 10",
            solution_steps_ar='["Actual = 8 × 50,000 = 400,000 cm","400,000 cm ÷ 100,000 = 4 km"]',
    tags="proportion,unit-conversion", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ── Q92 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.6,
            text_ar="A person deposits 20,000 riyals at 8% annual compound interest. What is the interest earned after 2 years?",
            option_a="3,200 riyals", option_b="3,456 riyals", option_c="3,400 riyals", option_d="3,328 riyals",
            correct_option="d",
            explanation_ar="Given:\n  P = 20,000, r = 8%, t = 2 years\n\nSolution:\n  A = 20,000 × (1.08)² = 20,000 × 1.1664 = 23,328\n  Interest = 23,328 − 20,000 = 3,328\n\nWhy other options are wrong:\n  • (a) 3,200 riyals: Simple interest only (20,000 × 0.08 × 2)\n  • (c) 3,400 riyals: Adds an arbitrary amount to simple interest\n  • (b) 3,456 riyals: Uses incorrect compounding calculation",
            solution_steps_ar='["A = 20,000 × (1.08)² = 23,328","Interest = 23,328 − 20,000","= 3,328 riyals"]',
    tags="compound-interest", stage="foundation",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        # ── Q93 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.6,
            text_ar="The average of four numbers is 35. If one number is removed, the average of the remaining three becomes 30. What number was removed?",
            option_a="50", option_b="45", option_c="40", option_d="55",
            correct_option="a",
            explanation_ar="Given:\n  Average of 4 numbers = 35, Average of remaining 3 = 30\n\nSolution:\n  Sum of 4 = 4 × 35 = 140\n  Sum of 3 = 3 × 30 = 90\n  Removed number = 140 − 90 = 50\n\nWhy other options are wrong:\n  • (c) 40: Subtracts 100 from 140 instead of 90\n  • (b) 45: Computes the average of 35 and 30 × 3 incorrectly\n  • (d) 55: Adds 5 to the correct answer",
            solution_steps_ar='["Sum of 4 = 140, Sum of 3 = 90","Removed = 140 − 90 = 50"]',
    tags="average", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ── Q94 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.7,
            text_ar="A number when divided by 7 gives a remainder of 3. What is the remainder when the square of the number is divided by 7?",
            option_a="2", option_b="1", option_c="4", option_d="6",
            correct_option="a",
            explanation_ar="Given:\n  N ≡ 3 (mod 7)\n\nSolution:\n  N² ≡ 3² ≡ 9 ≡ 2 (mod 7)\n  Since 9 = 7 × 1 + 2, remainder = 2\n\nWhy other options are wrong:\n  • (b) 1: Confuses with remainder of 1² ÷ 7\n  • (c) 4: Computes 3 + 1 instead of 3²\n  • (d) 6: Computes 3 × 2 instead of 3²",
            solution_steps_ar='["N ≡ 3 (mod 7)","N² ≡ 9 (mod 7)","9 = 7 × 1 + 2, remainder = 2"]',
    tags="number-properties", stage="foundation",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        # ── Q95 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.3,
            text_ar="Convert 3.5 kilometers to meters.",
            option_a="350 meters", option_b="35 meters", option_c="35,000 meters", option_d="3,500 meters",
            correct_option="d",
            explanation_ar="Given:\n  3.5 kilometers\n\nSolution:\n  1 km = 1,000 m\n  3.5 km = 3.5 × 1,000 = 3,500 m\n\nWhy other options are wrong:\n  • (a) 350 meters: Multiplies by 100 instead of 1,000\n  • (c) 35,000 meters: Multiplies by 10,000 instead of 1,000\n  • (b) 35 meters: Multiplies by 10 instead of 1,000",
            solution_steps_ar='["1 km = 1,000 meters","3.5 × 1,000 = 3,500 meters"]',
    tags="unit-conversion", stage="foundation",
    rating_clarity=5, rating_cognitive=3, rating_fairness=5, rating_distractors=4, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=3, rating_overall=4.14),

        # ── Q96 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.4,
            text_ar="What is the 10th term of the arithmetic sequence: 3, 7, 11, 15, ...?",
            option_a="39", option_b="37", option_c="35", option_d="43",
            correct_option="a",
            explanation_ar="Given:\n  First term a = 3, common difference d = 4\n\nSolution:\n  nth term = a + (n−1)d\n  10th term = 3 + (10−1) × 4 = 3 + 36 = 39\n\nWhy other options are wrong:\n  • (c) 35: Computes 3 + 8 × 4 = 35 (uses n−2 instead of n−1)\n  • (b) 37: Computes 3 + 34, an arithmetic error\n  • (d) 43: Computes 3 + 10 × 4 = 43 (uses n instead of n−1)",
            solution_steps_ar='["a = 3, d = 4","10th = 3 + (10−1) × 4","= 3 + 36 = 39"]',
    tags="sequences", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q97 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.4,
            text_ar="A product that costs 250 riyals is sold at a loss of 12%. What is the selling price?",
            option_a="200 riyals", option_b="210 riyals", option_c="230 riyals", option_d="220 riyals",
            correct_option="d",
            explanation_ar="Given:\n  Cost = 250, Loss = 12%\n\nSolution:\n  Selling price = 250 × (1 − 0.12) = 250 × 0.88 = 220\n\nWhy other options are wrong:\n  • (a) 200 riyals: Applies 20% loss instead of 12%\n  • (b) 210 riyals: Applies 16% loss instead of 12%\n  • (c) 230 riyals: Applies 8% loss instead of 12%",
            solution_steps_ar='["Selling = Cost × (1 − loss%)","= 250 × 0.88","= 220 riyals"]',
    tags="profit,percentage", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q98 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.5,
            text_ar="If y is directly proportional to x, and y = 12 when x = 4, what is y when x = 10?",
            option_a="24", option_b="30", option_c="28", option_d="36",
            correct_option="b",
            explanation_ar="Given:\n  y ∝ x, y = 12 when x = 4\n\nSolution:\n  k = y/x = 12/4 = 3\n  When x = 10: y = 3 × 10 = 30\n\nWhy other options are wrong:\n  • (a) 24: Computes 12 × 2 (doubles y for x going from 4 to 10)\n  • (c) 28: Computes 12 + 16, an incorrect method\n  • (d) 36: Computes 12 × 3 (triples y)",
            solution_steps_ar='["k = y/x = 12/4 = 3","When x = 10: y = 3 × 10","= 30"]',
    tags="proportion", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ── Q99 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.5,
            text_ar="Convert 72 km/h to m/s.",
            option_a="7.2 m/s", option_b="25 m/s", option_c="36 m/s", option_d="20 m/s",
            correct_option="d",
            explanation_ar="Given:\n  72 km/h\n\nSolution:\n  m/s = km/h ÷ 3.6\n  72 ÷ 3.6 = 20 m/s\n\nWhy other options are wrong:\n  • (a) 7.2 m/s: Divides by 10 instead of 3.6\n  • (c) 36 m/s: Divides by 2 instead of 3.6\n  • (b) 25 m/s: Divides 72 by 2.88 or makes another error",
            solution_steps_ar='["To convert km/h to m/s, divide by 3.6","72 ÷ 3.6 = 20 m/s"]',
    tags="unit-conversion,speed", stage="building",
    rating_clarity=5, rating_cognitive=3, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q100 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.5,
            text_ar="The sum of the first 20 natural numbers is:",
            option_a="190", option_b="200", option_c="220", option_d="210",
            correct_option="d",
            explanation_ar="Given:\n  Sum of 1 + 2 + 3 + ... + 20\n\nSolution:\n  Sum = n(n+1)/2 = 20 × 21 / 2 = 210\n\nWhy other options are wrong:\n  • (a) 190: Uses n(n−1)/2 = 20 × 19/2 = 190\n  • (b) 200: Uses 20 × 10 = 200 (wrong formula)\n  • (c) 220: Uses 20 × 22/2 = 220",
            solution_steps_ar='["Sum = n(n+1)/2","= 20 × 21 / 2","= 210"]',
    tags="sequences,number-properties", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ── Q101 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.6,
            text_ar="A person walks at 5 km/h for 2 hours, then cycles at 15 km/h for 1 hour. What is his average speed for the entire journey?",
            option_a="8.33 km/h", option_b="10 km/h", option_c="15 km/h", option_d="7.5 km/h",
            correct_option="a",
            explanation_ar="Given:\n  Walking: 5 km/h for 2 hours; Cycling: 15 km/h for 1 hour\n\nSolution:\n  Total distance = (5 × 2) + (15 × 1) = 10 + 15 = 25 km\n  Total time = 2 + 1 = 3 hours\n  Average speed = 25 ÷ 3 ≈ 8.33 km/h\n\nWhy other options are wrong:\n  • (b) 10 km/h: Averages 5 and 15 directly (5+15)/2\n  • (c) 15 km/h: Uses only cycling speed\n  • (d) 7.5 km/h: Computes 15/2 = 7.5",
            solution_steps_ar='["Total distance = 10 + 15 = 25 km","Total time = 3 hours","Average speed = 25/3 ≈ 8.33 km/h"]',
    tags="speed,average", stage="building",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        # ── Q102 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.6,
            text_ar="If 15% of a number is 45, what is 35% of the same number?",
            option_a="90", option_b="95", option_c="100", option_d="105",
            correct_option="d",
            explanation_ar="Given:\n  15% × N = 45\n\nSolution:\n  N = 45 ÷ 0.15 = 300\n  35% × 300 = 105\n\nWhy other options are wrong:\n  • (a) 90: Computes 30% of 300 = 90\n  • (b) 95: Adds 50 to 45 instead of computing correctly\n  • (c) 100: Computes 1/3 of 300 = 100",
            solution_steps_ar='["N = 45 ÷ 0.15 = 300","35% of 300 = 0.35 × 300","= 105"]',
    tags="percentage", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ── Q103 ──
        Question(skill_id="quant_arithmetic", question_type="comparison", difficulty=0.5,
            text_ar="Compare:\n\n▸ Column (A): 3/7 of 490\n▸ Column (B): 5/9 of 360",
            option_a="Column (A) is greater", option_b="Column (B) is greater", option_c="The two values are equal", option_d="The relationship cannot be determined",
            correct_option="a",
            explanation_ar="Given:\n  Column A: 3/7 × 490 = 210\n  Column B: 5/9 × 360 = 200\n\nSolution:\n  210 > 200, so Column A is greater\n\nWhy other options are wrong:\n  • (b) Column (B) is greater: 200 < 210\n  • (c) The two values are equal: 210 ≠ 200\n  • (d) The relationship cannot be determined: Both values are fixed",
            solution_steps_ar='["A = 3/7 × 490 = 210","B = 5/9 × 360 = 200","210 > 200, A is greater"]',
    tags="fraction,comparison", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ── Q104 ──
        Question(skill_id="quant_arithmetic", question_type="comparison", difficulty=0.6,
            text_ar="Compare:\n\n▸ Column (A): 40% of 150\n▸ Column (B): 60% of 100",
            option_a="Column (A) is greater", option_b="Column (B) is greater", option_c="The two values are equal", option_d="The relationship cannot be determined",
            correct_option="c",
            explanation_ar="Given:\n  Column A: 40% × 150 = 60\n  Column B: 60% × 100 = 60\n\nSolution:\n  60 = 60, so the two values are equal\n\nWhy other options are wrong:\n  • (a) Column (A) is greater: Both equal 60\n  • (b) Column (B) is greater: Both equal 60\n  • (d) The relationship cannot be determined: Both values are fixed",
            solution_steps_ar='["A = 0.40 × 150 = 60","B = 0.60 × 100 = 60","60 = 60, equal"]',
    tags="percentage,comparison", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ── Q105 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.7,
            text_ar="A can do a piece of work in 10 days. B can do it in 15 days. They work together for 4 days, then A leaves. How many more days will B take to finish?",
            option_a="3 days", option_b="4 days", option_c="6 days", option_d="5 days",
            correct_option="d",
            explanation_ar="Given:\n  A: 10 days, B: 15 days, together for 4 days\n\nSolution:\n  Rate A = 1/10, Rate B = 1/15\n  Together per day = 1/10 + 1/15 = 3/30 + 2/30 = 5/30 = 1/6\n  Work done in 4 days = 4 × 1/6 = 2/3\n  Remaining = 1 − 2/3 = 1/3\n  Days for B alone = (1/3) ÷ (1/15) = 5 days\n\nWhy other options are wrong:\n  • (a) 3 days: B does 3/15 = 1/5 in 3 days, not 1/3\n  • (b) 4 days: B does 4/15 in 4 days, not 1/3\n  • (c) 6 days: B does 6/15 = 2/5 in 6 days, not 1/3",
            solution_steps_ar='["Combined rate = 1/10 + 1/15 = 1/6","Work in 4 days = 4/6 = 2/3","Remaining = 1/3, B alone = (1/3)÷(1/15) = 5 days"]',
    tags="work-rate", stage="building",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        # ── Q106 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.7,
            text_ar="The price of an item increases by 20%, then decreases by 20%. What is the net percentage change from the original price?",
            option_a="0%", option_b="−4%", option_c="−2%", option_d="+4%",
            correct_option="b",
            explanation_ar="Given:\n  Increase 20%, then decrease 20%\n\nSolution:\n  Let original = 100\n  After increase: 100 × 1.20 = 120\n  After decrease: 120 × 0.80 = 96\n  Net change = 96 − 100 = −4, so −4%\n\nWhy other options are wrong:\n  • (a) 0%: Assumes increase and decrease cancel out\n  • (c) −2%: Halves the correct answer\n  • (d) +4%: Gets the sign wrong",
            solution_steps_ar='["After +20%: 100 × 1.20 = 120","After −20%: 120 × 0.80 = 96","Net change = −4%"]',
    tags="percentage", stage="building",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        # ── Q107 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.7,
            text_ar="A bag contains 5 red, 4 blue, and 3 green marbles. If 2 marbles are drawn at random without replacement, what is the probability that both are red?",
            option_a="5/33", option_b="5/36", option_c="1/6", option_d="25/144",
            correct_option="a",
            explanation_ar="Given:\n  Red=5, Blue=4, Green=3, Total=12\n\nSolution:\n  P(both red) = C(5,2)/C(12,2) = 10/66 = 5/33\n\nWhy other options are wrong:\n  • (b) 5/36: Uses 12 × 6 in denominator instead of C(12,2)\n  • (c) 1/6: Simplifies incorrectly\n  • (d) 25/144: Computes (5/12)² as if with replacement",
            solution_steps_ar='["C(5,2) = 10, C(12,2) = 66","P = 10/66 = 5/33"]',
    tags="number-properties", stage="building",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.86),

        # ── Q108 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.4,
            text_ar="If a clock shows 3:15, what is the angle between the hour hand and the minute hand?",
            option_a="7.5°", option_b="0°", option_c="15°", option_d="22.5°",
            correct_option="a",
            explanation_ar="Given:\n  Time = 3:15\n\nSolution:\n  Minute hand at 15 min = 90° (from 12)\n  Hour hand at 3:15 = 3 × 30° + 15 × 0.5° = 90° + 7.5° = 97.5°\n  Angle = 97.5° − 90° = 7.5°\n\nWhy other options are wrong:\n  • (b) 0°: Assumes both hands are at the same position (3 o'clock position)\n  • (c) 15°: Doubles the correct answer\n  • (d) 22.5°: Triples the correct answer",
            solution_steps_ar='["Minute hand = 90°","Hour hand = 90° + 7.5° = 97.5°","Angle = 7.5°"]',
    tags="time,estimation", stage="building",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ── Q109 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.6,
            text_ar="Simplify: (5/8) ÷ (15/16)",
            option_a="1/2", option_b="2/3", option_c="3/4", option_d="8/15",
            correct_option="b",
            explanation_ar="Given:\n  (5/8) ÷ (15/16)\n\nSolution:\n  (5/8) × (16/15) = (5 × 16)/(8 × 15) = 80/120 = 2/3\n\nWhy other options are wrong:\n  • (a) 1/2: Divides numerators only: 5/15 = 1/3, then doubles\n  • (c) 3/4: Multiplies 5/8 × 15/16 instead of dividing\n  • (d) 8/15: Inverts the wrong fraction",
            solution_steps_ar='["(5/8) ÷ (15/16) = (5/8) × (16/15)","= 80/120","= 2/3"]',
    tags="fraction", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ── Q110 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.7,
            text_ar="A car uses 8 litres of fuel per 100 km. If the fuel tank holds 56 litres, how far can the car travel on a full tank?",
            option_a="600 km", option_b="650 km", option_c="750 km", option_d="700 km",
            correct_option="d",
            explanation_ar="Given:\n  Consumption = 8 L per 100 km, Tank = 56 L\n\nSolution:\n  Distance = (56 ÷ 8) × 100 = 7 × 100 = 700 km\n\nWhy other options are wrong:\n  • (a) 600 km: Divides 56 by 9.33 instead of 8\n  • (b) 650 km: Computes 56/8 = 7, then 7 × 93\n  • (c) 750 km: Uses fuel rate of 7.5 L per 100 km",
            solution_steps_ar='["How many sets of 8L? 56 ÷ 8 = 7","Distance = 7 × 100 = 700 km"]',
    tags="proportion,unit-conversion", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ── Q111 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.7,
            text_ar="The present ages of A and B are in the ratio 4:5. Five years ago, their ages were in the ratio 3:4. What is the present age of B?",
            option_a="15 years", option_b="20 years", option_c="25 years", option_d="30 years",
            correct_option="c",
            explanation_ar="Given:\n  Present ratio A:B = 4:5, Five years ago ratio = 3:4\n\nSolution:\n  Let A = 4x, B = 5x\n  Five years ago: (4x−5)/(5x−5) = 3/4\n  4(4x−5) = 3(5x−5)\n  16x − 20 = 15x − 15\n  x = 5\n  B = 5 × 5 = 25 years\n\nWhy other options are wrong:\n  • (a) 15 years: Uses x = 3\n  • (b) 20 years: Uses x = 4\n  • (d) 30 years: Uses x = 6",
            solution_steps_ar='["Let A = 4x, B = 5x","(4x−5)/(5x−5) = 3/4","16x − 20 = 15x − 15, x = 5","B = 25 years"]',
    tags="age,ratio", stage="building",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        # ── Q112 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.5,
            text_ar="How many even numbers are there between 11 and 51 (exclusive)?",
            option_a="18", option_b="20", option_c="19", option_d="21",
            correct_option="b",
            explanation_ar="Given:\n  Even numbers between 11 and 51 (exclusive)\n\nSolution:\n  First even = 12, Last even = 50\n  Count = (50 − 12)/2 + 1 = 38/2 + 1 = 19 + 1 = 20\n\nWhy other options are wrong:\n  • (a) 18: Off by 2, possibly excluding endpoints\n  • (c) 19: Off by 1, forgetting to add 1 in the formula\n  • (d) 21: Includes 52 or makes an off-by-one error",
            solution_steps_ar='["First even after 11 = 12, Last even before 51 = 50","Count = (50 − 12)/2 + 1","= 20"]',
    tags="number-properties", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ── Q113 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.3,
            text_ar="If a rectangle has a perimeter of 30 cm and its length is 10 cm, what is its width?",
            option_a="5 cm", option_b="10 cm", option_c="15 cm", option_d="20 cm",
            correct_option="a",
            explanation_ar="Given:\n  Perimeter = 30 cm, Length = 10 cm\n\nSolution:\n  P = 2(L + W)\n  30 = 2(10 + W)\n  15 = 10 + W\n  W = 5 cm\n\nWhy other options are wrong:\n  • (b) 10 cm: Assumes it is a square (L = W)\n  • (c) 15 cm: Divides perimeter by 2 without subtracting length\n  • (d) 20 cm: Subtracts length from perimeter without dividing by 2",
            solution_steps_ar='["P = 2(L + W)","30 = 2(10 + W)","W = 5 cm"]',
    tags="proportion", stage="building",
    rating_clarity=5, rating_cognitive=3, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.43),

        # ── Q114 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.8,
            text_ar="A sum of 12,000 riyals is divided among A, B, and C such that A gets 1/2 of what B gets, and B gets 2/3 of what C gets. How much does C get?",
            option_a="3,600 riyals", option_b="4,000 riyals", option_c="5,000 riyals", option_d="6,000 riyals",
            correct_option="d",
            explanation_ar="Given:\n  A + B + C = 12,000, A = B/2, B = 2C/3\n\nSolution:\n  B = 2C/3\n  A = B/2 = C/3\n  A + B + C = C/3 + 2C/3 + C = C + C = 2C\n  2C = 12,000\n  C = 6,000 riyals\n\nWhy other options are wrong:\n  • (a) 3,600 riyals: Uses wrong ratio partition\n  • (b) 4,000 riyals: Divides 12,000 by 3\n  • (c) 5,000 riyals: Approximate guess",
            solution_steps_ar='["B = 2C/3, A = B/2 = C/3","C/3 + 2C/3 + C = 2C = 12,000","C = 6,000 riyals"]',
    tags="ratio,fraction", stage="peak",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        # ── Q115 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.8,
            text_ar="Two cyclists start from the same point. One cycles north at 12 km/h and the other cycles east at 16 km/h. After 2 hours, how far apart are they?",
            option_a="32 km", option_b="36 km", option_c="40 km", option_d="44 km",
            correct_option="c",
            explanation_ar="Given:\n  North at 12 km/h, East at 16 km/h, Time = 2 hours\n\nSolution:\n  North distance = 12 × 2 = 24 km\n  East distance = 16 × 2 = 32 km\n  Distance apart = √(24² + 32²) = √(576 + 1024) = √1600 = 40 km\n\nWhy other options are wrong:\n  • (a) 32 km: Uses only the east distance\n  • (b) 36 km: Computes (24 + 32)/2 × something\n  • (d) 44 km: Adds distances instead of using Pythagorean theorem",
            solution_steps_ar='["North = 24 km, East = 32 km","Distance = √(24² + 32²) = √1600","= 40 km"]',
    tags="speed,number-properties", stage="peak",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        # ── Q116 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.8,
            text_ar="A merchant mixes 20 kg of rice at 30 riyals/kg with 30 kg of rice at 40 riyals/kg. At what price per kg should he sell the mixture to make a 25% profit?",
            option_a="40 riyals/kg", option_b="43.75 riyals/kg", option_c="45 riyals/kg", option_d="46.25 riyals/kg",
            correct_option="c",
            explanation_ar="Given:\n  20 kg at 30 SR/kg, 30 kg at 40 SR/kg, profit = 25%\n\nSolution:\n  Total cost = 20 × 30 + 30 × 40 = 600 + 1,200 = 1,800\n  Total weight = 50 kg\n  Cost per kg = 1,800 ÷ 50 = 36\n  Selling price = 36 × 1.25 = 45 riyals/kg\n\nWhy other options are wrong:\n  • (a) 40 riyals/kg: Uses cost per kg of 32 instead of 36\n  • (b) 43.75 riyals/kg: Uses a profit of about 22%\n  • (d) 46.25 riyals/kg: Uses cost per kg of 37 instead of 36",
            solution_steps_ar='["Cost = 600 + 1,200 = 1,800 for 50 kg","Cost/kg = 36","Sell at 36 × 1.25 = 45 riyals/kg"]',
    tags="mixture,profit,percentage", stage="peak",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        # ── Q117 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.8,
            text_ar="If 30,000 riyals is invested at 10% per annum compound interest compounded annually, what is the amount after 3 years?",
            option_a="39,000 riyals", option_b="39,930 riyals", option_c="39,600 riyals", option_d="40,000 riyals",
            correct_option="b",
            explanation_ar="Given:\n  P = 30,000, r = 10%, t = 3 years\n\nSolution:\n  A = 30,000 × (1.10)³\n  (1.10)³ = 1.331\n  A = 30,000 × 1.331 = 39,930\n\nWhy other options are wrong:\n  • (a) 39,000 riyals: Simple interest (30,000 + 9,000)\n  • (c) 39,600 riyals: Incorrect compounding\n  • (d) 40,000 riyals: Rounds up incorrectly",
            solution_steps_ar='["A = 30,000 × (1.10)³","(1.10)³ = 1.331","A = 39,930 riyals"]',
    tags="compound-interest", stage="peak",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        # ── Q118 ──
        Question(skill_id="quant_arithmetic", question_type="comparison", difficulty=0.7,
            text_ar="Compare:\n\n▸ Column (A): The average of 10, 20, 30, 40, 50\n▸ Column (B): The median of 5, 15, 30, 45, 55",
            option_a="Column (A) is greater", option_b="Column (B) is greater", option_c="The two values are equal", option_d="The relationship cannot be determined",
            correct_option="c",
            explanation_ar="Given:\n  Column A: Average of 10, 20, 30, 40, 50 = 150/5 = 30\n  Column B: Median of 5, 15, 30, 45, 55 = 30\n\nSolution:\n  30 = 30, so they are equal\n\nWhy other options are wrong:\n  • (a) Column (A) is greater: Both equal 30\n  • (b) Column (B) is greater: Both equal 30\n  • (d) The relationship cannot be determined: Both values are fixed",
            solution_steps_ar='["A = (10+20+30+40+50)/5 = 30","B = median = 30","Equal"]',
    tags="average,comparison", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ── Q119 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.6,
            text_ar="The LCM of two numbers is 60 and their GCD is 5. If one number is 15, what is the other?",
            option_a="12", option_b="15", option_c="20", option_d="30",
            correct_option="c",
            explanation_ar="Given:\n  LCM = 60, GCD = 5, one number = 15\n\nSolution:\n  LCM × GCD = product of two numbers\n  60 × 5 = 15 × other\n  300 = 15 × other\n  Other = 300 ÷ 15 = 20\n\nWhy other options are wrong:\n  • (a) 12: GCD(15,12) = 3, not 5\n  • (b) 15: LCM(15,15) = 15, not 60\n  • (d) 30: LCM(15,30) = 30, not 60",
            solution_steps_ar='["LCM × GCD = a × b","60 × 5 = 15 × b","b = 300 ÷ 15 = 20"]',
    tags="lcm-gcd", stage="peak",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        # ── Q120 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.7,
            text_ar="If a number is divisible by both 4 and 6, which of the following must it also be divisible by?",
            option_a="8", option_b="12", option_c="16", option_d="24",
            correct_option="b",
            explanation_ar="Given:\n  Number divisible by 4 and 6\n\nSolution:\n  LCM(4, 6) = 12\n  If a number is divisible by both 4 and 6, it must be divisible by their LCM = 12\n\nWhy other options are wrong:\n  • (a) 8: 12 is divisible by 4 and 6 but not 8\n  • (c) 16: 12 is divisible by 4 and 6 but not 16\n  • (d) 24: 12 is divisible by 4 and 6 but not 24",
            solution_steps_ar='["LCM(4, 6) = 12","Divisible by both 4 and 6 means divisible by 12","Must be divisible by 12"]',
    tags="lcm-gcd,number-properties", stage="peak",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        # ── Q121 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.8,
            text_ar="A, B, and C can complete a work in 10, 15, and 12 days respectively. They start together but C leaves after 2 days. In how many more days will A and B finish the remaining work?",
            option_a="3 days", option_b="4 days", option_c="5 days", option_d="6 days",
            correct_option="a",
            explanation_ar="Given:\n  A: 10 days, B: 15 days, C: 12 days, C leaves after 2 days\n\nSolution:\n  Rates: A=1/10, B=1/15, C=1/12\n  Combined = 6/60 + 4/60 + 5/60 = 15/60 = 1/4\n  Work in 2 days = 2 × 1/4 = 1/2\n  Remaining = 1/2\n  A+B rate = 1/10 + 1/15 = 6/60 + 4/60 = 10/60 = 1/6\n  Days = (1/2) ÷ (1/6) = 3 days\n\nWhy other options are wrong:\n  • (b) 4 days: Overestimates the remaining work\n  • (c) 5 days: Uses A+B rate incorrectly\n  • (d) 6 days: Uses only A's rate for the remaining work",
            solution_steps_ar='["Rates: A=1/10, B=1/15, C=1/12","Together = 1/4 per day, 2 days = 1/2 done","A+B = 1/6 per day, remaining 1/2 takes 3 days"]',
    tags="work-rate", stage="peak",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        # ── Q122 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.4,
            text_ar="If 1 euro = 4.20 SAR, how many euros do you receive for 840 SAR?",
            option_a="200 euros", option_b="180 euros", option_c="210 euros", option_d="250 euros",
            correct_option="a",
            explanation_ar="Given:\n  1 euro = 4.20 SAR, amount = 840 SAR\n\nSolution:\n  Euros = 840 ÷ 4.20 = 200 euros\n\nWhy other options are wrong:\n  • (b) 180 euros: Divides 840 by 4.67\n  • (c) 210 euros: Divides 840 by 4.00 instead of 4.20\n  • (d) 250 euros: Divides 840 by 3.36",
            solution_steps_ar='["Euros = SAR ÷ rate","= 840 ÷ 4.20","= 200 euros"]',
    tags="currency", stage="peak",
    rating_clarity=5, rating_cognitive=3, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.43),

        # ── Q123 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.5,
            text_ar="Estimate the value of √(99) to the nearest whole number.",
            option_a="9", option_b="12", option_c="11", option_d="10",
            correct_option="d",
            explanation_ar="Given:\n  √99\n\nSolution:\n  9² = 81, 10² = 100\n  99 is very close to 100\n  √99 ≈ 9.95 ≈ 10\n\nWhy other options are wrong:\n  • (a) 9: 9² = 81, which is 18 away from 99\n  • (c) 11: 11² = 121, too far from 99\n  • (b) 12: 12² = 144, much too far from 99",
            solution_steps_ar='["9² = 81, 10² = 100","99 is closest to 100","√99 ≈ 10"]',
    tags="estimation,number-properties", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=4, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q124 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.6,
            text_ar="A boat can travel 20 km/h in still water. The river current flows at 4 km/h. How long does it take the boat to travel 48 km upstream?",
            option_a="2 hours", option_b="2.4 hours", option_c="3 hours", option_d="4 hours",
            correct_option="c",
            explanation_ar="Given:\n  Boat speed = 20 km/h, Current = 4 km/h, Distance = 48 km upstream\n\nSolution:\n  Upstream speed = 20 − 4 = 16 km/h\n  Time = 48 ÷ 16 = 3 hours\n\nWhy other options are wrong:\n  • (a) 2 hours: Uses 48 ÷ 24 (downstream speed)\n  • (b) 2.4 hours: Uses 48 ÷ 20 (still water speed)\n  • (d) 4 hours: Uses 48 ÷ 12 (subtracts 8 instead of 4)",
            solution_steps_ar='["Upstream speed = 20 − 4 = 16 km/h","Time = 48 ÷ 16","= 3 hours"]',
    tags="speed", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ── Q125 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.7,
            text_ar="The product of two numbers is 192. If their ratio is 4:3, what is the larger number?",
            option_a="12", option_b="14", option_c="18", option_d="16",
            correct_option="d",
            explanation_ar="Given:\n  Product = 192, Ratio = 4:3\n\nSolution:\n  Let numbers be 4x and 3x\n  4x × 3x = 192\n  12x² = 192\n  x² = 16, x = 4\n  Larger = 4 × 4 = 16\n\nWhy other options are wrong:\n  • (a) 12: This is the smaller number (3 × 4)\n  • (b) 14: Not a multiple of 4\n  • (c) 18: Uses x = 4.5",
            solution_steps_ar='["Let numbers = 4x and 3x","12x² = 192, x² = 16, x = 4","Larger = 4 × 4 = 16"]',
    tags="ratio,number-properties", stage="peak",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        # ── Q126 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.8,
            text_ar="A shopkeeper sells an article at 10% profit. If he had bought it for 10% less and sold it for 25 riyals more, he would have gained 25% profit. What is the original cost price?",
            option_a="800 riyals", option_b="900 riyals", option_c="1,000 riyals", option_d="1,200 riyals",
            correct_option="c",
            explanation_ar="Given:\n  Sells at 10% profit. If cost 10% less, sell for 25 more → 25% profit\n\nSolution:\n  Let CP = x\n  SP = 1.10x\n  New CP = 0.90x\n  New SP = 1.10x + 25\n  New SP must also = 1.25 × 0.90x = 1.125x\n  1.10x + 25 = 1.125x\n  0.025x = 25\n  x = 1,000 riyals\n\nWhy other options are wrong:\n  • (a) 800 riyals: 0.025 × 800 = 20, not 25\n  • (b) 900 riyals: 0.025 × 900 = 22.5, not 25\n  • (d) 1,200 riyals: 0.025 × 1,200 = 30, not 25",
            solution_steps_ar='["SP = 1.10x, New CP = 0.90x","New SP = 1.10x + 25 = 1.125x","0.025x = 25, x = 1,000 riyals"]',
    tags="profit,percentage", stage="peak",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        # ── Q127 ──
        Question(skill_id="quant_arithmetic", question_type="comparison", difficulty=0.7,
            text_ar="Compare:\n\n▸ Column (A): Simple interest on 5,000 at 8% for 3 years\n▸ Column (B): 1,250",
            option_a="Column (A) is greater", option_b="Column (B) is greater", option_c="The two values are equal", option_d="The relationship cannot be determined",
            correct_option="b",
            explanation_ar="Given:\n  Column A: SI = P×R×T/100 = 5,000 × 8 × 3/100 = 1,200\n  Column B: 1,250\n\nSolution:\n  1,200 < 1,250, so Column B is greater\n\nWhy other options are wrong:\n  • (a) Column (A) is greater: 1,200 < 1,250\n  • (c) The two values are equal: 1,200 ≠ 1,250\n  • (d) The relationship cannot be determined: Both values are fixed",
            solution_steps_ar='["A = 5,000 × 8% × 3 = 1,200","B = 1,250","1,200 < 1,250, B is greater"]',
    tags="compound-interest,comparison", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ── Q128 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.3,
            text_ar="What is 0.75 expressed as a fraction in simplest form?",
            option_a="3/5", option_b="3/4", option_c="7/10", option_d="4/5",
            correct_option="b",
            explanation_ar="Given:\n  0.75\n\nSolution:\n  0.75 = 75/100 = 3/4\n\nWhy other options are wrong:\n  • (a) 3/5: 3/5 = 0.60, not 0.75\n  • (c) 7/10: 7/10 = 0.70, not 0.75\n  • (d) 4/5: 4/5 = 0.80, not 0.75",
            solution_steps_ar='["0.75 = 75/100","Simplify: 75/100 = 3/4"]',
    tags="fraction", stage="foundation",
    rating_clarity=5, rating_cognitive=3, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=3, rating_overall=4.29),

        # ── Q129 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.2,
            text_ar="What is 15% of 600?",
            option_a="75", option_b="80", option_c="90", option_d="95",
            correct_option="c",
            explanation_ar="Given:\n  15% of 600\n\nSolution:\n  15/100 × 600 = 90\n\nWhy other options are wrong:\n  • (a) 75: Computes 12.5% of 600\n  • (b) 80: Computes 13.3% of 600\n  • (d) 95: Adds 5 to the correct answer",
            solution_steps_ar='["15% × 600 = 0.15 × 600","= 90"]',
    tags="percentage", stage="foundation",
    rating_clarity=5, rating_cognitive=3, rating_fairness=5, rating_distractors=4, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=3, rating_overall=4.14),

        # ── Q130 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.4,
            text_ar="A man can row 6 km/h in still water. If the river current is 2 km/h, what is his speed downstream?",
            option_a="4 km/h", option_b="6 km/h", option_c="8 km/h", option_d="10 km/h",
            correct_option="c",
            explanation_ar="Given:\n  Still water speed = 6 km/h, Current = 2 km/h\n\nSolution:\n  Downstream speed = still water + current = 6 + 2 = 8 km/h\n\nWhy other options are wrong:\n  • (a) 4 km/h: Subtracts current (upstream speed)\n  • (b) 6 km/h: Ignores current entirely\n  • (d) 10 km/h: Adds current twice",
            solution_steps_ar='["Downstream = still water + current","= 6 + 2","= 8 km/h"]',
    tags="speed", stage="foundation",
    rating_clarity=5, rating_cognitive=3, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.43),

        # ── Q131 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.6,
            text_ar="In a group of 60 students, 25 are boys. If 5 more boys join the group, what percentage of the total group are boys now? (Round to 2 decimal places.)",
            option_a="40%", option_b="43.08%", option_c="46.15%", option_d="50%",
            correct_option="c",
            explanation_ar="Given:\n  Total = 60, Boys = 25, 5 more boys join\n\nSolution:\n  New boys = 25 + 5 = 30\n  New total = 60 + 5 = 65\n  Percentage = 30/65 × 100 ≈ 46.15%\n\nWhy other options are wrong:\n  • (a) 40%: Uses the original percentage before new boys joined\n  • (b) 43.08%: Divides by wrong total\n  • (d) 50%: Assumes half are boys",
            solution_steps_ar='["Original: 25 boys out of 60","After 5 join: 30 boys out of 65","30/65 × 100 ≈ 46.15%"]',
    tags="percentage", stage="peak",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        # ── Q132 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.7,
            text_ar="The ages of three brothers are consecutive odd numbers. If the sum of their ages is 75, what is the age of the oldest brother?",
            option_a="23", option_b="25", option_c="29", option_d="27",
            correct_option="d",
            explanation_ar="Given:\n  Three consecutive odd numbers, sum = 75\n\nSolution:\n  Let the numbers be n, n+2, n+4\n  3n + 6 = 75\n  3n = 69\n  n = 23\n  Oldest = 23 + 4 = 27\n\nWhy other options are wrong:\n  • (a) 23: This is the youngest brother\n  • (b) 25: This is the middle brother\n  • (c) 29: Adds 6 to 23 instead of 4",
            solution_steps_ar='["n + (n+2) + (n+4) = 75","3n + 6 = 75, n = 23","Oldest = 23 + 4 = 27"]',
    tags="age,number-properties", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ── Q133 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.8,
            text_ar="A tank is filled by pipe A in 8 hours and by pipe B in 12 hours. Pipe C can empty the full tank in 24 hours. If all three pipes are opened simultaneously, how long will it take to fill the tank?",
            option_a="4 hours", option_b="6 hours", option_c="8 hours", option_d="10 hours",
            correct_option="b",
            explanation_ar="Given:\n  A fills in 8h, B fills in 12h, C empties in 24h\n\nSolution:\n  Net rate = 1/8 + 1/12 − 1/24\n  = 3/24 + 2/24 − 1/24 = 4/24 = 1/6\n  Time = 6 hours\n\nWhy other options are wrong:\n  • (a) 4 hours: Ignores the emptying pipe\n  • (c) 8 hours: Uses only pipe A's rate\n  • (d) 10 hours: Subtracts too much for the drain pipe",
            solution_steps_ar='["Net rate = 1/8 + 1/12 − 1/24","= 3/24 + 2/24 − 1/24 = 4/24 = 1/6","Time = 6 hours"]',
    tags="work-rate", stage="peak",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        # ── Q134 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.3,
            text_ar="What is the next term in the sequence: 5, 10, 20, 40, ...?",
            option_a="50", option_b="60", option_c="70", option_d="80",
            correct_option="d",
            explanation_ar="Given:\n  Sequence: 5, 10, 20, 40, ...\n\nSolution:\n  Each term doubles: 5×2=10, 10×2=20, 20×2=40\n  Next = 40 × 2 = 80\n\nWhy other options are wrong:\n  • (a) 50: Adds 10 to 40 instead of doubling\n  • (b) 60: Adds 20 to 40 instead of doubling\n  • (c) 70: Adds 30 to 40 instead of doubling",
            solution_steps_ar='["Pattern: each term × 2","10/5=2, 20/10=2, 40/20=2","Next = 40 × 2 = 80"]',
    tags="sequences", stage="building",
    rating_clarity=5, rating_cognitive=3, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.43),

        # ── Q135 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.5,
            text_ar="The cost of 5 pens and 3 pencils is 57 riyals. The cost of 3 pens and 5 pencils is 47 riyals. What is the cost of 1 pen?",
            option_a="9 riyals", option_b="8 riyals", option_c="6 riyals", option_d="10 riyals",
            correct_option="a",
            explanation_ar="Given:\n  5P + 3C = 57 ... (1)\n  3P + 5C = 47 ... (2)\n\nSolution:\n  Add (1)+(2): 8P + 8C = 104 → P + C = 13\n  Subtract (2) from (1): 2P − 2C = 10 → P − C = 5\n  P + C = 13 and P − C = 5\n  2P = 18, P = 9\n\nWhy other options are wrong:\n  • (c) 6 riyals: Confuses pen with pencil (C = 4, not the answer)\n  • (b) 8 riyals: Arithmetic error in solving\n  • (d) 10 riyals: Adds 1 extra to the correct answer",
            solution_steps_ar='["5P+3C=57, 3P+5C=47","Add: 8P+8C=104 → P+C=13","Subtract: 2P−2C=10 → P=9"]',
    tags="proportion", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        # ── Q136 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.6,
            text_ar="A worker earns 45 riyals per hour for regular hours and 67.50 riyals per hour for overtime. If he works 40 regular hours and 8 overtime hours, what are his total earnings?",
            option_a="2,160 riyals", option_b="2,340 riyals", option_c="2,250 riyals", option_d="2,430 riyals",
            correct_option="b",
            explanation_ar="Given:\n  Regular: 45 SR/h × 40h, Overtime: 67.50 SR/h × 8h\n\nSolution:\n  Regular pay = 45 × 40 = 1,800\n  Overtime pay = 67.50 × 8 = 540\n  Total = 1,800 + 540 = 2,340\n\nWhy other options are wrong:\n  • (a) 2,160 riyals: Uses 45 × 48 = 2,160 (no overtime rate)\n  • (c) 2,250 riyals: Uses 45 × 50 = 2,250\n  • (d) 2,430 riyals: Uses a higher overtime rate",
            solution_steps_ar='["Regular = 45 × 40 = 1,800","Overtime = 67.50 × 8 = 540","Total = 2,340 riyals"]',
    tags="proportion,currency", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ── Q137 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.7,
            text_ar="A sum of money doubles in 5 years at simple interest. What is the rate of interest per annum?",
            option_a="10%", option_b="15%", option_c="20%", option_d="25%",
            correct_option="c",
            explanation_ar="Given:\n  Money doubles in 5 years (simple interest)\n\nSolution:\n  If P doubles, Amount = 2P\n  Interest = 2P − P = P\n  SI = P × R × T / 100\n  P = P × R × 5 / 100\n  100 = 5R\n  R = 20%\n\nWhy other options are wrong:\n  • (a) 10%: At 10%, money doubles in 10 years, not 5\n  • (b) 15%: At 15%, money doubles in 6.67 years\n  • (d) 25%: At 25%, money doubles in 4 years",
            solution_steps_ar='["Interest = P (to double)","P = P × R × 5/100","R = 100/5 = 20%"]',
    tags="compound-interest,percentage", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ── Q138 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.8,
            text_ar="In a mixture of 80 litres, the ratio of milk to water is 7:3. How much milk must be added so that the ratio becomes 4:1?",
            option_a="32 litres", option_b="36 litres", option_c="40 litres", option_d="48 litres",
            correct_option="c",
            explanation_ar="Given:\n  Total = 80 L, Milk:Water = 7:3\n\nSolution:\n  Milk = 80 × 7/10 = 56 L\n  Water = 80 × 3/10 = 24 L\n  Let x litres of milk be added\n  (56 + x)/24 = 4\n  56 + x = 96\n  x = 40 litres\n\nWhy other options are wrong:\n  • (a) 32 litres: (56+32)/24 = 88/24 ≈ 3.67, not 4\n  • (b) 36 litres: (56+36)/24 = 92/24 ≈ 3.83, not 4\n  • (d) 48 litres: (56+48)/24 = 104/24 ≈ 4.33, not 4",
            solution_steps_ar='["Milk = 56 L, Water = 24 L","(56+x)/24 = 4","x = 96 − 56 = 40 litres"]',
    tags="mixture,ratio", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        # ── Q139 ──
        Question(skill_id="quant_arithmetic", question_type="comparison", difficulty=0.8,
            text_ar="Compare:\n\n▸ Column (A): Compound interest on 10,000 at 10% for 2 years\n▸ Column (B): Simple interest on 10,000 at 10% for 2 years + 100",
            option_a="Column (A) is greater", option_b="Column (B) is greater", option_c="The two values are equal", option_d="The relationship cannot be determined",
            correct_option="c",
            explanation_ar="Given:\n  Column A: CI = 10,000 × (1.10)² − 10,000 = 12,100 − 10,000 = 2,100\n  Column B: SI = 10,000 × 0.10 × 2 = 2,000; 2,000 + 100 = 2,100\n\nSolution:\n  2,100 = 2,100, equal\n\nWhy other options are wrong:\n  • (a) Column (A) is greater: Both equal 2,100\n  • (b) Column (B) is greater: Both equal 2,100\n  • (d) The relationship cannot be determined: Both values are fixed",
            solution_steps_ar='["CI = 12,100 − 10,000 = 2,100","SI + 100 = 2,000 + 100 = 2,100","Equal"]',
    tags="compound-interest,comparison", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        # ── Q140 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.4,
            text_ar="A 240 cm ribbon is cut into pieces in the ratio 3:5. What is the length of the shorter piece?",
            option_a="80 cm", option_b="120 cm", option_c="100 cm", option_d="90 cm",
            correct_option="d",
            explanation_ar="Given:\n  Total = 240 cm, Ratio = 3:5\n\nSolution:\n  Total parts = 3 + 5 = 8\n  One part = 240 ÷ 8 = 30\n  Shorter = 3 × 30 = 90 cm\n\nWhy other options are wrong:\n  • (a) 80 cm: Divides 240 by 3 = 80\n  • (c) 100 cm: Approximately half of 240 minus a bit\n  • (b) 120 cm: Divides 240 by 2 (assumes equal parts)",
            solution_steps_ar='["Parts = 3+5 = 8","One part = 240/8 = 30","Shorter = 3 × 30 = 90 cm"]',
    tags="ratio", stage="mock",
    rating_clarity=5, rating_cognitive=3, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.43),

        # ── Q141 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.5,
            text_ar="A shopkeeper buys 15 items for 600 riyals and sells 12 items for 600 riyals. What is his profit percentage?",
            option_a="15%", option_b="25%", option_c="20%", option_d="30%",
            correct_option="b",
            explanation_ar="Given:\n  CP of 15 items = 600, SP of 12 items = 600\n\nSolution:\n  CP per item = 600/15 = 40\n  SP per item = 600/12 = 50\n  Profit per item = 50 − 40 = 10\n  Profit % = 10/40 × 100 = 25%\n\nWhy other options are wrong:\n  • (a) 15%: Uses wrong division\n  • (c) 20%: Computes 10/50 × 100 = 20% (divides by SP instead of CP)\n  • (d) 30%: Overestimates the profit margin",
            solution_steps_ar='["CP/item = 600/15 = 40","SP/item = 600/12 = 50","Profit % = 10/40 × 100 = 25%"]',
    tags="profit", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        # ── Q142 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.6,
            text_ar="If the population of a city increases by 5% every year and the current population is 200,000, what will be the population after 2 years?",
            option_a="210,000", option_b="220,000", option_c="221,000", option_d="220,500",
            correct_option="d",
            explanation_ar="Given:\n  P = 200,000, Rate = 5% per year, Time = 2 years\n\nSolution:\n  After 2 years = 200,000 × (1.05)²\n  = 200,000 × 1.1025\n  = 220,500\n\nWhy other options are wrong:\n  • (a) 210,000: Growth for 1 year only\n  • (b) 220,000: Simple growth (200,000 + 2 × 10,000)\n  • (c) 221,000: Slightly overestimates the compound growth",
            solution_steps_ar='["Population = 200,000 × (1.05)²","= 200,000 × 1.1025","= 220,500"]',
    tags="compound-interest,percentage", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        # ── Q143 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.7,
            text_ar="A train 200 m long passes another train 150 m long running in the opposite direction in 10 seconds. If the speed of the first train is 54 km/h, what is the speed of the second train?",
            option_a="36 km/h", option_b="54 km/h", option_c="72 km/h", option_d="90 km/h",
            correct_option="c",
            explanation_ar="Given:\n  Train 1: 200 m, 54 km/h; Train 2: 150 m; Time = 10 s (opposite direction)\n\nSolution:\n  Total distance = 200 + 150 = 350 m\n  Relative speed = 350/10 = 35 m/s\n  Train 1 speed = 54 km/h = 15 m/s\n  Train 2 speed = 35 − 15 = 20 m/s = 72 km/h\n\nWhy other options are wrong:\n  • (a) 36 km/h: Gets 10 m/s for train 2\n  • (b) 54 km/h: Assumes same speed as train 1\n  • (d) 90 km/h: Gets 25 m/s for train 2",
            solution_steps_ar='["Total distance = 350 m, Time = 10 s","Relative speed = 35 m/s","Train 2 = 35 − 15 = 20 m/s = 72 km/h"]',
    tags="speed,unit-conversion", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        # ── Q144 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.8,
            text_ar="The average weight of 8 people increases by 2.5 kg when a new person replaces one who weighs 65 kg. What is the weight of the new person?",
            option_a="75 kg", option_b="80 kg", option_c="85 kg", option_d="90 kg",
            correct_option="c",
            explanation_ar="Given:\n  8 people, average increases by 2.5 kg, replaced person = 65 kg\n\nSolution:\n  Total weight increase = 8 × 2.5 = 20 kg\n  New person weight = 65 + 20 = 85 kg\n\nWhy other options are wrong:\n  • (a) 75 kg: Adds only 10 to 65 (4 × 2.5)\n  • (b) 80 kg: Adds 15 to 65 (6 × 2.5)\n  • (d) 90 kg: Adds 25 to 65 (10 × 2.5)",
            solution_steps_ar='["Total increase = 8 × 2.5 = 20 kg","New weight = 65 + 20","= 85 kg"]',
    tags="average", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        # ── Q145 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.3,
            text_ar="What fraction of a day is 6 hours?",
            option_a="1/6", option_b="1/4", option_c="1/3", option_d="1/2",
            correct_option="b",
            explanation_ar="Given:\n  6 hours out of 24 hours\n\nSolution:\n  6/24 = 1/4\n\nWhy other options are wrong:\n  • (a) 1/6: Would be 4 hours, not 6\n  • (c) 1/3: Would be 8 hours, not 6\n  • (d) 1/2: Would be 12 hours, not 6",
            solution_steps_ar='["1 day = 24 hours","6/24 = 1/4"]',
    tags="fraction,time", stage="building",
    rating_clarity=5, rating_cognitive=3, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=3, rating_overall=4.29),

        # ── Q146 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.4,
            text_ar="If the selling price of an article is 4/5 of its cost price, what is the loss percentage?",
            option_a="10%", option_b="15%", option_c="20%", option_d="25%",
            correct_option="c",
            explanation_ar="Given:\n  SP = 4/5 × CP\n\nSolution:\n  Loss = CP − SP = CP − 4CP/5 = CP/5\n  Loss % = (CP/5)/CP × 100 = 20%\n\nWhy other options are wrong:\n  • (a) 10%: SP would be 9/10 of CP\n  • (b) 15%: SP would be 17/20 of CP\n  • (d) 25%: SP would be 3/4 of CP",
            solution_steps_ar='["SP = 4/5 × CP","Loss = CP − 4CP/5 = CP/5","Loss % = 20%"]',
    tags="profit,fraction", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q147 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.5,
            text_ar="How many numbers between 1 and 100 (inclusive) are divisible by both 3 and 5?",
            option_a="5", option_b="6", option_c="7", option_d="10",
            correct_option="b",
            explanation_ar="Given:\n  Numbers 1-100 divisible by both 3 and 5\n\nSolution:\n  Divisible by both 3 and 5 = divisible by LCM(3,5) = 15\n  Numbers: 15, 30, 45, 60, 75, 90\n  Count = 100 ÷ 15 = 6.67 → 6 numbers\n\nWhy other options are wrong:\n  • (a) 5: Misses one number\n  • (c) 7: Includes 105 which is beyond 100\n  • (d) 10: Counts multiples of 10 instead of 15",
            solution_steps_ar='["LCM(3,5) = 15","Multiples of 15 up to 100: 15,30,45,60,75,90","Count = 6"]',
    tags="lcm-gcd,number-properties", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ── Q148 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.6,
            text_ar="An investor puts 40% of his savings in stocks and the rest in bonds. If his stock investment grows by 15% and bond investment grows by 8%, what is his overall growth percentage?",
            option_a="10.8%", option_b="10%", option_c="11.2%", option_d="12%",
            correct_option="a",
            explanation_ar="Given:\n  Stocks: 40% of savings, growth 15%; Bonds: 60%, growth 8%\n\nSolution:\n  Overall growth = 0.40 × 15% + 0.60 × 8%\n  = 6% + 4.8% = 10.8%\n\nWhy other options are wrong:\n  • (b) 10%: Rounds down incorrectly\n  • (c) 11.2%: Swaps the weights (60% stocks, 40% bonds)\n  • (d) 12%: Averages 15% and 8% directly as (15+8)/2 ≈ 11.5 then rounds",
            solution_steps_ar='["Stocks: 0.40 × 15% = 6%","Bonds: 0.60 × 8% = 4.8%","Total = 10.8%"]',
    tags="percentage,average", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        # ── Q149 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.7,
            text_ar="The difference between compound interest and simple interest on a sum of 8,000 for 2 years at 5% per annum is:",
            option_a="10 riyals", option_b="15 riyals", option_c="25 riyals", option_d="20 riyals",
            correct_option="d",
            explanation_ar="Given:\n  P = 8,000, R = 5%, T = 2 years\n\nSolution:\n  SI = 8,000 × 5 × 2/100 = 800\n  CI = 8,000 × (1.05)² − 8,000 = 8,000 × 1.1025 − 8,000 = 8,820 − 8,000 = 820\n  Difference = 820 − 800 = 20\n\nAlternatively: Diff = P × (R/100)² = 8,000 × 0.0025 = 20\n\nWhy other options are wrong:\n  • (a) 10 riyals: Uses P = 4,000\n  • (b) 15 riyals: Uses wrong rate\n  • (c) 25 riyals: Uses P = 10,000",
            solution_steps_ar='["SI = 800, CI = 820","Difference = 820 − 800 = 20 riyals"]',
    tags="compound-interest", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        # ── Q150 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.8,
            text_ar="A and B together can complete a work in 12 days. B and C together can complete it in 15 days. A and C together can complete it in 20 days. How long will all three take working together?",
            option_a="8 days", option_b="10 days", option_c="12 days", option_d="15 days",
            correct_option="b",
            explanation_ar="Given:\n  A+B=12 days, B+C=15 days, A+C=20 days\n\nSolution:\n  Rates: A+B=1/12, B+C=1/15, A+C=1/20\n  Add all: 2(A+B+C) = 1/12 + 1/15 + 1/20\n  LCM(12,15,20) = 60\n  = 5/60 + 4/60 + 3/60 = 12/60 = 1/5\n  A+B+C = 1/10\n  Time = 10 days\n\nWhy other options are wrong:\n  • (a) 8 days: Underestimates the time\n  • (c) 12 days: Uses only A+B rate\n  • (d) 15 days: Uses only B+C rate",
            solution_steps_ar='["2(A+B+C) = 1/12+1/15+1/20 = 12/60 = 1/5","A+B+C = 1/10","Time = 10 days"]',
    tags="work-rate", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        # ── Q151 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.2,
            text_ar="What is 50% of 84?",
            option_a="34", option_b="42", option_c="48", option_d="52",
            correct_option="b",
            explanation_ar="Given:\n  50% of 84\n\nSolution:\n  50% × 84 = 84/2 = 42\n\nWhy other options are wrong:\n  • (a) 34: Subtracts 50 from 84\n  • (c) 48: Computes 84 × 0.57\n  • (d) 52: Adds 10 to 42",
            solution_steps_ar='["50% of 84 = 84 ÷ 2","= 42"]',
    tags="percentage", stage="foundation",
    rating_clarity=5, rating_cognitive=2, rating_fairness=5, rating_distractors=4, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=3, rating_overall=4.14),

        # ── Q152 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.3,
            text_ar="A recipe requires flour and sugar in the ratio 5:2. If you use 300 grams of flour, how much sugar do you need?",
            option_a="60 grams", option_b="100 grams", option_c="120 grams", option_d="150 grams",
            correct_option="c",
            explanation_ar="Given:\n  Flour:Sugar = 5:2, Flour = 300 g\n\nSolution:\n  One part = 300 ÷ 5 = 60 g\n  Sugar = 2 × 60 = 120 g\n\nWhy other options are wrong:\n  • (a) 60 grams: One part only, not two\n  • (b) 100 grams: Divides 300 by 3 instead of 5/2\n  • (d) 150 grams: Divides 300 by 2",
            solution_steps_ar='["One part = 300 ÷ 5 = 60 g","Sugar = 2 × 60 = 120 grams"]',
    tags="ratio,proportion", stage="foundation",
    rating_clarity=5, rating_cognitive=3, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.43),

        # ── Q153 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.4,
            text_ar="5/6 − 1/3 = ?",
            option_a="4/6", option_b="1/2", option_c="4/3", option_d="2/3",
            correct_option="b",
            explanation_ar="Given:\n  5/6 − 1/3\n\nSolution:\n  1/3 = 2/6\n  5/6 − 2/6 = 3/6 = 1/2\n\nWhy other options are wrong:\n  • (a) 4/6: Subtracts numerators only (5−1)/6, ignoring different denominators\n  • (c) 4/3: Subtracts denominators (5−1)/(6−3)\n  • (d) 2/3: Converts 5/6 to 4/6 incorrectly",
            solution_steps_ar='["Convert: 1/3 = 2/6","5/6 − 2/6 = 3/6 = 1/2"]',
    tags="fraction", stage="building",
    rating_clarity=5, rating_cognitive=3, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.43),

        # ── Q154 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.5,
            text_ar="A bus leaves City A at 9:00 AM traveling at 60 km/h. Another bus leaves City A at 10:00 AM traveling at 80 km/h on the same route. At what time will the second bus catch the first?",
            option_a="12:00 PM", option_b="1:00 PM", option_c="2:00 PM", option_d="3:00 PM",
            correct_option="b",
            explanation_ar="Given:\n  Bus 1: 60 km/h leaves at 9:00; Bus 2: 80 km/h leaves at 10:00\n\nSolution:\n  By 10:00, Bus 1 has traveled 60 km\n  Relative speed = 80 − 60 = 20 km/h\n  Time to close 60 km gap = 60/20 = 3 hours after 10:00\n  Catch-up time = 1:00 PM\n\nWhy other options are wrong:\n  • (a) 12:00 PM: Only 2 hours gap closed = 40 km, Bus 1 ahead by 20\n  • (c) 2:00 PM: Bus 2 would have passed Bus 1 already\n  • (d) 3:00 PM: Way too late",
            solution_steps_ar='["Bus 1 lead at 10AM = 60 km","Relative speed = 80−60 = 20 km/h","Time = 60/20 = 3h after 10AM = 1:00 PM"]',
    tags="speed,time", stage="peak",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        # ── Q155 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.6,
            text_ar="A man bought 2 shirts at 400 riyals each. He sold one at 25% profit and the other at 25% loss. What is his overall gain or loss?",
            option_a="No gain, no loss", option_b="25 riyals loss", option_c="50 riyals loss", option_d="25 riyals gain",
            correct_option="a",
            explanation_ar="Given:\n  2 shirts at 400 each. One sold at 25% profit, one at 25% loss.\n\nSolution:\n  Total CP = 400 + 400 = 800\n  SP of first = 400 × 1.25 = 500\n  SP of second = 400 × 0.75 = 300\n  Total SP = 500 + 300 = 800\n  Net = 800 − 800 = 0 (no gain, no loss)\n\nWhy other options are wrong:\n  • (b) 25 riyals loss: Confuses with the case when SP is the same\n  • (c) 50 riyals loss: Confuses with the case when selling prices are equal\n  • (d) 25 riyals gain: Incorrect calculation",
            solution_steps_ar='["SP1 = 400 × 1.25 = 500","SP2 = 400 × 0.75 = 300","Total SP = 800 = Total CP, no gain/loss"]',
    tags="profit,percentage", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ── Q156 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.7,
            text_ar="If x inversely proportional to y, and x = 6 when y = 8, what is x when y = 12?",
            option_a="3", option_b="4", option_c="9", option_d="16",
            correct_option="b",
            explanation_ar="Given:\n  x ∝ 1/y, x=6 when y=8\n\nSolution:\n  k = x × y = 6 × 8 = 48\n  When y = 12: x = 48/12 = 4\n\nWhy other options are wrong:\n  • (a) 3: Divides 48 by 16 instead of 12\n  • (c) 9: Uses direct proportion (6 × 12/8)\n  • (d) 16: Multiplies instead of dividing",
            solution_steps_ar='["k = xy = 6 × 8 = 48","When y=12: x = 48/12","= 4"]',
    tags="proportion", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ── Q157 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.8,
            text_ar="Three taps A, B, and C can fill a pool. A alone takes 10 hours, B alone takes 20 hours, and C alone takes 25 hours. If A runs for 2 hours alone, then B joins for 3 more hours, how much work remains for C to finish?",
            option_a="3/20", option_b="7/20", option_c="9/20", option_d="11/20",
            correct_option="b",
            explanation_ar="Given:\n  A: 10h, B: 20h, C: 25h\n\nSolution:\n  A alone 2 hours: 2/10 = 1/5\n  A+B for 3 hours: 3 × (1/10 + 1/20) = 3 × 3/20 = 9/20\n  Total done = 1/5 + 9/20 = 4/20 + 9/20 = 13/20\n  Remaining = 1 − 13/20 = 7/20\n\nWhy other options are wrong:\n  • (a) 3/20: Underestimates remaining work\n  • (c) 9/20: Forgets A's solo work\n  • (d) 11/20: Computes A+B rate incorrectly",
            solution_steps_ar='["A alone 2h = 2/10 = 1/5","A+B 3h = 3×(3/20) = 9/20","Done = 4/20+9/20=13/20, Remaining = 7/20"]',
    tags="work-rate", stage="peak",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        # ── Q158 ──
        Question(skill_id="quant_arithmetic", question_type="comparison", difficulty=0.5,
            text_ar="Compare:\n\n▸ Column (A): 0.125 × 800\n▸ Column (B): 12.5% of 800",
            option_a="Column (A) is greater", option_b="Column (B) is greater", option_c="The two values are equal", option_d="The relationship cannot be determined",
            correct_option="c",
            explanation_ar="Given:\n  Column A: 0.125 × 800 = 100\n  Column B: 12.5% × 800 = 0.125 × 800 = 100\n\nSolution:\n  100 = 100, equal\n\nWhy other options are wrong:\n  • (a) Column (A) is greater: Both equal 100\n  • (b) Column (B) is greater: Both equal 100\n  • (d) The relationship cannot be determined: Both values are fixed",
            solution_steps_ar='["A = 0.125 × 800 = 100","B = 12.5% × 800 = 100","Equal"]',
    tags="percentage,fraction,comparison", stage="mock",
    rating_clarity=5, rating_cognitive=3, rating_fairness=5, rating_distractors=4, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=3, rating_overall=4.29),

        # ── Q159 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.4,
            text_ar="How many seconds are in 2 hours and 15 minutes?",
            option_a="7,200 seconds", option_b="7,500 seconds", option_c="8,100 seconds", option_d="8,400 seconds",
            correct_option="c",
            explanation_ar="Given:\n  2 hours 15 minutes\n\nSolution:\n  2 hours = 120 minutes\n  Total = 120 + 15 = 135 minutes\n  135 × 60 = 8,100 seconds\n\nWhy other options are wrong:\n  • (a) 7,200 seconds: Only 2 hours (120 × 60), ignores 15 minutes\n  • (b) 7,500 seconds: Adds only 5 minutes (7,200 + 300)\n  • (d) 8,400 seconds: Adds 20 minutes instead of 15 (7,200 + 1,200)",
            solution_steps_ar='["2h 15min = 135 minutes","135 × 60 = 8,100 seconds"]',
    tags="time,unit-conversion", stage="building",
    rating_clarity=5, rating_cognitive=3, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.43),

        # ── Q160 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.3,
            text_ar="Estimate: 197 + 304 + 498 ≈ ?",
            option_a="900", option_b="1,000", option_c="1,100", option_d="1,200",
            correct_option="b",
            explanation_ar="Given:\n  197 + 304 + 498\n\nSolution:\n  Round: 200 + 300 + 500 = 1,000\n  Exact: 197 + 304 + 498 = 999\n  Nearest hundred = 1,000\n\nWhy other options are wrong:\n  • (a) 900: Underestimates all three numbers\n  • (c) 1,100: Overestimates significantly\n  • (d) 1,200: Far too high",
            solution_steps_ar='["197 ≈ 200, 304 ≈ 300, 498 ≈ 500","200 + 300 + 500 = 1,000"]',
    tags="estimation", stage="building",
    rating_clarity=5, rating_cognitive=3, rating_fairness=5, rating_distractors=4, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=3, rating_overall=4.14),

        # ── Q161 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.7,
            text_ar="The average of 6 numbers is 42. If each number is increased by 3, what is the new average?",
            option_a="42", option_b="43", option_c="45", option_d="48",
            correct_option="c",
            explanation_ar="Given:\n  Average of 6 numbers = 42, each increased by 3\n\nSolution:\n  When each number increases by 3, the average also increases by 3\n  New average = 42 + 3 = 45\n\nWhy other options are wrong:\n  • (a) 42: Assumes the average stays the same\n  • (b) 43: Adds 3/3 = 1 instead of 3\n  • (d) 48: Adds 6 instead of 3 (multiplies 3 by number of items then divides wrong)",
            solution_steps_ar='["Original average = 42","Each increased by 3","New average = 42 + 3 = 45"]',
    tags="average", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ── Q162 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.8,
            text_ar="A cistern is normally filled in 8 hours, but due to a leak at the bottom, it takes 10 hours. If the cistern is full, how long will it take the leak to empty it?",
            option_a="20 hours", option_b="30 hours", option_c="40 hours", option_d="50 hours",
            correct_option="c",
            explanation_ar="Given:\n  Fill without leak: 8h, Fill with leak: 10h\n\nSolution:\n  Fill rate = 1/8, Net rate with leak = 1/10\n  Leak rate = 1/8 − 1/10 = 5/40 − 4/40 = 1/40\n  Time to empty = 40 hours\n\nWhy other options are wrong:\n  • (a) 20 hours: Computes 1/8 − 1/10 incorrectly\n  • (b) 30 hours: Uses wrong LCM\n  • (d) 50 hours: Uses 1/10 − 1/8 and takes absolute value wrong",
            solution_steps_ar='["Fill rate = 1/8, Net rate = 1/10","Leak = 1/8 − 1/10 = 1/40","Empty time = 40 hours"]',
    tags="work-rate", stage="mock",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        # ── Q163 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.3,
            text_ar="If a car travels at a constant speed and covers 240 km in 4 hours, how far will it travel in 7 hours?",
            option_a="360 km", option_b="400 km", option_c="420 km", option_d="480 km",
            correct_option="c",
            explanation_ar="Given:\n  240 km in 4 hours\n\nSolution:\n  Speed = 240/4 = 60 km/h\n  In 7 hours = 60 × 7 = 420 km\n\nWhy other options are wrong:\n  • (a) 360 km: Computes 60 × 6 (uses 6 hours)\n  • (b) 400 km: Computes approximately 240 × 5/3\n  • (d) 480 km: Computes 60 × 8 (uses 8 hours)",
            solution_steps_ar='["Speed = 240/4 = 60 km/h","7 hours: 60 × 7 = 420 km"]',
    tags="speed,proportion", stage="mock",
    rating_clarity=5, rating_cognitive=3, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.43),

        # ── Q164 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.2,
            text_ar="What is 1/5 of 200?",
            option_a="20", option_b="100", option_c="50", option_d="40",
            correct_option="d",
            explanation_ar="Given:\n  1/5 of 200\n\nSolution:\n  200 ÷ 5 = 40\n\nWhy other options are wrong:\n  • (a) 20: Computes 1/10 of 200\n  • (c) 50: Computes 1/4 of 200\n  • (b) 100: Computes 1/2 of 200",
            solution_steps_ar='["1/5 × 200 = 200 ÷ 5","= 40"]',
    tags="fraction", stage="diagnostic",
    rating_clarity=5, rating_cognitive=2, rating_fairness=5, rating_distractors=4, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=3, rating_overall=4.14),

        # ── Q165 ──
        Question(skill_id="quant_arithmetic", question_type="comparison", difficulty=0.4,
            text_ar="Compare:\n\n▸ Column (A): 25% of 120\n▸ Column (B): 30% of 90",
            option_a="Column (A) is greater", option_b="Column (B) is greater", option_c="The two values are equal", option_d="The relationship cannot be determined",
            correct_option="a",
            explanation_ar="Given:\n  Column A: 25% × 120 = 30\n  Column B: 30% × 90 = 27\n\nSolution:\n  30 > 27, Column A is greater\n\nWhy other options are wrong:\n  • (b) Column (B) is greater: 27 < 30\n  • (c) The two values are equal: 30 ≠ 27\n  • (d) The relationship cannot be determined: Both values are fixed",
            solution_steps_ar='["A = 0.25 × 120 = 30","B = 0.30 × 90 = 27","30 > 27, A is greater"]',
    tags="percentage,comparison", stage="peak",
    rating_clarity=5, rating_cognitive=3, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.43),

        # ── Q166 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.6,
            text_ar="The ratio of income to expenditure of a person is 7:5. If his savings are 4,000 riyals, what is his income?",
            option_a="10,000 riyals", option_b="12,000 riyals", option_c="14,000 riyals", option_d="16,000 riyals",
            correct_option="c",
            explanation_ar="Given:\n  Income:Expenditure = 7:5, Savings = Income − Expenditure = 4,000\n\nSolution:\n  Let Income = 7x, Expenditure = 5x\n  Savings = 7x − 5x = 2x = 4,000\n  x = 2,000\n  Income = 7 × 2,000 = 14,000\n\nWhy other options are wrong:\n  • (a) 10,000 riyals: Uses 5x as income\n  • (b) 12,000 riyals: Uses 6x as income\n  • (d) 16,000 riyals: Uses 8x as income",
            solution_steps_ar='["Income=7x, Expenditure=5x","Savings = 2x = 4,000, x = 2,000","Income = 14,000 riyals"]',
    tags="ratio,currency", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ── Q167 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.7,
            text_ar="A sum of 5,400 riyals is divided among A, B, and C in the ratio 2:3:4. What is the difference between C's share and A's share?",
            option_a="600 riyals", option_b="900 riyals", option_c="1,200 riyals", option_d="1,800 riyals",
            correct_option="c",
            explanation_ar="Given:\n  Total = 5,400, Ratio A:B:C = 2:3:4\n\nSolution:\n  Total parts = 2+3+4 = 9\n  One part = 5,400/9 = 600\n  A = 2 × 600 = 1,200\n  C = 4 × 600 = 2,400\n  Difference = 2,400 − 1,200 = 1,200\n\nWhy other options are wrong:\n  • (a) 600 riyals: One part only, not the difference\n  • (b) 900 riyals: C − B = 600, not C − A\n  • (d) 1,800 riyals: Computes 3 parts × 600",
            solution_steps_ar='["One part = 5,400/9 = 600","A=1,200, C=2,400","Difference = 1,200 riyals"]',
    tags="ratio", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

    ]
