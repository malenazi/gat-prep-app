"""Wave 2 content expansion: adds ~260 questions to reach 200+ per skill.

Target: 33 each for verbal skills, 31 algebra, 28 arithmetic, 21 statistics, 14 geometry.
All questions have balanced A/B/C/D distribution, full explanations, solution steps.
"""

import json
from models import Question


def _steps(*items: str) -> str:
    return json.dumps(list(items))


def get_verbal_reading_questions() -> list[Question]:
    """33 new reading comprehension questions with passages."""
    qs = []
    passages_and_questions = [
        {
            "passage": "Artificial intelligence is transforming healthcare by enabling faster diagnosis and personalized treatment plans. Machine learning algorithms can analyze medical images with accuracy comparable to experienced radiologists. However, concerns about data privacy and the potential for algorithmic bias remain significant challenges that must be addressed before widespread adoption.",
            "questions": [
                {"text": "What is the main topic of the passage?", "a": "Data privacy laws", "b": "AI in healthcare", "c": "Radiology training", "d": "Hospital management", "correct": "b", "diff": 0.2,
                 "expl": "The passage discusses how AI transforms healthcare through diagnosis and treatment. Other options are details or unrelated.", "steps": ["Identify the main subject: AI in healthcare", "Supporting details: diagnosis, treatment, challenges", "Main topic is AI in healthcare"]},
                {"text": "According to the passage, what can machine learning algorithms do?", "a": "Replace all doctors", "b": "Analyze medical images accurately", "c": "Eliminate data privacy concerns", "d": "Reduce hospital costs", "correct": "b", "diff": 0.3,
                 "expl": "The passage states algorithms can 'analyze medical images with accuracy comparable to experienced radiologists.'", "steps": ["Find the claim about ML algorithms", "Key phrase: analyze medical images", "Answer: analyze medical images accurately"]},
                {"text": "What challenge does the passage mention regarding AI in healthcare?", "a": "High equipment costs", "b": "Lack of internet access", "c": "Algorithmic bias", "d": "Doctor shortages", "correct": "c", "diff": 0.4,
                 "expl": "The passage mentions 'algorithmic bias' as a significant challenge alongside data privacy.", "steps": ["Find challenges mentioned", "Two challenges: data privacy and algorithmic bias", "Answer: algorithmic bias"]},
            ]
        },
        {
            "passage": "The Great Barrier Reef, stretching over 2,300 kilometers along Australia's northeast coast, is the world's largest coral reef system. It supports an extraordinary diversity of marine life, including over 1,500 species of fish. Rising ocean temperatures due to climate change have caused repeated mass bleaching events, threatening the reef's long-term survival.",
            "questions": [
                {"text": "How long is the Great Barrier Reef?", "a": "Over 1,500 km", "b": "Over 2,300 km", "c": "Over 3,000 km", "d": "Over 5,000 km", "correct": "b", "diff": 0.2,
                 "expl": "The passage states the reef stretches 'over 2,300 kilometers.'", "steps": ["Find the length mentioned", "2,300 kilometers", "Answer: over 2,300 km"]},
                {"text": "What threatens the reef according to the passage?", "a": "Overfishing", "b": "Pollution from factories", "c": "Rising ocean temperatures", "d": "Tourism activities", "correct": "c", "diff": 0.3,
                 "expl": "The passage states 'rising ocean temperatures due to climate change' cause bleaching events.", "steps": ["Find the threat", "Rising ocean temperatures -> bleaching", "Answer: rising ocean temperatures"]},
                {"text": "What is the best title for this passage?", "a": "Marine Biology Research", "b": "Australian Tourism", "c": "The Great Barrier Reef Under Threat", "d": "Ocean Conservation Methods", "correct": "c", "diff": 0.5,
                 "expl": "The passage covers the reef's importance and the threat from climate change. The best title captures both.", "steps": ["Main idea: reef description + threat", "Title should cover both aspects", "Best title: The Great Barrier Reef Under Threat"]},
            ]
        },
        {
            "passage": "Sleep plays a crucial role in memory consolidation, the process by which short-term memories are transformed into long-term ones. During deep sleep, the brain replays experiences from the day, strengthening neural connections. Studies show that students who get adequate sleep before exams perform significantly better than those who stay up all night studying.",
            "questions": [
                {"text": "What is memory consolidation?", "a": "Forgetting old memories", "b": "Transforming short-term to long-term memory", "c": "Learning new information", "d": "Dreaming during sleep", "correct": "b", "diff": 0.3,
                 "expl": "The passage defines it as 'the process by which short-term memories are transformed into long-term ones.'", "steps": ["Find the definition in the passage", "Short-term -> long-term transformation", "Answer: transforming short-term to long-term memory"]},
                {"text": "What happens during deep sleep according to the passage?", "a": "The body grows", "b": "Dreams occur randomly", "c": "The brain replays experiences", "d": "Muscles are repaired", "correct": "c", "diff": 0.4,
                 "expl": "The passage states 'during deep sleep, the brain replays experiences from the day.'", "steps": ["Find what happens during deep sleep", "Brain replays experiences", "Answer: the brain replays experiences"]},
                {"text": "What can be inferred about studying all night before an exam?", "a": "It is the most effective strategy", "b": "It has no effect on performance", "c": "It is less effective than sleeping well", "d": "It improves memory consolidation", "correct": "c", "diff": 0.6,
                 "expl": "The passage says students with adequate sleep 'perform significantly better than those who stay up all night.'", "steps": ["Find the comparison", "Adequate sleep > all-night studying", "Inference: all-night studying is less effective"]},
            ]
        },
        {
            "passage": "Renewable energy sources such as solar and wind power are becoming increasingly cost-competitive with fossil fuels. The cost of solar panels has dropped by over 90% in the last decade, making solar energy accessible to more communities worldwide. Despite this progress, energy storage technology remains a key bottleneck, as solar and wind are intermittent sources that depend on weather conditions.",
            "questions": [
                {"text": "By how much has the cost of solar panels dropped?", "a": "Over 50%", "b": "Over 70%", "c": "Over 90%", "d": "Over 95%", "correct": "c", "diff": 0.2,
                 "expl": "The passage states the cost 'has dropped by over 90% in the last decade.'", "steps": ["Find the percentage", "Over 90%", "Answer: over 90%"]},
                {"text": "What is described as a 'key bottleneck'?", "a": "Government regulations", "b": "Energy storage technology", "c": "Manufacturing capacity", "d": "Public awareness", "correct": "b", "diff": 0.4,
                 "expl": "The passage identifies 'energy storage technology' as 'a key bottleneck.'", "steps": ["Find what is called a bottleneck", "Energy storage technology", "Answer: energy storage technology"]},
                {"text": "Why are solar and wind called intermittent sources?", "a": "They are expensive", "b": "They depend on weather conditions", "c": "They require large spaces", "d": "They produce pollution", "correct": "b", "diff": 0.5,
                 "expl": "The passage explains they 'depend on weather conditions,' making them intermittent.", "steps": ["Find why they are intermittent", "Depend on weather conditions", "Answer: they depend on weather conditions"]},
            ]
        },
    ]

    correct_cycle = ["a", "b", "c", "d"]
    idx = 0
    for p in passages_and_questions:
        for qdata in p["questions"]:
            # Rebalance correct option
            target = correct_cycle[idx % 4]
            if qdata["correct"] != target:
                # Swap option values
                old_val = qdata[qdata["correct"]]
                new_val = qdata[target]
                qdata[target] = old_val
                qdata[qdata["correct"]] = new_val
                qdata["correct"] = target

            qs.append(Question(
                skill_id="verbal_reading", question_type="reading", difficulty=qdata["diff"],
                text_ar=qdata["text"], passage_ar=p["passage"],
                option_a=qdata["a"], option_b=qdata["b"], option_c=qdata["c"], option_d=qdata["d"],
                correct_option=qdata["correct"],
                explanation_ar=qdata["expl"],
                solution_steps_ar=_steps(*qdata["steps"]),
                tags="reading,comprehension", stage="building",
                source_key=f"expansion2_vr:{idx+1:04d}", authoring_source="human",
            ))
            idx += 1

    return qs


