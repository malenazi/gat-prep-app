from .verbal_reading import get_questions as _vr
from .verbal_analogy import get_questions as _va
from .verbal_completion import get_questions as _vc
from .verbal_error import get_questions as _ve
from .verbal_oddword import get_questions as _vo
from .quant_arithmetic import get_questions as _qa
from .quant_geometry import get_questions as _qg
from .quant_algebra import get_questions as _qal
from .quant_statistics import get_questions as _qs
from generated_question_bank import AUTHORING_SOURCE_HUMAN, load_generated_questions
from question_content import apply_content_refresh
from .visual_quant_upgrade import apply_visual_refresh
from .content_expansion import get_all_expansion_questions
from question_visuals import normalize_question_visual_fields

QUESTION_MODULES = (
    ("verbal_reading", _vr),
    ("verbal_analogy", _va),
    ("verbal_completion", _vc),
    ("verbal_error", _ve),
    ("verbal_oddword", _vo),
    ("quant_arithmetic", _qa),
    ("quant_geometry", _qg),
    ("quant_algebra", _qal),
    ("quant_statistics", _qs),
)

def assign_source_keys(questions, source_prefix: str):
    for index, question in enumerate(questions, start=1):
        if not getattr(question, "source_key", None):
            question.source_key = f"{source_prefix}:{index:04d}"
        if not getattr(question, "authoring_source", None):
            question.authoring_source = AUTHORING_SOURCE_HUMAN
    return questions


def load_all_questions(*, apply_refresh: bool = True):
    questions = []
    for source_prefix, loader in QUESTION_MODULES:
        questions.extend(assign_source_keys(loader(), source_prefix))
    questions.extend(load_generated_questions())

    apply_visual_refresh(questions)
    questions.extend(get_all_expansion_questions())
    if apply_refresh:
        apply_content_refresh(questions)
    return [normalize_question_visual_fields(question) for question in questions]
