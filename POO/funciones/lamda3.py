mi_lista=[1,2,3,4,5]
filtrado=[]

for num in mi_lista:
    if num%2 !=0:
        filtrado.append(num)

print(filtrado)

filtrado2=[x for x in [1,2,3,4,5] if x%2 !=0]
print(filtrado2)


filtrado3= filter( lambda x: x%2 !=0, mi_lista)

print(filtrado3)
x=list(filtrado3)
print(x)