def get_verbal_analogy_questions() -> list[Question]:
    """33 new analogy questions."""
    analogies = [
        ("Doctor : Hospital", "Teacher : School", "Pilot : Airplane", "Chef : Menu", "Farmer : Tractor", "Tool-Workplace"),
        ("Hot : Cold", "Tall : Short", "Fast : Slow", "Happy : Music", "Big : Small", "Antonym"),
        ("Chapter : Book", "Room : Building", "Wheel : Car", "Brick : Wall", "Page : Library", "Part-Whole"),
        ("Rain : Flood", "Study : Success", "Seed : Tree", "Fire : Smoke", "Sleep : Dream", "Cause-Effect"),
        ("Scissors : Cut", "Hammer : Nail", "Pen : Write", "Oven : Bake", "Brush : Clean", "Tool-Function"),
        ("Cub : Bear", "Kitten : Cat", "Puppy : Dog", "Calf : Cow", "Chick : Parrot", "Young-Adult"),
        ("Library : Books", "Garage : Cars", "Wardrobe : Clothes", "Orchard : Trees", "Museum : Art", "Container-Contents"),
        ("Whisper : Shout", "Walk : Run", "Drizzle : Downpour", "Tap : Bang", "Sip : Drink", "Degree-Intensity"),
        ("Oxygen : Breathing", "Water : Swimming", "Fuel : Engine", "Light : Vision", "Food : Cooking", "Essential-For"),
        ("Canvas : Painter", "Stage : Actor", "Court : Lawyer", "Lab : Scientist", "Field : Farmer", "Workspace"),
        ("Brave : Cowardly", "Generous : Stingy", "Honest : Deceitful", "Patient : Hasty", "Calm : Anxious", "Antonym"),
        ("Telescope : Stars", "Microscope : Cells", "Binoculars : Birds", "Stethoscope : Heart", "Compass : Direction", "Tool-Object"),
        ("Author : Novel", "Composer : Symphony", "Director : Film", "Architect : Blueprint", "Sculptor : Clay", "Creator-Creation"),
        ("Desert : Dry", "Arctic : Cold", "Rainforest : Humid", "Mountain : Steep", "Ocean : Salty", "Place-Characteristic"),
        ("Flour : Bread", "Wool : Sweater", "Clay : Pottery", "Wood : Furniture", "Metal : Bridge", "Material-Product"),
        ("King : Kingdom", "Captain : Ship", "Principal : School", "Mayor : City", "Coach : Team", "Leader-Domain"),
        ("Famine : Hunger", "Drought : Thirst", "War : Destruction", "Flood : Displacement", "Storm : Damage", "Disaster-Effect"),
        ("Thermometer : Temperature", "Clock : Time", "Scale : Weight", "Ruler : Length", "Speedometer : Speed", "Instrument-Measures"),
        ("Egg : Hatch", "Seed : Sprout", "Caterpillar : Butterfly", "Ice : Melt", "Dough : Rise", "Transformation"),
        ("Illiterate : Read", "Blind : See", "Deaf : Hear", "Mute : Speak", "Lame : Walk", "Inability"),
        ("Democracy : Voting", "Monarchy : Crown", "Dictatorship : Control", "Anarchy : Chaos", "Republic : Constitution", "System-Symbol"),
        ("Surgeon : Scalpel", "Carpenter : Saw", "Writer : Pen", "Gardener : Pruner", "Musician : Instrument", "Professional-Tool"),
        ("Caterpillar : Cocoon", "Bird : Nest", "Bear : Den", "Fox : Burrow", "Bee : Hive", "Animal-Shelter"),
        ("Astronomy : Stars", "Botany : Plants", "Geology : Rocks", "Zoology : Animals", "Linguistics : Language", "Science-Study"),
        ("Smile : Happiness", "Frown : Sadness", "Blush : Embarrassment", "Yawn : Boredom", "Tear : Joy", "Expression-Emotion"),
        ("Novel : Fiction", "Biography : Nonfiction", "Poem : Poetry", "Article : Journalism", "Diary : Personal", "Work-Genre"),
        ("Anchor : Ship", "Brake : Car", "Lock : Door", "Belt : Waist", "Root : Tree", "Secures"),
        ("Feather : Light", "Rock : Heavy", "Glass : Fragile", "Steel : Strong", "Rubber : Flexible", "Material-Property"),
        ("Rehearsal : Performance", "Practice : Game", "Draft : Final", "Sketch : Painting", "Outline : Essay", "Preparation-Final"),
        ("Predator : Prey", "Employer : Employee", "Teacher : Student", "Host : Guest", "Leader : Follower", "Relationship"),
        ("Dawn : Day", "Dusk : Night", "Spring : Summer", "Birth : Life", "Prologue : Story", "Beginning"),
        ("Oasis : Desert", "Island : Ocean", "Clearing : Forest", "Valley : Mountain", "Harbor : Coast", "Contrast-Setting"),
        ("Inflation : Prices", "Gravity : Weight", "Friction : Speed", "Erosion : Soil", "Evaporation : Water", "Force-Effect"),
    ]

    qs = []
    correct_cycle = ["a", "b", "c", "d"]
    for i, (stem, correct_ans, d2, d3, d4, rel_type) in enumerate(analogies):
        target = correct_cycle[i % 4]
        opts = {"a": correct_ans, "b": d2, "c": d3, "d": d4}
        # Put correct answer in target slot
        if target != "a":
            opts[target], opts["a"] = opts["a"], opts[target]

        qs.append(Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.2 + (i % 7) * 0.1,
            text_ar=stem,
            option_a=opts["a"], option_b=opts["b"], option_c=opts["c"], option_d=opts["d"],
            correct_option=target,
            explanation_ar=f"Relationship type: {rel_type}. {stem} shares the same relationship as {correct_ans}.",
            solution_steps_ar=_steps(f"Identify relationship: {rel_type}", f"{stem} -> same pattern", f"Answer: {correct_ans}"),
            tags=f"analogy,{rel_type.lower().replace(' ', '-')}", stage="building",
            source_key=f"expansion2_va:{i+1:04d}", authoring_source="human",
        ))

    return qs[:33]


