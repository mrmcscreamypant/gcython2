from .Num import Num
from gcython.core.IObject import IObject

def convert_base_types(obj: object) -> IObject|None:
    if type(obj) in [int, float]:
        return Num(obj)

__all__ = [
    "Num",
    "convert_base_types"
]