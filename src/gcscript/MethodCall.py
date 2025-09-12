from dataclasses import dataclass
from typing import Any


@dataclass
class MethodCall:
    parent: Any
    ref: Any
    args: list[Any]