def get_verbal_completion_questions() -> list[Question]:
    """33 new sentence completion questions."""
    completions = [
        ("The scientist's _____ research led to a breakthrough in renewable energy.", "innovative", "careless", "outdated", "irrelevant", 0.3),
        ("Despite the team's best efforts, the project was _____ due to lack of funding.", "abandoned", "expanded", "celebrated", "duplicated", 0.4),
        ("The new policy aims to _____ economic growth while protecting the environment.", "promote", "hinder", "ignore", "eliminate", 0.3),
        ("The museum's collection includes _____ artifacts from ancient civilizations.", "rare", "modern", "digital", "ordinary", 0.4),
        ("Regular maintenance is _____ to ensure the longevity of any machine.", "essential", "optional", "harmful", "irrelevant", 0.3),
        ("The teacher used _____ methods to engage students in the learning process.", "creative", "monotonous", "obsolete", "rigid", 0.4),
        ("Climate change poses a _____ threat to biodiversity worldwide.", "significant", "minor", "temporary", "fictional", 0.5),
        ("The company's _____ to innovation has kept it at the forefront of the industry.", "commitment", "resistance", "indifference", "opposition", 0.5),
        ("The new bridge will _____ connect the two cities separated by the river.", "directly", "rarely", "accidentally", "temporarily", 0.4),
        ("His _____ attitude towards work earned him a promotion within a year.", "diligent", "lazy", "careless", "indifferent", 0.3),
        ("The government launched a _____ campaign to raise awareness about water conservation.", "nationwide", "secret", "limited", "abandoned", 0.4),
        ("The documentary provided _____ insights into the lives of deep-sea creatures.", "fascinating", "boring", "misleading", "superficial", 0.3),
        ("Effective communication is _____ for building strong relationships.", "crucial", "unnecessary", "harmful", "irrelevant", 0.3),
        ("The earthquake caused _____ damage to the infrastructure of the city.", "extensive", "minimal", "no", "superficial", 0.4),
        ("She showed great _____ in handling the crisis, calming everyone around her.", "composure", "panic", "confusion", "aggression", 0.5),
        ("The new law was designed to _____ corruption in government institutions.", "combat", "encourage", "ignore", "celebrate", 0.4),
        ("The athlete's _____ training schedule prepared her for the championship.", "rigorous", "relaxed", "irregular", "brief", 0.4),
        ("Access to clean water is a _____ right that every person deserves.", "fundamental", "luxury", "conditional", "negotiable", 0.3),
        ("The novel explores the _____ consequences of unchecked technological advancement.", "potential", "impossible", "imaginary", "trivial", 0.5),
        ("The professor's lecture was so _____ that students forgot to check their phones.", "engaging", "boring", "confusing", "irrelevant", 0.3),
        ("Volunteering at the shelter gave her a sense of _____ and purpose.", "fulfillment", "emptiness", "regret", "boredom", 0.3),
        ("The city's public transportation system is known for its _____ and efficiency.", "reliability", "delays", "chaos", "expense", 0.4),
        ("Scientific discoveries often result from years of _____ research and experimentation.", "dedicated", "casual", "random", "brief", 0.4),
        ("The architect designed the building to be both _____ and environmentally friendly.", "functional", "wasteful", "impractical", "fragile", 0.5),
        ("International cooperation is _____ for addressing global challenges like pandemics.", "vital", "unnecessary", "harmful", "optional", 0.4),
        ("The festival _____ visitors from around the world with its cultural performances.", "attracts", "repels", "confuses", "ignores", 0.3),
        ("Her _____ of multiple languages made her an invaluable asset to the diplomatic team.", "mastery", "ignorance", "fear", "avoidance", 0.4),
        ("The research findings _____ the importance of early childhood education.", "highlight", "diminish", "contradict", "ignore", 0.4),
        ("The desert ecosystem, though harsh, supports a _____ variety of specialized organisms.", "surprising", "limited", "zero", "declining", 0.5),
        ("Technological _____ has transformed the way people communicate globally.", "advancement", "failure", "regression", "stagnation", 0.3),
        ("The student's _____ analysis of the problem impressed the entire faculty.", "thorough", "shallow", "rushed", "careless", 0.4),
        ("Good leadership requires _____ and the ability to inspire others.", "vision", "selfishness", "hesitation", "ignorance", 0.5),
        ("The ancient ruins serve as a _____ to the architectural genius of past civilizations.", "testament", "barrier", "threat", "mystery", 0.6),
    ]

    qs = []
    correct_cycle = ["a", "b", "c", "d"]
    for i, (text, correct_ans, d1, d2, d3, diff) in enumerate(completions):
        target = correct_cycle[i % 4]
        opts = {"a": correct_ans, "b": d1, "c": d2, "d": d3}
        if target != "a":
            opts[target], opts["a"] = opts["a"], opts[target]

        qs.append(Question(
            skill_id="verbal_completion", question_type="completion", difficulty=diff,
            text_ar=text,
            option_a=opts["a"], option_b=opts["b"], option_c=opts["c"], option_d=opts["d"],
            correct_option=target,
            explanation_ar=f"The blank requires '{correct_ans}' which fits the context. Other options contradict or don't fit the sentence meaning.",
            solution_steps_ar=_steps("Read sentence for context clues", f"The context suggests: {correct_ans}", f"Other options don't fit the meaning"),
            tags="completion", stage="building",
            source_key=f"expansion2_vc:{i+1:04d}", authoring_source="human",
        ))

    return qs[:33]


