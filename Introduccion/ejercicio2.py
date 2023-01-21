#Ciclo While con else
i=1

while(i<6):
    i+=1
    if(i== 3):
        continue
    print(i)

while i<6:
    print(i)
    i+=1
else: 
    print("i no es menor que 6")