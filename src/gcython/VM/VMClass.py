from gcython.expressions import Pointer, ActionList
from gcython.core import IObject
from gcython.expressions import Num
from .Var import VMVar
from .IVMObject import IVMObject
from dataclasses import dataclass

from typing import Any

class VMClass(IVMObject):
    __name__: str
    VARS: list[IVMObject] = []
    compiled: bool = False

    def __init__(self, name:str):
        super().__init__()
        self.__name__ = self.__class__.__name__
        self.name = name
    
    def _locate_marked_actions(self):
        static = (*self.__dict__.values(),)
        static_keys = (*self.__dict__.keys(),)
        for i,attr in enumerate(static):
            key = static_keys[i]

            if hasattr(attr, "is_vm_action"):
                pointer = VMClassMethod(self,attr)
                self.VARS.append(pointer)
                self.__dict__[key] = Pointer(self.methodname(self,attr))
            
            if isinstance(attr, Pointer):
                self.__dict__[key] = Pointer(self.attrname(self,attr))
                self.VARS.append(VMVar(self.attrname(self,attr), attr.inital))

    @classmethod
    def action(cls, func:Any):
        func.is_vm_action = True
        return func

    @staticmethod
    def methodname(obj,method):
        return obj.__name__+"M"+method.__name__
    
    @staticmethod
    def attrname(obj,attr):
        return obj.__name__+"A"+attr.__name__

    def __compose__(self) -> list[IObject[Any]]:
        if self.compiled:
            raise ReferenceError(f"Tried to recompile {self}")
        self._locate_marked_actions()
        expressions: list[IObject[Any]] = []
        for var in self.VARS:
            expressions += var.__compose__()
        self.compiled = True
        return expressions

@dataclass
class VMClassMethod(IVMObject):
    cls: VMClass
    method: Any

    def __compose__(self) -> list[IObject[Any]]:
        return VMVar(
            self.cls.methodname(self.cls, self.method),
            ActionList(*[
                (action.__compose__() if issubclass(action.__class__,IVMObject) else action)
                for action in self.method(self.cls)
            ])
        ).__compose__()