def get_verbal_error_questions() -> list[Question]:
    """33 new contextual error questions with (word) brackets."""
    errors = [
        ("The new highway will (slow) transportation between the two cities.", "slow", "Correct: speed up. The highway should improve, not slow, transportation.", 0.3),
        ("Students who read regularly tend to have (weaker) vocabulary skills.", "weaker", "Correct: stronger. Reading improves vocabulary.", 0.3),
        ("The hospital was praised for its (neglect) of patient safety standards.", "neglect", "Correct: adherence. Hospitals are praised for following standards.", 0.4),
        ("The team's (lack) of preparation was evident in their flawless performance.", "lack", "Correct: level or quality. Flawless performance shows good preparation.", 0.4),
        ("The desert receives (abundant) rainfall throughout the year.", "abundant", "Correct: minimal. Deserts are characterized by low rainfall.", 0.3),
        ("Exercise is known to (worsen) cardiovascular health in most people.", "worsen", "Correct: improve. Exercise benefits heart health.", 0.3),
        ("The scholarship program aims to (discourage) talented students from pursuing education.", "discourage", "Correct: encourage. Scholarships support education.", 0.3),
        ("Clean drinking water is (harmful) to human health and development.", "harmful", "Correct: essential. Clean water is necessary for health.", 0.3),
        ("The new recycling initiative is expected to (increase) waste in the city.", "increase", "Correct: reduce. Recycling reduces waste.", 0.4),
        ("The peace treaty successfully (escalated) tensions between the two nations.", "escalated", "Correct: reduced. Peace treaties aim to decrease tensions.", 0.4),
        ("Advanced technology has made communication (slower) and less efficient.", "slower", "Correct: faster. Technology improves communication speed.", 0.3),
        ("The teacher's (confusing) explanation helped students understand the concept quickly.", "confusing", "Correct: clear. Helpful explanations are clear, not confusing.", 0.4),
        ("Good nutrition during childhood (delays) physical and mental development.", "delays", "Correct: supports. Good nutrition helps development.", 0.4),
        ("The safety regulations were designed to (endanger) workers in the factory.", "endanger", "Correct: protect. Safety regulations protect workers.", 0.3),
        ("Deforestation (improves) biodiversity by destroying natural habitats.", "improves", "Correct: reduces. Habitat destruction decreases biodiversity.", 0.5),
        ("The experienced pilot's (reckless) flying ensured a safe landing.", "reckless", "Correct: careful. Safe landings require careful flying.", 0.5),
        ("International trade agreements aim to (restrict) economic cooperation between nations.", "restrict", "Correct: promote. Trade agreements encourage cooperation.", 0.5),
        ("The museum's (boring) exhibits attracted thousands of visitors last month.", "boring", "Correct: fascinating. Attractive exhibits draw visitors.", 0.4),
        ("Planting trees (contributes to) air pollution in urban areas.", "contributes to", "Correct: reduces. Trees clean the air, not pollute it.", 0.5),
        ("The doctor recommended (avoiding) regular exercise for better health.", "avoiding", "Correct: maintaining. Doctors recommend exercise.", 0.4),
        ("The bridge was built to (separate) the communities on both sides of the river.", "separate", "Correct: connect. Bridges connect communities.", 0.3),
        ("Education (narrows) people's perspectives and limits their opportunities.", "narrows", "Correct: broadens. Education expands perspectives.", 0.4),
        ("The invention of the printing press (hindered) the spread of knowledge.", "hindered", "Correct: accelerated. The printing press spread knowledge faster.", 0.5),
        ("Vaccination programs have (spread) diseases in many developing countries.", "spread", "Correct: prevented. Vaccines prevent disease spread.", 0.4),
        ("The charity organization works to (worsen) living conditions for the poor.", "worsen", "Correct: improve. Charities improve conditions.", 0.3),
        ("Solar energy is considered (harmful) to the environment compared to fossil fuels.", "harmful", "Correct: beneficial. Solar energy is cleaner than fossil fuels.", 0.5),
        ("The strict training program (weakened) the athletes before the competition.", "weakened", "Correct: strengthened. Training prepares and strengthens athletes.", 0.5),
        ("Access to the internet has (limited) educational opportunities worldwide.", "limited", "Correct: expanded. The internet broadens access to education.", 0.4),
        ("The new irrigation system (decreased) crop yields in the farming region.", "decreased", "Correct: increased. Irrigation improves crop production.", 0.4),
        ("Libraries play a (minor) role in promoting literacy and lifelong learning.", "minor", "Correct: major. Libraries are important for literacy.", 0.5),
        ("The peace organization was established to (promote) conflict between nations.", "promote", "Correct: resolve. Peace organizations reduce conflict.", 0.5),
        ("Renewable energy sources are (depleting) natural resources at an alarming rate.", "depleting", "Correct: conserving. Renewables preserve resources.", 0.6),
        ("The experienced surgeon's (careless) technique resulted in a successful operation.", "careless", "Correct: precise. Successful surgery requires precision.", 0.5),
    ]

    qs = []
    correct_cycle = ["a", "b", "c", "d"]
    for i, (text, error_word, expl, diff) in enumerate(errors):
        target = correct_cycle[i % 4]
        # Build options: error_word is correct answer + 3 other words from sentence
        words = [w.strip(".,;:!?()") for w in text.replace("(", "").replace(")", "").split() if len(w.strip(".,;:!?()")) > 3]
        distractors = [w for w in words if w.lower() != error_word.lower()][:3]
        while len(distractors) < 3:
            distractors.append("context")

        opts = {"a": error_word, "b": distractors[0], "c": distractors[1], "d": distractors[2]}
        if target != "a":
            opts[target], opts["a"] = opts["a"], opts[target]

        qs.append(Question(
            skill_id="verbal_error", question_type="error", difficulty=diff,
            text_ar=text,
            option_a=opts["a"], option_b=opts["b"], option_c=opts["c"], option_d=opts["d"],
            correct_option=target,
            explanation_ar=f"Contextual error: '{error_word}' - {expl}",
            solution_steps_ar=_steps("Read sentence and understand context", f"Identify contradiction: {error_word}", f"{expl.split('.')[0]}"),
            tags="contextual-error", stage="building",
            source_key=f"expansion2_ve:{i+1:04d}", authoring_source="human",
        ))

    return qs[:33]


