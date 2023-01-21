#Ejecutar el mayor de 3 numeros
import random
a= random.randrange(1,10)
b= random.randrange(1,10)
c= random.randrange(1,10)


print("A:",a,"B:",b,"C:",c)
if(a>b and a>c):
    print("A es mayor a B y C")

elif(b>a and b>c):
    print("B es mayor a A y C")

elif(c>a or c>b):
    print("C es mayor a B y C")

