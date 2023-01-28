## Las tuplas ya no son modificables
##No soportados
#insert()
#pop()
#append()
#
##tupla= ("manzana", "pera", "platano")
tupla=tuple(("manzana", "pera", "platano"))

if "manzana" in tupla:
    print("existe en la tupla")

x=("manzana", "pera", "platano")
y=list(x)

y[1]="naranja"
x = tuple(y)

print(x)
nuevaTupla=("coco",)
tupla+=nuevaTupla
print(tupla)
