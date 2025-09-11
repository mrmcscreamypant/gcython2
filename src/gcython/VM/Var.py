from gcython.core import IObject
from dataclasses import dataclass

@dataclass
class VMVar:
    name: str
    value: IObject

    def __compose__(self) -> str:
        return self.name