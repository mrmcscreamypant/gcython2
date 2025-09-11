from gcython.core.IObject import IObject, IProps
from dataclasses import dataclass
from strongtyping.strong_typing import match_class_typing

@match_class_typing
@dataclass
class Props(IProps):
    value: int|float

class Num(IObject[Props]):
    PropsClass = Props

    @property
    def value(self):
        return self.props.value

    def __latex__(self) -> str:
        return str(self.value)

    def __enter__(self):
        pass