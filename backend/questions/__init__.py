from .verbal_reading import get_questions as _vr
from .verbal_analogy import get_questions as _va
from .verbal_completion import get_questions as _vc
from .verbal_error import get_questions as _ve
from .verbal_oddword import get_questions as _vo
from .quant_arithmetic import get_questions as _qa
from .quant_geometry import get_questions as _qg
from .quant_algebra import get_questions as _qal
from .quant_statistics import get_questions as _qs


def load_all_questions():
    return _vr() + _va() + _vc() + _ve() + _vo() + _qa() + _qg() + _qal() + _qs()
