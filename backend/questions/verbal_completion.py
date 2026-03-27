from models import Question

def get_questions():
    return [

        # ══════════════════════════════════════════════════════════════
        # EXISTING 20 QUESTIONS (from seed.py)
        # ══════════════════════════════════════════════════════════════

        # --- Existing Q1 (difficulty 0.3) ---
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.3,
            text_ar="Water is essential for the _____ of all living organisms.",
            option_a="extinction", option_b="life", option_c="destruction", option_d="weakening",
            correct_option="b",
            explanation_ar="The context is positive (essential) so the appropriate word is also positive. Water is essential for the life of all organisms. Why the other options are wrong: (a) extinction is negative, contradicts essential which indicates positive importance. (c) destruction is negative and it is illogical for water to be essential for destruction. (d) weakening is negative, contradicts the context that links water with life.",
            solution_steps_ar='["Identify the clue: essential means positive context","Search for a positive word among the options","life is the only positive word so option (b)"]',
            tags="definition", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- Existing Q2 (difficulty 0.5) ---
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.5,
            text_ar="The successful scientist is characterized by patience and _____ in seeking the truth.",
            option_a="haste", option_b="neglect", option_c="perseverance", option_d="retreat",
            correct_option="c",
            explanation_ar="Context clue: patience is a positive characteristic. The complementary word must also be positive so perseverance.",
            solution_steps_ar='["Identify the clue: patience means positive characteristic","The coordinating conjunction requires a word similar in meaning","perseverance is a positive characteristic so option (c)"]',
            tags="tone-matching", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- Existing Q3 (difficulty 0.6) ---
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.6,
            text_ar="The more a person's _____ in reading increases, the broader their thinking horizons become.",
            option_a="distance", option_b="interest", option_c="preoccupation", option_d="boredom",
            correct_option="b",
            explanation_ar="Positive proportional relationship: increase in something leads to expansion of thinking. Interest is the positive word that produces this result.",
            solution_steps_ar='["Identify the relationship: the more X increases the broader thinking becomes","The relationship is positive and proportional","interest is the appropriate positive word so option (b)"]',
            tags="cause-effect", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- Existing Q4 (difficulty 0.2) ---
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.2,
            text_ar="The sun rises from the _____ and sets in the west.",
            option_a="north", option_b="south", option_c="east", option_d="west",
            correct_option="c",
            explanation_ar="Clue of contrast in the sentence: sets in the west so the opposite direction is the east. Why the other options are wrong: (a) north does not oppose west in the context of sunrise and sunset. (b) south does not oppose west in this context. (d) west produces repetition rises from the west and sets in the west which is scientifically and linguistically wrong.",
            solution_steps_ar='["Identify the clue: sets in the west","Use logical contrast: sunrise opposes sunset","east opposes west so The sun rises from the east so option (c)"]',
            tags="definition", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # --- Existing Q5 (difficulty 0.2) ---
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.2,
            text_ar="The student must study hard because the _____ requires good preparation.",
            option_a="play", option_b="sleep", option_c="exam", option_d="food",
            correct_option="c",
            explanation_ar="The context talks about studying and preparation, and the thing that requires academic preparation is the exam. Why the other options are wrong: (a) play is not related to studying or academic preparation. (b) sleep does not require hard studying. (d) food has no relation to academic preparation context.",
            solution_steps_ar='["Identify the context: studying plus preparation","Search for the word related to studying","the exam is what requires studying and preparation so option (c)"]',
            tags="cause-effect", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # --- Existing Q6 (difficulty 0.3) ---
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.3,
            text_ar="Despite the _____ of the weather, the farmers went out to their fields to harvest the crop.",
            option_a="moderation", option_b="beauty", option_c="harshness", option_d="warmth",
            correct_option="c",
            explanation_ar="Clue of despite indicates contrast: The weather was bad but they went out despite that. The appropriate word is harshness which is a negative characteristic contrasting with the action of going out.",
            solution_steps_ar='["Identify the conjunction: despite means contrast","The action is positive: they went out to harvest","The word must be negative: harshness of weather so option (c)"]',
            tags="contrast", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # --- Existing Q7 (difficulty 0.5) ---
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.5,
            text_ar="One cannot judge a person by their _____ but must get to know their essence and morals.",
            option_a="actions", option_b="appearance", option_c="words", option_d="mind",
            correct_option="b",
            explanation_ar="Contrast clue: but must get to know their essence means Essence is contrasted with appearance. Meaning: Do not judge by appearance but by essence.",
            solution_steps_ar='["Identify the conjunction: but means contrast and correction","Second part: their essence and morals means inner self","First part must be outer: appearance so option (b)"]',
            tags="contrast", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- Existing Q8 (difficulty 0.5) ---
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.5,
            text_ar="The population increased significantly, which led to a _____ in demand for housing.",
            option_a="decrease", option_b="stability", option_c="rise", option_d="decline",
            correct_option="c",
            explanation_ar="Proportional relationship: population increase leads to increase in housing demand. Clue which led to connects cause with logical result.",
            solution_steps_ar='["Identify the relationship: cause is population increase leads to result","Determine direction: proportional so increase leads to increase","rise in demand is the logical result so option (c)"]',
            tags="cause-effect", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- Existing Q9 (difficulty 0.6) ---
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.6,
            text_ar="The philosopher believes that true happiness lies in _____ not in possessing material things.",
            option_a="material wealth", option_b="accumulating money", option_c="peace of mind", option_d="buying possessions",
            correct_option="c",
            explanation_ar="Clue not in possessing material things means The required word must be spiritual, not material. Peace of mind is the only spiritual value among the options.",
            solution_steps_ar='["Identify the clue: not in possessing material things means negation","The required word opposes material: something spiritual","Examine options: peace of mind is the only spiritual one so option (c)"]',
            tags="contrast", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- Existing Q10 (difficulty 0.7) ---
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.7,
            text_ar="The speaker was _____ in presenting his ideas, leaving no room for doubt or ambiguity among the audience.",
            option_a="ambiguous", option_b="hesitant", option_c="clear", option_d="vague",
            correct_option="c",
            explanation_ar="Result clue: left no room for doubt or ambiguity means The cause must be the opposite of ambiguity. The appropriate characteristic is clear.",
            solution_steps_ar='["Identify the clue: left no room for doubt or ambiguity","Relationship: cause leads to result where the characteristic led to no ambiguity","The appropriate characteristic is opposite of ambiguity: clear so option (c)"]',
            tags="contrast", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # --- Existing Q11 (difficulty 0.8) ---
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.8,
            text_ar="While some see globalization as _____ local cultures, others emphasize that it enriches civilizational diversity through knowledge exchange.",
            option_a="enhancing", option_b="enriching", option_c="threatening", option_d="protecting",
            correct_option="c",
            explanation_ar="Clue while indicates contrast between two views: Second view is enriching diversity which is positive. First view must be negative: threatening local cultures.",
            solution_steps_ar='["Identify the conjunction: while means contrast between two views","Second view is positive: enriches civilizational diversity","First view must be negative: threatening so option (c)"]',
            tags="definition", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # --- Existing Q12 (difficulty 0.8) ---
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.8,
            text_ar="The progress of societies is measured not only by their technical advancement but also by their social cohesion and ability to achieve justice.",
            option_a="backwardness", option_b="progress", option_c="collapse", option_d="weakness",
            correct_option="b",
            explanation_ar="The context discusses positive criteria like technical advancement plus social cohesion plus justice. The measured word must be positive: progress of societies.",
            solution_steps_ar='["Identify the context: positive criteria like advancement, cohesion, and justice","The required word is what is measured by these criteria","progress is a positive word measured by advancement, cohesion, and justice so option (b)"]',
            tags="contrast", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # --- Existing Q13 (difficulty 0.2) ---
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.2,
            text_ar="After the storm ended, the sky _____ and the sun appeared again.",
            option_a="darkened", option_b="cleared", option_c="intensified", option_d="clouded over",
            correct_option="b",
            explanation_ar="Temporal clue after the storm ended indicates weather improvement. Cleared means became clear which is consistent with the appearance of the sun.",
            solution_steps_ar='["Clue: after the storm ended means improvement","Result: sun appeared means sky became clear","Appropriate word: cleared so option (b)"]',
            tags="cause-effect", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # --- Existing Q14 (difficulty 0.25 rounded to 0.3) ---
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.25,
            text_ar="Before the exam began, the student _____ a quick review of the main points.",
            option_a="neglected", option_b="ignored", option_c="conducted", option_d="left",
            correct_option="c",
            explanation_ar="Temporal clue before the exam indicates a preparatory action. Conducted a review is the correct and contextually appropriate phrasing.",
            solution_steps_ar='["Temporal clue: before the exam means preparatory action","Object: quick review requires a positive action","conducted a review is proper idiomatic expression so option (c)"]',
            tags="contrast", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # --- Existing Q15 (difficulty 0.3) ---
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.3,
            text_ar="If you plan your project well, your chances of _____ will be greater.",
            option_a="failure", option_b="success", option_c="retreat", option_d="loss",
            correct_option="b",
            explanation_ar="Conditional clue if you do well is positive, and the result must be positive. Success is the natural result of good planning.",
            solution_steps_ar='["Conditional clue: if you do well means positive result","chances plus positive word means success","option (b) is the only positive one"]',
            tags="cause-effect", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # --- Existing Q16 (difficulty 0.45) ---
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.45,
            text_ar="Despite the many difficulties he faced, he _____ in achieving his dream of graduating from university.",
            option_a="failed", option_b="hesitated", option_c="succeeded", option_d="withdrew",
            correct_option="c",
            explanation_ar="The conjunction despite indicates concession: difficulties did not stop him. Expected result after despite plus negative equals positive so succeeded.",
            solution_steps_ar='["Identify the conjunction: despite means concession which is opposite of expected","Premise is negative (difficulties) so result is positive","succeeded in achieving his dream so option (c)"]',
            tags="contrast", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- Existing Q17 (difficulty 0.5) ---
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.5,
            text_ar="Despite the _____ of available resources, the team was able to complete the project on time.",
            option_a="abundance", option_b="plenty", option_c="scarcity", option_d="variety",
            correct_option="c",
            explanation_ar="Despite indicates contrast: The team succeeded despite an obstacle. Logical obstacle equals scarcity of resources meaning fewness.",
            solution_steps_ar='["Conjunction: despite means contrast between two clauses","Second clause is positive (project completion)","First clause must be negative: scarcity of resources so option (c)"]',
            tags="contrast", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- Existing Q18 (difficulty 0.55) ---
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.55,
            text_ar="If the student had _____ his lessons well, he would not have failed the final exam.",
            option_a="neglected", option_b="ignored", option_c="prepared", option_d="forgotten",
            correct_option="c",
            explanation_ar="If counterfactual conditional: The action did not happen so the negative result (failure) occurred. Meaning: if he had prepared then he would not have failed. That is, he did not prepare so he failed.",
            solution_steps_ar='["Analyze counterfactual if: the action did not occur","Result: failed so he did not prepare","Blank needs positive action that did not occur: prepared so option (c)"]',
            tags="definition", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- Existing Q19 (difficulty 0.75) ---
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.75,
            text_ar="After the negotiations between the two parties _____ for weeks, they finally reached an agreement that satisfies both sides.",
            option_a="succeeded", option_b="stalled", option_c="ended", option_d="began",
            correct_option="b",
            explanation_ar="Temporal clue after...for weeks plus finally indicates difficulty preceded the result. Stalled reflects this difficulty before reaching the agreement.",
            solution_steps_ar='["Word finally indicates reaching the agreement came after hardship","For weeks indicates long duration due to an obstacle","stalled means faced difficulties which is consistent with context so option (b)"]',
            tags="contrast", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- Existing Q20 (difficulty 0.8) ---
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.8,
            text_ar="Although scientific evidence clearly _____ to the dangers of smoking, many people still practice this habit.",
            option_a="doubts", option_b="points", option_c="denies", option_d="ignores",
            correct_option="b",
            explanation_ar="Although is concessive: The evidence is clear but people do not respond. Evidence points clearly to the danger but behavior did not change.",
            solution_steps_ar='["Although means concession: fact but contrary behavior","Evidence plus clearly plus dangers of smoking needs verb indicating proof","points clearly is proper idiomatic expression so option (b)"]',
            tags="contrast", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),


        # ══════════════════════════════════════════════════════════════
        # NEW 91 QUESTIONS (Q21-Q111)
        # ══════════════════════════════════════════════════════════════

        # Q21 - definition
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.2,
            text_ar="The doctor is the person who _____ patients and treats them.",
            option_a="neglects", option_b="examines", option_c="punishes", option_d="avoids",
            correct_option="b",
            explanation_ar="Definition clue: The doctor's profession is examining patients and treating them. Examines is the word that defines the doctor's work.",
            solution_steps_ar='["Type of clue: definition means the doctor is the person who...","The verb must describe the doctor profession","examines patients is appropriate verb so option (b)"]',
            tags="definition", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # Q22 - tone matching
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.2,
            text_ar="The mother loves her children and cares for their _____.",
            option_a="harm", option_b="abuse", option_c="care", option_d="neglect",
            correct_option="c",
            explanation_ar="Tone matching clue: loves plus cares means The word must be positive. Care matches love and attention.",
            solution_steps_ar='["Tone is positive: loves plus cares","The required word must be positive","care is the only positive option so option (c)"]',
            tags="tone-matching", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # Q23 - cause/effect
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.2,
            text_ar="The student cleaned his room because it was _____.",
            option_a="organized", option_b="clean", option_c="messy", option_d="beautiful",
            correct_option="c",
            explanation_ar="Cause and effect clue: because explains the reason for cleaning. The logical reason for cleaning is that the room was messy.",
            solution_steps_ar='["Identify the conjunction: because means cause and effect","Action: cleaned means reason must be opposite of cleanliness","messy is the logical reason for cleaning so option (c)"]',
            tags="contrast", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # Q24 - temporal
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.2,
            text_ar="When the rain fell, the children _____ inside the house.",
            option_a="went out", option_b="entered", option_c="played", option_d="slept",
            correct_option="b",
            explanation_ar="Temporal clue when the rain fell means natural reaction is entering. Entered the children into the house to escape the rain.",
            solution_steps_ar='["Temporal clue: when the rain fell","Direction: inside the house needs entering verb","the children entered inside the house so option (b)"]',
            tags="temporal", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # Q25 - definition
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.2,
            text_ar="The teacher teaches students and helps them to _____ knowledge.",
            option_a="forget", option_b="acquire", option_c="reject", option_d="avoid",
            correct_option="b",
            explanation_ar="Definition clue: The teacher teaches and helps means context is positive educational. Acquiring knowledge is the goal of education.",
            solution_steps_ar='["Type of clue: definition of teacher profession","Context is positive: teaches plus helps","acquiring knowledge is natural goal so option (b)"]',
            tags="definition", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # Q26 - tone matching
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.2,
            text_ar="The garden is beautiful and full of flowers with _____ colors.",
            option_a="pale", option_b="withered", option_c="vibrant", option_d="dark",
            correct_option="c",
            explanation_ar="Positive tone matching clue: beautiful plus full of flowers. Vibrant describes cheerful colors matching the garden's beauty.",
            solution_steps_ar='["Tone is positive: beautiful plus full of flowers","Color description must be positive","vibrant colors so option (c)"]',
            tags="contrast", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # Q27 - example
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.2,
            text_ar="Means of transportation are varied, including the car, _____, and the airplane.",
            option_a="the book", option_b="the train", option_c="the pen", option_d="the chair",
            correct_option="b",
            explanation_ar="Example clue: The context lists means of transportation. Car and airplane are means of transportation so train is also a means of transportation.",
            solution_steps_ar='["Type of clue: examples of means of transportation","Car and airplane are means of transportation","train is the only means of transportation among options so option (b)"]',
            tags="definition", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # Q28 - contrast
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.3,
            text_ar="The road was not _____ but was rough and full of potholes.",
            option_a="difficult", option_b="rough", option_c="paved", option_d="dangerous",
            correct_option="c",
            explanation_ar="Contrast clue: but connects two opposite characteristics. Second part: rough means First part must be its opposite: paved.",
            solution_steps_ar='["Identify the conjunction: but means contrast","Second part: rough (negative)","First part must be positive: paved so option (c)"]',
            tags="contrast", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # Q29 - cause/effect
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.3,
            text_ar="The student reviewed extensively, so he _____ the exam with excellence.",
            option_a="failed", option_b="was absent", option_c="succeeded", option_d="withdrew",
            correct_option="c",
            explanation_ar="Cause and effect clue: so connects cause with result. Cause: extensive review means Logical result: success with excellence.",
            solution_steps_ar='["Identify the conjunction: so means cause and effect","Cause is positive: reviewed extensively","Result must be positive: succeeded with excellence so option (c)"]',
            tags="cause-effect", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q30 - temporal
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.3,
            text_ar="Before traveling, he _____ his bag carefully and checked all his belongings.",
            option_a="emptied", option_b="neglected", option_c="prepared", option_d="lost",
            correct_option="c",
            explanation_ar="Temporal clue before traveling indicates a preparatory action. Prepared his bag is the logical action before travel.",
            solution_steps_ar='["Temporal clue: before traveling means preparation","Action related to bag plus carefully","prepared his bag is preparatory action so option (c)"]',
            tags="contrast", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q31 - definition
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.3,
            text_ar="The library is a place that contains thousands of _____ and is frequented by researchers and readers.",
            option_a="games", option_b="foods", option_c="books", option_d="clothes",
            correct_option="c",
            explanation_ar="Definition clue: The library is a place means What the place contains defines its identity. The library contains books by definition.",
            solution_steps_ar='["Type of clue: definition means library is a place that contains...","Library is associated with books and reading","books are what the library contains so option (c)"]',
            tags="definition", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q32 - tone matching (negative)
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.3,
            text_ar="The general atmosphere in the city was _____ after the destructive earthquake that struck it.",
            option_a="joyful", option_b="celebratory", option_c="somber", option_d="cheerful",
            correct_option="c",
            explanation_ar="Negative tone matching clue: destructive earthquake means Atmosphere must be negative. Somber matches disaster atmospheres.",
            solution_steps_ar='["Tone is negative: destructive earthquake","General atmosphere must reflect the disaster","somber is appropriate negative description so option (c)"]',
            tags="contrast", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q33 - cause/effect
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.3,
            text_ar="The engine suddenly stopped because the car _____ fuel.",
            option_a="filled up with", option_b="ran out of", option_c="increased", option_d="overflowed with",
            correct_option="b",
            explanation_ar="Cause and effect clue: because explains the reason for engine stopping. Logical reason: running out of fuel means engine stops.",
            solution_steps_ar='["Conjunction: because means cause and effect","Result: engine stopped (negative)","Logical reason: ran out of fuel so option (b)"]',
            tags="cause-effect", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q34 - contrast
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.3,
            text_ar="He thought the problem was _____ but discovered it was extremely complex.",
            option_a="difficult", option_b="complicated", option_c="easy", option_d="impossible",
            correct_option="c",
            explanation_ar="Contrast clue: but connects assumption with opposite discovery. Discovered it is complex means He thought it was easy.",
            solution_steps_ar='["Conjunction: but means contrast","Discovery: extremely complex (difficult)","Assumption must be the opposite: easy so option (c)"]',
            tags="contrast", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q35 - example/illustration
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.3,
            text_ar="Among fruits rich in vitamin C: orange, _____, and guava.",
            option_a="rice", option_b="lemon", option_c="meat", option_d="bread",
            correct_option="b",
            explanation_ar="Example clue: The context lists fruits rich in vitamin C. Orange and guava are acidic fruits so lemon is also an acidic fruit.",
            solution_steps_ar='["Type of clue: examples of fruits rich in vitamin C","Orange and guava are fruits","lemon is the only fruit among options so option (b)"]',
            tags="definition", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q36 - tone matching
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.3,
            text_ar="The team celebrated the victory and _____ of joy appeared on the players' faces.",
            option_a="appeared", option_b="disappeared", option_c="were absent", option_d="faded",
            correct_option="a",
            explanation_ar="Positive tone matching clue: celebrated plus victory plus joy. Appeared means manifested on faces which is consistent with celebration.",
            solution_steps_ar='["Tone is positive: celebrated plus victory","Joy must be visible (positive)","joy appeared so option (a)"]',
            tags="tone-matching", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q37 - cause/effect
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.3,
            text_ar="He overindulged in eating sweets, which led to a noticeable _____ in his weight.",
            option_a="decrease", option_b="stability", option_c="increase", option_d="drop",
            correct_option="c",
            explanation_ar="Cause and effect clue: which led to connects cause with result. Overindulgence in sweets means weight gain.",
            solution_steps_ar='["Conjunction: which led to means cause and effect","Cause: overindulgence in sweets","Logical result: increase in weight so option (c)"]',
            tags="cause-effect", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q38 - temporal
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.3,
            text_ar="After the sun _____, the farmer turned on his lamp and returned home.",
            option_a="rose", option_b="set", option_c="shone", option_d="appeared",
            correct_option="b",
            explanation_ar="Temporal clue: after plus turned on lamp means it was dark. Sunset is what necessitates turning on the lamp.",
            solution_steps_ar='["Temporal clue: after plus turned on lamp","Turning on lamp indicates darkness has fallen","the sun set is cause of darkness so option (b)"]',
            tags="cause-effect", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q39 - definition
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.3,
            text_ar="The dictionary is considered an essential tool for knowing the _____ of words and regulating their use.",
            option_a="shapes", option_b="colors", option_c="meanings", option_d="sizes",
            correct_option="c",
            explanation_ar="Definition clue: The dictionary is a tool for knowing means What is sought in a dictionary is meanings. Meanings of words are the primary function of the dictionary.",
            solution_steps_ar='["Type of clue: definition of dictionary function","Dictionary is used to know word meanings","meanings so option (c)"]',
            tags="definition", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q40 - contrast
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.3,
            text_ar="Despite the summer's _____ heat, winter comes cold and biting.",
            option_a="intense", option_b="moderate", option_c="cold", option_d="low",
            correct_option="a",
            explanation_ar="Contrast clue: despite contrasts summer and winter. Winter is cold and biting means Summer must be intensely hot.",
            solution_steps_ar='["Conjunction: despite means contrast","Winter: cold and biting (extremely cold)","Summer opposes it: intense heat so option (a)"]',
            tags="contrast", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q41 - contrast
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.4,
            text_ar="While the audience was _____ of the opposing team, they surprised them by scoring the winning goal in the last minute.",
            option_a="expecting victory", option_b="underestimating", option_c="fearing", option_d="respecting",
            correct_option="b",
            explanation_ar="Contrast clue: while...surprised them means what happened was contrary to expectation. The audience was underestimating the team but they surprised them with victory.",
            solution_steps_ar='["Conjunction: while...surprised them means contrast","Result: winning goal (positive surprise for the team)","Audience was underestimating equals did not expect victory so option (b)"]',
            tags="contrast", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q42 - cause/effect
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.4,
            text_ar="Debts accumulated on the company, which led to _____ its doors permanently.",
            option_a="expanding", option_b="opening", option_c="closing", option_d="renovating",
            correct_option="c",
            explanation_ar="Cause and effect clue: debt accumulation means negative result. Which led to connects cause with result: closing its doors.",
            solution_steps_ar='["Conjunction: which led to means cause and effect","Cause is negative: debt accumulation","Negative result: closing doors permanently so option (c)"]',
            tags="cause-effect", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q43 - temporal
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.4,
            text_ar="When the teacher announced the exam results, the outstanding student _____ with joy.",
            option_a="cried sadly", option_b="got angry", option_c="rejoiced", option_d="was frustrated",
            correct_option="c",
            explanation_ar="Temporal clue when the results were announced plus description of student as outstanding. The outstanding student rejoices when results are announced because they are positive for him.",
            solution_steps_ar='["Temporal clue: when results were announced","Student description: outstanding means good result","Natural reaction: rejoiced with joy so option (c)"]',
            tags="cause-effect", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q44 - definition
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.4,
            text_ar="Volunteering is providing _____ to the community without expecting material compensation.",
            option_a="harm", option_b="help", option_c="punishment", option_d="injury",
            correct_option="b",
            explanation_ar="Definition clue: Volunteering is providing means Definition of the concept. Help is the essence of volunteering.",
            solution_steps_ar='["Type of clue: definition of volunteering concept","Volunteering is positive action without compensation","providing help is essence of volunteering so option (b)"]',
            tags="definition", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q45 - contrast
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.4,
            text_ar="Although the book is _____ in pages, reading it is enjoyable and quick.",
            option_a="few", option_b="many", option_c="lacking", option_d="light",
            correct_option="b",
            explanation_ar="Contrast clue: although...reading is means contrast. Reading is enjoyable and quick despite having many pages.",
            solution_steps_ar='["Conjunction: although...reading is means contrast","Result: enjoyable and quick (easy)","Expected obstacle: many pages so option (b)"]',
            tags="contrast", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q46 - tone matching (negative)
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.4,
            text_ar="Chaos spread in the street and _____ spread among the residents after the power outage.",
            option_a="calm", option_b="reassurance", option_c="panic", option_d="delight",
            correct_option="c",
            explanation_ar="Negative tone matching clue: chaos plus power outage. Panic is a negative feeling matching the atmosphere of chaos.",
            solution_steps_ar='["Tone is negative: chaos plus power outage","Spreading feeling must be negative","panic is appropriate negative feeling so option (c)"]',
            tags="tone-matching", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q47 - cause/effect
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.4,
            text_ar="The athlete maintained his daily training, so his physical fitness _____ noticeably.",
            option_a="declined", option_b="weakened", option_c="improved", option_d="deteriorated",
            correct_option="c",
            explanation_ar="Cause and effect clue: so connects cause with result. Daily training means improvement in physical fitness.",
            solution_steps_ar='["Conjunction: so means cause and effect","Cause is positive: daily training","Positive result: fitness improved so option (c)"]',
            tags="cause-effect", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q48 - example
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.4,
            text_ar="Renewable energy sources are diverse, such as solar energy, _____ energy, and hydro energy.",
            option_a="coal", option_b="oil", option_c="wind", option_d="gas",
            correct_option="c",
            explanation_ar="Example clue: The context lists renewable energy sources. Solar and hydro are renewable so wind is also renewable energy.",
            solution_steps_ar='["Type of clue: examples of renewable energy","Solar and hydro are renewable","Coal, oil, and gas are not renewable so wind so option (c)"]',
            tags="definition", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q49 - contrast
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.4,
            text_ar="The patient was not in a state of _____ but was suffering from severe pain.",
            option_a="fatigue", option_b="illness", option_c="wellness", option_d="exhaustion",
            correct_option="c",
            explanation_ar="Contrast clue: but indicates the opposite. Second part: severe pain (negative) means First part: wellness (positive).",
            solution_steps_ar='["Conjunction: but means contrast","Second part: severe pain (bad condition)","First part must be the opposite: wellness so option (c)"]',
            tags="contrast", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q50 - cause/effect
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.4,
            text_ar="The farmer neglected irrigating his crops throughout the summer, so the land _____ and the crops were ruined.",
            option_a="flourished", option_b="bore fruit", option_c="dried up", option_d="ripened",
            correct_option="c",
            explanation_ar="Cause and effect clue: neglect of irrigation means negative result. Dried up means became dry which is natural result of no irrigation.",
            solution_steps_ar='["Conjunction: so means cause and effect","Cause: neglect of irrigation (negative)","Result: land dried up plus crops ruined so option (c)"]',
            tags="definition", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),


        # Q51 - temporal
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.4,
            text_ar="After years of effort and perseverance, the researcher finally _____ his doctoral degree.",
            option_a="gave up", option_b="obtained", option_c="conceded", option_d="withdrew",
            correct_option="b",
            explanation_ar="Temporal clue: after years of effort plus finally means achievement after long wait. Obtained the doctorate means positive result.",
            solution_steps_ar='["Temporal clue: after years plus finally means achievement","Context is positive: effort and perseverance means accomplishment","obtained the doctorate so option (b)"]',
            tags="cause-effect", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q52 - definition
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.4,
            text_ar="The scientist who studies stars and planets is called an _____ scientist.",
            option_a="biology", option_b="chemistry", option_c="astronomy", option_d="geography",
            correct_option="c",
            explanation_ar="Definition clue: studies stars and planets means Definition of the specialty. Astronomy scientist is who studies stars and planets.",
            solution_steps_ar='["Type of clue: definition of specialty","Stars and planets means field of astronomy","astronomy scientist so option (c)"]',
            tags="definition", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q53 - tone matching
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.4,
            text_ar="The wise leader makes his decisions with _____ and deliberation, away from haste.",
            option_a="recklessness", option_b="randomness", option_c="thoughtfulness", option_d="impulsiveness",
            correct_option="c",
            explanation_ar="Tone matching clue: wise plus deliberation plus away from haste. Thoughtfulness means thinking and deliberating, consistent with wisdom.",
            solution_steps_ar='["Tone is positive: wise plus deliberation plus away from haste","Word must indicate wisdom and deliberation","thoughtfulness equals deliberation and reflection so option (c)"]',
            tags="tone-matching", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q54 - contrast
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.4,
            text_ar="Do not judge a book by its _____ but read its content then judge.",
            option_a="chapters", option_b="pages", option_c="cover", option_d="index",
            correct_option="c",
            explanation_ar="Contrast clue: but contrasts superficial judgment with real judgment. Cover equals external appearance, content equals essence.",
            solution_steps_ar='["Conjunction: but means contrast between appearance and essence","Second part: content (essence)","First part: cover (appearance) so option (c)"]',
            tags="contrast", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q55 - cause/effect
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.4,
            text_ar="Health awareness spread among people, so the percentage of infectious diseases _____.",
            option_a="rose", option_b="increased", option_c="decreased", option_d="doubled",
            correct_option="c",
            explanation_ar="Cause and effect clue: spread of health awareness means positive result. Logical result: decrease in percentage of diseases.",
            solution_steps_ar='["Conjunction: so means cause and effect","Cause is positive: spread of health awareness","Positive result: diseases decreased so option (c)"]',
            tags="cause-effect", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q56 - example
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.4,
            text_ar="Saudi Arabia is famous for several landmarks, including the Grand Mosque, _____, and the Prophet's Mosque.",
            option_a="Eiffel Tower", option_b="the Holy Kaaba", option_c="Great Wall of China", option_d="Taj Mahal",
            correct_option="b",
            explanation_ar="Example clue: Saudi landmarks. Grand Mosque and Prophet's Mosque are in Saudi Arabia so Holy Kaaba is also a Saudi landmark.",
            solution_steps_ar='["Type of clue: examples of Saudi landmarks","Grand Mosque and Prophet Mosque are in Saudi Arabia","Holy Kaaba is a Saudi landmark so option (b)"]',
            tags="definition", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q57 - temporal
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.4,
            text_ar="Before the judge issued his ruling, he _____ carefully to all witnesses.",
            option_a="ignored", option_b="listened", option_c="avoided", option_d="rejected",
            correct_option="b",
            explanation_ar="Temporal clue: before issuing the ruling means preparatory action. Listening to witnesses carefully is step preceding the ruling.",
            solution_steps_ar='["Temporal clue: before issuing means action preceding ruling","Context: witnesses plus carefully means positive action","listened to witnesses so option (b)"]',
            tags="contrast", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q58 - contrast
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.4,
            text_ar="Despite the _____ of the idea at the beginning, everyone liked it after implementation.",
            option_a="acceptance", option_b="excellence", option_c="rejection", option_d="support",
            correct_option="c",
            explanation_ar="Contrast clue: despite...but means contrast. Everyone liked after implementation means they were rejecting at the beginning.",
            solution_steps_ar='["Conjunction: despite...but means contrast","Result: everyone liked it (positive)","Beginning must be negative: rejection so option (c)"]',
            tags="definition", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q59 - tone matching
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.4,
            text_ar="Volunteer work is characterized by nobility and _____ and contributes to building a cohesive community.",
            option_a="selfishness", option_b="greed", option_c="altruism", option_d="stinginess",
            correct_option="c",
            explanation_ar="Positive tone matching clue: nobility plus building cohesive community. Altruism is a positive characteristic consistent with volunteer work.",
            solution_steps_ar='["Tone is positive: nobility plus building cohesive community","Characteristic must be positive and related to volunteering","altruism equals preferring others so option (c)"]',
            tags="contrast", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q60 - cause/effect
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.4,
            text_ar="The region experienced a long drought, so the well waters gradually _____.",
            option_a="overflowed", option_b="rose", option_c="dried up", option_d="flowed",
            correct_option="c",
            explanation_ar="Cause and effect clue: long drought means negative result on water. Dried up means became dry which is natural result of drought.",
            solution_steps_ar='["Conjunction: so means cause and effect","Cause: long drought","Result: well waters dried up (became dry) so option (c)"]',
            tags="cause-effect", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q61 - temporal
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.4,
            text_ar="When the child reached his first year, he _____ with his first steps amidst the family's joy.",
            option_a="stopped", option_b="sat", option_c="walked", option_d="slept",
            correct_option="c",
            explanation_ar="Temporal clue: when he reached his first year plus his first steps. First steps means child walked which is natural age achievement.",
            solution_steps_ar='["Temporal clue: when he reached his first year","Indication: his first steps means beginning of walking","walked with his first steps so option (c)"]',
            tags="contrast", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q62 - definition
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.4,
            text_ar="The person who writes novels and stories is called _____.",
            option_a="an engineer", option_b="a writer", option_c="a doctor", option_d="an accountant",
            correct_option="b",
            explanation_ar="Definition clue: writing novels and stories means Definition of the profession. Writer is who writes literary works like novels and stories.",
            solution_steps_ar='["Type of clue: definition means the person who writes...","Writing novels and stories means field of literature","writer so option (b)"]',
            tags="definition", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q63 - contrast
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.5,
            text_ar="While youth tend to _____ in decision-making, the elderly are characterized by wisdom and deliberation.",
            option_a="wisdom", option_b="deliberation", option_c="haste", option_d="composure",
            correct_option="c",
            explanation_ar="Contrast clue: while contrasts youth with elderly. Elderly: wisdom and deliberation means Youth: haste (the opposite).",
            solution_steps_ar='["Conjunction: while means contrast between two groups","Elderly: wisdom and deliberation (deliberation)","Youth must be the opposite: haste so option (c)"]',
            tags="contrast", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q64 - cause/effect
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.5,
            text_ar="The sudden _____ in prices led to consumer discontent and protests.",
            option_a="decrease", option_b="stability", option_c="rise", option_d="stabilization",
            correct_option="c",
            explanation_ar="Cause and effect clue: led to connects cause with result. Discontent and protest means caused by price rise.",
            solution_steps_ar='["Conjunction: led to means cause and effect","Result is negative: discontent and protest","Cause: rise in prices so option (c)"]',
            tags="cause-effect", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q65 - tone matching
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.5,
            text_ar="The manager dealt with the crisis with _____ and high professionalism, earning everyone's admiration.",
            option_a="chaos", option_b="confusion", option_c="competence", option_d="randomness",
            correct_option="c",
            explanation_ar="Positive tone matching clue: high professionalism plus admiration of everyone. Competence is a positive characteristic consistent with professionalism.",
            solution_steps_ar='["Tone is positive: professionalism plus admiration of everyone","Word must be a positive professional characteristic","competence so option (c)"]',
            tags="tone-matching", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q66 - temporal
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.5,
            text_ar="After the engineer _____ the plans carefully, the workers began implementing the project.",
            option_a="destroyed", option_b="neglected", option_c="reviewed", option_d="tore",
            correct_option="c",
            explanation_ar="Temporal clue: after...workers began means action preceding implementation. Reviewed the plans carefully is logical step before starting work.",
            solution_steps_ar='["Temporal clue: after means action preceding implementation","Context: plans plus carefully means positive action","reviewed the plans so option (c)"]',
            tags="contrast", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q67 - contrast
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.5,
            text_ar="The speech was not _____ as the audience expected, but came brief and concise.",
            option_a="short", option_b="brief", option_c="lengthy", option_d="concise",
            correct_option="c",
            explanation_ar="Contrast clue: but contrasts expectation with reality. Reality: brief and concise means Expectation: lengthy (the opposite).",
            solution_steps_ar='["Conjunction: but means contrast between expectation and reality","Reality: brief and concise (short)","Expectation must be the opposite: lengthy so option (c)"]',
            tags="contrast", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q68 - example
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.5,
            text_ar="Arabic is one of the oldest living languages, like _____ and Chinese.",
            option_a="Esperanto", option_b="Hebrew", option_c="sign language", option_d="programming",
            correct_option="b",
            explanation_ar="Example clue: ancient living languages. Arabic and Chinese are ancient languages so Hebrew is also an ancient living language.",
            solution_steps_ar='["Type of clue: examples of ancient living languages","Arabic and Chinese are ancient languages still living","Hebrew is an ancient living language so option (b)"]',
            tags="definition", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q69 - cause/effect
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.5,
            text_ar="The company's continuous _____ in innovation made it lead the market over its competitors.",
            option_a="shortcoming", option_b="failure", option_c="investment", option_d="neglect",
            correct_option="c",
            explanation_ar="Cause and effect clue: X made it lead means Cause is positive. Investment of the company in innovation means cause of leadership.",
            solution_steps_ar='["Relationship: cause (X) leads to result (market leadership)","Result is positive so Cause must be positive","investment in innovation so option (c)"]',
            tags="cause-effect", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q70 - contrast
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.5,
            text_ar="Although the medicine _____ in taste, its effect is fast and effective.",
            option_a="sweet", option_b="delicious", option_c="bitter", option_d="pleasant",
            correct_option="c",
            explanation_ar="Contrast clue: although...but means contrast. Effect is positive (fast and effective) means Taste is negative: bitter.",
            solution_steps_ar='["Conjunction: although...but means contrast","Positive side: fast and effective effect","Negative side: bitter taste so option (c)"]',
            tags="contrast", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q71 - definition
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.5,
            text_ar="Justice means giving everyone their _____ without favoritism or discrimination.",
            option_a="punishment", option_b="right", option_c="injustice", option_d="deprivation",
            correct_option="b",
            explanation_ar="Definition clue: Justice means means Definition of concept. Right is the word that completes justice definition: giving everyone their right.",
            solution_steps_ar='["Type of clue: definition of justice concept","without favoritism or discrimination means fairness","giving everyone their right is definition of justice so option (b)"]',
            tags="definition", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q72 - tone matching (negative)
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.5,
            text_ar="_____ prevailed in the hall after the loss was announced, and no one uttered a word.",
            option_a="noise", option_b="silence", option_c="laughter", option_d="singing",
            correct_option="b",
            explanation_ar="Negative tone matching clue: loss plus no one uttered a word. Silence matches the atmosphere of loss and shock.",
            solution_steps_ar='["Tone is negative: loss plus no one uttered a word","did not utter equals did not speak means silence","silence prevailed so option (b)"]',
            tags="tone-matching", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q73 - cause/effect
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.5,
            text_ar="The team relied on collective work, so they _____ in completing the task before the deadline.",
            option_a="failed", option_b="were delayed", option_c="succeeded", option_d="stalled",
            correct_option="c",
            explanation_ar="Cause and effect clue: so connects cause with result. Collective work means Success in completing before deadline.",
            solution_steps_ar='["Conjunction: so means cause and effect","Cause is positive: collective work","Positive result: succeeded in completion so option (c)"]',
            tags="contrast", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q74 - temporal
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.5,
            text_ar="When the news _____ on his ears, his facial features changed from surprise.",
            option_a="was absent", option_b="fell", option_c="disappeared", option_d="faded",
            correct_option="b",
            explanation_ar="Temporal clue: when plus reaction (features changed). News fell on his ears means he heard it which is proper idiomatic expression.",
            solution_steps_ar='["Temporal clue: when means moment of hearing news","Idiomatic expression: news fell on his ears","fell so option (b)"]',
            tags="temporal", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q75 - contrast
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.5,
            text_ar="The distance was not _____ as he thought, but it took long hours due to traffic.",
            option_a="far", option_b="long", option_c="close", option_d="vast",
            correct_option="a",
            explanation_ar="Contrast clue: but indicates contrast. Took long hours means he thought it was far but it was not (cause is traffic).",
            solution_steps_ar='["Conjunction: but means contrast","Result: took long time due to traffic not distance","Assumption: that it was far but cause was traffic so option (a)"]',
            tags="contrast", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q76 - example
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.5,
            text_ar="Among the noble Islamic values: honesty, _____, and kindness to others.",
            option_a="cheating", option_b="lying", option_c="trustworthiness", option_d="betrayal",
            correct_option="c",
            explanation_ar="Example clue: Listing noble Islamic values. Honesty and kindness are positive values so trustworthiness is a positive Islamic value.",
            solution_steps_ar='["Type of clue: examples of noble Islamic values","Honesty and kindness are positive values","trustworthiness is a positive value so option (c)"]',
            tags="tone-matching", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q77 - definition
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.5,
            text_ar="Sustainable development means achieving the needs of the present without harming the rights of future generations.",
            option_a="destruction", option_b="needs", option_c="waste", option_d="depletion",
            correct_option="b",
            explanation_ar="Definition clue: means means Definition of term. Sustainable development equals meeting present needs while preserving future rights.",
            solution_steps_ar='["Type of clue: definition (means...)","Sustainable development means balance between present and future","meeting needs of present so option (b)"]',
            tags="definition", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q78 - cause/effect
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.5,
            text_ar="Lack of supervision on markets _____ the spread of commercial fraud and counterfeit products.",
            option_a="prevented", option_b="limited", option_c="contributed to", option_d="eliminated",
            correct_option="c",
            explanation_ar="Cause and effect clue: lack of supervision (negative) means negative result. Contributed to spread of fraud means lack of supervision facilitated fraud.",
            solution_steps_ar='["Relationship: cause (lack of supervision) leads to result (spread of fraud)","Both sides are negative so relationship is contribution","contributed to is logical link so option (c)"]',
            tags="cause-effect", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q79 - tone matching
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.5,
            text_ar="The speaker showed great _____ in the environmental topic, and his words came from firm conviction.",
            option_a="indifference", option_b="interest", option_c="neglect", option_d="contempt",
            correct_option="b",
            explanation_ar="Positive tone matching clue: firm conviction plus words coming from faith. Interest matches firm conviction.",
            solution_steps_ar='["Tone is positive: firm conviction","Word must indicate enthusiasm and seriousness","great interest so option (b)"]',
            tags="cause-effect", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q80 - contrast
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.5,
            text_ar="Despite the experiment's _____ at the beginning, it produced amazing results.",
            option_a="success", option_b="excellence", option_c="failure", option_d="superiority",
            correct_option="c",
            explanation_ar="Contrast clue: despite...but means contrast. Results are amazing (positive) means Beginning: failure (negative).",
            solution_steps_ar='["Conjunction: despite...but means contrast","Final result: amazing (positive)","Beginning must be negative: failure so option (c)"]',
            tags="contrast", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),


        # Q81 - contrast
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.6,
            text_ar="While the scientific approach is characterized by _____ and precision, the literary approach relies on imagination and emotion.",
            option_a="ambiguity", option_b="randomness", option_c="objectivity", option_d="bias",
            correct_option="c",
            explanation_ar="Contrast clue: while contrasts the two approaches. Literary approach: imagination and emotion (subjective) means Scientific approach: objectivity and precision.",
            solution_steps_ar='["Conjunction: while means contrast","Literary approach: imagination and emotion (subjective)","Scientific approach opposes it: objectivity and precision so option (c)"]',
            tags="contrast", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q82 - cause/effect
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.6,
            text_ar="Because the leader effectively _____ his authority among the team, the department's productivity increased significantly.",
            option_a="monopolized", option_b="restricted", option_c="distributed", option_d="withdrew",
            correct_option="c",
            explanation_ar="Cause and effect clue: because connects cause with result. Productivity increase means due to effective distribution of authority.",
            solution_steps_ar='["Conjunction: because means cause and effect","Positive result: productivity increase","Positive cause: effective distribution of authority so option (c)"]',
            tags="cause-effect", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q83 - tone matching
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.6,
            text_ar="The poet distinguished himself by _____ in expressing his feelings, so his poems captivated readers' hearts.",
            option_a="stiffness", option_b="coldness", option_c="tenderness", option_d="harshness",
            correct_option="c",
            explanation_ar="Positive tone matching clue: captivated readers' hearts. Tenderness in expressing feelings means positive poetic characteristic.",
            solution_steps_ar='["Tone is positive: captivated hearts","Characteristic related to expressing feelings","tenderness equals gentleness and refinement in expression so option (c)"]',
            tags="tone-matching", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q84 - temporal
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.6,
            text_ar="Before the final results were announced, the committee _____ a precise recounting process for all votes.",
            option_a="canceled", option_b="skipped", option_c="conducted", option_d="ignored",
            correct_option="c",
            explanation_ar="Temporal clue: before announcement means procedure preceding announcement. Committee conducted recounting is verification step before official announcement.",
            solution_steps_ar='["Temporal clue: before means procedure preceding announcement","Context: recounting plus precise means formal positive action","committee conducted recounting process so option (c)"]',
            tags="contrast", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q85 - contrast
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.6,
            text_ar="The building's exterior was _____ but from inside it was luxurious and decorated with beautiful designs.",
            option_a="luxurious", option_b="elegant", option_c="modest", option_d="dazzling",
            correct_option="c",
            explanation_ar="Contrast clue: but contrasts exterior with interior. Interior is luxurious and decorated means Exterior: modest (the opposite).",
            solution_steps_ar='["Conjunction: but means contrast between exterior and interior","Interior: luxurious and decorated (positive)","Exterior must be the opposite: modest so option (c)"]',
            tags="contrast", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q86 - cause/effect
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.6,
            text_ar="Islamic civilization flourished because Muslim scholars _____ on translation and scientific research.",
            option_a="abstained", option_b="were keen", option_c="gave up", option_d="refrained",
            correct_option="b",
            explanation_ar="Cause and effect clue: because connects cause of flourishing. Flourishing means due to scholars' keenness on translation and research.",
            solution_steps_ar='["Conjunction: because means cause and effect","Positive result: flourishing of civilization","Cause: were keen on translation and research so option (b)"]',
            tags="cause-effect", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q87 - definition
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.6,
            text_ar="Inflation is defined as the continuous rise in the _____ of goods and services over a period of time.",
            option_a="quality", option_b="quantity", option_c="prices", option_d="sizes",
            correct_option="c",
            explanation_ar="Definition clue: is defined as means Economic definition. Inflation equals continuous rise in prices of goods and services.",
            solution_steps_ar='["Type of clue: economic definition (is defined as)","Inflation is economic term related to prices","rise in prices of goods and services so option (c)"]',
            tags="definition", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q88 - example
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.6,
            text_ar="Democracy is based on several principles, such as freedom of expression, _____, and rule of law.",
            option_a="despotism", option_b="domination", option_c="equality", option_d="repression",
            correct_option="c",
            explanation_ar="Example clue: Democratic principles. Freedom of expression and rule of law are positive principles so equality is a democratic principle.",
            solution_steps_ar='["Type of clue: examples of democratic principles","Freedom of expression and rule of law are positive principles","equality is a democratic principle so option (c)"]',
            tags="tone-matching", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q89 - contrast
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.6,
            text_ar="Although reason calls for _____ in such situations, emotion often drives a person to recklessness.",
            option_a="impulsiveness", option_b="recklessness", option_c="caution", option_d="risk-taking",
            correct_option="c",
            explanation_ar="Contrast clue: although...but means contrast between reason and emotion. Emotion: recklessness means Reason: caution (the opposite).",
            solution_steps_ar='["Conjunction: although...but means contrast","Emotion: recklessness (impulse)","Reason opposes it: caution and deliberation so option (c)"]',
            tags="contrast", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q90 - cause/effect
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.6,
            text_ar="The development of modern technology _____ in facilitating communication between peoples despite language differences.",
            option_a="absence", option_b="development", option_c="decline", option_d="lack",
            correct_option="b",
            explanation_ar="Cause and effect clue: X contributed to facilitating communication. Positive result means Positive cause: development of technology.",
            solution_steps_ar='["Relationship: cause leads to result (facilitating communication)","Result is positive","Cause must be positive: development of technology so option (b)"]',
            tags="contrast", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q91 - temporal
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.6,
            text_ar="After the author _____ his latest novel, it received wide praise from critics.",
            option_a="burned", option_b="published", option_c="destroyed", option_d="deleted",
            correct_option="b",
            explanation_ar="Temporal clue: after plus critics' praise means action preceding praise. Published the novel means logical step before receiving praise.",
            solution_steps_ar='["Temporal clue: after means action preceding praise","Critics only praise after publication","author published his novel so option (b)"]',
            tags="contrast", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q92 - tone matching
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.6,
            text_ar="The king honored the scientist in appreciation for the great _____ he provided to his country in medicine.",
            option_a="offenses", option_b="damages", option_c="contributions", option_d="violations",
            correct_option="c",
            explanation_ar="Positive tone matching clue: honored plus appreciation plus his country. Contributions means positive work deserving honor.",
            solution_steps_ar='["Tone is positive: honoring plus appreciation","Word must indicate positive work","great contributions in medicine so option (c)"]',
            tags="tone-matching", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q93 - contrast
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.6,
            text_ar="The decision was not _____ as it appeared at first glance, but was studied and based on scientific foundations.",
            option_a="wise", option_b="studied", option_c="random", option_d="sound",
            correct_option="c",
            explanation_ar="Contrast clue: but contrasts appearance with reality. Reality: studied and based on foundations means First appearance: random.",
            solution_steps_ar='["Conjunction: but means contrast between appearance and reality","Reality: studied and based on scientific foundations","First appearance must be the opposite: random so option (c)"]',
            tags="contrast", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q94 - cause/effect
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.6,
            text_ar="The _____ of communication channels between management and employees led to accumulation of misunderstanding between them.",
            option_a="abundance", option_b="plenty", option_c="scarcity", option_d="multiplicity",
            correct_option="c",
            explanation_ar="Cause and effect clue: led to accumulation of misunderstanding. Negative result means Negative cause: scarcity of communication channels.",
            solution_steps_ar='["Conjunction: led to means cause and effect","Negative result: accumulation of misunderstanding","Negative cause: scarcity of communication channels so option (c)"]',
            tags="cause-effect", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q95 - example
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.6,
            text_ar="Among the most prominent factors of project success: sound planning, _____, and continuous follow-up.",
            option_a="neglect", option_b="randomness", option_c="adequate funding", option_d="delay",
            correct_option="c",
            explanation_ar="Example clue: Factors of project success. Sound planning and continuous follow-up are positive factors so adequate funding is also a success factor.",
            solution_steps_ar='["Type of clue: examples of success factors","Planning and follow-up are positive factors","adequate funding is essential success factor so option (c)"]',
            tags="definition", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q96 - definition
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.6,
            text_ar="Emotional intelligence refers to a person's ability to _____ their emotions and others' emotions and deal with them wisely.",
            option_a="suppress", option_b="ignore", option_c="recognize", option_d="conceal",
            correct_option="c",
            explanation_ar="Definition clue: refers to concept means Definition. Emotional intelligence equals recognizing emotions plus dealing with them wisely.",
            solution_steps_ar='["Type of clue: definition (refers to concept...)","Emotional intelligence requires understanding emotions first","recognizing emotions is first step so option (c)"]',
            tags="definition", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q97 - tone matching (negative)
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.6,
            text_ar="The hurricane caused widespread _____, homes were destroyed and thousands were displaced.",
            option_a="reconstruction", option_b="prosperity", option_c="destruction", option_d="stability",
            correct_option="c",
            explanation_ar="Negative tone matching clue: hurricane plus homes destroyed plus thousands displaced. Destruction widespread means matches negative tone.",
            solution_steps_ar='["Tone is negative: hurricane plus destroyed plus displaced","Word must describe wide negative impact","widespread destruction so option (c)"]',
            tags="cause-effect", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q98 - temporal
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.6,
            text_ar="When the poet _____ his poem before the audience, a wave of warm applause erupted.",
            option_a="concealed", option_b="deleted", option_c="recited", option_d="neglected",
            correct_option="c",
            explanation_ar="Temporal clue: when plus audience reaction (warm applause). Recited his poem means the action that aroused audience admiration.",
            solution_steps_ar='["Temporal clue: when means moment of recitation","Result: warm applause means admiration","poet recited his poem so option (c)"]',
            tags="cause-effect", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q99 - contrast
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.7,
            text_ar="Although the theory seemed _____ logically, laboratory experiments proved its invalidity.",
            option_a="flimsy", option_b="weak", option_c="coherent", option_d="fragile",
            correct_option="c",
            explanation_ar="Contrast clue: although...but means contrast. Experiments proved invalidity (negative) means Theory seemed coherent (positive).",
            solution_steps_ar='["Conjunction: although...but means contrast","Result: experiments proved invalidity (failed)","Theory seemed the opposite: coherent logically so option (c)"]',
            tags="contrast", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q100 - cause/effect
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.7,
            text_ar="Because the government _____ strict economic policies at the right time, it was able to overcome the financial crisis.",
            option_a="neglected", option_b="adopted", option_c="rejected", option_d="delayed",
            correct_option="b",
            explanation_ar="Cause and effect clue: because connects cause with result. Overcoming crisis (positive) means due to adopting strict policies.",
            solution_steps_ar='["Conjunction: because means cause and effect","Positive result: overcoming crisis","Positive cause: adopted strict policies so option (b)"]',
            tags="cause-effect", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q101 - tone matching
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.7,
            text_ar="The president's speech was characterized by _____ and boldness, which aroused allies' admiration and opponents' concern at the same time.",
            option_a="evasiveness", option_b="frankness", option_c="ambiguity", option_d="deception",
            correct_option="b",
            explanation_ar="Tone matching clue: boldness plus admiration plus opponents' concern. Frankness matches boldness and explains opponents' concern.",
            solution_steps_ar='["Tone: boldness plus allies admiration plus opponents concern","Boldness paired with similar positive characteristic","frankness equals clarity and boldness so option (b)"]',
            tags="tone-matching", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q102 - temporal
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.7,
            text_ar="After investigators _____ conclusive evidence of the defendant's involvement, the prosecution referred him to court.",
            option_a="concealed", option_b="destroyed", option_c="gathered", option_d="ignored",
            correct_option="c",
            explanation_ar="Temporal clue: after means action preceding referral to court. Gathered conclusive evidence means investigative step preceding referral.",
            solution_steps_ar='["Temporal clue: after means action preceding referral","Context: conclusive evidence plus involvement means positive investigative action","gathered evidence so option (c)"]',
            tags="tone-matching", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q103 - contrast
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.7,
            text_ar="While optimists see the crisis as an opportunity for change, pessimists see it as a _____ foretelling collapse.",
            option_a="good omen", option_b="opportunity", option_c="disaster", option_d="blessing",
            correct_option="c",
            explanation_ar="Contrast clue: while contrasts optimists' and pessimists' views. Optimists: opportunity means Pessimists: disaster.",
            solution_steps_ar='["Conjunction: while means contrast between two views","Optimists: opportunity for change (positive)","Pessimists: disaster foretelling collapse (negative) so option (c)"]',
            tags="definition", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q104 - cause/effect
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.7,
            text_ar="The _____ of coordination between different government agencies hindered implementation of the comprehensive development plan.",
            option_a="success", option_b="integration", option_c="absence", option_d="effectiveness",
            correct_option="c",
            explanation_ar="Cause and effect clue: X hindered implementation means Cause is negative. Absence of coordination equals non-existence which is negative cause hindering implementation.",
            solution_steps_ar='["Relationship: cause leads to result (hindered implementation)","Negative result: hindrance of plan","Negative cause: absence of coordination so option (c)"]',
            tags="cause-effect", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q105 - definition
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.7,
            text_ar="Separation of powers means the _____ of each power in its work without interference in other powers' affairs.",
            option_a="overlap", option_b="merging", option_c="independence", option_d="dependence",
            correct_option="c",
            explanation_ar="Definition clue: means principle means legal definition. Separation of powers equals independence of each power in its work.",
            solution_steps_ar='["Type of clue: legal definition (means principle...)","Separation equals non-interference in others affairs","independence of each power in its work so option (c)"]',
            tags="definition", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q106 - contrast
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.7,
            text_ar="The audience's reaction was not _____ as organizers expected, but was lukewarm and far from enthusiastic.",
            option_a="cold", option_b="weak", option_c="enthusiastic", option_d="muted",
            correct_option="c",
            explanation_ar="Contrast clue: but contrasts expectation with reality. Reality: lukewarm and far from enthusiasm means Expectation: enthusiastic.",
            solution_steps_ar='["Conjunction: but means contrast between expectation and reality","Reality: lukewarm plus far from enthusiasm (negative)","Expectation must be the opposite: enthusiastic so option (c)"]',
            tags="contrast", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q107 - example
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.7,
            text_ar="Among the most prominent manifestations of Arab civilization are its contributions to astronomy, _____, and medicine that influenced Western civilization.",
            option_a="cooking", option_b="mathematics", option_c="dancing", option_d="hunting",
            correct_option="b",
            explanation_ar="Example clue: Sciences in which Arab civilization contributed. Astronomy and medicine are academic sciences so mathematics is an academic science Arabs were famous for.",
            solution_steps_ar='["Type of clue: examples of Arab civilization scientific contributions","Astronomy and medicine are fundamental sciences","mathematics is a science Arab scholars were famous for so option (b)"]',
            tags="condition", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q108 - contrast
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.8,
            text_ar="While diplomacy seeks to _____ conflicts through dialogue, military solutions often lead to complicating and escalating situations.",
            option_a="inflame", option_b="escalate", option_c="resolve", option_d="ignite",
            correct_option="c",
            explanation_ar="Contrast clue: while...but means contrast between diplomacy and military solutions. Military: complication and escalation means Diplomacy: resolving conflicts (the opposite).",
            solution_steps_ar='["Conjunction: while...but means contrast between two approaches","Military solutions: complication and escalation (negative)","Diplomacy: resolving conflicts (positive) so option (c)"]',
            tags="contrast", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q109 - cause/effect
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.8,
            text_ar="Because the institution _____ in building an organizational culture based on transparency and accountability, it attracted exceptional talents from various sectors.",
            option_a="failed", option_b="slackened", option_c="succeeded", option_d="neglected",
            correct_option="c",
            explanation_ar="Cause and effect clue: because...it attracted connects cause with result. Attracting talents (positive) means due to institution's success in building transparent culture.",
            solution_steps_ar='["Conjunction: because...it attracted means cause and effect","Positive result: attracting exceptional talents","Positive cause: succeeded in building transparency culture so option (c)"]',
            tags="cause-effect", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # Q110 - tone matching
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.8,
            text_ar="Research showed that individuals with high psychological _____ are more capable of adapting to crises and making sound decisions under pressure.",
            option_a="fragility", option_b="flexibility", option_c="rigidity", option_d="stiffness",
            correct_option="b",
            explanation_ar="Positive tone matching clue: ability to adapt plus sound decisions under pressure. Psychological flexibility equals the ability to adapt and recover which is precise psychological term.",
            solution_steps_ar='["Tone is positive: adaptation plus sound decisions","Word related to ability to deal with crises","psychological flexibility is precise psychological term so option (b)"]',
            tags="tone-matching", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # Q111 - contrast + cause/effect (compound)
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.8,
            text_ar="Although the project started with _____ resources and a small team, wise management and diligent work transformed it into one of the most successful projects in the region.",
            option_a="massive", option_b="abundant", option_c="scarce", option_d="huge",
            correct_option="c",
            explanation_ar="Compound contrast clue: although...but means negative beginning and positive result. Result: most successful projects means Beginning: scarce resources plus small team.",
            solution_steps_ar='["Conjunction: although...but means contrast","Result: most successful projects (positive)","Negative beginning: scarce resources plus small team so option (c)"]',
            tags="contrast", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),


        # ══════════════════════════════════════════════════════════════
        # 56 NEW QUESTIONS (Q112-Q167)
        # ══════════════════════════════════════════════════════════════

        # Q112
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.2,
            text_ar="Students go to _____ every morning to receive education.",
            option_a="the market", option_b="school", option_c="the playground", option_d="the restaurant",
            correct_option="b",
            explanation_ar="Context: receiving education every morning means Appropriate place is school.",
            solution_steps_ar='["Clue: receiving education means educational place","Students go in the morning means school routine","school is the appropriate place so option (b)"]',
            tags="definition", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # Q113
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.2,
            text_ar="The farmer uses _____ to plow the land and prepare it for agriculture.",
            option_a="the plow", option_b="the pen", option_c="the microscope", option_d="the phone",
            correct_option="a",
            explanation_ar="Context: plowing land means Appropriate tool is plow.",
            solution_steps_ar='["Clue: plowing land plus agriculture","Appropriate tool for plowing","plow is the farmer tool so option (a)"]',
            tags="definition", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # Q114
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.2,
            text_ar="In winter, _____ degrees drop and rain falls.",
            option_a="humidity", option_b="temperature", option_c="speed", option_d="density",
            correct_option="b",
            explanation_ar="Context: winter season plus dropping means Temperature degrees are what drop.",
            solution_steps_ar='["Clue: winter season means coldness","Dropping is associated with temperature degrees","temperature so option (b)"]',
            tags="definition", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # Q115
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.3,
            text_ar="The doctor examines the patient then writes him a _____ to buy medicine.",
            option_a="letter", option_b="prescription", option_c="poem", option_d="ticket",
            correct_option="b",
            explanation_ar="Context: examination plus medicine means Doctor writes prescription.",
            solution_steps_ar='["Clue: examining patient plus buying medicine","What the doctor writes for the patient","medical prescription so option (b)"]',
            tags="definition", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # Q116
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.3,
            text_ar="The father was keen on _____ his children to respect elders and be kind to young ones.",
            option_a="neglecting", option_b="raising", option_c="punishing", option_d="intimidating",
            correct_option="b",
            explanation_ar="Context: respecting elders plus kindness to young means Positive values instilled through upbringing.",
            solution_steps_ar='["Clue: respect plus kindness means positive values","Appropriate action: instilling values","raising children so option (b)"]',
            tags="tone-matching", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # Q117
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.3,
            text_ar="The diver cannot stay long underwater without _____ for breathing.",
            option_a="helmet", option_b="oxygen tank", option_c="shoes", option_d="watch",
            correct_option="b",
            explanation_ar="Context: diving plus breathing underwater means Oxygen tank.",
            solution_steps_ar='["Clue: staying underwater plus breathing","What the diver needs for breathing","oxygen tank so option (b)"]',
            tags="condition", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q118
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.3,
            text_ar="Petroleum is known as _____ gold due to its great economic importance.",
            option_a="white", option_b="black", option_c="red", option_d="green",
            correct_option="b",
            explanation_ar="Context: petroleum plus gold plus economic importance means Nicknamed black gold.",
            solution_steps_ar='["Clue: petroleum plus gold","Well-known nickname for petroleum","black gold so option (b)"]',
            tags="definition", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q119
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.3,
            text_ar="When the sun sets, _____ falls and stars appear in the sky.",
            option_a="light", option_b="darkness", option_c="morning", option_d="heat",
            correct_option="b",
            explanation_ar="Context: sun setting plus stars appearing means Darkness falls.",
            solution_steps_ar='["Clue: sun setting means absence of light","Stars appear means night time","darkness falls so option (b)"]',
            tags="temporal", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q120
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.4,
            text_ar="Despite the exam's difficulty, the diligent student was able to _____ all questions.",
            option_a="ignore", option_b="solve", option_c="delete", option_d="forget",
            correct_option="b",
            explanation_ar="Contrast clue: despite difficulty plus diligent student means was able to solve questions.",
            solution_steps_ar='["Conjunction: despite means contrast","Diligent student means positive result despite difficulty","solving all questions so option (b)"]',
            tags="contrast", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q121
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.4,
            text_ar="If you want to maintain your health, you must immediately _____ smoking.",
            option_a="continue", option_b="quit", option_c="start", option_d="persist in",
            correct_option="b",
            explanation_ar="Conditional clue: if you want to maintain health means Quitting smoking.",
            solution_steps_ar='["Clue: maintaining health means positive action","Smoking is harmful means must stop","quitting smoking so option (b)"]',
            tags="condition", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q122
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.4,
            text_ar="The desert climate is characterized by _____ temperature degrees during the day and their drop at night.",
            option_a="moderation", option_b="rise", option_c="stability", option_d="drop",
            correct_option="b",
            explanation_ar="Contrast clue: day temperature vs night drop means rise during day.",
            solution_steps_ar='["Clue: desert climate means extreme temperatures","Contrast: day vs night","rise during day and drop at night so option (b)"]',
            tags="contrast", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q123
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.4,
            text_ar="When scientists discovered the flaw in the experiment's _____, they repeated it from the beginning.",
            option_a="results", option_b="success", option_c="procedures", option_d="benefits",
            correct_option="c",
            explanation_ar="Cause clue: discovering flaw means repeating experiment means flaw in procedures.",
            solution_steps_ar='["Clue: discovering flaw means reason to repeat experiment","Flaw is in method not results","experiment procedures so option (c)"]',
            tags="cause-effect", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q124
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.4,
            text_ar="The more population _____ in major cities, the more traffic and housing problems intensified.",
            option_a="decline", option_b="decrease", option_c="congestion", option_d="migration",
            correct_option="c",
            explanation_ar="Cause and effect clue: increase in X means intensification of problems means congestion of population.",
            solution_steps_ar='["Relationship: the more means proportional relationship","Result: intensification of traffic and housing problems","Cause: congestion of population so option (c)"]',
            tags="cause-effect", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q125
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.4,
            text_ar="The National Library is considered a cultural _____ that preserves the nation's intellectual heritage.",
            option_a="obstacle", option_b="monument", option_c="danger", option_d="threat",
            correct_option="b",
            explanation_ar="Positive context: preserving intellectual heritage means monument culturally.",
            solution_steps_ar='["Clue: preserving intellectual heritage means positive value","Appropriate word is positive","cultural monument so option (b)"]',
            tags="tone-matching", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q126
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.4,
            text_ar="After the rains _____ heavily, valleys overflowed and water flooded the roads.",
            option_a="stopped", option_b="ceased", option_c="fell", option_d="decreased",
            correct_option="c",
            explanation_ar="Temporal clue: after plus flooding means heavy rainfall preceding flood.",
            solution_steps_ar='["Temporal clue: after means preceding action","Result: flooding plus road flooding","Cause: rain fell heavily so option (c)"]',
            tags="temporal", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q127
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.4,
            text_ar="Sustainable development means achieving economic growth while _____ on natural resources for future generations.",
            option_a="eliminating", option_b="preserving", option_c="attacking", option_d="depleting",
            correct_option="b",
            explanation_ar="Definition clue: Sustainable development means growth plus preservation of resources.",
            solution_steps_ar='["Clue: definition (means...)","Sustainable development equals balance between growth and environment","preserving natural resources so option (b)"]',
            tags="definition", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q128
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.4,
            text_ar="Were it not for firefighters' rapid _____, the flames would have consumed the entire building.",
            option_a="delay", option_b="absence", option_c="intervention", option_d="neglect",
            correct_option="c",
            explanation_ar="Conditional clue: were it not for means condition preventing disaster means intervention of firefighters.",
            solution_steps_ar='["Conjunction: were it not for means conditional prevention","Prevented result: flames consuming building","Preventing cause: firefighters intervention so option (c)"]',
            tags="condition", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q129
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.4,
            text_ar="Trade has become a _____ fundamental pillar in the modern economy thanks to Internet spread.",
            option_a="traditional", option_b="electronic", option_c="primitive", option_d="local",
            correct_option="b",
            explanation_ar="Cause clue: Internet spread means Electronic trade.",
            solution_steps_ar='["Clue: thanks to Internet spread","Type of trade associated with Internet","electronic trade so option (b)"]',
            tags="cause-effect", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q130
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.5,
            text_ar="While economists see that privatization enhances efficiency, others fear it may lead to _____ the gap between rich and poor.",
            option_a="narrowing", option_b="removing", option_c="widening", option_d="eliminating",
            correct_option="c",
            explanation_ar="Contrast clue: while...fear means enhancing efficiency (positive) vs fear of widening gap (negative).",
            solution_steps_ar='["Conjunction: while means contrast between two views","First view: enhancing efficiency (positive)","Fear: widening gap (negative) so option (c)"]',
            tags="contrast", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q131
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.5,
            text_ar="Because the researcher _____ a precise scientific methodology in his study, his results received wide acceptance in the academic community.",
            option_a="neglected", option_b="rejected", option_c="adopted", option_d="avoided",
            correct_option="c",
            explanation_ar="Cause and effect clue: because...received means wide acceptance due to adopting precise methodology.",
            solution_steps_ar='["Conjunction: because means cause and effect","Positive result: wide acceptance","Cause: adopted precise scientific methodology so option (c)"]',
            tags="cause-effect", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q132
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.5,
            text_ar="Scientific research requires _____ in collecting data and _____ in analyzing it to reach reliable results.",
            option_a="haste / superficiality", option_b="precision / objectivity", option_c="neglect / bias", option_d="randomness / subjectivity",
            correct_option="b",
            explanation_ar="Double clue: Scientific research plus reliable results means precision in collection and objectivity in analysis.",
            solution_steps_ar='["Clue: scientific research plus reliable results means positive characteristics","First blank: collecting data means precision","Second blank: analysis means objectivity so option (b)"]',
            tags="tone-matching", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q133
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.5,
            text_ar="Before the manager made his final decision, he _____ all reports and listened to his team's opinions.",
            option_a="neglected", option_b="destroyed", option_c="studied", option_d="ignored",
            correct_option="c",
            explanation_ar="Temporal clue: before means step preceding decision means studied reports.",
            solution_steps_ar='["Temporal clue: before means action preceding decision","Context: listening to team opinions means thoughtful approach","studied all reports so option (c)"]',
            tags="temporal", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q134
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.5,
            text_ar="If governments do not maintain balance between industrial development and environmental _____, they will face dire consequences.",
            option_a="protection", option_b="destruction", option_c="pollution", option_d="damage",
            correct_option="a",
            explanation_ar="Conditional clue: if do not maintain balance means between development and protection.",
            solution_steps_ar='["Clue: balance between development and...","Environment needs protection","environmental protection so option (a)"]',
            tags="condition", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q135
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.5,
            text_ar="Although artificial intelligence provides enormous _____ in productivity, it raises concerns about privacy and security.",
            option_a="losses", option_b="gains", option_c="damages", option_d="decline",
            correct_option="b",
            explanation_ar="Contrast clue: although...but means contrast. Second part negative: concerns means First part positive: enormous gains.",
            solution_steps_ar='["Conjunction: although...but means contrast","Second part negative: concerns","First part positive: enormous gains so option (b)"]',
            tags="contrast", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q136
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.5,
            text_ar="Inflation is defined as the continuous rise in the _____ of goods and services, which reduces the currency's purchasing power.",
            option_a="quality", option_b="prices", option_c="quantity", option_d="sizes",
            correct_option="b",
            explanation_ar="Definition clue: Inflation equals rise in prices of goods.",
            solution_steps_ar='["Type of clue: economic definition (is defined as)","Inflation is associated with rise","rising prices of goods and services so option (b)"]',
            tags="definition", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q137
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.5,
            text_ar="When the team lost its key player due to injury, his performance _____ significantly in the second half.",
            option_a="improved", option_b="declined", option_c="stabilized", option_d="excelled",
            correct_option="b",
            explanation_ar="Cause clue: losing key player means declined performance.",
            solution_steps_ar='["Clue: losing key player means negative impact","Result must be negative","declined performance so option (b)"]',
            tags="cause-effect", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q138
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.5,
            text_ar="Saudi Vision 2030 aims to _____ the Saudi economy away from total dependence on oil.",
            option_a="link", option_b="diversify", option_c="restrict", option_d="limit",
            correct_option="b",
            explanation_ar="Context: Vision 2030 plus reducing dependence on oil means diversify economy.",
            solution_steps_ar='["Clue: Vision 2030 plus reducing dependence on oil","Required: multiple income sources","diversify economy so option (b)"]',
            tags="definition", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q139
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.5,
            text_ar="As soon as the company announced its _____ of the new product, customers rushed to place their orders.",
            option_a="withdrawal", option_b="cancellation", option_c="launch", option_d="destruction",
            correct_option="c",
            explanation_ar="Temporal clue: as soon as...until means announcement precedes customers rushing means launch of product.",
            solution_steps_ar='["Temporal clue: as soon as...until means sequence","Result: customers rushing means positive event","launch of new product so option (c)"]',
            tags="temporal", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q140
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.6,
            text_ar="The leader was not only _____ in his decisions but also characterized by humility and respect for his subordinates' opinions.",
            option_a="hesitant", option_b="decisive", option_c="weak", option_d="lenient",
            correct_option="b",
            explanation_ar="Tone matching clue: humility plus respect means positive characteristics so decisive is positive leadership characteristic.",
            solution_steps_ar='["Clue: not only...but also means two co-occurring characteristics","Second characteristic positive: humility plus respect","First characteristic positive: decisive so option (b)"]',
            tags="tone-matching", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q141
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.6,
            text_ar="While some countries rely on nuclear energy, others prefer _____ to renewable energy sources like sun and wind.",
            option_a="returning", option_b="transitioning", option_c="retreating", option_d="withdrawing",
            correct_option="b",
            explanation_ar="Contrast clue: while means comparison between two options means transitioning to renewable energy.",
            solution_steps_ar='["Conjunction: while means comparison","Alternative option: renewable energy sources","transitioning to new sources so option (b)"]',
            tags="contrast", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q142
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.6,
            text_ar="Studies have proven that _____ sleep hours leads to weak concentration and _____ ability to make sound decisions.",
            option_a="increasing / enhancing", option_b="lack / decline", option_c="regulating / improving", option_d="excess / raising",
            correct_option="b",
            explanation_ar="Double clue: leads to weak concentration means negative cause means lack of sleep and decline in ability.",
            solution_steps_ar='["Result negative: weak concentration","First blank: negative cause means lack of sleep hours","Second blank: negative result means decline in ability so option (b)"]',
            tags="cause-effect", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q143
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.6,
            text_ar="The goal of education is not to _____ information in students' minds but to develop critical thinking and creativity.",
            option_a="build", option_b="cram", option_c="enhance", option_d="enrich",
            correct_option="b",
            explanation_ar="Contrast clue: not...but means developing thinking (positive) vs cramming information (negative).",
            solution_steps_ar='["Conjunction: not...but means contrast","True goal: developing thinking (positive)","Rejected goal: cramming information (negative) so option (b)"]',
            tags="contrast", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q144
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.6,
            text_ar="Due to the _____ climatic conditions in that region, residents resorted to building underground homes for protection.",
            option_a="moderation", option_b="severity", option_c="gentleness", option_d="kindness",
            correct_option="b",
            explanation_ar="Cause clue: due to means building underground for protection means due to severity of climate.",
            solution_steps_ar='["Conjunction: due to means cause","Result: building underground homes means protection","Cause: severity of climatic conditions so option (b)"]',
            tags="cause-effect", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q145
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.6,
            text_ar="Civilized dialogue represents an effective tool for _____ the cultural gap between peoples and enhancing mutual understanding.",
            option_a="widening", option_b="deepening", option_c="bridging", option_d="inflaming",
            correct_option="c",
            explanation_ar="Positive context: civilized dialogue plus enhancing mutual understanding means bridging the gap.",
            solution_steps_ar='["Clue: civilized dialogue plus mutual understanding (positive)","Cultural gap means problem to be solved","bridging the gap means eliminating the gap so option (c)"]',
            tags="tone-matching", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q146
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.6,
            text_ar="Whenever the employee adheres to work ethics and respects internal _____, he gains the trust of his superiors and colleagues.",
            option_a="chaos", option_b="violations", option_c="regulations", option_d="offenses",
            correct_option="c",
            explanation_ar="Conditional clue: whenever adheres means positive result (trust) means adherence to ethics plus respecting regulations.",
            solution_steps_ar='["Conjunction: whenever means condition","Positive result: trust of superiors and colleagues","Adherence to ethics plus respecting regulations so option (c)"]',
            tags="condition", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q147
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.6,
            text_ar="Emotional intelligence is the ability to _____ self and others' emotions and _____ dealing with them effectively.",
            option_a="suppress / reject", option_b="recognize / excel", option_c="ignore / mistreat", option_d="deny / fail",
            correct_option="b",
            explanation_ar="Double definition clue: Emotional intelligence equals recognizing emotions plus excelling in dealing.",
            solution_steps_ar='["Type of clue: definition (is the ability to...)","First blank: understanding emotions means recognize","Second blank: effective dealing means excel so option (b)"]',
            tags="definition", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q148
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.6,
            text_ar="After years of research and experimentation, the medical team finally _____ in developing an effective vaccine against the disease.",
            option_a="failed", option_b="failed", option_c="succeeded", option_d="retreated",
            correct_option="c",
            explanation_ar="Temporal clue: after years plus finally means achieving goal means team succeeded.",
            solution_steps_ar='["Temporal clue: after years plus finally means achievement","Result: developing effective vaccine (positive)","medical team succeeded so option (c)"]',
            tags="temporal", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q149
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.6,
            text_ar="The deeper a person studies the universe, the more _____ they become before the greatness of the Creator.",
            option_a="arrogant", option_b="proud", option_c="reverent", option_d="denying",
            correct_option="c",
            explanation_ar="Cause clue: the deeper means increased X before greatness of Creator means reverence.",
            solution_steps_ar='["Relationship: the more means proportional relationship","Result related to greatness of Creator and creation","increased reverence so option (c)"]',
            tags="cause-effect", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q150
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.6,
            text_ar="If a person spends _____ in planning their future and _____ in execution, they would achieve their goals easily.",
            option_a="sufficient time / sincere effort", option_b="little money / wasted time", option_c="much talk / flimsy excuse", option_d="sterile debate / sharp disagreement",
            correct_option="a",
            explanation_ar="Double conditional clue: if...would achieve means planning plus execution means sufficient time and sincere effort.",
            solution_steps_ar='["Conjunction: if...would achieve means condition and result","Condition must lead to achieving goals","sufficient time in planning plus sincere effort in execution so option (a)"]',
            tags="condition", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q151
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.6,
            text_ar="The scientific approach is characterized by _____ and avoiding preconceived judgments and personal impressions.",
            option_a="subjectivity", option_b="emotionality", option_c="objectivity", option_d="bias",
            correct_option="c",
            explanation_ar="Tone matching clue: avoiding preconceived judgments and impressions means objectivity.",
            solution_steps_ar='["Clue: avoiding preconceived judgments and personal impressions","Appropriate characteristic for scientific approach","objectivity so option (c)"]',
            tags="tone-matching", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q152
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.7,
            text_ar="Despite the _____ of financial resources available for the project, the team with their creative _____ managed to achieve results exceeding expectations.",
            option_a="abundance / their excuses", option_b="scarcity / their solutions", option_c="plenty / their problems", option_d="massiveness / their justifications",
            correct_option="b",
            explanation_ar="Double contrast clue: despite means scarcity of resources (negative) but their creative solutions saved the project.",
            solution_steps_ar='["Conjunction: despite means contrast","First blank: obstacle means scarcity of resources","Second blank: what saved project means their creative solutions so option (b)"]',
            tags="contrast", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q153
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.7,
            text_ar="The principle of rule of law is defined as the _____ of all individuals and institutions to legal rulings without discrimination or exception.",
            option_a="transcending", option_b="submission", option_c="resistance", option_d="rejection",
            correct_option="b",
            explanation_ar="Definition clue: rule of law means submission of all to its rulings without discrimination.",
            solution_steps_ar='["Type of clue: legal definition (is defined as)","Rule of law equals authority of law over all","submission of all to its rulings so option (b)"]',
            tags="definition", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q154
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.7,
            text_ar="When the company realized that rapid technological _____ might threaten its market position, it promptly _____ its research and development budget.",
            option_a="developments / reduced", option_b="developments / doubled", option_c="crises / canceled", option_d="losses / froze",
            correct_option="b",
            explanation_ar="Double clue: threat of developments means positive reaction: doubling research budget.",
            solution_steps_ar='["First blank: what threatens position means technological developments","Reaction: positive initiative","Second blank: doubling research budget so option (b)"]',
            tags="cause-effect", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q155
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.7,
            text_ar="If the _____ of the ozone layer continues at this rate, Earth will be exposed to dangerous levels of ultraviolet radiation.",
            option_a="recovery", option_b="renewal", option_c="depletion", option_d="solidity",
            correct_option="c",
            explanation_ar="Conditional clue: if continues means dangerous result means negative cause: depletion of ozone layer.",
            solution_steps_ar='["Conjunction: if means condition","Result: dangerous levels of radiation (negative)","Negative cause: depletion of ozone layer so option (c)"]',
            tags="condition", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q156
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.7,
            text_ar="As soon as negotiations between the two conflicting parties _____, a comprehensive ceasefire was announced and humanitarian aid began to arrive.",
            option_a="collapsed", option_b="stalled", option_c="succeeded", option_d="failed",
            correct_option="c",
            explanation_ar="Temporal clue: as soon as means event preceding ceasefire means negotiations succeeded to agreement.",
            solution_steps_ar='["Temporal clue: as soon as means immediate sequence","Positive result: comprehensive ceasefire plus aid","negotiations succeeded so option (c)"]',
            tags="temporal", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q157
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.7,
            text_ar="While the previous generation tends to _____ inherited customs, the new generation seeks renewal and development.",
            option_a="adhere to", option_b="abandon", option_c="disdain", option_d="scorn",
            correct_option="a",
            explanation_ar="Contrast clue: while means old generation opposite of new means adhering to customs vs renewal.",
            solution_steps_ar='["Conjunction: while means contrast between two generations","New generation: renewal and development","Previous generation: adhering to inherited customs so option (a)"]',
            tags="contrast", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q158
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.7,
            text_ar="Clinical trials have proven that the new drug not only _____ disease symptoms but also targets the _____ causing it.",
            option_a="relieves / roots", option_b="amplifies / results", option_c="neglects / evidence", option_d="hides / advantages",
            correct_option="a",
            explanation_ar="Double escalation clue: not only...but also means relieving symptoms plus targeting the roots.",
            solution_steps_ar='["Conjunction: not only...but also means escalation","First blank: minimum means relieving symptoms","Second blank: deeper goal means roots causing so option (a)"]',
            tags="cause-effect", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q159
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.7,
            text_ar="If ancient civilizations had not _____ irrigation and agriculture systems, great cities would not have been built on riverbanks.",
            option_a="neglected", option_b="destroyed", option_c="innovated", option_d="canceled",
            correct_option="c",
            explanation_ar="Conditional clue: if had not...would not means innovating irrigation is condition for building cities.",
            solution_steps_ar='["Conjunction: if had not...would not means conditional prevention","Result: cities built on riverbanks","Condition: innovating irrigation and agriculture systems so option (c)"]',
            tags="condition", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q160
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.7,
            text_ar="Ibn Khaldun's introduction was characterized by _____ of presentation and depth of analysis, making it a fundamental reference in sociology.",
            option_a="superficiality", option_b="weakness", option_c="originality", option_d="crudeness",
            correct_option="c",
            explanation_ar="Tone matching clue: depth of analysis plus fundamental reference means originality of presentation.",
            solution_steps_ar='["Tone is positive: depth of analysis plus fundamental reference","Appropriate characteristic is positive and complementary","originality of presentation so option (c)"]',
            tags="tone-matching", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q161
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.7,
            text_ar="Since the university _____ its scholarship program, the number of outstanding students enrolled has increased significantly.",
            option_a="canceled", option_b="suspended", option_c="launched", option_d="reduced",
            correct_option="c",
            explanation_ar="Temporal and causal clue: since means event causing increase means launched scholarship program.",
            solution_steps_ar='["Clue: since means beginning of positive change","Result: increase in number of outstanding students","Cause: launched scholarship program so option (c)"]',
            tags="temporal", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q162
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.8,
            text_ar="If _____ health institutions with qualified personnel represents a challenge in remote areas, then _____ remote medical technologies may help bridge this gap.",
            option_a="flooding / reducing", option_b="providing / employing", option_c="closing / canceling", option_d="emptying / disabling",
            correct_option="b",
            explanation_ar="Double clue: challenge plus solution means providing institutions with personnel (challenge) and employing technologies (solution).",
            solution_steps_ar='["First blank: challenge in remote areas means providing with personnel","Second blank: proposed solution means employing medical technologies","providing / employing so option (b)"]',
            tags="condition", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q163
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.8,
            text_ar="Although the theory of linguistic evolution provided a _____ explanation for the origin of human languages, it failed to explain the phenomenon of linguistic _____ among isolated communities.",
            option_a="convincing / similarity", option_b="weak / difference", option_c="flimsy / matching", option_d="rejected / diversity",
            correct_option="a",
            explanation_ar="Double contrast clue: although...but means convincing explanation but failed to explain similarity.",
            solution_steps_ar='["Conjunction: although...but means contrast","First part positive: convincing explanation","Second part: failed to explain linguistic similarity so option (a)"]',
            tags="contrast", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # Q164
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.8,
            text_ar="Because the scientific experiment showed that _____ cortisol levels in the blood are closely linked to _____ cognitive abilities, researchers recommended relaxation techniques.",
            option_a="decrease / improvement", option_b="increase / deterioration", option_c="stability / decline", option_d="disappearance / absence",
            correct_option="b",
            explanation_ar="Double causal clue: cortisol (stress hormone) plus recommendation for relaxation means increase in cortisol causes deterioration of cognition.",
            solution_steps_ar='["Recommendation: relaxation techniques means psychological pressure problem","First blank: increase in stress hormone","Second blank: deterioration of cognitive abilities so option (b)"]',
            tags="cause-effect", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # Q165
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.8,
            text_ar="While automation achieves tangible _____ in production costs, it simultaneously raises widespread _____ about the future of human labor market.",
            option_a="increases / optimism", option_b="savings / concerns", option_c="losses / hopes", option_d="burdens / joy",
            correct_option="b",
            explanation_ar="Double contrast clue: while...but means savings (positive) vs concerns (negative).",
            solution_steps_ar='["Conjunction: while...but means contrast","First part: positive means savings in costs","Second part: negative means concerns about labor market so option (b)"]',
            tags="contrast", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # Q166
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.8,
            text_ar="Transition to knowledge economy requires _____ the education system to keep pace with digital age requirements, as well as _____ an environment encouraging innovation and entrepreneurship.",
            option_a="freezing / dismantling", option_b="reforming / preparing", option_c="neglecting / undermining", option_d="disabling / combating",
            correct_option="b",
            explanation_ar="Double positive clue: knowledge economy means reforming education and preparing innovation environment.",
            solution_steps_ar='["Context: positive transition to knowledge economy","First blank: developing education means reforming","Second blank: supporting innovation means preparing environment so option (b)"]',
            tags="definition", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # Q167
        Question(skill_id="verbal_completion", question_type="completion", difficulty=0.8,
            text_ar="Had the International Court not been _____ by the conclusive evidence presented by the prosecution, a verdict of _____ would not have been issued against the defendants accused of war crimes.",
            option_a="convinced / conviction", option_b="doubted / acquittal", option_c="rejected / execution", option_d="ignored / pardon",
            correct_option="a",
            explanation_ar="Double conditional clue: had not...would not means court convinced by evidence leads to conviction verdict.",
            solution_steps_ar='["Conjunction: had not...would not means conditional prevention","First blank: what the court did means convinced by evidence","Second blank: type of verdict means conviction so option (a)"]',
            tags="cause-effect", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

    ]
