from .Num import Num
from .Point import Point
from .Var import Var
from .Action import Action, ActionList
from .Pointer import Pointer
from gcython.core.IObject import IObject

def convert_base_types(obj: object) -> IObject|None:
    if type(obj) in [int, float]:
        return Num(obj)

__all__ = [
    "Num",
    "Point",
    "Var",
    "Action",
    "ActionList",
    "Pointer",
    "convert_base_types",
]