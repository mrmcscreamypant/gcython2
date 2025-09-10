from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class IProps(ABC):
    pass

class IObject(ABC):
    props: IProps

    def __init__(self, *children) -> None:
        self.props = self.Props(*children)

    @property
    @abstractmethod
    def Props(self) -> type[IProps]:
        @dataclass
        class _Props(IProps):
            pass

        return _Props

    def __repr__(self) -> str:
        return repr(self.props)