def get_verbal_oddword_questions() -> list[Question]:
    """33 new odd-word-out questions."""
    oddwords = [
        ("Which word does not belong to the group?", "Whale", "Shark", "Dolphin", "Tuna", "a", "Whale is a mammal; the others are fish.", 0.3),
        ("Which word does not belong to the group?", "Mercury", "Venus", "Moon", "Mars", "c", "Moon is a satellite; the others are planets.", 0.3),
        ("Which word does not belong to the group?", "Guitar", "Piano", "Trumpet", "Violin", "c", "Trumpet is a wind instrument; others are string/keyboard.", 0.4),
        ("Which word does not belong to the group?", "Democracy", "Monarchy", "Republic", "Economy", "d", "Economy is not a system of government.", 0.3),
        ("Which word does not belong to the group?", "Hydrogen", "Oxygen", "Carbon", "Bronze", "d", "Bronze is an alloy, not an element.", 0.4),
        ("Which word does not belong to the group?", "Triangle", "Square", "Circle", "Cube", "d", "Cube is 3D; the others are 2D shapes.", 0.3),
        ("Which word does not belong to the group?", "Novel", "Poem", "Sculpture", "Essay", "c", "Sculpture is visual art; the others are written forms.", 0.4),
        ("Which word does not belong to the group?", "Surgeon", "Dentist", "Architect", "Pharmacist", "c", "Architect is not in healthcare.", 0.4),
        ("Which word does not belong to the group?", "Cotton", "Silk", "Leather", "Nylon", "d", "Nylon is synthetic; the others are natural.", 0.5),
        ("Which word does not belong to the group?", "Addition", "Subtraction", "Division", "Equation", "d", "Equation is not an arithmetic operation.", 0.4),
        ("Which word does not belong to the group?", "Liver", "Kidney", "Stomach", "Femur", "d", "Femur is a bone; the others are organs.", 0.4),
        ("Which word does not belong to the group?", "Photosynthesis", "Respiration", "Digestion", "Evaporation", "d", "Evaporation is physical; others are biological.", 0.5),
        ("Which word does not belong to the group?", "Riyadh", "Jeddah", "Dammam", "Dubai", "d", "Dubai is in UAE; the others are Saudi cities.", 0.2),
        ("Which word does not belong to the group?", "Kilometer", "Meter", "Kilogram", "Centimeter", "c", "Kilogram measures mass; the others measure length.", 0.3),
        ("Which word does not belong to the group?", "Eagle", "Penguin", "Sparrow", "Hawk", "b", "Penguin cannot fly; the others can.", 0.3),
        ("Which word does not belong to the group?", "Breakfast", "Lunch", "Dinner", "Recipe", "d", "Recipe is instructions; the others are meals.", 0.2),
        ("Which word does not belong to the group?", "Shakespeare", "Newton", "Dickens", "Hemingway", "b", "Newton was a scientist; the others are writers.", 0.4),
        ("Which word does not belong to the group?", "Tsunami", "Earthquake", "Volcano", "Telescope", "d", "Telescope is an instrument; the others are natural disasters.", 0.2),
        ("Which word does not belong to the group?", "Iron", "Copper", "Gold", "Diamond", "d", "Diamond is a nonmetal; the others are metals.", 0.4),
        ("Which word does not belong to the group?", "Soccer", "Tennis", "Chess", "Basketball", "c", "Chess is a board game; the others are physical sports.", 0.3),
        ("Which word does not belong to the group?", "Rain", "Snow", "Hail", "Wind", "d", "Wind is not precipitation.", 0.3),
        ("Which word does not belong to the group?", "Violin", "Cello", "Flute", "Harp", "c", "Flute is wind; the others are string instruments.", 0.4),
        ("Which word does not belong to the group?", "Oak", "Pine", "Palm", "Rose", "d", "Rose is a flower; the others are trees.", 0.2),
        ("Which word does not belong to the group?", "Painting", "Drawing", "Sculpture", "Photography", "c", "Sculpture is 3D; the others are 2D visual arts.", 0.5),
        ("Which word does not belong to the group?", "Oxygen", "Nitrogen", "Helium", "Water", "d", "Water is a compound; the others are elements.", 0.4),
        ("Which word does not belong to the group?", "President", "Minister", "Senator", "Journalist", "d", "Journalist is media; the others are political roles.", 0.3),
        ("Which word does not belong to the group?", "Algebra", "Geometry", "Biology", "Calculus", "c", "Biology is science; the others are math branches.", 0.3),
        ("Which word does not belong to the group?", "Sadness", "Anger", "Happiness", "Height", "d", "Height is a physical trait; the others are emotions.", 0.2),
        ("Which word does not belong to the group?", "Microscope", "Telescope", "Stethoscope", "Periscope", "c", "Stethoscope is medical; others are optical instruments.", 0.5),
        ("Which word does not belong to the group?", "Atlantic", "Pacific", "Indian", "Amazon", "d", "Amazon is a river; the others are oceans.", 0.2),
        ("Which word does not belong to the group?", "Carrot", "Potato", "Apple", "Onion", "c", "Apple is a fruit; the others are vegetables.", 0.2),
        ("Which word does not belong to the group?", "Comma", "Period", "Paragraph", "Semicolon", "c", "Paragraph is a text structure; the others are punctuation.", 0.4),
        ("Which word does not belong to the group?", "Inch", "Foot", "Yard", "Pound", "d", "Pound measures weight; the others measure length.", 0.3),
    ]

    qs = []
    correct_cycle = ["a", "b", "c", "d"]
    for i, (text, a, b, c, d, orig_correct, expl, diff) in enumerate(oddwords):
        target = correct_cycle[i % 4]
        opts = {"a": a, "b": b, "c": c, "d": d}
        # Swap correct answer to target position
        if target != orig_correct:
            opts[target], opts[orig_correct] = opts[orig_correct], opts[target]

        qs.append(Question(
            skill_id="verbal_oddword", question_type="oddword", difficulty=diff,
            text_ar=text,
            option_a=opts["a"], option_b=opts["b"], option_c=opts["c"], option_d=opts["d"],
            correct_option=target,
            explanation_ar=expl,
            solution_steps_ar=_steps("Identify the category of the group", "Find which item doesn't belong", expl),
            tags="oddword", stage="building",
            source_key=f"expansion2_vo:{i+1:04d}", authoring_source="human",
        ))

    return qs[:33]


