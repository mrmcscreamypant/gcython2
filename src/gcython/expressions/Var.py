from gcython.core.IObject import IObject, IProps
from dataclasses import dataclass
from strongtyping.strong_typing import match_class_typing
from .Pointer import Pointer

@match_class_typing
@dataclass
class VarProps(IProps):
    pointer: Pointer
    value: IObject

class Var(IObject[VarProps]):
    PropsClass = VarProps

    @property
    def pointer(self) -> Pointer:
        return self.props.pointer

    @property
    def value(self) -> IObject:
        return self.props.value

    def __latex__(self) -> str:
        return self.pointer.name+"="+self.value.__latex__()