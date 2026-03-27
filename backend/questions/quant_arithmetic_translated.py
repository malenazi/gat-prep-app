import json
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models import Question


def get_questions():
    return [

        # ══════════════════════════════════════════════════════════════
        #██ Existing questions (28 questions) ██
        # ══════════════════════════════════════════════════════════════

        #── Q1: Discount ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.2,
            text_ar="If the price of a book = 120 riyals, and you get a 25% discount, how much do you pay?",
            option_a="30 riyals", option_b="90 riyals", option_c="95 riyals", option_d="100 riyals",
            correct_option="b",
            explanation_ar="We are given: Price = 120 riyals Discount percentage = 25% Solution: Discount value = 120 25%\n • (d) 100 riyals: The result of subtracting the percentage (25) instead of the discount value (30)",
            solution_steps_ar='["Data: Price = 120 riyals, discount = 25%","Discount value = 120 x 0.25 = 30 riyals","Amount paid = 120 − 30 = 90 riyals"]',
    tags="percentage,discount", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        #── Q2: Ratio ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.3,
            text_ar="Ratio of boys to girls in a class = 3: 2\nIf the total number of students = 35, how many girls are there?",
            option_a="10", option_b="14", option_c="20", option_d="21",
            correct_option="b",
            explanation_ar="Data:\n Ratio: Boys : Girls = 3 : 2\n Total number = 35\n\nSolution:\n Sum of the parts of the ratio = 3 + 2 = 5\n Girls' share = (2 ÷ 5) x 35 = 14\n\nWhy are the other options wrong:\n • (a) 10: The result of the division is 35 ÷ 3.5 or an error in estimating the ratio\n • (c) 20: The result of the calculation Girls’ share as 35 − 15 with an incorrect estimation for boys\n • (d) 21: The result of calculating the share of boys (3 parts) instead of girls (2 parts)",
            solution_steps_ar='["Data: Ratio 3:2, total number = 35","Sum of parts = 3 + 2 = 5","Number of girls = (2 ÷ 5) x 35 = 14"]',
    tags="ratio", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        #── Q3: Fractional ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.4,
            text_ar="Ahmed walked ¾ of the distance to school. If the total distance = 12 km, how much is left?",
            option_a="3 km", option_b="4 km", option_c="8 km", option_d="٩ كم",
            correct_option="a",
            explanation_ar="Data:\n Total distance = 12 km\n Percentage traveled = ¾\n\nSolution:\n Distance traveled = ¾ x 12 = 9 km\n Remaining = 12 − 9 = 3 km\n\nWhy are the other options wrong:\n • (b) 4 km: The result of calculating ¼ x 12 = 3 and then mixing with 12 ÷ 3\n • (c) 8 km: The result of calculating ⅔ x 12 instead From ¼ x 12\n • (d) 9 km: This is the distance traveled, not the remaining distance (he forgot to subtract it from the total)",
            solution_steps_ar='["Distance traveled = ¾ x 12 = 9 km","Remaining = 12 − 9 = 3 km"]',
    tags="fraction", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        #── Q4: Work rate ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.5,
            text_ar="A worker completed ⅓ of the work in 4 hours.\nHow many hours does he need to complete the entire work?",
            option_a="8", option_b="10", option_c="12", option_d="16",
            correct_option="c",
            explanation_ar="Data:\n Part accomplished = ⅓\n Time = 4 hours\n\nSolution:\n If ⅓ of work = 4 hours\n Then full work (1) = 4 x 3 = 12 hours\n\nWhy are the other options wrong:\n • (A) 8: The result of doubling the time (4 x 2) instead of multiplying it by 3\n • (B) 10: Wrong estimation that does not depend on the correct inverse relationship\n • (D) 16: The result of multiplying 4 x 4 by mixing the denominator and the multiplier",
            solution_steps_ar='["Data: ⅓ work = 4 hours","Full work = 4 x 3 = 12 hours"]',
    tags="fraction,work-rate", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        #── Q5: Average ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.6,
            text_ar="Average grades of 5 students = 80\nA sixth student joined with a grade of 92\nWhat is the new average?",
            option_a="82", option_b="84", option_c="86", option_d="88",
            correct_option="a",
            explanation_ar="Data: Original number of students = 5, average = 80 New student: grade = 92 Solution: Original total = 5 92 directly without considering the numbers\n • (C) 86: The result of calculating (80 + 92) ÷ 2 = 86 (the average of only two values)\n • (D) 88: The result of dividing by 5 instead of 6 after adding the student",
            solution_steps_ar='["Original total = number of students x average = 5 x 80 = 400","New total = 400 + 92 = 492","New average = 492 ÷ 6 = 82"]',
    tags="average", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        #── Q6: Speed ​​──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.7,
            text_ar="A car travels a distance = 360 km in a time = 4 hours.\nIf its speed increases by 30 km/h, how many hours does it take to cover the same distance?",
            option_a="2", option_b="3", option_c="4", option_d="5",
            correct_option="b",
            explanation_ar="Data:\n Distance = 360 km, time = 4 h\n Increase in speed = 30 km/h\n\nSolution:\n Original speed = distance ÷ time = 360 ÷ 4 = 90 km/h\n New speed = 90 + 30 = 120 km/h\n New time = distance ÷ speed = 360 ÷ 120 = 3 hours\n\nWhy the other options? Error:\n • (a) 2: The result of dividing 360 ÷ 180 by mistakenly increasing the speed twice\n • (c) 4: This is the original time before increasing the speed\n • (d) 5: The result of using the original speed minus 30 instead of the increase",
            solution_steps_ar='["Original speed = 360 ÷ 4 = 90 km/h","New speed = 90 + 30 = 120 km/h","Time = 360 ÷ 120 = 3 hours"]',
    tags="speed", stage="foundation",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        #── Q7: Comparison — percentages ──
        Question(skill_id="quant_arithmetic", question_type="comparison", difficulty=0.5,
            text_ar="Compare:\n\n▸ Column A: 25% of 200\n▸ Column B: 50% of 100",
            option_a="Column A is larger", option_b="Column (b) is larger", option_c="The two values ​​are equal", option_d="The relationship cannot be determined",
            correct_option="c",
            explanation_ar="Calculating each column: Column A = 200 (d) The relationship cannot be determined: It can be determined because the values are constant and calculable",
            solution_steps_ar='["Column (A) = 200 x 0.25 = 50","Column (B) = 100 x 0.5 = 50","50 = 50 ∴ The two values ​​are equal"]',
    tags="comparison,percentage", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        #── Q8: Comparison — roots of ──
        Question(skill_id="quant_arithmetic", question_type="comparison", difficulty=0.6,
            text_ar="Compare:\n\n▸ Column (A): ∛27 (cube root of 27)\n▸ Column (B): √9 (square root of 9)",
            option_a="Column A is larger", option_b="Column (b) is larger", option_c="The two values ​​are equal", option_d="The relationship cannot be determined",
            correct_option="c",
            explanation_ar="Calculating each column:\n Column A: ∛27 = 3 (because 3 x 3 x 3 = 27)\n Column (B): √9 = 3 (because 3 x 3 = 9)\n\n∴ The two values are equal (3 = 3)\n\nWhy are the other options wrong:\n • (A) Column (A) is larger: wrong because ∛27 = 3 = √9\n • (b) Column (b) is larger: error for the same reason • (d) cannot be determined: both values can be calculated accurately",
            solution_steps_ar='["Column (A) = ∛27 = 3","Column (B) = √9 = 3","3 = 3 ∴ The two values ​​are equal"]',
    tags="comparison,profit", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        #── Q9: Simple multiplication ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.2,
            text_ar="Khaled bought 5 notebooks, the price of each notebook = 8 riyals. How much is the total amount?",
            option_a="13 riyals", option_b="40 riyals", option_c="35 riyals", option_d="45 riyals",
            correct_option="b",
            explanation_ar="Data: The number of notebooks = 5 The price of the notebook = 8 riyals The solution: The total amount = 5 Multiply 5 x 9 (book price error)",
            solution_steps_ar='["Data: Number of notebooks = 5, notebook price = 8 riyals","Total amount = 5 x 8 = 40 riyals"]',
    tags="ratio", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        #── Q10: Percentage ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.3,
            text_ar="Which of the following values ​​equals 20% of 150?",
            option_a="15", option_b="20", option_c="30", option_d="35",
            correct_option="c",
            explanation_ar="Data: Ratio = 20% Number = 150 Solution: 20% of 150 = 150 × approximately 0.25 (ratio error)",
            solution_steps_ar='["Data: Percentage = 20%, Number = 150","20% of 150 = 150 x 0.20 = 30"]',
    tags="percentage", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        #── Q11: Convert a fraction ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.3,
            text_ar="A fraction of ⅗ equals how many percent?",
            option_a="35%", option_b="53%", option_c="60%", option_d="٧٥٪",
            correct_option="c",
            explanation_ar="Data: Fraction = ⅗ Solution: ⅗ = 3 ÷ 5 = 0.6 0.6 As a number\n • (d) 75%: the result of mixing with a fraction of ¾ instead of ⅗",
            solution_steps_ar='["Fraction = ⅗","We divide: 3 ÷ 5 = 0.6","We multiply by 100: 0.6 x 100 = 60%"]',
    tags="percentage,fraction", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        #── Q12: Profit ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.4,
            text_ar="A merchant bought goods for 400 riyals and sold them for 520 riyals. What is the profit percentage?",
            option_a="20%", option_b="25%", option_c="30%", option_d="35%",
            correct_option="c",
            explanation_ar="Data: Purchase price = 400 riyals Selling price = 520 riyals Solution: Profit = 520 − 400 = 120 riyals Profit percentage = (120 ÷ 400) 25%: The result of calculating (120 ÷ 480) or a confusion in the division\n • (d) 35%: The result of calculating (140 ÷ 400) with an error in finding the profit",
            solution_steps_ar='["Profit = selling price − purchase price = 520 − 400 = 120 riyals","Profit percentage = (profit ÷ purchase price) x 100","= (120 ÷ 400) x 100 = 30%"]',
    tags="percentage,profit", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        #── Q13: Ratio and Proportion ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.5,
            text_ar="The ratio of water to juice in a mixture = 3:2\nIf the amount of water = 9 liters, what is the total amount of the mixture?",
            option_a="12 litres", option_b="15 litres", option_c="18 litres", option_d="6 litres",
            correct_option="b",
            explanation_ar="Data:\n Ratio: Water : Juice = 3 : 2\n Quantity of water = 9 litres\n\nSolution:\n One part = 9 ÷ 3 = 3 litres\n Quantity of juice = 2 x 3 = 6 litres\n Total quantity = 9 + 6 = 15 litres\n\nWhy are the other options wrong:\n • (a) 12 litres: the result of adding only 3 (one part) to the water\n • (c) 18 liters: The result of doubling the amount of water (9 x 2) instead of calculating the ratio\n • (d) 6 liters: This is the amount of juice only, not the total amount",
            solution_steps_ar='["One portion = amount of water ÷ number of parts of water = 9 ÷ 3 = 3 liters","Amount of juice = 2 x 3 = 6 liters","Total amount = 9 + 6 = 15 liters"]',
    tags="ratio,mixture", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        #── Q14: Comparison — Fractions ──
        Question(skill_id="quant_arithmetic", question_type="comparison", difficulty=0.5,
            text_ar="Compare: Column A: ³⁄₈ + Column B: ½",
            option_a="Column A is larger", option_b="Column (b) is larger", option_c="The two values ​​are equal", option_d="The relationship cannot be determined",
            correct_option="c",
            explanation_ar="Calculate each column: Column A = ³⁄₈ + ¹⁄₈ = ⁴⁄₈ = ½ Column B = ½\n\n∴ The two values are equal (½ = ½) Why are the other options wrong: • (A) Column A is larger: wrong because ³⁄₈ + ¹⁄₈ = ⁴⁄₈ = exactly ½\n • (b) Column (b) is larger: error for the same reason\n • (d) cannot be determined: addition and simplification of the fraction can be calculated",
            solution_steps_ar='["Column (A) = ³⁄₈ + ¹⁄₈ = ⁴⁄₈ = ½","Column (B) = ½","½ = ½ ∴ The two values ​​are equal"]',
    tags="comparison,fraction", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        #── Q15: Comparison — Average ──
        Question(skill_id="quant_arithmetic", question_type="comparison", difficulty=0.6,
            text_ar="Compare:\n\n▸ Column (A): Average of the numbers 4, 6, 8, 10\n▸ Column (B): 7.5",
            option_a="Column A is larger", option_b="Column (b) is larger", option_c="The two values ​​are equal", option_d="The relationship cannot be determined",
            correct_option="b",
            explanation_ar="Calculating each column: Column A: Sum = 4 + 6 + 8 + 10 = 28 Average = 28 ÷ 4 = 7 Column B = 7.5 Column B = 7.5 7 < 7.5 ← Column B Why are the other options wrong: A Column A is wrong because 7 < 7.5 C the two values Equal: False because 7 ≠ 7.5\n • (d) It is not possible to determine: the average can be calculated accurately",
            solution_steps_ar='["Column A: Sum = 4 + 6 + 8 + 10 = 28","Average = 28 ÷ 4 = 7","Column (B) = 7.5 ← Column (B) is larger"]',
    tags="comparison,average", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        #── Q16: Train and minutes ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.7,
            text_ar="A train is moving at a speed of 90 km/h.\nHow many minutes does it take to cover a distance of 60 km?",
            option_a="30 minutes", option_b="40 minutes", option_c="45 minutes", option_d="50 minutes",
            correct_option="b",
            explanation_ar="Data:\n Speed = 90 km/h\n Distance = 60 km\n\nSolution:\n Time = distance ÷ speed = 60 ÷ 90 = ⅔ hour\n ⅔ hour = ⅔ × 60 = 40 minutes\n\nWhy are the other options wrong:\n • (a) 30 minutes: The result of calculating 60 ÷ 90 = ⅔ then multiplying by ⅔ × 45 by mistake\n • (c) 45 minutes: The result of calculating ¾ hour instead of ⅔ hour\n • (d) 50 minutes: The result of forgetting the correct conversion from hours to minutes",
            solution_steps_ar='["Time = distance ÷ speed = 60 ÷ 90 = ⅔ hour","We convert to minutes: ⅔ x 60 = 40 minutes"]',
    tags="speed", stage="foundation",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        #── Q17: Increase and discount ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.8,
            text_ar="The price of an item increased by 20%, then the new price decreased by 20%.\nIf the original price = 500 riyals, what is the final price?",
            option_a="450 riyals", option_b="480 riyals", option_c="500 riyals", option_d="520 riyals",
            correct_option="b",
            explanation_ar="Data:\n The original price = 500 riyals\n An increase of 20%, then a discount of 20%\n\nThe solution:\n After the increase = 500 x 1.20 = 600 riyals\n After the discount = 600 x 0.80 = 480 riyals\n\nWhy are the other options wrong:\n • (a) 450 riyals: the result of subtracting 10% instead of calculating the increase and then the discount\n • (c) 500 riyals: belief The error is that a 20% increase then a 20% discount returns the original price\n • (d) 520 riyals: The result of calculating the increase is only 500 + 20 = 520 without the percentage",
            solution_steps_ar='["Price after increase = 500 x 1.20 = 600 riyals","Price after discount = 600 x 0.80 = 480 riyals","Note: The increase and discount in the same proportion does not return the original price"]',
    tags="percentage", stage="foundation",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        #── Q18: Workers ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.8,
            text_ar="6 workers work to finish a project in 10 days.\nIf 2 workers withdraw after 4 days, how many additional days do the rest need to finish the work?",
            option_a="6 days", option_b="8 days", option_c="9 days", option_d="10 days",
            correct_option="c",
            explanation_ar="Data:\n 6 workers ← 10 days\n After 4 days, 2 withdrew → 4 workers remaining\n\nSolution:\n Total work = 6 x 10 = 60 work units\n What was accomplished in 4 days = 6 x 4 = 24 units\n Remaining = 60 − 24 = 36 units\n Days required = 36 ÷ 4 = 9 days\n\nWhy are the other options wrong:\n • (a) 6 days: The result of calculating 10 − 4 = 6 (the remaining days without taking into account the change of workers)\n • (b) 8 days: The result of calculating 36 ÷ 4 ≈ 8 with wrong rounding\n • (d) 10 days: The complete original time without taking into account what was accomplished",
            solution_steps_ar='["Total work = 6 workers',
    tags="work-rate", stage="foundation",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        #── Q19: Compound interest ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.2,
            text_ar="Khaled deposited 10,000 riyals in a bank with an annual compound interest of 10% for two years.\nWhat is the total amount after two years?",
            option_a="12,000 riyals", option_b="12,100 riyals", option_c="11,000 riyals", option_d="١١٬١٠٠ ريال",
            correct_option="b",
            explanation_ar="Data: Capital = 10,000 riyals Interest rate = 10% annually Duration = two years Solution: After the first year = 10,000 (10,000 + 1,000 x 2) not the compound\n • (c) 11,000 riyals: The amount after only one year, not two years\n • (d) 11,100 riyals: The result of adding one year’s interest + 100 approximately",
            solution_steps_ar='["Data: Capital = 10,000, Interest = 10%, Duration = 2 years","After the first year = 10,000 x 1.1 = 11,000","After the second year = 11,000 x 1.1 = 12,100 riyals"]',
    tags="percentage,compound-interest", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        #── Q20: M.M.A. ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.25,
            text_ar="What is the smallest number that is divisible by both 4 and 6?",
            option_a="8", option_b="12", option_c="24", option_d="٣٦",
            correct_option="b",
            explanation_ar="Data: Numbers: 4 and 6 Solution: 4 = 2² 6 = 2 36: a common multiple but not the smallest",
            solution_steps_ar='["Factoring: 4 = 2², 6 = 2 x 3","M.A. = 2² x 3 = 4 x 3 = 12","So smallest common number = 12"]',
    tags="lcm-gcd", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        #── Q21: Ages ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.3,
            text_ar="Ahmed's age is now twice his son's age.\nIf the son's age = 12 years, how old will Ahmed be in 5 years?",
            option_a="24", option_b="27", option_c="29", option_d="٣٤",
            correct_option="c",
            explanation_ar="Data: Son's age = 12 years Father's age = 2 5)",
            solution_steps_ar='["Father\'s age now = 2 x 12 = 24 years","After 5 years = 24 + 5 = 29 years"]',
    tags="age", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        #── Q22: Mixing solutions ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.45,
            text_ar="Mix 3 liters of 20% juice with 7 liters of 40% juice. What is the concentration of the resulting mixture?",
            option_a="28%", option_b="30%", option_c="34%", option_d="36%",
            correct_option="c",
            explanation_ar="Data: Solution 1: 3 liters with a concentration of 20% Solution 2: 7 liters with a concentration of 40% Solution: Amount of substance = (3 0.34 = 34%\n\nWhy are the other options wrong:\n • (a) 28%: The result of calculating (20 + 40) ÷ 2 − 2 with an incorrect estimate\n • (b) 30%: The result of calculating the arithmetic mean (20 + 40) ÷ 2 without considering the quantities\n • (d) 36%: The result of adding an extra weight to the more concentrated solution",
            solution_steps_ar='["Amount of substance from solution 1 = 3 x 0.2 = 0.6","Amount of substance from solution 2 = 7 x 0.4 = 2.8","Total = 0.6 + 2.8 = 3.4, volume = 10","Concentration = 3.4 ÷ 10 = 34%"]',
    tags="percentage,mixture", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        #── Q23: Joint work ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.5,
            text_ar="One worker can finish a job in 6 days, and a second worker can finish it in 12 days.\nIf they work together, how many days does it take them to finish the work?",
            option_a="3 days", option_b="4 days", option_c="5 days", option_d="9 days",
            correct_option="b",
            explanation_ar="Data:\n The first worker: Finishes the work in 6 days\n The second worker: He finishes the work in 12 days\n\nThe solution:\n The production of the first one per day = ¹⁄₆\n The production of the second one per day = ¹⁄₁₂\n Production together = ¹⁄₆ + ¹⁄₁₂ = ²⁄₁₂ + ¹? = 18 ÷ 2 = 9 instead of adding the rates",
            solution_steps_ar='["Production of the first per day = ¹⁄₆, the second = ¹⁄₁₂","Production together = ¹⁄₆ + ¹⁄₁₂ = ³⁄₁₂ = ¼","Time = 1 ÷ ¼ = 4 days"]',
    tags="work-rate", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        #── Q24: Profit for ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.5,
            text_ar="A merchant bought goods for 800 riyals, and sold them at a profit of 35%.\nWhat is the selling price?",
            option_a="920 riyals", option_b="1,000 riyals", option_c="1,080 riyals", option_d="1,120 riyals",
            correct_option="c",
            explanation_ar="Data: Purchase price = 800 riyals Profit percentage = 35% Solution: Profit value = 800 Riyals: The result of calculating a profit of 25% instead of 35% • (d) 1,120 riyals: The result of calculating a profit of 40% instead of 35%",
            solution_steps_ar='["Profit value = 800 x 0.35 = 280 riyals","Sale price = 800 + 280 = 1,080 riyals"]',
    tags="percentage,profit", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        #── Q25: Currency conversion ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.55,
            text_ar="If the exchange rate of the dollar = 3.75 riyals.\nHow many riyals does a traveler need to buy 240 dollars?",
            option_a="750 riyals", option_b="840 riyals", option_c="900 riyals", option_d="٦٤ ريالاً",
            correct_option="c",
            explanation_ar="Data: Exchange rate = $1 = 3.75 riyals Amount required = $240 Solution: Amount in riyals = 240 3.5 instead of 3.75\n • (d) 64 riyals: the result of division is 240 ÷ 3.75 instead of multiplication",
            solution_steps_ar='["Data: 1 dollar = 3.75 riyals, required = 240 dollars","Amount = 240 x 3.75 = 900 riyals"]',
    tags="currency", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        #── Q26: Train and bridge ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.7,
            text_ar="A train 150 meters long is moving at a speed of 72 km/h. How many seconds does it take to cross a bridge 350 meters long?",
            option_a="18 seconds", option_b="20 seconds", option_c="25 seconds", option_d="30 seconds",
            correct_option="c",
            explanation_ar="Data: Train length = 150 m, bridge length = 350 m Speed = 72 km/h Solution: Total distance = 150 + 350 = 500 m Speed in meters/second = 72 25 seconds\n\nWhy the other options are wrong:\n • (a) 18 seconds: result of calculating 350 ÷ 20 (he forgot to add the length of the train)\n • (b) 20 seconds: result of incorrect speed conversion or forgetting part of the distance\n • (d) 30 seconds: result of using distance 600 m or incorrect speed",
            solution_steps_ar='["Total distance = train length + bridge length = 150 + 350 = 500 m","Speed ​​conversion: 72 km/h = 72 x (1000 ÷ 3600) = 20 m/s","Time = 500 ÷ 20 = 25 seconds"]',
    tags="speed", stage="foundation",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        #── Q27: Q.M.A. Application ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.75,
            text_ar="A farmer wanted to divide a rectangular field measuring 120 m x 84 m into equal squares that are as large as possible.\nWhat is the side length of one square?",
            option_a="6 pm", option_b="12 pm", option_c="14 AD", option_d="٢١ م",
            correct_option="b",
            explanation_ar="Data: Dimensions: 120 m Common denominator, but not the greatest\n • (c) 14 m: divides 84, but does not divide 120\n • (d) 21 m: divides 84, but does not divide 120",
            solution_steps_ar='["Factorization: 120 = 2³ x 3 x 5, 84 = 2² x 3 x 7","QM = 2² x 3 = 4 x 3 = 12","Length of the side of the largest square = 12 m"]',
    tags="ratio", stage="foundation",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        #── Q28: Compound work ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.8,
            text_ar="5 workers can finish a project in 18 days, working 8 hours a day.\nHow many workers are needed to finish the same project in 10 days, working 6 hours a day?",
            option_a="9", option_b="10", option_c="12", option_d="15",
            correct_option="c",
            explanation_ar="Data:\n Case 1: 5 workers x 18 days x 8 hours\n Case 2: 720 ÷ 80 (using 8 hours instead of 6)\n • (b) 10: Calculation result of 720 ÷ 72 or error in multiplying days x hours\n • (d) 15: Calculation result of 720 ÷ 48 (error in multiplying 10 x 6)",
            solution_steps_ar='["Size of work = workers x days x hours","Case 1: 5 x 18 x 8 = 720 labor units","Case 2: x x 10 x 6 = 60 x","60 x = 720 x = 12 workers"]',
    tags="work-rate", stage="foundation",
    rating_clarity=5, rating_cognitive=5, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=5.0),

        # ══════════════════════════════════════════════════════════════
        #██ New questions (83 questions) — from Q29 to Q111 ██
        # ══════════════════════════════════════════════════════════════

        # ════════════════════════════════════════
        #Difficulty 0.2 — very easy arithmetic questions
        # ════════════════════════════════════════

        # ── Q29 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.2,
            text_ar="If the price of 3 pens = 15 riyals, how much does one pen cost?",
            option_a="3 riyals", option_b="5 riyals", option_c="8 riyals", option_d="12 riyals",
            correct_option="b",
            explanation_ar="Data:\n The price of 3 pens = 15 riyals\n\nThe solution:\n The price of one pen = 15 ÷ 3 = 5 riyals\n\nWhy are the other options wrong:\n • (a) 28: The result of division by the sum of parts is wrong\n • (c) 36: The result of confusion between the share of the largest and smallest part\n • (d) 128: The result of multiplication instead of division or vice versa.",
            solution_steps_ar='["Data: 3 pens = 15 riyals","Pen price = 15 ÷ 3 = 5 riyals"]',
    tags="ratio", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # ── Q30 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.2,
            text_ar="What is the value of ½ of the number 64?",
            option_a="28", option_b="32", option_c="36", option_d="128",
            correct_option="b",
            explanation_ar="The solution: ½",
            solution_steps_ar='["½ x 64 = 64 ÷ 2 = 32"]',
    tags="fraction", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ── Q31 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.2,
            text_ar="Saad bought a shirt for 80 riyals, and got a 10% discount.\nHow much did he pay?",
            option_a="70 riyals", option_b="72 riyals", option_c="75 riyals", option_d="88 riyals",
            correct_option="b",
            explanation_ar="Data: Price = 80 riyals, discount = 10% Solution: Discount value = 80 The value of the ratio and the ratio itself",
            solution_steps_ar='["Discount value = 80 x 0.1 = 8 riyals","Amount paid = 80 − 8 = 72 riyals"]',
    tags="percentage,discount", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ── Q32 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.2,
            text_ar="If the number of apples in a basket = 48, and they are distributed equally among 6 children.\nHow many apples does each child get?",
            option_a="6", option_b="7", option_c="8", option_d="9",
            correct_option="c",
            explanation_ar="Solution:\n Number of apples per child = 48 ÷ 6 = 8 apples\n\nWhy are the other options wrong:\n • (a) 20: The result of division by the wrong sum of parts\n • (c) 40: The result of confusion between the share of the largest and smallest part\n • (d) 50: The result of multiplication instead of division or vice versa.",
            solution_steps_ar='["Number of apples per child = 48 ÷ 6 = 8"]',
    tags="ratio", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ── Q33 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.2,
            text_ar="What is the value of ¼ of the number 100?",
            option_a="20", option_b="25", option_c="40", option_d="50",
            correct_option="b",
            explanation_ar="The solution:\n ¼",
            solution_steps_ar='["¼ x 100 = 100 ÷ 4 = 25"]',
    tags="fraction", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ── Q34 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.2,
            text_ar="The price of a kilo of rice = 7 riyals.\nHow much does someone pay who buys 4 kilograms?",
            option_a="24 riyals", option_b="28 riyals", option_c="30 riyals", option_d="32 riyals",
            correct_option="b",
            explanation_ar="Solution: Amount = 4",
            solution_steps_ar='["Amount = number of kilos x price per kilo = 4 x 7 = 28 riyals"]',
    tags="ratio", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.14),

        # ════════════════════════════════════════
        #Difficulty 0.3 — easy arithmetic questions
        # ════════════════════════════════════════

        # ── Q35 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.3,
            text_ar="In a class of 40 students, the success rate is 75%. How many successes?",
            option_a="25", option_b="30", option_c="32", option_d="35",
            correct_option="b",
            explanation_ar="The solution: Number of successful people = 40 x 0.75 = 30 students Why are the other options wrong?",
            solution_steps_ar='["Number of successful people = 40 x 75% = 40 x 0.75 = 30"]',
    tags="percentage", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ── Q36 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.3,
            text_ar="What is the arithmetic mean of the numbers: 10, 20, 30?",
            option_a="15", option_b="20", option_c="25", option_d="30",
            correct_option="b",
            explanation_ar="Solution: Sum = 10 + 20 + 30 = 60 Average = 60 ÷ 3 = 20 Why are the other options wrong: (a) 4: The result of dividing by the wrong number of values\n • (c) 10: The result of forgetting to add the new value to the sum • (d) 16: The result of calculating the sum without dividing by the number of elements",
            solution_steps_ar='["Total = 10 + 20 + 30 = 60","Average = 60 ÷ 3 = 20"]',
    tags="average", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ── Q37 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.3,
            text_ar="The ratio of males to females in an office = 4:1.\nIf the number of males is 20, how many females?",
            option_a="4", option_b="5", option_c="10", option_d="16",
            correct_option="b",
            explanation_ar="Data: Ratio: Males: Females = 4 : 1 Number of males = 20 Solution: One part = 20 ÷ 4 = 5 Number of females = 1 Instead of dividing or vice versa",
            solution_steps_ar='["One part = 20 ÷ 4 = 5","Number of females = 1 x 5 = 5"]',
    tags="ratio", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q38 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.3,
            text_ar="Sami completed ⅖ of his project.\nWhat percentage of what was completed?",
            option_a="25%", option_b="30%", option_c="40%", option_d="45%",
            correct_option="c",
            explanation_ar="Solution: ⅖ = 2 ÷ 5 = 0.4 0.4",
            solution_steps_ar='["⅖ = 2 ÷ 5 = 0.4","0.4 x 100 = 40%"]',
    tags="percentage,fraction,work-rate", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q39 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.3,
            text_ar="Majed traveled a distance of 180 km in 3 hours.\nWhat is his speed in kilometers per hour?",
            option_a="45 km/h", option_b="50 km/h", option_c="60 km/h", option_d="90 km/h",
            correct_option="c",
            explanation_ar="The solution: Speed ​​= distance ÷ time = 180 ÷ 3 = 60 km/h Why are the other options wrong: • (a) 25 riyals: the result of division by a wrong sum of parts • (c) 75 riyals: the result of confusion between the share of the largest and smallest part • (d) 100 riyals: the result of multiplication instead of division or vice versa",
            solution_steps_ar='["Speed ​​= Distance ÷ Time","Speed ​​= 180 ÷ 3 = 60 km/h"]',
    tags="ratio", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q40 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.3,
            text_ar="Ali bought an item for 200 riyals and sold it for 250 riyals.\nHow many riyals did he profit?",
            option_a="25 riyals", option_b="50 riyals", option_c="75 riyals", option_d="100 riyals",
            correct_option="b",
            explanation_ar="The solution:\n Profit = selling price − purchase price = 250 − 200 = 50 riyals\n\nWhy are the other options wrong:\n • (a) 2 riyals: The result of calculating the percentage of profit from the selling price instead of the purchase\n • (c) 4 riyals: The result of calculating the amount of profit only without adding it to the price\n • (d) 6 riyals: The result of mixing profit and total revenue",
            solution_steps_ar='["Profit = 250 − 200 = 50 riyals"]',
    tags="profit", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q41 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.3,
            text_ar="If the price of 12 eggs = 9 riyals, how much does 4 eggs cost?",
            option_a="2 riyals", option_b="3 riyals", option_c="4 riyals", option_d="6 riyals",
            correct_option="b",
            explanation_ar="The solution: The price of one egg = 9 ÷ 12 = 0.75 riyals The price of 4 eggs = 4",
            solution_steps_ar='["The price of an egg = 9 ÷ 12 = 0.75 riyals","The price of 4 eggs = 4 x 0.75 = 3 riyals"]',
    tags="ratio", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q42 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.3,
            text_ar="What is the result: 0.5 + 0.25 + 0.25?",
            option_a="0.5", option_b="0.75", option_c="1", option_d="1.5",
            correct_option="c",
            explanation_ar="Solution:\n 0.5 + 0.25 = 0.75\n 0.75 + 0.25 = 1\n\nWhy are the other options wrong:\n • (a) 0.5: The result of forgetting to standardize the denominators\n • (b) 0.75: The result of calculating the intercept instead of the remainder or vice versa\n • (d) 1.5: The result of an error in multiplying or dividing fractions",
            solution_steps_ar='["0.5 + 0.25 = 0.75","0.75 + 0.25 = 1"]',
    tags="fraction", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ════════════════════════════════════════
        #Difficulty 0.4 — medium arithmetic questions
        # ════════════════════════════════════════

        # ── Q43 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.4,
            text_ar="If an employee’s salary = 6,000 riyals per month, and he saves 15% of it.\nHow much does he save per month?",
            option_a="750 riyals", option_b="800 riyals", option_c="900 riyals", option_d="1,000 riyals",
            correct_option="c",
            explanation_ar="Solution: Saving = 6,000",
            solution_steps_ar='["Savings = Salary x Savings Percentage","= 6,000 x 0.15 = 900 riyals"]',
    tags="percentage", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q44 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.4,
            text_ar="What is the arithmetic mean of the numbers: 15, 25, 30, 35, 45?",
            option_a="25", option_b="30", option_c="35", option_d="40",
            correct_option="b",
            explanation_ar="Solution: Sum = 15 + 25 + 30 + 35 + 45 = 150 Average = 150 ÷ ​​5 = 30 Why are the other options wrong: (a) 160 km: the result of dividing by the wrong number of values\n • (b) 180 km: the result of forgetting to add the new value to the sum • (d) 240 km: the result of calculating the sum without dividing by the number of elements",
            solution_steps_ar='["Sum = 15 + 25 + 30 + 35 + 45 = 150","Average = 150 ÷ ​​5 = 30"]',
    tags="average", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q45 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.4,
            text_ar="A car is traveling at 80 km/h.\nHow many kilometers does it travel in two and a half hours?",
            option_a="160 km", option_b="180 km", option_c="200 km", option_d="240 km",
            correct_option="c",
            explanation_ar="Solution: Distance = speed x time = 80",
            solution_steps_ar='["Distance = Speed ​​x Time","= 80 x 2.5 = 200 km"]',
    tags="speed", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q46 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.4,
            text_ar="A cheetah ate ⅜ of a candy bar. If the cake contains 24 pieces, how many pieces does he eat?",
            option_a="3", option_b="6", option_c="8", option_d="9",
            correct_option="d",
            explanation_ar="Solution: Number of pieces = ⅜",
            solution_steps_ar='["Number of pieces = ⅜ x 24","= (3 x 24) ÷ 8 = 72 ÷ 8 = 9 pieces"]',
    tags="fraction", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q47 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.4,
            text_ar="The price of a mobile phone was reduced from 2,000 riyals to 1,600 riyals. What is the percentage of reduction?",
            option_a="15%", option_b="20%", option_c="25%", option_d="30%",
            correct_option="b",
            explanation_ar="Solution:\n Amount of reduction = 2,000 − 1,600 = 400 riyals\n Percentage of reduction = (400 ÷ 2,000) x 100 = 20%\n\nWhy are the other options wrong:\n • (a) 0.25 liters: The result of calculating the ratio from the wrong number\n • (c) 1 liter: The result of forgetting to subtract or add the ratio to the original number\n • (d) 1.5 liters: The result of confusing the value of the ratio with the ratio itself",
            solution_steps_ar='["Discount amount = 2,000 − 1,600 = 400 riyals","Discount percentage = (400 ÷ 2,000) x 100 = 20%"]',
    tags="percentage,discount", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q48 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.4,
            text_ar="The ratio of salt to water in a solution = 1:9. If the total volume is 5 liters, how many liters of salt?",
            option_a="0.25 litre", option_b="0.5 litre", option_c="1 litre", option_d="1.5 litres",
            correct_option="b",
            explanation_ar="Solution: Sum of parts = 1 + 9 = 10 Amount of salt = (1 ÷ 10)",
            solution_steps_ar='["Sum of parts = 1 + 9 = 10","Amount of salt = (1 ÷ 10) x 5 = 0.5 litres"]',
    tags="ratio,mixture", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q49 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.4,
            text_ar="Muhammad bought 3 books at prices: 45, 35, and 20 riyals.\nHe got a 10% discount on the total.\nHow much did he pay?",
            option_a="81 riyals", option_b="90 riyals", option_c="95 riyals", option_d="100 riyals",
            correct_option="b",
            explanation_ar="Solution: Total = 45 + 35 + 20 = 100 riyals Discount = 100 • (D) ½: The result of confusion between the value of the ratio and the ratio itself",
            solution_steps_ar='["Total = 45 + 35 + 20 = 100 riyals","Discount = 100 x 0.1 = 10","Paid = 100 − 10 = 90 riyals"]',
    tags="percentage,discount", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q50 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.4,
            text_ar="A student spent ⅓ of his allowance on food, and ¼ on transportation.\nWhat is the remaining fraction?",
            option_a="¹⁄₁₂", option_b="⁵⁄₁₂", option_c="⁷⁄₁₂", option_d="½",
            correct_option="b",
            explanation_ar="Solution:\n What was spent = ⅓ + ¼ = ⁴⁄₁₂ + ³⁄₁₂ = ⁷⁄₁₂\n Remaining = 1 − ⁷⁄₁₂ = ⁵⁄₁₂\n\nWhy are the other options wrong:\n • (a) 45 euros: the result of forgetting to unify the denominators\n • (c) 84 euros: the result of calculating the cut off instead of the remainder or vice versa • (d) 882 euros: the result of an error in multiplying or dividing fractions",
            solution_steps_ar='["What was spent = ⅓ + ¼ = ⁴⁄₁₂ + ³⁄₁₂ = ⁷⁄₁₂","Remaining = 1 − ⁷⁄₁₂ = ⁵⁄₁₂"]',
    tags="fraction", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q51 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.4,
            text_ar="If the euro exchange rate = 4.20 riyals.\nHow many euros does someone who spends 210 riyals get?",
            option_a="45 euros", option_b="50 euros", option_c="84 euros", option_d="882 euros",
            correct_option="b",
            explanation_ar="Solution: Number of euros = 210 ÷ 4.20 = 50 euros Why are the other options wrong?",
            solution_steps_ar='["Number of Euros = Amount in Riyals ÷ Euro Price","= 210 ÷ 4.20 = 50 Euros"]',
    tags="currency", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q52 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.4,
            text_ar="Number of club subscribers = 300.\nThe number increased by 20%.\nHow many subscribers did there become?",
            option_a="320", option_b="350", option_c="360", option_d="380",
            correct_option="c",
            explanation_ar="Solution: Increment = 300",
            solution_steps_ar='["Increment = 300 x 0.2 = 60","New number = 300 + 60 = 360"]',
    tags="percentage", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ════════════════════════════════════════
        #Difficulty 0.5 — medium arithmetic questions
        # ════════════════════════════════════════

        # ── Q53 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.5,
            text_ar="Weighted average of two grades: Mathematics = 80 (weight 3) Science = 90 (weight 2) What is the weighted average?",
            option_a="82", option_b="84", option_c="85", option_d="86",
            correct_option="b",
            explanation_ar="Solution: Average = (80 Without dividing by the number of elements",
            solution_steps_ar='["Average = (80 x 3 + 90 x 2) ÷ (3 + 2)","= (240 + 180) ÷ 5 = 420 ÷ 5 = 84"]',
    tags="average", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q54 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.5,
            text_ar="A car travels a distance of 300 km. It went at a speed of 100 km/h and came back at a speed of 75 km/h. What is the time of the complete trip (round trip)?",
            option_a="6 hours", option_b="7 hours", option_c="8 hours", option_d="9 hours",
            correct_option="b",
            explanation_ar="Solution: Coming time = 300 ÷ 100 = 3 hours Return time = 300 ÷ 75 = 4 hours Total time = 3 + 4 = 7 hours Why are the other options wrong: • (a) 6 years: result of forgetting to convert units between hours and minutes or km/h and m/s\n • (c) 10 years: result of using distance instead of time in the equation • (d) 12 years: result of error In calculating average speed",
            solution_steps_ar='["Go time = 300 ÷ 100 = 3 hours","Return time = 300 ÷ 75 = 4 hours","Total time = 3 + 4 = 7 hours"]',
    tags="speed", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q55 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.5,
            text_ar="If the father's age is 4 times his son's age, and the difference between their ages is 24 years.\nWhat is the son's age?",
            option_a="6 years", option_b="8 years", option_c="10 years", option_d="12 years",
            correct_option="b",
            explanation_ar="Solution: Father's age = 4 x son's age Difference = 4x − x = 3x = 24 Age",
            solution_steps_ar='["Let the son\'s age = x, the father\'s age = 4x","Difference: 4x − x = 3x = 24","x = 24 ÷ 3 = 8 years"]',
    tags="age", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q56 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.5,
            text_ar="A merchant bought 50 pieces at a price of 20 riyals each.\nHe destroyed 10 pieces, and sold the rest at a price of 25 riyals.\nDid he gain or lose and how much?",
            option_a="He won 50 riyals", option_b="No gain or loss", option_c="Loss of 50 riyals", option_d="He won 100 riyals",
            correct_option="b",
            explanation_ar="Solution: Purchase cost = 50 48: The result of calculating the amount of profit only without adding it to the price\n • (D) 96: The result of mixing profit and total revenue",
            solution_steps_ar='["Purchase cost = 50 x 20 = 1,000 riyals","Sold = 40 pieces, revenue = 40 x 25 = 1,000","Difference = zero → neither profit nor loss"]',
    tags="profit", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q57 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.5,
            text_ar="The MMA of the numbers 8 and 12 is equal to:",
            option_a="4", option_b="24", option_c="48", option_d="96",
            correct_option="b",
            explanation_ar="Solution: 8 = 2³ 12 = 2²",
            solution_steps_ar='["8 = 2³, 12 = 2² x 3","M.A. = 2³ x 3 = 8 x 3 = 24"]',
    tags="lcm-gcd", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q58 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.5,
            text_ar="Mixing 4 liters of milk at a price of 5 riyals/liter with 6 liters of milk at a price of 8 riyals/liter. What is the price of a liter of the mixture?",
            option_a="6.2 riyals", option_b="6.5 riyals", option_c="6.8 riyals", option_d="7 riyals",
            correct_option="c",
            explanation_ar="Solution: Total cost = (4 Different quantities when mixing\n • (d) 35 km: The result of dividing by the number of solutions instead of the total volume",
            solution_steps_ar='["Cost = (4 x 5) + (6 x 8) = 20 + 48 = 68","Volume = 10 litres","Price per liter = 68 ÷ 10 = 6.8 riyals"]',
    tags="mixture", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.43),

        # ── Q59 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.5,
            text_ar="A cyclist covered ⅗ of the distance in one hour. If his speed was 15 km/h, what was the total distance?",
            option_a="20 km", option_b="25 km", option_c="30 km", option_d="35 km",
            correct_option="b",
            explanation_ar="Solution: Distance traveled in an hour = 15 km, which is equal to ⅗ of the total distance Total distance = 15 ÷ ⅗ = 15 I divided it",
            solution_steps_ar='["The total distance = 15 km = ⅗ the total distance","The total distance = 15 ÷ (3/5) = 15 x (5/3) = 25 km"]',
    tags="fraction,speed", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q60 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.5,
            text_ar="Distribute the amount of 600 riyals among three people in a ratio of 1:2:3.\nWhat is the share of the person with the largest share?",
            option_a="100 riyals", option_b="200 riyals", option_c="300 riyals", option_d="400 riyals",
            correct_option="c",
            explanation_ar="Solution: The sum of the parts = 1 + 2 + 3 = 6 The value of the part = 600 ÷ 6 = 100 riyals The largest share (3 parts) = 3",
            solution_steps_ar='["Sum of parts = 1 + 2 + 3 = 6","Part value = 600 ÷ 6 = 100","Largest share = 3 x 100 = 300 riyals"]',
    tags="percentage", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ════════════════════════════════════════
        #Difficulty 0.6 — Above average arithmetic questions
        # ════════════════════════════════════════

        # ── Q61 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.6,
            text_ar="Simple interest on the amount of 20,000 riyals at a rate of 5% annually for 3 years. What is the interest amount?",
            option_a="1,000 riyals", option_b="2,000 riyals", option_c="3,000 riyals", option_d="4,000 riyals",
            correct_option="c",
            explanation_ar="Solution: Interest = Capital × Rate × Duration = 20,000",
            solution_steps_ar='["Interest = Capital x Rate x Duration","= 20,000 x 0.05 x 3 = 3,000 riyals"]',
    tags="percentage", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q62 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.6,
            text_ar="A car travels 240 km with 20 liters of gasoline. How many liters do you need to travel 360 km?",
            option_a="25 litres", option_b="28 litres", option_c="30 litres", option_d="36 litres",
            correct_option="c",
            explanation_ar="Solution: Liter consumption = 240 ÷ 20 = 12 km/liter Liters = 360 ÷ 12 = 30 liters Why are the other options wrong: • (a) 8 years: as a result of division by a wrong sum of parts • (c) 12 years: as a result of confusion between the share of the larger and smaller parts • (d) 15 years: as a result of multiplication instead of division or vice versa",
            solution_steps_ar='["Liters consumption = 240 ÷ 20 = 12 km/litre","Liters required = 360 ÷ 12 = 30 litres"]',
    tags="ratio", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ── Q63 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.6,
            text_ar="The mother's age is now 3 times her daughter's age.\nAfter 10 years, the mother's age will be twice her daughter's age.\nHow old is the daughter now?",
            option_a="8 years", option_b="10 years", option_c="12 years", option_d="15 years",
            correct_option="b",
            explanation_ar="Solution: Let the daughter's age = x, the mother's age = 3x After 10 years: 3x + 10 = 2 x (x + 10) 3x + 10 = 2x + 20 Required\n • (d) 4 hours: result of confusion in forming the age equation",
            solution_steps_ar='["Let\'s assume the age of the daughter = x, the mother = 3x","After 10 years: 3x + 10 = 2(x + 10)","3x + 10 = 2x + 20 → x = 10"]',
    tags="age", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ── Q64 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.6,
            text_ar="A tap fills a tank in 6 hours, and another fills it in 3 hours. If they are opened together, in how many hours will the tank be filled?",
            option_a="1.5 hours", option_b="2 hours", option_c="2.5 hours", option_d="4 hours",
            correct_option="b",
            explanation_ar="Solution:\n The rate of the first = ¹⁄₆, the second = ⅓\n The rate together = ¹⁄₆ + ⅓ = ¹⁄₆ + ²⁄₆ = ³⁄₆ = ½\n Time = 1 ÷ ½ = 2 hours\n\nWhy are the other options wrong:\n • (a) 450 riyals: result of addition times instead of summing the daily rates\n • (b) 455 riyals: the result of calculating the production of only one worker\n • (d) 700 riyals: the result of forgetting to subtract the portion completed from the total work",
            solution_steps_ar='["First rate = ¹⁄₆, second = ¹⁄₃","Together = ¹⁄₆ + ²⁄₆ = ³⁄₆ = ½","Time = 1 ÷ ½ = 2 hours"]',
    tags="work-rate", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ── Q65 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.6,
            text_ar="The price of an item after a 30% discount became 350 riyals.\nWhat is the original price?",
            option_a="450 riyals", option_b="455 riyals", option_c="500 riyals", option_d="700 riyals",
            correct_option="c",
            explanation_ar="Solution: Price after discount = original price x (1 − 0.3) = 0.7 (d) 11 riyals: the result of confusion between the value of the percentage and the percentage itself",
            solution_steps_ar='["Price after discount = original price x 0.7","350 = 0.7 x original price","Original price = 350 ÷ 0.7 = 500 riyals"]',
    tags="percentage,discount", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ── Q66 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.6,
            text_ar="Mix 6 kg of rice at a price of 8 riyals/kg with 4 kg at a price of 13 riyals/kg.\nWhat is the price of a kilogram of the mixture?",
            option_a="9.5 riyals", option_b="10 riyals", option_c="10.5 riyals", option_d="11 riyals",
            correct_option="b",
            explanation_ar="Solution: Cost = (6 (d) 6 hours: The result of dividing by the number of solutions instead of the total volume",
            solution_steps_ar='["Cost = (6 x 8) + (4 x 13) = 48 + 52 = 100","Weight = 10 kg","Price per kilo = 100 ÷ 10 = 10 riyals"]',
    tags="mixture", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ── Q67 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.6,
            text_ar="3 workers work to paint a fence in 8 hours.\nHow many hours does it take 6 workers to paint the same fence?",
            option_a="3 hours", option_b="4 hours", option_c="5 hours", option_d="6 hours",
            correct_option="b",
            explanation_ar="Solution: Volume of work = 3",
            solution_steps_ar='["Work volume = 3 x 8 = 24 work units","Time = 24 ÷ 6 = 4 hours"]',
    tags="work-rate", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ── Q68 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.6,
            text_ar="BC (36, 48) equals:",
            option_a="6", option_b="8", option_c="12", option_d="24",
            correct_option="c",
            explanation_ar="Solution:\n 36 = 2² x 3²\n 48 = 2⁴ x 3\n BC = 2² x 3 = 4 x 3 = 12\n\nWhy are the other options wrong:\n • (a) 10%: This is BC instead of BC or vice versa\n • (C) 20%: the result of directly multiplying the two numbers\n • (d) 30%: the result of an error in factoring Primary factors",
            solution_steps_ar='["36 = 2² x 3², 48 = 2⁴ x 3","Q.M.A. = 2² x 3 = 12"]',
    tags="lcm-gcd", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ── Q69 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.6,
            text_ar="If the population of a city increases from 200,000 to 230,000, what is the percentage of increase?",
            option_a="10%", option_b="15%", option_c="20%", option_d="30%",
            correct_option="b",
            explanation_ar="Solution:\n Increase = 230,000 − 200,000 = 30,000\n Ratio = (30,000 ÷ 200,000) x 100 = 15%\n\nWhy are the other options wrong:\n • (a) 3,600 riyals: The result of calculating the percentage from the wrong number\n • (b) 3,960 riyals: The result of forgetting to subtract or add the ratio to the original number\n • (d) 4,800 riyals: the result of confusion between the value of the percentage and the percentage itself",
            solution_steps_ar='["Increase = 230,000 − 200,000 = 30,000","Percentage = (30,000 ÷ 200,000) x 100 = 15%"]',
    tags="percentage", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ── Q70 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.6,
            text_ar="An amount of 3,000 riyals with a compound interest of 20% annually. What is the amount after two years?",
            option_a="3,600 riyals", option_b="3,960 riyals", option_c="4,320 riyals", option_d="4,800 riyals",
            correct_option="c",
            explanation_ar="Solution: After the first year = 3,000 4,800 riyals: the result of confusion between the value of the percentage and the percentage itself",
            solution_steps_ar='["After year 1 = 3,000 x 1.2 = 3,600","After year 2 = 3,600 x 1.2 = 4,320 riyals"]',
    tags="percentage,compound-interest", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ════════════════════════════════════════
        #Difficulty 0.7 — Difficult arithmetic questions
        # ════════════════════════════════════════

        # ── Q71 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.7,
            text_ar="A cyclist went at 20 km/h and returned at 12 km/h. What is the average speed for the entire trip?",
            option_a="15 km/h", option_b="16 km/h", option_c="17 km/h", option_d="18 km/h",
            correct_option="a",
            explanation_ar="Solution: Average speed (round trip) = (2 x h₁ x h₂) ÷ (h₁ + x₂) = (2 x 20 x 12) ÷ (20 + 12) = 480 ÷ 32 = 15 km/h Why are the other options wrong: • (a) 4 years: the result of dividing by the wrong number of values • (b) 6 Years: The result of forgetting to add the new value to the sum\n • (c) 8 years: The result of calculating the sum without dividing by the number of elements",
            solution_steps_ar='["Average speed = (2 x h₁ x h₂) ÷ (h₁ + h₂)","= (2 x 20 x 12) ÷ (20 + 12)","= 480 ÷ 32 = 15 km/h"]',
    tags="average,speed", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ── Q72 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.7,
            text_ar="The sum of the ages of a father and his son = 56 years.\nAfter 8 years, the father’s age will be 3 times the age of his son.\nHow old is the son now?",
            option_a="4 years", option_b="6 years", option_c="8 years", option_d="10 years",
            correct_option="d",
            explanation_ar="Solution: Let the son's age = x, the father's age = 56 × 18 ✓\n\nWhy are the other options wrong:\n • (a) 35%: The result of forgetting to add the future years for both ages\n • (b) 40%: The result of calculating the current age only without the required addition\n • (d) 50%: The result of confusion in forming the age equation",
            solution_steps_ar='["Let the son\'s age =',
    tags="age", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ── Q73 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.7,
            text_ar="If a person spends 40% of his money and then spends 25% of the rest, what percentage of the original money is left?",
            option_a="35%", option_b="40%", option_c="45%", option_d="50%",
            correct_option="c",
            explanation_ar="Solution:\n Remaining after first spending = 100 − 40 = 60%\n Spend 25% of 60 = 15%\n Final remainder = 60 − 15 = 45%\n\nWhy are the other options wrong:\n • (a) 36: Result of calculating the ratio from the wrong number\n • (c) 108: Result of forgetting to subtract or add the ratio to the original number\n • (d) 144: Result of confusing the value of the ratio with the ratio itself",
            solution_steps_ar='["Remaining after first spending = 100 − 40 = 60%","Second spending = 25% x 60 = 15%","Remaining = 60 − 15 = 45%"]',
    tags="percentage", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ── Q74 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.7,
            text_ar="MMA (18, 24, 36) equals:",
            option_a="36", option_b="72", option_c="108", option_d="144",
            correct_option="b",
            explanation_ar="Solution:\n 18 = 2 x 3²\n 24 = 2³ x 3\n 36 = 2² x 3²\n M.A. = 2³ x 3² = 8 x 9 = 72\n\nWhy are the other options wrong:\n • (a) 1,800 Riyals: This is M.A. instead of M.A. or vice versa\n • (b) 1,900 Riyals: The result of multiplication The two numbers directly\n • (d) 2,100 riyals: the result of an error in prime factor analysis",
            solution_steps_ar='["18 = 2 x 3², 24 = 2³ x 3, 36 = 2² x 3²","M.A. = 2³ x 3² = 8 x 9 = 72"]',
    tags="lcm-gcd", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ── Q75 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.7,
            text_ar="A merchant bought goods for 1,500 riyals.\nIf he wanted to sell them at a profit of 20% after deducting 10% from the announced selling price.\nWhat is the announced price?",
            option_a="1,800 riyals", option_b="1,900 riyals", option_c="2,000 riyals", option_d="٢٬١٠٠ ريال",
            correct_option="c",
            explanation_ar="Solution:\n Required selling price = 1,500 The original\n • (D) 2,100 riyals: The result of confusion between the value of the ratio and the ratio itself",
            solution_steps_ar='["Requested selling price = 1,500 x 1.2 = 1,800","Advertised price x 0.9 = 1,800","Advertised price = 1,800 ÷ 0.9 = 2,000 riyals"]',
    tags="percentage,profit,discount", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ════════════════════════════════════════
        #Difficulty 0.8 — Very difficult arithmetic questions
        # ════════════════════════════════════════

        # ── Q76 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.8,
            text_ar="Compound interest on the amount of 5,000 riyals at a rate of 20% annually for 3 years. What is the total amount after 3 years?",
            option_a="7,200 riyals", option_b="8,000 riyals", option_c="8,640 riyals", option_d="9,000 riyals",
            correct_option="c",
            explanation_ar="Solution:\n After year 1 = 5,000 x 1.2 = 6,000\n After year 2 = 6,000 x 1.2 = 7,200\n After year 3 = 7,200 x 1.2 = 8,640 riyals\n\nWhy are the other options wrong:\n • (a) 7,200 riyals: The result of calculating the percentage from the wrong number\n • (b) 8,000 riyals: As a result of forgetting to subtract or add the ratio to the original number • (d) 9,000 riyals: As a result of confusing the value of the ratio with the ratio itself",
            solution_steps_ar='["After year 1 = 5,000 x 1.2 = 6,000","After year 2 = 6,000 x 1.2 = 7,200","After year 3 = 7,200 x 1.2 = 8,640"]',
    tags="percentage,compound-interest", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ══════════════════════════════════════════════════════════════
        #██ New comparison questions (22 questions) ██
        # ══════════════════════════════════════════════════════════════

        #── Q77: Comparison — Difficulty 0.2 ──
        Question(skill_id="quant_arithmetic", question_type="comparison", difficulty=0.2,
            text_ar="Compare:\n\n▸ Column (A): ½ x 10\n▸ Column (B): ¼ x 20",
            option_a="Column A is larger", option_b="Column (b) is larger", option_c="The two values ​​are equal", option_d="The relationship cannot be determined",
            correct_option="c",
            explanation_ar="Solution: Column (A) = ½ x 10 = 5 Column (B) = ¼ x 20 = 5 The two values ​​are equal Why are the other options Error: • (B) Column (B) is larger: An error in calculating the value of one of the two columns\n • (C) The two values ​​are equal: An error in comparing the two values\n • (D) The relationship cannot be determined: The belief that it is not possible to determine even though the values ​​are determined",
            solution_steps_ar='["Column (A) = ½ x 10 = 5","Column (B) = ¼ x 20 = 5","5 = 5 ∴ The two values ​​are equal"]',
    tags="comparison,fraction", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        #── Q78: Comparison — Difficulty 0.2 ──
        Question(skill_id="quant_arithmetic", question_type="comparison", difficulty=0.2,
            text_ar="Compare:\n\n▸ Column (A): 3 x 7\n▸ Column (B): 4 x 5",
            option_a="Column A is larger", option_b="Column (b) is larger", option_c="The two values ​​are equal", option_d="The relationship cannot be determined",
            correct_option="a",
            explanation_ar="Solution: Column (A) = 21 Column (B) = 20 21 > 20 ← Column (A) is larger Why are the other options Error: • (A) Column (A) is larger: An error in calculating the value of one of the two columns\n • (B) Column (B) is larger: An error in comparing the two values\n • (D) The relationship cannot be determined: the belief that it is not possible to determine even though the values ​​are determined",
            solution_steps_ar='["Column (A) = 3 x 7 = 21","Column (B) = 4 x 5 = 20","21 > 20 ← Column (A) is larger"]',
    tags="comparison", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        #── Q79: Comparison — Difficulty 0.3 ──
        Question(skill_id="quant_arithmetic", question_type="comparison", difficulty=0.3,
            text_ar="Compare:\n\n▸ Column A: 10% of 300\n▸ Column B: 30% of 100",
            option_a="Column A is larger", option_b="Column (b) is larger", option_c="The two values ​​are equal", option_d="The relationship cannot be determined",
            correct_option="c",
            explanation_ar="Solution: Column (A) = 300",
            solution_steps_ar='["Column (A) = 300 x 0.1 = 30","Column (B) = 100 x 0.3 = 30","30 = 30 ∴ The two values ​​are equal"]',
    tags="comparison,percentage", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.29),

        #── Q80: Compare — Difficulty 0.3 ──
        Question(skill_id="quant_arithmetic", question_type="comparison", difficulty=0.3,
            text_ar="Compare: Column A: ⅔ x 12 Column B: ¾ x 12",
            option_a="Column A is larger", option_b="Column (b) is larger", option_c="The two values ​​are equal", option_d="The relationship cannot be determined",
            correct_option="b",
            explanation_ar="Solution: Column (A) = ⅔ x 12 = 8 Column (B) = ¾ x 12 = 9 8 < 9 ← Column (B) is greater Why are the other options Error: • (A) Column (A) is greater: An error in calculating the value of one of the two columns\n • (B) Column (B) is greater: An error in comparing the two values\n • (D) The relationship cannot be determined: The belief that it is not possible to determine even though the values ​​are determined",
            solution_steps_ar='["Column A = ⅔ x 12 = 8","Column B = ¾ x 12 = 9","8 < 9 ← Column B is greater"]',
    tags="comparison,fraction", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        #── Q81: Comparison — Difficulty 0.3 ──
        Question(skill_id="quant_arithmetic", question_type="comparison", difficulty=0.3,
            text_ar="Compare:\n\n▸ Column (A): 0.75\n▸ Column (B): ¾",
            option_a="Column A is larger", option_b="Column (b) is larger", option_c="The two values ​​are equal", option_d="The relationship cannot be determined",
            correct_option="c",
            explanation_ar="Solution:\n Column (A) = 0.75\n Column (B) = ¾ = 3 ÷ 4 = 0.75\n The two values ​​are equal\n\nWhy are the other options Error:\n • (B) Column (B) is larger: An error in calculating the value of one of the two columns\n • (C) The two values ​​are equal: An error in comparing the two values\n • (D) The relationship cannot be determined: The belief that it is not possible to determine even though the values ​​are determined",
            solution_steps_ar='["Column (A) = 0.75","Column (B) = ¾ = 0.75","0.75 = 0.75 ∴ The two values ​​are equal"]',
    tags="comparison,fraction", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        #── Q82: Comparison — Difficulty 0.4 ──
        Question(skill_id="quant_arithmetic", question_type="comparison", difficulty=0.4,
            text_ar="Compare:\n\n▸ Column A: 25% of 400\n▸ Column B: ⅓ x 270",
            option_a="Column A is larger", option_b="Column (b) is larger", option_c="The two values ​​are equal", option_d="The relationship cannot be determined",
            correct_option="a",
            explanation_ar="Solution: Column (A) = 400 The relationship cannot be determined: the belief that it cannot be determined even though the values are defined",
            solution_steps_ar='["Column A = 400 x 0.25 = 100","Column (B) = 270 ÷ 3 = 90","100 > 90 ← Column A is larger"]',
    tags="comparison,percentage,fraction", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        #── Q83: Comparison — Difficulty 0.4 ──
        Question(skill_id="quant_arithmetic", question_type="comparison", difficulty=0.4,
            text_ar="Compare:\n\n▸ Column (A): average of 8 and 12\n▸ Column (B): average of 9 and 11",
            option_a="Column A is larger", option_b="Column (b) is larger", option_c="The two values ​​are equal", option_d="The relationship cannot be determined",
            correct_option="c",
            explanation_ar="Solution: Column (A) = (8 + 12) ÷ 2 = 10 Column (B) = (9 + 11) ÷ 2 = 10 The two values ​​are equal Why are the other options Error: • (B) Column (B) is larger: An error in calculating the value of one of the two columns\n • (C) The two values ​​are equal: An error in comparing the two values\n • (D) The relationship cannot be determined: The belief that it is not possible to determine even though the values ​​are determined",
            solution_steps_ar='["Column (A) = (8 + 12) ÷ 2 = 10","Column (B) = (9 + 11) ÷ 2 = 10","10 = 10 ∴ The two values ​​are equal"]',
    tags="comparison,average", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        #── Q84: Comparison — Difficulty 0.4 ──
        Question(skill_id="quant_arithmetic", question_type="comparison", difficulty=0.4,
            text_ar="Compare:\n\n▸ Column (A): Profit on selling a good that was bought for 200 and sold for 260\n▸ Column (B): Profit on selling a good that was bought for 300 and sold for 350",
            option_a="Column A is larger", option_b="Column (b) is larger", option_c="The two values ​​are equal", option_d="The relationship cannot be determined",
            correct_option="a",
            explanation_ar="Solution: Column (A) = 260 − 200 = 60 riyals Column B = 350 − 300 = 50 riyals 60 > 50 ← Column A is larger Why are the other options Error: A: Column A is larger: Error in calculating the value of one of the two columns • (C) The two values are equal: Error in comparing the two values • (D) The relationship cannot be determined: Belief It is not possible to determine even though the values are specified",
            solution_steps_ar='["Column A = 260 − 200 = 60","Column B = 350 − 300 = 50","60 > 50 ← Column A is larger"]',
    tags="comparison,profit", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.43),

        #── Q85: Comparison — Difficulty 0.4 ──
        Question(skill_id="quant_arithmetic", question_type="comparison", difficulty=0.4,
            text_ar="Compare: Column A: The speed of a car that travels 150 km in 3 hours Column B: The speed of a train that travels 240 km in 4 hours",
            option_a="Column A is larger", option_b="Column (b) is larger", option_c="The two values ​​are equal", option_d="The relationship cannot be determined",
            correct_option="b",
            explanation_ar="Solution:\n Column (A) = 150 ÷ 3 = 50 km/h\n Column (B) = 240 ÷ 4 = 60 km/h\n 50 < 60 ← Column (B) is larger\n\nWhy are the other options Error:\n • (A) Column (A) is larger: An error in calculating the value of one of the two columns\n • (B) Column (B) is larger: An error in comparing the two values\n • (D) No The relationship can be determined: the belief that it cannot be determined even though the values are defined",
            solution_steps_ar='["Column (A) = 150 ÷ ​​3 = 50 km/h","Column (B) = 240 ÷ 4 = 60 km/h","50 < 60 ← Column (B) is larger"]',
    tags="comparison,speed", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.43),

        #── Q86: Comparison — Difficulty 0.5 ──
        Question(skill_id="quant_arithmetic", question_type="comparison", difficulty=0.5,
            text_ar="Compare: Column A: ⅔ + ¼ Column B: ¾ + ⅙",
            option_a="Column A is larger", option_b="Column (b) is larger", option_c="The two values ​​are equal", option_d="The relationship cannot be determined",
            correct_option="c",
            explanation_ar="Solution: Column A = ⅔ + ¼ = ⁸⁄₁₂ + ³⁄₁₂ = ¹¹⁄₁₂ Column B = ¾ + ⅙ = ⁹⁄₁₂ + ²⁄₁₂ = ¹¹⁄₁₂\nThe two values are equal\n\nWhy are the other options Error:\n • (a) Column (A) is larger: An error in calculating the value of one of the two columns\n • (B) Column (B) is larger: An error in comparing the two values\n • (d) The relationship cannot be determined: the belief that it is not possible to determine even though the values are determined",
            solution_steps_ar='["Column A = ⅔ + ¼ = ⁸⁄₁₂ + ³⁄₁₂ = ¹¹⁄₁₂","Column B = ¾ + ⅙ = ⁹⁄₁₂ + ²⁄₁₂ = ¹¹⁄₁₂","¹¹⁄₁₂ = ¹¹⁄₁₂ ∴ The two values are equal"]',
    tags="comparison,fraction", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.43),

        #── Q87: Comparison — Difficulty 0.5 ──
        Question(skill_id="quant_arithmetic", question_type="comparison", difficulty=0.5,
            text_ar="Compare:\n\n▸ Column A: 15% of 400\n▸ Column B: 40% of 150",
            option_a="Column A is larger", option_b="Column (b) is larger", option_c="The two values ​​are equal", option_d="The relationship cannot be determined",
            correct_option="c",
            explanation_ar="Solution: Column (A) = 400",
            solution_steps_ar='["Column (A) = 400 x 0.15 = 60","Column (B) = 150 x 0.4 = 60","60 = 60 ∴ The two values ​​are equal"]',
    tags="comparison,percentage", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.43),

        #── Q88: Comparison — Difficulty 0.5 ──
        Question(skill_id="quant_arithmetic", question_type="comparison", difficulty=0.5,
            text_ar="Compare:\n\n▸ Column (A): Each person’s share if 90 riyals is distributed among 3 people\n▸ Column (B): Each person’s share if 150 riyals is distributed among 5 people",
            option_a="Column A is larger", option_b="Column (b) is larger", option_c="The two values ​​are equal", option_d="The relationship cannot be determined",
            correct_option="c",
            explanation_ar="Solution: Column (A) = 90 ÷ 3 = 30 Column (B) = 150 ÷ ​​5 = 30 The two values ​​are equal Why are the other options Error: • (A) Column (A) is larger: An error in calculating the value of one of the two columns\n • (C) The two values ​​are equal: An error in comparing the two values\n • (D) The relationship cannot be determined: The belief that it is not possible to determine even though the values ​​are determined",
            solution_steps_ar='["Column (A) = 90 ÷ 3 = 30","Column (B) = 150 ÷ ​​5 = 30","30 = 30 ∴ The two values ​​are equal"]',
    tags="comparison,ratio", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.43),

        #── Q89: Comparison — Difficulty 0.6 ──
        Question(skill_id="quant_arithmetic", question_type="comparison", difficulty=0.6,
            text_ar="Compare:\n\n▸ Column (A): Profit percentage on a commodity bought for 250 and sold for 300\n▸ Column (B): 25%",
            option_a="Column A is larger", option_b="Column (b) is larger", option_c="The two values ​​are equal", option_d="The relationship cannot be determined",
            correct_option="b",
            explanation_ar="Solution: Column (A): Profit = 300 − 250 = 50 Profit percentage = (50 ÷ 250) x 100 = 20% Column (B) = 25% 20% < 25% ← Column (B) is larger Why are the other options Error: • (B) Column (B) is larger: An error in calculating the value of one of the two columns • (C) The two values are equal: An error in comparing The two values\n • (d) The relationship cannot be determined: the belief that it is not possible to determine even though the values are defined",
            solution_steps_ar='["Column A: Profit = 50, Percentage = (50 ÷ 250) x 100 = 20%","Column (B) = 25%","20% < 25% ← Column (B) is greater"]',
    tags="comparison,percentage,profit", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.43),

        #── Q90: Comparison — Difficulty 0.6 ──
        Question(skill_id="quant_arithmetic", question_type="comparison", difficulty=0.6,
            text_ar="Compare:\n\n▸ Column (A): BC (6, 8)\n▸ Column (B): BC (36, 48)",
            option_a="Column A is larger", option_b="Column (b) is larger", option_c="The two values ​​are equal", option_d="The relationship cannot be determined",
            correct_option="a",
            explanation_ar="Solution:\n Column (A): QM (6, 8) = 24\n Column (B): QM (36, 48) = 12\n 24 > 12 ← Column (A) is larger\n\nWhy are the other options Error:\n • (A) Column (A) is larger: An error in calculating the value of one of the two columns\n • (C) The two values are equal: An error in comparing the two values\n • (D) It is not possible to determine Relationship: The belief that it is not possible to determine even though values are specified",
            solution_steps_ar='["Column (A) = BC (6, 8) = 24","Column (B) = BC (36, 48) = 12","24 > 12 ← Column (A) is larger"]',
    tags="comparison,lcm-gcd", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        #── Q91: Comparison — Difficulty 0.6 ──
        Question(skill_id="quant_arithmetic", question_type="comparison", difficulty=0.6,
            text_ar="Compare: Column (A): A time of traveling 180 km at a speed of 90 km/h\n▸ Column (B): A time of traveling 120 km at a speed of 40 km/h",
            option_a="Column A is larger", option_b="Column (b) is larger", option_c="The two values ​​are equal", option_d="The relationship cannot be determined",
            correct_option="b",
            explanation_ar="Solution: Column (A) = 180 ÷ 90 = 2 hours Column (B) = 120 ÷ 40 = 3 hours 2 < 3 ← Column (B) is greater Why are the other options Error: • (A) Column (A) is greater: An error in calculating the value of one of the two columns\n • (B) Column (B) is greater: An error in comparing the two values\n • (D) The relationship cannot be determined: The belief that it cannot be determined Although the values are specific",
            solution_steps_ar='["Column A = 180 ÷ 90 = 2 hours","Column (B) = 120 ÷ 40 = 3 hours","2 < 3 ← Column (B) is greater"]',
    tags="comparison,speed", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        #── Q92: Comparison — Difficulty 0.6 ──
        Question(skill_id="quant_arithmetic", question_type="comparison", difficulty=0.6,
            text_ar="Compare:\n\n▸ Column (A): 500 riyals after a 40% discount\n▸ Column (B): 400 riyals after a 25% discount",
            option_a="Column A is larger", option_b="Column (b) is larger", option_c="The two values ​​are equal", option_d="The relationship cannot be determined",
            correct_option="c",
            explanation_ar="Solution: Column (A) = 500",
            solution_steps_ar='["Column (A) = 500 x (1 − 0.4) = 500 x 0.6 = 300","Column (B) = 400 x (1 − 0.25) = 400 x 0.75 = 300","300 = 300 ∴ The two values ​​are equal"]',
    tags="comparison,percentage,discount", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        #── Q93: Comparison — Difficulty 0.7 ──
        Question(skill_id="quant_arithmetic", question_type="comparison", difficulty=0.7,
            text_ar="Compare between:\n\n▸ Column (A): The price of 3 kg at 12 riyals/kg after a 10% discount\n▸ Column (B): The price of 4 kg at 10 riyals/kg after a 20% discount",
            option_a="Column A is larger", option_b="Column (b) is larger", option_c="The two values ​​are equal", option_d="The relationship cannot be determined",
            correct_option="a",
            explanation_ar="Solution: Column A = 3 x 12 x 0.9 = 36 x 0.9 = 32.4 Column B = 4 x 10 x 0.8 = 40 x 0.8 = 32 32.4 > 32 ← Column A is larger Why are the other options Error: Column A is larger: An error in calculating the value of one The two columns\n • (c) The two values are equal: an error in comparing the two values\n • (d) The relationship cannot be determined: the belief that it is not possible to determine even though the values are defined",
            solution_steps_ar='["Column A = 3 x 12 x 0.9 = 32.4","Column (B) = 4 x 10 x 0.8 = 32","32.4 > 32 ← Column (A) is larger"]',
    tags="comparison,percentage,discount", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        #── Q94: Comparison — Difficulty 0.7 ──
        Question(skill_id="quant_arithmetic", question_type="comparison", difficulty=0.7,
            text_ar="Compare:\n\n▸ Column (A): Average speed of a car that went 120 km at 60 km/h and returned at 40 km/h\n▸ Column (B): 50 km/h",
            option_a="Column A is larger", option_b="Column (b) is larger", option_c="The two values ​​are equal", option_d="The relationship cannot be determined",
            correct_option="b",
            explanation_ar="Solution:\n Column (A) = (2 x 60 x 40) ÷ (60 + 40) = 4800 ÷ 100 = 48 km/h\n Column (B) = 50 km/h\n 48 < 50 ← Column (B) is larger\n\nWhy are the other options wrong:\n • (A) Column (A) is larger: an error in calculating the value of one of the columns\n • (B) Column (B) Greater: An error in comparing the two values\n • (d) The relationship cannot be determined: the belief that it is not possible to determine even though the values are specified",
            solution_steps_ar='["Average speed = (2 x 60 x 40) ÷ (60 + 40)","= 4800 ÷ 100 = 48 km/h","48 < 50 ← Column (B) is larger"]',
    tags="comparison,average,speed", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        #── Q95: Comparison — Difficulty 0.7 ──
        Question(skill_id="quant_arithmetic", question_type="comparison", difficulty=0.7,
            text_ar="Compare:\n\n▸ Column (A): Compound interest on 1,000 riyals at a rate of 10% for two years\n▸ Column (B): 210 riyals",
            option_a="Column A is larger", option_b="Column (b) is larger", option_c="The two values ​​are equal", option_d="The relationship cannot be determined",
            correct_option="c",
            explanation_ar="Solution: Column (A): After year 1 = 1,000 The two columns\n • (c) The two values are equal: an error in comparing the two values\n • (d) The relationship cannot be determined: the belief that it is not possible to determine even though the values are defined",
            solution_steps_ar='["After year 1 = 1,000 x 1.1 = 1,100","After year 2 = 1,100 x 1.1 = 1,210","Interest = 1,210 − 1,000 = 210 = 210 ← equal"]',
    tags="comparison,percentage,compound-interest", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        #── Q96: Comparison — Difficulty 0.8 ──
        Question(skill_id="quant_arithmetic", question_type="comparison", difficulty=0.8,
            text_ar="Compare:\n\n▸ Column (A): Original item price 1,000 riyals after a 10% increase and then a 10% discount\n▸ Column (B): 1,000 riyals",
            option_a="Column A is larger", option_b="Column (b) is larger", option_c="The two values ​​are equal", option_d="The relationship cannot be determined",
            correct_option="b",
            explanation_ar="Solution:\n Column (A) = 1,000 x 1.1 x 0.9 = 1,100 x 0.9 = 990\n Column (B) = 1,000\n 990 < 1,000 ← Column (B) is larger\n\nWhy are the other options Error:\n • (B) Column (B) is larger: an error in calculating the value of one of the two columns\n • (C) the two values are equal: an error in the comparison Between the two values\n • (d) The relationship cannot be determined: the belief that it is not possible to determine even though the values are specified",
            solution_steps_ar='["Column A = 1,000 x 1.1 x 0.9 = 990","Column (B) = 1,000","990 < 1,000 ← Column (B) is greater"]',
    tags="comparison,percentage,discount", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        #── Q97: Comparison — Difficulty 0.8 ──
        Question(skill_id="quant_arithmetic", question_type="comparison", difficulty=0.8,
            text_ar="Compare:\n\n▸ Column (A): The number of days needed for 4 workers to finish a job that 6 workers can finish in 10 days\n▸ Column (B): 14 days",
            option_a="Column A is larger", option_b="Column (b) is larger", option_c="The two values ​​are equal", option_d="The relationship cannot be determined",
            correct_option="a",
            explanation_ar="Solution:\n Work volume = 6 The relationship can be determined: the belief that it cannot be determined even though the values are defined",
            solution_steps_ar='["Work size = 6 x 10 = 60","Column (A) = 60 ÷ 4 = 15 days","15 > 14 ← Column (A) is larger"]',
    tags="comparison,work-rate", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        #── Q98: Comparison — Difficulty 0.5 ──
        Question(skill_id="quant_arithmetic", question_type="comparison", difficulty=0.5,
            text_ar="Compare:\n\n▸ Column (A): 1,200 ÷ 40\n▸ Column (B): 900 ÷ 30",
            option_a="Column A is larger", option_b="Column (b) is larger", option_c="The two values ​​are equal", option_d="The relationship cannot be determined",
            correct_option="c",
            explanation_ar="Solution:\n Column (A) = 1,200 ÷ 40 = 30\n Column (B) = 900 ÷ 30 = 30\n The two values ​​are equal\n\nWhy are the other options Error:\n • (A) Column (A) is larger: an error in calculating the value of one of the two columns\n • (B) Column (B) is larger: an error in comparing the two values\n • (D) The relationship cannot be determined: the belief that it is not possible to determine even though the values ​​are determined",
            solution_steps_ar='["Column (A) = 1,200 ÷ 40 = 30","Column (B) = 900 ÷ 30 = 30","30 = 30 ∴ The two values ​​are equal"]',
    tags="comparison", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # ══════════════════════════════════════════════════════════════
        #██ The rest of the arithmetic questions to complete 111 ██
        # ══════════════════════════════════════════════════════════════

        # ── Q99 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.6,
            text_ar="If the sum of the ages of two brothers = 40 years, and the difference between them = 8 years.\nWhat is the age of the eldest?",
            option_a="20 years", option_b="22 years old", option_c="24 years old", option_d="28 years old",
            correct_option="c",
            explanation_ar="Solution:\n Let the largest = x, the smallest = y\n x + y = 40\n",
            solution_steps_ar='["x + y = 40, x − y = 8","Add: 2x = 48","x = 24 years"]',
    tags="age", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q100 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.6,
            text_ar="A faucet fills a basin in 4 hours, and a drain faucet empties it in 6 hours. If they are opened together, in how many hours does the basin fill?",
            option_a="8 hours", option_b="10 hours", option_c="12 hours", option_d="15 hours",
            correct_option="c",
            explanation_ar="Solution: Fill rate = ¼ tub/hour Drain rate = ⅙ tub/hour Net rate = ¼ − ⅙ = ³⁄₁₂ − ²⁄₁₂ = ¹⁄₁₂ Time = 1 ÷ ¹⁄₁₂ = 12 hours Why are the other options wrong: • (A) 50: The result of adding times instead of adding daily rates\n • (B) 60: The result of calculating the production of only one worker\n • (D) 80: The result of forgetting to subtract the portion completed from the total work",
            solution_steps_ar='["Fill rate = ¼, drain rate = ⅙","Net rate = ¼ − ⅙ = ¹⁄₁₂","Time = 1 ÷ ¹⁄₁₂ = 12 hours"]',
    tags="work-rate", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.43),

        # ── Q101 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.4,
            text_ar="If ⅕ of the students play football, and ¹⁰⁄₁ play basketball.\nThe total number = 100 students.\nHow many students do not play either?",
            option_a="50", option_b="60", option_c="70", option_d="80",
            correct_option="c",
            explanation_ar="Solution: Football = ⅕ × 100 = 20 Basketball = ¹⁄₁₀ × 100 = 10 Remainder = 100 − 20 − 10 = 70 Why are the other options wrong: • (a) A profit of 15%: As a result of forgetting to unify the denominators • (c) A loss of 50 riyals: As a result of calculating the deductible instead of the remainder or vice versa • (d) A profit of 200 riyals: As a result of an error in Multiply or divide fractions",
            solution_steps_ar='["Football = ⅕ x 100 = 20","Basketball = ¹⁄₁₀ x 100 = 10","Remainder = 100 − 20 − 10 = 70"]',
    tags="fraction", stage="mock",
    rating_clarity=4, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ── Q102 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.5,
            text_ar="A merchant bought goods for 2,000 riyals.\nHe sold half of them at a 40% profit and the other half at a 10% loss.\nWhat is the total profit or loss?",
            option_a="15% profit", option_b="He won 300 riyals", option_c="Loss of 50 riyals", option_d="He won 200 riyals",
            correct_option="b",
            explanation_ar="Solution:\n Cost of the half = 1,000 riyals for each half\n Revenue for the first half = 1,000 x 1.4 = 1,400\n Revenue for the second half = 1,000 x 0.9 = 900\n Total revenue = 1,400 + 900 = 2,300\n Profit = 2,300 − 2,000 = 300 riyals\n\nWhy are the other options wrong:\n • (A) 16 riyals: The result of calculating the ratio from the wrong number\n • (c) 800 riyals: The result of forgetting to subtract or add the ratio to the original number\n • (d) 4,000 riyals: The result of confusing the value of the ratio with the ratio itself",
            solution_steps_ar='["Cost of each half = 1,000 riyals","First half: 1,000 x 1.4 = 1,400","Second half: 1,000 x 0.9 = 900","Profit = 2,300 − 2,000 = 300 riyals"]',
    tags="percentage,profit", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.43),

        # ── Q103 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.6,
            text_ar="If the exchange rate of one pound sterling = 5 riyals.\nA traveler bought goods for 80 pounds and paid in riyals.\nHow much did he pay in riyals?",
            option_a="16 riyals", option_b="400 riyals", option_c="800 riyals", option_d="4,000 riyals",
            correct_option="b",
            explanation_ar="Solution: Amount = 80",
            solution_steps_ar='["Amount in riyals = number of pounds x exchange rate","= 80 x 5 = 400 riyals"]',
    tags="currency", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q104 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.7,
            text_ar="Mix 5 liters of a 10% solution with an amount of a 50% solution. If the concentration of the mixture becomes 30%, how many liters of the second solution are added?",
            option_a="3 litres", option_b="4 litres", option_c="5 litres", option_d="6 litres",
            correct_option="c",
            explanation_ar="Solution:\n Let the quantity of the second solution = k\n (5 x 0.1) + (k x 0.5) = (5 + k) x 0.3\n 0.5 + 0.5 k = 1.5 + 0.3 k\n 0.2 k = 1\n k = 5 liters\n\nWhy are the other options wrong:\n • (a) 6 hours: The result of calculating the ratio from the wrong number\n • (b) 7 hours: As a result of forgetting to subtract or add the ratio to the original number • (d) 8 hours: As a result of confusing the value of the ratio with the ratio itself",
            solution_steps_ar='["(5 x 0.1) + (K x 0.5) = (5 + K) x 0.3","0.5 + 0.5K = 1.5 + 0.3K","0.2K = 1 → K = 5 litres"]',
    tags="percentage,mixture", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ── Q105 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.4,
            text_ar="The flight time from Riyadh to Jeddah is 10 hours at a speed of 90 km/h. How many hours does the flight take at a speed of 120 km/h?",
            option_a="6 hours", option_b="7 hours", option_c="7.5 hours", option_d="8 hours",
            correct_option="c",
            explanation_ar="Solution: Distance = 90 ⅓: The result of an error in calculating the average speed",
            solution_steps_ar='["Distance = 90 x 10 = 900 km","Time = 900 ÷ 120 = 7.5 hours"]',
    tags="speed", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=4, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.29),

        # ── Q106 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.6,
            text_ar="If a worker completes ¼ of the work in two days, and ⅓ of the work in another 3 days.\nWhat is the remaining fraction of the work?",
            option_a="¹⁄₁₂", option_b="⁵⁄₁₂", option_c="⁷⁄₁₂", option_d="⅓",
            correct_option="b",
            explanation_ar="Solution:\n What has been accomplished = ¼ + ⅓ = ³⁄₁₂ + ⁴⁄₁₂ = ⁷⁄₁₂\n Remaining = 1 − ⁷⁄₁₂ = ⁵⁄₁₂\n\nWhy are the other options wrong:\n • (a) 150 grams: the result of forgetting to unify the denominators\n • (b) 300 grams: The result of calculating the cut off part instead of the remainder or vice versa • (d) 400 grams: The result of an error in multiplying or dividing fractions",
            solution_steps_ar='["Achieved = ¼ + ⅓ = ³⁄₁₂ + ⁴⁄₁₂ = ⁷⁄₁₂","Remaining = 1 − ⁷⁄₁₂ = ⁵⁄₁₂"]',
    tags="fraction,work-rate", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ── Q107 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.5,
            text_ar="If the ratio of copper to zinc in an alloy = 7:3.\nWhat is the amount of copper in an alloy weighing 500 grams?",
            option_a="150 grams", option_b="300 grams", option_c="350 grams", option_d="400 grams",
            correct_option="c",
            explanation_ar="Solution: Sum of parts = 7 + 3 = 10 Amount of copper = (7 ÷ 10)",
            solution_steps_ar='["Sum of parts = 7 + 3 = 10","Amount of copper = (7 ÷ 10) x 500 = 350 grams"]',
    tags="ratio,mixture", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.43),

        # ── Q108 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.4,
            text_ar="A farmer wanted to distribute 72 trees in equal rows. If he placed 9 trees in each row, how many rows would he need?",
            option_a="6 rows", option_b="7 rows", option_c="8 rows", option_d="9 rows",
            correct_option="c",
            explanation_ar="Solution:\n Number of rows = 72 ÷ 9 = 8 rows\n\nWhy are the other options wrong:\n • (a) 12.5%: The result of division by the wrong sum of parts\n • (b) 20%: The result of confusion between the share of the largest and smallest part\n • (d) 30%: The result of multiplication instead of division or vice versa",
            solution_steps_ar='["Number of rows = 72 ÷ 9 = 8"]',
    tags="ratio", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ── Q109 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.6,
            text_ar="The share price rose from 50 riyals to 62.5 riyals. What is the percentage of increase?",
            option_a="12.5%", option_b="20%", option_c="25%", option_d="30%",
            correct_option="c",
            explanation_ar="Solution:\n Height = 62.5 − 50 = 12.5\n Ratio = (12.5 ÷ 50) x 100 = 25%\n\nWhy are the other options wrong:\n • (a) 90 riyals: The result of calculating the ratio from the wrong number\n • (b) 100 riyals: The result of forgetting to subtract or add the ratio to the original number\n • (d) 150 riyals: The result of confusing the value of the ratio with the ratio itself",
            solution_steps_ar='["Height = 62.5 − 50 = 12.5","Ratio = (12.5 ÷ 50) x 100 = 25%"]',
    tags="percentage", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q110 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.3,
            text_ar="If the price of 5 meters of fabric = 75 riyals.\nHow much is the price of 8 meters of the same fabric?",
            option_a="90 riyals", option_b="100 riyals", option_c="120 riyals", option_d="150 riyals",
            correct_option="c",
            explanation_ar="Solution: Price per meter = 75 ÷ 5 = 15 riyals Price of 8 meters = 8",
            solution_steps_ar='["Price per meter = 75 ÷ 5 = 15 riyals","Price for 8 meters = 8 x 15 = 120 riyals"]',
    tags="ratio", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q111 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.7,
            text_ar="A worker completes ²⁄₅ work in 6 hours.\nAnother worker with the same efficiency joins him.\nHow many hours do they need to complete the remaining work?",
            option_a="3 hours", option_b="4 hours", option_c="4.5 hours", option_d="6 hours",
            correct_option="c",
            explanation_ar="Solution:\n Rate of one worker = ²⁄₅ ÷ 6 = ²⁄₃₀ = ¹⁄₁₅ work/hour\n Remaining = 1 − ²⁄₅ = ³⁄₅\n Rate of both together = ²⁄₁₅ work/hour\n Time = ³⁄₅ ÷ ²⁄₁₅ = ³⁄₅ × ¹⁵⁄₂ = ⁴⁵⁄₁₀ = 4.5 hours\n\nWhy are the other options wrong:\n • (a) 3 hours: As a result of forgetting to unify denominators\n • (b) 4 hours: As a result of calculating the intercept instead of the remainder or vice versa\n • (d) 6 hours: As a result of an error in multiplying fractions Or divided it",
            solution_steps_ar='["Worker rate = ²⁄₅ ÷ 6 = ¹⁄₁₅ work/hour","Residual = 1 − ²⁄₅ = ³⁄₅","Together = ²⁄₁₅, time = ³⁄₅ ÷ ²⁄₁₅ = 4.5 hours"]',
    tags="fraction,work-rate", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ══════════════════════════════════════════════════════════════
        #██ New questions (112–167) ██
        # ══════════════════════════════════════════════════════════════

        #── Q112: Value Added Tax ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.3,
            text_ar="The price of an electronic device before tax = 2000 riyals.\nIf the value-added tax = 15%, what is the price including the tax?",
            option_a="2150 riyals", option_b="2300 riyals", option_c="2200 riyals", option_d="2500 riyals",
            correct_option="b",
            explanation_ar="Solution: Tax = 2000",
            solution_steps_ar='["Tax = 2000 x 0.15 = 300 riyals","Total price = 2000 + 300 = 2300 riyals"]',
    tags="percentage,tax", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.43),

        #── Q113: Tax — Find the original price ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.5,
            text_ar="Saeed paid 1,150 riyals for the phone, including 15% value-added tax.\nWhat is the price before tax?",
            option_a="977.5 riyals", option_b="1000 riyals", option_c="1035 riyals", option_d="1050 riyals",
            correct_option="b",
            explanation_ar="Solution: Price including tax = original price",
            solution_steps_ar='["Price including tax = original x 1.15","original = 1150 ÷ ​​1.15 = 1000 riyals"]',
    tags="percentage,tax", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        #── Q114: Installments ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.4,
            text_ar="Muhammad bought a car in installments. He paid 10,000 riyals in advance, then 24 monthly installments. The value of each installment = 2,500 riyals. How much was the total amount paid?",
            option_a="60,000 riyals", option_b="70,000 riyals", option_c="75,000 riyals", option_d="80,000 riyals",
            correct_option="b",
            explanation_ar="Solution: Total installments = 24",
            solution_steps_ar='["Total installments = 24 x 2500 = 60,000 riyals","Total = 10,000 + 60,000 = 70,000 riyals"]',
    tags="percentage,installment", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        #── Q115: Installments with interest ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.6,
            text_ar="Bank loan = 60,000 riyals with a simple interest of 10% annually for 3 years.\nWhat is the total amount paid?",
            option_a="72,000 riyals", option_b="78,000 riyals", option_c="80,000 riyals", option_d="66,000 riyals",
            correct_option="b",
            explanation_ar="Solution: Interest = 60,000",
            solution_steps_ar='["Simple interest = 60,000 x 0.10 x 3 = 18,000 riyals","Total = 60,000 + 18,000 = 78,000 riyals"]',
    tags="percentage,installment", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        #── Q116: Convert km to meters ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.2,
            text_ar="Distance between two cities = 3.5 km.\nHow much is this distance equal in meters?",
            option_a="35 metres", option_b="350 metres", option_c="3500 meters", option_d="35000 meters",
            correct_option="c",
            explanation_ar="Solution:\n 1 km = 1000 metres\n 3.5 km = 3.5",
            solution_steps_ar='["1 km = 1000 metres","3.5 x 1000 = 3500 metres"]',
    tags="unit-conversion", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        #── Q117: Convert kilograms to grams ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.3,
            text_ar="Weight of a bag = 2.75 kg.\nHow much is it worth in grams?",
            option_a="27.5 grams", option_b="275 grams", option_c="2750 grams", option_d="27500 grams",
            correct_option="c",
            explanation_ar="Solution: 1 kg = 1000 grams 2.75 kg = 2.75",
            solution_steps_ar='["1 kg = 1000 grams","2.75 x 1000 = 2750 grams"]',
    tags="unit-conversion", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        #── Q118: Convert hours to minutes ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.3,
            text_ar="The journey took 3 hours and 40 minutes.\nWhat is the time in minutes?",
            option_a="180 minutes", option_b="200 minutes", option_c="220 minutes", option_d="340 minutes",
            correct_option="c",
            explanation_ar="Solution:\n 3 hours = 3",
            solution_steps_ar='["3 hours = 3 x 60 = 180 minutes","Total = 180 + 40 = 220 minutes"]',
    tags="unit-conversion", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.29),

        #── Q119: Consecutive discounts ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.6,
            text_ar="Dress price = 400 riyals.\nI got a 20% discount, then an additional 10% discount on the price after the first discount.\nWhat is the final amount?",
            option_a="280 riyals", option_b="288 riyals", option_c="300 riyals", option_d="320 riyals",
            correct_option="b",
            explanation_ar="Solution:\n After the first discount = 400",
            solution_steps_ar='["After the first discount = 400 x 0.80 = 320 riyals","After the second discount = 320 x 0.90 = 288 riyals"]',
    tags="percentage,discount,successive-discount", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        #── Q120: Consecutive discounts — compared to a single discount ──
        Question(skill_id="quant_arithmetic", question_type="comparison", difficulty=0.6,
            text_ar="Compare:\n\n▸ Column (A): 30% discount once on 1,000 riyals\n▸ Column (B): 20% discount, then 10% successive discount on 1,000 riyals",
            option_a="Column A is larger", option_b="Column (b) is larger", option_c="The two values ​​are equal", option_d="The relationship cannot be determined",
            correct_option="a",
            explanation_ar="Calculating each column: Column A: 1000 (A) 3 hours: An error in calculating the value of one of the two columns\n • (C) 5 hours: An error in comparing the two values\n • (D) 9 hours: The belief that it is not possible to determine even though the values are specified",
            solution_steps_ar='["Column A: Discount = 1000',
    tags="comparison,discount,successive-discount", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.43),

        #── Q121: Pipes filling a basin ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.6,
            text_ar="One tube fills a basin in 6 hours, and another tube fills it in 12 hours.\nIf they work together, how many hours does it take to fill the basin?",
            option_a="3 hours", option_b="4 hours", option_c="5 hours", option_d="9 hours",
            correct_option="b",
            explanation_ar="Solution:\n The rate of the first = ¹⁄₆ basin/hour\n The rate of the second = ¹⁄₁₂ basin/hour\n Together = ¹⁄₆ + ¹⁄₁₂ = ²⁄₁₂ + ¹⁄₁₂ = ³⁄₁₂ = ¼\n Time = 1 ÷ ¼ = 4 hours\n\nWhy are the other options wrong:\n • (a) 12 hours: the result of adding times instead of adding daily rates\n • (b) 20 hours: the result of calculating the production of only one worker\n • (d) 16 hours: the result of forgetting to subtract the portion completed from the total work",
            solution_steps_ar='["First rate = ¹⁄₆, second rate = ¹⁄₁₂","Together = ¹⁄₆ + ¹⁄₁₂ = ¼ basin/hour","Time = 1 ÷ ¼ = 4 hours"]',
    tags="work-rate,pipes", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        #── Q122: Filling tube and draining tube ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.7,
            text_ar="A tube fills a tank in 8 hours, and a drain tube empties it in 12 hours. If they are opened together and the tank is empty, in how many hours will the tank be filled?",
            option_a="12 hours", option_b="20 hours", option_c="24 hours", option_d="16 hours",
            correct_option="c",
            explanation_ar="Solution:\n Filling rate = ¹⁄₈ tank/hour\n Discharge rate = ¹⁄₁₂ tank/hour\n Net rate = ¹⁄₈ − ¹⁄₁₂ = ³⁄₂₄ − ²⁄₂₄ = ¹⁄₂₄\n Time = 1 ÷ ¹⁄₂₄ = 24 hours\n\nWhy are the other options wrong:\n • (b) 2.5 hours: the result of adding times instead of adding daily rates\n • (c) 3 hours: the result of calculating the production of only one worker\n • (d) 4 hours: the result of forgetting to subtract the portion completed from the total work",
            solution_steps_ar='["Fill = ¹⁄₈, Drain = ¹⁄₁₂","Net = ¹⁄₈ − ¹⁄₁₂ = ¹⁄₂₄ Tank/hour","Time = 24 hours"]',
    tags="work-rate,pipes", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        #── Q123: Two trains meet ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.5,
            text_ar="A train departed from City A at a speed of 80 km/h, and another train from City B at a speed of 120 km/h towards each other.\nThe distance between the two cities = 400 km.\nAfter how many hours will they meet?",
            option_a="Two hours", option_b="2.5 hours", option_c="3 hours", option_d="4 hours",
            correct_option="a",
            explanation_ar="The solution: The sum of the two speeds = 80 + 120 = 200 km/h The encounter time = 400 ÷ 200 = 2 hours Why are the other options wrong: • (a) 40 seconds: The result of forgetting to convert units between hours and minutes or km/h and m/s\n • (c) 60 seconds: The result of using distance instead of time in the equation • (d) 72 seconds: The result of an error in calculating average speed",
            solution_steps_ar='["Sum of the two speeds = 80 + 120 = 200 km/h","Meeting time = 400 ÷ 200 = 2 hours"]',
    tags="speed,train", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        #── Q124: A train crosses a bridge ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.7,
            text_ar="The length of a train = 200 metres, and the length of a bridge = 800 metres. The speed of the train = 72 km/h. How many seconds does it take the train to completely cross the bridge?",
            option_a="40 seconds", option_b="50 seconds", option_c="60 seconds", option_d="72 seconds",
            correct_option="b",
            explanation_ar="Solution: Total distance = 200 + 800 = 1000 meters Speed in meters/second = 72 In the equation\n • (d) 120°: the result of an error in calculating the average speed",
            solution_steps_ar='["Distance = 200 + 800 = 1000 metres","Speed ​​= 72 km/h = 20 m/s","Time = 1000 ÷ 20 = 50 seconds"]',
    tags="speed,train,unit-conversion", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.43),

        #── Q125: Clockwise angle ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.7,
            text_ar="What is the angle between the clock hands at 3:00?",
            option_a="60°", option_b="75°", option_c="90°", option_d="120°",
            correct_option="c",
            explanation_ar="Solution: Every hour = 360° ÷ 12 = 30° At 3:00 the difference = 3 hours = 3",
            solution_steps_ar='["Every hour on a clock face = 30°","At 3:00 the difference = 3 x 30° = 90°"]',
    tags="clock-angle", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        #── Q126: Clockwise angle — advanced ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.8,
            text_ar="What is the angle between the clock hands at 4:30?",
            option_a="30°", option_b="45°", option_c="60°", option_d="75°",
            correct_option="b",
            explanation_ar="Solution: The minute hand at 30 minutes = 180° The hour hand at 4:30 = 4 True\n • (D) 29: As a result of forgetting a step in the solution or performing an incorrect operation",
            solution_steps_ar='["minute hand = 180°","hour hand = 4 x 30 + 30 x 0.5 = 135°","angle = 180 − 135 = 45°"]',
    tags="clock-angle", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        #── Q127: Numbers problem — sum ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.5,
            text_ar="A two-digit number, the sum of its digits = 11, and the ones digit is 3 more than the tens digit. What is the number?",
            option_a="38", option_b="47", option_c="56", option_d="29",
            correct_option="b",
            explanation_ar="Solution:\n p + a = 11, a = p + 3\n p + (p + 3) = 11 → 2p = 8 → p = 4, a = 7\n Number = 47\n\nWhy are the other options wrong:\n • (b) 45: The result of a common arithmetic error in one of the steps\n • (c) 27: The result of applying the law or relationship incorrectly\n • (d) 18: The result of forgetting a step in the solution or performing an operation Wrong",
            solution_steps_ar='["p + a = 11, a − p = 3","2p + 3 = 11 → p = 4, a = 7","number = 47"]',
    tags="digit-problem", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.43),

        #── Q128: A number problem — the opposite of a number ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.6,
            text_ar="A two-digit number. If we reverse its numbers, we get a number that is 27 more than the original.\nIf the sum of the two numbers = 9, what is the original number?",
            option_a="36", option_b="45", option_c="27", option_d="18",
            correct_option="a",
            explanation_ar="Solution: A + A = 9 Converse − Origin = 27 (10 A + A) − (10 A + A) = 27 9(A − A) = 27 → A − A = 3 A = 6, A = 3 → Number = 36 Why are the other options wrong: (A) 90: The result of a common arithmetic error in one of the steps\n • (B) 100: The result of applying the law or relationship incorrectly Incorrect\n • (D) 120: As a result of forgetting a step in the solution or performing an incorrect operation",
            solution_steps_ar='["p + a = 9, 9(a − p) = 27 → a − p = 3","p = 3, a = 6","number = 36"]',
    tags="digit-problem", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        #── Q129: Division — Odd/Even ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.4,
            text_ar="What is the sum of the even numbers from 2 to 20 (inclusive)?",
            option_a="90", option_b="100", option_c="110", option_d="120",
            correct_option="c",
            explanation_ar="Solution:\n Numbers: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20\n Their number = 10\n Total = (2 + 20) × 10 ÷ 2 = 22 The relationship incorrectly\n • (D) 28: As a result of forgetting a step in the solution or performing an incorrect operation",
            solution_steps_ar='["Even numbers from 2 to 20: their number = 10","Total = (2 + 20) x 10 ÷ 2 = 110"]',
    tags="number-properties", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        #── Q130: Divisibility ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.4,
            text_ar="Which of the following numbers is divisible by both 3 and 4?",
            option_a="18", option_b="20", option_c="24", option_d="28",
            correct_option="c",
            explanation_ar="Solution:\n 18 ÷ 4 = 4.5 ✗\n 20 ÷ 3 = 6.67 ✗\n 24 ÷ 3 = 8 ✓, 24 ÷ 4 = 6 ✓\n 28 ÷ 3 = 9.33 ✗\n\nWhy are the other options wrong:\n • (A) Column (A) is larger: this is Q.M.A. instead of M.M.A., or vice versa\n • (b) Column (b) is larger: the result of directly multiplying the two numbers\n • (d) The relationship cannot be determined: the result of an error in prime factor analysis",
            solution_steps_ar='["We test division by 3 and 4","24 ÷ 3 = 8 ✓, 24 ÷ 4 = 6 ✓","Answer = 24"]',
    tags="number-properties,lcm-gcd", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        #── Q131: Comparison — Tax ──
        Question(skill_id="quant_arithmetic", question_type="comparison", difficulty=0.5,
            text_ar="Compare:\n\n▸ Column (A): 15% of 800 riyals (tax value)\n▸ Column (B): 120 riyals",
            option_a="Column A is larger", option_b="Column (b) is larger", option_c="The two values ​​are equal", option_d="The relationship cannot be determined",
            correct_option="c",
            explanation_ar="Calculating each column: Column (A) = 800",
            solution_steps_ar='["Column (A) = 800 x 0.15 = 120","Column (B) = 120","120 = 120 ∴ The two values ​​are equal"]',
    tags="comparison,tax,percentage", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        #── Q132: Tax — Calculate the tax amount ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.3,
            text_ar="Restaurant bill = 340 riyals before tax.\nIf a 15% tax is added, how much is the tax value only?",
            option_a="45 riyals", option_b="51 riyals", option_c="55 riyals", option_d="60 riyals",
            correct_option="b",
            explanation_ar="Solution: Tax = 340 x 0.15 = 51 riyals Why are the other options wrong?",
            solution_steps_ar='["Tax = 340 x 0.15 = 51 riyals"]',
    tags="percentage,tax", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        #── Q133: Installments — number of months ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.5,
            text_ar="The price of the device = 9,600 riyals. Ahmed paid 1,600 riyals in advance, and the rest in monthly installments = 400 riyals. How many months does he need to pay the installments?",
            option_a="16 months", option_b="20 months", option_c="24 months", option_d="12 months",
            correct_option="b",
            explanation_ar="The solution:\n The remaining amount = 9600 − 1600 = 8000 riyals\n Number of months = 8000 ÷ 400 = 20 months\n\nWhy the other options Error:\n • (a) 0.45 km: as a result of a common arithmetic error in one of the steps\n • (c) 45 km: as a result of applying the law or relationship incorrectly\n • (d) 450 km: as a result of forgetting a step in the solution or performing a wrong operation",
            solution_steps_ar='["Remaining = 9600 − 1600 = 8000 riyals","Number of months = 8000 ÷ 400 = 20 months"]',
    tags="installment", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        #── Q134: Convert meters to kilometers ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.3,
            text_ar="Walking distance = 4500 metres. How much is it in kilometers?",
            option_a="0.45 km", option_b="4.5 km", option_c="٤٥ كم", option_d="450 km",
            correct_option="b",
            explanation_ar="Solution:\n 1 km = 1000 metres\n 4500 meters = 4500 ÷ 1000 = 4.5 km\n\nWhy are the other options wrong:\n • (b) Column (b) is larger: as a result of using the conversion factor in the opposite direction\n • (c) The two values ​​are equal: as a result of forgetting the number of zeros in the conversion\n • (d) The relationship cannot be determined: as a result of confusion between the units of measurement",
            solution_steps_ar='["1 km = 1000 metres","4500 ÷ 1000 = 4.5 km"]',
    tags="unit-conversion", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        #── Q135: Comparison — units ──
        Question(skill_id="quant_arithmetic", question_type="comparison", difficulty=0.4,
            text_ar="Compare: Column A: 3.2 km Column B: 3150 meters",
            option_a="Column A is larger", option_b="Column (b) is larger", option_c="The two values ​​are equal", option_d="The relationship cannot be determined",
            correct_option="a",
            explanation_ar="Calculating each column:\n Column (A) = 3.2 km = 3200 meters\n Column (B) = 3150 meters\n\n 3200 > 3150 ∴ Column (A) is larger\n\nWhy are the other options an error:\n • (A) 700 riyals: Error in calculating the value of one of the two columns\n • (C) 730 riyals: Error in comparing the two values\n • (D) 750 SAR: The belief that it is not possible to determine even though the values are specified",
            solution_steps_ar='["Column A = 3.2',
    tags="comparison,unit-conversion", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        #── Q136: Triple consecutive discounts ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.7,
            text_ar="Price of an item = 1000 riyals.\nI got successive discounts: 10%, then 10%, then 10%.\nWhat is the final price?",
            option_a="700 riyals", option_b="729 riyals", option_c="730 riyals", option_d="750 riyals",
            correct_option="b",
            explanation_ar="Solution: After the first = 1000 The value of the ratio and the ratio itself",
            solution_steps_ar='["After the first discount = 1000 x 0.9 = 900","After the second = 900 x 0.9 = 810","After the third = 810 x 0.9 = 729 riyals"]',
    tags="percentage,successive-discount", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q137: أنبوبان يملآن ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.5,
            text_ar="Tube (A) fills a basin in 10 hours, and tube (B) fills it in 15 hours.\nIf (A) works alone for 5 hours and then (B) is opened with him, how many additional hours until it is full?",
            option_a="2 hours", option_b="3 hours", option_c="4 hours", option_d="5 hours",
            correct_option="b",
            explanation_ar="Solution:\n Complete (A) in 5 hours = ⁵⁄₁₀ = ½\n Remaining = ½\n Average them together = ¹⁄₁₀ + ¹⁄₁₅ = ³⁄₃₀ + ²⁄₃₀ = ⁵⁄₃₀ = ¹⁄₆\n Time = ½ ÷ ¹⁄₆ = ½ x 6 = 3 hours\n\nWhy are the other options wrong:\n • (b) 3 hours: The result of adding times instead of adding daily rates\n • (c) 4 hours: The result of calculating the production of only one worker\n • (d) 5 hours: The result of forgetting to subtract the portion completed from the total work",
            solution_steps_ar='["(A) Complete ½ in 5 hours","Remaining = ½, average = ¹⁄₆","Time = ½ ÷ ¹⁄₆ = 3 hours"]',
    tags="work-rate,pipes", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        #── Q138: Two trains — same direction ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.6,
            text_ar="A fast train is moving at a speed of 150 km/h, and a slow train is in front of it at a speed of 90 km/h.\nThe distance between them = 120 km.\nAfter how many hours will the fast train catch up with the slow one?",
            option_a="Two hours", option_b="3 hours", option_c="٤ ساعات", option_d="5 hours",
            correct_option="a",
            explanation_ar="The solution:\n The difference in speeds = 150 − 90 = 60 km/h\n Time = 120 ÷ 60 = 2 hours\n\nWhy are the other options wrong:\n • (a) Column (A) is larger: as a result of forgetting to convert units between hours and minutes or km/h and m/s\n • (b) Column (B) is larger: as a result of using distance instead of time in the equation\n • (d) The relationship cannot be determined: as a result of an error in calculating average speed",
            solution_steps_ar='["The difference in speed = 150 − 90 = 60 km/h","Time = 120 ÷ 60 = 2 hours"]',
    tags="speed,train", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.43),

        #── Q139: 9:00 o’clock corner ──
        Question(skill_id="quant_arithmetic", question_type="comparison", difficulty=0.4,
            text_ar="Compare:\n\n▸ Column (A): The angle between the two hands of the clock at 9:00\n▸ Column (B): 270°",
            option_a="Column A is larger", option_b="Column (b) is larger", option_c="The two values ​​are equal", option_d="The relationship cannot be determined",
            correct_option="c",
            explanation_ar="Calculating each column: Column A: At 9:00 the difference = 9 (d) 92: The belief that it is not possible to determine even though values are specified",
            solution_steps_ar='["At 9:00 the hour hand is at 270°","Column (B) = 270°","270 = 270 ∴ are equal"]',
    tags="comparison,clock-angle", stage="foundation",
    rating_clarity=4, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        #── Q140: Numbers problem — multiplication product ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.6,
            text_ar="A two-digit number, the product of its two numbers = 18, and the difference between them = 3. What is the largest possible number?",
            option_a="36", option_b="63", option_c="29", option_d="92",
            correct_option="b",
            explanation_ar="Solution:\n We are looking for two numbers whose multiplication = 18 and difference = 3\n 6 x 3 = 18 ✓, 6 − 3 = 3 ✓\n The two possible numbers: 36 and 63\n The largest of them = 63\n\nWhy are the other options wrong:\n • (a) 453: The result of a common arithmetic error in one of the steps\n • (c) 514: The result of applying the law or relationship incorrectly True\n • (d) 836: The result of forgetting a step in the solution or performing an incorrect operation",
            solution_steps_ar='["6 x 3 = 18, 6 − 3 = 3","The numbers: 36 and 63","The largest = 63"]',
    tags="digit-problem", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.43),

        #── Q141: Divisibility by 9 ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.4,
            text_ar="Which of the following numbers is divisible by 9?",
            option_a="453", option_b="729", option_c="٥١٤", option_d="836",
            correct_option="b",
            explanation_ar="Solution:\n Sum of 729 numbers = 7 + 2 + 9 = 18\n 18 ÷ 9 = 2 ✓\n Sum of 453 numbers = 12 (not accepted)\n Sum of 514 numbers = 10 (not accepted)\n Sum of 836 numbers = 17 (not accepted)\n\nWhy the other options are wrong:\n • (a) Column (A) is larger: the result of a common arithmetic error in one of the steps\n • (B) Column (b) Greater: as a result of applying the law or relationship incorrectly\n • (d) The relationship cannot be determined: as a result of forgetting a step in the solution or performing an incorrect operation",
            solution_steps_ar='["A number is divisible by 9 if the sum of its digits is a multiple of 9","The sum of the digits of 729 = 18, and 18 ÷ 9 = 2 ✓"]',
    tags="number-properties", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.43),

        #── Q142: Comparison — Pipes ──
        Question(skill_id="quant_arithmetic", question_type="comparison", difficulty=0.6,
            text_ar="Compare:\n\n▸ Column (A): Time to fill a basin with two pipes together (one fills it in 4 hours and the other in 4 hours)\n▸ Column (B): 2 hours",
            option_a="Column A is larger", option_b="Column (b) is larger", option_c="The two values ​​are equal", option_d="The relationship cannot be determined",
            correct_option="c",
            explanation_ar="Calculating each column:\n Column (A): Their rate = ¼ + ¼ = ½, time = 2 hours\n Column (B) = 2 hours\n\n∴ The two values ​​are equal\n\nWhy are the other options wrong:\n • (B) 2100 riyals: An error in calculating the value of one of the two columns\n • (C) 1890 riyals: An error in comparing the two values\n • (D) 1950 riyals: The belief that it is not possible to determine even though the values ​​are specified",
            solution_steps_ar='["Their rate = ¼ + ¼ = ½ basin/hour","Time = 1 ÷ ½ = 2 hours","2 = 2 ∴ are equal"]',
    tags="comparison,pipes,work-rate", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        #── Q143: Tax + discount together ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.6,
            text_ar="Device price = 2000 riyals.\nI got a 10% discount, then a 15% tax was added to the price after the discount.\nHow much do you pay?",
            option_a="2070 riyals", option_b="2100 riyals", option_c="1890 riyals", option_d="1950 riyals",
            correct_option="a",
            explanation_ar="Solution: After discount = 2000 2 hours and 45 minutes: the result of confusion between the value of the ratio and the ratio itself",
            solution_steps_ar='["After discount = 2000 x 0.9 = 1800","Tax = 1800 x 0.15 = 270","Total = 1800 + 270 = 2070 riyals"]',
    tags="percentage,tax,discount", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        #── Q144: Convert minutes to hours ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.2,
            text_ar="Movie duration = 150 minutes.\nHow much is it worth in hours and minutes?",
            option_a="1 hour and 50 minutes", option_b="2 hours and 10 minutes", option_c="2 hours and 30 minutes", option_d="2 hours and 45 minutes",
            correct_option="c",
            explanation_ar="The solution:\n 150 ÷ ​​60 = 2 hours and the remaining 30 minutes\n = 2 hours and 30 minutes\n\nWhy are the other options wrong:\n • (a) 11,000 riyals: The result of using the conversion factor in the opposite direction\n • (b) 12,000 riyals: The result of forgetting the number of zeros in the conversion\n • (d) 12,200 riyals: The result of mixing up the units of measurement",
            solution_steps_ar='["150 ÷ ​​60 = 2 remaining 30","= 2 hours and 30 minutes"]',
    tags="unit-conversion", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        #── Q145: Compound interest ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.8,
            text_ar="Khaled deposited 10,000 riyals with a compound interest of 10% annually.\nHow much will the amount become after two years?",
            option_a="11,000 riyals", option_b="12,000 riyals", option_c="١٢١٠٠ ريال", option_d="12,200 riyals",
            correct_option="c",
            explanation_ar="Solution:\n After the first year = 10,000",
            solution_steps_ar='["After one year = 10,000 x 1.1 = 11,000","After two years = 11,000 x 1.1 = 12,100 riyals"]',
    tags="compound-interest", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        #── Q146: Comparison — simple and compound interest ──
        Question(skill_id="quant_arithmetic", question_type="comparison", difficulty=0.7,
            text_ar="Compare: Column (A): Simple interest on 5,000 riyals at 10% for 2 years Column (B): Compound interest on 5,000 riyals at 10% for 2 years",
            option_a="Column A is larger", option_b="Column (b) is larger", option_c="The two values ​​are equal", option_d="The relationship cannot be determined",
            correct_option="b",
            explanation_ar="Calculate each column: Column A: simple interest = 5000 In comparing the two values\n • (d) 18 seconds: The belief that it is not possible to determine even though the values are specified",
            solution_steps_ar='["Simple = 5000 x 0.1 x 2 = 1000","Compound: 5000 → 5500 → 6050, interest = 1050","1050 > 1000 ∴ Column (B) is greater"]',
    tags="comparison,compound-interest", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        #── Q147: A train passes in front of a person ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.5,
            text_ar="The length of a train = 180 meters and its speed = 54 km/h.\nHow many seconds does it take a standing person to cross?",
            option_a="10 seconds", option_b="12 seconds", option_c="15 seconds", option_d="18 seconds",
            correct_option="b",
            explanation_ar="Solution: Speed ​​in meters/second = 54",
            solution_steps_ar='["Speed ​​= 54 km/h = 15 m/s","Time = 180 ÷ 15 = 12 seconds"]',
    tags="speed,train,unit-conversion", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        #── Q148: Numbers problem — sum = product ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.4,
            text_ar="Two positive integers whose sum = 11 and their product = 30. What is the difference between them?",
            option_a="1", option_b="3", option_c="5", option_d="7",
            correct_option="a",
            explanation_ar="Solution: We look for two numbers whose sum is 11 and multiply them by 30. 5 As a result of forgetting a step in the solution or performing an incorrect operation",
            solution_steps_ar='["5 + 6 = 11 ✓, 5 x 6 = 30 ✓","Difference = 6 − 5 = 1"]',
    tags="digit-problem", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.43),

        #── Q149: Comparison — converting weights ──
        Question(skill_id="quant_arithmetic", question_type="comparison", difficulty=0.3,
            text_ar="Compare: Column A: 2.5 kg Column B: 2400 grams",
            option_a="Column A is larger", option_b="Column (b) is larger", option_c="The two values ​​are equal", option_d="The relationship cannot be determined",
            correct_option="a",
            explanation_ar="Calculating each column: Column (A) = 2.5 kg = 2500 grams Column B = 2400 grams 2500 > 2400 ∴ Column A is larger Why are the other options wrong: A (A) 195.65 riyals: error in calculating the value of one of the two columns C) 210 riyals: error in comparing the two values D) 215 riyals: believing that it is not possible Identification even though the values are specified",
            solution_steps_ar='["Column (A) = 2.5 x 1000 = 2500 grams","Column (B) = 2400 grams","2500 > 2400 ∴ Column (A) is larger"]',
    tags="comparison,unit-conversion", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        #── Q150: Tax on service ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.4,
            text_ar="Internet subscription cost = 230 riyals per month, including 15% tax.\nHow much is the monthly cost before tax?",
            option_a="195.65 riyals", option_b="200 riyals", option_c="210 riyals", option_d="215 riyals",
            correct_option="b",
            explanation_ar="The solution:\n The price including the price",
            solution_steps_ar='["Price x 1.15 = 230","Price = 230 ÷ 1.15 = 200 riyals"]',
    tags="percentage,tax", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        #── Q151: Tubes — three tubes ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.7,
            text_ar="Three tubes fill a basin: the first in 6 hours, the second in 8 hours, and the third in 12 hours. How many hours does it take to fill it if all three work together?",
            option_a="2 hours", option_b="2.4 hours", option_c="٢٫٦٧ ساعة", option_d="3 hours",
            correct_option="c",
            explanation_ar="Solution: Rate = ¹⁄₆ + ¹⁄₈ + ¹⁄₁₂\n = ⁴⁄₂₄ + ³⁄₂₄ + ²⁄₂₄ = ⁹⁄₂₄ = ³⁄₈\n Time = ⁘",
            solution_steps_ar='["Rate = ¹⁄₆ + ¹⁄₈ + ¹⁄₁₂ = ³⁄₈ basin/hour","Time = ⁸⁄₃ ≈ 2.67 hours"]',
    tags="work-rate,pipes", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        #── Q152: 6:20 o’clock angle ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.8,
            text_ar="What is the (minimum) angle between the clock hands at 6:20?",
            option_a="60°", option_b="70°", option_c="80°", option_d="90°",
            correct_option="b",
            explanation_ar="Solution: The minute hand at 20 minutes = 20 Incorrectly\n • (D) 31: As a result of forgetting a step in the solution or performing an incorrect operation",
            solution_steps_ar='["minute hand = 20 x 6 = 120°","hour hand = 180 + 10 = 190°","angle = 190 − 120 = 70°"]',
    tags="clock-angle", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        #── Q153: Consecutive odd numbers ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.5,
            text_ar="Three consecutive odd numbers whose sum = 81.\nWhat is the largest?",
            option_a="25", option_b="27", option_c="29", option_d="31",
            correct_option="c",
            explanation_ar="Solution: Numbers: x, 38%: As a result of forgetting a step in the solution or performing an incorrect operation",
            solution_steps_ar='["3x + 6 = 81 → x = 25","Numbers: 25, 27, 29","largest = 29"]',
    tags="number-properties", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        #── Q154: Consecutive discount — actual discount percentage ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.7,
            text_ar="A customer received two consecutive discounts of 20% and 25%.\nWhat is the actual total discount percentage?",
            option_a="40%", option_b="45%", option_c="35%", option_d="38%",
            correct_option="a",
            explanation_ar="Solution: Let's assume the price = 100 After 20% = 100 Adding the ratio to the original number\n • (d) 480 riyals: The result of confusion between the value of the ratio and the ratio itself",
            solution_steps_ar='["We charge the price as 100","After 20% = 80, after 25% = 60","Actual discount = 40%"]',
    tags="percentage,successive-discount", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        #── Q155: monthly installment with interest ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.7,
            text_ar="Saad bought a refrigerator for 4,000 riyals in installments over 10 months with a 5% increase on the total price. How much is the monthly installment?",
            option_a="400 riyals", option_b="420 riyals", option_c="450 riyals", option_d="480 riyals",
            correct_option="b",
            explanation_ar="Solution: Total = 4000",
            solution_steps_ar='["Total = 4000 x 1.05 = 4200 riyals","Instalment = 4200 ÷ 10 = 420 riyals"]',
    tags="installment,percentage", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        #── Q156: Speed ​​conversion ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.4,
            text_ar="Car speed = 90 km/h. How much is it in meters/second?",
            option_a="15 m/s", option_b="20 m/s", option_c="٢٥ م/ث", option_d="30 m/s",
            correct_option="c",
            explanation_ar="Solution: 90 km/h = 90",
            solution_steps_ar='["90 km/h = 90 x 1000 ÷ 3600","= 25 m/s"]',
    tags="unit-conversion,speed", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        #── Q157: Comparison — Installments ──
        Question(skill_id="quant_arithmetic", question_type="comparison", difficulty=0.5,
            text_ar="Compare:\n\n▸ Column (A): Total installments (12 installments x 500 riyals)\n▸ Column (B): 5,800 riyals",
            option_a="Column A is larger", option_b="Column (b) is larger", option_c="The two values ​​are equal", option_d="The relationship cannot be determined",
            correct_option="a",
            explanation_ar="Calculating each column: Column (A) = 12 That the values are specific",
            solution_steps_ar='["Column A = 12 x 500 = 6000","Column B = 5800","6000 > 5800 ∴ Column A is larger"]',
    tags="comparison,installment", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        #── Q158: Numbers problem — 3-digit number ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.7,
            text_ar="A number consisting of 3 digits, the hundreds digit = 3, the tens digit twice the ones digit, and the sum of its digits = 12. What is the number?",
            option_a="363", option_b="342", option_c="384", option_d="362",
            correct_option="a",
            explanation_ar="Solution:\n Hundreds number = 3\n n = 2a (tens times the ones)\n 3 + 2a + a = 12 → 3a = 9 → a = 3\n n = 6\n Number = 363\n\nWhy are the other options wrong:\n • (a) Column (a) is larger: the result of a common arithmetic error in one of the steps\n • (c) the two values are equal: the result of applying the law or relationship incorrectly\n • (d) it cannot Determining the relationship: the result of forgetting a step in the solution or performing an incorrect operation",
            solution_steps_ar='["Hundreds = 3, tens = 2 x ones","3 + 2a + a = 12 → a = 3, a = 6","number = 363"]',
    tags="digit-problem", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.43),

        #── Q159: Tax — Comparison ──
        Question(skill_id="quant_arithmetic", question_type="comparison", difficulty=0.5,
            text_ar="Compare:\n\n▸ Column (A): The price of an item is 500 riyals + 15% tax\n▸ Column (B): The price of an item is 600 riyals without tax",
            option_a="Column A is larger", option_b="Column (b) is larger", option_c="The two values ​​are equal", option_d="The relationship cannot be determined",
            correct_option="b",
            explanation_ar="Calculating each column: Column (A) = 500 The values are specific",
            solution_steps_ar='["Column A = 500 x 1.15 = 575","Column B = 600","600 > 575 ∴ Column B is greater"]',
    tags="comparison,tax,percentage", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.43),

        #── Q160: Two trains — different lengths ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.8,
            text_ar="Two trains are moving in opposite directions, their length is 150 m and 250 m. The speed of the first = 36 km/h and the second = 54 km/h. How many seconds does it take for them to pass each other?",
            option_a="12 seconds", option_b="16 seconds", option_c="20 seconds", option_d="24 seconds",
            correct_option="b",
            explanation_ar="Solution:\n Distance = 150 + 250 = 400 meters\n Sum of the two speeds = 36 + 54 = 90 km/h = 25 m/s\n Time = 400 ÷ 25 = 16 seconds\n\nWhy are the other options wrong:\n • (a) 12: The result of forgetting to convert units between hours and minutes or km/h and m/s\n • (c) 16: The result of using distance instead of time in the equation\n • (D) 18: The result of an error in calculating the average speed",
            solution_steps_ar='["Distance = 150 + 250 = 400 m","Speed ​​= 90 km/h = 25 m/s","Time = 400 ÷ 25 = 16 seconds"]',
    tags="speed,train,unit-conversion", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        #── Q161: Consecutive even numbers ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.4,
            text_ar="Four consecutive even numbers whose sum = 68. What is the smallest?",
            option_a="12", option_b="14", option_c="16", option_d="18",
            correct_option="b",
            explanation_ar="Solution: Numbers: x, (d) The relationship cannot be determined: as a result of forgetting a step in the solution or performing an incorrect operation",
            solution_steps_ar='["4x + 12 = 68 → x = 14","Numbers: 14, 16, 18, 20"]',
    tags="number-properties", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        #── Q162: Comparison — simple benefit ──
        Question(skill_id="quant_arithmetic", question_type="comparison", difficulty=0.6,
            text_ar="Compare:\n\n▸ Column (A): Simple interest on 20,000 riyals at 5% for 4 years\n▸ Column (B): 4,500 riyals",
            option_a="Column A is larger", option_b="Column (b) is larger", option_c="The two values ​​are equal", option_d="The relationship cannot be determined",
            correct_option="b",
            explanation_ar="Calculating each column: Column A = 20,000 x 0.05 It is not possible to determine even though the values are specified",
            solution_steps_ar='["Column A = 20,000 x 0.05 x 4 = 4000","Column (B) = 4500","4500 > 4000 ∴ Column (B) is larger"]',
    tags="comparison,compound-interest", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.43),

        #── Q163: Drainage pipe — how much is left ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.6,
            text_ar="A full basin has a capacity of 480 litres. A drain pipe empties 40 liters per minute. How many minutes to empty ¾ of the basin?",
            option_a="6 minutes", option_b="9 minutes", option_c="10 minutes", option_d="12 minutes",
            correct_option="b",
            explanation_ar="Solution: ¾ basin = ¾ x 480 = 360 litres. Time = 360 ÷ 40 = 9 minutes. Why are the other options wrong?",
            solution_steps_ar='["¾ basin = 360 litres","Time = 360 ÷ 40 = 9 minutes"]',
    tags="work-rate,pipes,fraction", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        #── Q164: 10:10 o’clock angle ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.8,
            text_ar="What is the (minimum) angle between the clock hands at 10:10?",
            option_a="95°", option_b="115°", option_c="١٢٠°", option_d="135°",
            correct_option="b",
            explanation_ar="Solution: The minute hand at 10 minutes = 10 0.075 kg: As a result of a common arithmetic error in one of the steps\n • (c) 7.5 kg: As a result of applying the law or relationship incorrectly\n • (d) 75 kg: As a result of forgetting a step in the solution or performing an incorrect operation",
            solution_steps_ar='["The minute hand = 60°","The hour hand = 305°","The difference = 245°, the smallest = 360 − 245 = 115°"]',
    tags="clock-angle", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        #── Q165: Convert grams to kilograms ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.2,
            text_ar="Weight of a box = 750 grams.\nHow much is it worth in kilograms?",
            option_a="0.075 kg", option_b="0.75 kg", option_c="7.5 kg", option_d="75 kg",
            correct_option="b",
            explanation_ar="Solution:\n 1 kg = 1000 grams\n 750 grams = 750 ÷ 1000 = 0.75 kg\n\nWhy are the other options wrong:\n • (a) 1200 riyals: the result of using the conversion factor in the opposite direction\n • (c) 1320 riyals: the result of forgetting the number of zeros in the conversion\n • (d) 1400 riyals: the result of mixing up the units of measurement",
            solution_steps_ar='["1 kg = 1000 grams","750 ÷ 1000 = 0.75 kg"]',
    tags="unit-conversion", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        #── Q166: Compound interest for 3 years ──
        Question(skill_id="quant_arithmetic", question_type="arithmetic", difficulty=0.8,
            text_ar="The amount of 8000 riyals with a compound interest of 5% annually.\nHow much interest is earned after 3 years?\n(8000 x 1.05³ = 9261)",
            option_a="1200 riyals", option_b="1261 riyals", option_c="1320 riyals", option_d="1400 riyals",
            correct_option="b",
            explanation_ar="Solution: Amount after 3 years = 8000 The vehicle is calculated on the accumulated amount",
            solution_steps_ar='["Amount = 8000 x 1.05³ = 9261","Interest = 9261 − 8000 = 1261 riyals"]',
    tags="compound-interest", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        #── Q167: Comparison — Speed ​​of two trains ──
        Question(skill_id="quant_arithmetic", question_type="comparison", difficulty=0.7,
            text_ar="Compare:\n\n▸ Column (A): The meeting time of two trains (speeds of 60 and 90 km/h), the distance between them is 300 km\n▸ Column (B): two hours",
            option_a="Column A is larger", option_b="Column (b) is larger", option_c="The two values ​​are equal", option_d="The relationship cannot be determined",
            correct_option="c",
            explanation_ar="Calculating each column:\n Column (A): The sum of the two speeds = 60 + 90 = 150 km/h\n Time = 300 ÷ 150 = 2 hours\n Column (B) = 2 hours\n\n∴ The two values are equal\n\nWhy are the other options wrong:\n • (A) Column (A) is greater: An error in calculating the value of one of the two columns\n • (B) Column (B) is greater: An error in comparing the two values\n • (D) The relationship cannot be determined: the belief that it cannot be determined even though the values are defined",
            solution_steps_ar='["The sum of the two speeds = 150 km/h","Time = 300 ÷ 150 = 2 hours","2 = 2 ∴ are equal"]',
    tags="comparison,speed,train", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

    ]
