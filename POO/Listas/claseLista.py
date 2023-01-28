#abs Retorna el valor absoluto o magnitud de un numero
def mifuncion(n):
    return abs(n-50)

lista= [100,50,65,82,23]
lista.sort(key=mifuncion)
print(lista)

listaFrutas=["manzana", "Pera", "pepino","uva"]
listaFrutas.sort(key=str.lower)
print(listaFrutas)

listaFrutas.reverse()
print(listaFrutas)

## Con referencias
nuevalista=listaFrutas

##Copia una lista sin mutar las referencias
del nuevalista
listaFrutas=["manzana", "Pera", "pepino","uva"]
nuevalista=listaFrutas.copy()
nuevalista= list(listaFrutas)
print(nuevalista)