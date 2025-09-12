from gcython.VM import VM, VMClass
from gcython.core import IObject
from gcython.expressions import ActionList, Pointer, Num
from .MethodCall import MethodCall
from .ClassMethod import ClassMethod
from typing import Any
from types import FunctionType


class GCScriptVM(VM):
    @property
    def TICKER(self):
        return ActionList()

CAST_MAPPINGS: dict[str, type[IObject[Any]]] = {
    "Number": Num,
}

CAST_POINTERS: dict[type[Any], FunctionType] = {
    MethodCall: lambda pointer, t, compiler: compiler.cast_type(t, pointer.ref),
    ClassMethod: lambda method, t, compiler: Pointer(method.full_name(compiler.vm)),
}

class Compiler:
    vm: VM

    def __init__(self, model):
        print("Starting compile...")
        self.model = model
        self.vm = GCScriptVM()
        self.locate_classes()
        print(self.vm.compose())
    
    def cast_type(self, t:str, v: Any) -> IObject[Any]:
        print(t, v)
        if type(v) in CAST_POINTERS:
            return CAST_POINTERS[type(v)](v,t,self)
        if t in CAST_MAPPINGS:
            return CAST_MAPPINGS[t](v)
        raise TypeError(f"Cannot cast {v} to '{t}'")
    
    def inject_class(self, cls):
        print(f"Injecting class {cls.name} into {self.vm}")
        newcls = VMClass(cls.name)
        newcls.__name__ = cls.name # Cursed
        for attr in cls.attrs:
            newcls.__setattr__(attr.name, Pointer(attr.name, self.cast_type(attr.type.name, attr.value)))
        
        self.vm.CLASSES.append(newcls)
    
    def locate_classes(self):
        for cls in self.model.classes:
            self.inject_class(cls)