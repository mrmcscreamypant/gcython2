from .Var import VMVar
from .VMClass import VMClass
from gcython.core import IObject
from gcython.expressions import ActionList, Pointer, Action
from dataclasses import dataclass
from .IVMObject import IVMObject
from pylatexenc.latex2text import LatexNodes2Text
from typing import Any
from abc import ABC, abstractmethod

from rich.table import Table

@dataclass(frozen=True)
class CompiledVM:
    expressions: list[str]
    ticker: None|IObject

    def __rich__(self) -> Table:
        table = Table(highlight=True,show_lines=True)

        table.add_column("latex")
        table.add_column("expression")
        
        for exp in self.expressions:
            unicode = str(LatexNodes2Text().latex_to_text(exp))
            table.add_row(exp,unicode)
    
        return table
            

class VM(ABC):
    GLOBAL_VARS: list[IVMObject] = []
    CLASSES: list[VMClass] = []

    @property
    @abstractmethod
    def TICKER(self) -> ActionList|Action:
        pass

    def __init__(self):
        super().__init__()
    
    def _locate_marked_actions(self):
        for i,attr in enumerate(self.__class__.__dict__.values()):
            key = [*self.__class__.__dict__.keys()][i]

            if hasattr(attr, "is_vm_action"):
                pointer = VMMethod(self,attr)
                self.GLOBAL_VARS.append(pointer)
                self.__dict__[key] = Pointer(self.methodname(self,attr))
            
            if isinstance(attr, Pointer):
                self.__dict__[key] = Pointer(self.attrname(self,attr))
                self.GLOBAL_VARS.append(VMVar(self.attrname(self,attr), attr.inital))

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

    def compose(self, minify=True, obfiscate=False) -> CompiledVM:
        """Compile the VM to latex.
        
        Keyword arguments:
        minify -- compress the compiled code. (default True)
        obfiscate -- replace variable names with shorter names (default False)
        """
        self._locate_marked_actions()
        expressions: list[IObject[Any]] = []

        for var in self.GLOBAL_VARS:
            expressions += var.__compose__()
        
        for cls in self.CLASSES:
            cls.__name__ = self.__class__.__name__ + "C" + cls.__name__
            expressions += cls.__compose__()

        ticker = None
        if self.TICKER:
            ticker = self.TICKER
        
        compiled_expressions: list[str] = []

        for exp in expressions:
            compiled_expressions.append(exp.__latex__())
        
        return CompiledVM(compiled_expressions,ticker)

@dataclass
class VMMethod(IVMObject):
    vm: VM
    method: Any

    def __compose__(self) -> list[IObject[Any]]:
        return VMVar(
            self.vm.methodname(self.vm, self.method),
            ActionList(*[
                (action.__compose__() if issubclass(action.__class__,IVMObject) else action)
                for action in self.method(self.vm)
            ])
        ).__compose__()