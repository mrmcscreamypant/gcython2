from gcython.core.IObject import IObject, IProps
from dataclasses import dataclass
from strongtyping.strong_typing import match_class_typing

@match_class_typing
@dataclass
class Props(IProps):
    name: str
    value: IObject

class Var(IObject[Props]):
    PropsClass = Props

    @property
    def name(self):
        return self.props.name

    @property
    def value(self):
        return self.props.value

    def __latex__(self) -> str:
        return str(self.value)