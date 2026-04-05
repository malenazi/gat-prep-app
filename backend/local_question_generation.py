import random
from collections import Counter
from typing import Any

from generated_question_bank import AUTHORING_SOURCE_AI, build_manifest
from question_generation import (
    PROMPT_VERSION_V1,
    SKILL_BLUEPRINTS,
    canonical_source_key,
    difficulty_targets,
    stage_targets,
)


def _shuffle_pool(items: list[Any], *, seed: str) -> list[Any]:
    pool = list(items)
    random.Random(seed).shuffle(pool)
    return pool


def _expand_targets(targets: dict[str, int], *, seed: str) -> list[str]:
    expanded: list[str] = []
    for key, count in targets.items():
        expanded.extend([key] * count)
    return _shuffle_pool(expanded, seed=seed)


def _difficulty_values(count: int, *, seed: str) -> list[float]:
    bucket_counts = difficulty_targets(count)
    palette = {
        "foundation": [0.08, 0.12, 0.16, 0.20, 0.24],
        "target_core": [0.28, 0.34, 0.40, 0.46, 0.52, 0.58],
        "challenging": [0.64, 0.70, 0.76],
        "stretch": [0.82, 0.88, 0.94],
    }
    values: list[float] = []
    for bucket, bucket_count in bucket_counts.items():
        colors = palette[bucket]
        for index in range(bucket_count):
            values.append(colors[index % len(colors)])
    return _shuffle_pool(values, seed=seed)


def _stage_values(count: int, *, seed: str) -> list[str]:
    return _expand_targets(stage_targets(count), seed=seed)


def _fraction(n: int, d: int) -> str:
    return f"$\\frac{{{n}}}{{{d}}}$"


def _option_pack(correct: str, distractors: list[str], *, seed: int) -> tuple[dict[str, str], str]:
    options = [correct] + distractors[:3]
    rotation = seed % 4
    options = options[rotation:] + options[:rotation]
    keys = ("a", "b", "c", "d")
    correct_key = keys[options.index(correct)]
    return {key: value for key, value in zip(keys, options)}, correct_key


def _question_payload(
    *,
    skill_id: str,
    question_type: str,
    blueprint_id: str,
    variant_index: int,
    batch_id: str,
    stage: str,
    difficulty: float,
    text_ar: str,
    correct_value: str,
    distractors: list[str],
    explanation_ar: str,
    tags: list[str],
    content_format: str = "markdown_math",
    passage_ar: str | None = None,
    solution_steps_ar: list[str] | None = None,
    table_ar: dict[str, Any] | None = None,
    table_caption: str | None = None,
) -> dict[str, Any]:
    options, correct_option = _option_pack(correct_value, distractors, seed=variant_index + len(blueprint_id))
    return {
        "source_key": canonical_source_key(skill_id, batch_id, variant_index + 1),
        "batch_id": batch_id,
        "generation_prompt_version": PROMPT_VERSION_V1,
        "authoring_source": AUTHORING_SOURCE_AI,
        "blueprint_id": blueprint_id,
        "variant_group": f"{blueprint_id}-{variant_index + 1:02d}",
        "skill_id": skill_id,
        "question_type": question_type,
        "difficulty": difficulty,
        "text_ar": text_ar,
        "passage_ar": passage_ar,
        "content_format": content_format,
        "figure_svg": None,
        "figure_alt": None,
        "table_ar": table_ar,
        "table_caption": table_caption,
        "comparison_columns": None,
        "option_a": options["a"],
        "option_b": options["b"],
        "option_c": options["c"],
        "option_d": options["d"],
        "correct_option": correct_option,
        "explanation_ar": explanation_ar,
        "solution_steps_ar": solution_steps_ar,
        "tags": ",".join(tags),
        "paper_only": False,
        "stage": stage,
        "status": "active",
    }


