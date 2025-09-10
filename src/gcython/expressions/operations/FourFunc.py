from gcython.core.IObject import IObject, IProps
from dataclasses import dataclass
from strongtyping.strong_typing import match_class_typing
from enum import Enum

class FourFuncOperation(Enum):
    ADD = "+"
    SUB = "-"
    MUL = "*"
    DIV = "/"

@match_class_typing
@dataclass
class Props(IProps):
    operation: FourFuncOperation
    children: tuple[IObject,...]

    def __init__(self, operation:FourFuncOperation, *children: IObject):
        self.operation = operation
        self.children = children

class FourFunc(IObject[Props]):
    PropsClass = Props

    @property
    def contents(self):
        return self.props.children

    def __latex__(self) -> str:
        return "\\left(" + \
            self.props.operation.value.join(
                [child.__latex__() for child in self.contents]
            ) + "\\right)"