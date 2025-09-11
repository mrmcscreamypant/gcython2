"""gcython demo"""
print(__doc__)

"""
import rich

from gcython.expressions import Num, Point
from gcython.expressions.operations import Sqrt, FourFunc, FourFuncSymbol
from pylatexenc.latex2text import LatexNodes2Text

def gen_exp():
    yield FourFunc(FourFuncSymbol.MUL,
        Sqrt(Num(2)),
        Num(0.2)
    )
    yield Num(-2)
    yield Point(Num(2.3),Num(0),Num(1))

exp = FourFunc(FourFuncSymbol.DIV,*gen_exp())

latex = exp.__latex__()
unicode = LatexNodes2Text().latex_to_text(latex)
#rich.print(exp)
#print(latex)
print(unicode)
"""

from gcython.VM import VM, VMVar
from gcython.expressions import Num

class App(VM):
    GLOBAL_VARS = [
        VMVar("a",Num(2))
    ]

if __name__ == "__main__":
    app = App()
    print(app.compose())