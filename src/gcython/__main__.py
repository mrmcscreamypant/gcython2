"""gcython demo"""
print(__doc__)

from gcython.expressions import Num
from gcython.expressions.operations import Sqrt
from pylatexenc.latex2text import latex2text
from rich.markdown import Markdown

latex = "\\begin{math}"+Sqrt(Num(0.2)).__latex__()+"\\end{math}"
markdown = latex2text(latex)
print(markdown)