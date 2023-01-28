#Tipos de programacion en python
#peocedural
#funcional
#phytonic
def decorador(funcion):
    def nueva_funcion(a,c):
        print("Se va a llamar")
        c= funcion(a,c)
        print("Se ha llamado")
        return c

    return nueva_funcion

def decorador2(funcion2):
    def SumaRecursiva(*n):        
        resultado= funcion2(*n)
        return resultado
    return SumaRecursiva

@decorador
def suma(a, b):
    print("entra a la funcion suma")
    return a+b

@decorador
def resta(a,b):
    print("resta")
    return a-b

@decorador2
def SumaR(*n):
    total=0
    for x in n:
        total+=x
    return total


#Parametrso definidos
print("Parametraos Definidos")
print(suma(5,6))
print(resta(5,6))

#Parametros indefinidos
print("Metodos Recursivos")
print(SumaR(1,5,4,8))


