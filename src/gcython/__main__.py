"""gcython demo"""
print(__doc__)

from gcython.objects import Num

print(Num(1).__latex__(), Num(0.2))