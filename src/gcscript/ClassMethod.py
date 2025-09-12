from dataclasses import dataclass
from typing import Any
from gcython.VM import VM

@dataclass
class ClassMethod:
    parent: Any
    scope: str
    static: bool
    return_type: Any
    name: str
    attrs: list[Any]

    def full_name(self, vm: VM):
        return f"{vm.__class__.__name__}C{self.parent.name}M{self.name}"