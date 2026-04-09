from models import Question

def get_questions():
        return [
                # ══════════════════════════════════════════════════════════════
                # ██ Existing Questions (14 question) ██
                # ══════════════════════════════════════════════════════════════

                # ── Q1: Rectangle 8×5 Area (diff=0.3) ──
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.3,
                                    text_ar="Rectangle: Length = 8 cm , Width = 5 cm\nWhat is its area?",
                                    option_a="13 cm²",             option_b="26 cm²",             option_c="40 cm²",             option_d="80 cm²",
                                    correct_option="c",
                                    explanation_ar="Formula:\n        Area = Length × Width\n\nSubstitution:\n        Area = 8 × 5 = 40 cm²\n\nWhy other options are wrong:\n            • (b) 26 cm²: Result of using formula Perimeter instead of Area or vice versa\n            • (c) 7 cm: Result of forgetting multiplying sum dimensions by 2 when calculating Perimeter\n            • (d) 80 cm²: Result of adding dimensions instead of multiplying",
                                    solution_steps_ar='["Formula: Area = Length × Width","Substitution: Area = 8 × 5 = 40 cm²"]',
        tags="rectangle", stage="diagnostic",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # ── Q2: Triangle Right 3,4 Hypotenuse (diff=0.4) ──
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.4,
                                    text_ar="Right triangle:\nFirst Side = 3 cm , Second Side = 4 cm\nWhat is length of Hypotenuse?",
                                    option_a="5 cm",             option_b="6 cm",             option_c="7 cm",             option_d="8 cm",
                                    correct_option="a",
                                    explanation_ar="Formula (Pythagorean Theorem):\n Hypotenuse² = Side₁² + Side₂²\n\nSubstitution:\n Hypotenuse² = 3² + 4² = 9 + 16 = 25\n Hypotenuse = √25 = 5 cm\n\nWhy other options are wrong:\n            • (a) 22 cm: Result of forgetting division by 2 in formula Area of Triangle\n            • (c) 7 cm: Result of using formula Rectangle without division by 2\n            • (d) 8 cm: Result of adding Base and Height instead of multiplying them",
                                    solution_steps_ar='["Pythagorean Theorem: Hypotenuse² = Side₁² + Side₂²","Hypotenuse² = 9 + 16 = 25","Hypotenuse = √25 = 5 cm"]',
        tags="triangle,angle,pythagorean", stage="diagnostic",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # ── Q3: Circle r=7 Perimeter (diff=0.5) ──
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.5,
                                    text_ar="Circle: Radius (r) = 7 cm\nCalculate Perimeter.\n(π = ²²⁄₇)",
                                    option_a="22 cm",             option_b="44 cm",             option_c="154 cm",             option_d="308 cm",
                                    correct_option="b",
                                    explanation_ar="Formula:\n Perimeter = 2 × π × r\n\nSubstitution:\n Perimeter = 2 × (22 ÷ 7) × 7\n = 2 × 22 = 44 cm\n\nWhy other options are wrong:\n            • (a) 22 cm: Result of using formula Perimeter instead of Area or vice versa\n            • (c) 154 cm: Result of using Diameter instead of Radius in Formula\n            • (d) 308 cm: Result of forgetting squaring Radius when calculating Area",
                                    solution_steps_ar='["Formula: Perimeter = 2 × π × r","Substitution: = 2 × (22 ÷ 7) × 7","= 2 × 22 = 44 cm"]',
        tags="circle,perimeter", stage="diagnostic",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # ── Q4: Square Perimeter=24 Area (diff=0.7) ──
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.7,
                                    text_ar="Square: Perimeter = 24 cm\nWhat is its area?",
                                    option_a="24 cm²",             option_b="36 cm²",             option_c="48 cm²",             option_d="144 cm²",
                                    correct_option="b",
                                    explanation_ar="Step 1: Finding edge Side\n Side = Perimeter ÷ 4 = 24 ÷ 4 = 6 cm\n\nStep 2: Calculate Area\n        Area = Side² = 6² = 36 cm²\n\nWhy other options are wrong:\n            • (a) 24 cm²: Result of confusing formula Perimeter and Area\n            • (b) 27 cm: Result of multiplying Side in wrong number\n            • (d) 144 cm²: Result of Calculate Area using formula Perimeter or vice versa",
                                    solution_steps_ar='["Side = Perimeter ÷ 4 = 24 ÷ 4 = 6 cm","Area = Side × Side = 6 × 6 = 36 cm²"]',
        tags="square,perimeter", stage="diagnostic",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # ── Q5: Square side=9 Perimeter (diff=0.2) ──
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.2,
                                    text_ar="Square side edge = 9 cm.\nWhat is its perimeter?",
                                    option_a="18 cm",             option_b="27 cm",             option_c="36 cm",             option_d="81 cm",
                                    correct_option="c",
                                    explanation_ar="Formula:\n Perimeter of Square = 4 × Side\n\nSubstitution:\n Perimeter = 4 × 9 = 36 cm\n\nWhy other options are wrong:\n            • (a) 18 cm: Result of confusing formula Perimeter and Area\n            • (c) 60 cm²: Result of multiplying Side in wrong number\n            • (d) 81 cm: Result of Calculate Area using formula Perimeter or vice versa",
                                    solution_steps_ar='["Formula: Perimeter of Square = 4 × Side","Perimeter = 4 × 9 = 36 cm"]',
        tags="square,perimeter", stage="diagnostic",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # ── Q6: Triangle Base=10 =6 Area (diff=0.3) ──
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.3,
                                    text_ar="Triangle: Base = 10 cm , Height = 6 cm.\nWhat is its area?",
                                    option_a="16 cm²",             option_b="30 cm²",             option_c="60 cm²",             option_d="45 cm²",
                                    correct_option="b",
                                    explanation_ar="Formula:\n        Area of Triangle = ½ × Base × Height\n\nSubstitution:\n        Area = ½ × 10 × 6 = 30 cm²\n\nWhy other options are wrong:\n            • (a) 16 cm²: Result of forgetting division by 2 in formula Area of Triangle\n            • (c) 60 cm²: Result of using formula Rectangle without division by 2\n            • (d) 45 cm²: Result of adding Base and Height instead of multiplying them",
                                    solution_steps_ar='["Formula: Area of Triangle = ½ × Base × Height","Area = ½ × 10 × 6 = 30 cm²"]',
        tags="triangle", stage="foundation",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # ── Q7: Rectangle 12×4 Perimeter (diff=0.3) ──
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.3,
                                    text_ar="Rectangle: Length = 12 cm , Width = 4 cm.\nWhat is its perimeter?",
                                    option_a="16 cm",             option_b="32 cm",             option_c="48 cm",             option_d="64 cm",
                                    correct_option="b",
                                    explanation_ar="Formula:\n Perimeter of Rectangle = 2 × (Length + Width)\n\nSubstitution:\n Perimeter = 2 × (12 + 4) = 2 × 16 = 32 cm\n\nWhy other options are wrong:\n            • (a) 16 cm: Result of using formula Perimeter instead of Area or vice versa\n            • (b) 88 cm²: Result of forgetting multiplying sum dimensions by 2 when calculating Perimeter\n            • (d) 64 cm: Result of adding dimensions instead of multiplying",
                                    solution_steps_ar='["Formula: Perimeter of Rectangle = 2 × (Length + Width)","Perimeter = 2 × (12 + 4) = 2 × 16 = 32 cm"]',
        tags="rectangle,perimeter", stage="foundation",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

                # ── Q8: Circle r=14 Area (diff=0.4) ──
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.4,
                                    text_ar="Circle: Radius (r) = 14 cm.\nCalculate Area.\n(π = ²²⁄₇)",
                                    option_a="44 cm²",             option_b="88 cm²",             option_c="616 cm²",             option_d="308 cm²",
                                    correct_option="c",
                                    explanation_ar="Formula:\n        Area = π × r²\n\nSubstitution:\n        Area = (22 ÷ 7) × 14²\n = (22 ÷ 7) × 196\n = 22 × 28 = 616 cm²\n\nWhy other options are wrong:\n            • (a) 44 cm²: Result of using formula Perimeter instead of Area or vice versa\n            • (b) 88 cm²: Result of using Diameter instead of Radius in Formula\n            • (c) 47 cm³: Result of forgetting squaring Radius when calculating Area",
                                    solution_steps_ar='["Formula: Area = π × r²","Area = (22 ÷ 7) × 14 × 14","= (22 ÷ 7) × 196 = 616 cm²"]',
        tags="circle,area", stage="foundation",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # ── Q9: Rectangular prism 5×4×3 Volume (diff=0.5) ──
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.5,
                                    text_ar="Rectangular prism: Length = 5 cm , Width = 4 cm , Height = 3 cm.\nWhat is its volume?",
                                    option_a="12 cm³",             option_b="20 cm³",             option_c="47 cm³",             option_d="60 cm³",
                                    correct_option="d",
                                    explanation_ar="Formula:\n Volume = Length × Width × Height\n\nSubstitution:\n Volume = 5 × 4 × 3 = 60 cm³\n\nWhy other options are wrong:\n            • (a) 12 cm³: Result of Calculate Area instead of Volume\n            • (c) 47 cm³: Result of forgetting one dimension\n            • (d) 16 cm²: Result of using 2D shape formula",
                                    solution_steps_ar='["Formula: Volume = Length × Width × Height","Volume = 5 × 4 × 3 = 60 cm³"]',
        tags="3d-shape,volume", stage="foundation",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # ── Q10: Cube =4 Total surface area (diff=0.5) ──
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.5,
                                    text_ar="Cube: length = 4 cm.\nWhat is its area?",
                                    option_a="64 cm²",             option_b="96 cm²",             option_c="128 cm²",             option_d="16 cm²",
                                    correct_option="b",
                                    explanation_ar="Formula:\n Total surface area of Cube = 6 × Edge²\n\nSubstitution:\n        Area = 6 × 4² = 6 × 16 = 96 cm²\n\nWhy other options are wrong:\n            • (a) 64 cm²: Result of Calculate Area of faces instead of 6 Lateral faces\n            • (b) 10 cm: Result of confusing Volume and Total surface area\n            • (d) 16 cm²: Result of squaring Edge instead of cubing it or vice versa",
                                    solution_steps_ar='["Formula: Total surface area = 6 × Edge²","Area = 6 × 16 = 96 cm²"]',
        tags="cube", stage="foundation",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # ── Q11: Triangle Right Hypotenuse=13 side=5 (diff=0.6) ──
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.6,
                                    text_ar="Right triangle: Hypotenuse = 13 cm ,  Side = 5 cm.\nWhat is length of Other side?",
                                    option_a="8 cm",             option_b="10 cm",             option_c="12 cm",             option_d="14 cm",
                                    correct_option="c",
                                    explanation_ar="Formula (Pythagorean Theorem):\n Hypotenuse² = Side₁² + Side₂²\n\nSubstitution:\n 13² = 5² + Side₂²\n 169 = 25 + Side₂²\n Side₂² = 144\n Side₂ = √144 = 12 cm\n\nWhy other options are wrong:\n            • (b) 10 cm: Result of forgetting division by 2 in formula Area of Triangle\n            • (c) 685 cm²: Result of using formula Rectangle without division by 2\n            • (d) 14 cm: Result of adding Base and Height instead of multiplying them",
                                    solution_steps_ar='["Pythagorean Theorem: Hypotenuse² = Side₁² + Side₂²","13² = 5² + Side₂² → 169 = 25 + Side₂²","Side₂² = 144 → Side₂ = 12 cm"]',
        tags="triangle,angle,pythagorean", stage="foundation",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # ── Q12:  Square Quarter circle (diff=0.7) ──
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.7,
                                    text_ar="Shape: Square side edge = 10 cm of it Quarter circle (r) = 10 cm.\nWhat is remaining area?\n(π = 314)",
                                    option_a="215 cm²",             option_b="785 cm²",             option_c="685 cm²",             option_d="100 cm²",
                                    correct_option="a",
                                    explanation_ar="Formula:\n Remaining area = Area of Square − Area of Circle\n\nCalculation:\n        Area of Diagonal = 10² = 100 cm²\n        Area of Circle = ¼ × π × r² = ¼ × 314 × 100 = 785 cm²\n = 100 − 785 = 215 cm²\n\nWhy other options are wrong:\n            • (b) 785 cm²: Result of confusing formula Perimeter and Area\n            • (c) 685 cm²: Result of multiplying Side in wrong number\n            • (d) 100 cm²: Result of Calculate Area using formula Perimeter or vice versa",
                                    solution_steps_ar='["Area of Diagonal = 10 × 10 = 100 cm²","Area of Circle = ¼ × 314 × 10² = 785 cm²"," = 100 − 785 = 215 cm²"]',
        tags="square,circle,area,composite", stage="foundation",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # ── Q13: Equilateral triangle Perimeter=36 Area (diff=0.8) ──
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.8,
                                    text_ar="Equilateral triangle: Perimeter = 36 cm.\nWhat is its area?\n(: Area Equilateral triangle = (√3 ÷ 4) × Side²)",
                                    option_a="36√3 cm²",             option_b="27√3 cm²",             option_c="12√3 cm²",             option_d="9√3 cm²",
                                    correct_option="a",
                                    explanation_ar="Step 1: Finding edge Side\n Side = Perimeter ÷ 3 = 36 ÷ 3 = 12 cm\n\nStep 2: Calculate Area\n        Area = (√3 ÷ 4) × 12²\n = (√3 ÷ 4) × 144\n = 36√3 cm²\n\nWhy other options are wrong:\n            • (a) 231 cm²: Result of forgetting division by 2 in formula Area of Triangle\n            • (c) 12√3 cm²: Result of using formula Rectangle without division by 2\n            • (d) 9√3 cm²: Result of adding Base and Height instead of multiplying them",
                                    solution_steps_ar='["Side = Perimeter ÷ 3 = 36 ÷ 3 = 12 cm","Area = (√3 ÷ 4) × Side² = (√3 ÷ 4) × 144","= 36√3 cm²"]',
        tags="triangle,area,perimeter", stage="foundation",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # ── Q14: Circular sector r=21 Angle=120° (diff=0.8) ──
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.8,
                                    text_ar="Circular sector: Radius (r) = 21 cm , Sector angle = 120°.\nWhat is Area?\n(π = ²²⁄₇)",
                                    option_a="231 cm²",             option_b="462 cm²",             option_c="693 cm²",             option_d="1386 cm²",
                                    correct_option="b",
                                    explanation_ar="Formula:\n        Area = (Angle ÷ 360) × π × r²\n\nSubstitution:\n = (120 ÷ 360) × (22 ÷ 7) × 21²\n = ⅓ × (22 ÷ 7) × 441\n = ⅓ × 22 × 63\n = ⅓ × 1386 = 462 cm²\n\nWhy other options are wrong:\n            • (a) 231 cm²: Result of using formula Perimeter instead of Area or vice versa\n            • (c) 693 cm²: Result of using Diameter instead of Radius in Formula\n            • (d) 1386 cm²: Result of forgetting squaring Radius when calculating Area",
                                    solution_steps_ar='["Formula: Area = (Angle ÷ 360) × π × r²","= (120 ÷ 360) × (22 ÷ 7) × 21²","= ⅓ × (22 ÷ 7) × 441 = ⅓ × 1386 = 462 cm²"]',
        tags="circle,angle,area,sector", stage="foundation",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

                # ══════════════════════════════════════════════════════════════
                # ██ New Questions (97 question) ██
                # ══════════════════════════════════════════════════════════════
                # Required distribution (Total 111):
                # 0.2 → 11 (existing 1 → need 10)
                # 0.3 → 17 (existing 4 → need 13)
                # 0.4 → 22 (existing 2 → need 20)
                # 0.5 → 22 (existing 3 → need 19)
                # 0.6 → 22 (existing 1 → need 21)
                # 0.7 → 11 (existing 2 → need 9)
                # 0.8 → 6           (existing 2 → need 4)

                # ══════════════════════════════════════════════════════════════
                # ██ Difficulty 02 — 10 New Questions██
                # ══════════════════════════════════════════════════════════════

                # Q15
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.2,
                                    text_ar="Rectangle: Length = 6 cm , Width = 3 cm.\nWhat is its area?",
                                    option_a="9 cm²",             option_b="12 cm²",             option_c="18 cm²",             option_d="36 cm²",
                                    correct_option="c",
                                    explanation_ar="Formula:\n        Area = Length × Width\n\nSubstitution:\n        Area = 6 × 3 = 18 cm²\n\nWhy other options are wrong:\n            • (a) 9 cm²: Result of using formula Perimeter instead of Area or vice versa\n            • (b) 12 cm²: Result of forgetting multiplying sum dimensions by 2 when calculating Perimeter\n            • (d) 36 cm²: Result of adding dimensions instead of multiplying",
                                    solution_steps_ar='["Formula: Area = Length × Width","Area = 6 × 3 = 18 cm²"]',
        tags="rectangle", stage="foundation",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

                # Q16
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.2,
                                    text_ar="Square side edge = 5 cm.\nWhat is its area?",
                                    option_a="10 cm²",             option_b="20 cm²",             option_c="25 cm²",             option_d="30 cm²",
                                    correct_option="c",
                                    explanation_ar="Formula:\n        Area of Diagonal = Side × Side\n\nSubstitution:\n        Area = 5 × 5 = 25 cm²\n\nWhy other options are wrong:\n            • (a) 10 cm²: Result of confusing formula Perimeter and Area\n            • (b) 20 cm²: Result of multiplying Side in wrong number\n            • (d) 30 cm²: Result of Calculate Area using formula Perimeter or vice versa",
                                    solution_steps_ar='["Formula: Area of Diagonal = Side²","Area = 5 × 5 = 25 cm²"]',
        tags="square", stage="foundation",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

                # Q17
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.2,
                                    text_ar="Rectangle: Length = 10 cm , Width = 4 cm.\nWhat is its perimeter?",
                                    option_a="14 cm",             option_b="20 cm",             option_c="28 cm",             option_d="40 cm",
                                    correct_option="c",
                                    explanation_ar="Formula:\n Perimeter of Rectangle = 2 × (Length + Width)\n\nSubstitution:\n Perimeter = 2 × (10 + 4) = 2 × 14 = 28 cm\n\nWhy other options are wrong:\n            • (a) 14 cm: Result of using formula Perimeter instead of Area or vice versa\n            • (b) 20 cm: Result of forgetting multiplying sum dimensions by 2 when calculating Perimeter\n            • (d) 40 cm: Result of adding dimensions instead of multiplying",
                                    solution_steps_ar='["Formula: Perimeter of Rectangle = 2 × (Length + Width)","Perimeter = 2 × (10 + 4) = 2 × 14 = 28 cm"]',
        tags="rectangle,perimeter", stage="foundation",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

                # Q18
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.2,
                                    text_ar="Square side edge = 12 cm.\nWhat is its perimeter?",
                                    option_a="24 cm",             option_b="36 cm",             option_c="48 cm",             option_d="144 cm",
                                    correct_option="c",
                                    explanation_ar="Formula:\n Perimeter of Square = 4 × Side\n\nSubstitution:\n Perimeter = 4 × 12 = 48 cm\n\nWhy other options are wrong:\n            • (a) 24 cm: Result of confusing formula Perimeter and Area\n            • (c) 693 cm²: Result of multiplying Side in wrong number\n            • (d) 144 cm: Result of Calculate Area using formula Perimeter or vice versa",
                                    solution_steps_ar='["Formula: Perimeter of Square = 4 × Side","Perimeter = 4 × 12 = 48 cm"]',
        tags="square,perimeter", stage="foundation",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

                # Q19
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.2,
                                    text_ar="Triangle: Base = 8 cm , Height = 4 cm.\nWhat is its area?",
                                    option_a="12 cm²",             option_b="16 cm²",             option_c="24 cm²",             option_d="32 cm²",
                                    correct_option="b",
                                    explanation_ar="Formula:\n        Area of Triangle = ½ × Base × Height\n\nSubstitution:\n        Area = ½ × 8 × 4 = 16 cm²\n\nWhy other options are wrong:\n            • (a) 12 cm²: Result of forgetting division by 2 in formula Area of Triangle\n            • (b) 18 cm³: Result of using formula Rectangle without division by 2\n            • (d) 32 cm²: Result of adding Base and Height instead of multiplying them",
                                    solution_steps_ar='["Formula: Area of Triangle = ½ × Base × Height","Area = ½ × 8 × 4 = 16 cm²"]',
        tags="triangle", stage="foundation",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

                # Q20
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.2,
                                    text_ar="Cube: length = 3 cm.\nWhat is its volume?",
                                    option_a="9 cm³",             option_b="18 cm³",             option_c="27 cm³",             option_d="36 cm³",
                                    correct_option="c",
                                    explanation_ar="Formula:\n Volume of the Cube = Edge³\n\nSubstitution:\n Volume = 3³ = 3 × 3 × 3 = 27 cm³\n\nWhy other options are wrong:\n            • (a) 9 cm³: Result of Calculate Area of faces instead of 6 Lateral faces\n            • (c) 693 cm²: Result of confusing Volume and Total surface area\n            • (d) 36 cm³: Result of squaring Edge instead of cubing it or vice versa",
                                    solution_steps_ar='["Formula: Volume of the Cube = Edge³","Volume = 3 × 3 × 3 = 27 cm³"]',
        tags="cube,volume", stage="foundation",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

                # Q21
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.2,
                                    text_ar="What is sum of angles of Triangle?",
                                    option_a="90°",             option_b="180°",             option_c="270°",             option_d="360°",
                                    correct_option="b",
                                    explanation_ar="Rule:\n sum of angles of Triangle = 180°\n\nWhy other options are wrong:\n            • (a) 90°: Result of forgetting division by 2 in formula Area of Triangle\n            • (b) 20 cm²: Result of using formula Rectangle without division by 2\n            • (d) 360°: Result of adding Base and Height instead of multiplying them",
                                    solution_steps_ar='["Basic rule: sum of angles of Triangle = 180°"]',
        tags="triangle,angle", stage="foundation",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

                # Q22
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.2,
                                    text_ar="Rectangle: Length = 7 cm , Width = 3 cm.\nWhat is its area?",
                                    option_a="10 cm²",             option_b="20 cm²",             option_c="21 cm²",             option_d="42 cm²",
                                    correct_option="c",
                                    explanation_ar="Formula:\n        Area = Length × Width\n\nSubstitution:\n        Area = 7 × 3 = 21 cm²\n\nWhy other options are wrong:\n            • (a) 10 cm²: Result of using formula Perimeter instead of Area or vice versa\n            • (b) 20 cm²: Result of forgetting multiplying sum dimensions by 2 when calculating Perimeter\n            • (d) 42 cm²: Result of adding dimensions instead of multiplying",
                                    solution_steps_ar='["Formula: Area = Length × Width","Area = 7 × 3 = 21 cm²"]',
        tags="rectangle", stage="foundation",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

                # Q23
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.2,
                                    text_ar="Square side edge = 7 cm.\nWhat is its area?",
                                    option_a="28 cm²",             option_b="35 cm²",             option_c="49 cm²",             option_d="14 cm²",
                                    correct_option="c",
                                    explanation_ar="Formula:\n        Area of Diagonal = Side²\n\nSubstitution:\n        Area = 7² = 49 cm²\n\nWhy other options are wrong:\n            • (a) 28 cm²: Result of confusing formula Perimeter and Area\n            • (c) 693 cm²: Result of multiplying Side in wrong number\n            • (d) 14 cm²: Result of Calculate Area using formula Perimeter or vice versa",
                                    solution_steps_ar='["Formula: Area of Diagonal = Side²","Area = 7 × 7 = 49 cm²"]',
        tags="square", stage="foundation",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

                # Q24
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.2,
                                    text_ar="If Two angles in Triangle Measure 60° and 80°, What is measure of  angle?",
                                    option_a="20°",             option_b="40°",             option_c="60°",             option_d="80°",
                                    correct_option="b",
                                    explanation_ar="Formula:\n sum of angles of Triangle = 180°\n\nSubstitution:\n         angle = 180 − 60 − 80 = 40°\n\nWhy other options are wrong:\n            • (a) 20°: Result of forgetting division by 2 in formula Area of Triangle\n            • (c) 60°: Result of using formula Rectangle without division by 2\n            • (d) 80°: Result of adding Base and Height instead of multiplying them",
                                    solution_steps_ar='["sum of angles of Triangle = 180°"," angle = 180 − 60 − 80 = 40°"]',
        tags="triangle,angle", stage="foundation",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

                # ══════════════════════════════════════════════════════════════
                # ██ Difficulty 03 — 13 new question██
                # ══════════════════════════════════════════════════════════════

                # Q25
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.3,
                                    text_ar="Rectangle: Length = 15 cm , Width = 6 cm.\nWhat is its area?",
                                    option_a="42 cm²",             option_b="60 cm²",             option_c="90 cm²",             option_d="120 cm²",
                                    correct_option="c",
                                    explanation_ar="Formula:\n        Area = Length × Width\n\nSubstitution:\n        Area = 15 × 6 = 90 cm²\n\nWhy other options are wrong:\n            • (a) 42 cm²: Result of using formula Perimeter instead of Area or vice versa\n            • (b) 60 cm²: Result of forgetting multiplying sum dimensions by 2 when calculating Perimeter\n            • (d) 120 cm²: Result of adding dimensions instead of multiplying",
                                    solution_steps_ar='["Formula: Area = Length × Width","Area = 15 × 6 = 90 cm²"]',
        tags="rectangle", stage="foundation",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

                # Q26
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.3,
                                    text_ar="Square side edge = 11 cm.\nWhat is its perimeter?",
                                    option_a="22 cm",             option_b="33 cm",             option_c="44 cm",             option_d="121 cm",
                                    correct_option="c",
                                    explanation_ar="Formula:\n Perimeter of Square = 4 × Side\n\nSubstitution:\n Perimeter = 4 × 11 = 44 cm\n\nWhy other options are wrong:\n            • (a) 22 cm: Result of confusing formula Perimeter and Area\n            • (b) 33 cm: Result of multiplying Side in wrong number\n            • (d) 121 cm: Result of Calculate Area using formula Perimeter or vice versa",
                                    solution_steps_ar='["Formula: Perimeter of Square = 4 × Side","Perimeter = 4 × 11 = 44 cm"]',
        tags="square,perimeter", stage="foundation",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

                # Q27
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.3,
                                    text_ar="Triangle: Base = 14 cm , Height = 8 cm.\nWhat is its area?",
                                    option_a="22 cm²",             option_b="44 cm²",             option_c="56 cm²",             option_d="112 cm²",
                                    correct_option="c",
                                    explanation_ar="Formula:\n        Area of Triangle = ½ × Base × Height\n\nSubstitution:\n        Area = ½ × 14 × 8 = 56 cm²\n\nWhy other options are wrong:\n            • (a) 22 cm²: Result of forgetting division by 2 in formula Area of Triangle\n            • (b) 44 cm²: Result of using formula Rectangle without division by 2\n            • (d) 112 cm²: Result of adding Base and Height instead of multiplying them",
                                    solution_steps_ar='["Formula: Area of Triangle = ½ × Base × Height","Area = ½ × 14 × 8 = 56 cm²"]',
        tags="triangle", stage="foundation",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # Q28
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.3,
                                    text_ar="Cube: length = 5 cm.\nWhat is its volume?",
                                    option_a="25 cm³",             option_b="75 cm³",             option_c="125 cm³",             option_d="150 cm³",
                                    correct_option="c",
                                    explanation_ar="Formula:\n Volume of the Cube = Edge³\n\nSubstitution:\n Volume = 5³ = 5 × 5 × 5 = 125 cm³\n\nWhy other options are wrong:\n            • (a) 25 cm³: Result of Calculate Area of faces instead of 6 Lateral faces\n            • (c) 693 cm²: Result of confusing Volume and Total surface area\n            • (d) 150 cm³: Result of squaring Edge instead of cubing it or vice versa",
                                    solution_steps_ar='["Formula: Volume of the Cube = Edge³","Volume = 5 × 5 × 5 = 125 cm³"]',
        tags="cube,volume", stage="foundation",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # Q29
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.3,
                                    text_ar="Rectangle: Length = 9 cm , Width = 7 cm.\nWhat is its perimeter?",
                                    option_a="16 cm",             option_b="32 cm",             option_c="63 cm",             option_d="128 cm",
                                    correct_option="b",
                                    explanation_ar="Formula:\n Perimeter of Rectangle = 2 × (Length + Width)\n\nSubstitution:\n Perimeter = 2 × (9 + 7) = 2 × 16 = 32 cm\n\nWhy other options are wrong:\n            • (a) 16 cm: Result of using formula Perimeter instead of Area or vice versa\n            • (c) 63 cm: Result of forgetting multiplying sum dimensions by 2 when calculating Perimeter\n            • (d) 128 cm: Result of adding dimensions instead of multiplying",
                                    solution_steps_ar='["Formula: Perimeter of Rectangle = 2 × (Length + Width)","Perimeter = 2 × (9 + 7) = 2 × 16 = 32 cm"]',
        tags="rectangle,perimeter", stage="foundation",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # Q30
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.3,
                                    text_ar="If Two angles Complementary and Measure of one 35°, Measure of other?",
                                    option_a="45°",             option_b="55°",             option_c="145°",             option_d="155°",
                                    correct_option="b",
                                    explanation_ar="Formula:\n Two angles sum = 90°\n\nSubstitution:\n Angle = 90 − 35 = 55°\n\nWhy other options are wrong:\n            • (a) 45°: Result of confusing sum (90°) sum (180°)\n            • (c) 145°: Result of using wrong angle sum for shape\n            • (d) 155°: Result of forgetting to subtract given angles",
                                    solution_steps_ar='["Two angles : sum = 90°","Angle = 90 − 35 = 55°"]',
        tags="angle", stage="foundation",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # Q31
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.3,
                                    text_ar="If Two angles Supplementary and Measure of one 110°, Measure of other?",
                                    option_a="50°",             option_b="70°",             option_c="110°",             option_d="180°",
                                    correct_option="b",
                                    explanation_ar="Formula:\n Two angles sum = 180°\n\nSubstitution:\n Angle = 180 − 110 = 70°\n\nWhy other options are wrong:\n            • (a) 50°: Result of confusing sum (90°) sum (180°)\n            • (b) 22 cm²: Result of using wrong angle sum for shape\n            • (d) 180°: Result of forgetting to subtract given angles",
                                    solution_steps_ar='["Two angles : sum = 180°","Angle = 180 − 110 = 70°"]',
        tags="angle", stage="building",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # Q32
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.3,
                                    text_ar="Circle: Radius (r) = 7 cm.\nCalculate Area.\n(π = ²²⁄₇)",
                                    option_a="44 cm²",             option_b="22 cm²",             option_c="154 cm²",             option_d="308 cm²",
                                    correct_option="c",
                                    explanation_ar="Formula:\n        Area = π × r²\n\nSubstitution:\n        Area = (22 ÷ 7) × 7²\n = (22 ÷ 7) × 49\n = 22 × 7 = 154 cm²\n\nWhy other options are wrong:\n            • (a) 44 cm²: Result of using formula Perimeter instead of Area or vice versa\n            • (b) 22 cm²: Result of using Diameter instead of Radius in Formula\n            • (d) 308 cm²: Result of forgetting squaring Radius when calculating Area",
                                    solution_steps_ar='["Formula: Area = π × r²","Area = (22 ÷ 7) × 49","= 22 × 7 = 154 cm²"]',
        tags="circle,area", stage="building",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # Q33
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.3,
                                    text_ar="Triangle: Base = 20 cm , Height = 10 cm.\nWhat is its area?",
                                    option_a="30 cm²",             option_b="60 cm²",             option_c="100 cm²",             option_d="200 cm²",
                                    correct_option="c",
                                    explanation_ar="Formula:\n        Area of Triangle = ½ × Base × Height\n\nSubstitution:\n        Area = ½ × 20 × 10 = 100 cm²\n\nWhy other options are wrong:\n            • (a) 30 cm²: Result of forgetting division by 2 in formula Area of Triangle\n            • (b) 60 cm²: Result of using formula Rectangle without division by 2\n            • (d) 200 cm²: Result of adding Base and Height instead of multiplying them",
                                    solution_steps_ar='["Formula: Area of Triangle = ½ × Base × Height","Area = ½ × 20 × 10 = 100 cm²"]',
        tags="triangle", stage="building",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # Q34
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.3,
                                    text_ar="Rectangle: Length = 11 cm , Width = 5 cm.\nWhat is its area?",
                                    option_a="16 cm²",             option_b="32 cm²",             option_c="55 cm²",             option_d="110 cm²",
                                    correct_option="c",
                                    explanation_ar="Formula:\n        Area = Length × Width\n\nSubstitution:\n        Area = 11 × 5 = 55 cm²\n\nWhy other options are wrong:\n            • (a) 16 cm²: Result of using formula Perimeter instead of Area or vice versa\n            • (b) 32 cm²: Result of forgetting multiplying sum dimensions by 2 when calculating Perimeter\n            • (d) 110 cm²: Result of adding dimensions instead of multiplying",
                                    solution_steps_ar='["Formula: Area = Length × Width","Area = 11 × 5 = 55 cm²"]',
        tags="rectangle", stage="building",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # Q35
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.3,
                                    text_ar="Rectangular prism: Length = 6 cm , Width = 3 cm , Height = 2 cm.\nWhat is its volume?",
                                    option_a="11 cm³",             option_b="18 cm³",             option_c="36 cm³",             option_d="72 cm³",
                                    correct_option="c",
                                    explanation_ar="Formula:\n Volume = Length × Width × Height\n\nSubstitution:\n Volume = 6 × 3 × 2 = 36 cm³\n\nWhy other options are wrong:\n            • (a) 11 cm³: Result of Calculate Area instead of Volume\n            • (b) 18 cm³: Result of forgetting one dimension\n            • (d) 72 cm³: Result of using 2D shape formula",
                                    solution_steps_ar='["Formula: Volume = Length × Width × Height","Volume = 6 × 3 × 2 = 36 cm³"]',
        tags="3d-shape,volume", stage="building",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # Q36
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.3,
                                    text_ar="Square side edge = 8 cm.\nWhat is its area?",
                                    option_a="32 cm²",             option_b="48 cm²",             option_c="64 cm²",             option_d="128 cm²",
                                    correct_option="c",
                                    explanation_ar="Formula:\n        Area of Diagonal = Side²\n\nSubstitution:\n        Area = 8² = 64 cm²\n\nWhy other options are wrong:\n            • (a) 32 cm²: Result of confusing formula Perimeter and Area\n            • (c) 693 cm²: Result of multiplying Side in wrong number\n            • (d) 128 cm²: Result of Calculate Area using formula Perimeter or vice versa",
                                    solution_steps_ar='["Formula: Area of Diagonal = Side²","Area = 8 × 8 = 64 cm²"]',
        tags="square", stage="building",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # Q37
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.3,
                                    text_ar="If Two angles in Triangle Measure 45° and 90°, What is measure of  angle?",
                                    option_a="35°",             option_b="45°",             option_c="55°",             option_d="90°",
                                    correct_option="b",
                                    explanation_ar="Formula:\n sum of angles of Triangle = 180°\n\nSubstitution:\n         angle = 180 − 45 − 90 = 45°\n\nWhy other options are wrong:\n            • (a) 35°: Result of forgetting division by 2 in formula Area of Triangle\n            • (c) 55°: Result of using formula Rectangle without division by 2\n            • (d) 90°: Result of adding Base and Height instead of multiplying them",
                                    solution_steps_ar='["sum of angles of Triangle = 180°"," angle = 180 − 45 − 90 = 45°"]',
        tags="triangle,angle", stage="building",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # ══════════════════════════════════════════════════════════════
                # ██ Difficulty 04 — 20 new question██
                # ══════════════════════════════════════════════════════════════

                # Q38
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.4,
                                    text_ar="Right triangle:\nFirst Side = 6 cm , Second Side = 8 cm.\nWhat is length of Hypotenuse?",
                                    option_a="10 cm",             option_b="12 cm",             option_c="14 cm",             option_d="16 cm",
                                    correct_option="a",
                                    explanation_ar="Pythagorean Theorem:\n Hypotenuse² = 6² + 8² = 36 + 64 = 100\n Hypotenuse = √100 = 10 cm\n\nWhy other options are wrong:\n            • (a) 231 cm²: Result of forgetting division by 2 in formula Area of Triangle\n            • (b) 12 cm: Result of using formula Rectangle without division by 2\n            • (d) 16 cm: Result of adding Base and Height instead of multiplying them",
                                    solution_steps_ar='["Pythagorean Theorem: Hypotenuse² = 6² + 8²","Hypotenuse² = 36 + 64 = 100","Hypotenuse = √100 = 10 cm"]',
        tags="triangle,angle,pythagorean", stage="building",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # Q39
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.4,
                                    text_ar="Circle: Diameter = 28 cm.\nCalculate Perimeter.\n(π = ²²⁄₇)",
                                    option_a="44 cm",             option_b="66 cm",             option_c="88 cm",             option_d="176 cm",
                                    correct_option="c",
                                    explanation_ar="Formula:\n Perimeter = π × Diameter\n\nSubstitution:\n Perimeter = (22 ÷ 7) × 28 = 22 × 4 = 88 cm\n\nWhy other options are wrong:\n            • (a) 44 cm: Result of using formula Perimeter instead of Area or vice versa\n            • (c) 693 cm²: Result of using Diameter instead of Radius in Formula\n            • (d) 176 cm: Result of forgetting squaring Radius when calculating Area",
                                    solution_steps_ar='["Formula: Perimeter = π × Diameter","Perimeter = (22 ÷ 7) × 28","= 22 × 4 = 88 cm"]',
        tags="circle,perimeter", stage="building",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # Q40
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.4,
                                    text_ar="Square: Perimeter = 32 cm.\nWhat is length of side?",
                                    option_a="4 cm",             option_b="8 cm",             option_c="12 cm",             option_d="16 cm",
                                    correct_option="b",
                                    explanation_ar="Formula:\n Side = Perimeter ÷ 4\n\nSubstitution:\n Side = 32 ÷ 4 = 8 cm\n\nWhy other options are wrong:\n            • (a) 4 cm: Result of confusing formula Perimeter and Area\n            • (b) 72 cm³: Result of multiplying Side in wrong number\n            • (c) 12 cm: Result of Calculate Area using formula Perimeter or vice versa",
                                    solution_steps_ar='["Formula: Side = Perimeter ÷ 4","Side = 32 ÷ 4 = 8 cm"]',
        tags="square,perimeter", stage="building",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # Q41
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.4,
                                    text_ar="Cube: length = 6 cm.\nWhat is its volume?",
                                    option_a="36 cm³",             option_b="72 cm³",             option_c="144 cm³",             option_d="216 cm³",
                                    correct_option="d",
                                    explanation_ar="Formula:\n Volume of the Cube = Edge³\n\nSubstitution:\n Volume = 6³ = 6 × 6 × 6 = 216 cm³\n\nWhy other options are wrong:\n            • (a) 36 cm³: Result of Calculate Area of faces instead of 6 Lateral faces\n            • (c) 144 cm³: Result of confusing Volume and Total surface area\n            • (d) 1386 cm²: Result of squaring Edge instead of cubing it or vice versa",
                                    solution_steps_ar='["Formula: Volume of the Cube = Edge³","Volume = 6 × 6 × 6 = 216 cm³"]',
        tags="cube,volume", stage="building",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # Q42
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.4,
                                    text_ar="Isosceles triangle: edge Leg = 10 cm , Base = 12 cm.\nWhat is its perimeter?",
                                    option_a="22 cm",             option_b="32 cm",             option_c="42 cm",             option_d="120 cm",
                                    correct_option="b",
                                    explanation_ar="Formula:\n Perimeter Triangle = sum of sides \n\nSubstitution:\n Perimeter = 10 + 10 + 12 = 32 cm\n\nWhy other options are wrong:\n            • (a) 22 cm: Result of forgetting division by 2 in formula Area of Triangle\n            • (b) 40 cm³: Result of using formula Rectangle without division by 2\n            • (c) 42 cm: Result of adding Base and Height instead of multiplying them",
                                    solution_steps_ar='["Isosceles triangle: interior = 10 cm","Perimeter = 10 + 10 + 12 = 32 cm"]',
        tags="triangle,perimeter", stage="building",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # Q43
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.4,
                                    text_ar="Rectangular prism: Length = 8 cm , Width = 5 cm , Height = 4 cm.\nWhat is its volume?",
                                    option_a="17 cm³",             option_b="40 cm³",             option_c="120 cm³",             option_d="160 cm³",
                                    correct_option="d",
                                    explanation_ar="Formula:\n Volume = Length × Width × Height\n\nSubstitution:\n Volume = 8 × 5 × 4 = 160 cm³\n\nWhy other options are wrong:\n            • (a) 17 cm³: Result of Calculate Area instead of Volume\n            • (c) 120 cm³: Result of forgetting one dimension\n            • (d) 1386 cm: Result of using 2D shape formula",
                                    solution_steps_ar='["Formula: Volume = Length × Width × Height","Volume = 8 × 5 × 4 = 160 cm³"]',
        tags="3d-shape,volume", stage="building",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # Q44
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.4,
                                    text_ar="Circle: Radius (r) = 21 cm.\nCalculate Perimeter.\n(π = ²²⁄₇)",
                                    option_a="66 cm",             option_b="132 cm",             option_c="154 cm",             option_d="1386 cm",
                                    correct_option="b",
                                    explanation_ar="Formula:\n Perimeter = 2 × π × r\n\nSubstitution:\n Perimeter = 2 × (22 ÷ 7) × 21\n = 2 × 22 × 3 = 132 cm\n\nWhy other options are wrong:\n            • (a) 66 cm: Result of using formula Perimeter instead of Area or vice versa\n            • (c) 154 cm: Result of using Diameter instead of Radius in Formula\n            • (d) 1386 cm: Result of forgetting squaring Radius when calculating Area",
                                    solution_steps_ar='["Formula: Perimeter = 2 × π × r","Perimeter = 2 × (22 ÷ 7) × 21","= 2 × 66 = 132 cm"]',
        tags="circle,perimeter", stage="building",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # Q45
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.4,
                                    text_ar="Rectangle: 72 cm² , Length = 12 cm.\nWhat is Width?",
                                    option_a="4 cm",             option_b="6 cm",             option_c="8 cm",             option_d="9 cm",
                                    correct_option="b",
                                    explanation_ar="Formula:\n Width = Area ÷ Length\n\nSubstitution:\n Width = 72 ÷ 12 = 6 cm\n\nWhy other options are wrong:\n            • (b) 14 cm: Result of using formula Perimeter instead of Area or vice versa\n            • (c) 8 cm: Result of forgetting multiplying sum dimensions by 2 when calculating Perimeter\n            • (d) 9 cm: Result of adding dimensions instead of multiplying",
                                    solution_steps_ar='["Formula: Width = Area ÷ Length","Width = 72 ÷ 12 = 6 cm"]',
        tags="rectangle", stage="building",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # Q46
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.4,
                                    text_ar="Right triangle:\nFirst Side = 5 cm , Second Side = 12 cm.\nWhat is length of Hypotenuse?",
                                    option_a="13 cm",             option_b="14 cm",             option_c="15 cm",             option_d="17 cm",
                                    correct_option="a",
                                    explanation_ar="Pythagorean Theorem:\n Hypotenuse² = 5² + 12² = 25 + 144 = 169\n Hypotenuse = √169 = 13 cm\n\nWhy other options are wrong:\n            • (a) 231 cm²: Result of forgetting division by 2 in formula Area of Triangle\n            • (c) 15 cm: Result of using formula Rectangle without division by 2\n            • (d) 17 cm: Result of adding Base and Height instead of multiplying them",
                                    solution_steps_ar='["Pythagorean Theorem: Hypotenuse² = 5² + 12²","Hypotenuse² = 25 + 144 = 169","Hypotenuse = √169 = 13 cm"]',
        tags="triangle,angle,pythagorean", stage="building",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # Q47
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.4,
                                    text_ar="Square side edge = 10 cm.\nWhat is its diagonal length?",
                                    option_a="10 cm",             option_b="10√2 cm",             option_c="20 cm",             option_d="10√3 cm",
                                    correct_option="b",
                                    explanation_ar="Formula:\n Diagonal = Side × √2\n\nSubstitution:\n Diameter = 10 × √2 = 10√2 cm\n\nWhy other options are wrong:\n            • (a) 10 cm: Result of confusing formula Perimeter and Area\n            • (b) 12 cm²: Result of multiplying Side in wrong number\n            • (d) 10√3 cm: Result of Calculate Area using formula Perimeter or vice versa",
                                    solution_steps_ar='["Formula: Square = Side × √2","Diameter = 10 × √2 = 10√2 cm"]',
        tags="square", stage="building",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # Q48
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.4,
                                    text_ar="Cube: length = 2 cm.\nWhat is its area?",
                                    option_a="8 cm²",             option_b="12 cm²",             option_c="24 cm²",             option_d="48 cm²",
                                    correct_option="c",
                                    explanation_ar="Formula:\n Total surface area = 6 × Edge²\n\nSubstitution:\n        Area = 6 × 2² = 6 × 4 = 24 cm²\n\nWhy other options are wrong:\n            • (a) 8 cm²: Result of Calculate Area of faces instead of 6 Lateral faces\n            • (b) 12 cm²: Result of confusing Volume and Total surface area\n            • (d) 48 cm²: Result of squaring Edge instead of cubing it or vice versa",
                                    solution_steps_ar='["Formula: Total surface area = 6 × Edge²","Area = 6 × 4 = 24 cm²"]',
        tags="cube", stage="building",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # Q49
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.4,
                                    text_ar="Triangle: 48 cm² , Base = 16 cm.\nWhat is its height?",
                                    option_a="3 cm",             option_b="4 cm",             option_c="6 cm",             option_d="8 cm",
                                    correct_option="c",
                                    explanation_ar="Formula:\n        Area = ½ × Base × Height\n Height = (2 × Area) ÷ Base\n\nSubstitution:\n Height = (2 × 48) ÷ 16 = 96 ÷ 16 = 6 cm\n\nWhy other options are wrong:\n            • (a) 3 cm: Result of forgetting division by 2 in formula Area of Triangle\n            • (b) 4 cm: Result of using formula Rectangle without division by 2\n            • (d) 8 cm: Result of adding Base and Height instead of multiplying them",
                                    solution_steps_ar='["Formula: Height = (2 × Area) ÷ Base","Height = (2 × 48) ÷ 16","= 96 ÷ 16 = 6 cm"]',
        tags="triangle", stage="building",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # Q50
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.4,
                                    text_ar="If Two angles Supplementary and Measure of one 65°, Measure of other?",
                                    option_a="25°",             option_b="35°",             option_c="115°",             option_d="125°",
                                    correct_option="c",
                                    explanation_ar="Formula:\n Two angles sum = 180°\n\nSubstitution:\n Angle = 180 − 65 = 115°\n\nWhy other options are wrong:\n            • (a) 25°: Result of confusing sum (90°) sum (180°)\n            • (b) 35°: Result of using wrong angle sum for shape\n            • (d) 125°: Result of forgetting to subtract given angles",
                                    solution_steps_ar='["Two angles : sum = 180°","Angle = 180 − 65 = 115°"]',
        tags="angle", stage="building",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # Q51
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.4,
                                    text_ar="Circle: Radius (r) = 35 cm.\nCalculate Area.\n(π = ²²⁄₇)",
                                    option_a="11 cm²",             option_b="22 cm²",             option_c="385 cm²",             option_d="77 cm²",
                                    correct_option="c",
                                    explanation_ar="Formula:\n        Area = π × r²\n\nSubstitution:\n        Area = (22 ÷ 7) × 35²\n = (22 ÷ 7) × 1225\n = 385 cm²\n\nWhy other options are wrong:\n            • (a) 11 cm²: Result of using formula Perimeter instead of Area or vice versa\n            • (c) 693 cm²: Result of using Diameter instead of Radius in Formula\n            • (d) 77 cm²: Result of forgetting squaring Radius when calculating Area",
                                    solution_steps_ar='["Formula: Area = π × r²","Area = (22 ÷ 7) × (35)²","= (22 ÷ 7) × 1225 = 385 cm²"]',
        tags="circle,area", stage="building",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # Q52
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.4,
                                    text_ar="Rectangle: Perimeter = 30 cm , Length = 10 cm.\nWhat is Width?",
                                    option_a="3 cm",             option_b="5 cm",             option_c="10 cm",             option_d="15 cm",
                                    correct_option="b",
                                    explanation_ar="Formula:\n Perimeter of Rectangle = 2 × (Length + Width)\n Length + Width = Perimeter ÷ 2\n\nSubstitution:\n Length + Width = 30 ÷ 2 = 15\n Width = 15 − 10 = 5 cm\n\nWhy other options are wrong:\n            • (a) 3 cm: Result of using formula Perimeter instead of Area or vice versa\n            • (c) 10 cm: Result of forgetting multiplying sum dimensions by 2 when calculating Perimeter\n            • (d) 15 cm: Result of adding dimensions instead of multiplying",
                                    solution_steps_ar='["Length + Width = Perimeter ÷ 2 = 30 ÷ 2 = 15","Width = 15 − 10 = 5 cm"]',
        tags="rectangle,perimeter", stage="building",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # Q53
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.4,
                                    text_ar="Equilateral triangle: side edge = 9 cm.\nWhat is its perimeter?",
                                    option_a="18 cm",             option_b="27 cm",             option_c="36 cm",             option_d="81 cm",
                                    correct_option="b",
                                    explanation_ar="Formula:\n Perimeter Equilateral triangle = 3 × Side\n\nSubstitution:\n Perimeter = 3 × 9 = 27 cm\n\nWhy other options are wrong:\n            • (a) 18 cm: Result of forgetting division by 2 in formula Area of Triangle\n            • (c) 36 cm: Result of using formula Rectangle without division by 2\n            • (d) 81 cm: Result of adding Base and Height instead of multiplying them",
                                    solution_steps_ar='["Formula: Perimeter = 3 × Side","Perimeter = 3 × 9 = 27 cm"]',
        tags="triangle,perimeter", stage="building",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # Q54
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.4,
                                    text_ar="Right triangle:\nFirst Side = 8 cm , Second Side = 15 cm.\nWhat is length of Hypotenuse?",
                                    option_a="15 cm",             option_b="17 cm",             option_c="19 cm",             option_d="23 cm",
                                    correct_option="b",
                                    explanation_ar="Pythagorean Theorem:\n Hypotenuse² = 8² + 15² = 64 + 225 = 289\n Hypotenuse = √289 = 17 cm\n\nWhy other options are wrong:\n            • (a) 15 cm: Result of forgetting division by 2 in formula Area of Triangle\n            • (c) 19 cm: Result of using formula Rectangle without division by 2\n            • (d) 23 cm: Result of adding Base and Height instead of multiplying them",
                                    solution_steps_ar='["Pythagorean Theorem: Hypotenuse² = 8² + 15²","Hypotenuse² = 64 + 225 = 289","Hypotenuse = √289 = 17 cm"]',
        tags="triangle,angle,pythagorean", stage="building",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # Q55
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.4,
                                    text_ar="Cylinder: Base radius (r) = 7 cm , Height = 10 cm.\nCalculate volume.\n(π = ²²⁄₇)",
                                    option_a="770 cm³",             option_b="1540 cm³",             option_c="220 cm³",             option_d="440 cm³",
                                    correct_option="b",
                                    explanation_ar="Formula:\n Volume of Cylinder = π × r² × Height\n\nSubstitution:\n Volume = (22 ÷ 7) × 7² × 10\n = (22 ÷ 7) × 49 × 10\n = 22 × 7 × 10 = 1540 cm³\n\nWhy other options are wrong:\n            • (a) 770 cm³: Result of Calculate AreaBase without multiplying in Height\n            • (c) 220 cm³: Result of forgetting multiplying Area in Height\n            • (d) 440 cm³: Result of using Diameter instead of Radius",
                                    solution_steps_ar='["Formula: Volume of Cylinder = π × r² × Height","Volume = (22 ÷ 7) × 49 × 10","= 22 × 70 = 1540 cm³"]',
        tags="cylinder,volume", stage="building",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # Q56
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.4,
                                    text_ar="Square side edge = 6 cm.\nWhat is its diagonal length?",
                                    option_a="6 cm",             option_b="6√2 cm",             option_c="12 cm",             option_d="6√3 cm",
                                    correct_option="b",
                                    explanation_ar="Formula:\n Diagonal = Side × √2\n\nSubstitution:\n Diameter = 6 × √2 = 6√2 cm\n\nWhy other options are wrong:\n            • (a) 6 cm: Result of confusing formula Perimeter and Area\n            • (c) 12 cm: Result of multiplying Side in wrong number\n            • (d) 6√3 cm: Result of Calculate Area using formula Perimeter or vice versa",
                                    solution_steps_ar='["Formula: Square = Side × √2","Diameter = 6 × √2 = 6√2 cm"]',
        tags="square", stage="building",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # Q57
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.4,
                                    text_ar="Rectangle: Length = 20 cm , Width = 15 cm.\nWhat is its diagonal length?",
                                    option_a="20 cm",             option_b="25 cm",             option_c="30 cm",             option_d="35 cm",
                                    correct_option="b",
                                    explanation_ar="Pythagorean Theorem (Diameter  and Hypotenuse Triangle):\n Diameter² = Length² + Width²\n = 20² + 15² = 400 + 225 = 625\n Diameter = √625 = 25 cm\n\nWhy other options are wrong:\n            • (a) 20 cm: Result of using formula Perimeter instead of Area or vice versa\n            • (c) 30 cm: Result of forgetting multiplying sum dimensions by 2 when calculating Perimeter\n            • (d) 35 cm: Result of adding dimensions instead of multiplying",
                                    solution_steps_ar='["Diameter² = Length² + Width²","Diameter² = 400 + 225 = 625","Diameter = √625 = 25 cm"]',
        tags="rectangle", stage="building",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # ══════════════════════════════════════════════════════════════
                # ██ Difficulty 05 — 19 new question██
                # ══════════════════════════════════════════════════════════════

                # Q58
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.5,
                                    text_ar="Square: 121 cm².\nWhat is length of side?",
                                    option_a="9 cm",             option_b="10 cm",             option_c="11 cm",             option_d="12 cm",
                                    correct_option="c",
                                    explanation_ar="Formula:\n Side = √Area\n\nSubstitution:\n Side = √121 = 11 cm\n\nWhy other options are wrong:\n            • (a) 9 cm: Result of confusing formula Perimeter and Area\n            • (c) 693 cm²: Result of multiplying Side in wrong number\n            • (d) 12 cm: Result of Calculate Area using formula Perimeter or vice versa",
                                    solution_steps_ar='["Formula: Side = √Area","Side = √121 = 11 cm"]',
        tags="square", stage="building",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # Q59
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.5,
                                    text_ar="Circle: Diameter = 14 cm.\nCalculate Area.\n(π = ²²⁄₇)",
                                    option_a="44 cm²",             option_b="154 cm²",             option_c="308 cm²",             option_d="616 cm²",
                                    correct_option="b",
                                    explanation_ar="Formula:\n r = Diameter ÷ 2 = 14 ÷ 2 = 7 cm\n        Area = π × r²\n\nSubstitution:\n        Area = (22 ÷ 7) × 7² = 22 × 7 = 154 cm²\n\nWhy other options are wrong:\n            • (a) 44 cm²: Result of using formula Perimeter instead of Area or vice versa\n            • (b) 100 cm²: Result of using Diameter instead of Radius in Formula\n            • (c) 308 cm²: Result of forgetting squaring Radius when calculating Area",
                                    solution_steps_ar='["r = Diameter ÷ 2 = 14 ÷ 2 = 7 cm","Area = π × r² = (22 ÷ 7) × 49","= 22 × 7 = 154 cm²"]',
        tags="circle,area", stage="building",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # Q60
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.5,
                                    text_ar="Cube: length = 5 cm.\nWhat is its area?",
                                    option_a="25 cm²",             option_b="100 cm²",             option_c="125 cm²",             option_d="150 cm²",
                                    correct_option="d",
                                    explanation_ar="Formula:\n Total surface area = 6 × Edge²\n\nSubstitution:\n        Area = 6 × 5² = 6 × 25 = 150 cm²\n\nWhy other options are wrong:\n            • (a) 25 cm²: Result of Calculate Area of faces instead of 6 Lateral faces\n            • (b) 100 cm²: Result of confusing Volume and Total surface area\n            • (d) 1386 cm²: Result of squaring Edge instead of cubing it or vice versa",
                                    solution_steps_ar='["Formula: Total surface area = 6 × Edge²","Area = 6 × 25 = 150 cm²"]',
        tags="cube", stage="building",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # Q61
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.5,
                                    text_ar="Cylinder: Base radius (r) = 35 cm , Height = 6 cm.\nCalculate volume.\n(π = ²²⁄₇)",
                                    option_a="1155 cm³",             option_b="154 cm³",             option_c="231 cm³",             option_d="462 cm³",
                                    correct_option="c",
                                    explanation_ar="Formula:\n Volume of Cylinder = π × r² × Height\n\nSubstitution:\n Volume = (22 ÷ 7) × 35² × 6\n = (22 ÷ 7) × 1225 × 6\n = 385 × 6 = 231 cm³\n\nWhy other options are wrong:\n            • (a) 1155 cm³: Result of Calculate AreaBase without multiplying in Height\n            • (c) 693 cm²: Result of forgetting multiplying Area in Height\n            • (d) 462 cm³: Result of using Diameter instead of Radius",
                                    solution_steps_ar='["Formula: Volume of Cylinder = π × r² × Height","Volume = (22 ÷ 7) × (35)² × 6","= 385 × 6 = 231 cm³"]',
        tags="cylinder,volume", stage="building",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # Q62
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.5,
                                    text_ar="Similar Triangles Similar:            First 3 cm and 4 cm and 5 cm.\nIf  length in Second = 15 cm,          in it?",
                                    option_a="6 cm",             option_b="9 cm",             option_c="10 cm",             option_d="12 cm",
                                    correct_option="b",
                                    explanation_ar="Similarity ratio:\n = 15 ÷ 5 = 3\n\n in Second:\n= 3 × 3 = 9 cm\n\nWhy other options are wrong:\n            • (a) 6 cm: Result of forgetting division by 2 in formula Area of Triangle\n            • (b) 200 cm²: Result of using formula Rectangle without division by 2\n            • (d) 12 cm: Result of adding Base and Height instead of multiplying them",
                                    solution_steps_ar='["Similarity ratio = 15 ÷ 5 = 3","= 3 × 3 = 9 cm"]',
        tags="triangle", stage="building",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # Q63
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.5,
                                    text_ar="Rectangular prism: Length = 10 cm , Width = 6 cm , Height = 4 cm.\nWhat is its area?",
                                    option_a="148 cm²",             option_b="200 cm²",             option_c="248 cm²",             option_d="496 cm²",
                                    correct_option="c",
                                    explanation_ar="Formula:\n Total surface area = 2 × (× + × + ×)\n\nSubstitution:\n = 2 × (10×6 + 10×4 + 6×4)\n = 2 × (60 + 40 + 24)\n = 2 × 124 = 248 cm²\n\nWhy other options are wrong:\n            • (a) 148 cm²: Result of Calculate Area instead of Volume\n            • (b) 200 cm²: Result of forgetting one dimension\n            • (d) 496 cm²: Result of using 2D shape formula",
                                    solution_steps_ar='["Formula: Total surface area = 2(× + × + ×)","= 2 × (60 + 40 + 24)","= 2 × 124 = 248 cm²"]',
        tags="3d-shape", stage="building",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # Q64
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.5,
                                    text_ar="Right triangle: Hypotenuse = 10 cm ,  Side = 6 cm.\nWhat is length of Other side?",
                                    option_a="4 cm",             option_b="6 cm",             option_c="8 cm",             option_d="12 cm",
                                    correct_option="c",
                                    explanation_ar="Pythagorean Theorem:\n Hypotenuse² = Side₁² + Side₂²\n 10² = 6² + Side₂²\n 100 = 36 + Side₂²\n Side₂² = 64\n Side₂ = √64 = 8 cm\n\nWhy other options are wrong:\n            • (a) 4 cm: Result of forgetting division by 2 in formula Area of Triangle\n            • (c) 693 cm²: Result of using formula Rectangle without division by 2\n            • (d) 12 cm: Result of adding Base and Height instead of multiplying them",
                                    solution_steps_ar='["Pythagorean Theorem: 10² = 6² + Side₂²","100 = 36 + Side₂²","Side₂² = 64 → Side₂ = 8 cm"]',
        tags="triangle,angle,pythagorean", stage="building",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # Q65
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.5,
                                    text_ar="Square: length = 8√2 cm.\nWhat is its area?",
                                    option_a="32 cm²",             option_b="64 cm²",             option_c="128 cm²",             option_d="256 cm²",
                                    correct_option="b",
                                    explanation_ar="Formula:\n Diagonal = Side × √2\n Side = Diameter ÷ √2 = 8√2 ÷ √2 = 8 cm\n\nArea = 8² = 64 cm²\n\nWhy other options are wrong:\n            • (a) 32 cm²: Result of confusing formula Perimeter and Area\n            • (c) 128 cm²: Result of multiplying Side in wrong number\n            • (d) 256 cm²: Result of Calculate Area using formula Perimeter or vice versa",
                                    solution_steps_ar='["Side = Diameter ÷ √2 = 8√2 ÷ √2 = 8 cm","Area = Side² = 8² = 64 cm²"]',
        tags="square", stage="building",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # Q66
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.5,
                                    text_ar="Semicircle: Radius (r) = 7 cm.\nCalculate total perimeter (arc + Diameter).\n(π = ²²⁄₇)",
                                    option_a="22 cm",             option_b="36 cm",             option_c="44 cm",             option_d="58 cm",
                                    correct_option="b",
                                    explanation_ar="Formula:\n Perimeter of Circle = π × r + 2 × r\n (Perimeter + Diameter)\n\nSubstitution:\n = (22 ÷ 7) × 7 + 2 × 7\n = 22 + 14 = 36 cm\n\nWhy other options are wrong:\n            • (a) 22 cm: Result of using formula Perimeter instead of Area or vice versa\n            • (c) 44 cm: Result of using Diameter instead of Radius in Formula\n            • (d) 58 cm: Result of forgetting squaring Radius when calculating Area",
                                    solution_steps_ar='["length arc = π × r = (22 ÷ 7) × 7 = 22 cm","Diameter = 2 × r = 14 cm","Perimeter = 22 + 14 = 36 cm"]',
        tags="circle,perimeter", stage="peak",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # Q67
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.5,
                                    text_ar="Cube: Volume of = 64 cm³.\nWhat is length of ?",
                                    option_a="2 cm",             option_b="4 cm",             option_c="8 cm",             option_d="16 cm",
                                    correct_option="b",
                                    explanation_ar="Formula:\n Edge = ∛Volume\n\nSubstitution:\n Edge = ∛64 = 4 cm\n (because 4 × 4 × 4 = 64)\n\nWhy other options are wrong:\n            • (a) 2 cm: Result of Calculate Area of faces instead of 6 Lateral faces\n            • (b) 32 cm²: Result of confusing Volume and Total surface area\n            • (d) 16 cm: Result of squaring Edge instead of cubing it or vice versa",
                                    solution_steps_ar='["Formula: Edge = ∛Volume","Edge = ∛64 = 4 cm"]',
        tags="cube,volume", stage="peak",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # Q68
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.5,
                                    text_ar="Similar Triangles Similar: Similarity ratio = 2 : 3.\nIf Area First = 16 cm²,        Area Second?",
                                    option_a="24 cm²",             option_b="32 cm²",             option_c="36 cm²",             option_d="48 cm²",
                                    correct_option="c",
                                    explanation_ar="Formula:\n        Area ratio = Square Similarity ratio\n        Area ratio = (2/3)² = 4/9\n\nSubstitution:\n 16/Area₂ = 4/9\n        Area₂ = 16 × 9 ÷ 4 = 36 cm²\n\nWhy other options are wrong:\n            • (a) 24 cm²: Result of using formula Perimeter instead of Area\n            • (b) 32 cm²: Result of forgetting sides in Calculate Area\n            • (d) 48 cm²: Result of error in Calculate",
                                    solution_steps_ar='["Area ratio = Square Similarity ratio = (2/3)² = 4/9","16 ÷ Area₂ = 4 ÷ 9","Area₂ = 16 × 9 ÷ 4 = 36 cm²"]',
        tags="area,triangle", stage="peak",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # Q69
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.5,
                                    text_ar="Rectangle: Length = Width , Perimeter = 42 cm.\nWhat is its area?",
                                    option_a="49 cm²",             option_b="72 cm²",             option_c="98 cm²",             option_d="144 cm²",
                                    correct_option="c",
                                    explanation_ar="Let Width = \n Length = 2\n Perimeter = 2(2 + ) = 2 × 3 = 6\n 6 = 42 → = 7 cm\n Length = 14 cm\n\nArea = 14 × 7 = 98 cm²\n\nWhy other options are wrong:\n            • (a) 49 cm²: Result of using formula Perimeter instead of Area or vice versa\n            • (b) 72 cm²: Result of forgetting multiplying sum dimensions by 2 when calculating Perimeter\n            • (d) 144 cm²: Result of adding dimensions instead of multiplying",
                                    solution_steps_ar='["Let Width = , Length = 2","Perimeter = 2(2 + ) = 6 = 42"," = 7 cm , Length = 14 cm","Area = 14 × 7 = 98 cm²"]',
        tags="rectangle,perimeter", stage="peak",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # Q70
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.5,
                                    text_ar="Distance between (0 , 0) and (3 , 4) in coordinate plane?",
                                    option_a="3 units",             option_b="4 units",             option_c="5 units",             option_d="7 units",
                                    correct_option="c",
                                    explanation_ar="Distance formula:\n = √[(₂ − ₁)² + (₂ − ₁)²]\n = √[(3 − 0)² + (4 − 0)²]\n = √[9 + 16] = √25 = 5 units\n\nWhy other options are wrong:\n            • (a) 3 units: Result of forgetting to square coordinate differences\n            • (b) 4 units: Result of adding coordinates instead of Calculate differences\n            • (c) 693 cm²: Result of forgetting to take square root",
                                    solution_steps_ar='["Distance formula: √[(₂−₁)² + (₂−₁)²]","= √[(3)² + (4)²] = √[9 + 16]","= √25 = 5 units"]',
        tags="coordinate", stage="peak",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # Q71
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.5,
                                    text_ar="Rectangular prism: Length = 12 cm , Width = 5 cm , Height = 3 cm.\nWhat is its volume?",
                                    option_a="60 cm³",             option_b="90 cm³",             option_c="120 cm³",             option_d="180 cm³",
                                    correct_option="d",
                                    explanation_ar="Formula:\n Volume = Length × Width × Height\n\nSubstitution:\n Volume = 12 × 5 × 3 = 180 cm³\n\nWhy other options are wrong:\n            • (a) 60 cm³: Result of Calculate Area instead of Volume\n            • (c) 120 cm³: Result of forgetting one dimension\n            • (d) 1386 cm²: Result of using 2D shape formula",
                                    solution_steps_ar='["Formula: Volume = Length × Width × Height","Volume = 12 × 5 × 3 = 180 cm³"]',
        tags="3d-shape,volume", stage="peak",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # Q72
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.5,
                                    text_ar="Circle: Perimeter = 88 cm.\nWhat is its radius?\n(π = ²²⁄₇)",
                                    option_a="7 cm",             option_b="14 cm",             option_c="21 cm",             option_d="28 cm",
                                    correct_option="b",
                                    explanation_ar="Formula:\n Perimeter = 2 × π × r\n r = Perimeter ÷ (2 × )\n\nSubstitution:\n r = 88 ÷ (2 × ²²⁄₇)\n = 88 ÷ (⁴⁴⁄₇)\n = 88 × ⁷⁄₄₄ = 14 cm\n\nWhy other options are wrong:\n            • (b) 875 cm²: Result of using formula Perimeter instead of Area or vice versa\n            • (c) 21 cm: Result of using Diameter instead of Radius in Formula\n            • (d) 28 cm: Result of forgetting squaring Radius when calculating Area",
                                    solution_steps_ar='["Formula: r = Perimeter ÷ (2 × )","r = 88 ÷ (2 × ²²⁄₇)","= 88 × 7 ÷ 44 = 14 cm"]',
        tags="circle,perimeter", stage="peak",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # Q73
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.5,
                                    text_ar="Triangle: calculation 7 cm , 24 cm , 25 cm.\nIs it Right triangle?\nIf , What is its area?",
                                    option_a="84 cm²",             option_b="875 cm²",             option_c="175 cm²",             option_d="300 cm²",
                                    correct_option="a",
                                    explanation_ar=" Right Angle:\n 7² + 24² = 49 + 576 = 625 = 25² ✓\n\nArea = ½ × 7 × 24 = 84 cm²\n\nWhy other options are wrong:\n            • (a) 231 cm²: Result of forgetting division by 2 in formula Area of Triangle\n            • (c) 175 cm²: Result of using formula Rectangle without division by 2\n            • (d) 300 cm²: Result of adding Base and Height instead of multiplying them",
                                    solution_steps_ar='[": 7² + 24² = 49 + 576 = 625 = 25² → Right Angle ✓","Area = ½ × Base × Height","= ½ × 7 × 24 = 84 cm²"]',
        tags="triangle,angle,pythagorean", stage="peak",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # Q74
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.5,
                                    text_ar="What are coordinates rπ (2 , 6) and (8 , 10)?",
                                    option_a="(4 , 7)",             option_b="(5 , 8)",             option_c="(6 , 10)",             option_d="(10 , 16)",
                                    correct_option="b",
                                    explanation_ar="formula rπ :\n = (₁ + ₂) ÷ 2 = (2 + 8) ÷ 2 = 5\n = (₁ + ₂) ÷ 2 = (6 + 10) ÷ 2 = 8\n\nrπ = (5 , 8)\n\nWhy other options are wrong:\n            • (a) (4 , 7): Result of forgetting to square coordinate differences\n            • (b) 10 cm: Result of adding coordinates instead of Calculate differences\n            • (d) (10 , 16): Result of forgetting to take square root",
                                    solution_steps_ar='[" = (2 + 8) ÷ 2 = 5"," = (6 + 10) ÷ 2 = 8","rπ = (5 , 8)"]',
        tags="coordinate", stage="peak",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # Q75
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.5,
                                    text_ar="Isosceles triangle: edge Leg = 13 cm , Base = 10 cm.\nWhat is its height?",
                                    option_a="8 cm",             option_b="10 cm",             option_c="12 cm",             option_d="15 cm",
                                    correct_option="c",
                                    explanation_ar="Height from Base: 5 cm and 5 cm.\nApplying Pythagorean theorem:\n Height² = 13² − 5² = 169 − 25 = 144\n Height = √144 = 12 cm\n\nWhy other options are wrong:\n            • (a) 8 cm: Result of forgetting division by 2 in formula Area of Triangle\n            • (b) 10 cm: Result of using formula Rectangle without division by 2\n            • (c) 693 cm²: Result of adding Base and Height instead of multiplying them",
                                    solution_steps_ar='["Height from Base: Base = 5 cm","inPythagorean: Height² = 13² − 5²","= 169 − 25 = 144 → Height = 12 cm"]',
        tags="triangle", stage="peak",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # Q76
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.5,
                                    text_ar="Cube: = 216 cm².\nWhat is its volume?",
                                    option_a="36 cm³",             option_b="64 cm³",             option_c="125 cm³",             option_d="216 cm³",
                                    correct_option="d",
                                    explanation_ar="Formula:\n Total surface area = 6 × Edge²\n 216 = 6 × Edge²\n Edge² = 36\n Edge = 6 cm\n\nVolume = 6³ = 216 cm³\n\nWhy other options are wrong:\n            • (a) 36 cm³: Result of Calculate Area of faces instead of 6 Lateral faces\n            • (b) 64 cm³: Result of confusing Volume and Total surface area\n            • (c) 125 cm³: Result of squaring Edge instead of cubing it or vice versa",
                                    solution_steps_ar='["Total surface area = 6 × Edge² = 216","Edge² = 36 → Edge = 6 cm","Volume = 6³ = 216 cm³"]',
        tags="cube,volume", stage="peak",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # ══════════════════════════════════════════════════════════════
                # ██ Difficulty 06 — 21 new question██
                # ══════════════════════════════════════════════════════════════

                # Q77
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.6,
                                    text_ar="Circle: Area = 616 cm².\nWhat is its radius?\n(π = ²²⁄₇)",
                                    option_a="7 cm",             option_b="14 cm",             option_c="21 cm",             option_d="28 cm",
                                    correct_option="b",
                                    explanation_ar="Formula:\n        Area = π × r²\n 616 = (22 ÷ 7) × r²\n r² = 616 × 7 ÷ 22 = 4312 ÷ 22 = 196\n r = √196 = 14 cm\n\nWhy other options are wrong:\n            • (a) 7 cm: Result of using formula Perimeter instead of Area or vice versa\n            • (b) 12 cm: Result of using Diameter instead of Radius in Formula\n            • (d) 28 cm: Result of forgetting squaring Radius when calculating Area",
                                    solution_steps_ar='["Area = π × r²","r² = 616 × 7 ÷ 22 = 196","r = √196 = 14 cm"]',
        tags="circle,area", stage="peak",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # Q78
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.6,
                                    text_ar="Right triangle: Hypotenuse = 17 cm ,  Side = 8 cm.\nWhat is length of Other side?",
                                    option_a="9 cm",             option_b="12 cm",             option_c="15 cm",             option_d="20 cm",
                                    correct_option="c",
                                    explanation_ar="Pythagorean Theorem:\n Side₂² = Hypotenuse² − Side₁²\n = 17² − 8² = 289 − 64 = 225\n Side₂ = √225 = 15 cm\n\nWhy other options are wrong:\n            • (a) 9 cm: Result of forgetting division by 2 in formula Area of Triangle\n            • (b) 12 cm: Result of using formula Rectangle without division by 2\n            • (d) 20 cm: Result of adding Base and Height instead of multiplying them",
                                    solution_steps_ar='["Side₂² = Hypotenuse² − Side₁²","= 289 − 64 = 225","Side₂ = √225 = 15 cm"]',
        tags="triangle,angle,pythagorean", stage="peak",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # Q79
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.6,
                                    text_ar="Trapezoid: Large base = 14 cm , Small base = 8 cm , Height = 6 cm.\nWhat is its area?",
                                    option_a="44 cm²",             option_b="52 cm²",             option_c="66 cm²",             option_d="132 cm²",
                                    correct_option="c",
                                    explanation_ar="Formula:\n        Area Trapezoid = ½ × (Base₁ + Base₂) × Height\n\nSubstitution:\n = ½ × (14 + 8) × 6\n = ½ × 22 × 6 = 66 cm²\n\nWhy other options are wrong:\n            • (a) 44 cm²: Result of using formula Perimeter instead of Area or vice versa\n            • (c) 693 cm²: Result of forgetting multiplying sum dimensions by 2 when calculating Perimeter\n            • (d) 132 cm²: Result of adding dimensions instead of multiplying",
                                    solution_steps_ar='["Formula: Area = ½ × (Base₁ + Base₂) × Height","= ½ × (14 + 8) × 6","= ½ × 22 × 6 = 66 cm²"]',
        tags="rectangle", stage="peak",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # Q80
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.6,
                                    text_ar="Cylinder: Base radius (r) = 14 cm , Height = 5 cm.\nCalculate volume.\n(π = ²²⁄₇)",
                                    option_a="1540 cm³",             option_b="3080 cm³",             option_c="4620 cm³",             option_d="6160 cm³",
                                    correct_option="b",
                                    explanation_ar="Formula:\n Volume of Cylinder = π × r² × Height\n\nSubstitution:\n = (22 ÷ 7) × 14² × 5\n = (22 ÷ 7) × 196 × 5\n = 616 × 5 = 3080 cm³\n\nWhy other options are wrong:\n            • (a) 1540 cm³: Result of Calculate AreaBase without multiplying in Height\n            • (b) 40 cm²: Result of forgetting multiplying Area in Height\n            • (d) 6160 cm³: Result of using Diameter instead of Radius",
                                    solution_steps_ar='["Formula: Volume of Cylinder = π × r² × Height","= (22 ÷ 7) × 196 × 5","= 616 × 5 = 3080 cm³"]',
        tags="cylinder,volume", stage="peak",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # Q81
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.6,
                                    text_ar="Rectangle: Length Width 4 cm , Perimeter = 28 cm.\nWhat is its area?",
                                    option_a="35 cm²",             option_b="40 cm²",             option_c="45 cm²",             option_d="48 cm²",
                                    correct_option="c",
                                    explanation_ar="Let Width = , Length = + 4\n Perimeter = 2( + + 4) = 2(2 + 4) = 4 + 8\n 4 + 8 = 28 → 4 = 20 → = 5 cm\n Length = 9 cm\n\nArea = 9 × 5 = 45 cm²\n\nWhy other options are wrong:\n            • (a) 35 cm²: Result of using formula Perimeter instead of Area or vice versa\n            • (b) 40 cm²: Result of forgetting multiplying sum dimensions by 2 when calculating Perimeter\n            • (d) 48 cm²: Result of adding dimensions instead of multiplying",
                                    solution_steps_ar='["Let Width = , Length = + 4","Perimeter = 2( + + 4) = 4 + 8 = 28"," = 5 cm , Length = 9 cm","Area = 9 × 5 = 45 cm²"]',
        tags="rectangle,perimeter", stage="peak",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # Q82
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.6,
                                    text_ar="Similar Triangles Similar:            First 4 cm and 6 cm and 8 cm.\nIf in Second = 10 cm,         length in it?",
                                    option_a="15 cm",             option_b="18 cm",             option_c="20 cm",             option_d="24 cm",
                                    correct_option="c",
                                    explanation_ar="Similarity ratio:\n = 10 ÷ 4 = 25\n\n lengthin Second:\n = 8 × 25 = 20 cm\n\nWhy other options are wrong:\n            • (a) 15 cm: Result of forgetting division by 2 in formula Area of Triangle\n            • (b) 18 cm: Result of using formula Rectangle without division by 2\n            • (d) 24 cm: Result of adding Base and Height instead of multiplying them",
                                    solution_steps_ar='["Similarity ratio = 10 ÷ 4 = 25"," length = 8 × 25 = 20 cm"]',
        tags="triangle", stage="peak",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # Q83
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.6,
                                    text_ar="Distance between (1 , 2) and (4 , 6) in coordinate plane?",
                                    option_a="3 units",             option_b="4 units",             option_c="5 units",             option_d="7 units",
                                    correct_option="c",
                                    explanation_ar="Distance formula:\n = √[(4 − 1)² + (6 − 2)²]\n = √[9 + 16] = √25 = 5 units\n\nWhy other options are wrong:\n            • (a) 3 units: Result of forgetting to square coordinate differences\n            • (c) 693 cm²: Result of adding coordinates instead of Calculate differences\n            • (d) 7 units: Result of forgetting to take square root",
                                    solution_steps_ar='[" = √[(4−1)² + (6−2)²]","= √[9 + 16] = √25","= 5 units"]',
        tags="coordinate", stage="peak",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # Q84
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.6,
                                    text_ar="Circular sector: Radius (r) = 14 cm , Sector angle = 90°.\nWhat is Area?\n(π = ²²⁄₇)",
                                    option_a="77 cm²",             option_b="154 cm²",             option_c="308 cm²",             option_d="616 cm²",
                                    correct_option="b",
                                    explanation_ar="Formula:\n        Area = (Angle ÷ 360) × π × r²\n\nSubstitution:\n = (90 ÷ 360) × (22 ÷ 7) × 14²\n = ¼ × (22 ÷ 7) × 196\n = ¼ × 616 = 154 cm²\n\nWhy other options are wrong:\n            • (a) 77 cm²: Result of using formula Perimeter instead of Area or vice versa\n            • (b) 180 cm²: Result of using Diameter instead of Radius in Formula\n            • (d) 616 cm²: Result of forgetting squaring Radius when calculating Area",
                                    solution_steps_ar='["Area = (Angle ÷ 360) × π × r²","= (90 ÷ 360) × (22 ÷ 7) × 196","= ¼ × 616 = 154 cm²"]',
        tags="circle,angle,area,sector", stage="peak",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # Q85
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.6,
                                    text_ar="Rectangular prism: Length = 8 cm , Width = 6 cm , Height = 5 cm.\nWhat is its area?",
                                    option_a="140 cm²",             option_b="180 cm²",             option_c="236 cm²",             option_d="240 cm²",
                                    correct_option="c",
                                    explanation_ar="Formula:\n Total surface area = 2(× + × + ×)\n\nSubstitution:\n = 2(8×6 + 8×5 + 6×5)\n = 2(48 + 40 + 30)\n = 2 × 118 = 236 cm²\n\nWhy other options are wrong:\n            • (a) 140 cm²: Result of Calculate Area instead of Volume\n            • (b) 180 cm²: Result of forgetting one dimension\n            • (d) 240 cm²: Result of using 2D shape formula",
                                    solution_steps_ar='["Total surface area = 2(× + × + ×)","= 2(48 + 40 + 30)","= 2 × 118 = 236 cm²"]',
        tags="3d-shape", stage="peak",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # Q86
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.6,
                                    text_ar="Equilateral triangle: side edge = 8 cm.\nWhat is its area?\n(Area = (√3 ÷ 4) × Side²)",
                                    option_a="8√3 cm²",             option_b="12√3 cm²",             option_c="16√3 cm²",             option_d="32√3 cm²",
                                    correct_option="c",
                                    explanation_ar="Formula:\n        Area = (√3 ÷ 4) × Side²\n\nSubstitution:\n = (√3 ÷ 4) × 8²\n = (√3 ÷ 4) × 64\n = 16√3 cm²\n\nWhy other options are wrong:\n            • (a) 8√3 cm²: Result of forgetting division by 2 in formula Area of Triangle\n            • (c) 693 cm²: Result of using formula Rectangle without division by 2\n            • (d) 32√3 cm²: Result of adding Base and Height instead of multiplying them",
                                    solution_steps_ar='["Area = (√3 ÷ 4) × Side²","= (√3 ÷ 4) × 64","= 16√3 cm²"]',
        tags="triangle,area", stage="mock",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # Q87
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.6,
                                    text_ar="length arc in Circle (r) = 21 cm andCentral angle = 60°.\nWhat is length of arc?\n(π = ²²⁄₇)",
                                    option_a="11 cm",             option_b="22 cm",             option_c="33 cm",             option_d="44 cm",
                                    correct_option="b",
                                    explanation_ar="Formula:\n length arc = (Angle ÷ 360) × 2 × π × r\n\nSubstitution:\n = (60 ÷ 360) × 2 × (22 ÷ 7) × 21\n = ⅙ × 2 × 22 × 3\n = ⅙ × 132 = 22 cm\n\nWhy other options are wrong:\n            • (a) 11 cm: Result of using formula Perimeter instead of Area or vice versa\n            • (c) 33 cm: Result of using Diameter instead of Radius in Formula\n            • (d) 44 cm: Result of forgetting squaring Radius when calculating Area",
                                    solution_steps_ar='["length arc = (Angle ÷ 360) × 2 × π × r","= (60 ÷ 360) × 2 × (22 ÷ 7) × 21","= ⅙ × 132 = 22 cm"]',
        tags="circle,angle", stage="mock",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # Q88
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.6,
                                    text_ar="Square: Perimeter = 40 cm.\nWhat is its diagonal length?",
                                    option_a="10 cm",             option_b="10√2 cm",             option_c="20 cm",             option_d="20√2 cm",
                                    correct_option="b",
                                    explanation_ar="Side = Perimeter ÷ 4 = 40 ÷ 4 = 10 cm\nDiameter = Side × √2 = 10√2 cm\n\nWhy other options are wrong:\n            • (a) 10 cm: Result of confusing formula Perimeter and Area\n            • (c) 20 cm: Result of multiplying Side in wrong number\n            • (d) 20√2 cm: Result of Calculate Area using formula Perimeter or vice versa",
                                    solution_steps_ar='["Side = 40 ÷ 4 = 10 cm","Diameter = Side × √2 = 10√2 cm"]',
        tags="square,perimeter", stage="mock",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # Q89
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.6,
                                    text_ar="Triangle: calculation 9 cm , 12 cm , 15 cm.\nWhat is its area?",
                                    option_a="45 cm²",             option_b="54 cm²",             option_c="90 cm²",             option_d="108 cm²",
                                    correct_option="b",
                                    explanation_ar=": 9² + 12² = 81 + 144 = 225 = 15² ✓ (Triangle Right)\n\nArea = ½ × 9 × 12 = 54 cm²\n\nWhy other options are wrong:\n            • (a) 45 cm²: Result of forgetting division by 2 in formula Area of Triangle\n            • (b) 196 cm²: Result of using formula Rectangle without division by 2\n            • (c) 90 cm²: Result of adding Base and Height instead of multiplying them",
                                    solution_steps_ar='[": 9² + 12² = 225 = 15² → Triangle Right","Area = ½ × 9 × 12 = 54 cm²"]',
        tags="triangle", stage="mock",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # Q90
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.6,
                                    text_ar="Cube: Volume of = 343 cm³.\nWhat is its area?",
                                    option_a="147 cm²",             option_b="196 cm²",             option_c="245 cm²",             option_d="294 cm²",
                                    correct_option="d",
                                    explanation_ar="Edge = ∛343 = 7 cm\n(because 7 × 7 × 7 = 343)\n\nTotal surface area = 6 × 7² = 6 × 49 = 294 cm²\n\nWhy other options are wrong:\n            • (a) 147 cm²: Result of Calculate Area of faces instead of 6 Lateral faces\n            • (c) 245 cm²: Result of confusing Volume and Total surface area\n            • (d) 1386 cm²: Result of squaring Edge instead of cubing it or vice versa",
                                    solution_steps_ar='["Edge = ∛343 = 7 cm","Total surface area = 6 × Edge² = 6 × 49","= 294 cm²"]',
        tags="cube,volume", stage="mock",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # Q91
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.6,
                                    text_ar="Trapezoid: Large base = 20 cm , Small base = 12 cm , Height = 8 cm.\nWhat is its area?",
                                    option_a="64 cm²",             option_b="128 cm²",             option_c="160 cm²",             option_d="256 cm²",
                                    correct_option="b",
                                    explanation_ar="Formula:\n        Area Trapezoid = ½ × (Base₁ + Base₂) × Height\n\nSubstitution:\n = ½ × (20 + 12) × 8\n = ½ × 32 × 8 = 128 cm²\n\nWhy other options are wrong:\n            • (a) 64 cm²: Result of using formula Perimeter instead of Area or vice versa\n            • (b) 4 units: Result of forgetting multiplying sum dimensions by 2 when calculating Perimeter\n            • (d) 256 cm²: Result of adding dimensions instead of multiplying",
                                    solution_steps_ar='["Area = ½ × (Base₁ + Base₂) × Height","= ½ × (20 + 12) × 8","= ½ × 32 × 8 = 128 cm²"]',
        tags="rectangle", stage="mock",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # Q92
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.6,
                                    text_ar="Distance between (−2 , 1) and (1 , 5) in coordinate plane?",
                                    option_a="3 units",             option_b="4 units",             option_c="5 units",             option_d="6 units",
                                    correct_option="c",
                                    explanation_ar="Distance formula:\n = √[(1 − (−2))² + (5 − 1)²]\n = √[3² + 4²] = √[9 + 16]\n = √25 = 5 units\n\nWhy other options are wrong:\n            • (a) 3 units: Result of forgetting to square coordinate differences\n            • (b) 4 units: Result of adding coordinates instead of Calculate differences\n            • (d) 6 units: Result of forgetting to take square root",
                                    solution_steps_ar='[" = √[(1−(−2))² + (5−1)²]","= √[9 + 16] = √25","= 5 units"]',
        tags="coordinate", stage="mock",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # Q93
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.6,
                                    text_ar="Right triangle: Hypotenuse = 25 cm ,  Side = 7 cm.\nWhat is length of Other side?",
                                    option_a="18 cm",             option_b="20 cm",             option_c="24 cm",             option_d="26 cm",
                                    correct_option="c",
                                    explanation_ar="Pythagorean Theorem:\n Side₂² = 25² − 7² = 625 − 49 = 576\n Side₂ = √576 = 24 cm\n\nWhy other options are wrong:\n            • (a) 18 cm: Result of forgetting division by 2 in formula Area of Triangle\n            • (c) 693 cm²: Result of using formula Rectangle without division by 2\n            • (d) 26 cm: Result of adding Base and Height instead of multiplying them",
                                    solution_steps_ar='["Side₂² = 25² − 7²","= 625 − 49 = 576","Side₂ = √576 = 24 cm"]',
        tags="triangle,angle,pythagorean", stage="mock",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # Q94
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.6,
                                    text_ar="Circle: 154 cm².\nCalculate Perimeter.\n(π = ²²⁄₇)",
                                    option_a="22 cm",             option_b="44 cm",             option_c="66 cm",             option_d="88 cm",
                                    correct_option="b",
                                    explanation_ar="First: Finding Radius\n π × r² = 154\n (22 ÷ 7) × r² = 154\n r² = 154 × 7 ÷ 22 = 49\n r = 7 cm\n\nPerimeter = 2 × π × r = 2 × (22 ÷ 7) × 7 = 44 cm\n\nWhy other options are wrong:\n            • (a) 22 cm: Result of using formula Perimeter instead of Area or vice versa\n            • (c) 66 cm: Result of using Diameter instead of Radius in Formula\n            • (d) 88 cm: Result of forgetting squaring Radius when calculating Area",
                                    solution_steps_ar='["r² = 154 × 7 ÷ 22 = 49 → r = 7 cm","Perimeter = 2 × π × r","= 2 × (22 ÷ 7) × 7 = 44 cm"]',
        tags="circle,perimeter", stage="mock",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # Q95
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.6,
                                    text_ar="Similar Triangles Similar: Similarity ratio = 1 : 3.\nIf Perimeter First = 12 cm, Perimeter Second?",
                                    option_a="24 cm",             option_b="36 cm",             option_c="48 cm",             option_d="108 cm",
                                    correct_option="b",
                                    explanation_ar="in Similar Triangles Similarity: Ratio of Perimeters = Similarity ratio\n\nPerimeter Second = 12 × 3 = 36 cm\n\nWhy other options are wrong:\n            • (a) 24 cm: Result of Calculate Area instead of Perimeter\n            • (c) 48 cm: Result of forgetting sum dimensions\n            • (d) 108 cm: Result of adding instead of Sides",
                                    solution_steps_ar='[" Ratio of Perimeters = Similarity ratio = 1 : 3","Perimeter Second = 12 × 3 = 36 cm"]',
        tags="perimeter,triangle", stage="mock",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # Q96
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.6,
                                    text_ar="Cylinder: Base radius (r) = 7 cm , Height = 15 cm.\nCalculate volume.\n(π = ²²⁄₇)",
                                    option_a="1155 cm³",             option_b="2310 cm³",             option_c="4620 cm³",             option_d="9240 cm³",
                                    correct_option="b",
                                    explanation_ar="Formula:\n Volume of Cylinder = π × r² × Height\n\nSubstitution:\n = (22 ÷ 7) × 49 × 15\n = 22 × 7 × 15\n = 154 × 15 = 2310 cm³\n\nWhy other options are wrong:\n            • (b) Right Angle , 90°: Result of Calculate AreaBase without multiplying in Height\n            • (c) 4620 cm³: Result of forgetting multiplying Area in Height\n            • (d)Therefore , 80°: Result of using Diameter instead of Radius",
                                    solution_steps_ar='["Volume of Cylinder = π × r² × Height","= (22 ÷ 7) × 49 × 15","= 154 × 15 = 2310 cm³"]',
        tags="cylinder,volume", stage="mock",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # Q97
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.6,
                                    text_ar="Triangle: Two angles of it Measure 50° and 60°.\nWhat type Triangle Therefore? andWhat is measure of  angle?",
                                    option_a=" Therefore , 70°",             option_b="Right interior , 90°",             option_c=" interior , 70°",             option_d=" Therefore , 80°",
                                    correct_option="a",
                                    explanation_ar=" angle = 180 − 50 − 60 = 70°\nTherefore 90° → Acute triangle\n\nWhy other options are wrong:\n            • (b) Right interior , 90°: Result of forgetting division by 2 in formula Area of Triangle\n            • (c)  interior , 70°: Result of using formula Rectangle without division by 2\n            • (d)Therefore , 80°: Result of adding Base and Height instead of multiplying them",
                                    solution_steps_ar='[" angle = 180 − 50 − 60 = 70°"," Therefore (50° , 60° , 70°) 90°","Therefore, Acute triangle"]',
        tags="triangle,angle", stage="mock",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # ══════════════════════════════════════════════════════════════
                # ██ Difficulty 07 — 9 New Questions██
                # ══════════════════════════════════════════════════════════════

                # Q98
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.7,
                                    text_ar=" : Rectangle length 20 cm and width 14 cm, of it Semicircle = 14 cm.\nWhat is remaining area?\n(π = ²²⁄₇)",
                                    option_a="123 cm²",             option_b="203 cm²",             option_c="147 cm²",             option_d="280 cm²",
                                    correct_option="b",
                                    explanation_ar="Area of Rectangle = 20 × 14 = 280 cm²\nArea of Circle = ½ × π × r²\n r = 14 ÷ 2 = 7 cm\n = ½ × (22 ÷ 7) × 49 = ½ × 154 = 77 cm²\n\nRemaining = 280 − 77 = 203 cm²\n\nWhy other options are wrong:\n            • (a) 123 cm²: Result of using formula Perimeter instead of Area or vice versa\n            • (b) 100 cm²: Result of forgetting multiplying sum dimensions by 2 when calculating Perimeter\n            • (d) 280 cm²: Result of adding dimensions instead of multiplying",
                                    solution_steps_ar='["Area of Rectangle = 20 × 14 = 280 cm²","r = 14 ÷ 2 = 7 cm","Area of Circle = ½ × (22 ÷ 7) × 49 = 77 cm²"," = 280 − 77 = 203 cm²"]',
        tags="rectangle,circle,area,composite", stage="mock",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # Q99
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.7,
                                    text_ar="Similar Triangles Similar: Similarity ratio = 2 : 5.\nIf Area = 20 cm²,        Area ?",
                                    option_a="50 cm²",             option_b="100 cm²",             option_c="125 cm²",             option_d="200 cm²",
                                    correct_option="c",
                                    explanation_ar="Area ratio = Square Similarity ratio\n = (2/5)² = 4/25\n\n20 ÷ Area = 4 ÷ 25\nArea = 20 × 25 ÷ 4 = 125 cm²\n\nWhy other options are wrong:\n            • (a) 50 cm²: Result of using formula Perimeter instead of Area\n            • (b) 100 cm²: Result of forgetting sides in Calculate Area\n            • (d) 200 cm²: Result of error in Calculate",
                                    solution_steps_ar='["Area ratio = (2/5)² = 4/25","20 ÷ Area₂ = 4 ÷ 25","Area₂ = 20 × 25 ÷ 4 = 125 cm²"]',
        tags="area,triangle", stage="mock",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # Q100
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.7,
                                    text_ar="Circular sector: Radius (r) = 14 cm , Sector angle = 270°.\nWhat is Area?\n(π = ²²⁄₇)",
                                    option_a="154 cm²",             option_b="308 cm²",             option_c="462 cm²",             option_d="616 cm²",
                                    correct_option="c",
                                    explanation_ar="Formula:\n        Area = (Angle ÷ 360) × π × r²\n\nSubstitution:\n = (270 ÷ 360) × (22 ÷ 7) × 14²\n = ¾ × (22 ÷ 7) × 196\n = ¾ × 616 = 462 cm²\n\nWhy other options are wrong:\n            • (b) 308 cm²: Result of using formula Perimeter instead of Area or vice versa\n            • (c) 693 cm²: Result of using Diameter instead of Radius in Formula\n            • (d) 616 cm²: Result of forgetting squaring Radius when calculating Area",
                                    solution_steps_ar='["Area = (Angle ÷ 360) × π × r²","= (270 ÷ 360) × (22 ÷ 7) × 196","= ¾ × 616 = 462 cm²"]',
        tags="circle,angle,area,sector", stage="mock",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # Q101
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.7,
                                    text_ar="Equilateral triangle: 6√3 cm.\nWhat is its area?",
                                    option_a="36√3 cm²",             option_b="36 cm²",             option_c="18√3 cm²",             option_d="72 cm²",
                                    correct_option="a",
                                    explanation_ar="in Equilateral triangle:\n Height = (√3 ÷ 2) × Side\n 6√3 = (√3 ÷ 2) × Side\n Side = 12 cm\n\nArea = (√3 ÷ 4) × 12² = (√3 ÷ 4) × 144 = 36√3 cm²\n\nWhy other options are wrong:\n            • (a) 231 cm²: Result of forgetting division by 2 in formula Area of Triangle\n            • (c) 18√3 cm²: Result of using formula Rectangle without division by 2\n            • (d) 72 cm²: Result of adding Base and Height instead of multiplying them",
                                    solution_steps_ar='["Height = (√3 ÷ 2) × Side","6√3 = (√3 ÷ 2) × Side → Side = 12 cm","Area = (√3 ÷ 4) × 144 = 36√3 cm²"]',
        tags="triangle", stage="mock",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # Q102
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.7,
                                    text_ar="Cylinder: Volume of = 1540 cm³ , Base radius (r) = 7 cm.\nWhat is its height?\n(π = ²²⁄₇)",
                                    option_a="5 cm",             option_b="10 cm",             option_c="15 cm",             option_d="20 cm",
                                    correct_option="b",
                                    explanation_ar="Formula:\n Volume = π × r² × Height\n Height = Volume ÷ (π × r²)\n\nSubstitution:\n = 1540 ÷ [(22 ÷ 7) × 49]\n = 1540 ÷ 154 = 10 cm\n\nWhy other options are wrong:\n            • (a) 5 cm: Result of Calculate AreaBase without multiplying in Height\n            • (c) 15 cm: Result of forgetting multiplying Area in Height\n            • (d) 20 cm: Result of using Diameter instead of Radius",
                                    solution_steps_ar='["Height = Volume ÷ (π × r²)","= 1540 ÷ [(22 ÷ 7) × 49]","= 1540 ÷ 154 = 10 cm"]',
        tags="cylinder,volume", stage="mock",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # Q103
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.7,
                                    text_ar="Shape: Square side 14 cm and inscribed in it Circle        .\nWhat is Area Shaded region ()?\n(π = ²²⁄₇)",
                                    option_a="24 cm²",             option_b="42 cm²",             option_c="56 cm²",             option_d="78 cm²",
                                    correct_option="b",
                                    explanation_ar="r Circle = 14 ÷ 2 = 7 cm\nArea of Diagonal = 14² = 196 cm²\nArea of Circle = (22 ÷ 7) × 7² = 154 cm²\n\nShaded region = 196 − 154 = 42 cm²\n\nWhy other options are wrong:\n            • (a) 24 cm²: Result of using formula Perimeter instead of Area or vice versa\n            • (b) 4 cm: Result of using Diameter instead of Radius in Formula\n            • (c) 56 cm²: Result of forgetting squaring Radius when calculating Area",
                                    solution_steps_ar='["r = 14 ÷ 2 = 7 cm","Area of Diagonal = 14² = 196 cm²","Area of Circle = (22 ÷ 7) × 49 = 154 cm²"," = 196 − 154 = 42 cm²"]',
        tags="circle,area,composite", stage="mock",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # Q104
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.7,
                                    text_ar="Rectangular prism: = 214 cm² , Length = 7 cm , Width = 5 cm.\nWhat is its height?",
                                    option_a="3 cm",             option_b="4 cm",             option_c="5 cm",             option_d="6 cm",
                                    correct_option="d",
                                    explanation_ar="Formula:\n Total surface area = 2(× + × + ×)\n 214 = 2(7×5 + 7× + 5×)\n 107 = 35 + 12\n 12 = 72\n = 6 cm\n\nWhy other options are wrong:\n            • (a) 3 cm: Result of Calculate Area instead of Volume\n            • (b) 4 cm: Result of forgetting one dimension\n            • (d) 1386 cm²: Result of using 2D shape formula",
                                    solution_steps_ar='["Total surface area = 2(× + × + ×)","214 = 2(35 + 7 + 5) → 107 = 35 + 12","12 = 72 → = 6 cm"]',
        tags="3d-shape", stage="mock",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # Q105
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.7,
                                    text_ar="Right triangle: Hypotenuse = 20 cm ,  Side = 12 cm.\nWhat is Area of Triangle?",
                                    option_a="48 cm²",             option_b="72 cm²",             option_c="96 cm²",             option_d="120 cm²",
                                    correct_option="c",
                                    explanation_ar="First: Finding Other side (inPythagorean):\n Side₂² = 20² − 12² = 400 − 144 = 256\n Side₂ = √256 = 16 cm\n\nArea = ½ × 12 × 16 = 96 cm²\n\nWhy other options are wrong:\n            • (a) 48 cm²: Result of forgetting division by 2 in formula Area of Triangle\n            • (c) 693 cm²: Result of using formula Rectangle without division by 2\n            • (d) 120 cm²: Result of adding Base and Height instead of multiplying them",
                                    solution_steps_ar='["Side₂² = 20² − 12² = 400 − 144 = 256","Side₂ = √256 = 16 cm","Area = ½ × 12 × 16 = 96 cm²"]',
        tags="triangle,angle,pythagorean,area", stage="mock",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # Q106
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.7,
                                    text_ar="length arc in Circle (r) = 14 cm andCentral angle = 180°.\nWhat is length of arc?\n(π = ²²⁄₇)",
                                    option_a="22 cm",             option_b="44 cm",             option_c="66 cm",             option_d="88 cm",
                                    correct_option="b",
                                    explanation_ar="length arc = (Angle ÷ 360) × 2 × π × r\n = (180 ÷ 360) × 2 × (22 ÷ 7) × 14\n = ½ × 2 × 22 × 2 = 44 cm\n\nWhy other options are wrong:\n            • (a) 22 cm: Result of using formula Perimeter instead of Area or vice versa\n            • (c) 66 cm: Result of using Diameter instead of Radius in Formula\n            • (d) 88 cm: Result of forgetting squaring Radius when calculating Area",
                                    solution_steps_ar='["length arc = (Angle ÷ 360) × 2 × π × r","= ½ × 2 × (22 ÷ 7) × 14","= ½ × 88 = 44 cm"]',
        tags="circle,angle", stage="mock",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # ══════════════════════════════════════════════════════════════
                # ██ Difficulty 08 — 4 New Questions██
                # ══════════════════════════════════════════════════════════════

                # Q107
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.8,
                                    text_ar=" : Rectangle length 21 cm and width 14 cm,         Semicircle = 14 cm.\nCalculate Perimeter.\n(π = ²²⁄₇)",
                                    option_a="64 cm",             option_b="78 cm",             option_c="92 cm",             option_d="100 cm",
                                    correct_option="b",
                                    explanation_ar="Perimeter =\n Length + Length + Width + Circumference of Circle\n (  Therefore arc of Circle)\n\nr = 7 cm\nlength arc = ½ × 2 × π × r = π × r = (22 ÷ 7) × 7 = 22 cm\n\nPerimeter = 21 + 14 + 21 + 22 = 78 cm\n\nWhy other options are wrong:\n            • (a) 64 cm: Result of using formula Perimeter instead of Area or vice versa\n            • (c) 92 cm: Result of forgetting multiplying sum dimensions by 2 when calculating Perimeter\n            • (d) 100 cm: Result of adding dimensions instead of multiplying",
                                    solution_steps_ar='["r = 14 ÷ 2 = 7 cm","length arc = π × r = 22 cm","Perimeter = 21 + 14 + 21 + 22 = 78 cm"]',
        tags="rectangle,circle,perimeter,composite", stage="mock",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # Q108
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.8,
                                    text_ar="Similar Triangles Similar: Similarity ratio = 3 : 5.\nIf Volume of First = 54 cm³, Volume of Third?",
                                    option_a="150 cm³",             option_b="250 cm³",             option_c="375 cm³",             option_d="450 cm³",
                                    correct_option="b",
                                    explanation_ar="Volume ratio = Cube of similarity ratio\n = (3/5)³ = 27/125\n\n54 ÷ Volume₂ = 27 ÷ 125\nVolume₂ = 54 × 125 ÷ 27 = 2 × 125 = 250 cm³\n\nWhy other options are wrong:\n            • (a) 150 cm³: Result of Calculate Area instead of Volume\n            • (c) 375 cm³: Result of forgetting one of three dimensions\n            • (d) 450 cm³: Result of using 2D shape formula",
                                    solution_steps_ar='["Volume ratio = (3/5)³ = 27/125","54 ÷ Volume₂ = 27 ÷ 125","Volume₂ = 54 × 125 ÷ 27 = 250 cm³"]',
        tags="volume,triangle", stage="mock",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # Q109
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.8,
                                    text_ar="Cylinder: = 880 cm² , Base radius (r) = 20 cm.\nWhat is its height?\n(π = ²²⁄₇)",
                                    option_a="5 cm",             option_b="7 cm",             option_c="10 cm",             option_d="14 cm",
                                    correct_option="b",
                                    explanation_ar="Formula:\n Lateral area = 2 × π × r × Height\n 880 = 2 × (22 ÷ 7) × 20 × \n 880 = (44 ÷ 7) × 20 × \n 880 = (880 ÷ 7) × \n = 7 cm\n\nWhy other options are wrong:\n            • (a) 5 cm: Result of Calculate AreaBase without multiplying in Height\n            • (c) 10 cm: Result of forgetting multiplying Area in Height\n            • (d) 14 cm: Result of using Diameter instead of Radius",
                                    solution_steps_ar='["Lateral area = 2 × π × r × ","880 = 2 × (22 ÷ 7) × 20 × ","880 = (880 ÷ 7) × → = 7 cm"]',
        tags="cylinder", stage="mock",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # Q110
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.8,
                                    text_ar="Equilateral triangle: 25√3 cm².\nWhat is length of side?",
                                    option_a="5 cm",             option_b="10 cm",             option_c="15 cm",             option_d="20 cm",
                                    correct_option="b",
                                    explanation_ar="Formula:\n        Area = (√3 ÷ 4) × Side²\n 25√3 = (√3 ÷ 4) × Side²\n Side² = 25 × 4 = 100\n Side = √100 = 10 cm\n\nWhy other options are wrong:\n            • (a) 5 cm: Result of forgetting division by 2 in formula Area of Triangle\n            • (c) 15 cm: Result of using formula Rectangle without division by 2\n            • (d) 20 cm: Result of adding Base and Height instead of multiplying them",
                                    solution_steps_ar='["Area = (√3 ÷ 4) × Side²","25√3 = (√3 ÷ 4) × Side²","Side² = 100 → Side = 10 cm"]',
        tags="triangle", stage="mock",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # Q111
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.3,
                                    text_ar="Rectangle: Length = 13 cm , Width = 6 cm.\nWhat is its perimeter?",
                                    option_a="19 cm",             option_b="38 cm",             option_c="78 cm",             option_d="156 cm",
                                    correct_option="b",
                                    explanation_ar="Formula:\n Perimeter of Rectangle = 2 × (Length + Width)\n\nSubstitution:\n Perimeter = 2 × (13 + 6) = 2 × 19 = 38 cm\n\nWhy other options are wrong:\n            • (a) 19 cm: Result of using formula Perimeter instead of Area or vice versa\n            • (c) 78 cm: Result of forgetting multiplying sum dimensions by 2 when calculating Perimeter\n            • (d) 156 cm: Result of adding dimensions instead of multiplying",
                                    solution_steps_ar='["Formula: Perimeter of Rectangle = 2 × (Length + Width)","Perimeter = 2 × (13 + 6) = 2 × 19 = 38 cm"]',
        tags="rectangle,perimeter", stage="mock",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # ══════════════════════════════════════════════════════════════
                # ██ New Questions 112–167 (56 question) ██
                # ══════════════════════════════════════════════════════════════

                # ── Q112: Cone r=3 =4 Volume (diff=0.2) ── diagnostic
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.2,
                                    text_ar="Cone: Base radius (r) = 3 cm , Height = 4 cm.\nWhat is its volume?\n(π = ²²⁄₇)",
                                    option_a="12 cm³",             option_b="24 cm³",             option_c="36 cm³",             option_d="³77 cm³",
                                    correct_option="d",
                                    explanation_ar="Formula:\n Volume of Cone = ⅓ × π × r² × \n\nSubstitution:\n = ⅓ × (22 ÷ 7) × 3² × 4\n = ⅓ × (22 ÷ 7) × 9 × 4\n = ⅓ × (22 ÷ 7) × 36\n = (22 × 36) ÷ (7 × 3)\n = 792 ÷ 21 = 377 cm³\n\nWhy other options are wrong:\n            • (a) 12 cm³: Result of Calculate Area instead of Volume\n            • (c) 36 cm³: Result of forgetting one of three dimensions\n            • (d) 205 cm³: Result of using 2D shape formula",
                                    solution_steps_ar='["Volume of Cone = ⅓ × π × r² × ","= ⅓ × (22 ÷ 7) × 9 × 4","= 792 ÷ 21 ≈ 377 cm³"]',
        tags="cone,volume,3d-shape", stage="diagnostic",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # ── Q113: Sphere r=7 Volume (diff=0.2) ── diagnostic
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.2,
                                    text_ar="Sphere: Radius (r) = 7 cm.\nWhat is its volume?\n(π = ²²⁄₇)",
                                    option_a="9053 cm³",             option_b="14373 cm³",             option_c="616 cm³",             option_d="205 cm³",
                                    correct_option="b",
                                    explanation_ar="Formula:\n Volume of Sphere = ⁴⁄₃ × π × r³\n\nSubstitution:\n = ⁴⁄₃ × (22 ÷ 7) × 7³\n = ⁴⁄₃ × (22 ÷ 7) × 343\n = ⁴⁄₃ × 22 × 49\n = ⁴⁄₃ × 1078\n = 4312 ÷ 3 = 14373 cm³\n\nWhy other options are wrong:\n            • (a) 9053 cm³: Result of using formula Area instead of Volume\n            • (c) 616 cm³: Result of forgetting ⁴⁄₃ in formula Volume\n            • (d) 205 cm³: Result of error in Calculate cubing",
                                    solution_steps_ar='["Volume of Sphere = ⁴⁄₃ × π × r³","= ⁴⁄₃ × (22 ÷ 7) × 343","= 4312 ÷ 3 ≈ 14373 cm³"]',
        tags="sphere,volume,3d-shape", stage="diagnostic",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

                # ── Q114: Rhombus Diagonals 6 and 8 Area (diff=0.2) ── diagnostic
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.2,
                                    text_ar="Rhombus: Diameter First = 6 cm , Diameter Second = 8 cm.\nWhat is its area?",
                                    option_a="14 cm²",             option_b="24 cm²",             option_c="48 cm²",             option_d="12 cm²",
                                    correct_option="b",
                                    explanation_ar="Formula:\n        Area of Rhombus = ½ × Diameter₁ × Diameter₂\n\nSubstitution:\n        Area = ½ × 6 × 8 = 24 cm²\n\nWhy other options are wrong:\n            • (b) 16√3 cm²: Result of using formula Perimeter instead of Area\n            • (c) 48 cm²: Result of forgetting sides in Calculate Area\n            • (d) 12 cm²: Result of error in Calculate",
                                    solution_steps_ar='["Area of Rhombus = ½ × Diameter₁ × Diameter₂","= ½ × 6 × 8 = 24 cm²"]',
        tags="rhombus,diagonal,area", stage="diagnostic",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

                # ── Q115: Regular hexagon side=4 Area (diff=0.3) ── foundation
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.3,
                                    text_ar="Regular hexagon: side edge = 4 cm.\nWhat is its area?",
                                    option_a="24√3 cm²",             option_b="16√3 cm²",             option_c="48√3 cm²",             option_d="12√3 cm²",
                                    correct_option="a",
                                    explanation_ar="Formula:\n        Area = (3√3 ÷ 2) × Side²\n\nSubstitution:\n = (3√3 ÷ 2) × 4²\n = (3√3 ÷ 2) × 16\n = 24√3 cm²\n\nWhy other options are wrong:\n            • (a) 744 cm³: Result of using formula Perimeter instead of Area\n            • (c) 48√3 cm²: Result of forgetting sides in Calculate Area\n            • (d) 12√3 cm²: Result of error in Calculate",
                                    solution_steps_ar='["Area = (3√3 ÷ 2) × Side²","= (3√3 ÷ 2) × 16 = 24√3 cm²"]',
        tags="area", stage="foundation",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

                # ── Q116: Cone r=7 =24 Volume (diff=0.3) ── foundation
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.3,
                                    text_ar="Cone: Base radius (r) = 7 cm , Height = 24 cm.\nWhat is its volume?\n(π = ²²⁄₇)",
                                    option_a="744 cm³",             option_b="1232 cm³",             option_c="1848 cm³",             option_d="3696 cm³",
                                    correct_option="b",
                                    explanation_ar="Formula:\n Volume of Cone = ⅓ × π × r² × h\n\nSubstitution:\n = ⅓ × (22 ÷ 7) × 7² × 24\n = ⅓ × (22 ÷ 7) × 49 × 24\n = ⅓ × 22 × 7 × 24\n = ⅓ × 3696 = 1232 cm³\n\nWhy other options are wrong:\n            • (a) 744 cm³: Result of using wrong formula or miscalculating π × r² × h\n            • (c) 1848 cm³: Result of using ½ instead of ⅓ in the cone volume formula\n            • (d) 3696 cm³: Result of forgetting to divide by 3 (this is π × r² × h, the cylinder volume)",
                                    solution_steps_ar='["Volume of Cone = ⅓ × π × r² × ","= ⅓ × (22 ÷ 7) × 49 × 24","= ⅓ × 3696 = 1232 cm³"]',
        tags="cone,volume,3d-shape", stage="foundation",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # ── Q117: Sphere r=3 Area (diff=0.3) ── foundation
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.3,
                                    text_ar="Sphere: Radius (r) = 3 cm.\nWhat is Surface area?\n(π = ²²⁄₇)",
                                    option_a="72 cm²",             option_b="1131 cm²",             option_c="36 cm²",             option_d="154 cm²",
                                    correct_option="b",
                                    explanation_ar="Formula:\nSurface Area of Sphere = 4 × π × r²\n\nSubstitution:\n= 4 × (22/7) × 3²\n= 4 × (22/7) × 9\n= (4 × 22 × 9) / 7\n= 792 / 7 ≈ 113.1 cm²\n\nWhy other options are wrong:\n• (a) 72 cm²: Incorrect formula application\n• (c) 36 cm²: Only calculated r² without full formula\n• (d) 154 cm²: Used wrong radius value",
                                    solution_steps_ar='["Surface Area of Sphere = 4 × π × r²","= 4 × (22/7) × 9","= 792 / 7 ≈ 113.1 cm²"]',
        tags="sphere,area,3d-shape", stage="foundation",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # ── Q118: sum of angles of Polygon (diff=0.3) ── foundation
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.3,
                                    text_ar="Regular pentagon.\nWhat is Measure of each angle in it?",
                                    option_a="90°",             option_b="108°",             option_c="120°",             option_d="135°",
                                    correct_option="b",
                                    explanation_ar="Formula:\n sum Interior angles = ( − 2) × 180°\n Angle = sum ÷ \n\nSubstitution:\n sum = (5 − 2) × 180 = 3 × 180 = 540°\n Angle = 540 ÷ 5 = 108°\n\nWhy other options are wrong:\n            • (a) 90°: Result of confusing sum (90°) sum (180°)\n            • (c) 120°: Result of using wrong angle sum for shape\n            • (d) 135°: Result of forgetting to subtract given angles",
                                    solution_steps_ar='["sum Therefore = ( − 2) × 180°","= (5 − 2) × 180 = 540°"," Angle = 540 ÷ 5 = 108°"]',
        tags="angle", stage="foundation",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # ── Q119: Rhombus Diagonals 10 and 24 Area (diff=0.3) ── foundation
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.3,
                                    text_ar="Rhombus: Diameter First = 10 cm , Diameter Second = 24 cm.\nWhat is its area?",
                                    option_a="60 cm²",             option_b="120 cm²",             option_c="240 cm²",             option_d="34 cm²",
                                    correct_option="b",
                                    explanation_ar="Formula:\n        Area of Rhombus = ½ × Diameter₁ × Diameter₂\n\nSubstitution:\n        Area = ½ × 10 × 24 = 120 cm²\n\nWhy other options are wrong:\n            • (a) 60 cm²: Result of using formula Perimeter instead of Area\n            • (b) 12 cm: Result of forgetting sides in Calculate Area\n            • (d) 34 cm²: Result of error in Calculate",
                                    solution_steps_ar='["Area of Rhombus = ½ × Diameter₁ × Diameter₂","= ½ × 10 × 24 = 120 cm²"]',
        tags="rhombus,diagonal,area", stage="foundation",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # ── Q120: of Rectangular prism 3×4×12 (diff=0.4) ── foundation
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.4,
                                    text_ar="Rectangular prism: Length = 3 cm , Width = 4 cm , Height = 12 cm.\nWhat is length of Space diagonal?",
                                    option_a="5 cm",             option_b="12 cm",             option_c="13 cm",             option_d="19 cm",
                                    correct_option="c",
                                    explanation_ar="Formula:\n Space diagonal = √(Length² + Width² + Height²)\n\nSubstitution:\n = √(3² + 4² + 12²)\n = √(9 + 16 + 144)\n = √169 = 13 cm\n\nWhy other options are wrong:\n            • (a) 5 cm: Result of Calculate Area instead of Volume\n            • (b) 12 cm: Result of forgetting one dimension\n            • (d) 19 cm: Result of using 2D shape formula",
                                    solution_steps_ar='["Space diagonal = √(Length² + Width² + Height²)","= √(9 + 16 + 144)","= √169 = 13 cm"]',
        tags="3d-shape,diagonal", stage="foundation",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # ── Q121: Open-top box 10×6×4 Area (diff=0.4) ── foundation
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.4,
                                    text_ar="Open-top box: Length = 10 cm , Width = 6 cm , Height = 4 cm.\nWhat is Area?",
                                    option_a="128 cm²",             option_b="248 cm²",             option_c="188 cm²",             option_d="240 cm³",
                                    correct_option="c",
                                    explanation_ar="Area = Base + Lateral faces (no top lid)\n = (10 × 6) + 2 × (10 × 4) + 2 × (6 × 4)\n = 60 + 80 + 48 = 188 cm²\n\nWhy other options are wrong:\n            • (a) 128 cm²: Only lateral faces without the base (80 + 48)\n            • (b) 248 cm²: Closed box with top lid included (188 + 60)\n            • (d) 240 cm³: This is the volume (10 × 6 × 4), not the surface area",
                                    solution_steps_ar='["Base = 10 × 6 = 60 cm²","Lateral faces sides = 2 × (10 × 4) = 80 cm²","Lateral faces = 2 × (6 × 4) = 48 cm²","sum = 60 + 80 + 48 = 188 cm²"]',
        tags="3d-shape,area", stage="foundation",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # ── Q122: Cone r=5 =13 Lateral area (diff=0.4) ── foundation
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.4,
                                    text_ar="Cone: Base radius (r) = 5 cm , Slant height () = 13 cm.\nWhat is Lateral area?\n(π = ²²⁄₇)",
                                    option_a="65 cm²",             option_b="130 cm²",             option_c="²043 cm²",             option_d="4086 cm²",
                                    correct_option="c",
                                    explanation_ar="Formula:\n Lateral area = π × r × \n\nSubstitution:\n = (22 ÷ 7) × 5 × 13\n = (22 × 65) ÷ 7\n = 1430 ÷ 7 = 2043 cm²\n\nWhy other options are wrong:\n            • (a) 65 cm²: Result of using formula Perimeter instead of Area\n            • (c) 144°: Result of forgetting sides in Calculate Area\n            • (d) 4086 cm²: Result of error in Calculate",
                                    solution_steps_ar='["Lateral area = π × r × ","= (22 ÷ 7) × 5 × 13","= 1430 ÷ 7 ≈ 2043 cm²"]',
        tags="cone,area,3d-shape", stage="foundation",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # ── Q123: sum of angles of Polygon (diff=0.4) ── building
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.4,
                                    text_ar="Regular octagon.\nWhat is Measure of each angle in it?",
                                    option_a="120°",             option_b="135°",             option_c="144°",             option_d="150°",
                                    correct_option="b",
                                    explanation_ar="Formula:\n Angle = ( − 2) × 180 ÷ \n\nSubstitution:\n = (8 − 2) × 180 ÷ 8\n = 6 × 180 ÷ 8\n = 1080 ÷ 8 = 135°\n\nWhy other options are wrong:\n            • (a) 120°: Result of confusing sum (90°) sum (180°)\n            • (c) 144°: Result of using wrong angle sum for shape\n            • (d) 150°: Result of forgetting to subtract given angles",
                                    solution_steps_ar='[" Angle = ( − 2) × 180 ÷ ","= (8 − 2) × 180 ÷ 8","= 1080 ÷ 8 = 135°"]',
        tags="angle", stage="foundation",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # ── Q124: Sphere r=14 Volume (diff=0.4) ── foundation
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.4,
                                    text_ar="Sphere: Radius (r) = 14 cm.\nWhat is its volume?\n(π = ²²⁄₇)",
                                    option_a="8624 cm³",             option_b="114987 cm³",             option_c="2464 cm³",             option_d="34653 cm³",
                                    correct_option="b",
                                    explanation_ar="Formula:\n Volume of Sphere = ⁴⁄₃ × π × r³\n\nSubstitution:\n = ⁴⁄₃ × (22 ÷ 7) × 14³\n = ⁴⁄₃ × (22 ÷ 7) × 2744\n = ⁴⁄₃ × 22 × 392\n = ⁴⁄₃ × 8624\n = 34496 ÷ 3 = 114987 cm³\n\nWhy other options are wrong:\n            • (b) 158 cm²: Result of using formula Area instead of Volume\n            • (c) 2464 cm³: Result of forgetting ⁴⁄₃ in formula Volume\n            • (d) 34653 cm³: Result of error in Calculate cubing",
                                    solution_steps_ar='["Volume of Sphere = ⁴⁄₃ × π × r³","= ⁴⁄₃ × (22 ÷ 7) × 2744","= 34496 ÷ 3 ≈ 114987 cm³"]',
        tags="sphere,volume,3d-shape", stage="foundation",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # ── Q125: Open-top box 8×5×3 Area (diff=0.4) ── foundation
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.4,
                                    text_ar="Open-top box: Length = 8 cm , Width = 5 cm , Height = 3 cm.\nWhat is Area?",
                                    option_a="118 cm²",             option_b="158 cm²",             option_c="79 cm²",             option_d="120 cm²",
                                    correct_option="a",
                                    explanation_ar="Area = Base + Lateral faces\n = (8 × 5) + 2 × (8 × 3) + 2 × (5 × 3)\n = 40 + 48 + 30 = 118 cm²\n\nWhy other options are wrong:\n            • (a) 8 cm: Result of Calculate Area instead of Volume\n            • (c) 79 cm²: Result of forgetting one dimension\n            • (d) 158 cm²: Result of using 2D shape formula",
                                    solution_steps_ar='["Base = 8 × 5 = 40 cm²","Lateral faces sides = 2 × (8 × 3) = 48 cm²","Lateral faces = 2 × (5 × 3) = 30 cm²","sum = 40 + 48 + 30 = 118 cm²"]',
        tags="3d-shape,area", stage="foundation",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # ── Q126: Rhombus Diagonals 12 and 16 side (diff=0.4) ── foundation
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.4,
                                    text_ar="Rhombus: Diameter First = 12 cm , Diameter Second = 16 cm.\nWhat is length of of Rhombus?",
                                    option_a="8 cm",             option_b="10 cm",             option_c="14 cm",             option_d="20 cm",
                                    correct_option="b",
                                    explanation_ar=" Rhombus intersect at Right angle andbisect .\n Radius₁ = 6 cm , Radius₂ = 8 cm\n\nusing Pythagorean:\n Side = √(6² + 8²) = √(36 + 64) = √100 = 10 cm\n\nWhy other options are wrong:\n            • (b) 13 cm: Result of adding Sides instead of using Pythagorean Theorem\n            • (c) 14 cm: Result of forgetting squaring adding Square\n            • (d) 20 cm: Result of confusing Square Hypotenuse and Square Side of Right",
                                    solution_steps_ar='["Radius₁ = 6 , Radius₂ = 8","Side = √(6² + 8²)","= √(36 + 64) = √100 = 10 cm"]',
        tags="rhombus,diagonal,pythagorean", stage="foundation",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # ── Q127: of Rectangular prism 2×6×9 (diff=0.4) ── building
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.4,
                                    text_ar="Rectangular prism: Length = 2 cm , Width = 6 cm , Height = 9 cm.\nWhat is length of Space diagonal?",
                                    option_a="11 cm",             option_b="13 cm",             option_c="17 cm",             option_d="√121 cm",
                                    correct_option="a",
                                    explanation_ar="Formula:\n Space diagonal = √(Length² + Width² + Height²)\n\nSubstitution:\n = √(2² + 6² + 9²)\n = √(4 + 36 + 81)\n = √121 = 11 cm\n\nWhy other options are wrong:\n            • (a) 15 cm²: Result of Calculate Area instead of Volume\n            • (b) 13 cm: Result of forgetting one dimension\n            • (d) √121 cm: Result of using 2D shape formula",
                                    solution_steps_ar='["Space diagonal = √(Length² + Width² + Height²)","= √(4 + 36 + 81)","= √121 = 11 cm"]',
        tags="3d-shape,diagonal", stage="building",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # ── Q128: Similarity 1:3 Area (diff=0.5) ── building
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.5,
                                    text_ar="Similar Triangles Similar: Similarity ratio = 1 : 3.\nIf Area of Triangle = 5 cm²,        Area ?",
                                    option_a="15 cm²",             option_b="25 cm²",             option_c="45 cm²",             option_d="125 cm²",
                                    correct_option="c",
                                    explanation_ar="Area ratio = Square Similarity ratio\n = (1/3)² = 1/9\n\n5 ÷ Area₂ = 1 ÷ 9\nArea₂ = 5 × 9 = 45 cm²\n\nWhy other options are wrong:\n            • (a) 15 cm²: Result of forgetting division by 2 in formula Area of Triangle\n            • (c) 72√3 cm²: Result of using formula Rectangle without division by 2\n            • (d) 125 cm²: Result of adding Base and Height instead of multiplying them",
                                    solution_steps_ar='["Area ratio = Square Similarity ratio = 1/9","5 ÷ Area₂ = 1 ÷ 9","Area₂ = 5 × 9 = 45 cm²"]',
        tags="triangle,area", stage="building",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # ── Q129: Regular hexagon side=6 Area (diff=0.5) ── building
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.5,
                                    text_ar="Regular hexagon: side edge = 6 cm.\nWhat is its area?",
                                    option_a="36√3 cm²",             option_b="54√3 cm²",             option_c="72√3 cm²",             option_d="108√3 cm²",
                                    correct_option="b",
                                    explanation_ar="Formula:\n        Area = (3√3 ÷ 2) × Side²\n\nSubstitution:\n = (3√3 ÷ 2) × 6²\n = (3√3 ÷ 2) × 36\n = 54√3 cm²\n\nWhy other options are wrong:\n            • (b) 43 cm²: Result of using formula Perimeter instead of Area\n            • (c) 72√3 cm²: Result of forgetting sides in Calculate Area\n            • (d) 108√3 cm²: Result of error in Calculate",
                                    solution_steps_ar='["Area = (3√3 ÷ 2) × Side²","= (3√3 ÷ 2) × 36","= 54√3 cm²"]',
        tags="area", stage="building",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # ── Q130: Circle inscribed in Square side 10 (diff=0.5) ── building
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.5,
                                    text_ar="A square has side length 10 cm.\nA circle is inscribed inside the square.\nWhat is the area of the circle?\n(π = 22/7)",
                                    option_a="215 cm²",             option_b="43 cm²",             option_c="785 cm²",             option_d="100 cm²",
                                    correct_option="a",
                                    explanation_ar="r Circle = Square ÷ 2 = 5 cm\n\nArea of Diagonal = 10² = 100 cm²\nArea of Circle = π × r² = (22 ÷ 7) × 25 = 550 ÷ 7 = 786 cm²\n\nRemaining = 100 − 786 ≈ 214 ≈ 215 cm²\n\nWhy other options are wrong:\n            • (a) 8 cm: Result of using formula Perimeter instead of Area or vice versa\n            • (b) 43 cm²: Result of using Diameter instead of Radius in Formula\n            • (d) 100 cm²: Result of forgetting squaring Radius when calculating Area",
                                    solution_steps_ar='["r = 10 ÷ 2 = 5 cm","Area of Diagonal = 100 cm²","Area of Circle = (22 ÷ 7) × 25 ≈ 786 cm²"," ≈ 100 − 786 ≈ 215 cm²"]',
        tags="circle,square,area,composite", stage="building",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # ── Q131: of Circle and length (diff=0.5) ── building
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.5,
                                    text_ar="Circle center, (r) = 5 cm.\nrπ 13 cm.\nTangent drawn from Circle in .\nWhat is tangent edge ?",
                                    option_a="8 cm",             option_b="10 cm",             option_c="12 cm",             option_d="18 cm",
                                    correct_option="c",
                                    explanation_ar=" Tangent Radius at rπ .\nTriangle        Right Angle in .\n\nusing Pythagorean:\n ² = ² − ²\n = 13² − 5²\n = 169 − 25 = 144\n = √144 = 12 cm\n\nWhy other options are wrong:\n            • (a) 8 cm: Result of using formula Perimeter instead of Area or vice versa\n            • (c) 1620°: Result of using Diameter instead of Radius in Formula\n            • (d) 18 cm: Result of forgetting squaring Radius when calculating Area",
                                    solution_steps_ar='[" ⊥ Radius at rπ ","² = ² − ² = 13² − 5²","= 169 − 25 = 144"," = √144 = 12 cm"]',
        tags="circle,pythagorean", stage="building",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # ── Q132: sum sum of angles of Polygon (diff=0.5) ── building
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.5,
                                    text_ar="What is sum Interior angles of Decagon (10 )?",
                                    option_a="1260°",             option_b="1440°",             option_c="1620°",             option_d="1800°",
                                    correct_option="b",
                                    explanation_ar="Formula:\n sum Interior angles = ( − 2) × 180°\n\nSubstitution:\n = (10 − 2) × 180\n = 8 × 180 = 1440°\n\nWhy other options are wrong:\n            • (a) 1260°: Result of confusing sum (90°) sum (180°)\n            • (c) 1620°: Result of using wrong angle sum for shape\n            • (d) 1800°: Result of forgetting to subtract given angles",
                                    solution_steps_ar='["sum Therefore = ( − 2) × 180°","= (10 − 2) × 180","= 8 × 180 = 1440°"]',
        tags="angle", stage="building",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # ── Q133: Sphere r=7 Area (diff=0.5) ── building
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.5,
                                    text_ar="Sphere: Radius (r) = 7 cm.\nWhat is Surface area?\n(π = ²²⁄₇)",
                                    option_a="308 cm²",             option_b="616 cm²",             option_c="154 cm²",             option_d="1232 cm²",
                                    correct_option="b",
                                    explanation_ar="Formula:\nSurface Area of Sphere = 4 × π × r²\n\nSubstitution:\n= 4 × (22/7) × 7²\n= 4 × (22/7) × 49\n= 4 × 22 × 7 = 616 cm²\n\nWhy other options are wrong:\n• (a) 308 cm²: Only calculated 2πr² (half the surface area)\n• (c) 154 cm²: Only calculated πr² (one-quarter of surface area)\n• (d) 1232 cm²: Doubled the correct answer",
                                    solution_steps_ar='["Surface Area of Sphere = 4 × π × r²","= 4 × (22/7) × 49","= 4 × 22 × 7 = 616 cm²"]',
        tags="sphere,area,3d-shape", stage="building",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # ── Q134: Cone r=6 =8 Slant height (diff=0.5) ── peak
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.5,
                                    text_ar="Cone: Base radius (r) = 6 cm , Height = 8 cm.\nWhat is length of Slant height ()?",
                                    option_a="7 cm",             option_b="10 cm",             option_c="12 cm",             option_d="14 cm",
                                    correct_option="b",
                                    explanation_ar="using Pythagorean:\n ² = r² + ²\n = 6² + 8²\n = 36 + 64 = 100\n = √100 = 10 cm\n\nWhy other options are wrong:\n            • (a) 7 cm: Result of adding Sides instead of using Pythagorean Theorem\n            • (b) 98 cm²: Result of forgetting squaring adding Square\n            • (c) 12 cm: Result of confusing Square Hypotenuse and Square Side of Right",
                                    solution_steps_ar='["² = r² + ²","= 36 + 64 = 100"," = √100 = 10 cm"]',
        tags="cone,pythagorean,3d-shape", stage="peak",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # ── Q135: Square Circumscribed around Circle r=7 (diff=0.5) ── peak
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.5,
                                    text_ar="Circle (r) = 7 cm.\nSquareinscribed in Circle (Circle inscribed in Square).\nWhat is Area of Square?",
                                    option_a="49 cm²",             option_b="98 cm²",             option_c="144 cm²",             option_d="196 cm²",
                                    correct_option="d",
                                    explanation_ar=" Square = of Circle = 2 × r = 14 cm\n\nArea of Diagonal = 14² = 196 cm²\n\nWhy other options are wrong:\n            • (a) 49 cm²: Result of using formula Perimeter instead of Area or vice versa\n            • (b) 98 cm²: Result of using Diameter instead of Radius in Formula\n            • (d) 64 cm: Result of forgetting squaring Radius when calculating Area",
                                    solution_steps_ar='[" Square = of Circle = 2 × 7 = 14 cm","Area of Diagonal = 14² = 196 cm²"]',
        tags="circle,square,area", stage="peak",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # ── Q136: Similarity 2:5 Perimeter (diff=0.5) ── peak
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.5,
                                    text_ar="Polygons Similar: Similarity ratio = 2 : 5.\nIf Perimeter of Polygon = 16 cm, Perimeter ?",
                                    option_a="24 cm",             option_b="32 cm",             option_c="40 cm",             option_d="64 cm",
                                    correct_option="c",
                                    explanation_ar=" Ratio of Perimeters = Similarity ratio\n 16 ÷ Perimeter₂ = 2 ÷ 5\n Perimeter₂ = 16 × 5 ÷ 2 = 40 cm\n\nWhy other options are wrong:\n            • (a) 24 cm: Result of Calculate Area instead of Perimeter\n            • (c) 135°: Result of forgetting sum dimensions\n            • (d) 64 cm: Result of adding instead of Sides",
                                    solution_steps_ar='[" Ratio of Perimeters = Similarity ratio = 2/5","16 ÷ Perimeter₂ = 2 ÷ 5","Perimeter₂ = 16 × 5 ÷ 2 = 40 cm"]',
        tags="perimeter", stage="peak",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # ── Q137: sum of angles of Polygon (diff=0.6) ── building
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.6,
                                    text_ar="Regular hexagon.\nWhat is Measure of each angle in it?",
                                    option_a="108°",             option_b="120°",             option_c="135°",             option_d="140°",
                                    correct_option="b",
                                    explanation_ar="Formula:\n Angle = ( − 2) × 180 ÷ \n\nSubstitution:\n = (6 − 2) × 180 ÷ 6\n = 4 × 180 ÷ 6\n = 720 ÷ 6 = 120°\n\nWhy other options are wrong:\n            • (a) 108°: Result of confusing sum (90°) sum (180°)\n            • (b) 12 cm: Result of using wrong angle sum for shape\n            • (d) 140°: Result of forgetting to subtract given angles",
                                    solution_steps_ar='[" Angle = ( − 2) × 180 ÷ ","= (6 − 2) × 180 ÷ 6","= 720 ÷ 6 = 120°"]',
        tags="angle", stage="building",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # ── Q138: of Circle r=8 =17 (diff=0.6) ── building
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.6,
                                    text_ar="Circle center, (r) = 8 cm.\nrπ 17 cm.\nTangent drawn from Circle in .\nWhat is tangent edge ?",
                                    option_a="9 cm",             option_b="12 cm",             option_c="15 cm",             option_d="20 cm",
                                    correct_option="c",
                                    explanation_ar=" ⊥ Radius at rπ .\n ² = ² − ²\n = 17² − 8²\n = 289 − 64 = 225\n = √225 = 15 cm\n\nWhy other options are wrong:\n            • (a) 9 cm: Result of using formula Perimeter instead of Area or vice versa\n            • (b) 12 cm: Result of using Diameter instead of Radius in Formula\n            • (d) 20 cm: Result of forgetting squaring Radius when calculating Area",
                                    solution_steps_ar='["² = ² − ²","= 17² − 8² = 289 − 64 = 225"," = √225 = 15 cm"]',
        tags="circle,pythagorean", stage="building",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # ── Q139: Cone Total surface area r=7 =25 (diff=0.6) ── building
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.6,
                                    text_ar="Cone: Base radius (r) = 7 cm , Slant height () = 25 cm.\nWhat is Total surface area?\n(π = ²²⁄₇)",
                                    option_a="400 cm²",             option_b="550 cm²",             option_c="704 cm²",             option_d="858 cm²",
                                    correct_option="c",
                                    explanation_ar="Total surface area = Lateral area + Area Base\n = π × r × + π × r²\n = π × r × ( + r)\n = (22 ÷ 7) × 7 × (25 + 7)\n = 22 × 32 = 704 cm²\n\nWhy other options are wrong:\n            • (b) 550 cm²: Result of using formula Perimeter instead of Area\n            • (c) 4√3 cm: Result of forgetting sides in Calculate Area\n            • (d) 858 cm²: Result of error in Calculate",
                                    solution_steps_ar='["Total surface area = π × r × ( + r)","= (22 ÷ 7) × 7 × 32","= 22 × 32 = 704 cm²"]',
        tags="cone,area,3d-shape", stage="building",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # ── Q140: Circle inscribed in Equilateral triangle side 12 (diff=0.6) ── peak
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.6,
                                    text_ar="Equilateral triangle side edge = 12 cm.\nWhat is  Circle()?",
                                    option_a="2√3 cm",             option_b="3√3 cm",             option_c="4√3 cm",             option_d="6√3 cm",
                                    correct_option="a",
                                    explanation_ar="Formula:\n r Circle Equilateral triangle = Side ÷ (2√3)\n or = Side × √3 ÷ 6\n\nSubstitution:\n = 12 × √3 ÷ 6 = 2√3 cm\n\nWhy other options are wrong:\n            • (b) 3√3 cm: Result of using formula Perimeter instead of Area or vice versa\n            • (c) 4√3 cm: Result of using Diameter instead of Radius in Formula\n            • (d) 6√3 cm: Result of forgetting squaring Radius when calculating Area",
                                    solution_steps_ar='["r = Side × √3 ÷ 6","= 12 × √3 ÷ 6","= 2√3 cm"]',
        tags="circle,triangle", stage="peak",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # ── Q141: Regular hexagon side=10 Perimeter (diff=0.6) ── peak
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.6,
                                    text_ar="Regular hexagon: side edge = 10 cm.\nWhat is its perimeter and Area?",
                                    option_a="Perimeter = 60 cm , Area = 150√3 cm²",             option_b="Perimeter = 50 cm , Area = 100√3 cm²",
                                    option_c="Perimeter = 60 cm , Area = 100√3 cm²",             option_d="Perimeter = 60 cm , Area = 200√3 cm²",
                                    correct_option="a",
                                    explanation_ar="Perimeter = 6 × Side = 6 × 10 = 60 cm\n\nArea = (3√3 ÷ 2) × Side²\n = (3√3 ÷ 2) × 100 = 150√3 cm²\n\nWhy other options are wrong:\n            • (a) 6√2 cm: Result of using formula Perimeter instead of Area\n            • (c) Perimeter = 60 cm , Area = 100√3 cm²: Result of forgetting sides in Calculate Area\n            • (d) Perimeter = 60 cm , Area = 200√3 cm²: Result of error in Calculate",
                                    solution_steps_ar='["Perimeter = 6 × 10 = 60 cm","Area = (3√3 ÷ 2) × 100","= 150√3 cm²"]',
        tags="area,perimeter", stage="peak",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # ── Q142: of Cube 6 (diff=0.6) ── peak
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.6,
                                    text_ar="Cube: length = 6 cm.\nWhat is its diagonal edge ?",
                                    option_a="6√2 cm",             option_b="6√3 cm",             option_c="12 cm",             option_d="18 cm",
                                    correct_option="b",
                                    explanation_ar="Formula:\n Space diagonal of Cube = Edge × √3\n\nSubstitution:\n = 6 × √3 = 6√3 cm\n\nWhy other options are wrong:\n            • (b) 168 cm²: Result of Calculate Area of faces instead of 6 Lateral faces\n            • (c) 12 cm: Result of confusing Volume and Total surface area\n            • (d) 18 cm: Result of squaring Edge instead of cubing it or vice versa",
                                    solution_steps_ar='["Space diagonal = Edge × √3","= 6 × √3 = 6√3 cm"]',
        tags="cube,diagonal,3d-shape", stage="peak",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # ── Q143: Rhombus Diagonals 14 and 48 Area andSide (diff=0.6) ── mock
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.6,
                                    text_ar="Rhombus: Diameter First = 14 cm , Diameter Second = 48 cm.\nWhat is its area?",
                                    option_a="336 cm²",             option_b="168 cm²",             option_c="672 cm²",             option_d="62 cm²",
                                    correct_option="a",
                                    explanation_ar="Formula:\n        Area of Rhombus = ½ × Diameter₁ × Diameter₂\n\nSubstitution:\n        Area = ½ × 14 × 48 = 336 cm²\n\nWhy other options are wrong:\n            • (a) 3 cm: Result of using formula Perimeter instead of Area\n            • (c) 672 cm²: Result of forgetting sides in Calculate Area\n            • (d) 62 cm²: Result of error in Calculate",
                                    solution_steps_ar='["Area of Rhombus = ½ × Diameter₁ × Diameter₂","= ½ × 14 × 48 = 336 cm²"]',
        tags="rhombus,diagonal,area", stage="mock",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # ── Q144: Circle Circumscribed around Triangle Right Hypotenuse 10 (diff=0.6) ── mock
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.6,
                                    text_ar="Right triangle: Hypotenuse = 10 cm.\nWhat is  Circle Circumscribed around Triangle?",
                                    option_a="3 cm",             option_b="5 cm",             option_c="7 cm",             option_d="10 cm",
                                    correct_option="b",
                                    explanation_ar="in Right Triangle: Circumcircle center Hypotenuse.\n r = Hypotenuse ÷ 2 = 10 ÷ 2 = 5 cm\n\nWhy other options are wrong:\n            • (a) 3 cm: Result of using formula Perimeter instead of Area or vice versa\n            • (c) 7 cm: Result of using Diameter instead of Radius in Formula\n            • (d) 10 cm: Result of forgetting squaring Radius when calculating Area",
                                    solution_steps_ar='["in Right Triangle: r Circle Circumference = Hypotenuse ÷ 2","r = 10 ÷ 2 = 5 cm"]',
        tags="circle,triangle", stage="mock",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # ── Q145: Similarity 2:3 (diff=0.6) ── mock
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.6,
                                    text_ar="Polygons Similar: Similarity ratio = 2 : 3.\nIf Area = 20 cm²,        Area ?",
                                    option_a="30 cm²",             option_b="45 cm²",             option_c="60 cm²",             option_d="90 cm²",
                                    correct_option="b",
                                    explanation_ar="Area ratio = Square Similarity ratio\n = (2/3)² = 4/9\n\n20 ÷ Area₂ = 4 ÷ 9\nArea₂ = 20 × 9 ÷ 4 = 45 cm²\n\nWhy other options are wrong:\n            • (a) 30 cm²: Result of using formula Perimeter instead of Area\n            • (c) 60 cm²: Result of forgetting sides in Calculate Area\n            • (d) 90 cm²: Result of error in Calculate",
                                    solution_steps_ar='["Area ratio = (2/3)² = 4/9","20 ÷ Area₂ = 4 ÷ 9","Area₂ = 20 × 9 ÷ 4 = 45 cm²"]',
        tags="area", stage="mock",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # ── Q146: Open-top box Square Base side=7 =3 (diff=0.6) ── mock
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.6,
                                    text_ar="Open-top box with Square Base: Base = 7 cm , Height = 3 cm.\nWhat is Area?",
                                    option_a="49 cm²",             option_b="133 cm²",             option_c="182 cm²",             option_d="84 cm²",
                                    correct_option="b",
                                    explanation_ar="Area = Base + 4 Lateral faces \n = 7² + 4 × (7 × 3)\n = 49 + 4 × 21\n = 49 + 84 = 133 cm²\n\nWhy other options are wrong:\n            • (a) 49 cm²: Result of Calculate Area instead of Volume\n            • (c) 182 cm²: Result of forgetting one dimension\n            • (d) 84 cm²: Result of using 2D shape formula",
                                    solution_steps_ar='["Base = 7² = 49 cm²","Lateral faces = 4 × (7 × 3) = 84 cm²","sum = 49 + 84 = 133 cm²"]',
        tags="3d-shape,area,square", stage="mock",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # ── Q147: Sphere r=21 Volume (diff=0.6) ── mock
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.6,
                                    text_ar="Sphere: Radius (r) = 21 cm.\nWhat is its volume?\n(π = ²²⁄₇)",
                                    option_a="19404 cm³",             option_b="38808 cm³",             option_c="55440 cm³",             option_d="27720 cm³",
                                    correct_option="b",
                                    explanation_ar="Formula:\n Volume of Sphere = ⁴⁄₃ × π × r³\n\nSubstitution:\n = ⁴⁄₃ × (22 ÷ 7) × 21³\n = ⁴⁄₃ × (22 ÷ 7) × 9261\n = ⁴⁄₃ × 22 × 1323\n = ⁴⁄₃ × 29106\n = 116424 ÷ 3 = 38808 cm³\n\nWhy other options are wrong:\n            • (a) 19404 cm³: Result of using formula Area instead of Volume\n            • (c) 55440 cm³: Result of forgetting ⁴⁄₃ in formula Volume\n            • (d) 27720 cm³: Result of error in Calculate cubing",
                                    solution_steps_ar='["Volume of Sphere = ⁴⁄₃ × π × r³","= ⁴⁄₃ × (22 ÷ 7) × 9261","= 116424 ÷ 3 = 38808 cm³"]',
        tags="sphere,volume,3d-shape", stage="mock",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # ── Q148: Cone r=14 =24 Volume (diff=0.6) ── mock
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.6,
                                    text_ar="Cone: Base radius (r) = 14 cm , Height = 24 cm.\nWhat is its volume?\n(π = ²²⁄₇)",
                                    option_a="2464 cm³",             option_b="4928 cm³",             option_c="7392 cm³",             option_d="14784 cm³",
                                    correct_option="b",
                                    explanation_ar="Formula:\n Volume of Cone = ⅓ × π × r² × \n\nSubstitution:\n = ⅓ × (22 ÷ 7) × 14² × 24\n = ⅓ × (22 ÷ 7) × 196 × 24\n = ⅓ × 22 × 28 × 24\n = ⅓ × 14784 = 4928 cm³\n\nWhy other options are wrong:\n            • (a) 2464 cm³: Result of Calculate Area instead of Volume\n            • (c) 7392 cm³: Result of forgetting one of three dimensions\n            • (d) 14784 cm³: Result of using 2D shape formula",
                                    solution_steps_ar='["Volume of Cone = ⅓ × π × r² × ","= ⅓ × (22 ÷ 7) × 196 × 24","= ⅓ × 14784 = 4928 cm³"]',
        tags="cone,volume,3d-shape", stage="mock",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # ── Q149: of Polygon (diff=0.7) ── peak
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.7,
                                    text_ar="Nonagon (9 ).\nHow many Diagonals?",
                                    option_a="18",             option_b="27",             option_c="36",             option_d="45",
                                    correct_option="b",
                                    explanation_ar="Formula:\n        = × ( − 3) ÷ 2\n\nSubstitution:\n = 9 × (9 − 3) ÷ 2\n = 9 × 6 ÷ 2 = 27\n\nWhy other options are wrong:\n            • (a) 18: Result of error Calculation in calculation\n            • (c) 36: Result of incorrectly applying formula\n            • (d) 45: Result of forgetting sides calculation   ",
                                    solution_steps_ar='[" = × ( − 3) ÷ 2","= 9 × 6 ÷ 2 = 27"]',
        tags="diagonal", stage="peak",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # ── Q150: Circle Circumscribed around Square side 10 (diff=0.7) ── mock
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.7,
                                    text_ar="Square side edge = 10 cm.\nWhat is  Circle Circumscribed around Square?",
                                    option_a="5 cm",             option_b="5√2 cm",             option_c="10 cm",             option_d="10√2 cm",
                                    correct_option="b",
                                    explanation_ar=" Diagonal = Side × √2 = 10√2 cm\n\nso Circle Circumference = Radius\n = 10√2 ÷ 2 = 5√2 cm\n\nWhy other options are wrong:\n            • (a) 5 cm: Result of using formula Perimeter instead of Area or vice versa\n            • (c) 10 cm: Result of using Diameter instead of Radius in Formula\n            • (d) 10√2 cm: Result of forgetting squaring Radius when calculating Area",
                                    solution_steps_ar='[" Diagonal = Side × √2 = 10√2 cm","r = 10√2 ÷ 2 = 5√2 cm"]',
        tags="circle,square,diagonal", stage="mock",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # ── Q151: Area Trapezoid (diff=0.7) ── mock
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.7,
                                    text_ar="Trapezoid: Large base = 18 cm , Small base = 12 cm , Height = 8 cm.\nWhat is its area?",
                                    option_a="96 cm²",             option_b="120 cm²",             option_c="144 cm²",             option_d="240 cm²",
                                    correct_option="b",
                                    explanation_ar="Formula:\n        Area Trapezoid = ½ × (Base₁ + Base₂) × Height\n\nSubstitution:\n = ½ × (18 + 12) × 8\n = ½ × 30 × 8 = 120 cm²\n\nWhy other options are wrong:\n            • (b) 308 cm²: Result of using formula Perimeter instead of Area\n            • (c) 144 cm²: Result of forgetting sides in Calculate Area\n            • (d) 240 cm²: Result of error in Calculate",
                                    solution_steps_ar='["Area = ½ × (Base₁ + Base₂) × Height","= ½ × (18 + 12) × 8","= ½ × 30 × 8 = 120 cm²"]',
        tags="trapezoid,area", stage="mock",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # ── Q152: Circle of Square side 14 (diff=0.7) ── mock
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.7,
                                    text_ar="A square has side length 14 cm.\nA circle is inscribed inside the square.\nWhat is the area of the circle?\n(π = 22/7)",
                                    option_a="154 cm²",             option_b="308 cm²",             option_c="616 cm²",             option_d="44 cm²",
                                    correct_option="a",
                                    explanation_ar="r = Square ÷ 2 = 14 ÷ 2 = 7 cm\n\nArea of Circle = π × r²\n = (22 ÷ 7) × 7² = (22 ÷ 7) × 49 = 154 cm²\n\nWhy other options are wrong:\n            • (a) 770 cm²: Result of using formula Perimeter instead of Area or vice versa\n            • (c) 616 cm²: Result of using Diameter instead of Radius in Formula\n            • (d) 44 cm²: Result of forgetting squaring Radius when calculating Area",
                                    solution_steps_ar='["r = 14 ÷ 2 = 7 cm","Area = π × r² = (22 ÷ 7) × 49","= 22 × 7 = 154 cm²"]',
        tags="circle,square,area", stage="mock",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # ── Q153: Cone Total surface area r=14 =21 (diff=0.7) ── peak
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.7,
                                    text_ar="Cone: Base radius (r) = 14 cm , Slant height () = 21 cm.\nWhat is its area?\n(π = ²²⁄₇)",
                                    option_a="770 cm²",             option_b="1540 cm²",             option_c="2156 cm²",             option_d="1078 cm²",
                                    correct_option="b",
                                    explanation_ar="Total surface area = π × r × ( + r)\n = (22 ÷ 7) × 14 × (21 + 14)\n = (22 ÷ 7) × 14 × 35\n = 22 × 2 × 35\n = 22 × 70 = 1540 cm²\n\nWhy other options are wrong:\n            • (a) 770 cm²: Result of using formula Perimeter instead of Area\n            • (b) 480 cm³: Result of forgetting sides in Calculate Area\n            • (d) 1078 cm²: Result of error in Calculate",
                                    solution_steps_ar='["Total surface area = π × r × ( + r)","= (22 ÷ 7) × 14 × 35","= 22 × 70 = 1540 cm²"]',
        tags="cone,area,3d-shape", stage="peak",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # ── Q154:Similarity 3:4 Volume (diff=0.7) ── mock
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.7,
                                    text_ar="Similar Similar: Similarity ratio = 3 : 4.\nIf Volume = 270 cm³, Volume ?",
                                    option_a="360 cm³",             option_b="480 cm³",             option_c="640 cm³",             option_d="1080 cm³",
                                    correct_option="c",
                                    explanation_ar="Volume ratio = Cube of similarity ratio\n = (3/4)³ = 27/64\n\n270 ÷ Volume₂ = 27 ÷ 64\nVolume₂ = 270 × 64 ÷ 27 = 10 × 64 = 640 cm³\n\nWhy other options are wrong:\n            • (b) 480 cm³: Result of Calculate Area instead of Volume\n            • (c) 5 cm: Result of forgetting one of three dimensions\n            • (d) 1080 cm³: Result of using 2D shape formula",
                                    solution_steps_ar='["Volume ratio = (3/4)³ = 27/64","270 ÷ Volume₂ = 27 ÷ 64","Volume₂ = 270 × 64 ÷ 27 = 640 cm³"]',
        tags="volume,3d-shape", stage="mock",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # ── Q155: Isosceles trapezoid 20 and 12 5 (diff=0.7) ── mock
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.7,
                                    text_ar="Isosceles trapezoid: Large base = 20 cm , Small base = 12 cm , Leg = 5 cm.\nWhat is its height?",
                                    option_a="3 cm",             option_b="4 cm",             option_c="5 cm",             option_d="6 cm",
                                    correct_option="a",
                                    explanation_ar="Difference between bases = 20 − 12 = 8 cm\nHalf the difference = 4 cm ( )\n\nusing Pythagorean:\n Height² = Leg² − 4²\n = 5² − 4² = 25 − 16 = 9\n Height = 3 cm\n\nWhy other options are wrong:\n            • (a) 4 cm: Result of adding Sides instead of using Pythagorean Theorem\n            • (c) 5 cm: Result of forgetting squaring adding Square\n            • (d) 6 cm: Result of confusing Square Hypotenuse and Square Side of Right",
                                    solution_steps_ar='["Half the difference = (20 − 12) ÷ 2 = 4 cm","Height² = 5² − 4² = 25 − 16 = 9","Height = 3 cm"]',
        tags="trapezoid,pythagorean", stage="mock",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # ── Q156: Regular hexagon side 8 r Circle Circumference (diff=0.7) ── peak
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.7,
                                    text_ar="Regular hexagon: side edge = 8 cm.\nWhat is  Circle Circumference of it?",
                                    option_a="4 cm",             option_b="8 cm",             option_c="8√3 cm",             option_d="16 cm",
                                    correct_option="b",
                                    explanation_ar="In regular hexagon: Circle Circumference = edge Side.\n\n r = 8 cm\n\nWhy other options are wrong:\n            • (a) 4 cm: Result of using formula Perimeter instead of Area or vice versa\n            • (c) 8√3 cm: Result of using Diameter instead of Radius in Formula\n            • (d) 16 cm: Result of forgetting squaring Radius when calculating Area",
                                    solution_steps_ar='["In regular hexagon: r Circle Circumference = Side","r = 8 cm"]',
        tags="circle,area", stage="peak",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # ── Q157: Rhombus side 13 24 (diff=0.7) ── mock
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.7,
                                    text_ar="Rhombus: side edge = 13 cm , = 24 cm.\nWhat is length of Diameter ?",
                                    option_a="5 cm",             option_b="10 cm",             option_c="12 cm",             option_d="20 cm",
                                    correct_option="b",
                                    explanation_ar=" Rhombus intersect and bisect at Right angle.\n Radius₁ = 12 cm\n\nusing Pythagorean:\n Radius₂² = 13² − 12² = 169 − 144 = 25\n Radius₂ = 5 cm\n Diameter₂ = 10 cm\n\nWhy other options are wrong:\n            • (a) 5 cm: Result of adding Sides instead of using Pythagorean Theorem\n            • (c) 12 cm: Result of forgetting squaring adding Square\n            • (d) 20 cm: Result of confusing Square Hypotenuse and Square Side of Right",
                                    solution_steps_ar='["Radius₁ = 24 ÷ 2 = 12 cm","Radius₂² = 13² − 12² = 25","Radius₂ = 5 → Diameter₂ = 10 cm"]',
        tags="rhombus,diagonal,pythagorean", stage="mock",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # ── Q158: Sphere Surface area 2464 r (diff=0.7) ── mock
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.7,
                                    text_ar="Sphere: Surface area = 2464 cm².\nWhat is its radius?\n(π = ²²⁄₇)",
                                    option_a="7 cm",             option_b="14 cm",             option_c="21 cm",             option_d="28 cm",
                                    correct_option="b",
                                    explanation_ar="Formula:\nSurface Area of Sphere = 4 × π × r²\n2464 = 4 × (22/7) × r²\n2464 = (88/7) × r²\nr² = 2464 × 7 / 88 = 17248 / 88 = 196\nr = sqrt(196) = 14 cm\n\nWhy other options are wrong:\n• (a) 7 cm: Used r instead of r² in the formula\n• (c) 21 cm: Arithmetic error in the division step\n• (d) 28 cm: Calculated diameter (2r) instead of radius",
                                    solution_steps_ar='["4 × π × r² = 2464","r² = 2464 × 7 ÷ 88 = 196","r = √196 = 14 cm"]',
        tags="sphere,area,3d-shape", stage="mock",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # ── Q159: Composite shape: Triangle + Semicircle (diff=0.8) ── building
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.8,
                                    text_ar=" : Equilateral triangle side = 14 cm, and Semicircle = 14 cm.\nWhat is Total surface area?\n(π = ²²⁄₇)",
                                    option_a="49√3 + 77 cm²",             option_b="49√3 + 154 cm²",             option_c="98√3 + 77 cm²",             option_d="49√3 + 308 cm²",
                                    correct_option="a",
                                    explanation_ar="Area of Triangle = (√3 ÷ 4) × 14² = (√3 ÷ 4) × 196 = 49√3 cm²\n\nArea of Circle = ½ × π × r²\n r = 7 cm\n = ½ × (22 ÷ 7) × 49 = ½ × 154 = 77 cm²\n\nSum = 49√3 + 77 cm²\n\nWhy other options are wrong:\n            • (a) 12 cm: Result of forgetting division by 2 in formula Area of Triangle\n            • (b) 49√3 + 154 cm²: Result of using formula Rectangle without division by 2\n            • (d) 49√3 + 308 cm²: Result of adding Base and Height instead of multiplying them",
                                    solution_steps_ar='["Area of Triangle = (√3 ÷ 4) × 196 = 49√3 cm²"," Circle = ½ × π × 7² = 77 cm²","sum = 49√3 + 77 cm²"]',
        tags="triangle,circle,composite,area", stage="building",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # ── Q160: Cone Volume of 1232 r=7 Height (diff=0.8) ── building
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.8,
                                    text_ar="Cone: Volume of = 1232 cm³ ,        (r) = 7 cm.\nWhat is its height?\n(π = ²²⁄₇)",
                                    option_a="12 cm",             option_b="18 cm",             option_c="24 cm",             option_d="30 cm",
                                    correct_option="c",
                                    explanation_ar="Formula:\n Volume = ⅓ × π × r² × \n 1232 = ⅓ × (22 ÷ 7) × 49 × \n 1232 = ⅓ × 22 × 7 × \n 1232 = (154 ÷ 3) × \n = 1232 × 3 ÷ 154 = 3696 ÷ 154 = 24 cm\n\nWhy other options are wrong:\n            • (a) 12 cm: Result of Calculate Area instead of Volume\n            • (c) 3 cm: Result of forgetting one of three dimensions\n            • (d) 30 cm: Result of using 2D shape formula",
                                    solution_steps_ar='["⅓ × π × r² × = 1232","⅓ × (22 ÷ 7) × 49 × = 1232"," = 1232 × 3 ÷ 154 = 24 cm"]',
        tags="cone,volume,3d-shape", stage="building",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # ── Q161: Circle inscribed in Triangle Right 6-8-10 (diff=0.8) ── building
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.8,
                                    text_ar="Right triangle: 6 cm and 8 cm and 10 cm.\nWhat is  Circle()?",
                                    option_a="1 cm",             option_b="2 cm",             option_c="3 cm",             option_d="4 cm",
                                    correct_option="b",
                                    explanation_ar="Formula of Right Triangle:\n r = (Side₁ + Side₂ − Hypotenuse) ÷ 2\n\nSubstitution:\n r = (6 + 8 − 10) ÷ 2 = 4 ÷ 2 = 2 cm\n\nWhy other options are wrong:\n            • (a) 1 cm: Result of using formula Perimeter instead of Area or vice versa\n            • (b) 9 cm: Result of using Diameter instead of Radius in Formula\n            • (d) 4 cm: Result of forgetting squaring Radius when calculating Area",
                                    solution_steps_ar='["r Circle = (Side₁ + Side₂ − Hypotenuse) ÷ 2","= (6 + 8 − 10) ÷ 2","= 4 ÷ 2 = 2 cm"]',
        tags="circle,triangle,pythagorean", stage="building",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # ── Q162: Rectangular prism 13 and (diff=0.8) ── building
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.8,
                                    text_ar="Rectangular prism: 4 cm and 6 cm andrdcm.\nIf Space diagonal = 13 cm, What is value ?",
                                    option_a="7 cm",             option_b="9 cm",             option_c="11 cm",             option_d="15 cm",
                                    correct_option="c",
                                    explanation_ar="Space diagonal² = Length² + Width² + Height²\n 13² = 4² + 6² + ²\n 169 = 16 + 36 + ²\n ² = 169 − 52 = 117\n\nso √117 ≈ 108 ≈ 11 cm\n\nNote: 13² = 4² + 6² + ²\n ² = 117 → ≈ 11 cm\n\nWhy other options are wrong:\n            • (a) 7 cm: Result of Calculate Area instead of Volume\n            • (c) 308 cm²: Result of forgetting one dimension\n            • (d) 15 cm: Result of using 2D shape formula",
                                    solution_steps_ar='["13² = 4² + 6² + ²","169 = 16 + 36 + ²","² = 117 → ≈ 11 cm"]',
        tags="3d-shape,diagonal", stage="building",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # ── Q163: Area Circular sector r=21 Angle=120 (diff=0.8) ── building
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.8,
                                    text_ar="Circular sector: Radius (r) = 21 cm , Central angle = 120°.\nWhat is its area?\n(π = ²²⁄₇)",
                                    option_a="154 cm²",             option_b="462 cm²",             option_c="308 cm²",             option_d="616 cm²",
                                    correct_option="b",
                                    explanation_ar="Formula:\n        Area = (Angle ÷ 360) × π × r²\n\nSubstitution:\n = (120 ÷ 360) × (22 ÷ 7) × 21²\n = ⅓ × (22 ÷ 7) × 441\n = ⅓ × 22 × 63\n = ⅓ × 1386 = 462 cm²\n\nWhy other options are wrong:\n            • (b) 176 cm²: Result of using formula Perimeter instead of Area or vice versa\n            • (c) 308 cm²: Result of using Diameter instead of Radius in Formula\n            • (d) 616 cm²: Result of forgetting squaring Radius when calculating Area",
                                    solution_steps_ar='["Area = (Angle ÷ 360) × π × r²","= ⅓ × (22 ÷ 7) × 441","= ⅓ × 1386 = 462 cm²"]',
        tags="circle,sector,area", stage="building",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # ── Q164: Composite shape: Square − Circle side=28 (diff=0.8) ── building
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.8,
                                    text_ar="Square side edge = 28 cm.\ndrawn inscribed in it 4regions (Quarter circle inside Square with 14 cm).\nWhat is uncovered area of Square?\n(π = ²²⁄₇)",
                                    option_a="168 cm²",             option_b="176 cm²",             option_c="308 cm²",             option_d="784 cm²",
                                    correct_option="a",
                                    explanation_ar="Area of Square = 28² = 784 cm²\n\nArea of 4 quarter circles = full circle with r = 14\n = π × 14² = (22 ÷ 7) × 196 = 616 cm²\n\nUncovered = 784 − 616 = 168 cm²\n\nWhy other options are wrong:\n            • (b) 176 cm²: Result of using π ≈ 3.1 instead of 22/7, giving approximate circle area of 608\n            • (c) 308 cm²: Result of subtracting only half the circle area (616 ÷ 2 = 308) from 784 − 308 is wrong\n            • (d) 784 cm²: This is just the square area without subtracting the circles",
                                    solution_steps_ar='["Area of Diagonal = 28² = 784 cm²","Area of 4 regions = π × 14² = 616 cm²"," = 784 − 616 = 168 cm²"]',
        tags="square,circle,composite,area", stage="building",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # ── Q165: rπ (diff=0.4) ── building
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.4,
                                    text_ar=" distance from Circle center to cm Circle in and .\nIf = 24 cm and = 25 cm.\nWhat is  Circle?",
                                    option_a="5 cm",             option_b="7 cm",             option_c="12 cm",             option_d="13 cm",
                                    correct_option="b",
                                    explanation_ar=" ⊥ Radius.\n ² = ² − ²\n = 25² − 24²\n = 625 − 576 = 49\n = √49 = 7 cm\n\nWhy other options are wrong:\n            • (a) 5 cm: Result of using formula Perimeter instead of Area or vice versa\n            • (b) 10: Result of using Diameter instead of Radius in Formula\n            • (d) 13 cm: Result of forgetting squaring Radius when calculating Area",
                                    solution_steps_ar='["² = ² − ²","= 625 − 576 = 49"," = 7 cm"]',
        tags="circle,pythagorean", stage="building",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

                # ── Q166: Polygon interior 150° (diff=0.4) ── building
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.4,
                                    text_ar="Polygon : Measure of each angle in it = 150°.\nHow many ?",
                                    option_a="8",             option_b="10",             option_c="12",             option_d="15",
                                    correct_option="c",
                                    explanation_ar="Formula:\n Interior angle = ( − 2) × 180 ÷ \n 150 = ( − 2) × 180 ÷ \n 150 = 180 − 360\n 30 = 360\n = 12\n\nWhy other options are wrong:\n            • (a) 8: Result of confusing sum (90°) sum (180°)\n            • (c) 4 cm: Result of using wrong angle sum for shape\n            • (d) 15: Result of forgetting to subtract given angles",
                                    solution_steps_ar='["150 = ( − 2) × 180 ÷ ","150 = 180 − 360","30 = 360 → = 12"]',
        tags="angle", stage="building",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

                # ── Q167: Sphere Volume of 36 r (diff=0.5) ── building
                Question(skill_id="quant_geometry", question_type="geometry", difficulty=0.5,
                                    text_ar="Sphere: Volume of = 36 cm³.\nWhat is its radius?",
                                    option_a="2 cm",             option_b="3 cm",             option_c="4 cm",             option_d="6 cm",
                                    correct_option="b",
                                    explanation_ar="Formula:\n Volume of Sphere = ⁴⁄₃ × π × r³\n 36π = ⁴⁄₃ × π × r³\n 36 = ⁴⁄₃ × r³\n r³ = 36 × 3 ÷ 4 = 108 ÷ 4 = 27\n r = ³√27 = 3 cm\n\nWhy other options are wrong:\n            • (a) 2 cm: Result of using formula Area instead of Volume\n            • (c) 4 cm: Result of forgetting ⁴⁄₃ in formula Volume\n            • (d) 6 cm: Result of error in Calculate cubing",
                                    solution_steps_ar='["⁴⁄₃ × π × r³ = 36","r³ = 36 × 3 ÷ 4 = 27","r = ³√27 = 3 cm"]',
        tags="sphere,volume,3d-shape", stage="peak",
        rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),
        ]
