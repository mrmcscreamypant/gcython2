"""
A scripting language that compiles to Desmos.

Made with TextX.
"""

from textx import language, generator, metamodel_from_str
import importlib.resources

import gcscript
from gcscript.ClassMethod import ClassMethod
from gcscript.MethodCall import MethodCall
from gcython.expressions import Pointer

from .compiler import Compiler

from dataclasses import dataclass
from typing import Any
from rich.console import Console

@dataclass
class Type:
    parent: Any
    name: str

@language('gcscript', '*.gc')
def gcscript_lang():
    """
    A scripting language that compiles to Desmos.
    """
    
    mm_str = importlib.resources.open_text(gcscript,"gcscript.tx")
    mm = metamodel_from_str(
        mm_str.read(),
        classes=[
            Type,
            MethodCall,
            ClassMethod
        ],
        builtins={
            "Number": Type(None, "Number"),
            "String": Type(None, "String"),
        }
    )
    return mm

@generator('gcscript', 'desmos')
def gcscript_latex_generator(metamodel, model, output_path, overwrite, debug, **custom_args):
    """
    Compile gcscript to latex.
    """
    
    try:
        Compiler(model)
    except Exception:
        Console().print_exception(show_locals=True)