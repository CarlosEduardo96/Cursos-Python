from collections.abc import Sequence, Callable
print(type(Sequence))
print(type(Callable))
#*args **kwargs
def sumaRecursiva(seq: Sequence[int])-> int:
    if len(seq)==0:
        return 0
    return seq[0]+sumaRecursiva(seq[1:])


def util(
    limit: int, 
    filtro: Callable[[int],bool],
    v:int
)-> list[int]:
    if v==limit:
        return []
    
    elif filtro(v):
        return [v]+util(limit, filtro, v+1)

    else:
        return util(limit, filtro, v+1)

def multiplos_2_3(x: int)->int:
    return x%3 ==0 or x%2 ==0

def sumafuncional(limit: int=10)-> int:
    return sumaRecursiva(util(limit, multiplos_2_3, 0))

print(sumafuncional())