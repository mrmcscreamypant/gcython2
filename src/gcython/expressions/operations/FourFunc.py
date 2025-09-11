from gcython.core.IObject import IObject, IProps
from dataclasses import dataclass
from strongtyping.strong_typing import match_class_typing
from enum import Enum

def _div_exp(*c):
    c = [*c]
    l = c.pop()
    f = _div_exp(*c) if len(c) > 1 else c[0]
    return "\\frac{"+f+"}{"+l+"}"

class FourFuncSymbol(Enum):
    ADD = (lambda *c:"+".join(c),)
    SUB = (lambda *c:"-".join(c),)
    MUL = (lambda *c:"\\cdot".join(c),)
    DIV = (_div_exp,)

@match_class_typing
@dataclass
class Props(IProps):
    operation: FourFuncSymbol
    children: tuple[IObject,...]

    def __init__(self, operation:FourFuncSymbol, *children: IObject):
        self.operation = operation
        self.children = children


class FourFunc(IObject[Props]):
    PropsClass = Props

    @property
    def contents(self):
        return self.props.children

    def __latex__(self) -> str:
        return "\\left(" + \
            self.props.operation.value[0](
                *[child.__latex__() for child in self.contents]
            ) + "\\right)"