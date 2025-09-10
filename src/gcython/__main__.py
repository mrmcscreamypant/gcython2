"""gcython demo"""
print(__doc__)

import rich

from gcython.expressions import Num
from gcython.expressions.operations import Sqrt, FourFunc
from gcython.expressions.operations.FourFunc import FourFuncOperation
from pylatexenc.latex2text import LatexNodes2Text

def gen_exp():
    yield Sqrt(Num(2))
    yield Num(0.2)

exp = FourFunc(FourFuncOperation.ADD,*gen_exp())

latex = exp.__latex__()
markdown = LatexNodes2Text().latex_to_text(latex)
rich.print(exp)
print(latex)
print(markdown)