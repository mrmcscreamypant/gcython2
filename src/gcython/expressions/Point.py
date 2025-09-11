from gcython.core.IObject import IObject, IProps
from dataclasses import dataclass
from strongtyping.strong_typing import match_class_typing
from typing import Optional
from . import Num

@match_class_typing
@dataclass
class Props(IProps):
    x: Num
    y: Num
    z: Num|None = None

class PointDimensionError(Exception):
    pass

class Point(IObject[Props]):
    PropsClass = Props

    @property
    def x(self) -> Num:
        return self.props.x
    
    @property
    def y(self) -> Num:
        return self.props.y

    @property
    def z(self) -> Num:
        if not self.props.z:
            raise PointDimensionError("foo")
        return self.props.z

    @property
    def tuple(self) -> tuple[Num,...]:
        try:
            return (self.x,self.y,self.z)
        except PointDimensionError:
            return (self.x,self.y)

    def __latex__(self) -> str:
        return "("+",".join([value.__latex__() for value in self.tuple])