ARITH_CONTEXTS = {
    "percent-change": ["bookstore", "bakery", "science club", "library desk", "bike rental", "clinic", "museum desk", "training center", "sports kiosk", "coffee stall", "camp office", "art workshop", "flower stand", "music class", "garden shop"],
    "ratio-proportion": ["paint mix", "recipe", "seed packets", "gift bags", "study kits", "juice blend", "badge design", "bracelet set", "tile pattern", "desk layout", "photo album", "flower bed", "robot kit", "class roster", "snack box"],
    "unit-rate": ["printer", "delivery van", "water pump", "typing coach", "packing team", "school bus", "tour guide", "factory belt", "photo printer", "drone charger", "fitness coach", "movie editor", "service desk", "repair team", "courier route"],
    "profit-loss-discount": ["shoe store", "book fair", "gift stand", "uniform shop", "toy booth", "phone shop", "photo studio", "music store", "snack cart", "sports stall", "craft market", "repair shop", "online seller", "camp market", "stationery sale"],
}


def _arithmetic_item(blueprint_id: str, variant_index: int, stage: str, difficulty: float, batch_id: str) -> dict[str, Any]:
    seed = variant_index + 1
    if blueprint_id == "percent-change":
        before = 20 + seed * 4
        pct = [10, 20, 25, 40, 50][variant_index % 5]
        after = before * (100 + pct) // 100
        context = ARITH_CONTEXTS["percent-change"][variant_index % len(ARITH_CONTEXTS["percent-change"])]
        text = f"A {context} sold {before} items one day and {after} items the next day. What was the percent increase?"
        correct, distractors = f"{pct}%", [f"{pct - 5}%", f"{pct + 10}%", f"{after - before}%"]
        explanation = f"The increase is {after - before}. Divide by the original amount {before}: $\\frac{{{after-before}}}{{{before}}} = {pct}\\%$."
        steps = [f"Find the increase: {after} - {before} = {after - before}.", f"Divide by the original amount {before}.", f"Convert the result to {pct}%."]
        tags = ["generated", "percent", "change"]
    elif blueprint_id == "ratio-proportion":
        a = 2 + (variant_index % 4)
        b = 3 + ((variant_index + 1) % 5)
        factor = 6 + variant_index
        context = ARITH_CONTEXTS["ratio-proportion"][variant_index % len(ARITH_CONTEXTS["ratio-proportion"])]
        text = f"In a {context}, the ratio of blue parts to red parts is {a}:{b}. If there are {b * factor} red parts, how many blue parts are there?"
        correct, distractors = str(a * factor), [str(b * factor), str(a * factor + b), str(a * factor - a if a * factor - a > 0 else a * factor + a)]
        explanation = "Use the same scale factor on both sides of the ratio."
        steps = [f"{b} ratio units correspond to {b * factor}, so 1 unit is {factor}.", f"Multiply {a} by {factor} to get {a * factor}."]
        tags = ["generated", "ratio", "proportion"]
    elif blueprint_id == "fraction-equivalence":
        n = 1 + (variant_index % 5)
        d = n + 2 + (variant_index % 4)
        scale = 2 + (variant_index % 4)
        text = f"Which fraction is equivalent to { _fraction(n, d) }?"
        correct, distractors = _fraction(n * scale, d * scale), [_fraction(n * scale + 1, d * scale), _fraction(n, d + scale), _fraction(n * scale, d * scale + 1)]
        explanation = "Equivalent fractions multiply the numerator and denominator by the same number."
        steps = [f"Start with { _fraction(n, d) }.", f"Multiply the numerator and denominator by {scale}.", f"The result is { _fraction(n * scale, d * scale) }."]
        tags = ["generated", "fractions"]
    elif blueprint_id == "unit-rate":
        hours = 6 + variant_index
        rate = 4 + (variant_index % 5)
        total = hours * rate
        context = ARITH_CONTEXTS["unit-rate"][variant_index % len(ARITH_CONTEXTS["unit-rate"])]
        text = f"A {context} completes {total} tasks in {hours} hours. What is the unit rate in tasks per hour?"
        correct, distractors = str(rate), [str(hours), str(total), str(rate + 2)]
        explanation = "Unit rate means per 1 hour, so divide the total amount by the number of hours."
        steps = [f"Write the division: {total} ÷ {hours}.", f"The result is {rate} tasks per hour."]
        tags = ["generated", "unit-rate"]
    elif blueprint_id == "work-rate":
        first = 6 + (variant_index % 5)
        second = 8 + ((variant_index + 2) % 5)
        total_hours = round((first * second) / (first + second), 1)
        text = f"One worker finishes a job in {first} hours and another finishes the same job in {second} hours. About how many hours will they take together?"
        correct, distractors = f"{total_hours}", [f"{round((first + second) / 2, 1)}", f"{round(total_hours + 1.5, 1)}", f"{round(total_hours - 1.0, 1)}"]
        explanation = "Add the two hourly work rates, then divide 1 whole task by the combined rate."
        steps = [f"The combined rate is $\\frac{{1}}{{{first}}} + \\frac{{1}}{{{second}}}$.", "Take the reciprocal of the combined rate to find the time."]
        tags = ["generated", "work-rate"]
    elif blueprint_id == "average-and-mean":
        values = [12 + variant_index, 15 + variant_index, 18 + variant_index, 21 + variant_index]
        total = sum(values)
        mean = total // 4
        text = f"The scores are {', '.join(str(v) for v in values)}. What is the mean?"
        correct, distractors = str(mean), [str(values[1]), str(mean + 2), str(mean - 2)]
        explanation = "Add the values and divide by how many values there are."
        steps = [f"Add the scores to get {total}.", f"Divide by 4 to get {mean}."]
        tags = ["generated", "mean", "average"]
    elif blueprint_id == "mixed-operations":
        a = 18 + variant_index
        b = 3 + (variant_index % 4)
        c = 5 + (variant_index % 6)
        answer = (a // b) + c
        text = f"Evaluate $\\frac{{{a}}}{{{b}}} + {c}$."
        correct, distractors = str(answer), [str((a + c) // b), str((a // b) * c), str(answer + b)]
        explanation = "Use order of operations: divide first, then add."
        steps = [f"Compute {a} ÷ {b} = {a // b}.", f"Then add {c} to get {answer}."]
        tags = ["generated", "operations"]
    elif blueprint_id == "number-properties":
        base = 24 + variant_index * 2
        text, correct, distractors = f"Which value is definitely a factor of {base}?", "2", ["3", "5", "7"]
        explanation, steps, tags = "Any even number is divisible by 2.", [f"{base} is even.", "So 2 divides it exactly."], ["generated", "number-properties"]
    elif blueprint_id == "decimals-and-place-value":
        whole = 12 + variant_index
        tenths = (variant_index * 3 + 2) % 10
        value = f"{whole}.{tenths}"
        text = f"In the decimal {value}, what digit is in the tenths place?"
        correct, distractors = str(tenths), [str(whole % 10), str((tenths + 2) % 10), str((tenths + 5) % 10)]
        explanation, steps, tags = "The tenths place is the first digit to the right of the decimal point.", [f"Look at {value}.", f"The first digit after the decimal is {tenths}."], ["generated", "decimals"]
    elif blueprint_id == "profit-loss-discount":
        cost = 20 + variant_index * 3
        profit = 6 + (variant_index % 5)
        context = ARITH_CONTEXTS["profit-loss-discount"][variant_index % len(ARITH_CONTEXTS["profit-loss-discount"])]
        text = f"A {context} bought an item for {cost} riyals and sold it for {cost + profit} riyals. What was the profit?"
        correct, distractors = str(profit), [str(cost), str(cost + profit), str(profit + 4)]
        explanation, steps, tags = "Profit equals selling price minus cost.", [f"Subtract the cost from the selling price: {cost + profit} - {cost}.", f"The profit is {profit}."], ["generated", "profit"]
    elif blueprint_id == "simple-interest":
        principal = 1000 + variant_index * 100
        rate = 4 + (variant_index % 4)
        years = 2 + (variant_index % 3)
        interest = principal * rate * years // 100
        text = f"A savings account earns simple interest on {principal} riyals at {rate}% per year for {years} years. How much interest is earned?"
        correct, distractors = str(interest), [str(principal * rate // 100), str(interest + 20), str(principal + interest)]
        explanation, steps, tags = "Use the simple-interest formula $I = Prt$.", [f"Compute one year of interest: {principal} × {rate}% = {principal * rate // 100}.", f"Multiply by {years} years to get {interest}."], ["generated", "interest"]
    else:
        speed = 40 + variant_index * 2
        hours = 2 + (variant_index % 4)
        distance = speed * hours
        text = f"A vehicle travels at {speed} km/h for {hours} hours. How far does it travel?"
        correct, distractors = str(distance), [str(speed + hours), str(distance - speed), str(distance + hours)]
        explanation, steps, tags = "Distance equals speed multiplied by time.", [f"Use $d = rt$.", f"{speed} × {hours} = {distance}."], ["generated", "speed", "distance", "time"]
    return _question_payload(
        skill_id="quant_arithmetic",
        question_type="arithmetic",
        blueprint_id=blueprint_id,
        variant_index=variant_index,
        batch_id=batch_id,
        stage=stage,
        difficulty=difficulty,
        text_ar=text,
        correct_value=correct,
        distractors=distractors,
        explanation_ar=explanation,
        solution_steps_ar=steps,
        tags=tags,
    )


def _algebra_item(blueprint_id: str, variant_index: int, stage: str, difficulty: float, batch_id: str) -> dict[str, Any]:
    if blueprint_id == "linear-equations":
        x = 4 + variant_index
        add = 4 + (variant_index % 5)
        text, correct, distractors = f"Solve $x + {add} = {x + add}$.", str(x), [str(x + add), str(add), str(x + 2)]
        explanation, steps = "Subtract the constant from both sides.", [f"Subtract {add} from both sides.", f"$x = {x}$."]
    elif blueprint_id == "two-step-equations":
        x = 2 + (variant_index % 9)
        mult = 2 + (variant_index % 4)
        add = 3 + ((variant_index + 2) % 5)
        total = mult * x + add
        text, correct, distractors = f"Solve ${mult}x + {add} = {total}$.", str(x), [str(total - add), str((total - add) // max(1, mult - 1)), str(x + 1)]
        explanation, steps = "Undo addition first, then divide by the coefficient.", [f"Subtract {add}: ${mult}x = {total - add}$.", f"Divide by {mult}: $x = {x}$."]
    elif blueprint_id == "systems-of-equations":
        x = 2 + (variant_index % 6)
        y = 5 + (variant_index % 7)
        text, correct, distractors = f"If $x + y = {x + y}$ and $y - x = {y - x}$, what is the value of $y$?", str(y), [str(x), str(x + y), str(y - x)]
        explanation, steps = "Add the equations to eliminate $x$.", [f"Adding the equations gives $2y = {x + y + y - x}$.", f"So $y = {y}$."]
    elif blueprint_id == "inequalities":
        base = 4 + (variant_index % 6)
        add = 3 + (variant_index % 4)
        text, correct, distractors = f"Which inequality is equivalent to $x + {add} > {base + add}$?", f"x > {base}", [f"x > {base + add}", f"x < {base}", f"x > {base + 2}"]
        explanation, steps = "Subtract the same number from both sides of the inequality.", [f"Subtract {add} from both sides.", f"This leaves $x > {base}$."]
    elif blueprint_id == "exponents-and-powers":
        base = 2 + (variant_index % 4)
        exp = 3 + (variant_index % 3)
        ans = base ** exp
        text, correct, distractors = f"What is ${base}^{{{exp}}}$?", str(ans), [str(base * exp), str(base ** (exp - 1)), str(ans + base)]
        explanation, steps = "Multiply the base by itself the indicated number of times.", [f"Write {base} multiplied by itself {exp} times.", f"The product is {ans}."]
    elif blueprint_id == "polynomials":
        x = 2 + (variant_index % 5)
        coeff = 3 + (variant_index % 4)
        add = 4 + ((variant_index + 1) % 5)
        ans = coeff * x + add
        text, correct, distractors = f"If $x = {x}$, what is the value of ${coeff}x + {add}$?", str(ans), [str(coeff * x), str(coeff + x + add), str(ans + coeff)]
        explanation, steps = "Substitute the value of $x$ into the expression.", [f"Replace $x$ with {x}.", f"Compute ${coeff}({x}) + {add} = {ans}$."]
    elif blueprint_id == "factoring":
        a = 2 + (variant_index % 4)
        b = 3 + ((variant_index + 1) % 5)
        text, correct, distractors = f"Which expression is equal to $x^2 + {a + b}x + {a * b}$?", f"$(x + {a})(x + {b})$", [f"$(x - {a})(x + {b})$", f"$(x + {a + b})(x + 1)$", f"$(x + {a*b})(x + 1)$"]
        explanation, steps = "Look for two numbers that add to the middle coefficient and multiply to the constant.", [f"{a} and {b} add to {a+b} and multiply to {a*b}.", f"So the factorization is $(x + {a})(x + {b})$."]
    elif blueprint_id == "quadratic-patterns":
        n = 2 + (variant_index % 5)
        ans = n * n
        text, correct, distractors = f"If the rule is $n^2$, what is the output when $n = {n}$?", str(ans), [str(2*n), str(ans + n), str(ans - 1)]
        explanation, steps = "Substitute the value of $n$ into the rule.", [f"Use the rule $n^2$.", f"${n}^2 = {ans}$."]
    elif blueprint_id == "function-tables":
        mult = 2 + (variant_index % 4)
        add = 1 + ((variant_index + 1) % 5)
        x = 3 + variant_index
        ans = mult * x + add
        text, correct, distractors = f"A function follows the rule $f(x) = {mult}x + {add}$. What is $f({x})$?", str(ans), [str(mult * x), str(mult + x + add), str(ans + add)]
        explanation, steps = "Substitute the input into the function rule.", [f"Replace $x$ with {x}.", f"${mult}({x}) + {add} = {ans}$."]
    elif blueprint_id == "sequence-rules":
        start = 4 + variant_index
        step = 3 + (variant_index % 4)
        ans = start + 3 * step
        text, correct, distractors = f"The sequence begins {start}, {start + step}, {start + 2 * step}, ... What is the next term?", str(ans), [str(start + step), str(start + 4 * step), str(ans - 1)]
        explanation, steps = "Find the common difference and keep adding it.", [f"The common difference is {step}.", f"Add {step} to {start + 2*step} to get {ans}."]
    elif blueprint_id == "algebraic-word-problems":
        notebooks = 4 + (variant_index % 5)
        note_price = 6 + (variant_index % 5)
        pen_price = 3 + (variant_index % 4)
        total = notebooks * note_price + pen_price
        text, correct, distractors = f"A student buys {notebooks} notebooks at {note_price} riyals each and one pen for {pen_price} riyals. Which expression gives the total cost?", f"${notebooks}({note_price}) + {pen_price}$", [f"${notebooks} + {note_price} + {pen_price}$", f"${notebooks}({pen_price}) + {note_price}$", f"${total}$"]
        explanation, steps = "Multiply the number of notebooks by the notebook price, then add the pen price.", [f"Notebook cost: {notebooks} × {note_price}.", f"Add {pen_price} for the pen."]
    else:
        x = 2 + (variant_index % 4)
        y = 5 + (variant_index % 5)
        ans = 2 * x + y
        text, correct, distractors = f"If $x = {x}$ and $y = {y}$, what is the value of $2x + y$?", str(ans), [str(x + y), str(2 * y + x), str(ans + 2)]
        explanation, steps = "Replace the variables with their values and simplify.", [f"Substitute $x = {x}$ and $y = {y}$.", f"$2({x}) + {y} = {ans}$."]
    return _question_payload(
        skill_id="quant_algebra",
        question_type="algebra",
        blueprint_id=blueprint_id,
        variant_index=variant_index,
        batch_id=batch_id,
        stage=stage,
        difficulty=difficulty,
        text_ar=text,
        correct_value=correct,
        distractors=distractors,
        explanation_ar=explanation,
        solution_steps_ar=steps,
        tags=["generated", "algebra", blueprint_id],
    )


def _statistics_item(blueprint_id: str, variant_index: int, stage: str, difficulty: float, batch_id: str) -> dict[str, Any]:
    table_ar = None
    table_caption = None
    if blueprint_id == "mean-median-mode":
        values = [6 + variant_index, 8 + variant_index, 8 + variant_index, 10 + variant_index, 12 + variant_index]
        mode = 8 + variant_index
        text, correct, distractors = f"For the data set {', '.join(str(v) for v in values)}, what is the mode?", str(mode), [str(values[0]), str(values[-1]), str(sum(values)//len(values))]
        explanation, steps = "The mode is the value that appears most often.", [f"{mode} appears more often than any other value.", f"So the mode is {mode}."]
    elif blueprint_id == "range-and-spread":
        low = 12 + variant_index
        high = low + 18 + (variant_index % 5)
        text, correct, distractors = f"The data values are {low}, {low+4}, {low+9}, {high}. What is the range?", str(high-low), [str(high), str(low), str(high-low+4)]
        explanation, steps = "Range is the greatest value minus the least value.", [f"Greatest: {high}; least: {low}.", f"{high} - {low} = {high-low}."]
    elif blueprint_id == "probability-basics":
        total = 10 + variant_index
        red = 2 + (variant_index % 5)
        text, correct, distractors = f"A bag contains {red} red marbles and {total-red} blue marbles. What is the probability of selecting a red marble?", _fraction(red, total), [_fraction(total-red, total), _fraction(red, total-red), _fraction(total, red)]
        explanation, steps = "Probability equals favorable outcomes divided by total outcomes.", [f"Favorable outcomes: {red}.", f"Total outcomes: {total}.", f"The probability is { _fraction(red, total) }."]
    elif blueprint_id == "compound-events":
        first = 2 + (variant_index % 4)
        second = 3 + ((variant_index + 1) % 4)
        text, correct, distractors = f"A fair die is rolled twice. What is the probability that the first roll is at most {first} and the second roll is at most {second}?", _fraction(first * second, 36), [_fraction(first + second, 36), _fraction(first * second, 12), _fraction(first + second, 12)]
        explanation, steps = "Multiply the two independent probabilities.", [f"The first probability is {first}/6 and the second is {second}/6.", f"Multiply to get { _fraction(first * second, 36) }."]
    elif blueprint_id == "data-interpretation":
        monday = 40 + variant_index
        tuesday = monday + 5
        wednesday = tuesday + 7
        text, correct, distractors = "According to the table, which day had the greatest number of visitors?", "Wednesday", ["Monday", "Tuesday", str(wednesday)]
        explanation, steps = "Compare the values in the Visitors column.", [f"The largest value is {wednesday}.", "That value belongs to Wednesday."]
        table_ar = {"headers": ["Day", "Visitors"], "rows": [["Monday", str(monday)], ["Tuesday", str(tuesday)], ["Wednesday", str(wednesday)]]}
        table_caption = "Visitor totals across three days."
    elif blueprint_id == "tables-and-graphs":
        a, b, c = 12 + variant_index, 16 + variant_index, 19 + variant_index
        text, correct, distractors = f"A chart summary shows values of {a}, {b}, and {c}. What is the difference between the greatest and least values?", str(c - a), [str(c), str(a), str(c-a+3)]
        explanation, steps = "Subtract the least value from the greatest value.", [f"Greatest: {c}; least: {a}.", f"{c} - {a} = {c-a}."]
    elif blueprint_id == "sample-space":
        text, correct, distractors = "A code uses 1 letter chosen from 4 letters and 1 digit chosen from 3 digits. How many different codes are possible?", "12", ["7", "10", "24"]
        explanation, steps = "Multiply the number of choices for each part.", ["There are 4 letter choices and 3 digit choices.", "4 × 3 = 12."]
    elif blueprint_id == "weighted-average":
        a_count = 2 + (variant_index % 3)
        b_count = 3 + (variant_index % 4)
        a_value = 10 + variant_index
        b_value = 14 + variant_index
        total = a_count * a_value + b_count * b_value
        denom = a_count + b_count
        ans = total / denom
        text, correct, distractors = f"A class has {a_count} quizzes worth {a_value} points each and {b_count} quizzes worth {b_value} points each. What is the weighted average score per quiz?", f"{ans:.1f}", [f"{((a_value+b_value)/2):.1f}", f"{ans+1.5:.1f}", f"{denom:.1f}"]
        explanation, steps = "Multiply each value by its frequency, add, then divide by the total count.", [f"Weighted sum = {total}.", f"Divide by {denom} to get {ans:.1f}."]
    elif blueprint_id == "percent-of-data":
        total = 40 + variant_index * 2
        chosen = total // 4
        text, correct, distractors = f"In a survey of {total} students, {chosen} chose science club. What percent chose science club?", "25%", ["20%", "30%", f"{chosen}%"]
        explanation, steps = "Convert the fraction to a percent.", [f"The fraction is {chosen}/{total}.", "That fraction equals 25%."]
    elif blueprint_id == "boxplot-reading":
        q1 = 10 + variant_index
        q3 = q1 + 12
        text, correct, distractors = f"A data set has first quartile {q1} and third quartile {q3}. What is the interquartile range?", str(q3 - q1), [str(q3), str(q1), str(q3-q1+4)]
        explanation, steps = "The interquartile range is Q3 minus Q1.", [f"IQR = {q3} - {q1}.", f"So the IQR is {q3-q1}."]
    elif blueprint_id == "frequency-distribution":
        books = 4 + variant_index
        pens = 7 + variant_index
        folders = 3 + variant_index
        text, correct, distractors = "Which category has the highest frequency in the table?", "Pens", ["Books", "Folders", str(pens)]
        explanation, steps = "Choose the category with the greatest frequency.", [f"The largest frequency is {pens}.", "That value belongs to Pens."]
        table_ar = {"headers": ["Category", "Frequency"], "rows": [["Books", str(books)], ["Pens", str(pens)], ["Folders", str(folders)]]}
        table_caption = "Frequency table for three categories."
    else:
        prize = 8 + variant_index
        ans = prize / 4
        text, correct, distractors = f"A game gives a prize of {prize} points with probability { _fraction(1,4) } and 0 points otherwise. What is the expected value?", f"{ans:.1f}", [f"{prize:.1f}", f"{ans+1:.1f}", f"{ans-0.5:.1f}"]
        explanation, steps = "Expected value is each outcome multiplied by its probability.", [f"Multiply {prize} by { _fraction(1,4) }.", f"The expected value is {ans:.1f}."]
    return _question_payload(
        skill_id="quant_statistics",
        question_type="statistics",
        blueprint_id=blueprint_id,
        variant_index=variant_index,
        batch_id=batch_id,
        stage=stage,
        difficulty=difficulty,
        text_ar=text,
        correct_value=correct,
        distractors=distractors,
        explanation_ar=explanation,
        solution_steps_ar=steps,
        tags=["generated", "statistics", blueprint_id],
        table_ar=table_ar,
        table_caption=table_caption,
    )


VERBAL_TOPICS = [
    ("library", "opened one hour earlier on Saturdays", "students needed a quiet place to study", "attendance rose quickly", "the schedule continued through the summer"),
    ("farm", "installed soil sensors in the fields", "the owner wanted to reduce wasted water", "water use fell without lowering crop output", "more fields will get sensors next season"),
    ("art club", "posted short project videos", "new members felt uncertain about joining", "participation increased", "the club now records an introduction for each major activity"),
    ("grocery store", "added shelf cards explaining where produce came from", "customers often overlooked local items", "shoppers asked more questions and spent longer reading", "the manager wants to add more local-produce features"),
    ("science class", "replaced long weekly reviews with short daily check-ins", "students forgot what they needed to practice", "confidence improved before quizzes", "the teacher plans to keep the routine"),
    ("bus route", "added displays showing how many open seats were available", "crowding at one stop was severe", "commuters spread out more evenly", "planners want to test the display on more routes"),
    ("museum", "moved its family guide to a phone-based audio tour", "visitors wanted more flexible pacing", "children spent more time at the exhibits", "the museum will build similar tours for other galleries"),
    ("sports center", "created a quiet workout hour", "some members found the normal environment too intense", "attendance stayed steady", "the center added a second quiet session"),
    ("cafeteria", "tested smaller plates", "too much food was being wasted", "students still returned for seconds when needed", "the team concluded the smaller plates encouraged better portions"),
    ("language course", "began sending short reminder messages", "learners struggled to keep a steady routine", "completion rates improved", "the team plans to keep the reminders"),
]


def _verbal_item(blueprint_id: str, variant_index: int, stage: str, difficulty: float, batch_id: str) -> dict[str, Any]:
    subject, change, need, result, next_step = VERBAL_TOPICS[variant_index % len(VERBAL_TOPICS)]
    passage = f"The {subject} {change} because {need}. As a result, {result}. Because of that response, {next_step}."
    if blueprint_id == "main-idea":
        text, correct, distractors = "Which choice best states the main idea of the passage?", f"The {subject} made a change that worked well enough to continue.", [f"The {subject} changed direction only because of bad weather.", f"The {subject} found that the change created more problems than benefits.", f"The passage mainly explains how to copy the {subject}'s exact schedule."]
    elif blueprint_id == "supporting-detail":
        text, correct, distractors = "According to the passage, what happened after the change was introduced?", result[:1].upper() + result[1:] + ".", [need[:1].upper() + need[1:] + ".", change[:1].upper() + change[1:] + ".", next_step[:1].upper() + next_step[1:] + "."]
    elif blueprint_id == "inference":
        text, correct, distractors = "What can reasonably be inferred from the passage?", f"The change probably addressed a real need in the {subject}.", [f"The {subject} plans to undo the change immediately.", f"The people involved ignored the change most of the time.", "The result occurred for reasons unrelated to the change."]
    elif blueprint_id == "tone-and-attitude":
        text, correct, distractors = "Which phrase best describes the author's tone?", "Positive and approving", ["Bitter and sarcastic", "Indifferent and detached", "Confused and doubtful"]
    elif blueprint_id == "vocabulary-in-context":
        passage = f"The writer describes the response to the new plan as steady because {result}. In context, the word \"steady\" suggests that the progress was reliable rather than dramatic."
        text, correct, distractors = "In the passage, the word \"steady\" most nearly means:", "consistent", ["surprising", "temporary", "careless"]
    else:
        passage = f"First, the passage explains why the {subject} needed to change. Next, it describes the change itself. Finally, it reports that {result} and notes that {next_step}."
        text, correct, distractors = "Why does the passage mention the final result?", "To show the effect of the change before looking ahead", ["To replace the main topic with a different idea", "To argue that the change should be canceled", "To list details that are unrelated to the opening problem"]
    return _question_payload(
        skill_id="verbal_reading",
        question_type="reading",
        blueprint_id=blueprint_id,
        variant_index=variant_index,
        batch_id=batch_id,
        stage=stage,
        difficulty=difficulty,
        text_ar=text,
        passage_ar=passage,
        correct_value=correct,
        distractors=distractors,
        explanation_ar=f"The correct answer is the option most clearly supported by the passage: {correct}",
        solution_steps_ar=None,
        tags=["generated", "reading", blueprint_id],
        content_format="plain",
    )


def _generate_item(skill_id: str, blueprint_id: str, variant_index: int, stage: str, difficulty: float, batch_id: str) -> dict[str, Any]:
    if skill_id == "quant_arithmetic":
        return _arithmetic_item(blueprint_id, variant_index, stage, difficulty, batch_id)
    if skill_id == "quant_algebra":
        return _algebra_item(blueprint_id, variant_index, stage, difficulty, batch_id)
    if skill_id == "quant_statistics":
        return _statistics_item(blueprint_id, variant_index, stage, difficulty, batch_id)
    if skill_id == "verbal_reading":
        return _verbal_item(blueprint_id, variant_index, stage, difficulty, batch_id)
    raise ValueError(f"Unsupported skill for local generation: {skill_id}")


def generate_local_batch_manifest(*, skill_id: str, count: int, batch_id: str, prompt_version: str = PROMPT_VERSION_V1) -> dict[str, Any]:
    blueprints = SKILL_BLUEPRINTS[skill_id]
    stage_values = _stage_values(count, seed=f"{batch_id}:stage")
    difficulty_values = _difficulty_values(count, seed=f"{batch_id}:difficulty")
    base_count = count // len(blueprints)
    remainder = count % len(blueprints)
    blueprint_counts = {
        blueprint: base_count + (1 if index < remainder else 0)
        for index, blueprint in enumerate(blueprints)
    }

    items: list[dict[str, Any]] = []
    blueprint_counter: Counter[str] = Counter()
    overall_index = 0
    for blueprint in blueprints:
        for _ in range(blueprint_counts[blueprint]):
            items.append(
                _generate_item(
                    skill_id,
                    blueprint,
                    blueprint_counter[blueprint],
                    stage_values[overall_index],
                    difficulty_values[overall_index],
                    batch_id,
                )
            )
            blueprint_counter[blueprint] += 1
            overall_index += 1

    return build_manifest(
        batch_id=batch_id,
        items=items,
        generation_prompt_version=prompt_version,
        authoring_source=AUTHORING_SOURCE_AI,
        metadata={
            "provider": "local-blueprint",
            "skill_id": skill_id,
            "count": count,
            "blueprint_counts": dict(blueprint_counter),
        },
    )
