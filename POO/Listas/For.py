lista=["manzana", "pera", "piña"]

for x in lista:
    print(x)

for i in range(len(lista)):
    print(lista[i])

[print(x) for x in lista]
#lista =["expresion" for "item" in "interaccion" if "condicion" valorfinal]
nuevaLista= [x for x in lista if "p" in x]
print(nuevaLista)

nuevaLista= [x for x in lista if x!="manzana"]
print(nuevaLista)

nuevaLista= [x for x in lista]
print(nuevaLista)

##Compresion con rangos
numeros= [i for i in range(10) if i%2==0]
print(numeros)

del numeros

numeros=[i for i in range(50) if i%2==0 if i%3==0]
print(numeros)

del numeros

numeros=[i for i in range(30) if i>=2 if i<=25 if i%8==0]


numeros.clear()
lista.clear()
lista=["mango" if i%3==0 else "orange" for i in range(10)]

print(lista)


## Metodo sort
## Normal
lista =["manzana", "banana", "pera"]
lista.sort()
print(lista)
#Ordenamiento inverso
lista =["manzana", "banana", "pera"]
lista.sort(reverse=True)
print(lista)