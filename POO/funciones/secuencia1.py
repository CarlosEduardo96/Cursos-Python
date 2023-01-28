#Secuencia recursiva
from collections.abc import Sequence

print(type(Sequence))

def sumaRecursiva(seq: Sequence[int])-> int:
    if len(seq)==0:
        return 0
    return seq[0]+sumaRecursiva(seq[1:])

print(sumaRecursiva([7,11]))

print(sumaRecursiva([7,11,13]))
