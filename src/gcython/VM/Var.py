from gcython.core import IObject
from gcython.expressions import Var, Pointer
from dataclasses import dataclass
from .IVMObject import IVMObject
from typing import Any

@dataclass
class VMVar(IVMObject):
    name: str
    value: IObject

    def __compose__(self) -> list[IObject[Any]]:
        return [Var(Pointer(self.name),self.value)]