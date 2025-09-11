from gcython.core.IObject import IObject, IProps
from dataclasses import dataclass
from strongtyping.strong_typing import match_class_typing
from .Pointer import Pointer

@match_class_typing
@dataclass
class ActionProps(IProps):
    target: Pointer
    value: IObject

class Action(IObject[ActionProps]):
    PropsClass = ActionProps

    @property
    def target(self) -> Pointer:
        return self.props.target
    
    @property
    def value(self) -> IObject:
        return self.props.value

    def __latex__(self) -> str:
        return self.target.name+"\\to"+self.value.__latex__()

#@match_class_typing
@dataclass
class ActionListProps(IProps):
    children: tuple[IObject, ...]
    def __init__(self,*children: Action):
        self.children = children

class ActionList(IObject[ActionListProps]):
    PropsClass = ActionListProps

    @property
    def children(self):
        return self.props.children

    def __latex__(self) -> str:
        return "\\left("+",".join(
            [child.__latex__() for child in self.children]
        )+"\\right)"