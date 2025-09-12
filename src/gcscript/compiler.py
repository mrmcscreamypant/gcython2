from gcython.VM import VM
from gcython.expressions import ActionList

class GCScriptVM(VM):
    @property
    def TICKER(self):
        return ActionList()

class Compiler:
    vm: VM

    def __init__(self, model):
        print("Starting compile...")
        self.model = model
        self.vm = GCScriptVM()
        self.locate_classes()
    
    def inject_class(self, cls):
        print(f"Injecting class {cls.name} into {self.vm}")
    
    def locate_classes(self):
        for cls in self.model.classes:
            self.inject_class(cls)