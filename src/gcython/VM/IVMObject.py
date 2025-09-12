from abc import ABC, abstractmethod
from gcython.core import IObject
from typing import Any

class IVMObject(ABC):
    @abstractmethod
    def __compose__(self) -> list[IObject[Any]]:
        pass