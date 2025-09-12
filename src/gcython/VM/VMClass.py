from gcython.expressions import Pointer, ActionList
from gcython.core import IObject
from .Var import VMVar
from .IVMObject import IVMObject
from dataclasses import dataclass

from typing import Any

class VMClass():
    VARS: list[IVMObject] = []

    def __init__(self):
        super().__init__()
        self._locate_marked_actions()
    
    def _locate_marked_actions(self):
        for i,attr in enumerate(self.__class__.__dict__.values()):
            key = [*self.__class__.__dict__.keys()][i]

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
        return obj.__class__.__name__+"M"+method.__name__
    
    @staticmethod
    def attrname(obj,attr):
        return obj.__class__.__name__+"A"+attr.__name__

@dataclass
class VMClassMethod(IVMObject):
    cls: VMClass
    method: Any

    def __compose__(self) -> IObject:
        return VMVar(
            self.cls.methodname(self.cls, self.method),
            ActionList(*[
                (action.__compose__() if issubclass(action.__class__,IVMObject) else action)
                for action in self.method(self.cls)
            ])
        ).__compose__()