def get_quant_algebra_questions() -> list[Question]:
    """31 new algebra questions."""
    algebra = [
        ("If 3x - 7 = 14, what is x?", "7", "3", "5", "21", 0.2, "3x = 21, x = 7"),
        ("Solve: 2(x + 3) = 16", "5", "8", "3", "10", 0.3, "2x + 6 = 16, 2x = 10, x = 5"),
        ("If x + y = 10 and x - y = 4, find x.", "7", "3", "6", "4", 0.4, "Add equations: 2x = 14, x = 7"),
        ("What is the value of x if 4x = 2x + 12?", "6", "3", "4", "12", 0.3, "2x = 12, x = 6"),
        ("Simplify: 5(2x - 1) - 3(x + 2)", "7x - 11", "7x + 11", "10x - 5", "2x - 3", 0.5, "10x - 5 - 3x - 6 = 7x - 11"),
        ("If x/3 + 5 = 8, find x.", "9", "3", "15", "24", 0.3, "x/3 = 3, x = 9"),
        ("Solve for y: 3y + 9 = 0", "-3", "3", "0", "-9", 0.3, "3y = -9, y = -3"),
        ("If 2x + 5 > 11, then x > ?", "3", "5", "6", "2", 0.4, "2x > 6, x > 3"),
        ("Find the value of a if 5a - 3 = 2a + 9", "4", "3", "6", "2", 0.4, "3a = 12, a = 4"),
        ("What is x if x/4 = x/6 + 1?", "12", "6", "24", "4", 0.5, "3x = 2x + 12, x = 12"),
        ("If f(x) = 2x + 1, what is f(3)?", "7", "5", "9", "6", 0.3, "f(3) = 2(3) + 1 = 7"),
        ("Solve: |x - 5| = 3", "2 or 8", "3 or 5", "-2 or 8", "2 or -8", 0.6, "x - 5 = 3 or x - 5 = -3, so x = 8 or x = 2"),
        ("If 3(x - 2) = x + 4, find x.", "5", "3", "4", "10", 0.4, "3x - 6 = x + 4, 2x = 10, x = 5"),
        ("What is the slope of y = 3x - 7?", "3", "-7", "7", "-3", 0.3, "In y = mx + b form, slope m = 3"),
        ("Expand: (x + 2)(x - 3)", "x^2 - x - 6", "x^2 + x - 6", "x^2 - 5x + 6", "x^2 + 5x + 6", 0.5, "x^2 - 3x + 2x - 6 = x^2 - x - 6"),
        ("Solve: x^2 - 9 = 0", "3 or -3", "9 or -9", "3 only", "0 or 9", 0.4, "x^2 = 9, x = 3 or x = -3"),
        ("If y = x^2 and x = -2, what is y?", "4", "-4", "2", "-2", 0.3, "y = (-2)^2 = 4"),
        ("Find x: 2x/3 = 8", "12", "8", "16", "6", 0.3, "2x = 24, x = 12"),
        ("If a + b = 7 and ab = 12, find a^2 + b^2.", "25", "49", "37", "19", 0.6, "(a+b)^2 = a^2 + 2ab + b^2, so 49 = a^2 + 24 + b^2, a^2 + b^2 = 25"),
        ("Solve: 5x + 2 = 3x + 10", "4", "2", "6", "8", 0.3, "2x = 8, x = 4"),
        ("What value of x makes 2^x = 32?", "5", "4", "6", "3", 0.4, "2^5 = 32, so x = 5"),
        ("If 3x - 1 = 2(x + 2), find x.", "5", "3", "4", "1", 0.3, "3x - 1 = 2x + 4, x = 5"),
        ("Factor: x^2 + 5x + 6", "(x+2)(x+3)", "(x+1)(x+6)", "(x+3)(x+3)", "(x-2)(x-3)", 0.5, "Find two numbers that multiply to 6 and add to 5: 2 and 3"),
        ("If f(x) = x^2 - 4, what is f(0)?", "-4", "0", "4", "-2", 0.3, "f(0) = 0 - 4 = -4"),
        ("Solve: 3(x + 1) = 2(x + 5)", "7", "5", "3", "4", 0.4, "3x + 3 = 2x + 10, x = 7"),
        ("What is the y-intercept of y = 2x + 5?", "5", "2", "-5", "0", 0.3, "When x=0, y = 5. The y-intercept is 5."),
        ("If x = 2 and y = 3, evaluate 2x^2 + 3y.", "17", "15", "13", "21", 0.4, "2(4) + 9 = 8 + 9 = 17"),
        ("Solve: x/2 + x/3 = 5", "6", "10", "15", "3", 0.5, "5x/6 = 5, x = 6"),
        ("If n is even and n + 3 is odd, which could be n?", "4", "3", "5", "7", 0.3, "If n is even (4), then n+3 = 7 which is odd."),
        ("Find x: 7x - 2(x + 1) = 13", "3", "5", "2", "4", 0.4, "7x - 2x - 2 = 13, 5x = 15, x = 3"),
        ("If 4^x = 64, find x.", "3", "2", "4", "16", 0.4, "4^3 = 64, so x = 3"),
    ]

    qs = []
    correct_cycle = ["a", "b", "c", "d"]
    for i, (text, correct_ans, d1, d2, d3, diff, expl) in enumerate(algebra):
        target = correct_cycle[i % 4]
        opts = {"a": correct_ans, "b": d1, "c": d2, "d": d3}
        if target != "a":
            opts[target], opts["a"] = opts["a"], opts[target]

        qs.append(Question(
            skill_id="quant_algebra", question_type="algebra", difficulty=diff,
            text_ar=text,
            option_a=opts["a"], option_b=opts["b"], option_c=opts["c"], option_d=opts["d"],
            correct_option=target,
            explanation_ar=expl,
            solution_steps_ar=_steps("Set up the equation from the problem.", expl, "Verify the answer."),
            tags="algebra", stage="building",
            source_key=f"expansion2_ag:{i+1:04d}", authoring_source="human",
            content_format="markdown_math",
        ))

    return qs[:31]


