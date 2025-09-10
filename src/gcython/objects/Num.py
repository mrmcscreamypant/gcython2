from gcython.core.IObject import IObject, IProps
from dataclasses import dataclass

@dataclass
class Props(IProps):
    value: int

class Num(IObject):
    @property
    def Props(self) -> type[IProps]:
        return Props