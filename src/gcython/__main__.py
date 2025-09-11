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
from gcython.expressions import Num, Action, Pointer, ActionList
from gcython.expressions.operations import FourFunc, FourFuncSymbol
from typing import Generator, Any
from rich import print

class App(VM):
    a = Pointer("a", Num(1))
    b = Pointer("b", Num(0))

    @VM.action
    def foo(self) -> Generator[ActionList|Action, Any, None]:
        yield Action(self.a,FourFunc(
            FourFuncSymbol.DIV,
            self.a,
            Num(2)
        ))
        yield Action(self.b,FourFunc(
            FourFuncSymbol.ADD,
            self.b,
            self.a
        ))
    
    @property
    def TICKER(self):
        return ActionList(self.foo)

if __name__ == "__main__":
    app = App()
    print(app.compose())