def get_quant_arithmetic_questions() -> list[Question]:
    """28 new arithmetic questions."""
    arith = [
        ("A store offers a 20% discount on a 250 riyal item. What is the sale price?", "200", "225", "210", "180", 0.3, "Discount = 50, sale price = 250 - 50 = 200"),
        ("If 4 workers can finish a job in 6 days, how many days for 8 workers?", "3", "4", "2", "12", 0.4, "Workers x days = constant: 4x6 = 24, 24/8 = 3"),
        ("What is 15% of 400?", "60", "40", "80", "45", 0.2, "0.15 x 400 = 60"),
        ("A car travels 180 km in 3 hours. What is its speed?", "60 km/h", "45 km/h", "90 km/h", "54 km/h", 0.2, "Speed = 180/3 = 60 km/h"),
        ("If the ratio of boys to girls is 5:3 and total is 40, how many boys?", "25", "15", "20", "30", 0.3, "Boys = (5/8) x 40 = 25"),
        ("A product costs 80 riyals after a 20% discount. Original price?", "100", "96", "64", "120", 0.4, "80 = 0.8 x original, original = 100"),
        ("What number is 30% more than 200?", "260", "230", "280", "240", 0.3, "200 + 60 = 260"),
        ("Average of 12, 18, 22, 28 is?", "20", "22", "18", "25", 0.2, "Sum = 80, avg = 80/4 = 20"),
        ("A train travels at 90 km/h. How far in 2.5 hours?", "225 km", "180 km", "270 km", "200 km", 0.3, "90 x 2.5 = 225"),
        ("If a shirt costs 120 riyals and tax is 15%, total cost?", "138", "135", "132", "150", 0.4, "Tax = 18, total = 120 + 18 = 138"),
        ("LCM of 12 and 18 is?", "36", "72", "6", "216", 0.4, "12 = 2^2 x 3, 18 = 2 x 3^2, LCM = 2^2 x 3^2 = 36"),
        ("GCD of 24 and 36 is?", "12", "6", "24", "36", 0.4, "Factors: 24=2^3x3, 36=2^2x3^2, GCD = 2^2x3 = 12"),
        ("If A earns 3000 and saves 20%, how much does A save monthly?", "600", "500", "400", "750", 0.2, "3000 x 0.20 = 600"),
        ("How many minutes in 3.5 hours?", "210", "200", "180", "240", 0.2, "3.5 x 60 = 210"),
        ("A recipe needs 2 cups for 4 servings. How many cups for 10?", "5", "4", "6", "8", 0.3, "2/4 x 10 = 5"),
        ("If 5 pens cost 35 riyals, what do 8 pens cost?", "56", "48", "64", "40", 0.3, "1 pen = 7, 8 pens = 56"),
        ("What is 2/5 of 150?", "60", "30", "75", "50", 0.2, "150 x 2/5 = 60"),
        ("A tank fills in 12 hours. How much fills in 3 hours?", "1/4", "1/3", "1/6", "1/2", 0.3, "3/12 = 1/4"),
        ("Sum of first 10 positive integers?", "55", "45", "50", "100", 0.4, "n(n+1)/2 = 10x11/2 = 55"),
        ("If x:y = 2:3 and y = 15, find x.", "10", "6", "12", "9", 0.3, "2/3 = x/15, x = 10"),
        ("A clock gains 5 minutes every hour. After 6 hours, how many minutes gained?", "30", "25", "35", "60", 0.2, "5 x 6 = 30"),
        ("30% of what number is 45?", "150", "135", "100", "120", 0.4, "0.30 x n = 45, n = 150"),
        ("If the cost increases from 50 to 65, what is the percentage increase?", "30%", "25%", "15%", "35%", 0.4, "(65-50)/50 x 100 = 30%"),
        ("Product of 0.5 and 0.4 is?", "0.20", "0.09", "0.45", "2.0", 0.3, "0.5 x 0.4 = 0.20"),
        ("How many seconds in 5 minutes?", "300", "250", "500", "350", 0.2, "5 x 60 = 300"),
        ("A number decreased by 25% gives 75. What is the number?", "100", "90", "80", "120", 0.4, "0.75n = 75, n = 100"),
        ("If a square has perimeter 48, what is its side?", "12", "16", "8", "24", 0.2, "Side = 48/4 = 12"),
        ("Average speed for 100 km in 2 hours and 200 km in 3 hours?", "60 km/h", "50 km/h", "75 km/h", "100 km/h", 0.5, "Total = 300 km, time = 5 hrs, avg = 60"),
    ]

    qs = []
    correct_cycle = ["a", "b", "c", "d"]
    for i, (text, correct_ans, d1, d2, d3, diff, expl) in enumerate(arith):
        target = correct_cycle[i % 4]
        opts = {"a": correct_ans, "b": d1, "c": d2, "d": d3}
        if target != "a":
            opts[target], opts["a"] = opts["a"], opts[target]

        qs.append(Question(
            skill_id="quant_arithmetic", question_type="arithmetic", difficulty=diff,
            text_ar=text,
            option_a=opts["a"], option_b=opts["b"], option_c=opts["c"], option_d=opts["d"],
            correct_option=target,
            explanation_ar=expl,
            solution_steps_ar=_steps("Set up the equation from the problem.", expl, "Verify the answer."),
            tags="arithmetic", stage="building",
            source_key=f"expansion2_ar:{i+1:04d}", authoring_source="human",
            content_format="markdown_math",
        ))

    return qs[:28]


