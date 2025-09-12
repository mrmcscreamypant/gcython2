"""
A scripting language that compiles to Desmos.

Made with TextX.
"""

from textx import language, generator, metamodel_from_str
import importlib.resources

import gcscript

from .compiler import Compiler

@language('gcscript', '*.gc')
def gcscript_lang():
    """
    A scripting language that compiles to Desmos.
    """
    
    mm_str = importlib.resources.open_text(gcscript,"gcscript.tx")
    mm = metamodel_from_str(mm_str.read())
    return mm

@generator('gcscript', 'desmos')
def gcscript_latex_generator(metamodel, model, output_path, overwrite, debug, **custom_args):
    """
    Compile gcscript to latex.
    """
    
    Compiler(model)