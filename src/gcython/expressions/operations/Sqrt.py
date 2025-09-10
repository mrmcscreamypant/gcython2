from gcython.core.IObject import IObject, IProps
from dataclasses import dataclass
from strongtyping.strong_typing import match_class_typing

@match_class_typing
@dataclass
class Props(IProps):
    child: IObject

class Sqrt(IObject[Props]):
    PropsClass = Props

    @property
    def contents(self):
        return self.props.child

    def __latex__(self) -> str:
        return "\\sqrt{"+self.contents.__latex__()+"}"