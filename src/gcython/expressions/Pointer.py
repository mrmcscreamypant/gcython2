from gcython.core.IObject import IObject, IProps
from dataclasses import dataclass
from gcython.expressions import Num
from strongtyping.strong_typing import match_class_typing

@match_class_typing
@dataclass
class PointerProps(IProps):
    name: str
    inital: IObject|Num = Num(0)

@dataclass
class Pointer(IObject[PointerProps]):
    PropsClass = PointerProps
    _instances = []

    def __init__(self, *children):
        IObject.__init__(self,*children)
        self.__name__ = self.name
        if not self in self._instances:
            self._instances.append(self)
        else:
            self = self._instances[self._instances.index(self)]
        
    @property
    def name(self) -> str:
        name = self.props.name
        if len(name) > 1:
            name = name[0]+"_{"+name[1:]+"}"
        return name

    @property
    def inital(self) -> IObject|Num:
        return self.props.inital

    def __latex__(self) -> str:
        return str(self.name)