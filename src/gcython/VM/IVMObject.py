from abc import ABC, abstractmethod
from gcython.core import IObject

class IVMObject(ABC):
    @abstractmethod
    def __compose__(self) -> IObject:
        pass