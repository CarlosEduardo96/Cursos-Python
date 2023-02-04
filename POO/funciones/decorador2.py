#Parametros multiparametros
# def log(fichero_log):
#     def decorador_log(func):
#         def decorador_funcion(*args, **kwargs):
#             with open(fichero_log, 'a') as opened_file:
#                 output= func(*args, **kwargs)
#                 opened_file.write(f"{output}\n")
#         return decorador_funcion
#     return decorador_log

# @log('ficherosalida.log')
# def resta(a,b):
#     return a-b

# @log('ficherosalida.log')
# def suma(a,b):
#     return a+b

# @log('ficherosalida.log')
# def multiplicacion(a,b,c):
#     return a*b/c


# suma(10, 15)
# resta(10, 15)
# multiplicacion(10, 15,10)

## Decorador con parametros fijos
# def mi_decorador(arg):
#     def mi_decorador_real(funcion):
#         def nueva_funcion(a,b):
#             print(arg)
#             c=funcion(a,b)
#             print(arg)
#             return c
#         return nueva_funcion
#     return mi_decorador_real


# @mi_decorador("imprime esto antes y despues")
# def suma(a,b):
#     print("entra a la funcion suma")

# suma(5,6)

########## Autentificacion #########################
autenticado=True

def requiero_autorizacion(f):
    def funcion_decorador(*args, **kwargs):
        if not autenticado:
            print("Error: Usuario no identificado")
        else:
            return f(*args, **kwargs)
    return funcion_decorador

@requiero_autorizacion
def di_hola():
    print("Hola, deseo entrar")

@requiero_autorizacion
def suma(a,b):
    print(a+b)

di_hola()
suma(45,50)