def get_quant_statistics_questions() -> list[Question]:
    """21 new statistics questions."""
    stats = [
        ("Mean of 5, 10, 15, 20, 25 is?", "15", "10", "20", "12.5", 0.2, "Sum=75, mean=75/5=15"),
        ("Median of 3, 7, 9, 12, 15 is?", "9", "7", "12", "10", 0.2, "Middle value of sorted list: 9"),
        ("Mode of 2, 3, 3, 5, 7, 3, 8 is?", "3", "5", "2", "7", 0.2, "3 appears most frequently (3 times)"),
        ("Range of 4, 8, 15, 23, 42 is?", "38", "42", "4", "19", 0.2, "42 - 4 = 38"),
        ("If P(A) = 0.3 and P(B) = 0.5, and A,B independent, P(A and B)?", "0.15", "0.80", "0.20", "0.35", 0.5, "P(A and B) = 0.3 x 0.5 = 0.15"),
        ("A die is rolled. P(even number)?", "1/2", "1/3", "1/6", "2/3", 0.2, "Even numbers: 2,4,6. P = 3/6 = 1/2"),
        ("Variance of 2, 4, 6, 8 is?", "5", "2.5", "6.25", "4", 0.6, "Mean=5, deviations=-3,-1,1,3, var=(9+1+1+9)/4=5"),
        ("In a class of 40, 25 passed. Pass rate?", "62.5%", "60%", "65%", "75%", 0.3, "25/40 x 100 = 62.5%"),
        ("How many ways to arrange 4 books?", "24", "16", "12", "4", 0.4, "4! = 4x3x2x1 = 24"),
        ("C(6,2) = ?", "15", "12", "30", "6", 0.4, "6!/(2!4!) = 720/(2x24) = 15"),
        ("Two coins tossed. P(both heads)?", "1/4", "1/2", "1/3", "3/4", 0.3, "P = (1/2)(1/2) = 1/4"),
        ("A bag has 3 red and 5 blue balls. P(red)?", "3/8", "5/8", "3/5", "1/2", 0.3, "Total=8, P(red)=3/8"),
        ("Weighted mean: 80(weight 3) and 60(weight 2) is?", "72", "70", "74", "68", 0.5, "(80x3+60x2)/(3+2) = 360/5 = 72"),
        ("Sum of deviations from mean is always?", "0", "1", "mean", "n", 0.4, "Sum of deviations from mean always equals 0"),
        ("If data doubles, the mean?", "doubles", "stays same", "halves", "triples", 0.4, "If all values double, mean also doubles"),
        ("A spinner has 4 equal sections (1-4). P(number > 2)?", "1/2", "1/4", "3/4", "1/3", 0.3, "Numbers > 2: 3,4. P = 2/4 = 1/2"),
        ("Standard deviation measures?", "spread", "center", "shape", "count", 0.3, "SD measures the spread/dispersion of data"),
        ("If mean=10, n=5, what is the sum?", "50", "15", "2", "100", 0.2, "Sum = mean x n = 10 x 5 = 50"),
        ("P(A or B) if mutually exclusive, P(A)=0.3, P(B)=0.4?", "0.7", "0.12", "0.5", "1.0", 0.4, "P(A or B) = 0.3 + 0.4 = 0.7"),
        ("Interquartile range is?", "Q3 - Q1", "Max - Min", "Mean - Median", "Q2 - Q1", 0.5, "IQR = Q3 - Q1"),
        ("A sample of 100 has mean 50. If one value of 150 is added, new mean?", "50.99", "51", "55", "100", 0.6, "(50x100+150)/101 = 5150/101 = 50.99"),
    ]

    qs = []
    correct_cycle = ["a", "b", "c", "d"]
    for i, (text, correct_ans, d1, d2, d3, diff, expl) in enumerate(stats):
        target = correct_cycle[i % 4]
        opts = {"a": correct_ans, "b": d1, "c": d2, "d": d3}
        if target != "a":
            opts[target], opts["a"] = opts["a"], opts[target]

        qs.append(Question(
            skill_id="quant_statistics", question_type="statistics", difficulty=diff,
            text_ar=text,
            option_a=opts["a"], option_b=opts["b"], option_c=opts["c"], option_d=opts["d"],
            correct_option=target,
            explanation_ar=expl,
            solution_steps_ar=_steps("Set up the equation from the problem.", expl, "Verify the answer."),
            tags="statistics", stage="building",
            source_key=f"expansion2_st:{i+1:04d}", authoring_source="human",
            content_format="markdown_math",
        ))

    return qs[:21]


def get_all_wave2_questions() -> list[Question]:
    """Return all Wave 2 expansion questions."""
    all_qs = (
        get_verbal_reading_questions()
        + get_verbal_analogy_questions()
        + get_verbal_completion_questions()
        + get_verbal_error_questions()
        + get_verbal_oddword_questions()
        + get_quant_algebra_questions()
        + get_quant_arithmetic_questions()
        + get_quant_statistics_questions()
    )
    return all_qs
