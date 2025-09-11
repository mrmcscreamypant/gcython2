from .Var import VMVar
from gcython.core import IObject

class VM:
    GLOBAL_VARS: list[VMVar]

    def compose(self, minify=True, obfiscate=False):
        """Compile the VM to latex.
        
        Keyword arguments:
        minify -- compress the compiled code. (default True)
        obfiscate -- replace variable names with shorter names (default False)
        """
        result: list[IObject] = []

        for var in self.GLOBAL_VARS:
            result.append(var.__compose__())