## funciones en python palabra reservada def
##Argumentos fijos
def mi_funcion1():
    print("Hola mundo")

def mi_funcion2(mensaje):
    print("Hola",mensaje)

def funcion3(niño1,niño2,niño3):
     print("El nombre del niño/a es: ", niño3)

def funcion4(ciudad="mexico"):
    print("yo soy de "+ ciudad)

def funcion5():
    pass

def suma_numero1(n1, n2):
    return n1+n2

def suma_numerica(limit: int =10)-> int:
    s=0
    for n in range(1, limit):
        if n%3 ==0 or n%5==0:
            s+=n
    return s
##Argumentos no definidos
def funcionMultiparametros(*param):
    print("El nombre del niño/a es: ", param[2])

#*args **kwargs
def suma_numero2(*numeros):
    total=0
    for n in numeros:
        total=total+n

    return total
##Argumento definido por clave
def funcionporClave(**niño):
    print("El nombre del niño/a es: "+ niño["apellido"])
##################################################



mi_funcion1()
mi_funcion2("Carlos Eduardo")
funcionMultiparametros("Angel", "Carlos", "Nedy")
funcion3("Angel", "Carlos", "Nedy")
funcionporClave(nombre="luis", apellido="perez")
print(suma_numero1(4,8))
print(suma_numero2(4,8,3,4,5))
##Valores por defecto
funcion4()
funcion4("USA")
funcion5()
print(suma_numerica(100))












