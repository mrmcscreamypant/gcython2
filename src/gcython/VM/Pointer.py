from gcython.core import IObject
from gcython.expressions import Pointer
from dataclasses import dataclass
from .IVMObject import IVMObject

@dataclass
class VMPointer(IVMObject):
    name: str
    initial: IObject

    def __compose__(self) -> Pointer:
        return Pointer(self.name, self.initial)