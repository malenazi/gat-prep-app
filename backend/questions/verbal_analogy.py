from models import Question


def get_questions():
    return [
        # ════════════════════════════════════════════════════════════════
        # 20 أسئلة موجودة (Existing Questions)
        # ════════════════════════════════════════════════════════════════

        # ── 1. أداة ← وظيفة (Tool → Function) ──

        # Q1 — قلم : كتابة (existing)
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.3,
            text_ar="قلم : كتابة",
            option_a="سيارة : طريق",
            option_b="شمس : حرارة",
            option_c="مجهر : تكبير",
            option_d="كتاب : مكتبة",
            correct_option="c",
            explanation_ar="نوع العلاقة: أداة ← وظيفتها\n• القلم أداة وظيفتها الكتابة → المجهر أداة وظيفتها التكبير ✓\nلماذا الخيارات الأخرى خطأ:\n(أ) سيارة : طريق ← علاقة وسيلة بمكان (لا أداة ووظيفة)\n(ب) شمس : حرارة ← علاقة مصدر بناتج طبيعي (لا أداة مصنوعة)\n(د) كتاب : مكتبة ← علاقة عنصر بمكان تخزينه",
            solution_steps_ar='["تحديد العلاقة: القلم أداة وظيفتها الكتابة","البحث عن نفس العلاقة: أداة ← وظيفة","المجهر أداة وظيفتها التكبير ✓"]',
        tags="tool-function", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q2 — مفتاح : قفل (existing)
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.4,
            text_ar="مفتاح : قفل",
            option_a="مشط : شعر",
            option_b="كتاب : رف",
            option_c="نافذة : جدار",
            option_d="سيارة : طريق",
            correct_option="a",
            explanation_ar="نوع العلاقة: أداة ← ما تعمل عليه\n• المفتاح أداة تعمل على القفل → المشط أداة تعمل على الشعر ✓\nلماذا الخيارات الأخرى خطأ:\n(ب) كتاب : رف ← علاقة عنصر بمكان وضعه (لا أداة وعمل)\n(ج) نافذة : جدار ← علاقة جزء بكلّ (لا أداة ووظيفة)\n(د) سيارة : طريق ← علاقة وسيلة بمكان الاستخدام",
            solution_steps_ar='["تحديد العلاقة: المفتاح أداة تعمل على القفل","البحث عن نفس العلاقة: أداة ← ما تعمل عليه","المشط أداة تعمل على الشعر ✓"]',
        tags="tool-function", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q3 — منشار : خشب (existing)
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.5,
            text_ar="منشار : خشب",
            option_a="مقص : قماش",
            option_b="طبيب : مريض",
            option_c="نهر : بحر",
            option_d="شجرة : ثمرة",
            correct_option="a",
            explanation_ar="نوع العلاقة: أداة قاطعة ← المادة التي تقطعها\n• المنشار يقطع الخشب → المقص يقطع القماش ✓\nلماذا الخيارات الأخرى خطأ:\n(ب) طبيب : مريض ← علاقة شخص بشخص (معالِج ومعالَج)\n(ج) نهر : بحر ← علاقة رافد بمصبّ (لا أداة ومادة)\n(د) شجرة : ثمرة ← علاقة مصدر بناتج",
            solution_steps_ar='["تحديد العلاقة: المنشار أداة تقطع الخشب","البحث عن نفس العلاقة: أداة ← المادة التي تعمل عليها","المقص أداة تقطع القماش ✓"]',
        tags="tool-function", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q4 — نحّات : إزميل (existing)
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.6,
            text_ar="نحّات : إزميل",
            option_a="رسّام : ريشة",
            option_b="شاعر : قصيدة",
            option_c="قمح : خبز",
            option_d="فرح : حزن",
            correct_option="a",
            explanation_ar="نوع العلاقة: حِرَفي ← أداته الخاصة\n• النحّات يستخدم الإزميل → الرسّام يستخدم الريشة ✓\nلماذا الخيارات الأخرى خطأ:\n(ب) شاعر : قصيدة ← علاقة مُنتِج بمُنتَج (لا شخص وأداة)\n(ج) قمح : خبز ← علاقة مادة خام بمنتج نهائي\n(د) فرح : حزن ← علاقة تضاد (لا علاقة بالأدوات)",
            solution_steps_ar='["تحديد العلاقة: النحّات يستخدم الإزميل كأداة","البحث عن نفس العلاقة: شخص ← أداته","الرسّام يستخدم الريشة كأداة ✓"]',
        tags="tool-function", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── 2. جزء ← كلّ (Part → Whole) ──

        # Q5 — عين : وجه (existing)
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.3,
            text_ar="عين : وجه",
            option_a="إصبع : يد",
            option_b="شمس : قمر",
            option_c="كتاب : قلم",
            option_d="ماء : نار",
            correct_option="a",
            explanation_ar="نوع العلاقة: جزء ← كلّ\n• العين جزء من الوجه → الإصبع جزء من اليد ✓\nلماذا الخيارات الأخرى خطأ:\n(ب) شمس : قمر ← علاقة تجاور/مقارنة لا جزء وكلّ\n(ج) كتاب : قلم ← علاقة أداة بأداة (لا احتواء)\n(د) ماء : نار ← علاقة تضاد لا جزئية",
            solution_steps_ar='["تحديد العلاقة: العين جزء من الوجه","البحث عن نفس العلاقة: جزء ← كلّ","الإصبع جزء من اليد ✓"]',
        tags="part-whole", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q6 — زجاجة : ماء (existing)
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.4,
            text_ar="زجاجة : ماء",
            option_a="صحن : طعام",
            option_b="شجرة : غابة",
            option_c="نهر : سمك",
            option_d="باب : مفتاح",
            correct_option="a",
            explanation_ar="نوع العلاقة: وعاء ← محتوى\n• الزجاجة وعاء للماء\n• الصحن وعاء للطعام ✓",
            solution_steps_ar='["تحديد العلاقة: الزجاجة تحتوي الماء","البحث عن نفس العلاقة: وعاء ← محتوى","الصحن يحتوي الطعام ✓"]',
        tags="tool-function", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ── 3. ترادف (Synonym) ──

        # ── 4. تضاد (Antonym) ──

        # Q7 — فرح : حزن (existing)
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.3,
            text_ar="فرح : حزن",
            option_a="غنى : فقر",
            option_b="طعام : شراب",
            option_c="صيف : حرّ",
            option_d="كتاب : قراءة",
            correct_option="a",
            explanation_ar="نوع العلاقة: تضاد (عكس)\n• فرح ↔ حزن → غنى ↔ فقر ✓\nلماذا الخيارات الأخرى خطأ:\n(ب) طعام : شراب ← علاقة تجانس/تلازم لا تضاد\n(ج) صيف : حرّ ← علاقة سبب ونتيجة/ارتباط لا تضاد\n(د) كتاب : قراءة ← علاقة أداة بوظيفة لا تضاد",
            solution_steps_ar='["تحديد العلاقة: فرح عكس حزن","البحث عن نفس العلاقة: تضاد","غنى عكس فقر ✓"]',
        tags="antonym", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q8 — تواضع : غرور (existing)
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.5,
            text_ar="تواضع : غرور",
            option_a="كرم : بخل",
            option_b="علم : كتاب",
            option_c="شمس : نور",
            option_d="قمح : طحين",
            correct_option="a",
            explanation_ar="نوع العلاقة: تضاد (عكس)\n• تواضع ↔ غرور\n• كرم ↔ بخل ✓",
            solution_steps_ar='["تحديد العلاقة: تواضع عكس غرور","البحث عن نفس العلاقة: تضاد","كرم عكس بخل ✓"]',
        tags="antonym", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q9 — تبخّر : تكاثف (existing)
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.6,
            text_ar="تبخّر : تكاثف",
            option_a="انصهار : تجمّد",
            option_b="ماء : بخار",
            option_c="حرارة : شمس",
            option_d="سحاب : مطر",
            correct_option="a",
            explanation_ar="نوع العلاقة: تضاد (عمليتان عكسيتان)\n• التبخّر عكس التكاثف\n• الانصهار عكس التجمّد ✓",
            solution_steps_ar='["تحديد العلاقة: التبخّر عملية عكس التكاثف","البحث عن نفس العلاقة: عمليتان عكسيتان","الانصهار عملية عكس التجمّد ✓"]',
        tags="antonym", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── 5. سبب ← نتيجة (Cause → Effect) ──

        # Q10 — حرارة : تبخّر (existing)
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.4,
            text_ar="حرارة : تبخّر",
            option_a="برودة : تجمّد",
            option_b="ماء : نهر",
            option_c="شمس : قمر",
            option_d="كتاب : قراءة",
            correct_option="a",
            explanation_ar="نوع العلاقة: سبب ← نتيجة\n• الحرارة تسبّب التبخّر\n• البرودة تسبّب التجمّد ✓",
            solution_steps_ar='["تحديد العلاقة: الحرارة سبب والتبخّر نتيجة","البحث عن نفس العلاقة: سبب ← نتيجة","البرودة سبب والتجمّد نتيجة ✓"]',
        tags="cause-effect", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q11 — اجتهاد : نجاح (existing)
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.4,
            text_ar="اجتهاد : نجاح",
            option_a="إهمال : فشل",
            option_b="كتاب : مكتبة",
            option_c="طبيب : مريض",
            option_d="ماء : عطش",
            correct_option="a",
            explanation_ar="نوع العلاقة: سبب ← نتيجة\n• الاجتهاد يؤدي إلى النجاح\n• الإهمال يؤدي إلى الفشل ✓",
            solution_steps_ar='["تحديد العلاقة: الاجتهاد سبب والنجاح نتيجة","البحث عن نفس العلاقة: سبب ← نتيجة","الإهمال سبب والفشل نتيجة ✓"]',
        tags="cause-effect", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q12 — شمس : نهار (existing)
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.2,
            text_ar="شمس : نهار",
            option_a="قمر : ليل",
            option_b="نجم : سماء",
            option_c="ورقة : شجرة",
            option_d="كتاب : قلم",
            correct_option="a",
            explanation_ar="نوع العلاقة: سبب ← نتيجة (ارتباط زمني)\n• الشمس مرتبطة بالنهار\n• القمر مرتبط بالليل ✓",
            solution_steps_ar='["تحديد العلاقة: الشمس ترتبط بالنهار","البحث عن نفس العلاقة: ارتباط سببي زمني","القمر يرتبط بالليل ✓"]',
        tags="cause-effect", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q13 — جوع : طعام (existing)
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.2,
            text_ar="جوع : طعام",
            option_a="نوم : سرير",
            option_b="عطش : ماء",
            option_c="كتاب : رفّ",
            option_d="برد : شتاء",
            correct_option="b",
            explanation_ar="نوع العلاقة: حاجة ← ما يسدّها\n• الجوع يُسدّ بالطعام\n• العطش يُسدّ بالماء ✓",
            solution_steps_ar='["تحديد العلاقة: الجوع حاجة والطعام يسدّها","البحث عن نفس العلاقة: حاجة ← ما يسدّها","العطش حاجة والماء يسدّها ✓"]',
        tags="tool-function", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── 6. شخص ← مكان (Agent → Place) ──

        # Q14 — طبيب : مستشفى (existing)
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.3,
            text_ar="طبيب : مستشفى",
            option_a="طالب : مدرسة",
            option_b="مريض : دواء",
            option_c="كتاب : علم",
            option_d="شجرة : غابة",
            correct_option="a",
            explanation_ar="نوع العلاقة: شخص ← مكان عمله\n• الطبيب يعمل في المستشفى\n• الطالب يدرس في المدرسة ✓",
            solution_steps_ar='["تحديد العلاقة: الطبيب يعمل في المستشفى","البحث عن نفس العلاقة: شخص ← مكان","الطالب يدرس في المدرسة ✓"]',
        tags="agent-place", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ── 7. مُنتِج ← مُنتَج (Agent → Product) ──

        # Q15 — شاعر : قصيدة (existing)
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.4,
            text_ar="شاعر : قصيدة",
            option_a="رسّام : لوحة",
            option_b="قلم : ورقة",
            option_c="طبيب : مستشفى",
            option_d="فرح : حزن",
            correct_option="a",
            explanation_ar="نوع العلاقة: مُنتِج ← مُنتَج\n• الشاعر يُنتج القصيدة\n• الرسّام يُنتج اللوحة ✓",
            solution_steps_ar='["تحديد العلاقة: الشاعر يُنتج القصيدة","البحث عن نفس العلاقة: مُنتِج ← مُنتَج","الرسّام يُنتج اللوحة ✓"]',
        tags="agent-product", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── 8. مادة خام ← منتج (Raw material → Product) ──

        # Q16 — قمح : خبز (existing)
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.4,
            text_ar="قمح : خبز",
            option_a="حليب : جبن",
            option_b="شجرة : غابة",
            option_c="طبيب : دواء",
            option_d="نهر : ماء",
            correct_option="a",
            explanation_ar="نوع العلاقة: مادة خام ← منتج\n• القمح مادة خام يُصنع منها الخبز\n• الحليب مادة خام يُصنع منه الجبن ✓",
            solution_steps_ar='["تحديد العلاقة: القمح يُصنع منه الخبز","البحث عن نفس العلاقة: مادة خام ← منتج","الحليب يُصنع منه الجبن ✓"]',
        tags="material-product", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── 9. تدرّج (Degree/Intensity) ──

        # Q17 — همس : صراخ (existing)
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.5,
            text_ar="همس : صراخ",
            option_a="مشي : ركض",
            option_b="كتاب : قلم",
            option_c="شمس : قمر",
            option_d="طبيب : مريض",
            correct_option="a",
            explanation_ar="نوع العلاقة: تدرّج في الشدّة\n• الهمس أقل شدّة من الصراخ (في الصوت)\n• المشي أقل شدّة من الركض (في الحركة) ✓",
            solution_steps_ar='["تحديد العلاقة: همس وصراخ تدرّج في شدّة الصوت","البحث عن نفس العلاقة: تدرّج في الشدّة","مشي وركض تدرّج في شدّة الحركة ✓"]',
        tags="degree", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q18 — بذرة : شجرة (existing)
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.2,
            text_ar="بذرة : شجرة",
            option_a="بيضة : دجاجة",
            option_b="ماء : نار",
            option_c="كتاب : مكتبة",
            option_d="قلم : حبر",
            correct_option="a",
            explanation_ar="نوع العلاقة: تدرّج (مرحلة نموّ)\n• البذرة تنمو لتصبح شجرة\n• البيضة تنمو لتصبح دجاجة ✓",
            solution_steps_ar='["تحديد العلاقة: البذرة مرحلة أولى والشجرة مرحلة نهائية","البحث عن نفس العلاقة: تدرّج في النموّ","البيضة مرحلة أولى والدجاجة مرحلة نهائية ✓"]',
        tags="degree", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── 10. رمز ← معنى (Symbol → Meaning) ──

        # Q19 — حمامة : سلام (existing)
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.5,
            text_ar="حمامة : سلام",
            option_a="أسد : شجاعة",
            option_b="شمس : حرارة",
            option_c="قلم : ورقة",
            option_d="نهر : بحر",
            correct_option="a",
            explanation_ar="نوع العلاقة: رمز ← معنى\n• الحمامة رمز للسلام\n• الأسد رمز للشجاعة ✓",
            solution_steps_ar='["تحديد العلاقة: الحمامة ترمز إلى السلام","البحث عن نفس العلاقة: رمز ← معنى","الأسد يرمز إلى الشجاعة ✓"]',
        tags="symbol-meaning", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ── سؤال متنوّع (existing) ──

        # Q20 — يرقة : فراشة (growth stage)
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.6,
            text_ar="يرقة : فراشة",
            option_a="طفل : رجل",
            option_b="كتاب : مكتبة",
            option_c="ماء : بحر",
            option_d="حجر : جبل",
            correct_option="a",
            explanation_ar="نوع العلاقة: تدرّج (مرحلة نموّ)\n• اليرقة تتطوّر إلى فراشة\n• الطفل يتطوّر إلى رجل ✓",
            solution_steps_ar='["تحديد العلاقة: اليرقة أصل والفراشة نتيجة النموّ","البحث عن نفس العلاقة: تدرّج في النموّ","الطفل أصل والرجل نتيجة النموّ ✓"]',
        tags="degree", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ════════════════════════════════════════════════════════════════
        # 91 سؤالاً جديداً (New Questions)
        # ════════════════════════════════════════════════════════════════

        # ══════════════════════════════════════
        # أداة ← وظيفة (Tool → Function) — 7 جديدة
        # ══════════════════════════════════════

        # Q21
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.2,
            text_ar="سماعة : استماع",
            option_a="نظّارة : رؤية",
            option_b="طبيب : مريض",
            option_c="شمس : ضوء",
            option_d="كتاب : مكتبة",
            correct_option="a",
            explanation_ar="نوع العلاقة: أداة ← وظيفتها\n• السماعة أداة للاستماع\n• النظّارة أداة للرؤية ✓",
            solution_steps_ar='["تحديد العلاقة: السماعة أداة وظيفتها الاستماع","البحث عن نفس العلاقة: أداة ← وظيفة","النظّارة أداة وظيفتها الرؤية ✓"]',
        tags="tool-function", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q22
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.3,
            text_ar="مكنسة : تنظيف",
            option_a="مبرد : تبريد",
            option_b="شجرة : ظلّ",
            option_c="نار : دخان",
            option_d="فرح : ابتسامة",
            correct_option="a",
            explanation_ar="نوع العلاقة: أداة ← وظيفتها\n• المكنسة أداة للتنظيف\n• المبرد أداة للتبريد ✓",
            solution_steps_ar='["تحديد العلاقة: المكنسة أداة وظيفتها التنظيف","البحث عن نفس العلاقة: أداة ← وظيفة","المبرد أداة وظيفتها التبريد ✓"]',
        tags="tool-function", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # Q23
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.4,
            text_ar="ميزان : وزن",
            option_a="مسطرة : قياس",
            option_b="قمر : ليل",
            option_c="طالب : واجب",
            option_d="بحر : سمك",
            correct_option="a",
            explanation_ar="نوع العلاقة: أداة ← وظيفتها\n• الميزان أداة لقياس الوزن\n• المسطرة أداة للقياس ✓",
            solution_steps_ar='["تحديد العلاقة: الميزان أداة وظيفتها الوزن","البحث عن نفس العلاقة: أداة ← وظيفة","المسطرة أداة وظيفتها القياس ✓"]',
        tags="tool-function", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # Q24
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.5,
            text_ar="مصباح : إنارة",
            option_a="مدفأة : تدفئة",
            option_b="حديقة : زهور",
            option_c="نجم : سماء",
            option_d="غيمة : سحاب",
            correct_option="a",
            explanation_ar="نوع العلاقة: أداة ← وظيفتها\n• المصباح أداة للإنارة\n• المدفأة أداة للتدفئة ✓",
            solution_steps_ar='["تحديد العلاقة: المصباح أداة وظيفتها الإنارة","البحث عن نفس العلاقة: أداة ← وظيفة","المدفأة أداة وظيفتها التدفئة ✓"]',
        tags="tool-function", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q25
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.6,
            text_ar="رافعة : رفع",
            option_a="حفّارة : حفر",
            option_b="أرض : زراعة",
            option_c="عامل : مصنع",
            option_d="حديد : صلابة",
            correct_option="a",
            explanation_ar="نوع العلاقة: أداة ← وظيفتها\n• الرافعة أداة للرفع\n• الحفّارة أداة للحفر ✓",
            solution_steps_ar='["تحديد العلاقة: الرافعة أداة وظيفتها الرفع","البحث عن نفس العلاقة: أداة ← وظيفة","الحفّارة أداة وظيفتها الحفر ✓"]',
        tags="tool-function", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q26
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.7,
            text_ar="بوصلة : اتجاه",
            option_a="ساعة : وقت",
            option_b="سفينة : بحر",
            option_c="خريطة : ورق",
            option_d="طائرة : سماء",
            correct_option="a",
            explanation_ar="نوع العلاقة: أداة ← وظيفتها\n• البوصلة أداة لتحديد الاتجاه\n• الساعة أداة لتحديد الوقت ✓",
            solution_steps_ar='["تحديد العلاقة: البوصلة أداة وظيفتها تحديد الاتجاه","البحث عن نفس العلاقة: أداة ← وظيفة","الساعة أداة وظيفتها تحديد الوقت ✓"]',
        tags="tool-function", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q27
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.8,
            text_ar="محراث : حراثة",
            option_a="منجل : حصاد",
            option_b="فلّاح : أرض",
            option_c="بذرة : ثمرة",
            option_d="تربة : خصوبة",
            correct_option="a",
            explanation_ar="نوع العلاقة: أداة ← وظيفتها\n• المحراث أداة للحراثة\n• المنجل أداة للحصاد ✓",
            solution_steps_ar='["تحديد العلاقة: المحراث أداة وظيفتها الحراثة","البحث عن نفس العلاقة: أداة ← وظيفة","المنجل أداة وظيفتها الحصاد ✓"]',
        tags="tool-function", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ══════════════════════════════════════
        # جزء ← كلّ (Part → Whole) — 9 جديدة
        # ══════════════════════════════════════

        # Q28
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.2,
            text_ar="ورقة : شجرة",
            option_a="ريشة : طائر",
            option_b="سماء : أرض",
            option_c="قلم : كتابة",
            option_d="نهر : ماء",
            correct_option="a",
            explanation_ar="نوع العلاقة: جزء ← كلّ\n• الورقة جزء من الشجرة\n• الريشة جزء من الطائر ✓",
            solution_steps_ar='["تحديد العلاقة: الورقة جزء من الشجرة","البحث عن نفس العلاقة: جزء ← كلّ","الريشة جزء من الطائر ✓"]',
        tags="part-whole", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # Q29
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.3,
            text_ar="صفحة : كتاب",
            option_a="طابق : مبنى",
            option_b="قلم : حبر",
            option_c="شمس : ضوء",
            option_d="حرارة : صيف",
            correct_option="a",
            explanation_ar="نوع العلاقة: جزء ← كلّ\n• الصفحة جزء من الكتاب\n• الطابق جزء من المبنى ✓",
            solution_steps_ar='["تحديد العلاقة: الصفحة جزء من الكتاب","البحث عن نفس العلاقة: جزء ← كلّ","الطابق جزء من المبنى ✓"]',
        tags="part-whole", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # Q30
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.4,
            text_ar="غرفة : منزل",
            option_a="فصل : مدرسة",
            option_b="طبيب : علاج",
            option_c="مطر : سحاب",
            option_d="فرح : سعادة",
            correct_option="a",
            explanation_ar="نوع العلاقة: جزء ← كلّ\n• الغرفة جزء من المنزل\n• الفصل جزء من المدرسة ✓",
            solution_steps_ar='["تحديد العلاقة: الغرفة جزء من المنزل","البحث عن نفس العلاقة: جزء ← كلّ","الفصل جزء من المدرسة ✓"]',
        tags="part-whole", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # Q31
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.4,
            text_ar="محرّك : سيارة",
            option_a="قلب : جسم",
            option_b="سرعة : طريق",
            option_c="بنزين : محطة",
            option_d="سائق : رخصة",
            correct_option="a",
            explanation_ar="نوع العلاقة: جزء ← كلّ\n• المحرّك جزء من السيارة\n• القلب جزء من الجسم ✓",
            solution_steps_ar='["تحديد العلاقة: المحرّك جزء أساسي من السيارة","البحث عن نفس العلاقة: جزء ← كلّ","القلب جزء أساسي من الجسم ✓"]',
        tags="part-whole", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q32
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.5,
            text_ar="فرع : جذع",
            option_a="إصبع : كفّ",
            option_b="ثمرة : بستان",
            option_c="نهر : بحر",
            option_d="سحاب : سماء",
            correct_option="a",
            explanation_ar="نوع العلاقة: جزء ← كلّ\n• الفرع جزء متّصل بالجذع\n• الإصبع جزء متّصل بالكفّ ✓",
            solution_steps_ar='["تحديد العلاقة: الفرع جزء يتّصل بالجذع","البحث عن نفس العلاقة: جزء ← كلّ","الإصبع جزء يتّصل بالكفّ ✓"]',
        tags="part-whole", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q33
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.6,
            text_ar="حرف : كلمة",
            option_a="كلمة : جملة",
            option_b="قلم : دفتر",
            option_c="صوت : أذن",
            option_d="لون : عين",
            correct_option="a",
            explanation_ar="نوع العلاقة: جزء ← كلّ\n• الحرف جزء من الكلمة\n• الكلمة جزء من الجملة ✓",
            solution_steps_ar='["تحديد العلاقة: الحرف وحدة أصغر تكوّن الكلمة","البحث عن نفس العلاقة: جزء ← كلّ","الكلمة وحدة أصغر تكوّن الجملة ✓"]',
        tags="part-whole", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q34
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.6,
            text_ar="جناح : طائرة",
            option_a="شراع : سفينة",
            option_b="ركّاب : مطار",
            option_c="سماء : فضاء",
            option_d="ريح : عاصفة",
            correct_option="a",
            explanation_ar="نوع العلاقة: جزء ← كلّ\n• الجناح جزء من الطائرة\n• الشراع جزء من السفينة ✓",
            solution_steps_ar='["تحديد العلاقة: الجناح جزء وظيفي من الطائرة","البحث عن نفس العلاقة: جزء ← كلّ","الشراع جزء وظيفي من السفينة ✓"]',
        tags="part-whole", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q35
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.7,
            text_ar="بتلة : زهرة",
            option_a="حبّة : سنبلة",
            option_b="لون : رسم",
            option_c="ريح : شتاء",
            option_d="نحلة : عسل",
            correct_option="a",
            explanation_ar="نوع العلاقة: جزء ← كلّ\n• البتلة جزء من الزهرة\n• الحبّة جزء من السنبلة ✓",
            solution_steps_ar='["تحديد العلاقة: البتلة جزء من الزهرة","البحث عن نفس العلاقة: جزء ← كلّ","الحبّة جزء من السنبلة ✓"]',
        tags="part-whole", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q36
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.8,
            text_ar="خليّة : نسيج",
            option_a="ذرّة : جُزيء",
            option_b="دم : وريد",
            option_c="مجهر : مختبر",
            option_d="عالِم : اكتشاف",
            correct_option="a",
            explanation_ar="نوع العلاقة: جزء ← كلّ\n• الخليّة وحدة تكوّن النسيج\n• الذرّة وحدة تكوّن الجُزيء ✓",
            solution_steps_ar='["تحديد العلاقة: الخليّة وحدة بنائية تكوّن النسيج","البحث عن نفس العلاقة: جزء ← كلّ","الذرّة وحدة بنائية تكوّن الجُزيء ✓"]',
        tags="part-whole", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ══════════════════════════════════════
        # ترادف (Synonym) — 11 جديدة
        # ══════════════════════════════════════

        # Q37
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.2,
            text_ar="سعادة : فرح",
            option_a="حزن : أسى",
            option_b="شمس : قمر",
            option_c="كتاب : قلم",
            option_d="ماء : نار",
            correct_option="a",
            explanation_ar="نوع العلاقة: ترادف\n• سعادة وفرح بمعنى واحد\n• حزن وأسى بمعنى واحد ✓",
            solution_steps_ar='["تحديد العلاقة: سعادة وفرح مترادفان","البحث عن نفس العلاقة: ترادف","حزن وأسى مترادفان ✓"]',
        tags="synonym", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # Q38
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.3,
            text_ar="شجاعة : بسالة",
            option_a="كرم : سخاء",
            option_b="ليل : نهار",
            option_c="قلم : كتاب",
            option_d="مدرسة : طالب",
            correct_option="a",
            explanation_ar="نوع العلاقة: ترادف\n• شجاعة وبسالة بمعنى واحد\n• كرم وسخاء بمعنى واحد ✓",
            solution_steps_ar='["تحديد العلاقة: شجاعة وبسالة مترادفان","البحث عن نفس العلاقة: ترادف","كرم وسخاء مترادفان ✓"]',
        tags="synonym", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # Q39
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.3,
            text_ar="غضب : سخط",
            option_a="خوف : رهبة",
            option_b="نار : ماء",
            option_c="طبيب : دواء",
            option_d="سيارة : طريق",
            correct_option="a",
            explanation_ar="نوع العلاقة: ترادف\n• غضب وسخط بمعنى واحد\n• خوف ورهبة بمعنى واحد ✓",
            solution_steps_ar='["تحديد العلاقة: غضب وسخط مترادفان","البحث عن نفس العلاقة: ترادف","خوف ورهبة مترادفان ✓"]',
        tags="synonym", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # Q40
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.4,
            text_ar="عِلم : معرفة",
            option_a="حيرة : ارتباك",
            option_b="كتاب : مكتبة",
            option_c="قمر : نجم",
            option_d="طعام : شراب",
            correct_option="a",
            explanation_ar="نوع العلاقة: ترادف\n• عِلم ومعرفة بمعنى متقارب\n• حيرة وارتباك بمعنى متقارب ✓",
            solution_steps_ar='["تحديد العلاقة: عِلم ومعرفة مترادفان","البحث عن نفس العلاقة: ترادف","حيرة وارتباك مترادفان ✓"]',
        tags="synonym", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q41
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.4,
            text_ar="وفاء : إخلاص",
            option_a="عجز : ضعف",
            option_b="كذب : حقيقة",
            option_c="نهر : جبل",
            option_d="شجرة : ثمرة",
            correct_option="a",
            explanation_ar="نوع العلاقة: ترادف\n• وفاء وإخلاص بمعنى واحد\n• عجز وضعف بمعنى متقارب ✓",
            solution_steps_ar='["تحديد العلاقة: وفاء وإخلاص مترادفان","البحث عن نفس العلاقة: ترادف","عجز وضعف مترادفان ✓"]',
        tags="synonym", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q42
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.5,
            text_ar="ظلام : دُجى",
            option_a="نور : ضياء",
            option_b="شمس : حرارة",
            option_c="ليل : نوم",
            option_d="قمر : سماء",
            correct_option="a",
            explanation_ar="نوع العلاقة: ترادف\n• ظلام ودُجى بمعنى واحد\n• نور وضياء بمعنى واحد ✓",
            solution_steps_ar='["تحديد العلاقة: ظلام ودُجى مترادفان","البحث عن نفس العلاقة: ترادف","نور وضياء مترادفان ✓"]',
        tags="synonym", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q43
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.5,
            text_ar="هدوء : سكينة",
            option_a="قلق : اضطراب",
            option_b="ماء : ثلج",
            option_c="حرب : سلاح",
            option_d="طائر : عشّ",
            correct_option="a",
            explanation_ar="نوع العلاقة: ترادف\n• هدوء وسكينة بمعنى واحد\n• قلق واضطراب بمعنى واحد ✓",
            solution_steps_ar='["تحديد العلاقة: هدوء وسكينة مترادفان","البحث عن نفس العلاقة: ترادف","قلق واضطراب مترادفان ✓"]',
        tags="synonym", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q44
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.6,
            text_ar="عطاء : بذل",
            option_a="منع : حرمان",
            option_b="قلم : ورقة",
            option_c="بحر : موج",
            option_d="جبل : صخر",
            correct_option="a",
            explanation_ar="نوع العلاقة: ترادف\n• عطاء وبذل بمعنى واحد\n• منع وحرمان بمعنى واحد ✓",
            solution_steps_ar='["تحديد العلاقة: عطاء وبذل مترادفان","البحث عن نفس العلاقة: ترادف","منع وحرمان مترادفان ✓"]',
        tags="synonym", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q45
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.6,
            text_ar="رحمة : شفقة",
            option_a="قسوة : غلظة",
            option_b="ماء : هواء",
            option_c="مدينة : قرية",
            option_d="صيف : شتاء",
            correct_option="a",
            explanation_ar="نوع العلاقة: ترادف\n• رحمة وشفقة بمعنى واحد\n• قسوة وغلظة بمعنى واحد ✓",
            solution_steps_ar='["تحديد العلاقة: رحمة وشفقة مترادفان","البحث عن نفس العلاقة: ترادف","قسوة وغلظة مترادفان ✓"]',
        tags="synonym", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q46
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.7,
            text_ar="تأمّل : تفكّر",
            option_a="تدبّر : تبصّر",
            option_b="سمع : كلام",
            option_c="جلوس : كرسي",
            option_d="طعام : جوع",
            correct_option="a",
            explanation_ar="نوع العلاقة: ترادف\n• تأمّل وتفكّر بمعنى واحد\n• تدبّر وتبصّر بمعنى واحد ✓",
            solution_steps_ar='["تحديد العلاقة: تأمّل وتفكّر مترادفان","البحث عن نفس العلاقة: ترادف","تدبّر وتبصّر مترادفان ✓"]',
        tags="synonym", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q47
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.8,
            text_ar="نُبوغ : عبقرية",
            option_a="فطنة : ذكاء",
            option_b="كسل : راحة",
            option_c="ورقة : شجرة",
            option_d="قمر : هلال",
            correct_option="a",
            explanation_ar="نوع العلاقة: ترادف\n• نُبوغ وعبقرية بمعنى واحد\n• فطنة وذكاء بمعنى واحد ✓",
            solution_steps_ar='["تحديد العلاقة: نُبوغ وعبقرية مترادفان","البحث عن نفس العلاقة: ترادف","فطنة وذكاء مترادفان ✓"]',
        tags="synonym", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ══════════════════════════════════════
        # تضاد (Antonym) — 8 جديدة
        # ══════════════════════════════════════

        # Q48
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.2,
            text_ar="حرّ : برد",
            option_a="نور : ظلام",
            option_b="شمس : صيف",
            option_c="كتاب : قراءة",
            option_d="ماء : عصير",
            correct_option="a",
            explanation_ar="نوع العلاقة: تضاد\n• حرّ عكس برد\n• نور عكس ظلام ✓",
            solution_steps_ar='["تحديد العلاقة: حرّ وبرد متضادان","البحث عن نفس العلاقة: تضاد","نور وظلام متضادان ✓"]',
        tags="antonym", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q49
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.3,
            text_ar="قوّة : ضعف",
            option_a="علم : جهل",
            option_b="كتاب : قلم",
            option_c="شمس : قمر",
            option_d="بحر : نهر",
            correct_option="a",
            explanation_ar="نوع العلاقة: تضاد\n• قوّة عكس ضعف\n• علم عكس جهل ✓",
            solution_steps_ar='["تحديد العلاقة: قوّة وضعف متضادان","البحث عن نفس العلاقة: تضاد","علم وجهل متضادان ✓"]',
        tags="antonym", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # Q50
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.4,
            text_ar="صعود : هبوط",
            option_a="تقدّم : تراجع",
            option_b="جبل : سهل",
            option_c="طائرة : مطار",
            option_d="سلّم : بناء",
            correct_option="a",
            explanation_ar="نوع العلاقة: تضاد\n• صعود عكس هبوط\n• تقدّم عكس تراجع ✓",
            solution_steps_ar='["تحديد العلاقة: صعود وهبوط متضادان","البحث عن نفس العلاقة: تضاد","تقدّم وتراجع متضادان ✓"]',
        tags="antonym", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # Q51
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.5,
            text_ar="شجاعة : جبن",
            option_a="صدق : كذب",
            option_b="سيف : حرب",
            option_c="أسد : غابة",
            option_d="جندي : معركة",
            correct_option="a",
            explanation_ar="نوع العلاقة: تضاد\n• شجاعة عكس جبن\n• صدق عكس كذب ✓",
            solution_steps_ar='["تحديد العلاقة: شجاعة وجبن متضادان","البحث عن نفس العلاقة: تضاد","صدق وكذب متضادان ✓"]',
        tags="antonym", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q52
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.5,
            text_ar="حرب : سلام",
            option_a="فوضى : نظام",
            option_b="جيش : جندي",
            option_c="سلاح : رصاصة",
            option_d="ميدان : معركة",
            correct_option="a",
            explanation_ar="نوع العلاقة: تضاد\n• حرب عكس سلام\n• فوضى عكس نظام ✓",
            solution_steps_ar='["تحديد العلاقة: حرب وسلام متضادان","البحث عن نفس العلاقة: تضاد","فوضى ونظام متضادان ✓"]',
        tags="antonym", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q53
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.6,
            text_ar="وفرة : شُحّ",
            option_a="رخاء : شدّة",
            option_b="ماء : صحراء",
            option_c="غنيّ : مال",
            option_d="سوق : بضاعة",
            correct_option="a",
            explanation_ar="نوع العلاقة: تضاد\n• وفرة عكس شُحّ\n• رخاء عكس شدّة ✓",
            solution_steps_ar='["تحديد العلاقة: وفرة وشُحّ متضادان","البحث عن نفس العلاقة: تضاد","رخاء وشدّة متضادان ✓"]',
        tags="antonym", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q54
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.7,
            text_ar="إسراف : اقتصاد",
            option_a="تبذير : ادّخار",
            option_b="مال : بنك",
            option_c="راتب : عمل",
            option_d="ثروة : استثمار",
            correct_option="a",
            explanation_ar="نوع العلاقة: تضاد\n• إسراف عكس اقتصاد (في المال)\n• تبذير عكس ادّخار ✓",
            solution_steps_ar='["تحديد العلاقة: إسراف واقتصاد متضادان","البحث عن نفس العلاقة: تضاد","تبذير وادّخار متضادان ✓"]',
        tags="antonym", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q55
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.6,
            text_ar="إيجاز : إطناب",
            option_a="اختصار : إسهاب",
            option_b="كلام : صمت",
            option_c="خطبة : مسجد",
            option_d="كاتب : مقال",
            correct_option="a",
            explanation_ar="نوع العلاقة: تضاد\n• إيجاز عكس إطناب (في الكلام)\n• اختصار عكس إسهاب ✓",
            solution_steps_ar='["تحديد العلاقة: إيجاز وإطناب متضادان","البحث عن نفس العلاقة: تضاد","اختصار وإسهاب متضادان ✓"]',
        tags="antonym", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ══════════════════════════════════════
        # سبب ← نتيجة (Cause → Effect) — 8 جديدة
        # ══════════════════════════════════════

        # Q56
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.2,
            text_ar="نار : دخان",
            option_a="مطر : فيضان",
            option_b="سماء : نجوم",
            option_c="بحر : سمك",
            option_d="جبل : صخر",
            correct_option="a",
            explanation_ar="نوع العلاقة: سبب ← نتيجة\n• النار تسبّب الدخان\n• المطر يسبّب الفيضان ✓",
            solution_steps_ar='["تحديد العلاقة: النار سبب والدخان نتيجة","البحث عن نفس العلاقة: سبب ← نتيجة","المطر سبب والفيضان نتيجة ✓"]',
        tags="cause-effect", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q57
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.3,
            text_ar="دراسة : تفوّق",
            option_a="تدريب : مهارة",
            option_b="كتاب : مكتبة",
            option_c="طالب : مدرسة",
            option_d="قلم : ورقة",
            correct_option="a",
            explanation_ar="نوع العلاقة: سبب ← نتيجة\n• الدراسة تؤدي إلى التفوّق\n• التدريب يؤدي إلى المهارة ✓",
            solution_steps_ar='["تحديد العلاقة: الدراسة سبب والتفوّق نتيجة","البحث عن نفس العلاقة: سبب ← نتيجة","التدريب سبب والمهارة نتيجة ✓"]',
        tags="cause-effect", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # Q58
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.4,
            text_ar="رياح : أمواج",
            option_a="زلزال : دمار",
            option_b="بحر : شاطئ",
            option_c="سفينة : بحّار",
            option_d="سحاب : سماء",
            correct_option="a",
            explanation_ar="نوع العلاقة: سبب ← نتيجة\n• الرياح تسبّب الأمواج\n• الزلزال يسبّب الدمار ✓",
            solution_steps_ar='["تحديد العلاقة: الرياح سبب والأمواج نتيجة","البحث عن نفس العلاقة: سبب ← نتيجة","الزلزال سبب والدمار نتيجة ✓"]',
        tags="cause-effect", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # Q59
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.5,
            text_ar="تلوّث : أمراض",
            option_a="جفاف : مجاعة",
            option_b="نهر : ماء",
            option_c="مصنع : عامل",
            option_d="هواء : أكسجين",
            correct_option="a",
            explanation_ar="نوع العلاقة: سبب ← نتيجة\n• التلوّث يسبّب الأمراض\n• الجفاف يسبّب المجاعة ✓",
            solution_steps_ar='["تحديد العلاقة: التلوّث سبب والأمراض نتيجة","البحث عن نفس العلاقة: سبب ← نتيجة","الجفاف سبب والمجاعة نتيجة ✓"]',
        tags="cause-effect", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q60
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.5,
            text_ar="ظلم : ثورة",
            option_a="فساد : انهيار",
            option_b="حاكم : شعب",
            option_c="سجن : قضبان",
            option_d="عدل : قاضٍ",
            correct_option="a",
            explanation_ar="نوع العلاقة: سبب ← نتيجة\n• الظلم يؤدي إلى الثورة\n• الفساد يؤدي إلى الانهيار ✓",
            solution_steps_ar='["تحديد العلاقة: الظلم سبب والثورة نتيجة","البحث عن نفس العلاقة: سبب ← نتيجة","الفساد سبب والانهيار نتيجة ✓"]',
        tags="cause-effect", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q61
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.6,
            text_ar="كسل : فشل",
            option_a="سهر : إرهاق",
            option_b="نوم : سرير",
            option_c="راحة : إجازة",
            option_d="عمل : مكتب",
            correct_option="a",
            explanation_ar="نوع العلاقة: سبب ← نتيجة\n• الكسل يؤدي إلى الفشل\n• السهر يؤدي إلى الإرهاق ✓",
            solution_steps_ar='["تحديد العلاقة: الكسل سبب والفشل نتيجة","البحث عن نفس العلاقة: سبب ← نتيجة","السهر سبب والإرهاق نتيجة ✓"]',
        tags="cause-effect", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q62
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.7,
            text_ar="ضغط : انفجار",
            option_a="احتكاك : حرارة",
            option_b="معدن : صلابة",
            option_c="ماء : سائل",
            option_d="حجر : جبل",
            correct_option="a",
            explanation_ar="نوع العلاقة: سبب ← نتيجة\n• الضغط يسبّب الانفجار\n• الاحتكاك يسبّب الحرارة ✓",
            solution_steps_ar='["تحديد العلاقة: الضغط سبب والانفجار نتيجة","البحث عن نفس العلاقة: سبب ← نتيجة","الاحتكاك سبب والحرارة نتيجة ✓"]',
        tags="cause-effect", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q63
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.8,
            text_ar="تصحّر : هجرة",
            option_a="حرب : نزوح",
            option_b="صحراء : رمل",
            option_c="مدينة : سكّان",
            option_d="أرض : زراعة",
            correct_option="a",
            explanation_ar="نوع العلاقة: سبب ← نتيجة\n• التصحّر يسبّب الهجرة\n• الحرب تسبّب النزوح ✓",
            solution_steps_ar='["تحديد العلاقة: التصحّر سبب والهجرة نتيجة","البحث عن نفس العلاقة: سبب ← نتيجة","الحرب سبب والنزوح نتيجة ✓"]',
        tags="cause-effect", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ══════════════════════════════════════
        # شخص ← مكان (Agent → Place) — 10 جديدة
        # ══════════════════════════════════════

        # Q64
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.2,
            text_ar="معلّم : مدرسة",
            option_a="إمام : مسجد",
            option_b="كتاب : رفّ",
            option_c="طعام : مطبخ",
            option_d="شجرة : حديقة",
            correct_option="a",
            explanation_ar="نوع العلاقة: شخص ← مكان عمله\n• المعلّم يعمل في المدرسة\n• الإمام يعمل في المسجد ✓",
            solution_steps_ar='["تحديد العلاقة: المعلّم يعمل في المدرسة","البحث عن نفس العلاقة: شخص ← مكان عمله","الإمام يعمل في المسجد ✓"]',
        tags="agent-place", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # Q65
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.3,
            text_ar="طيّار : طائرة",
            option_a="قبطان : سفينة",
            option_b="سماء : سحاب",
            option_c="مسافر : حقيبة",
            option_d="مطار : تذكرة",
            correct_option="a",
            explanation_ar="نوع العلاقة: شخص ← مكان عمله\n• الطيّار يعمل في الطائرة\n• القبطان يعمل في السفينة ✓",
            solution_steps_ar='["تحديد العلاقة: الطيّار يعمل في الطائرة","البحث عن نفس العلاقة: شخص ← مكان عمله","القبطان يعمل في السفينة ✓"]',
        tags="agent-place", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # Q66
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.4,
            text_ar="فلّاح : حقل",
            option_a="صيّاد : بحر",
            option_b="قمح : خبز",
            option_c="شمس : محصول",
            option_d="بذرة : تربة",
            correct_option="a",
            explanation_ar="نوع العلاقة: شخص ← مكان عمله\n• الفلّاح يعمل في الحقل\n• الصيّاد يعمل في البحر ✓",
            solution_steps_ar='["تحديد العلاقة: الفلّاح يعمل في الحقل","البحث عن نفس العلاقة: شخص ← مكان عمله","الصيّاد يعمل في البحر ✓"]',
        tags="agent-place", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # Q67
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.4,
            text_ar="عامل : مصنع",
            option_a="موظّف : مكتب",
            option_b="آلة : إنتاج",
            option_c="حديد : معدن",
            option_d="بضاعة : سوق",
            correct_option="a",
            explanation_ar="نوع العلاقة: شخص ← مكان عمله\n• العامل يعمل في المصنع\n• الموظّف يعمل في المكتب ✓",
            solution_steps_ar='["تحديد العلاقة: العامل يعمل في المصنع","البحث عن نفس العلاقة: شخص ← مكان عمله","الموظّف يعمل في المكتب ✓"]',
        tags="agent-place", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q68
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.5,
            text_ar="قاضٍ : محكمة",
            option_a="سفير : سفارة",
            option_b="قانون : عدالة",
            option_c="محامٍ : قضيّة",
            option_d="جريمة : عقوبة",
            correct_option="a",
            explanation_ar="نوع العلاقة: شخص ← مكان عمله\n• القاضي يعمل في المحكمة\n• السفير يعمل في السفارة ✓",
            solution_steps_ar='["تحديد العلاقة: القاضي يعمل في المحكمة","البحث عن نفس العلاقة: شخص ← مكان عمله","السفير يعمل في السفارة ✓"]',
        tags="agent-place", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q69
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.5,
            text_ar="طاهٍ : مطبخ",
            option_a="حارس : بوّابة",
            option_b="طعام : صحن",
            option_c="نار : موقد",
            option_d="ملح : توابل",
            correct_option="a",
            explanation_ar="نوع العلاقة: شخص ← مكان عمله\n• الطاهي يعمل في المطبخ\n• الحارس يعمل في البوّابة ✓",
            solution_steps_ar='["تحديد العلاقة: الطاهي يعمل في المطبخ","البحث عن نفس العلاقة: شخص ← مكان عمله","الحارس يعمل في البوّابة ✓"]',
        tags="agent-place", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q70
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.6,
            text_ar="صيدلي : صيدلية",
            option_a="مهندس : موقع",
            option_b="دواء : مرض",
            option_c="علاج : شفاء",
            option_d="وصفة : طبيب",
            correct_option="a",
            explanation_ar="نوع العلاقة: شخص ← مكان عمله\n• الصيدلي يعمل في الصيدلية\n• المهندس يعمل في الموقع ✓",
            solution_steps_ar='["تحديد العلاقة: الصيدلي يعمل في الصيدلية","البحث عن نفس العلاقة: شخص ← مكان عمله","المهندس يعمل في الموقع ✓"]',
        tags="agent-place", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q71
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.6,
            text_ar="لاعب : ملعب",
            option_a="ممثّل : مسرح",
            option_b="كرة : شبكة",
            option_c="فوز : هزيمة",
            option_d="تدريب : لياقة",
            correct_option="a",
            explanation_ar="نوع العلاقة: شخص ← مكان عمله\n• اللاعب يعمل في الملعب\n• الممثّل يعمل في المسرح ✓",
            solution_steps_ar='["تحديد العلاقة: اللاعب يعمل في الملعب","البحث عن نفس العلاقة: شخص ← مكان عمله","الممثّل يعمل في المسرح ✓"]',
        tags="agent-place", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q72
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.7,
            text_ar="راهب : دير",
            option_a="عالِم : مختبر",
            option_b="صلاة : عبادة",
            option_c="كنيسة : صليب",
            option_d="إيمان : دين",
            correct_option="a",
            explanation_ar="نوع العلاقة: شخص ← مكان عمله\n• الراهب يقيم في الدير\n• العالِم يعمل في المختبر ✓",
            solution_steps_ar='["تحديد العلاقة: الراهب يقيم في الدير","البحث عن نفس العلاقة: شخص ← مكان عمله","العالِم يعمل في المختبر ✓"]',
        tags="agent-place", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q73
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.8,
            text_ar="فلكي : مرصد",
            option_a="جيولوجي : منجم",
            option_b="نجم : كوكب",
            option_c="تلسكوب : عدسة",
            option_d="فضاء : مجرّة",
            correct_option="a",
            explanation_ar="نوع العلاقة: شخص ← مكان عمله\n• الفلكي يعمل في المرصد\n• الجيولوجي يعمل في المنجم ✓",
            solution_steps_ar='["تحديد العلاقة: الفلكي يعمل في المرصد","البحث عن نفس العلاقة: شخص ← مكان عمله","الجيولوجي يعمل في المنجم ✓"]',
        tags="agent-place", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ══════════════════════════════════════
        # مُنتِج ← مُنتَج (Agent → Product) — 10 جديدة
        # ══════════════════════════════════════

        # Q74
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.2,
            text_ar="خبّاز : خبز",
            option_a="حدّاد : سيف",
            option_b="فرن : حرارة",
            option_c="قمح : طحين",
            option_d="مطبخ : طعام",
            correct_option="a",
            explanation_ar="نوع العلاقة: مُنتِج ← مُنتَج\n• الخبّاز يُنتج الخبز\n• الحدّاد يُنتج السيف ✓",
            solution_steps_ar='["تحديد العلاقة: الخبّاز يُنتج الخبز","البحث عن نفس العلاقة: مُنتِج ← مُنتَج","الحدّاد يُنتج السيف ✓"]',
        tags="agent-product", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # Q75
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.3,
            text_ar="نجّار : أثاث",
            option_a="خيّاط : ثوب",
            option_b="خشب : شجرة",
            option_c="مطرقة : مسمار",
            option_d="منزل : باب",
            correct_option="a",
            explanation_ar="نوع العلاقة: مُنتِج ← مُنتَج\n• النجّار يُنتج الأثاث\n• الخيّاط يُنتج الثوب ✓",
            solution_steps_ar='["تحديد العلاقة: النجّار يُنتج الأثاث","البحث عن نفس العلاقة: مُنتِج ← مُنتَج","الخيّاط يُنتج الثوب ✓"]',
        tags="agent-product", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # Q76
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.4,
            text_ar="مؤلّف : كتاب",
            option_a="مخترع : اختراع",
            option_b="مكتبة : رفّ",
            option_c="قراءة : علم",
            option_d="ورقة : حبر",
            correct_option="a",
            explanation_ar="نوع العلاقة: مُنتِج ← مُنتَج\n• المؤلّف يُنتج الكتاب\n• المخترع يُنتج الاختراع ✓",
            solution_steps_ar='["تحديد العلاقة: المؤلّف يُنتج الكتاب","البحث عن نفس العلاقة: مُنتِج ← مُنتَج","المخترع يُنتج الاختراع ✓"]',
        tags="agent-product", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # Q77
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.5,
            text_ar="ملحّن : لحن",
            option_a="مصوّر : صورة",
            option_b="موسيقى : آلة",
            option_c="أغنية : مطرب",
            option_d="صوت : أذن",
            correct_option="a",
            explanation_ar="نوع العلاقة: مُنتِج ← مُنتَج\n• الملحّن يُنتج اللحن\n• المصوّر يُنتج الصورة ✓",
            solution_steps_ar='["تحديد العلاقة: الملحّن يُنتج اللحن","البحث عن نفس العلاقة: مُنتِج ← مُنتَج","المصوّر يُنتج الصورة ✓"]',
        tags="agent-product", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q78
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.5,
            text_ar="نحلة : عسل",
            option_a="بقرة : حليب",
            option_b="حقل : قمح",
            option_c="غابة : أشجار",
            option_d="حشرة : جناح",
            correct_option="a",
            explanation_ar="نوع العلاقة: مُنتِج ← مُنتَج\n• النحلة تُنتج العسل\n• البقرة تُنتج الحليب ✓",
            solution_steps_ar='["تحديد العلاقة: النحلة تُنتج العسل","البحث عن نفس العلاقة: مُنتِج ← مُنتَج","البقرة تُنتج الحليب ✓"]',
        tags="agent-product", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q79
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.6,
            text_ar="مهندس : تصميم",
            option_a="معماري : مخطّط",
            option_b="بناء : حجر",
            option_c="مبنى : طابق",
            option_d="حاسوب : برنامج",
            correct_option="a",
            explanation_ar="نوع العلاقة: مُنتِج ← مُنتَج\n• المهندس يُنتج التصميم\n• المعماري يُنتج المخطّط ✓",
            solution_steps_ar='["تحديد العلاقة: المهندس يُنتج التصميم","البحث عن نفس العلاقة: مُنتِج ← مُنتَج","المعماري يُنتج المخطّط ✓"]',
        tags="agent-product", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q80
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.6,
            text_ar="صحفي : مقال",
            option_a="مذيع : نشرة",
            option_b="جريدة : ورق",
            option_c="خبر : حدث",
            option_d="قارئ : كتاب",
            correct_option="a",
            explanation_ar="نوع العلاقة: مُنتِج ← مُنتَج\n• الصحفي يُنتج المقال\n• المذيع يُنتج النشرة ✓",
            solution_steps_ar='["تحديد العلاقة: الصحفي يُنتج المقال","البحث عن نفس العلاقة: مُنتِج ← مُنتَج","المذيع يُنتج النشرة ✓"]',
        tags="agent-product", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q81
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.7,
            text_ar="خطّاط : لوحة خطّ",
            option_a="نقّاش : زخرفة",
            option_b="حبر : ورق",
            option_c="فنّ : جمال",
            option_d="معرض : زائر",
            correct_option="a",
            explanation_ar="نوع العلاقة: مُنتِج ← مُنتَج\n• الخطّاط يُنتج لوحة الخطّ\n• النقّاش يُنتج الزخرفة ✓",
            solution_steps_ar='["تحديد العلاقة: الخطّاط يُنتج لوحة الخطّ","البحث عن نفس العلاقة: مُنتِج ← مُنتَج","النقّاش يُنتج الزخرفة ✓"]',
        tags="agent-product", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q82
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.7,
            text_ar="مبرمج : برنامج",
            option_a="مصمّم : واجهة",
            option_b="حاسوب : شاشة",
            option_c="كهرباء : طاقة",
            option_d="إنترنت : شبكة",
            correct_option="a",
            explanation_ar="نوع العلاقة: مُنتِج ← مُنتَج\n• المبرمج يُنتج البرنامج\n• المصمّم يُنتج الواجهة ✓",
            solution_steps_ar='["تحديد العلاقة: المبرمج يُنتج البرنامج","البحث عن نفس العلاقة: مُنتِج ← مُنتَج","المصمّم يُنتج الواجهة ✓"]',
        tags="agent-product", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q83
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.6,
            text_ar="حائك : سجّادة",
            option_a="فخّاري : إناء",
            option_b="خيط : نسيج",
            option_c="صوف : غنم",
            option_d="سوق : بيع",
            correct_option="a",
            explanation_ar="نوع العلاقة: مُنتِج ← مُنتَج\n• الحائك يُنتج السجّادة\n• الفخّاري يُنتج الإناء ✓",
            solution_steps_ar='["تحديد العلاقة: الحائك يُنتج السجّادة","البحث عن نفس العلاقة: مُنتِج ← مُنتَج","الفخّاري يُنتج الإناء ✓"]',
        tags="agent-product", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ══════════════════════════════════════
        # مادة خام ← منتج (Raw material → Product) — 10 جديدة
        # ══════════════════════════════════════

        # Q84
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.2,
            text_ar="حديد : سيف",
            option_a="طين : فخّار",
            option_b="حدّاد : نار",
            option_c="معدن : منجم",
            option_d="قوّة : صلابة",
            correct_option="a",
            explanation_ar="نوع العلاقة: مادة خام ← منتج\n• الحديد يُصنع منه السيف\n• الطين يُصنع منه الفخّار ✓",
            solution_steps_ar='["تحديد العلاقة: الحديد مادة خام يُصنع منها السيف","البحث عن نفس العلاقة: مادة خام ← منتج","الطين مادة خام يُصنع منها الفخّار ✓"]',
        tags="material-product", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q85
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.3,
            text_ar="خشب : طاولة",
            option_a="قطن : قماش",
            option_b="نجّار : مطرقة",
            option_c="غابة : شجرة",
            option_d="أثاث : منزل",
            correct_option="a",
            explanation_ar="نوع العلاقة: مادة خام ← منتج\n• الخشب يُصنع منه الطاولة\n• القطن يُصنع منه القماش ✓",
            solution_steps_ar='["تحديد العلاقة: الخشب مادة خام تُصنع منها الطاولة","البحث عن نفس العلاقة: مادة خام ← منتج","القطن مادة خام يُصنع منها القماش ✓"]',
        tags="material-product", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # Q86
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.4,
            text_ar="صوف : بِساط",
            option_a="جلد : حذاء",
            option_b="خروف : مزرعة",
            option_c="شتاء : برد",
            option_d="لون : صبغة",
            correct_option="a",
            explanation_ar="نوع العلاقة: مادة خام ← منتج\n• الصوف يُصنع منه البِساط\n• الجلد يُصنع منه الحذاء ✓",
            solution_steps_ar='["تحديد العلاقة: الصوف مادة خام يُصنع منها البِساط","البحث عن نفس العلاقة: مادة خام ← منتج","الجلد مادة خام يُصنع منها الحذاء ✓"]',
        tags="material-product", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q87
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.4,
            text_ar="رمل : زجاج",
            option_a="نفط : بلاستيك",
            option_b="صحراء : حرارة",
            option_c="مصنع : عامل",
            option_d="شفافية : نقاء",
            correct_option="a",
            explanation_ar="نوع العلاقة: مادة خام ← منتج\n• الرمل يُصنع منه الزجاج\n• النفط يُصنع منه البلاستيك ✓",
            solution_steps_ar='["تحديد العلاقة: الرمل مادة خام يُصنع منها الزجاج","البحث عن نفس العلاقة: مادة خام ← منتج","النفط مادة خام يُصنع منها البلاستيك ✓"]',
        tags="material-product", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q88
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.5,
            text_ar="عنب : زبيب",
            option_a="مشمش : قمر الدين",
            option_b="فاكهة : شجرة",
            option_c="كأس : مائدة",
            option_d="حلو : مرّ",
            correct_option="a",
            explanation_ar="نوع العلاقة: مادة خام ← منتج\n• العنب يُصنع منه الزبيب\n• المشمش يُصنع منه قمر الدين ✓",
            solution_steps_ar='["تحديد العلاقة: العنب مادة خام يُصنع منها الزبيب","البحث عن نفس العلاقة: مادة خام ← منتج","المشمش مادة خام يُصنع منها قمر الدين ✓"]',
        tags="material-product", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q89
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.5,
            text_ar="زيتون : زيت",
            option_a="سمسم : طحينة",
            option_b="شجرة : ثمرة",
            option_c="مزرعة : فلّاح",
            option_d="أخضر : أسود",
            correct_option="a",
            explanation_ar="نوع العلاقة: مادة خام ← منتج\n• الزيتون يُصنع منه الزيت\n• السمسم يُصنع منه الطحينة ✓",
            solution_steps_ar='["تحديد العلاقة: الزيتون مادة خام يُصنع منها الزيت","البحث عن نفس العلاقة: مادة خام ← منتج","السمسم مادة خام يُصنع منها الطحينة ✓"]',
        tags="material-product", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q90
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.6,
            text_ar="كاكاو : شوكولاتة",
            option_a="قصب : سكّر",
            option_b="مصنع : إنتاج",
            option_c="حلوى : طفل",
            option_d="بنّي : لون",
            correct_option="a",
            explanation_ar="نوع العلاقة: مادة خام ← منتج\n• الكاكاو يُصنع منه الشوكولاتة\n• القصب يُصنع منه السكّر ✓",
            solution_steps_ar='["تحديد العلاقة: الكاكاو مادة خام تُصنع منها الشوكولاتة","البحث عن نفس العلاقة: مادة خام ← منتج","القصب مادة خام يُصنع منها السكّر ✓"]',
        tags="material-product", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q91
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.6,
            text_ar="حرير : فستان",
            option_a="كتّان : عباءة",
            option_b="دودة : فراشة",
            option_c="جمال : أناقة",
            option_d="خياطة : إبرة",
            correct_option="a",
            explanation_ar="نوع العلاقة: مادة خام ← منتج\n• الحرير يُصنع منه الفستان\n• الكتّان يُصنع منه العباءة ✓",
            solution_steps_ar='["تحديد العلاقة: الحرير مادة خام يُصنع منها الفستان","البحث عن نفس العلاقة: مادة خام ← منتج","الكتّان مادة خام يُصنع منها العباءة ✓"]',
        tags="material-product", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q92
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.7,
            text_ar="بترول : بنزين",
            option_a="قمح : دقيق",
            option_b="محطة : سيارة",
            option_c="أنبوب : ماء",
            option_d="طاقة : حركة",
            correct_option="a",
            explanation_ar="نوع العلاقة: مادة خام ← منتج\n• البترول يُكرّر ليصبح بنزين\n• القمح يُطحن ليصبح دقيق ✓",
            solution_steps_ar='["تحديد العلاقة: البترول مادة خام تُنتج البنزين","البحث عن نفس العلاقة: مادة خام ← منتج","القمح مادة خام يُنتج منها الدقيق ✓"]',
        tags="material-product", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q93
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.8,
            text_ar="بوكسيت : ألمنيوم",
            option_a="لاتكس : مطّاط",
            option_b="منجم : عامل",
            option_c="معدن : لمعان",
            option_d="صناعة : تقنية",
            correct_option="a",
            explanation_ar="نوع العلاقة: مادة خام ← منتج\n• البوكسيت خام يُستخرج منه الألمنيوم\n• اللاتكس مادة خام يُصنع منها المطّاط ✓",
            solution_steps_ar='["تحديد العلاقة: البوكسيت مادة خام يُستخرج منها الألمنيوم","البحث عن نفس العلاقة: مادة خام ← منتج","اللاتكس مادة خام يُصنع منها المطّاط ✓"]',
        tags="material-product", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ══════════════════════════════════════
        # تدرّج (Degree/Intensity) — 9 جديدة
        # ══════════════════════════════════════

        # Q94
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.3,
            text_ar="دافئ : حارّ",
            option_a="بارد : مُتجمّد",
            option_b="ماء : ثلج",
            option_c="شمس : صيف",
            option_d="نار : رماد",
            correct_option="a",
            explanation_ar="نوع العلاقة: تدرّج في الشدّة\n• دافئ أقل شدّة من حارّ (في الحرارة)\n• بارد أقل شدّة من مُتجمّد (في البرودة) ✓",
            solution_steps_ar='["تحديد العلاقة: دافئ وحارّ تدرّج في الحرارة","البحث عن نفس العلاقة: تدرّج في الشدّة","بارد ومُتجمّد تدرّج في البرودة ✓"]',
        tags="degree", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # Q95
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.4,
            text_ar="ابتسامة : ضحك",
            option_a="دمعة : بكاء",
            option_b="فرح : عيد",
            option_c="وجه : عين",
            option_d="فم : أسنان",
            correct_option="a",
            explanation_ar="نوع العلاقة: تدرّج في الشدّة\n• الابتسامة أقل شدّة من الضحك\n• الدمعة أقل شدّة من البكاء ✓",
            solution_steps_ar='["تحديد العلاقة: ابتسامة وضحك تدرّج في التعبير","البحث عن نفس العلاقة: تدرّج في الشدّة","دمعة وبكاء تدرّج في الحزن ✓"]',
        tags="degree", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q96
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.4,
            text_ar="غضب : هياج",
            option_a="خوف : ذعر",
            option_b="شجاعة : جبن",
            option_c="حرب : سلام",
            option_d="جيش : جندي",
            correct_option="a",
            explanation_ar="نوع العلاقة: تدرّج في الشدّة\n• الغضب أقل شدّة من الهياج\n• الخوف أقل شدّة من الذعر ✓",
            solution_steps_ar='["تحديد العلاقة: غضب وهياج تدرّج في الانفعال","البحث عن نفس العلاقة: تدرّج في الشدّة","خوف وذعر تدرّج في الشعور ✓"]',
        tags="degree", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q97
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.5,
            text_ar="نسيم : عاصفة",
            option_a="قطرة : سيل",
            option_b="سماء : أرض",
            option_c="هواء : ماء",
            option_d="شجرة : غابة",
            correct_option="a",
            explanation_ar="نوع العلاقة: تدرّج في الشدّة\n• النسيم أقل شدّة من العاصفة (في الرياح)\n• القطرة أقل شدّة من السيل (في الماء) ✓",
            solution_steps_ar='["تحديد العلاقة: نسيم وعاصفة تدرّج في شدّة الرياح","البحث عن نفس العلاقة: تدرّج في الشدّة","قطرة وسيل تدرّج في كمّية الماء ✓"]',
        tags="degree", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q98
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.5,
            text_ar="انزعاج : غضب",
            option_a="قلق : فزع",
            option_b="حبّ : كره",
            option_c="صوت : أذن",
            option_d="مرض : دواء",
            correct_option="a",
            explanation_ar="نوع العلاقة: تدرّج في الشدّة\n• الانزعاج أقل شدّة من الغضب\n• القلق أقل شدّة من الفزع ✓",
            solution_steps_ar='["تحديد العلاقة: انزعاج وغضب تدرّج في الانفعال","البحث عن نفس العلاقة: تدرّج في الشدّة","قلق وفزع تدرّج في الشعور ✓"]',
        tags="degree", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q99
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.6,
            text_ar="إعجاب : عشق",
            option_a="استحسان : افتتان",
            option_b="حبّ : زواج",
            option_c="قلب : عقل",
            option_d="شعر : نثر",
            correct_option="a",
            explanation_ar="نوع العلاقة: تدرّج في الشدّة\n• الإعجاب أقل شدّة من العشق\n• الاستحسان أقل شدّة من الافتتان ✓",
            solution_steps_ar='["تحديد العلاقة: إعجاب وعشق تدرّج في الشعور","البحث عن نفس العلاقة: تدرّج في الشدّة","استحسان وافتتان تدرّج في الإعجاب ✓"]',
        tags="degree", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q100
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.6,
            text_ar="تعب : إنهاك",
            option_a="ألم : عذاب",
            option_b="نوم : راحة",
            option_c="عمل : مكتب",
            option_d="جسم : عضلة",
            correct_option="a",
            explanation_ar="نوع العلاقة: تدرّج في الشدّة\n• التعب أقل شدّة من الإنهاك\n• الألم أقل شدّة من العذاب ✓",
            solution_steps_ar='["تحديد العلاقة: تعب وإنهاك تدرّج في الإرهاق","البحث عن نفس العلاقة: تدرّج في الشدّة","ألم وعذاب تدرّج في المعاناة ✓"]',
        tags="degree", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q101
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.3,
            text_ar="حُزن : كآبة",
            option_a="فرح : نشوة",
            option_b="بكاء : عين",
            option_c="ليل : وحدة",
            option_d="شتاء : برد",
            correct_option="a",
            explanation_ar="نوع العلاقة: تدرّج في الشدّة\n• الحُزن أقل شدّة من الكآبة\n• الفرح أقل شدّة من النشوة ✓",
            solution_steps_ar='["تحديد العلاقة: حُزن وكآبة تدرّج في الشعور السلبي","البحث عن نفس العلاقة: تدرّج في الشدّة","فرح ونشوة تدرّج في الشعور الإيجابي ✓"]',
        tags="degree", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q102
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.3,
            text_ar="ضيق : اختناق",
            option_a="ألم : وجع شديد",
            option_b="عقل : قلب",
            option_c="سؤال : جواب",
            option_d="صحّة : مرض",
            correct_option="a",
            explanation_ar="نوع العلاقة: تدرّج في الشدّة\n• الضيق أقل شدّة من الاختناق\n• الألم أقل شدّة من الوجع الشديد ✓",
            solution_steps_ar='["تحديد العلاقة: ضيق واختناق تدرّج في شدّة الشعور","البحث عن نفس العلاقة: تدرّج في الشدّة","ألم ووجع شديد تدرّج في شدّة المعاناة ✓"]',
        tags="degree", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ══════════════════════════════════════
        # رمز ← معنى (Symbol → Meaning) — 10 جديدة
        # ══════════════════════════════════════

        # Q103
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.3,
            text_ar="ميزان : عدل",
            option_a="تاج : سلطة",
            option_b="قاضٍ : محكمة",
            option_c="قانون : عقوبة",
            option_d="حقّ : واجب",
            correct_option="a",
            explanation_ar="نوع العلاقة: رمز ← معنى\n• الميزان رمز للعدل\n• التاج رمز للسلطة ✓",
            solution_steps_ar='["تحديد العلاقة: الميزان يرمز إلى العدل","البحث عن نفس العلاقة: رمز ← معنى","التاج يرمز إلى السلطة ✓"]',
        tags="symbol-meaning", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q104
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.4,
            text_ar="غصن زيتون : سلام",
            option_a="علم : وطن",
            option_b="شجرة : ظلّ",
            option_c="أخضر : طبيعة",
            option_d="حرب : دمار",
            correct_option="a",
            explanation_ar="نوع العلاقة: رمز ← معنى\n• غصن الزيتون رمز للسلام\n• العلم رمز للوطن ✓",
            solution_steps_ar='["تحديد العلاقة: غصن الزيتون يرمز إلى السلام","البحث عن نفس العلاقة: رمز ← معنى","العلم يرمز إلى الوطن ✓"]',
        tags="symbol-meaning", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q105
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.4,
            text_ar="وردة : حبّ",
            option_a="خاتم : زواج",
            option_b="حديقة : زهور",
            option_c="عطر : رائحة",
            option_d="أحمر : لون",
            correct_option="a",
            explanation_ar="نوع العلاقة: رمز ← معنى\n• الوردة رمز للحبّ\n• الخاتم رمز للزواج ✓",
            solution_steps_ar='["تحديد العلاقة: الوردة ترمز إلى الحبّ","البحث عن نفس العلاقة: رمز ← معنى","الخاتم يرمز إلى الزواج ✓"]',
        tags="symbol-meaning", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q106
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.5,
            text_ar="جمجمة : موت",
            option_a="قلب : حبّ",
            option_b="عظم : جسم",
            option_c="مقبرة : حزن",
            option_d="أسود : ليل",
            correct_option="a",
            explanation_ar="نوع العلاقة: رمز ← معنى\n• الجمجمة رمز للموت\n• القلب رمز للحبّ ✓",
            solution_steps_ar='["تحديد العلاقة: الجمجمة ترمز إلى الموت","البحث عن نفس العلاقة: رمز ← معنى","القلب يرمز إلى الحبّ ✓"]',
        tags="symbol-meaning", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q107
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.5,
            text_ar="نسر : قوّة",
            option_a="بومة : حكمة",
            option_b="طائر : جناح",
            option_c="سماء : طيران",
            option_d="جبل : ارتفاع",
            correct_option="a",
            explanation_ar="نوع العلاقة: رمز ← معنى\n• النسر رمز للقوّة\n• البومة رمز للحكمة ✓",
            solution_steps_ar='["تحديد العلاقة: النسر يرمز إلى القوّة","البحث عن نفس العلاقة: رمز ← معنى","البومة ترمز إلى الحكمة ✓"]',
        tags="symbol-meaning", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q108
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.6,
            text_ar="سلسلة : عبودية",
            option_a="مفتاح : حرّية",
            option_b="حديد : قوّة",
            option_c="سجن : عقوبة",
            option_d="قيد : يد",
            correct_option="a",
            explanation_ar="نوع العلاقة: رمز ← معنى\n• السلسلة رمز للعبودية\n• المفتاح رمز للحرّية ✓",
            solution_steps_ar='["تحديد العلاقة: السلسلة ترمز إلى العبودية","البحث عن نفس العلاقة: رمز ← معنى","المفتاح يرمز إلى الحرّية ✓"]',
        tags="symbol-meaning", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q109
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.6,
            text_ar="شمعة : أمل",
            option_a="فجر : بداية",
            option_b="نور : كهرباء",
            option_c="ليل : نوم",
            option_d="نار : حطب",
            correct_option="a",
            explanation_ar="نوع العلاقة: رمز ← معنى\n• الشمعة رمز للأمل\n• الفجر رمز للبداية ✓",
            solution_steps_ar='["تحديد العلاقة: الشمعة ترمز إلى الأمل","البحث عن نفس العلاقة: رمز ← معنى","الفجر يرمز إلى البداية ✓"]',
        tags="symbol-meaning", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # Q110
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.7,
            text_ar="ثعلب : مكر",
            option_a="حمل : وداعة",
            option_b="حيوان : غابة",
            option_c="صياد : فريسة",
            option_d="ذكاء : عقل",
            correct_option="a",
            explanation_ar="نوع العلاقة: رمز ← معنى\n• الثعلب رمز للمكر\n• الحمل رمز للوداعة ✓",
            solution_steps_ar='["تحديد العلاقة: الثعلب يرمز إلى المكر","البحث عن نفس العلاقة: رمز ← معنى","الحمل يرمز إلى الوداعة ✓"]',
        tags="symbol-meaning", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # Q111
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.7,
            text_ar="طاووس : تباهٍ",
            option_a="غراب : تشاؤم",
            option_b="طائر : ريش",
            option_c="جمال : ألوان",
            option_d="حديقة : حيوان",
            correct_option="a",
            explanation_ar="نوع العلاقة: رمز ← معنى\n• الطاووس رمز للتباهي\n• الغراب رمز للتشاؤم ✓",
            solution_steps_ar='["تحديد العلاقة: الطاووس يرمز إلى التباهي","البحث عن نفس العلاقة: رمز ← معنى","الغراب يرمز إلى التشاؤم ✓"]',
        tags="symbol-meaning", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ════════════════════════════════════════════════════════════════
        # 56 سؤالاً إضافياً (Questions 112–167)
        # ════════════════════════════════════════════════════════════════

        # ── Q112 — أداة ← وظيفة | diagnostic | 0.2 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.2,
            text_ar="مطرقة : طرق",
            option_a="مفكّ : لفّ",
            option_b="حديد : صلابة",
            option_c="بنّاء : جدار",
            option_d="خشب : باب",
            correct_option="a",
            explanation_ar="نوع العلاقة: أداة ← وظيفتها\n• المطرقة أداة للطرق\n• المفكّ أداة للفّ ✓",
            solution_steps_ar='["تحديد العلاقة: المطرقة أداة وظيفتها الطرق","البحث عن نفس العلاقة: أداة ← وظيفة","المفكّ أداة وظيفتها اللفّ ✓"]',
        tags="tool-function", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ── Q113 — جزء ← كلّ | diagnostic | 0.2 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.2,
            text_ar="نافذة : غرفة",
            option_a="عجلة : دراجة",
            option_b="شمس : ضوء",
            option_c="كتاب : قراءة",
            option_d="ماء : عطش",
            correct_option="a",
            explanation_ar="نوع العلاقة: جزء ← كلّ\n• النافذة جزء من الغرفة\n• العجلة جزء من الدراجة ✓",
            solution_steps_ar='["تحديد العلاقة: النافذة جزء من الغرفة","البحث عن نفس العلاقة: جزء ← كلّ","العجلة جزء من الدراجة ✓"]',
        tags="part-whole", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ── Q114 — سبب ← نتيجة | diagnostic | 0.3 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.3,
            text_ar="مطر : فيضان",
            option_a="جفاف : قحط",
            option_b="نهر : سمك",
            option_c="سحاب : سماء",
            option_d="مزرعة : فلّاح",
            correct_option="a",
            explanation_ar="نوع العلاقة: سبب ← نتيجة\n• المطر الغزير يسبّب الفيضان\n• الجفاف يسبّب القحط ✓",
            solution_steps_ar='["تحديد العلاقة: المطر سبب والفيضان نتيجة","البحث عن نفس العلاقة: سبب ← نتيجة","الجفاف سبب والقحط نتيجة ✓"]',
        tags="cause-effect", stage="diagnostic",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ── Q115 — ترادف | foundation | 0.3 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.3,
            text_ar="جُود : سخاء",
            option_a="حِلم : صبر",
            option_b="نار : ماء",
            option_c="كتاب : مكتبة",
            option_d="سيارة : طريق",
            correct_option="a",
            explanation_ar="نوع العلاقة: ترادف\n• الجُود والسخاء بمعنى واحد\n• الحِلم والصبر بمعنى واحد ✓",
            solution_steps_ar='["تحديد العلاقة: الجُود يرادف السخاء","البحث عن نفس العلاقة: ترادف","الحِلم يرادف الصبر ✓"]',
        tags="synonym", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ── Q116 — تضاد | foundation | 0.3 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.3,
            text_ar="نظافة : قذارة",
            option_a="أمانة : خيانة",
            option_b="ماء : بحر",
            option_c="مدرسة : طالب",
            option_d="شجرة : ظلّ",
            correct_option="a",
            explanation_ar="نوع العلاقة: تضاد\n• نظافة عكس قذارة\n• أمانة عكس خيانة ✓",
            solution_steps_ar='["تحديد العلاقة: نظافة عكس قذارة","البحث عن نفس العلاقة: تضاد","أمانة عكس خيانة ✓"]',
        tags="antonym", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q117 — مادة ← منتج | foundation | 0.4 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.4,
            text_ar="طين : فخّار",
            option_a="قطن : قماش",
            option_b="فلّاح : حقل",
            option_c="نهر : سمك",
            option_d="شجاعة : جبن",
            correct_option="a",
            explanation_ar="نوع العلاقة: مادة خام ← منتج\n• الطين يُصنع منه الفخّار\n• القطن يُصنع منه القماش ✓",
            solution_steps_ar='["تحديد العلاقة: الطين مادة خام تُصنع منها الفخّار","البحث عن نفس العلاقة: مادة خام ← منتج","القطن مادة خام يُصنع منها القماش ✓"]',
        tags="material-product", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q118 — شخص ← مكان | foundation | 0.4 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.4,
            text_ar="بحّار : سفينة",
            option_a="سائق : حافلة",
            option_b="بحر : موج",
            option_c="سمك : ماء",
            option_d="رمل : صحراء",
            correct_option="a",
            explanation_ar="نوع العلاقة: شخص ← مكان عمله\n• البحّار يعمل في السفينة\n• السائق يعمل في الحافلة ✓",
            solution_steps_ar='["تحديد العلاقة: البحّار يعمل في السفينة","البحث عن نفس العلاقة: شخص ← مكان","السائق يعمل في الحافلة ✓"]',
        tags="agent-place", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q119 — مُنتِج ← مُنتَج | foundation | 0.4 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.4,
            text_ar="بنّاء : مبنى",
            option_a="حدّاد : سيف",
            option_b="حديد : صلابة",
            option_c="مصنع : عامل",
            option_d="طريق : سيارة",
            correct_option="a",
            explanation_ar="نوع العلاقة: مُنتِج ← مُنتَج\n• البنّاء يُنتج المبنى\n• الحدّاد يُنتج السيف ✓",
            solution_steps_ar='["تحديد العلاقة: البنّاء يُنتج المبنى","البحث عن نفس العلاقة: مُنتِج ← مُنتَج","الحدّاد يُنتج السيف ✓"]',
        tags="agent-product", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q120 — تدرّج | foundation | 0.4 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.4,
            text_ar="قلق : هلع",
            option_a="فرح : نشوة",
            option_b="كتاب : مكتبة",
            option_c="طبيب : مريض",
            option_d="شمس : قمر",
            correct_option="a",
            explanation_ar="نوع العلاقة: تدرّج في الشدّة\n• القلق أقلّ شدّة من الهلع\n• الفرح أقلّ شدّة من النشوة ✓",
            solution_steps_ar='["تحديد العلاقة: القلق أقلّ حدّة من الهلع","البحث عن نفس العلاقة: تدرّج في الشدّة","الفرح أقلّ حدّة من النشوة ✓"]',
        tags="degree", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q121 — رمز ← معنى | foundation | 0.3 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.3,
            text_ar="تاج : مُلك",
            option_a="خاتم : زواج",
            option_b="ذهب : ثمن",
            option_c="ملك : قصر",
            option_d="جيش : حرب",
            correct_option="a",
            explanation_ar="نوع العلاقة: رمز ← معنى\n• التاج رمز للمُلك\n• الخاتم رمز للزواج ✓",
            solution_steps_ar='["تحديد العلاقة: التاج يرمز إلى المُلك","البحث عن نفس العلاقة: رمز ← معنى","الخاتم يرمز إلى الزواج ✓"]',
        tags="symbol-meaning", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q122 — أداة ← وظيفة | foundation | 0.4 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.4,
            text_ar="مِبراة : بري",
            option_a="مِمحاة : محو",
            option_b="تلميذ : دفتر",
            option_c="لون : رسم",
            option_d="ورقة : شجرة",
            correct_option="a",
            explanation_ar="نوع العلاقة: أداة ← وظيفتها\n• المِبراة أداة للبري\n• المِمحاة أداة للمحو ✓",
            solution_steps_ar='["تحديد العلاقة: المِبراة أداة وظيفتها البري","البحث عن نفس العلاقة: أداة ← وظيفة","المِمحاة أداة وظيفتها المحو ✓"]',
        tags="tool-function", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q123 — ترادف | foundation | 0.4 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.4,
            text_ar="خوف : فزع",
            option_a="حيرة : ارتباك",
            option_b="ليل : نهار",
            option_c="قلم : كتابة",
            option_d="مدرسة : معلّم",
            correct_option="a",
            explanation_ar="نوع العلاقة: ترادف\n• الخوف والفزع بمعنى متقارب\n• الحيرة والارتباك بمعنى متقارب ✓",
            solution_steps_ar='["تحديد العلاقة: الخوف يرادف الفزع","البحث عن نفس العلاقة: ترادف","الحيرة ترادف الارتباك ✓"]',
        tags="synonym", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ══════════════════════════════════════
        # Building stage — 18 questions
        # ══════════════════════════════════════

        # ── Q124 — سبب ← نتيجة | building | 0.5 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.5,
            text_ar="إسراف : ديون",
            option_a="تدخين : مرض",
            option_b="كتاب : رفّ",
            option_c="طبيب : عيادة",
            option_d="شجرة : ورقة",
            correct_option="a",
            explanation_ar="نوع العلاقة: سبب ← نتيجة\n• الإسراف يؤدي إلى الديون\n• التدخين يؤدي إلى المرض ✓",
            solution_steps_ar='["تحديد العلاقة: الإسراف سبب والديون نتيجة","البحث عن نفس العلاقة: سبب ← نتيجة","التدخين سبب والمرض نتيجة ✓"]',
        tags="cause-effect", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q125 — تضاد | building | 0.5 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.5,
            text_ar="عدل : ظلم",
            option_a="صدق : كذب",
            option_b="قاضٍ : محكمة",
            option_c="كتاب : علم",
            option_d="طعام : شراب",
            correct_option="a",
            explanation_ar="نوع العلاقة: تضاد\n• عدل عكس ظلم\n• صدق عكس كذب ✓",
            solution_steps_ar='["تحديد العلاقة: عدل عكس ظلم","البحث عن نفس العلاقة: تضاد","صدق عكس كذب ✓"]',
        tags="antonym", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q126 — جزء ← كلّ | building | 0.5 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.5,
            text_ar="مقطع : قصيدة",
            option_a="فصل : رواية",
            option_b="شاعر : أدب",
            option_c="قلم : حبر",
            option_d="غنى : فقر",
            correct_option="a",
            explanation_ar="نوع العلاقة: جزء ← كلّ\n• المقطع جزء من القصيدة\n• الفصل جزء من الرواية ✓",
            solution_steps_ar='["تحديد العلاقة: المقطع جزء من القصيدة","البحث عن نفس العلاقة: جزء ← كلّ","الفصل جزء من الرواية ✓"]',
        tags="part-whole", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q127 — مادة ← منتج | building | 0.5 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.5,
            text_ar="جلد : حذاء",
            option_a="مطّاط : إطار",
            option_b="حذّاء : سوق",
            option_c="قدم : ساق",
            option_d="مشي : طريق",
            correct_option="a",
            explanation_ar="نوع العلاقة: مادة خام ← منتج\n• الجلد يُصنع منه الحذاء\n• المطّاط يُصنع منه الإطار ✓",
            solution_steps_ar='["تحديد العلاقة: الجلد مادة خام تُصنع منها الحذاء","البحث عن نفس العلاقة: مادة خام ← منتج","المطّاط مادة خام يُصنع منها الإطار ✓"]',
        tags="material-product", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q128 — شخص ← مكان | building | 0.5 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.5,
            text_ar="مهندس : موقع",
            option_a="مذيع : استوديو",
            option_b="تصميم : خريطة",
            option_c="بناء : إسمنت",
            option_d="أرض : سماء",
            correct_option="a",
            explanation_ar="نوع العلاقة: شخص ← مكان عمله\n• المهندس يعمل في الموقع\n• المذيع يعمل في الاستوديو ✓",
            solution_steps_ar='["تحديد العلاقة: المهندس يعمل في الموقع","البحث عن نفس العلاقة: شخص ← مكان","المذيع يعمل في الاستوديو ✓"]',
        tags="agent-place", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q129 — تدرّج | building | 0.4 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.4,
            text_ar="دفء : حرّ شديد",
            option_a="برودة : تجمّد",
            option_b="شمس : قمر",
            option_c="صيف : شتاء",
            option_d="نار : حطب",
            correct_option="a",
            explanation_ar="نوع العلاقة: تدرّج في الشدّة\n• الدفء أقلّ شدّة من الحرّ الشديد\n• البرودة أقلّ شدّة من التجمّد ✓",
            solution_steps_ar='["تحديد العلاقة: الدفء أقلّ حدّة من الحرّ الشديد","البحث عن نفس العلاقة: تدرّج في الشدّة","البرودة أقلّ حدّة من التجمّد ✓"]',
        tags="degree", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q130 — رمز ← معنى | building | 0.4 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.4,
            text_ar="هلال : إسلام",
            option_a="صليب : مسيحية",
            option_b="مسجد : صلاة",
            option_c="كتاب : علم",
            option_d="شمس : نهار",
            correct_option="a",
            explanation_ar="نوع العلاقة: رمز ← معنى\n• الهلال رمز للإسلام\n• الصليب رمز للمسيحية ✓",
            solution_steps_ar='["تحديد العلاقة: الهلال يرمز إلى الإسلام","البحث عن نفس العلاقة: رمز ← معنى","الصليب يرمز إلى المسيحية ✓"]',
        tags="symbol-meaning", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q131 — مُنتِج ← مُنتَج | building | 0.6 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.6,
            text_ar="فنّان : تمثال",
            option_a="مصوّر : صورة",
            option_b="متحف : زائر",
            option_c="حجر : صخرة",
            option_d="جمال : طبيعة",
            correct_option="a",
            explanation_ar="نوع العلاقة: مُنتِج ← مُنتَج\n• الفنّان يُنتج التمثال\n• المصوّر يُنتج الصورة ✓",
            solution_steps_ar='["تحديد العلاقة: الفنّان يُنتج التمثال","البحث عن نفس العلاقة: مُنتِج ← مُنتَج","المصوّر يُنتج الصورة ✓"]',
        tags="agent-product", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q132 — أداة ← وظيفة | building | 0.6 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.6,
            text_ar="مِنظار : مراقبة",
            option_a="رادار : رصد",
            option_b="طائرة : سماء",
            option_c="عالِم : مختبر",
            option_d="بحر : سفينة",
            correct_option="a",
            explanation_ar="نوع العلاقة: أداة ← وظيفتها\n• المِنظار أداة للمراقبة\n• الرادار أداة للرصد ✓",
            solution_steps_ar='["تحديد العلاقة: المِنظار أداة وظيفتها المراقبة","البحث عن نفس العلاقة: أداة ← وظيفة","الرادار أداة وظيفتها الرصد ✓"]',
        tags="tool-function", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ── Q133 — ترادف | building | 0.5 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.5,
            text_ar="بأس : شدّة",
            option_a="عزم : إصرار",
            option_b="ضعف : قوّة",
            option_c="طبيب : مريض",
            option_d="نهر : جسر",
            correct_option="a",
            explanation_ar="نوع العلاقة: ترادف\n• البأس والشدّة بمعنى واحد\n• العزم والإصرار بمعنى واحد ✓",
            solution_steps_ar='["تحديد العلاقة: البأس يرادف الشدّة","البحث عن نفس العلاقة: ترادف","العزم يرادف الإصرار ✓"]',
        tags="synonym", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ── Q134 — سبب ← نتيجة | building | 0.6 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.6,
            text_ar="زلزال : دمار",
            option_a="بركان : حمم",
            option_b="جبل : صخر",
            option_c="أرض : سماء",
            option_d="بيت : سقف",
            correct_option="a",
            explanation_ar="نوع العلاقة: سبب ← نتيجة\n• الزلزال يسبّب الدمار\n• البركان يسبّب الحمم ✓",
            solution_steps_ar='["تحديد العلاقة: الزلزال سبب والدمار نتيجة","البحث عن نفس العلاقة: سبب ← نتيجة","البركان سبب والحمم نتيجة ✓"]',
        tags="cause-effect", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ── Q135 — تضاد | building | 0.6 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.6,
            text_ar="إقدام : إحجام",
            option_a="تقدّم : تراجع",
            option_b="جيش : معركة",
            option_c="كتاب : قلم",
            option_d="طبيب : دواء",
            correct_option="a",
            explanation_ar="نوع العلاقة: تضاد\n• إقدام عكس إحجام\n• تقدّم عكس تراجع ✓",
            solution_steps_ar='["تحديد العلاقة: إقدام عكس إحجام","البحث عن نفس العلاقة: تضاد","تقدّم عكس تراجع ✓"]',
        tags="antonym", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q136 — جزء ← كلّ | building | 0.6 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.6,
            text_ar="آية : سورة",
            option_a="بيت شعر : قصيدة",
            option_b="مسجد : صلاة",
            option_c="حفظ : تلاوة",
            option_d="معلّم : طالب",
            correct_option="a",
            explanation_ar="نوع العلاقة: جزء ← كلّ\n• الآية جزء من السورة\n• بيت الشعر جزء من القصيدة ✓",
            solution_steps_ar='["تحديد العلاقة: الآية جزء من السورة","البحث عن نفس العلاقة: جزء ← كلّ","بيت الشعر جزء من القصيدة ✓"]',
        tags="part-whole", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ── Q137 — مادة ← منتج | building | 0.5 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.5,
            text_ar="نحاس : أسلاك",
            option_a="ذهب : حُلِيّ",
            option_b="منجم : عامل",
            option_c="معدن : صلابة",
            option_d="كهرباء : مصباح",
            correct_option="a",
            explanation_ar="نوع العلاقة: مادة خام ← منتج\n• النحاس يُصنع منه الأسلاك\n• الذهب يُصنع منه الحُلِيّ ✓",
            solution_steps_ar='["تحديد العلاقة: النحاس مادة خام تُصنع منها الأسلاك","البحث عن نفس العلاقة: مادة خام ← منتج","الذهب مادة خام يُصنع منها الحُلِيّ ✓"]',
        tags="material-product", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ── Q138 — شخص ← مكان | building | 0.5 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.5,
            text_ar="حارس : بوّابة",
            option_a="أمين مكتبة : مكتبة",
            option_b="كتاب : رفّ",
            option_c="باب : مفتاح",
            option_d="قلم : ورقة",
            correct_option="a",
            explanation_ar="نوع العلاقة: شخص ← مكان عمله\n• الحارس يعمل عند البوّابة\n• أمين المكتبة يعمل في المكتبة ✓",
            solution_steps_ar='["تحديد العلاقة: الحارس يعمل عند البوّابة","البحث عن نفس العلاقة: شخص ← مكان","أمين المكتبة يعمل في المكتبة ✓"]',
        tags="agent-place", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q139 — أداة ← وظيفة | building | 0.6 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.6,
            text_ar="مِشرط : جراحة",
            option_a="إبرة : خياطة",
            option_b="طبيب : مستشفى",
            option_c="دم : قلب",
            option_d="مريض : علاج",
            correct_option="a",
            explanation_ar="نوع العلاقة: أداة ← وظيفتها\n• المِشرط أداة للجراحة\n• الإبرة أداة للخياطة ✓",
            solution_steps_ar='["تحديد العلاقة: المِشرط أداة وظيفتها الجراحة","البحث عن نفس العلاقة: أداة ← وظيفة","الإبرة أداة وظيفتها الخياطة ✓"]',
        tags="tool-function", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q140 — تدرّج | building | 0.6 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.6,
            text_ar="خطأ : كارثة",
            option_a="شرارة : حريق",
            option_b="ماء : نار",
            option_c="كتاب : مؤلّف",
            option_d="أرض : سماء",
            correct_option="a",
            explanation_ar="نوع العلاقة: تدرّج في الشدّة\n• الخطأ أقلّ شدّة من الكارثة\n• الشرارة أقلّ شدّة من الحريق ✓",
            solution_steps_ar='["تحديد العلاقة: الخطأ أقلّ حدّة من الكارثة","البحث عن نفس العلاقة: تدرّج في الشدّة","الشرارة أقلّ حدّة من الحريق ✓"]',
        tags="degree", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ── Q141 — رمز ← معنى | building | 0.6 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.6,
            text_ar="سيف : بطش",
            option_a="قلم : علم",
            option_b="حرب : جيش",
            option_c="حديد : قوّة",
            option_d="سلاح : رصاص",
            correct_option="a",
            explanation_ar="نوع العلاقة: رمز ← معنى\n• السيف رمز للبطش\n• القلم رمز للعلم ✓",
            solution_steps_ar='["تحديد العلاقة: السيف يرمز إلى البطش","البحث عن نفس العلاقة: رمز ← معنى","القلم يرمز إلى العلم ✓"]',
        tags="symbol-meaning", stage="building",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ══════════════════════════════════════
        # Peak stage — 10 questions
        # ══════════════════════════════════════

        # ── Q142 — ترادف | peak | 0.7 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.7,
            text_ar="فِطنة : ذكاء",
            option_a="حصافة : رشد",
            option_b="جهل : علم",
            option_c="مدرسة : طالب",
            option_d="كتاب : ورقة",
            correct_option="a",
            explanation_ar="نوع العلاقة: ترادف\n• الفِطنة والذكاء بمعنى واحد\n• الحصافة والرشد بمعنى واحد ✓",
            solution_steps_ar='["تحديد العلاقة: الفِطنة ترادف الذكاء","البحث عن نفس العلاقة: ترادف","الحصافة ترادف الرشد ✓"]',
        tags="synonym", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ── Q143 — تضاد | peak | 0.7 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.7,
            text_ar="شُحّ : سخاء",
            option_a="جحود : اعتراف",
            option_b="مال : فقر",
            option_c="طعام : جوع",
            option_d="بيت : سكن",
            correct_option="a",
            explanation_ar="نوع العلاقة: تضاد\n• شُحّ عكس سخاء\n• جحود عكس اعتراف ✓",
            solution_steps_ar='["تحديد العلاقة: شُحّ عكس سخاء","البحث عن نفس العلاقة: تضاد","جحود عكس اعتراف ✓"]',
        tags="antonym", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ── Q144 — سبب ← نتيجة | peak | 0.7 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.7,
            text_ar="احتكار : غلاء",
            option_a="منافسة : انخفاض أسعار",
            option_b="سوق : بضاعة",
            option_c="تاجر : متجر",
            option_d="ذهب : فضة",
            correct_option="a",
            explanation_ar="نوع العلاقة: سبب ← نتيجة\n• الاحتكار يسبّب الغلاء\n• المنافسة تسبّب انخفاض الأسعار ✓",
            solution_steps_ar='["تحديد العلاقة: الاحتكار سبب والغلاء نتيجة","البحث عن نفس العلاقة: سبب ← نتيجة","المنافسة سبب وانخفاض الأسعار نتيجة ✓"]',
        tags="cause-effect", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ── Q145 — مُنتِج ← مُنتَج | peak | 0.7 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.7,
            text_ar="عالِم : نظرية",
            option_a="مخترع : اختراع",
            option_b="مختبر : تجربة",
            option_c="كتاب : مكتبة",
            option_d="جامعة : طالب",
            correct_option="a",
            explanation_ar="نوع العلاقة: مُنتِج ← مُنتَج\n• العالِم يُنتج النظرية\n• المخترع يُنتج الاختراع ✓",
            solution_steps_ar='["تحديد العلاقة: العالِم يُنتج النظرية","البحث عن نفس العلاقة: مُنتِج ← مُنتَج","المخترع يُنتج الاختراع ✓"]',
        tags="agent-product", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ── Q146 — جزء ← كلّ | peak | 0.7 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.7,
            text_ar="خلية : عضو",
            option_a="ذرّة : جُزيء",
            option_b="دم : قلب",
            option_c="طبيب : مستشفى",
            option_d="علم : كتاب",
            correct_option="a",
            explanation_ar="نوع العلاقة: جزء ← كلّ\n• الخلية جزء من العضو\n• الذرّة جزء من الجُزيء ✓",
            solution_steps_ar='["تحديد العلاقة: الخلية جزء من العضو","البحث عن نفس العلاقة: جزء ← كلّ","الذرّة جزء من الجُزيء ✓"]',
        tags="part-whole", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ── Q147 — أداة ← وظيفة | peak | 0.8 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.8,
            text_ar="مِسبار : استكشاف",
            option_a="قمر صناعي : اتصال",
            option_b="فضاء : كوكب",
            option_c="عالِم : مختبر",
            option_d="صاروخ : وقود",
            correct_option="a",
            explanation_ar="نوع العلاقة: أداة ← وظيفتها\n• المِسبار أداة للاستكشاف\n• القمر الصناعي أداة للاتصال ✓",
            solution_steps_ar='["تحديد العلاقة: المِسبار أداة وظيفتها الاستكشاف","البحث عن نفس العلاقة: أداة ← وظيفة","القمر الصناعي أداة وظيفتها الاتصال ✓"]',
        tags="tool-function", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ── Q148 — مادة ← منتج | peak | 0.7 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.7,
            text_ar="سيليكون : رقاقة",
            option_a="ألياف بصرية : كابل",
            option_b="حاسوب : برنامج",
            option_c="مهندس : مصنع",
            option_d="كهرباء : مصباح",
            correct_option="a",
            explanation_ar="نوع العلاقة: مادة خام ← منتج\n• السيليكون يُصنع منه الرقاقة\n• الألياف البصرية يُصنع منها الكابل ✓",
            solution_steps_ar='["تحديد العلاقة: السيليكون مادة خام تُصنع منها الرقاقة","البحث عن نفس العلاقة: مادة خام ← منتج","الألياف البصرية مادة خام يُصنع منها الكابل ✓"]',
        tags="material-product", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # ── Q149 — رمز ← معنى | peak | 0.8 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.8,
            text_ar="بومة : حكمة",
            option_a="نملة : اجتهاد",
            option_b="حيوان : غابة",
            option_c="عين : بصر",
            option_d="طائر : سماء",
            correct_option="a",
            explanation_ar="نوع العلاقة: رمز ← معنى\n• البومة رمز للحكمة\n• النملة رمز للاجتهاد ✓",
            solution_steps_ar='["تحديد العلاقة: البومة ترمز إلى الحكمة","البحث عن نفس العلاقة: رمز ← معنى","النملة ترمز إلى الاجتهاد ✓"]',
        tags="symbol-meaning", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ── Q150 — تدرّج | peak | 0.7 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.7,
            text_ar="إعجاب : افتتان",
            option_a="ريبة : يقين",
            option_b="كُره : بغض",
            option_c="صداقة : عداوة",
            option_d="كتاب : قراءة",
            correct_option="b",
            explanation_ar="نوع العلاقة: تدرّج في الشدّة\n• الإعجاب أقلّ شدّة من الافتتان\n• الكُره أقلّ شدّة من البغض ✓",
            solution_steps_ar='["تحديد العلاقة: الإعجاب أقلّ حدّة من الافتتان","البحث عن نفس العلاقة: تدرّج في الشدّة","الكُره أقلّ حدّة من البغض ✓"]',
        tags="degree", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # ── Q151 — شخص ← مكان | peak | 0.8 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.8,
            text_ar="دبلوماسي : سفارة",
            option_a="قنصل : قنصلية",
            option_b="دولة : حكومة",
            option_c="جواز : سفر",
            option_d="وثيقة : ختم",
            correct_option="a",
            explanation_ar="نوع العلاقة: شخص ← مكان عمله\n• الدبلوماسي يعمل في السفارة\n• القنصل يعمل في القنصلية ✓",
            solution_steps_ar='["تحديد العلاقة: الدبلوماسي يعمل في السفارة","البحث عن نفس العلاقة: شخص ← مكان","القنصل يعمل في القنصلية ✓"]',
        tags="agent-place", stage="peak",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ══════════════════════════════════════
        # Mock stage — 13 questions
        # ══════════════════════════════════════

        # ── Q152 — تضاد | mock | 0.7 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.7,
            text_ar="يقظة : غفلة",
            option_a="حذر : تهوّر",
            option_b="نوم : سرير",
            option_c="ليل : ظلام",
            option_d="عين : نظر",
            correct_option="a",
            explanation_ar="نوع العلاقة: تضاد\n• يقظة عكس غفلة\n• حذر عكس تهوّر ✓",
            solution_steps_ar='["تحديد العلاقة: يقظة عكس غفلة","البحث عن نفس العلاقة: تضاد","حذر عكس تهوّر ✓"]',
        tags="antonym", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # ── Q153 — ترادف | mock | 0.7 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.7,
            text_ar="نُبل : شهامة",
            option_a="مروءة : شرف",
            option_b="غنى : فقر",
            option_c="رجل : امرأة",
            option_d="سيف : حرب",
            correct_option="a",
            explanation_ar="نوع العلاقة: ترادف\n• النُبل والشهامة بمعنى واحد\n• المروءة والشرف بمعنى واحد ✓",
            solution_steps_ar='["تحديد العلاقة: النُبل يرادف الشهامة","البحث عن نفس العلاقة: ترادف","المروءة ترادف الشرف ✓"]',
        tags="synonym", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ── Q154 — سبب ← نتيجة | mock | 0.8 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.8,
            text_ar="تضخّم : انخفاض قيمة العملة",
            option_a="ركود : بطالة",
            option_b="بنك : نقود",
            option_c="تاجر : سوق",
            option_d="ذهب : فضة",
            correct_option="a",
            explanation_ar="نوع العلاقة: سبب ← نتيجة\n• التضخّم يسبّب انخفاض قيمة العملة\n• الركود يسبّب البطالة ✓",
            solution_steps_ar='["تحديد العلاقة: التضخّم سبب وانخفاض قيمة العملة نتيجة","البحث عن نفس العلاقة: سبب ← نتيجة","الركود سبب والبطالة نتيجة ✓"]',
        tags="cause-effect", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ── Q155 — مُنتِج ← مُنتَج | mock | 0.8 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.8,
            text_ar="معماري : مخطّط",
            option_a="رياضي : نظرية",
            option_b="بناية : طابق",
            option_c="هندسة : علم",
            option_d="خريطة : أرض",
            correct_option="a",
            explanation_ar="نوع العلاقة: مُنتِج ← مُنتَج\n• المعماري يُنتج المخطّط\n• الرياضي يُنتج النظرية ✓",
            solution_steps_ar='["تحديد العلاقة: المعماري يُنتج المخطّط","البحث عن نفس العلاقة: مُنتِج ← مُنتَج","الرياضي يُنتج النظرية ✓"]',
        tags="agent-product", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # ── Q156 — جزء ← كلّ | mock | 0.6 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.6,
            text_ar="مقدّمة : بحث",
            option_a="خاتمة : خطبة",
            option_b="كتاب : مؤلّف",
            option_c="علم : جهل",
            option_d="ورقة : قلم",
            correct_option="a",
            explanation_ar="نوع العلاقة: جزء ← كلّ\n• المقدّمة جزء من البحث\n• الخاتمة جزء من الخطبة ✓",
            solution_steps_ar='["تحديد العلاقة: المقدّمة جزء من البحث","البحث عن نفس العلاقة: جزء ← كلّ","الخاتمة جزء من الخطبة ✓"]',
        tags="part-whole", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # ── Q157 — مادة ← منتج | mock | 0.6 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.6,
            text_ar="شمع : شمعة",
            option_a="ورق : كرتون",
            option_b="مصباح : نور",
            option_c="نار : دخان",
            option_d="ليل : ظلام",
            correct_option="a",
            explanation_ar="نوع العلاقة: مادة خام ← منتج\n• الشمع يُصنع منه الشمعة\n• الورق يُصنع منه الكرتون ✓",
            solution_steps_ar='["تحديد العلاقة: الشمع مادة خام تُصنع منها الشمعة","البحث عن نفس العلاقة: مادة خام ← منتج","الورق مادة خام يُصنع منها الكرتون ✓"]',
        tags="material-product", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ── Q158 — تدرّج | mock | 0.2 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.2,
            text_ar="رذاذ : مطر غزير",
            option_a="وميض : بَرق",
            option_b="سحاب : سماء",
            option_c="ماء : نهر",
            option_d="شمس : قمر",
            correct_option="a",
            explanation_ar="نوع العلاقة: تدرّج في الشدّة\n• الرذاذ أقلّ شدّة من المطر الغزير\n• الوميض أقلّ شدّة من البرق ✓",
            solution_steps_ar='["تحديد العلاقة: الرذاذ أقلّ حدّة من المطر الغزير","البحث عن نفس العلاقة: تدرّج في الشدّة","الوميض أقلّ حدّة من البرق ✓"]',
        tags="degree", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ── Q159 — رمز ← معنى | mock | 0.5 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.5,
            text_ar="نخلة : صمود",
            option_a="جبل : ثبات",
            option_b="صحراء : رمل",
            option_c="واحة : ماء",
            option_d="شجرة : ظلّ",
            correct_option="a",
            explanation_ar="نوع العلاقة: رمز ← معنى\n• النخلة رمز للصمود\n• الجبل رمز للثبات ✓",
            solution_steps_ar='["تحديد العلاقة: النخلة ترمز إلى الصمود","البحث عن نفس العلاقة: رمز ← معنى","الجبل يرمز إلى الثبات ✓"]',
        tags="symbol-meaning", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=4, rating_overall=4.71),

        # ── Q160 — أداة ← وظيفة | mock | 0.6 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.6,
            text_ar="مِجهر إلكتروني : تحليل",
            option_a="طيف كتلي : قياس",
            option_b="عالِم : مختبر",
            option_c="ذرّة : جُزيء",
            option_d="كيمياء : تفاعل",
            correct_option="a",
            explanation_ar="نوع العلاقة: أداة ← وظيفتها\n• المِجهر الإلكتروني أداة للتحليل\n• الطيف الكتلي أداة للقياس ✓",
            solution_steps_ar='["تحديد العلاقة: المِجهر الإلكتروني أداة وظيفتها التحليل","البحث عن نفس العلاقة: أداة ← وظيفة","الطيف الكتلي أداة وظيفتها القياس ✓"]',
        tags="tool-function", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q161 — شخص ← مكان | mock | 0.6 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.6,
            text_ar="جرّاح : غرفة عمليات",
            option_a="ربّان : قُمرة قيادة",
            option_b="مريض : سرير",
            option_c="دواء : صيدلية",
            option_d="مشرط : دم",
            correct_option="a",
            explanation_ar="نوع العلاقة: شخص ← مكان عمله\n• الجرّاح يعمل في غرفة العمليات\n• الربّان يعمل في قُمرة القيادة ✓",
            solution_steps_ar='["تحديد العلاقة: الجرّاح يعمل في غرفة العمليات","البحث عن نفس العلاقة: شخص ← مكان","الربّان يعمل في قُمرة القيادة ✓"]',
        tags="agent-place", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ── Q162 — تضاد | mock | 0.4 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.4,
            text_ar="إفراط : تفريط",
            option_a="إسهاب : إيجاز",
            option_b="كلام : صمت",
            option_c="كتاب : قلم",
            option_d="بحر : نهر",
            correct_option="a",
            explanation_ar="نوع العلاقة: تضاد\n• إفراط عكس تفريط\n• إسهاب عكس إيجاز ✓",
            solution_steps_ar='["تحديد العلاقة: إفراط عكس تفريط","البحث عن نفس العلاقة: تضاد","إسهاب عكس إيجاز ✓"]',
        tags="antonym", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ── Q163 — سبب ← نتيجة | mock | 0.7 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.7,
            text_ar="قراءة : ثقافة",
            option_a="تدريب : مهارة",
            option_b="كتاب : مكتبة",
            option_c="معلّم : فصل",
            option_d="طالب : شهادة",
            correct_option="a",
            explanation_ar="نوع العلاقة: سبب ← نتيجة\n• القراءة تؤدي إلى الثقافة\n• التدريب يؤدي إلى المهارة ✓",
            solution_steps_ar='["تحديد العلاقة: القراءة سبب والثقافة نتيجة","البحث عن نفس العلاقة: سبب ← نتيجة","التدريب سبب والمهارة نتيجة ✓"]',
        tags="cause-effect", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=5, rating_overall=4.71),

        # ── Q164 — ترادف | mock | 0.3 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.3,
            text_ar="ظلمة : عتمة",
            option_a="وضوح : جلاء",
            option_b="نور : ظلام",
            option_c="شمس : قمر",
            option_d="نهار : صباح",
            correct_option="a",
            explanation_ar="نوع العلاقة: ترادف\n• الظلمة والعتمة بمعنى واحد\n• الوضوح والجلاء بمعنى واحد ✓",
            solution_steps_ar='["تحديد العلاقة: الظلمة ترادف العتمة","البحث عن نفس العلاقة: ترادف","الوضوح يرادف الجلاء ✓"]',
        tags="synonym", stage="mock",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q165 — مُنتِج ← مُنتَج | foundation | 0.8 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.8,
            text_ar="فيلسوف : فلسفة",
            option_a="عالِم لغة : قاموس",
            option_b="كتاب : مكتبة",
            option_c="جامعة : طالب",
            option_d="فكر : عقل",
            correct_option="a",
            explanation_ar="نوع العلاقة: مُنتِج ← مُنتَج\n• الفيلسوف يُنتج الفلسفة\n• عالِم اللغة يُنتج القاموس ✓",
            solution_steps_ar='["تحديد العلاقة: الفيلسوف يُنتج الفلسفة","البحث عن نفس العلاقة: مُنتِج ← مُنتَج","عالِم اللغة يُنتج القاموس ✓"]',
        tags="agent-product", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),

        # ── Q166 — جزء ← كلّ | foundation | 0.5 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.5,
            text_ar="مشهد : مسرحية",
            option_a="حلقة : مسلسل",
            option_b="ممثّل : جمهور",
            option_c="تمثيل : فنّ",
            option_d="مسرح : ستارة",
            correct_option="a",
            explanation_ar="نوع العلاقة: جزء ← كلّ\n• المشهد جزء من المسرحية\n• الحلقة جزء من المسلسل ✓",
            solution_steps_ar='["تحديد العلاقة: المشهد جزء من المسرحية","البحث عن نفس العلاقة: جزء ← كلّ","الحلقة جزء من المسلسل ✓"]',
        tags="part-whole", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=5, rating_explanation=5, rating_discrimination=5, rating_overall=4.86),

        # ── Q167 — أداة ← وظيفة | foundation | 0.4 ──
        Question(
            skill_id="verbal_analogy", question_type="analogy", difficulty=0.4,
            text_ar="مِروحة : تهوية",
            option_a="مكيّف : تبريد",
            option_b="حرارة : صيف",
            option_c="غرفة : نافذة",
            option_d="هواء : أكسجين",
            correct_option="a",
            explanation_ar="نوع العلاقة: أداة ← وظيفتها\n• المِروحة أداة للتهوية\n• المكيّف أداة للتبريد ✓",
            solution_steps_ar='["تحديد العلاقة: المِروحة أداة وظيفتها التهوية","البحث عن نفس العلاقة: أداة ← وظيفة","المكيّف أداة وظيفتها التبريد ✓"]',
        tags="tool-function", stage="foundation",
    rating_clarity=5, rating_cognitive=4, rating_fairness=5, rating_distractors=5, rating_difficulty_align=4, rating_explanation=5, rating_discrimination=4, rating_overall=4.57),
    ]
