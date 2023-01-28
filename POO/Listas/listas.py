# theslist=["Base", "Caso", "Barra"]
# print(theslist)

# #Longitud de lista
# print(len(theslist))

# #Contenido homogeneo

# lalista=[1,2,3]
# laotralista=["queso","papa","tipo"]
# verlista=[True,False,False]

# #Contenido Heterogeneo

# helista=[True, "papa", 2]

# print(type(helista))

# #contructor

# thislist = list(("manzana", "piña", "mango"))

# print(thislist)

# #Listas es una colección ordenada y mutable. Permite duplicar miembros.
# laotralista=["queso","papa","tipo"]
# print(laotralista[-1])

# otherlist=["Numero", "Pieza", "Formato", "Fecha", "Modelo", "Tipo", "Zona"]
# print(otherlist[2:5])
# print(otherlist[:4])
# print(otherlist[2:])

# # in listas- rngos

# otherlist=["Numero", "Pieza", "Formato", "Fecha", "Modelo", "Tipo", "Zona"]
# if "Pieza" in otherlist:
#     print("Tengo una pieza")

# lost=["Numero", "Pieza", "Formato", "Fecha", "Modelo", "Tipo", "Zona"]
# print(lost)
# lost[1] = "queso"
# print(lost)

# lost=["Numero", "Pieza", "Formato", "Fecha", "Modelo", "Tipo", "Zona"]
# print(lost)
# lost[1:3] = ["queso1", "queso2", "queso3"]
# print(lost)

# lust=["apple","banana","Cherry", "orange", "kiwi"]
# lust[1:4] = ["melon"]
# print(lust)

lista=["banana", "manzana","platano"]

##Inserta en una posicion especifica
lista.insert(1,"uva")
print(lista)

## Inserta al final de la lista
lista.append("pera")
print(lista)
##Extender lista
listaTropical=["piña", "mango"]
lista.extend(listaTropical)
print(lista)

##Tuplas
tupla=("kiwi", "naranja")
lista.extend(tupla)
print("Tupla")
print(lista)

##Operador SobreCargado
lista=["manzana","platano", "fresa"]
listaTropical=["mango", *lista,"piña"]


