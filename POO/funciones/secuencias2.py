from collections.abc import Sequence, Callable
print(type(Sequence))
print(type(Callable))

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

def multiplicacion(x: int)-> bool:
    return x%3==0 or x%5==0

def multiplos_2_3(x: int)->int:
    return x%3 ==0 or x%2 ==0

print(util(10, multiplicacion, 0))
print(util(10, multiplos_2_3, 0))