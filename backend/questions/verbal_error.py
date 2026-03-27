from models import Question

def get_questions():
    return [
        # ════════════════════════════════════════════════════════════════
        # 20 Existing questions
        # ════════════════════════════════════════════════════════════════

        # --- Existing #1 (difficulty 0.4) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.4,
            text_ar="We must preserve the environment because it (harms) human health and provides natural resources.",
            option_a="preserve", option_b="harms", option_c="health", option_d="resources",
            correct_option="b",
            explanation_ar="Contextual error: 'harms' - The context speaks of environmental benefits (preservation + providing resources). Correct: 'benefits' or 'helps'.",
            solution_steps_ar='["Read the sentence and understand context: environment is beneficial","Identify contradiction: harms contradicts preservation and resources","Correct: benefits or helps"]',
            tags="positive-negative", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- Existing #2 (difficulty 0.5) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.5,
            text_ar="Make exercise a daily habit as it (increases) blood pressure and improves overall mood.",
            option_a="habit", option_b="increases", option_c="pressure", option_d="mood",
            correct_option="b",
            explanation_ar="Contextual error: 'increases' - The context is positive (habit + improves mood), and increased blood pressure is a negative effect. Correct: 'reduces' blood pressure.",
            solution_steps_ar='["Context is positive: daily exercise habit + improves mood","Increases blood pressure = negative effect contradicting context","Correct: reduces"]',
            tags="positive-negative", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- Existing #3 (difficulty 0.6) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.6,
            text_ar="Regular reading (weakens) mental abilities and increases knowledge and culture.",
            option_a="Regular", option_b="weakens", option_c="abilities", option_d="knowledge",
            correct_option="b",
            explanation_ar="Contextual error: 'weakens' - Context is positive: Regular reading + increases knowledge. Correct: 'strengthens' or 'enhances'.",
            solution_steps_ar='["Context is positive: increases knowledge and culture","Weakens abilities = negative contradicting context","Correct: strengthens or enhances"]',
            tags="positive-negative", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- Existing #4 (difficulty 0.2) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.2,
            text_ar="The sun is considered a main source of (darkness) on Earth's surface, and without it life cannot continue.",
            option_a="sun", option_b="darkness", option_c="earth", option_d="life",
            correct_option="b",
            explanation_ar="Contextual error: 'darkness' - The sun is a source of light and energy, not darkness. Supporting evidence: 'without it life cannot continue' confirms it is positive. Correct: 'light' or 'illumination'.",
            solution_steps_ar='["Context: sun is essential for life","Evidence: without it life cannot continue","Identify contradiction: source of darkness","Correct: source of light"]',
            tags="positive-negative", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # --- Existing #5 (difficulty 0.3) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.3,
            text_ar="A child learns language from (isolation) from others, as they acquire it through listening and imitation.",
            option_a="learns", option_b="isolation", option_c="listening", option_d="imitation",
            correct_option="b",
            explanation_ar="Contextual error: 'isolation' - The context speaks of learning from others (listening and imitation), and isolation contradicts that. Correct: 'interaction' or 'contact'.",
            solution_steps_ar='["Read sentence: child learns language from others","Evidence: acquires through listening and imitation","Isolation contradicts interaction"]',
            tags="positive-negative", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # --- Existing #6 (difficulty 0.3) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.3,
            text_ar="The driver must follow traffic rules to maintain (exposing) people's lives to danger.",
            option_a="driver", option_b="following", option_c="exposing", option_d="people",
            correct_option="c",
            explanation_ar="Contextual error: 'exposing' - The context is positive (following + maintaining). Correct: 'safety' or 'protection'.",
            solution_steps_ar='["Context: following traffic rules to maintain","Positive context: following + maintaining","Exposing lives to danger contradicts context"]',
            tags="positive-negative", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- Existing #7 (difficulty 0.5) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.5,
            text_ar="Volunteering contributes to building society and promoting values of (selfishness) and giving among its members.",
            option_a="volunteering", option_b="building", option_c="selfishness", option_d="giving",
            correct_option="c",
            explanation_ar="Contextual error: 'selfishness' - Volunteering promotes positive values. Correct: 'altruism' or 'cooperation'.",
            solution_steps_ar='["Context: Volunteering promotes values and giving","Selfishness contradicts giving","Correct: altruism"]',
            tags="positive-negative", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- Existing #8 (difficulty 0.5) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.5,
            text_ar="The student achieved first place thanks to (neglecting) and persevering throughout the academic year.",
            option_a="achieved", option_b="neglecting", option_c="persevering", option_d="academic",
            correct_option="b",
            explanation_ar="Contextual error: 'neglecting' - Context is positive (first place + perseverance). Correct: 'diligence' or 'hard work'.",
            solution_steps_ar='["Context: achieved first place thanks to perseverance","Neglect contradicts success","Correct: diligence"]',
            tags="positive-negative", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- Existing #9 (difficulty 0.6) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.6,
            text_ar="Saudi Arabia is distinguished by its (isolated) geographical location that connects three continents and makes it a global commercial center.",
            option_a="distinguished", option_b="isolated", option_c="connects", option_d="commercial",
            correct_option="b",
            explanation_ar="Contextual error: 'isolated' - The context describes a location connecting continents. Correct: 'strategic' or 'distinguished'.",
            solution_steps_ar='["Sentence: location that connects three continents","Isolation contradicts connection","Correct: strategic"]',
            tags="context-contradiction", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- Existing #10 (difficulty 0.7) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.7,
            text_ar="Constructive dialogue is one of the most important means of (deepening) disputes between peoples and achieving mutual understanding.",
            option_a="dialogue", option_b="deepening", option_c="peoples", option_d="understanding",
            correct_option="b",
            explanation_ar="Contextual error: 'deepening' - Constructive dialogue aims to resolve disputes. Correct: 'resolving' or 'bridging'.",
            solution_steps_ar='["Context: Constructive dialogue + achieve understanding","Deepening disputes contradicts constructive dialogue","Correct: resolving"]',
            tags="positive-negative", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # --- Existing #11 (difficulty 0.7) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.7,
            text_ar="Doctors advise eating plenty of fruits and vegetables because they (deprive) the body of essential vitamins and minerals.",
            option_a="advise", option_b="plenty", option_c="deprive", option_d="essential",
            correct_option="c",
            explanation_ar="Contextual error: 'deprive' - The context is positive (advise + plenty). Fruits and vegetables provide vitamins. Correct: 'provide' or 'supply'.",
            solution_steps_ar='["Context: advise eating plenty of fruits","Advice implies benefit","Deprive contradicts advice"]',
            tags="positive-negative", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # --- Existing #12 (difficulty 0.8) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.8,
            text_ar="Precise scientific research requires (rushing) in collecting and analyzing data to reach reliable results.",
            option_a="requires", option_b="rushing", option_c="analyzing", option_d="reliable",
            correct_option="b",
            explanation_ar="Contextual error: 'rushing' - Precise research requires deliberation. Correct: 'deliberation' or 'precision'.",
            solution_steps_ar='["Context: Precise research + reliable results","Rushing contradicts precision","Correct: deliberation"]',
            tags="semantic-mismatch", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # --- Existing #13 (difficulty 0.2) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.2,
            text_ar="A successful teacher is keen on (frustrating) students and encouraging them to continue learning.",
            option_a="keen", option_b="frustrating", option_c="encouraging", option_d="continuous",
            correct_option="b",
            explanation_ar="Contextual error: 'frustrating' - Context is positive (keen + encouraging). Correct: 'motivating'.",
            solution_steps_ar='["Context: keen + encouraging + learning","Frustrating contradicts encouraging","Correct: motivating"]',
            tags="positive-negative", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # --- Existing #14 (difficulty 0.25) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.2,
            text_ar="Regular exercise (destroys) body health and strengthens muscles and bones.",
            option_a="exercise", option_b="destroys", option_c="health", option_d="bones",
            correct_option="b",
            explanation_ar="Contextual error: 'destroys' - Context is positive (strengthens muscles). Correct: 'enhances' or 'improves'.",
            solution_steps_ar='["Context: strengthens muscles and bones","Destroys contradicts strengthening","Correct: enhances"]',
            tags="positive-negative", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # --- Existing #15 (difficulty 0.3) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.3,
            text_ar="Honesty (distances) people from you and makes them trust and respect you.",
            option_a="honesty", option_b="distances", option_c="trust", option_d="respect",
            correct_option="b",
            explanation_ar="Contextual error: 'distances' - Context is positive (trust + respect). Correct: 'brings closer'.",
            solution_steps_ar='["Results: trust + respect = positive","Distances contradicts these results","Correct: brings closer"]',
            tags="positive-negative", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # --- Existing #16 (difficulty 0.5) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.5,
            text_ar="When a student (masters) their academic skills, they (regress) in results and achieve highest grades.",
            option_a="masters", option_b="skills", option_c="regress", option_d="grades",
            correct_option="c",
            explanation_ar="Contextual error: 'regress' - Mastery + highest grades = positive context. Correct: 'advance' or 'excel'.",
            solution_steps_ar='["Premise: masters skills","Result: highest grades","Regress contradicts highest grades"]',
            tags="positive-negative", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- Existing #17 (difficulty 0.5) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.5,
            text_ar="A leader should listen to subordinates' opinions and ignore (their suggestions) to achieve organizational success.",
            option_a="leader", option_b="subordinates'", option_c="their suggestions", option_d="organization",
            correct_option="c",
            explanation_ar="Contextual error: 'ignore their suggestions' - Context calls for listening. Correct: 'adopt their suggestions'.",
            solution_steps_ar='["Action: listens","Ignoring contradicts listening","Goal: success requires adopting suggestions"]',
            tags="positive-negative", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- Existing #18 (difficulty 0.6) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.6,
            text_ar="A researcher must be objective and (biased) in analyzing data to reach accurate results.",
            option_a="researcher", option_b="objectivity", option_c="biased", option_d="accurate",
            correct_option="c",
            explanation_ar="Contextual error: 'biased' - Context demands objectivity and accuracy. Correct: 'be neutral' or 'not be biased'.",
            solution_steps_ar='["Context requires: objectivity + accurate results","Biased contradicts objectivity","Correct: be neutral"]',
            tags="semantic-mismatch", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- Existing #19 (difficulty 0.7) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.7,
            text_ar="Austerity policy contributed to (reducing) spending, but led to (raising) service levels for citizens.",
            option_a="reducing", option_b="spending", option_c="raising", option_d="provided",
            correct_option="c",
            explanation_ar="Contextual error: 'raising' - Austerity = reducing spending. Word 'but' indicates negative result. Correct: 'reducing' or 'decline'.",
            solution_steps_ar='["Austerity = reducing spending","But indicates negative result","Raising contradicts austerity"]',
            tags="positive-negative", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # --- Existing #20 (difficulty 0.8) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.8,
            text_ar="The more population (increases), the (demand) for housing (decreases) and real estate prices rise.",
            option_a="increases", option_b="decreases", option_c="housing", option_d="real estate",
            correct_option="b",
            explanation_ar="Contextual error: 'decreases' demand - Population increase leads to increased demand. Correct: 'increases'.",
            solution_steps_ar='["Relationship: population increase leads to demand increase","Rising prices confirms increased demand","Decreases contradicts this logic"]',
            tags="context-contradiction", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),


        # ════════════════════════════════════════════════════════════════
        # 91 New questions (Q21-Q111)
        # ════════════════════════════════════════════════════════════════

        # --- New #21 (0.2) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.2,
            text_ar="Knowledge is the key to (ignorance) and progress in the lives of nations.",
            option_a="knowledge", option_b="ignorance", option_c="progress", option_d="nations",
            correct_option="b",
            explanation_ar="Contextual error: 'ignorance' - Knowledge leads to progress, not ignorance. Correct: 'knowledge' or 'success'.",
            solution_steps_ar='["Context: knowledge + progress + nations","Ignorance contradicts knowledge","Correct: knowledge"]',
            tags="positive-negative", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # --- New #22 (0.2) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.2,
            text_ar="Water is necessary (to harm) the human body and maintain vital functions.",
            option_a="to harm", option_b="water", option_c="human", option_d="vital",
            correct_option="a",
            explanation_ar="Contextual error: 'to harm' - Water benefits the body. Correct: 'for health'.",
            solution_steps_ar='["Context: necessary + maintaining vital functions","To harm contradicts necessity","Correct: for health"]',
            tags="positive-negative", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # --- New #23 (0.2) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.2,
            text_ar="Trees contribute to (polluting) the air and providing shade and oxygen.",
            option_a="trees", option_b="polluting", option_c="shade", option_d="living",
            correct_option="b",
            explanation_ar="Contextual error: 'polluting' - Trees purify air. Correct: 'purifying'.",
            solution_steps_ar='["Context: providing shade and oxygen","Polluting contradicts role of trees","Correct: purifying"]',
            tags="positive-negative", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # --- New #24 (0.2) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.2,
            text_ar="We should respect elderly and appreciate (mistreating them) and their role in society.",
            option_a="respect", option_b="appreciate", option_c="society", option_d="mistreating them",
            correct_option="d",
            explanation_ar="Contextual error: 'mistreating them' - Context calls for respect. Correct: 'their efforts'.",
            solution_steps_ar='["Context: respect + appreciate + building society","Mistreating contradicts respect","Correct: their efforts"]',
            tags="positive-negative", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # --- New #25 (0.2) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.2,
            text_ar="Work success requires (laziness), perseverance, and good planning.",
            option_a="success", option_b="laziness", option_c="perseverance", option_d="planning",
            correct_option="b",
            explanation_ar="Contextual error: 'laziness' - Success requires positive traits. Correct: 'diligence'.",
            solution_steps_ar='["Context: success + perseverance + planning","Laziness contradicts success requirements","Correct: diligence"]',
            tags="positive-negative", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # --- New #26 (0.2) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.2,
            text_ar="Football promotes (enmity) and cooperation among players.",
            option_a="enmity", option_b="beloved", option_c="promotes", option_d="cooperation",
            correct_option="a",
            explanation_ar="Contextual error: 'enmity' - Context speaks of beloved sport and cooperation. Correct: 'teamwork'.",
            solution_steps_ar='["Context: beloved + promotes + cooperation","Enmity contradicts cooperation","Correct: teamwork"]',
            tags="positive-negative", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # --- New #27 (0.2) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.2,
            text_ar="A cohesive family is the foundation of (disintegration), stability, and progress.",
            option_a="family", option_b="stability", option_c="progress", option_d="disintegration",
            correct_option="d",
            explanation_ar="Contextual error: 'disintegration' - Cohesive family builds stability. Correct: 'cohesion'.",
            solution_steps_ar='["Context: cohesive + stability + progress","Disintegration contradicts cohesion","Correct: cohesion"]',
            tags="positive-negative", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # --- New #28 (0.2) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.2,
            text_ar="A book is the best (enemy) of man, enriching his mind and expanding horizons.",
            option_a="book", option_b="enemy", option_c="enriches", option_d="horizons",
            correct_option="b",
            explanation_ar="Contextual error: 'enemy' - Context describes benefits. Correct: 'friend'.",
            solution_steps_ar='["Context: enriches mind + expands horizons","Enemy contradicts benefits","Correct: friend"]',
            tags="positive-negative", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # --- New #29 (0.3) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.3,
            text_ar="Technology helped in (hindering) communication and facilitating information exchange.",
            option_a="helped", option_b="communication", option_c="information", option_d="hindering",
            correct_option="d",
            explanation_ar="Contextual error: 'hindering' - Technology facilitates communication. Correct: 'facilitating'.",
            solution_steps_ar='["Context: helped + facilitating exchange","Hindering contradicts facilitation","Correct: facilitating"]',
            tags="positive-negative", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # --- New #30 (0.3) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.3,
            text_ar="Vision 2030 aims to (hinder) economic development and diversify income sources.",
            option_a="hinder", option_b="aims", option_c="development", option_d="national",
            correct_option="a",
            explanation_ar="Contextual error: 'hinder' - Vision seeks achievement. Correct: 'achieve'.",
            solution_steps_ar='["Context: aims + development + diversification","Hinder contradicts development goals","Correct: achieve"]',
            tags="positive-negative", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- New #31 (0.3) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.3,
            text_ar="New drugs (worsen) diseases and help patients recover.",
            option_a="discovered", option_b="patients", option_c="worsen", option_d="recovery",
            correct_option="c",
            explanation_ar="Contextual error: 'worsen' - Drugs treat diseases. Correct: 'treat'.",
            solution_steps_ar='["Context: new drugs + help recovery","Worsen contradicts recovery","Correct: treat"]',
            tags="semantic-mismatch", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- New #32 (0.3) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.3,
            text_ar="Humility (repels) people and earns love and respect.",
            option_a="humility", option_b="love", option_c="respect", option_d="repels",
            correct_option="d",
            explanation_ar="Contextual error: 'repels' - Humility earns positive traits. Correct: 'attracts'.",
            solution_steps_ar='["Context: noble trait + love + respect","Repels contradicts love","Correct: attracts"]',
            tags="positive-negative", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- New #33 (0.3) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.3,
            text_ar="Saving leads to (bankruptcy) and financial stability.",
            option_a="saving", option_b="wise", option_c="bankruptcy", option_d="future",
            correct_option="c",
            explanation_ar="Contextual error: 'bankruptcy' - Saving achieves stability. Correct: 'security'.",
            solution_steps_ar='["Context: wise habit + stability","Bankruptcy contradicts wise saving","Correct: security"]',
            tags="positive-negative", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- New #34 (0.3) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.3,
            text_ar="Travel (narrows) horizons and introduces diverse cultures.",
            option_a="narrows", option_b="travel", option_c="human", option_d="diverse",
            correct_option="a",
            explanation_ar="Contextual error: 'narrows' - Travel broadens horizons. Correct: 'of' or remove 'narrows'.",
            solution_steps_ar='["Context: broadens + diverse cultures","Narrows contradicts broadening","Correct: of horizons"]',
            tags="positive-negative", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- New #35 (0.3) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.3,
            text_ar="Organic fertilizer helps in (destroying) soil and increasing fertility.",
            option_a="fertilizer", option_b="destroying", option_c="fertility", option_d="productivity",
            correct_option="b",
            explanation_ar="Contextual error: 'destroying' - Fertilizer improves soil. Correct: 'improving'.",
            solution_steps_ar='["Context: helps + increasing fertility","Destroying contradicts help","Correct: improving"]',
            tags="positive-negative", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- New #36 (0.3) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.3,
            text_ar="Hand washing protects from (health) and infectious diseases.",
            option_a="washing", option_b="regularly", option_c="infectious", option_d="health",
            correct_option="d",
            explanation_ar="Contextual error: 'health' - Hand washing protects from diseases. Correct: 'infection'.",
            solution_steps_ar='["Context: protection from negative","Health is positive - not protected from","Correct: infection"]',
            tags="positive-negative", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- New #37 (0.3) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.3,
            text_ar="A distinguished teacher makes effort in (keeping students ignorant) and preparing them for future.",
            option_a="keeping ignorant", option_b="distinguished", option_c="makes effort", option_d="future",
            correct_option="a",
            explanation_ar="Contextual error: 'keeping ignorant' - Distinguished teacher educates. Correct: 'teaching'.",
            solution_steps_ar='["Context: distinguished + effort + preparation","Keeping ignorant contradicts distinction","Correct: teaching"]',
            tags="positive-negative", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- New #38 (0.3) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.3,
            text_ar="Recycling contributes to protecting environment and (depleting) natural resources.",
            option_a="recycling", option_b="contributes", option_c="protecting", option_d="depleting",
            correct_option="d",
            explanation_ar="Contextual error: 'depleting' - Recycling preserves resources. Correct: 'preserving'.",
            solution_steps_ar='["Context: recycling + protecting environment","Depleting contradicts protection","Correct: preserving"]',
            tags="positive-negative", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- New #39 (0.3) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.3,
            text_ar="Honesty earns (contempt) and appreciation from people.",
            option_a="honesty", option_b="great", option_c="contempt", option_d="appreciation",
            correct_option="c",
            explanation_ar="Contextual error: 'contempt' - Honesty earns trust. Correct: 'trust'.",
            solution_steps_ar='["Context: great trait + appreciation","Contempt = disdain, opposite of appreciation","Correct: trust"]',
            tags="semantic-mismatch", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),


        # --- New #40 (0.4) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.4,
            text_ar="The school library is a source (for misleading) students and enriching knowledge.",
            option_a="library", option_b="for misleading", option_c="enriching", option_d="diverse",
            correct_option="b",
            explanation_ar="Contextual error: 'for misleading' - Library educates students. Correct: 'for educating'.",
            solution_steps_ar='["Context: important source + enriching knowledge","Misleading contradicts library role","Correct: for educating"]',
            tags="positive-negative", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- New #41 (0.4) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.4,
            text_ar="Adequate sleep helps renew energy and (weaken) immunity to resist diseases.",
            option_a="weaken", option_b="adequate", option_c="renew", option_d="diseases",
            correct_option="a",
            explanation_ar="Contextual error: 'weaken' - Sleep strengthens immunity. Correct: 'strengthening'.",
            solution_steps_ar='["Context: adequate sleep + renew energy + resist diseases","Weaken contradicts resistance","Correct: strengthening"]',
            tags="positive-negative", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- New #42 (0.4) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.4,
            text_ar="Internet contributed to (restricting) access to information and providing it to millions.",
            option_a="contributed", option_b="information", option_c="restricting", option_d="users",
            correct_option="c",
            explanation_ar="Contextual error: 'restricting' - Internet expanded access. Correct: 'expanding'.",
            solution_steps_ar='["Context: contributed + providing to millions","Restricting contradicts provision","Correct: expanding"]',
            tags="positive-negative", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- New #43 (0.4) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.4,
            text_ar="Teamwork promotes (division) among colleagues and improves performance.",
            option_a="promotes", option_b="colleagues", option_c="team", option_d="division",
            correct_option="d",
            explanation_ar="Contextual error: 'division' - Teamwork promotes cooperation. Correct: 'cooperation'.",
            solution_steps_ar='["Context: promotes + improves performance","Division contradicts teamwork","Correct: cooperation"]',
            tags="positive-negative", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- New #44 (0.4) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.4,
            text_ar="Saudi Arabia cares about education as the pillar (for backwardness) of future generations.",
            option_a="cares", option_b="pillar", option_c="for backwardness", option_d="future",
            correct_option="c",
            explanation_ar="Contextual error: 'for backwardness' - Education enables progress. Correct: 'for progress'.",
            solution_steps_ar='["Context: care + education + pillar","Backwardness contradicts education","Correct: for progress"]',
            tags="positive-negative", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- New #45 (0.4) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.4,
            text_ar="Scientists seek to develop vaccines (to spread) epidemics and protect health.",
            option_a="seek", option_b="vaccines", option_c="to spread", option_d="health",
            correct_option="c",
            explanation_ar="Contextual error: 'to spread' - Vaccines combat epidemics. Correct: 'to combat'.",
            solution_steps_ar='["Context: develop vaccines + protect health","Spread contradicts protection","Correct: to combat"]',
            tags="positive-negative", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- New #46 (0.4) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.4,
            text_ar="A loyal employee is keen on (wasting) time in accomplishing tasks with excellence.",
            option_a="loyal", option_b="accomplishing", option_c="excellence", option_d="wasting",
            correct_option="d",
            explanation_ar="Contextual error: 'wasting' - Loyal employee invests time. Correct: 'investing'.",
            solution_steps_ar='["Context: loyal + keen + accomplishing + excellence","Wasting contradicts loyalty","Correct: investing"]',
            tags="positive-negative", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- New #47 (0.4) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.4,
            text_ar="Parent dialogue contributes to (widening) the gap and strengthening family bonds.",
            option_a="dialogue", option_b="gap", option_c="family", option_d="widening",
            correct_option="d",
            explanation_ar="Contextual error: 'widening' - Dialogue reduces gaps. Correct: 'narrowing'.",
            solution_steps_ar='["Context: dialogue + strengthening bonds","Widening contradicts strengthening","Correct: narrowing"]',
            tags="positive-negative", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- New #48 (0.4) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.4,
            text_ar="Daily reading (dulls) the mind and develops critical thinking.",
            option_a="dulls", option_b="reading", option_c="mind", option_d="critical",
            correct_option="a",
            explanation_ar="Contextual error: 'dulls' - Reading activates the mind. Correct: 'activates'.",
            solution_steps_ar='["Context: beneficial habit + develops thinking","Dulls contradicts development","Correct: activates"]',
            tags="positive-negative", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- New #49 (0.4) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.4,
            text_ar="E-commerce provided opportunities (to reduce) market size and increase choices.",
            option_a="to reduce", option_b="provided", option_c="markets", option_d="consumers",
            correct_option="a",
            explanation_ar="Contextual error: 'to reduce' - E-commerce expands markets. Correct: 'to expand'.",
            solution_steps_ar='["Context: opportunities + increase choices","Reduce contradicts expansion","Correct: to expand"]',
            tags="positive-negative", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- New #50 (0.4) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.4,
            text_ar="Travel gives opportunity for (closure) to new cultures and gaining experiences.",
            option_a="gives", option_b="cultures", option_c="rich", option_d="closure",
            correct_option="d",
            explanation_ar="Contextual error: 'closure' - Travel enables openness. Correct: 'openness'.",
            solution_steps_ar='["Context: gives + new cultures + experiences","Closure contradicts openness","Correct: openness"]',
            tags="positive-negative", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- New #51 (0.4) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.4,
            text_ar="Modern agriculture relies on technology (to destroy) crops and increase production.",
            option_a="relies", option_b="advanced", option_c="to destroy", option_d="food",
            correct_option="c",
            explanation_ar="Contextual error: 'to destroy' - Technology improves crops. Correct: 'to improve'.",
            solution_steps_ar='["Context: advanced technology + increase production","Destroy contradicts advancement","Correct: to improve"]',
            tags="positive-negative", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- New #52 (0.4) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.4,
            text_ar="Fulfilling promises (lowers) standing and raises esteem among people.",
            option_a="lower", option_b="fulfilling", option_c="standing", option_d="people",
            correct_option="a",
            explanation_ar="Contextual error: 'lowers' - Fulfilling promises raises standing. Correct: 'raises'.",
            solution_steps_ar='["Context: fulfilling promises + raises esteem","Lowers contradicts raising","Correct: raises"]',
            tags="positive-negative", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- New #53 (0.4) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.4,
            text_ar="Swimming is among best sports that (exhaust) the heart and improve fitness.",
            option_a="best", option_b="exhaust", option_c="heart", option_d="fitness",
            correct_option="b",
            explanation_ar="Contextual error: 'exhaust' - Swimming strengthens the heart. Correct: 'strengthens'.",
            solution_steps_ar='["Context: best sports + improve fitness","Exhaust contradicts excellence","Correct: strengthens"]',
            tags="positive-negative", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- New #54 (0.4) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.4,
            text_ar="Justice spreads (injustice) and stability in society.",
            option_a="justice", option_b="rule", option_c="injustice", option_d="stability",
            correct_option="c",
            explanation_ar="Contextual error: 'injustice' - Justice spreads security. Correct: 'security'.",
            solution_steps_ar='["Context: justice foundation + stability","Injustice contradicts justice","Correct: security"]',
            tags="positive-negative", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- New #55 (0.4) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.4,
            text_ar="AI helps in (complicating) medical procedures and speeding diagnosis.",
            option_a="intelligence", option_b="medical", option_c="diseases", option_d="complicating",
            correct_option="d",
            explanation_ar="Contextual error: 'complicating' - AI simplifies procedures. Correct: 'simplifying'.",
            solution_steps_ar='["Context: helps + speed up diagnosis","Complicating contradicts help and speed","Correct: simplifying"]',
            tags="positive-negative", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- New #56 (0.4) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.4,
            text_ar="NEOM aims to build a city that (hinders) innovation and provides ideal environment.",
            option_a="NEOM", option_b="future", option_c="hinders", option_d="ideal",
            correct_option="c",
            explanation_ar="Contextual error: 'hinders' - NEOM supports innovation. Correct: 'supports'.",
            solution_steps_ar='["Context: future city + ideal environment","Hinders contradicts project goal","Correct: supports"]',
            tags="positive-negative", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- New #57 (0.4) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.4,
            text_ar="Solar energy contributes to (destroying) environment and reducing emissions.",
            option_a="clean", option_b="renewable", option_c="destroying", option_d="harmful",
            correct_option="c",
            explanation_ar="Contextual error: 'destroying' - Solar energy protects environment. Correct: 'protecting'.",
            solution_steps_ar='["Context: clean + renewable + reducing emissions","Destroying contradicts cleanliness","Correct: protecting"]',
            tags="positive-negative", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- New #58 (0.4) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.4,
            text_ar="Obeying parents (angers) God and brings blessings in provision.",
            option_a="obeying", option_b="greatest", option_c="angers", option_d="blessings",
            correct_option="c",
            explanation_ar="Contextual error: 'angers' - Obeying pleases God. Correct: 'pleases'.",
            solution_steps_ar='["Context: greatest acts + blessings","Angers contradicts worship","Correct: pleases"]',
            tags="positive-negative", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),


        # --- New #59 (0.5) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.5,
            text_ar="Distance learning gave opportunity (to be deprived) of diverse digital sources.",
            option_a="learning", option_b="digital", option_c="to be deprived", option_d="diverse",
            correct_option="c",
            explanation_ar="Contextual error: 'to be deprived' - Distance learning enables access. Correct: 'to benefit'.",
            solution_steps_ar='["Context: opportunity + diverse sources","Deprived contradicts enablement","Correct: to benefit"]',
            tags="positive-negative", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- New #60 (0.5) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.5,
            text_ar="Vegetables are rich in fiber that (disrupts) digestion and improves performance.",
            option_a="disrupts", option_b="experts", option_c="fresh", option_d="performance",
            correct_option="a",
            explanation_ar="Contextual error: 'disrupts' - Fiber regulates digestion. Correct: 'regulates'.",
            solution_steps_ar='["Context: recommend + rich in fiber + improves","Disrupts contradicts improvement","Correct: regulates"]',
            tags="positive-negative", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- New #61 (0.5) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.5,
            text_ar="Tree planting reduces pollution and (spoils) urban quality of life.",
            option_a="planting", option_b="pollution", option_c="spoils", option_d="residents",
            correct_option="c",
            explanation_ar="Contextual error: 'spoils' - Trees improve quality of life. Correct: 'improves'.",
            solution_steps_ar='["Context: reduces pollution + quality","Spoils contradicts improvement","Correct: improves"]',
            tags="positive-negative", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- New #62 (0.5) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.5,
            text_ar="Smartphone apps helped in (delaying) transactions and saving time.",
            option_a="applications", option_b="transactions", option_c="citizens", option_d="delaying",
            correct_option="d",
            explanation_ar="Contextual error: 'delaying' - Apps speed up transactions. Correct: 'speeding up'.",
            solution_steps_ar='["Context: helped + saving time","Delaying contradicts saving","Correct: speeding up"]',
            tags="positive-negative", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- New #63 (0.5) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.5,
            text_ar="State builds hospitals (to deprive) citizens of medical care.",
            option_a="keen", option_b="hospitals", option_c="to deprive", option_d="necessary",
            correct_option="c",
            explanation_ar="Contextual error: 'to deprive' - Hospitals provide care. Correct: 'to provide'.",
            solution_steps_ar='["Context: keen + building hospitals + care","Deprive contradicts keenness","Correct: to provide"]',
            tags="positive-negative", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- New #64 (0.5) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.5,
            text_ar="Space exploration helps understand universe and (ignore) natural phenomena.",
            option_a="exploration", option_b="humanity", option_c="ignore", option_d="lives",
            correct_option="c",
            explanation_ar="Contextual error: 'ignore' - Exploration helps study phenomena. Correct: 'study'.",
            solution_steps_ar='["Context: helps + understand universe","Ignore contradicts understanding","Correct: study"]',
            tags="positive-negative", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- New #65 (0.5) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.5,
            text_ar="Training enables employee (to lose) new skills that enhance competence.",
            option_a="to lose", option_b="training", option_c="enhance", option_d="professional",
            correct_option="a",
            explanation_ar="Contextual error: 'to lose' - Training enables acquiring skills. Correct: 'to acquire'.",
            solution_steps_ar='["Context: training + enhance competence","Lose contradicts enablement","Correct: to acquire"]',
            tags="positive-negative", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- New #66 (0.5) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.5,
            text_ar="Daily walking is enough (to exhaust) body and improve circulation.",
            option_a="daily", option_b="circulation", option_c="to exhaust", option_d="mental",
            correct_option="c",
            explanation_ar="Contextual error: 'to exhaust' - Walking activates body. Correct: 'to activate'.",
            solution_steps_ar='["Context: enough + improve circulation","Exhaust contradicts improvement","Correct: to activate"]',
            tags="positive-negative", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- New #67 (0.5) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.5,
            text_ar="Cultural competitions contribute (to extinguishing) competitive spirit and motivating youth.",
            option_a="competitions", option_b="fair", option_c="research", option_d="to extinguishing",
            correct_option="d",
            explanation_ar="Contextual error: 'to extinguishing' - Competitions ignite spirit. Correct: 'igniting'.",
            solution_steps_ar='["Context: contribute + fair competition + motivation","Extinguishing contradicts motivation","Correct: igniting"]',
            tags="positive-negative", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- New #68 (0.5) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.5,
            text_ar="Small projects contribute to (stagnation) of economy and its growth.",
            option_a="projects", option_b="opportunities", option_c="stagnation", option_d="growth",
            correct_option="c",
            explanation_ar="Contextual error: 'stagnation' - Small projects revitalize economy. Correct: 'revival'.",
            solution_steps_ar='["Context: job opportunities + growth","Stagnation contradicts growth","Correct: revival"]',
            tags="positive-negative", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- New #69 (0.5) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.5,
            text_ar="Domestic tourism contributes to (decline) of tourism income.",
            option_a="decline", option_b="tourism", option_c="heritage", option_d="local",
            correct_option="a",
            explanation_ar="Contextual error: 'decline' - Domestic tourism raises income. Correct: 'increase'.",
            solution_steps_ar='["Context: introduce heritage + contribute to income","Decline contradicts contribution","Correct: increase"]',
            tags="positive-negative", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- New #70 (0.5) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.5,
            text_ar="Drip irrigation contributes to (wasting) water and preserving resources.",
            option_a="irrigation", option_b="modern", option_c="wasting", option_d="water",
            correct_option="c",
            explanation_ar="Contextual error: 'wasting' - Drip irrigation saves water. Correct: 'saving'.",
            solution_steps_ar='["Context: modern method + preserving resources","Wasting contradicts preservation","Correct: saving"]',
            tags="positive-negative", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- New #71 (0.5) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.5,
            text_ar="Forgiveness indicates (weakness) of self, elevation, and high aspiration.",
            option_a="forgiveness", option_b="noble", option_c="weakness", option_d="aspiration",
            correct_option="c",
            explanation_ar="Contextual error: 'weakness' - Forgiveness indicates strength. Correct: 'strength'.",
            solution_steps_ar='["Context: noble traits + elevation + aspiration","Weakness contradicts elevation","Correct: strength"]',
            tags="positive-negative", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- New #72 (0.3) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.3,
            text_ar="Raising children on independence helps in (depending on others) for themselves.",
            option_a="raising", option_b="independence", option_c="depending on others", option_d="confidence",
            correct_option="c",
            explanation_ar="Contextual error: 'depending on others' - Independence means self-reliance. Correct: 'self-reliance'.",
            solution_steps_ar='["Context: independence + facing challenges","Depending contradicts independence","Correct: self-reliance"]',
            tags="positive-negative", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- New #73 (0.5) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.5,
            text_ar="Entertainment sector contributes to (reducing) quality of life and happiness.",
            option_a="achievements", option_b="entertainment", option_c="reducing", option_d="happiness",
            correct_option="c",
            explanation_ar="Contextual error: 'reducing' - Entertainment raises quality of life. Correct: 'raising'.",
            solution_steps_ar='["Context: achievements + happiness","Reducing contradicts achievement","Correct: raising"]',
            tags="positive-negative", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- New #74 (0.3) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.3,
            text_ar="Self-learning enables (mental rigidity) and continuous development.",
            option_a="learning", option_b="skills", option_c="mental rigidity", option_d="continuous",
            correct_option="c",
            explanation_ar="Contextual error: 'mental rigidity' - Self-learning enables growth. Correct: 'growth'.",
            solution_steps_ar='["Context: important skills + continuous development","Rigidity contradicts development","Correct: growth"]',
            tags="positive-negative", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- New #75 (0.6) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.6,
            text_ar="Critical thinking helps with (dependence) in making decisions.",
            option_a="critical", option_b="instilled", option_c="dependence", option_d="information",
            correct_option="c",
            explanation_ar="Contextual error: 'dependence' - Critical thinking enables independence. Correct: 'independence'.",
            solution_steps_ar='["Context: basic skill + analyze information","Dependence contradicts critical thinking","Correct: independence"]',
            tags="positive-negative", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- New #76 (0.6) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.6,
            text_ar="Medical examination is effective (to delay) detecting diseases early.",
            option_a="periodic", option_b="to delay", option_c="early", option_d="worsen",
            correct_option="b",
            explanation_ar="Contextual error: 'to delay' - Examination accelerates detection. Correct: 'to accelerate'.",
            solution_steps_ar='["Context: effective + early stages + treatment","Delay contradicts early detection","Correct: to accelerate"]',
            tags="positive-negative", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # --- New #77 (0.6) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.6,
            text_ar="Strict laws on factories (encourage) pollution and protect health.",
            option_a="strict", option_b="factories", option_c="encourage", option_d="citizens",
            correct_option="c",
            explanation_ar="Contextual error: 'encourage' - Laws aim to limit pollution. Correct: 'to limit'.",
            solution_steps_ar='["Context: strict laws + protect health","Encourage contradicts strictness","Correct: to limit"]',
            tags="semantic-mismatch", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # --- New #78 (0.6) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.6,
            text_ar="Robots revolutionized industry with ability to (slow down) production lines.",
            option_a="revolution", option_b="production", option_c="human", option_d="slow down",
            correct_option="d",
            explanation_ar="Contextual error: 'slow down' - Robots speed up production. Correct: 'speed up'.",
            solution_steps_ar='["Context: revolution + increase accuracy","Slow down contradicts revolution","Correct: speed up"]',
            tags="positive-negative", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # --- New #79 (0.6) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.6,
            text_ar="Justice system aims to (reward) criminals and deter them.",
            option_a="system", option_b="reward", option_c="deter", option_d="crime",
            correct_option="b",
            explanation_ar="Contextual error: 'reward' - Justice aims to punish. Correct: 'punish'.",
            solution_steps_ar='["Context: justice + deter + protect","Reward contradicts deterrence","Correct: punish"]',
            tags="context-contradiction", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # --- New #80 (0.6) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.6,
            text_ar="Citizen Account program succeeded in (withdrawing) support from deserving families.",
            option_a="withdrawing", option_b="succeeded", option_c="deserving", option_d="economic",
            correct_option="a",
            explanation_ar="Contextual error: 'withdrawing' - Program provides support. Correct: 'providing'.",
            solution_steps_ar='["Context: succeeded + deserving + alleviating burdens","Withdrawing contradicts success","Correct: providing"]',
            tags="positive-negative", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # --- New #81 (0.6) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.6,
            text_ar="Antibiotics led to (spread) of bacterial diseases and saving lives.",
            option_a="invention", option_b="spread", option_c="bacterial", option_d="lives",
            correct_option="b",
            explanation_ar="Contextual error: 'spread' - Antibiotics reduced diseases. Correct: 'decline'.",
            solution_steps_ar='["Context: invention + saving lives","Spread contradicts saving","Correct: decline"]',
            tags="positive-negative", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # --- New #82 (0.6) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.6,
            text_ar="Comfortable work environment leads to (decline) in productivity and increased loyalty.",
            option_a="experts", option_b="comfortable", option_c="loyalty", option_d="decline",
            correct_option="d",
            explanation_ar="Contextual error: 'decline' - Comfortable environment raises productivity. Correct: 'increase'.",
            solution_steps_ar='["Context: comfortable + increased loyalty","Decline contradicts comfort","Correct: increase"]',
            tags="positive-negative", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),


        # --- New #83 (0.6) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.6,
            text_ar="Good parental role models leave (negative) effect on children development.",
            option_a="role models", option_b="negative", option_c="personality", option_d="noble",
            correct_option="b",
            explanation_ar="Contextual error: 'negative' - Good models leave positive effects. Correct: 'positive'.",
            solution_steps_ar='["Context: good + noble values","Negative contradicts good","Correct: positive"]',
            tags="positive-negative", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # --- New #84 (0.6) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.6,
            text_ar="Historic victory confirmed (decline) of Saudi football and its development.",
            option_a="historic", option_b="fans", option_c="decline", option_d="noticeable",
            correct_option="c",
            explanation_ar="Contextual error: 'decline' - Victory confirms progress. Correct: 'progress'.",
            solution_steps_ar='["Context: historic victory + development","Decline contradicts development","Correct: progress"]',
            tags="positive-negative", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # --- New #85 (0.6) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.6,
            text_ar="Reading before sleep helps (tense) nerves and relaxation.",
            option_a="tense", option_b="studies", option_c="relaxation", option_d="deep",
            correct_option="a",
            explanation_ar="Contextual error: 'tense' - Reading calms nerves. Correct: 'calming'.",
            solution_steps_ar='["Context: helps + relaxation + sleep","Tense contradicts relaxation","Correct: calming"]',
            tags="positive-negative", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # --- New #86 (0.6) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.6,
            text_ar="Foreign investment contributes to (weakening) economy and providing jobs.",
            option_a="investment", option_b="opportunities", option_c="weakening", option_d="advanced",
            correct_option="c",
            explanation_ar="Contextual error: 'weakening' - Investment strengthens economy. Correct: 'enhancing'.",
            solution_steps_ar='["Context: contributes + jobs + technology","Weakening contradicts contribution","Correct: enhancing"]',
            tags="positive-negative", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # --- New #87 (0.6) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.6,
            text_ar="Airport development contributes to (disrupting) travel and passenger comfort.",
            option_a="developing", option_b="air", option_c="procedures", option_d="disrupting",
            correct_option="d",
            explanation_ar="Contextual error: 'disrupting' - Development activates travel. Correct: 'activating'.",
            solution_steps_ar='["Context: development + comfort + facilitating","Disrupting contradicts development","Correct: activating"]',
            tags="positive-negative", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # --- New #88 (0.6) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.6,
            text_ar="Greenhouses enabled farmers (to reduce) production and provide crops year-round.",
            option_a="greenhouses", option_b="to reduce", option_c="agricultural", option_d="crops",
            correct_option="b",
            explanation_ar="Contextual error: 'to reduce' - Greenhouses increase production. Correct: 'to increase'.",
            solution_steps_ar='["Context: enabled + provide crops year-round","Reduce contradicts provision","Correct: to increase"]',
            tags="positive-negative", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # --- New #89 (0.6) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.6,
            text_ar="Patience indicates (fragility) of faith, strength of will, and trust.",
            option_a="patience", option_b="fragility", option_c="will", option_d="destiny",
            correct_option="b",
            explanation_ar="Contextual error: 'fragility' - Patience indicates firmness. Correct: 'firmness'.",
            solution_steps_ar='["Context: patience + strength + trust","Fragility contradicts strength","Correct: firmness"]',
            tags="semantic-mismatch", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # --- New #90 (0.6) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.6,
            text_ar="Satellites enabled scientists (to disrupt) global communications.",
            option_a="to disrupt", option_b="enabled", option_c="global", option_d="extreme",
            correct_option="a",
            explanation_ar="Contextual error: 'to disrupt' - Satellites improve communications. Correct: 'to improve'.",
            solution_steps_ar='["Context: enabled + extreme precision","Disrupt contradicts enablement","Correct: to improve"]',
            tags="positive-negative", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # --- New #91 (0.7) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.7,
            text_ar="Modern teaching methods contribute to (standardizing) thinking and unleashing creativity.",
            option_a="educators", option_b="standardizing", option_c="creativity", option_d="analytical",
            correct_option="b",
            explanation_ar="Contextual error: 'standardizing' - Modern methods promote creativity. Correct: 'diversifying'.",
            solution_steps_ar='["Context: modern methods + creativity","Standardizing contradicts creativity","Correct: diversifying"]',
            tags="semantic-mismatch", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # --- New #92 (0.7) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.7,
            text_ar="Chronic stress leads to (strengthening) immunity and increasing disease risk.",
            option_a="research", option_b="immune", option_c="diabetes", option_d="strengthening",
            correct_option="d",
            explanation_ar="Contextual error: 'strengthening' - Stress weakens immunity. Correct: 'weakening'.",
            solution_steps_ar='["Context: chronic stress + disease risk","Strengthening contradicts negative context","Correct: weakening"]',
            tags="positive-negative", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # --- New #93 (0.7) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.7,
            text_ar="Charities seek to (expand) poverty circle through assistance programs.",
            option_a="charitable", option_b="assistance", option_c="needy", option_d="expand",
            correct_option="d",
            explanation_ar="Contextual error: 'expand' - Charities narrow poverty. Correct: 'narrow'.",
            solution_steps_ar='["Context: charitable + assistance + rehabilitation","Expand contradicts charitable work","Correct: narrow"]',
            tags="positive-negative", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # --- New #94 (0.7) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.7,
            text_ar="Penicillin discovery is a (regression) point in medical history.",
            option_a="regression", option_b="discovery", option_c="modern", option_d="deadly",
            correct_option="a",
            explanation_ar="Contextual error: 'regression' - Discovery was a turning point. Correct: 'turning point'.",
            solution_steps_ar='["Context: saved millions","Regression contradicts saving","Correct: turning point"]',
            tags="positive-negative", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # --- New #95 (0.7) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.7,
            text_ar="Entrepreneurship contributes to (wasting) national wealth and creating jobs.",
            option_a="wasting", option_b="encourages", option_c="national", option_d="innovative",
            correct_option="a",
            explanation_ar="Contextual error: 'wasting' - Entrepreneurship develops wealth. Correct: 'developing'.",
            solution_steps_ar='["Context: encourages + innovative jobs","Wasting contradicts encouragement","Correct: developing"]',
            tags="positive-negative", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # --- New #96 (0.7) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.7,
            text_ar="Reserves work to (accelerate) extinction of rare animals.",
            option_a="reserves", option_b="rare", option_c="accelerate", option_d="biodiversity",
            correct_option="c",
            explanation_ar="Contextual error: 'accelerate' - Reserves prevent extinction. Correct: 'prevent'.",
            solution_steps_ar='["Context: reserves + preserve biodiversity","Accelerate contradicts preservation","Correct: prevent"]',
            tags="positive-negative", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # --- New #97 (0.3) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.3,
            text_ar="Remote work proved (its failure) in raising productivity and achieving balance.",
            option_a="experts", option_b="failure", option_c="balance", option_d="personal",
            correct_option="b",
            explanation_ar="Contextual error: 'failure' - Context mentions positive results. Correct: 'success'.",
            solution_steps_ar='["Results: productivity + balance = positive","Failure contradicts positive results","Correct: success"]',
            tags="positive-negative", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # --- New #98 (0.8) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.8,
            text_ar="Higher education makes social problems (more severe) and increases development.",
            option_a="higher", option_b="more severe", option_c="development", option_d="life",
            correct_option="b",
            explanation_ar="Contextual error: 'more severe' - Education reduces problems. Correct: 'less severe'.",
            solution_steps_ar='["Relationship: education improves community","Evidence: development + improved quality","More severe contradicts this"]',
            tags="positive-negative", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- New #99 (0.8) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.8,
            text_ar="Despite rising oil prices, government (reduced) infrastructure spending and increased investments.",
            option_a="reduced", option_b="rising", option_c="infrastructure", option_d="vital",
            correct_option="a",
            explanation_ar="Contextual error: 'reduced' - Rising prices mean more revenue. Correct: 'raised'.",
            solution_steps_ar='["Rising prices = increased revenues","Evidence: increased investments","Reduced contradicts logic"]',
            tags="context-contradiction", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # --- New #100 (0.8) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.8,
            text_ar="Experts warn that (ignoring) updates enhances protection and reduces risks.",
            option_a="warn", option_b="ignoring", option_c="protection", option_d="hacking",
            correct_option="b",
            explanation_ar="Contextual error: 'ignoring' - Warning implies danger, but results are positive. Correct: 'adhering'.",
            solution_steps_ar='["Warn implies danger","But results: enhancing + reducing = positive","Ignoring does not enhance protection"]',
            tags="semantic-mismatch", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # --- New #101 (0.8) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.8,
            text_ar="Qiddiya project contributed to (reducing) entertainment industry size and attracting investments.",
            option_a="project", option_b="investments", option_c="jobs", option_d="reducing",
            correct_option="d",
            explanation_ar="Contextual error: 'reducing' - Qiddiya expands industry. Correct: 'expanding'.",
            solution_steps_ar='["Context: contributed + attracting + providing jobs","Reducing contradicts attraction","Correct: expanding"]',
            tags="positive-negative", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # --- New #102 (0.4) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.4,
            text_ar="Water helps in (drying out) body cells and regulating temperature.",
            option_a="advised", option_b="adequate", option_c="drying out", option_d="temperature",
            correct_option="c",
            explanation_ar="Contextual error: 'drying out' - Water moisturizes cells. Correct: 'moisturizing'.",
            solution_steps_ar='["Context: advised + adequate + regulate","Drying contradicts water benefit","Correct: moisturizing"]',
            tags="positive-negative", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # --- New #103 (0.5) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.5,
            text_ar="Satellite is essential in (obscuring) communications and providing services.",
            option_a="satellite", option_b="obscuring", option_c="navigation", option_d="television",
            correct_option="b",
            explanation_ar="Contextual error: 'obscuring' - Satellites improve communications. Correct: 'improving'.",
            solution_steps_ar='["Context: essential tool + providing services","Obscuring contradicts improvement","Correct: improving"]',
            tags="positive-negative", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- New #104 (0.6) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.6,
            text_ar="Strategic planning leads to (randomness) in decisions and achieving goals.",
            option_a="planning", option_b="randomness", option_c="administrative", option_d="specified",
            correct_option="b",
            explanation_ar="Contextual error: 'randomness' - Planning organizes decisions. Correct: 'precision'.",
            solution_steps_ar='["Context: planning + achieving goals efficiently","Randomness contradicts planning","Correct: precision"]',
            tags="positive-negative", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- New #105 (0.5) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.5,
            text_ar="Renewable energy represents (threat) to planet and clean alternative to fossil fuels.",
            option_a="energy", option_b="threat", option_c="clean", option_d="polluting",
            correct_option="b",
            explanation_ar="Contextual error: 'threat' - Renewable energy is hope. Correct: 'hope'.",
            solution_steps_ar='["Context: clean alternative to polluting fuel","Threat contradicts being clean alternative","Correct: hope"]',
            tags="positive-negative", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # --- New #106 (0.6) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.6,
            text_ar="Red Sea Project contributed to (disfiguring) natural landscapes and developing eco-tourism.",
            option_a="contributed", option_b="disfiguring", option_c="natural", option_d="sustainable",
            correct_option="b",
            explanation_ar="Contextual error: 'disfiguring' - Project preserves landscapes. Correct: 'highlighting'.",
            solution_steps_ar='["Context: contributed + developing sustainable tourism","Disfiguring contradicts sustainability","Correct: highlighting"]',
            tags="positive-negative", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- New #107 (0.7) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.7,
            text_ar="Children in (disrupted) family environments enjoy high confidence and stability.",
            option_a="studies", option_b="confidence", option_c="disrupted", option_d="noticeable",
            correct_option="c",
            explanation_ar="Contextual error: 'disrupted' - Results are positive. Correct: 'stable'.",
            solution_steps_ar='["Results: high confidence + stability","Disrupted environment does not produce these","Correct: stable"]',
            tags="semantic-mismatch", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # --- New #108 (0.4) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.4,
            text_ar="Running strengthens heart and (slows down) circulation and gives vitality.",
            option_a="doctors", option_b="strengthens", option_c="slows down", option_d="vitality",
            correct_option="c",
            explanation_ar="Contextual error: 'slows down' - Running activates circulation. Correct: 'activates'.",
            solution_steps_ar='["Context: strengthens + vitality","Slowing contradicts strengthening","Correct: activates"]',
            tags="positive-negative", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # --- New #109 (0.5) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.5,
            text_ar="Good manners open doors of (hatred) and make one loved.",
            option_a="good", option_b="open", option_c="hatred", option_d="loved",
            correct_option="c",
            explanation_ar="Contextual error: 'hatred' - Good manners open love. Correct: 'love'.",
            solution_steps_ar='["Context: good manners + loved everywhere","Hatred contradicts love","Correct: love"]',
            tags="positive-negative", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- New #110 (0.7) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.7,
            text_ar="Countries seek to (expand) desertification area by planting trees.",
            option_a="desertification", option_b="food", option_c="expand", option_d="trees",
            correct_option="c",
            explanation_ar="Contextual error: 'expand' - Countries seek to reduce desertification. Correct: 'reduce'.",
            solution_steps_ar='["Desertification = threat to food security","Solution: planting trees = combating","Expand contradicts combating"]',
            tags="context-contradiction", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # --- New #111 (0.6) ---
        Question(skill_id="verbal_error", question_type="error", difficulty=0.6,
            text_ar="Scientific progress (restricts) freedom, while experiments prove it gives wider choices.",
            option_a="philosophers", option_b="restricts", option_c="choices", option_d="destiny",
            correct_option="b",
            explanation_ar="Contextual error: 'restricts' - Results show expansion. Correct: 'expands'.",
            solution_steps_ar='["While experiments prove = correction","Results: wider choices + control = expansion","Restricts contradicts evidence"]',
            tags="context-contradiction", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),


        # ══════════════════════════════════════════════════════════════
        # 56 NEW QUESTIONS (Q112–Q167)
        # ══════════════════════════════════════════════════════════════

        # ── difficulty 0.2 — 3 questions (diagnostic) ──

        # Q112
        Question(skill_id="verbal_error", question_type="error", difficulty=0.2,
            text_ar="Students use pens (for eating) when writing homework.",
            option_a="use", option_b="for eating", option_c="writing", option_d="notes",
            correct_option="b",
            explanation_ar="Contextual error: 'for eating' - Pens are for writing. Correct: 'for writing'.",
            solution_steps_ar='["Context: pens + homework = writing tool","Eating = wrong use","Correct: for writing"]',
            tags="semantic-mismatch", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q113
        Question(skill_id="verbal_error", question_type="error", difficulty=0.2,
            text_ar="People trust the (ignorant) doctor with extensive experience.",
            option_a="trust", option_b="ignorant", option_c="experience", option_d="difficult",
            correct_option="b",
            explanation_ar="Contextual error: 'ignorant' - Doctor has experience. Correct: 'skilled'.",
            solution_steps_ar='["Context: trust + extensive experience","Ignorant contradicts experience","Correct: skilled"]',
            tags="positive-negative", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # Q114
        Question(skill_id="verbal_error", question_type="error", difficulty=0.2,
            text_ar="Children go to park (to cry) and enjoy playing.",
            option_a="go", option_b="park", option_c="to cry", option_d="fresh",
            correct_option="c",
            explanation_ar="Contextual error: 'to cry' - Children go to enjoy. Correct: 'to enjoy'.",
            solution_steps_ar='["Context: enjoy + play + run","Cry contradicts enjoyment","Correct: to enjoy"]',
            tags="positive-negative", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ── difficulty 0.3 — 5 questions (foundation) ──

        # Q115
        Question(skill_id="verbal_error", question_type="error", difficulty=0.3,
            text_ar="Farmer is keen on (neglecting) crops and watering regularly.",
            option_a="farmer", option_b="neglecting", option_c="regularly", option_d="abundant",
            correct_option="b",
            explanation_ar="Contextual error: 'neglecting' - Context mentions regular watering. Correct: 'caring for'.",
            solution_steps_ar='["Context: keen + regular watering + abundant","Neglecting contradicts keenness","Correct: caring for"]',
            tags="positive-negative", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # Q116
        Question(skill_id="verbal_error", question_type="error", difficulty=0.3,
            text_ar="Saudi Arabia has vast area and (narrow) diversity of deserts, mountains, coasts.",
            option_a="distinguished", option_b="vast", option_c="narrow", option_d="coasts",
            correct_option="c",
            explanation_ar="Contextual error: 'narrow' - Context mentions diverse geography. Correct: 'rich'.",
            solution_steps_ar='["Context: vast + deserts + mountains + coasts","Narrow contradicts diversity","Correct: rich"]',
            tags="context-contradiction", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q117
        Question(skill_id="verbal_error", question_type="error", difficulty=0.3,
            text_ar="Exercise helps in (weakening) muscles and improving fitness.",
            option_a="exercise", option_b="weakening", option_c="fitness", option_d="overall",
            correct_option="b",
            explanation_ar="Contextual error: 'weakening' - Exercise strengthens muscles. Correct: 'strengthening'.",
            solution_steps_ar='["Context: helps + improve fitness","Weakening contradicts improvement","Correct: strengthening"]',
            tags="positive-negative", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q118
        Question(skill_id="verbal_error", question_type="error", difficulty=0.3,
            text_ar="Fasting is from (sunset) until Maghrib.",
            option_a="greatest", option_b="abstain", option_c="sunset", option_d="Maghrib",
            correct_option="c",
            explanation_ar="Contextual error: 'sunset' - Fasting begins at dawn. Correct: 'dawn'.",
            solution_steps_ar='["Fasting: from time to time","Ends at Maghrib sunset","Sunset same as Maghrib, should be dawn"]',
            tags="logical-error", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q119
        Question(skill_id="verbal_error", question_type="error", difficulty=0.3,
            text_ar="School team achieved crushing (defeat) and returned with cup and medals.",
            option_a="team", option_b="defeat", option_c="championship", option_d="gold",
            correct_option="b",
            explanation_ar="Contextual error: 'defeat' - Team won cup and medals. Correct: 'victory'.",
            solution_steps_ar='["Context: cup + gold medals = win","Defeat contradicts winning","Correct: victory"]',
            tags="positive-negative", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── difficulty 0.4 — 10 questions ──

        # Q120
        Question(skill_id="verbal_error", question_type="error", difficulty=0.4,
            text_ar="True scholar has humility and (boasting) about achievements.",
            option_a="characterized", option_b="humility", option_c="boasting", option_d="society",
            correct_option="c",
            explanation_ar="Contextual error: 'boasting' - Humility contradicts boasting. Correct: 'modesty'.",
            solution_steps_ar='["Context: humility + serve society","Boasting contradicts humility","Correct: modesty"]',
            tags="context-contradiction", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q121
        Question(skill_id="verbal_error", question_type="error", difficulty=0.4,
            text_ar="Ministry announced initiative (to reduce) education opportunities and make available to all.",
            option_a="announced", option_b="initiative", option_c="to reduce", option_d="citizens",
            correct_option="c",
            explanation_ar="Contextual error: 'to reduce' - Making available means expanding. Correct: 'to expand'.",
            solution_steps_ar='["Context: initiative + make available to all","Reduce contradicts availability","Correct: to expand"]',
            tags="positive-negative", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q122
        Question(skill_id="verbal_error", question_type="error", difficulty=0.4,
            text_ar="Merchant success requires (betraying) trust and providing quality goods.",
            option_a="success", option_b="betraying", option_c="dealing", option_d="quality",
            correct_option="b",
            explanation_ar="Contextual error: 'betraying' - Success requires honesty. Correct: 'maintaining'.",
            solution_steps_ar='["Context: success + quality + good dealing","Betraying contradicts success","Correct: maintaining trust"]',
            tags="positive-negative", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q123
        Question(skill_id="verbal_error", question_type="error", difficulty=0.4,
            text_ar="Blood donation contributes to (spreading) epidemics and saving lives.",
            option_a="donation", option_b="spreading", option_c="saving", option_d="needy",
            correct_option="b",
            explanation_ar="Contextual error: 'spreading' - Donation saves lives. Correct: 'combating'.",
            solution_steps_ar='["Context: contributes + saving lives","Spreading contradicts saving","Correct: combating"]',
            tags="positive-negative", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q124
        Question(skill_id="verbal_error", question_type="error", difficulty=0.4,
            text_ar="Parents provide (hostile) environment that enhances confidence and develops talents.",
            option_a="keen", option_b="hostile", option_c="confidence", option_d="talents",
            correct_option="b",
            explanation_ar="Contextual error: 'hostile' - Enhancing confidence needs safe environment. Correct: 'safe'.",
            solution_steps_ar='["Context: keen + enhance confidence + develop talents","Hostile contradicts enhancement","Correct: safe"]',
            tags="semantic-mismatch", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q125
        Question(skill_id="verbal_error", question_type="error", difficulty=0.4,
            text_ar="Cultural festivals are held (to erase) heritage and introducing cultures.",
            option_a="held", option_b="erase", option_c="heritage", option_d="arts",
            correct_option="b",
            explanation_ar="Contextual error: 'erase' - Festivals revive heritage. Correct: 'revive'.",
            solution_steps_ar='["Context: cultural festivals + introduce cultures","Erase contradicts revival","Correct: revive"]',
            tags="positive-negative", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q126
        Question(skill_id="verbal_error", question_type="error", difficulty=0.4,
            text_ar="Grand Mosque is (smallest) mosque, receiving millions of pilgrims.",
            option_a="smallest", option_b="world", option_c="pilgrims", option_d="yearly",
            correct_option="a",
            explanation_ar="Contextual error: 'smallest' - Grand Mosque is largest. Correct: 'largest'.",
            solution_steps_ar='["Context: millions of pilgrims = massive","Smallest contradicts accommodating millions","Correct: largest"]',
            tags="logical-error", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q127
        Question(skill_id="verbal_error", question_type="error", difficulty=0.4,
            text_ar="Reading is food for (body) that expands horizons and develops imagination.",
            option_a="reading", option_b="body", option_c="horizons", option_d="vocabulary",
            correct_option="b",
            explanation_ar="Contextual error: 'body' - Reading nourishes mind. Correct: 'mind'.",
            solution_steps_ar='["Evidence: expands horizons + develops imagination + enriches vocabulary","All are mental functions","Correct: mind"]',
            tags="semantic-mismatch", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q128
        Question(skill_id="verbal_error", question_type="error", difficulty=0.4,
            text_ar="Teacher confirmed that (cheating) in exams enhances personality and builds confidence.",
            option_a="teacher", option_b="cheating", option_c="personality", option_d="responsibility",
            correct_option="b",
            explanation_ar="Contextual error: 'cheating' - Enhancing personality needs effort. Correct: 'diligence'.",
            solution_steps_ar='["Results: enhance personality build confidence responsibility","Cheating does not achieve these","Correct: diligence"]',
            tags="semantic-mismatch", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q129
        Question(skill_id="verbal_error", question_type="error", difficulty=0.4,
            text_ar="NEOM seeks to build (traditional) city using AI and renewable energy.",
            option_a="seeks", option_b="traditional", option_c="AI", option_d="renewable",
            correct_option="b",
            explanation_ar="Contextual error: 'traditional' - AI and renewable indicate futuristic. Correct: 'futuristic'.",
            solution_steps_ar='["Context: AI + renewable energy = modern tech","Traditional contradicts advanced tech","Correct: futuristic"]',
            tags="context-contradiction", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),


        # ── difficulty 0.5 — 10 questions ──

        # Q130
        Question(skill_id="verbal_error", question_type="error", difficulty=0.5,
            text_ar="Tourism contributes to (reducing) job opportunities and activating commerce.",
            option_a="resource", option_b="reducing", option_c="activating", option_d="country",
            correct_option="b",
            explanation_ar="Contextual error: 'reducing' - Tourism increases jobs. Correct: 'increasing'.",
            solution_steps_ar='["Context: economic resource + activate commerce","Reducing contradicts context","Correct: increasing"]',
            tags="positive-negative", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q131
        Question(skill_id="verbal_error", question_type="error", difficulty=0.5,
            text_ar="As craftsman masters skill, product quality (declines) and demand rises.",
            option_a="mastery", option_b="declines", option_c="products", option_d="markets",
            correct_option="b",
            explanation_ar="Contextual error: 'declines' - Mastery improves quality. Correct: 'improves'.",
            solution_steps_ar='["Relationship: more mastery = positive result","Rising demand = quality proof","Declines contradicts demand"]',
            tags="positive-negative", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q132
        Question(skill_id="verbal_error", question_type="error", difficulty=0.5,
            text_ar="Penicillin proved mold, considered harmful, could be source (for disease) that saves lives.",
            option_a="mold", option_b="harmful", option_c="for disease", option_d="lives",
            correct_option="c",
            explanation_ar="Contextual error: 'for disease' - Penicillin is medicine. Correct: 'for cure'.",
            solution_steps_ar='["Context: penicillin = medicine","Result: saving lives","For disease contradicts saving"]',
            tags="context-contradiction", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q133
        Question(skill_id="verbal_error", question_type="error", difficulty=0.5,
            text_ar="Keeping appointments leads to (losing) trust and enhancing relationships.",
            option_a="respect", option_b="losing", option_c="relationships", option_d="social",
            correct_option="b",
            explanation_ar="Contextual error: 'losing' - Keeping appointments earns trust. Correct: 'earning'.",
            solution_steps_ar='["Context: respect + commitment + enhance","Losing contradicts context","Correct: earning"]',
            tags="positive-negative", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q134
        Question(skill_id="verbal_error", question_type="error", difficulty=0.5,
            text_ar="Sleep helps brain (scatter) acquired information and consolidate memory.",
            option_a="body", option_b="adequate", option_c="scatter", option_d="memory",
            correct_option="c",
            explanation_ar="Contextual error: 'scatter' - Sleep consolidates information. Correct: 'process'.",
            solution_steps_ar='["Context: adequate sleep + consolidate memory","Scatter = opposite of consolidate","Correct: process"]',
            tags="positive-negative", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q135
        Question(skill_id="verbal_error", question_type="error", difficulty=0.5,
            text_ar="Industrial Revolution transformed societies from (industry) to agriculture.",
            option_a="contributed", option_b="industry", option_c="agriculture", option_d="patterns",
            correct_option="b",
            explanation_ar="Contextual error: 'industry' - Revolution moved to industry. Correct: 'agriculture' (reversed).",
            solution_steps_ar='["Industrial Revolution = move to industry","Logic: from agriculture to industry","Industry to agriculture = reversed"]',
            tags="logical-error", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q136
        Question(skill_id="verbal_error", question_type="error", difficulty=0.5,
            text_ar="Volunteering enhances (selfishness) and teaches meaning of giving.",
            option_a="volunteering", option_b="selfishness", option_c="giving", option_d="society",
            correct_option="b",
            explanation_ar="Contextual error: 'selfishness' - Volunteering teaches altruism. Correct: 'altruism'.",
            solution_steps_ar='["Context: volunteering + giving + responsibility","Selfishness contradicts giving","Correct: altruism"]',
            tags="positive-negative", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q137
        Question(skill_id="verbal_error", question_type="error", difficulty=0.5,
            text_ar="Success of (demolishing) Holy Mosques project depends on providing best services.",
            option_a="success", option_b="demolishing", option_c="services", option_d="pilgrims",
            correct_option="b",
            explanation_ar="Contextual error: 'demolishing' - Project serves pilgrims. Correct: 'expansion'.",
            solution_steps_ar='["Context: success + serve pilgrims","Demolishing contradicts service","Correct: expansion"]',
            tags="semantic-mismatch", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q138
        Question(skill_id="verbal_error", question_type="error", difficulty=0.5,
            text_ar="Experts warn excess (vegetables) causes obesity and heart disease.",
            option_a="experts", option_b="vegetables", option_c="obesity", option_d="heart",
            correct_option="b",
            explanation_ar="Contextual error: 'vegetables' - These result from fatty foods. Correct: 'fats'.",
            solution_steps_ar='["Results: obesity cholesterol heart disease","Vegetables are healthy","Correct: fats"]',
            tags="semantic-mismatch", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q139
        Question(skill_id="verbal_error", question_type="error", difficulty=0.5,
            text_ar="Invention of (wheel) complicated transportation and delayed civilization development.",
            option_a="invention", option_b="wheel", option_c="complicated", option_d="history",
            correct_option="c",
            explanation_ar="Contextual error: 'complicated' - Wheel simplified transportation. Correct: 'simplified'.",
            solution_steps_ar='["Wheel = pivotal invention","Advanced civilizations","Complicated contradicts contribution"]',
            tags="context-contradiction", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── difficulty 0.6 — 12 questions ──

        # Q140
        Question(skill_id="verbal_error", question_type="error", difficulty=0.6,
            text_ar="Family dialogue leads to (disintegration) of bonds and increases understanding.",
            option_a="constructive", option_b="disintegration", option_c="understanding", option_d="members",
            correct_option="b",
            explanation_ar="Contextual error: 'disintegration' - Dialogue strengthens bonds. Correct: 'strengthening'.",
            solution_steps_ar='["Context: constructive dialogue + understanding + harmony","Disintegration contradicts context","Correct: strengthening"]',
            tags="positive-negative", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q141
        Question(skill_id="verbal_error", question_type="error", difficulty=0.6,
            text_ar="Excessive sun exposure (protects) skin from burns and increases cancer risk.",
            option_a="research", option_b="excessive", option_c="protects", option_d="cancer",
            correct_option="c",
            explanation_ar="Contextual error: 'protects' - Excess exposure harms skin. Correct: 'harms'.",
            solution_steps_ar='["Context: excessive + cancer risk","Protects contradicts harm context","Correct: harms"]',
            tags="context-contradiction", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q142
        Question(skill_id="verbal_error", question_type="error", difficulty=0.6,
            text_ar="We trust (biased) judge who rules with justice and equality.",
            option_a="trust", option_b="biased", option_c="justice", option_d="status",
            correct_option="b",
            explanation_ar="Contextual error: 'biased' - Justice requires impartiality. Correct: 'impartial'.",
            solution_steps_ar='["Context: trust + justice + equality + no discrimination","Biased contradicts justice","Correct: impartial"]',
            tags="context-contradiction", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q143
        Question(skill_id="verbal_error", question_type="error", difficulty=0.6,
            text_ar="Muslim scientists were keen on (destroying) Greek manuscripts and translating them.",
            option_a="keen", option_b="destroying", option_c="translating", option_d="sciences",
            correct_option="b",
            explanation_ar="Contextual error: 'destroying' - Scientists preserved manuscripts. Correct: 'preserving'.",
            solution_steps_ar='["Context: keen + translate + develop sciences","Destroying contradicts preservation","Correct: preserving"]',
            tags="semantic-mismatch", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q144
        Question(skill_id="verbal_error", question_type="error", difficulty=0.6,
            text_ar="Tropical climate has (low) rainfall and dense vegetation.",
            option_a="characterized", option_b="low", option_c="vegetation", option_d="dense",
            correct_option="b",
            explanation_ar="Contextual error: 'low' - Tropical climate has heavy rain. Correct: 'heavy'.",
            solution_steps_ar='["Context: dense vegetation + rain forests","Low rainfall contradicts dense vegetation","Correct: heavy"]',
            tags="logical-error", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q145
        Question(skill_id="verbal_error", question_type="error", difficulty=0.6,
            text_ar="WHO aims to (spread) infectious diseases and combat epidemics.",
            option_a="aims", option_b="spread", option_c="combat", option_d="care",
            correct_option="b",
            explanation_ar="Contextual error: 'spread' - WHO combats diseases. Correct: 'eliminate'.",
            solution_steps_ar='["Context: health organization + combat epidemics","Spread contradicts combat","Correct: eliminate"]',
            tags="positive-negative", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q146
        Question(skill_id="verbal_error", question_type="error", difficulty=0.6,
            text_ar="High unemployment contributes to (stability) and increases crime.",
            option_a="experts", option_b="stability", option_c="crime", option_d="domestic",
            correct_option="b",
            explanation_ar="Contextual error: 'stability' - Unemployment causes instability. Correct: 'instability'.",
            solution_steps_ar='["Context: unemployment + crime + violence","Stability contradicts crime","Correct: instability"]',
            tags="context-contradiction", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q147
        Question(skill_id="verbal_error", question_type="error", difficulty=0.6,
            text_ar="Learning second language (weakens) memory and enhances mental flexibility.",
            option_a="studies", option_b="weakens", option_c="flexibility", option_d="early",
            correct_option="b",
            explanation_ar="Contextual error: 'weakens' - Learning strengthens mind. Correct: 'strengthens'.",
            solution_steps_ar='["Context: enhance flexibility + delay dementia","Weakens contradicts benefits","Correct: strengthens"]',
            tags="positive-negative", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q148
        Question(skill_id="verbal_error", question_type="error", difficulty=0.6,
            text_ar="Moon landing was not a (failure) but a giant leap in space exploration.",
            option_a="landing", option_b="failure", option_c="leap", option_d="exploration",
            correct_option="b",
            explanation_ar="Contextual error: 'failure' - Landing was great achievement. Correct: 'achievement'.",
            solution_steps_ar='["Context: giant leap = positive","Failure contradicts giant leap","Correct: achievement"]',
            tags="positive-negative", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q149
        Question(skill_id="verbal_error", question_type="error", difficulty=0.6,
            text_ar="Tolerance contributes to (igniting) conflicts and building bridges.",
            option_a="tolerance", option_b="igniting", option_c="bridges", option_d="peoples",
            correct_option="b",
            explanation_ar="Contextual error: 'igniting' - Tolerance resolves conflicts. Correct: 'resolving'.",
            solution_steps_ar='["Context: noble values + building bridges","Igniting contradicts tolerance","Correct: resolving"]',
            tags="positive-negative", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q150
        Question(skill_id="verbal_error", question_type="error", difficulty=0.6,
            text_ar="Children who read regularly (decline) in language proficiency.",
            option_a="notice", option_b="regularly", option_c="proficiency", option_d="decline",
            correct_option="d",
            explanation_ar="Contextual error: 'decline' - Reading increases proficiency. Correct: 'increase'.",
            solution_steps_ar='["Context: children who read = positive effect","Decline contradicts logic","Correct: increase"]',
            tags="logical-error", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q151
        Question(skill_id="verbal_error", question_type="error", difficulty=0.6,
            text_ar="Saudi Green Initiative contributed to (stripping) vegetation and planting billions of trees.",
            option_a="contributed", option_b="stripping", option_c="vegetation", option_d="desertification",
            correct_option="b",
            explanation_ar="Contextual error: 'stripping' - Initiative enriches vegetation. Correct: 'enriching'.",
            solution_steps_ar='["Context: green initiative + planting billions","Stripping contradicts planting","Correct: enriching"]',
            tags="context-contradiction", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),


        # ── difficulty 0.7 — 10 questions ──

        # Q152
        Question(skill_id="verbal_error", question_type="error", difficulty=0.7,
            text_ar="Meditation practitioners suffer from (high) stress and reduced focus.",
            option_a="indicate", option_b="regularly", option_c="high", option_d="focus",
            correct_option="c",
            explanation_ar="Contextual error: 'high' - Meditation reduces stress. Correct: 'low'.",
            solution_steps_ar='["Meditation = known benefit","High stress low focus = negative","Correct: low stress"]',
            tags="logical-error", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q153
        Question(skill_id="verbal_error", question_type="error", difficulty=0.7,
            text_ar="Innovation requires environment encouraging (imitation) and risk-taking.",
            option_a="innovation", option_b="imitation", option_c="risk", option_d="traditional",
            correct_option="b",
            explanation_ar="Contextual error: 'imitation' - Innovation requires experimentation. Correct: 'experimentation'.",
            solution_steps_ar='["Context: innovation + risk = creative environment","Imitation = opposite of innovation","Correct: experimentation"]',
            tags="semantic-mismatch", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q154
        Question(skill_id="verbal_error", question_type="error", difficulty=0.7,
            text_ar="Antibiotics led to (rise) in bacterial disease mortality and saved lives.",
            option_a="discovery", option_b="rise", option_c="bacterial", option_d="lives",
            correct_option="b",
            explanation_ar="Contextual error: 'rise' - Antibiotics reduced mortality. Correct: 'decline'.",
            solution_steps_ar='["Context: saving lives = positive","Rise in mortality contradicts saving","Correct: decline"]',
            tags="positive-negative", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q155
        Question(skill_id="verbal_error", question_type="error", difficulty=0.7,
            text_ar="Organic farming reduces (fertility) and increases water pollution.",
            option_a="field", option_b="organic", option_c="fertility", option_d="groundwater",
            correct_option="c",
            explanation_ar="Contextual error: 'fertility' - Organic farming preserves fertility. Correct: 'pollution'.",
            solution_steps_ar='["Organic farming = eco-friendly","Reducing fertility increasing pollution wrong","Correct: reduces pollution"]',
            tags="context-contradiction", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q156
        Question(skill_id="verbal_error", question_type="error", difficulty=0.7,
            text_ar="Socrates believed virtue lies in (ignorance) and knowledge leads to ethical behavior.",
            option_a="philosopher", option_b="virtue", option_c="ignorance", option_d="ethical",
            correct_option="c",
            explanation_ar="Contextual error: 'ignorance' - Socrates believed virtue is knowledge. Correct: 'knowledge'.",
            solution_steps_ar='["Socrates philosophy: knowledge = virtue","Ignorance contradicts knowledge mentioned","Correct: knowledge"]',
            tags="semantic-mismatch", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q157
        Question(skill_id="verbal_error", question_type="error", difficulty=0.7,
            text_ar="Countries investing in education see (decline) in GDP and improved living standards.",
            option_a="statistics", option_b="invest", option_c="decline", option_d="living",
            correct_option="c",
            explanation_ar="Contextual error: 'decline' - Education investment raises GDP. Correct: 'growth'.",
            solution_steps_ar='["Context: investment + improved living","Decline contradicts improved living","Correct: growth"]',
            tags="context-contradiction", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q158
        Question(skill_id="verbal_error", question_type="error", difficulty=0.7,
            text_ar="Bees play vital role in (destroying) ecosystem by pollinating plants.",
            option_a="researchers", option_b="vital", option_c="destroying", option_d="diversity",
            correct_option="c",
            explanation_ar="Contextual error: 'destroying' - Bees protect ecosystem. Correct: 'protecting'.",
            solution_steps_ar='["Context: vital role + pollinate + diversity = positive","Destroying contradicts protection","Correct: protecting"]',
            tags="positive-negative", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q159
        Question(skill_id="verbal_error", question_type="error", difficulty=0.7,
            text_ar="Printing press contributed to (restricting) knowledge spread and keeping books elite.",
            option_a="historians", option_b="printing", option_c="restricting", option_d="elite",
            correct_option="c",
            explanation_ar="Contextual error: 'restricting' - Printing expanded knowledge. Correct: 'expanding'.",
            solution_steps_ar='["Printing = revolution in knowledge spread","Restricting elite-only wrong","Correct: expanding"]',
            tags="logical-error", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q160
        Question(skill_id="verbal_error", question_type="error", difficulty=0.7,
            text_ar="Ozone layer protects from UV rays, so we should seek to (puncture) it.",
            option_a="scientists", option_b="harmful", option_c="puncture", option_d="preserve",
            correct_option="c",
            explanation_ar="Contextual error: 'puncture' - Ozone protects, so preserve it. Correct: 'preserve'.",
            solution_steps_ar='["Context: ozone protects + must preserve","Puncture contradicts protection","Correct: preserve"]',
            tags="semantic-mismatch", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q161
        Question(skill_id="verbal_error", question_type="error", difficulty=0.7,
            text_ar="Smart cities use IoT in (complicating) urban services and improving life quality.",
            option_a="smart", option_b="complicating", option_c="urban", option_d="residents",
            correct_option="b",
            explanation_ar="Contextual error: 'complicating' - Smart cities simplify services. Correct: 'simplifying'.",
            solution_steps_ar='["Context: smart cities + tech + improve life quality","Complicating contradicts smart city goal","Correct: simplifying"]',
            tags="context-contradiction", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ── difficulty 0.8 — 6 questions (mock) ──

        # Q162
        Question(skill_id="verbal_error", question_type="error", difficulty=0.8,
            text_ar="Sustainability means depleting resources (extravagantly) for future generations.",
            option_a="sustainability", option_b="extravagantly", option_c="generations", option_d="safe",
            correct_option="b",
            explanation_ar="Contextual error: 'extravagantly' - Sustainability means conservation. Correct: 'wisely'.",
            solution_steps_ar='["Concept: environmental sustainability = protect resources","Extravagant contradicts sustainability","Correct: wisely"]',
            tags="semantic-mismatch", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q163
        Question(skill_id="verbal_error", question_type="error", difficulty=0.8,
            text_ar="Economists warn that (diversifying) income sources exposes country to single-resource risk.",
            option_a="warn", option_b="diversifying", option_c="risks", option_d="crises",
            correct_option="b",
            explanation_ar="Contextual error: 'diversifying' - Diversification protects. Correct: 'not diversifying'.",
            solution_steps_ar='["Warning: risk of single-resource dependence","Diversification is solution not problem","Correct: not diversifying"]',
            tags="logical-error", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # Q164
        Question(skill_id="verbal_error", question_type="error", difficulty=0.8,
            text_ar="Early music practice contributes to (shrinking) brain language areas.",
            option_a="neurological", option_b="early", option_c="shrinking", option_d="fine",
            correct_option="c",
            explanation_ar="Contextual error: 'shrinking' - Music develops brain areas. Correct: 'growth'.",
            solution_steps_ar='["Context: music benefit on brain = positive","Shrinking areas = negative result","Correct: growth"]',
            tags="context-contradiction", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # Q165
        Question(skill_id="verbal_error", question_type="error", difficulty=0.8,
            text_ar="Vision 2030 success in tourism is due to (closing) heritage sites and developing infrastructure.",
            option_a="success", option_b="closing", option_c="heritage", option_d="visas",
            correct_option="b",
            explanation_ar="Contextual error: 'closing' - Tourism development requires opening sites. Correct: 'opening'.",
            solution_steps_ar='["Context: tourism success + develop infrastructure + facilitate visas","Closing contradicts facilitation","Correct: opening"]',
            tags="context-contradiction", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # Q166
        Question(skill_id="verbal_error", question_type="error", difficulty=0.8,
            text_ar="Quantum computing promises huge leap in (slowing) data processing speed.",
            option_a="quantum", option_b="slowing", option_c="data", option_d="cooling",
            correct_option="b",
            explanation_ar="Contextual error: 'slowing' - Quantum computing speeds up processing. Correct: 'speed'.",
            solution_steps_ar='["Context: huge leap in speed = positive","Slowing contradicts leap","Correct: speed"]',
            tags="context-contradiction", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # Q167
        Question(skill_id="verbal_error", question_type="error", difficulty=0.8,
            text_ar="Separation of powers ensures (concentrating) authority in one entity and prevents tyranny.",
            option_a="separation", option_b="democratic", option_c="concentrating", option_d="tyranny",
            correct_option="c",
            explanation_ar="Contextual error: 'concentrating' - Separation distributes authority. Correct: 'distributing'.",
            solution_steps_ar='["Principle: separation of powers = distribution not concentration","Preventing tyranny requires no concentration","Correct: distributing"]',
            tags="logical-error", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

    ]
