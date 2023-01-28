#Set Datos
thisset ={"manzana", "platano", "gresa"}

print(type(thisset))
thisset= {"manzana","platano", "pera"}

print(thisset)

thisset= set({"manzana","platano", "pera"})

#no permitido
#print(thisset{1})
#Permitido con in

#primera Forma
for x in thisset:
    print(x)


thisset={"manzana","platano", "pera"}
print("manzana" in thisset)

#Agegar Nuevos Elementos
thisset.add("piña")
print(thisset)

thisset={"manzana","platano", "pera"}
frutas={"peña","papaya"}

thisset.update(frutas)

print(thisset)

##Convertir set de datos en una lista
estalista=["kiwi","naranja"]

thisset.update(estalista)


##remove elimina elementos de una lista
thisset={"manzana","platano", "pera"}
thisset.remove("pera") ## si no encuentra el elemento manda una excepcion

##funcion discard
thisset.discard("platano") ## si no enco¿entra nada no envia una excepcion

##pop funcionamiento
## si la lista tiene inice este elimina el ultimo
## Pero en este caso como no se trabaja con indices elimina de forma aleatoria
thisset={"manzana","platano", "pera"}
x=thisset.pop()
print(x)

#clear -- limpiar datos de un set de datos, y arreglos
thisset={"manzana","platano", "pera"}
del thisset
print(thisset) ## manda error por que el set de datpos ya no existe

##Conjunto de datos

set1={"a","b", "c"}
set2={1,2,3}

##Union ocupa una ariable para almacenar los elementos
set3= set1.union(set2)
print(set3)

## Ocupa alguna de las dos variables para que contenga la nueva lista
set1.update(set2)
print(set1)

x={"manzana","platano", "pera"}
y={"google", "udemy"}

## permite actualizar la variable
x.intersection_update(y)
print(x)


x={"manzana","platano", "pera"}
y={"google", "udemy"}

##Intercepta los elementos que se repiten
z=x.intersection(y)
print(z)

##Agregar elementos que son diferentes
x={"manzana","platano", "pera"}
y={"google", "udemy", ",mamzana"}

x.symmetric_difference_update(y)
print(x)

x={"manzana","platano", "pera"}
y={"google", "udemy", ",mamzana"}

z=x.symmetric_difference(y)
print(z)