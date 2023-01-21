#global declarar variables globales
x="Hola"
def mifuncion():
    global y
    y="Hola"
    print("x: "+x)

mifuncion()
print(y)