from gcython.core import IObject
from gcython.expressions import Var, Pointer
from dataclasses import dataclass
from .IVMObject import IVMObject

@dataclass
class VMVar(IVMObject):
    name: str
    value: IObject

    def __compose__(self) -> Var:
        return Var(Pointer(self.name),self.value)