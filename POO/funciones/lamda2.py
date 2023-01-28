#lamda
#lamda argumentos : expresion
x = lambda a:a +10
print (x(5))

x = lambda a,b:a*b
print(x(10,5))

def myFuncion(n): 
    return lambda a: a*n

resultado=myFuncion(2)
print(resultado(5))


duplicador=myFuncion(2)
triplicador=myFuncion(3)

print(duplicador(11))
print(triplicador(11))