"""gcython demo"""
print(__doc__)

import rich

from gcython.expressions import Num
from gcython.expressions.operations import Sqrt, FourFunc, FourFuncSymbol
from pylatexenc.latex2text import LatexNodes2Text

def gen_exp():
    yield FourFunc(FourFuncSymbol.MUL,
        Sqrt(Num(2)),
        Num(0.2)
    )
    yield Num(-2)

exp = FourFunc(FourFuncSymbol.DIV,*gen_exp())

latex = exp.__latex__()
markdown = LatexNodes2Text().latex_to_text(latex)
rich.print(exp)
print(latex)
print(markdown)