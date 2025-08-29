"""
A scripting language that compiles to Desmos.

Made with TextX.
"""

from textx import language, generator, metamodel_from_file
import importlib.resources

import gcython

@language('gcscript', '*.gc')
def gcscript_lang():
    """
    A scripting language that compiles to Desmos.
    """
    
    filepath = importlib.resources.path(gcython,"gcscript.tx")
    print(filepath)
    mm = metamodel_from_file(filepath)
    return mm

@generator('gcscript', 'desmos')
def gcscript_latex_generator(metamodel, model, output_path, overwrite, debug, **custom_args):
    """
    Compile gcscript to latex.
    """
    
    print(metamodel)