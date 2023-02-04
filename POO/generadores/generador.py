def funcion():
    return 5

def generador():
    yield 20

def generador_2():
    if True:
        return 10
    else:
        yield 20

def generador_multiple():
    n=1
    yield n

    n+=1
    yield n
    
    n+=1
    yield n

print(funcion())
a=generador()
print(next(a))

b= generador_multiple()
print(next(b))
print(next(b))
print(next(b))

lista= [2,4,6,8,10]
##Array
# al_cuadrado=[x**2 for x in lista]

##Convertir una lista a generador
al_cuadrado=(x**2 for x in lista)
print(al_cuadrado)

for i in al_cuadrado:
    print(i)