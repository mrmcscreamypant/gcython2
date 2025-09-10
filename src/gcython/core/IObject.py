from dataclasses import dataclass
from abc import ABC, abstractmethod
from strongtyping.strong_typing_utils import TypeMisMatch
from typing import TypeVar, Generic
import sys

P = TypeVar("P")

@dataclass
class IProps(ABC):
    """Please extend with @strongtyping.strong_typing.match_class_typing"""
    pass

class IObject(ABC, Generic[P]):
    PropsClass: type[P]
    props: P

    def __init__(self, *children) -> None:
        try:
            self.props = self.PropsClass(*children)
        except TypeMisMatch as e:
            sys.exit(1)

    def __repr__(self) -> str:
        return repr(self.props)

    @abstractmethod
    def __latex__(self) -> str:
        """Return a latex string representing an object"""
        pass