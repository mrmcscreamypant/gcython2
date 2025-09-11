from .Var import VMVar
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
    expressions: list[IObject]
    ticker: None|IObject

    def __rich__(self) -> Table:
        table = Table(highlight=True,show_lines=True)

        table.add_column("latex")
        table.add_column("expression")
        
        for exp in self.expressions:
            latex = exp.__latex__()
            unicode = str(LatexNodes2Text().latex_to_text(latex))
            table.add_row(latex,unicode)
    
        return table
            

class VM(ABC):
    GLOBAL_VARS: list[IVMObject] = []

    @property
    @abstractmethod
    def TICKER(self) -> ActionList|Action:
        pass

    def __init__(self):
        super().__init__()
        self._locate_marked_actions()
    
    def _locate_marked_actions(self):
        for method in self.__class__.__dict__.values():
            if hasattr(method, "is_vm_action"):
                pointer = VMMethod(self,method)
                self.GLOBAL_VARS.append(pointer)
                self.__dict__[method.__name__] = Pointer(self.methodname(self,method))

    @classmethod
    def action(cls, func:Any):
        func.is_vm_action = True
        return func

    @staticmethod
    def methodname(obj,method):
        return obj.__class__.__name__+"M"+method.__name__

    def compose(self, minify=True, obfiscate=False) -> CompiledVM:
        """Compile the VM to latex.
        
        Keyword arguments:
        minify -- compress the compiled code. (default True)
        obfiscate -- replace variable names with shorter names (default False)
        """
        expressions: list[IObject] = []

        for var in self.GLOBAL_VARS:
            expressions.append(var.__compose__())

        ticker = None
        if self.TICKER:
            ticker = self.TICKER
        
        return CompiledVM(expressions,ticker)

@dataclass
class VMMethod(IVMObject):
    vm: VM
    method: Any

    def __compose__(self) -> IObject:
        return VMVar(
            self.vm.methodname(self.vm, self.method),
            ActionList(*[
                (action.__compose__() if issubclass(action.__class__,IVMObject) else action)
                for action in self.method(self.vm)
            ])
        ).__compose__()