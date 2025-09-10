"""gcython demo"""
print(__doc__)

from gcython.expressions import Num
from gcython.expressions.operations import Sqrt
from latex2markdown import LaTeX2Markdown

print(LaTeX2Markdown(Num(1).__latex__()).to_markdown(), Num(0.2))