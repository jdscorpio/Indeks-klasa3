import random as rnd

n = 10
lista = [rnd.randint(-100,100) for _ in range(n)]
print(lista)

lista2 = []
for el in lista:
    lista2.append(str(el)+'\n')
print(lista2)

with open('dane2.txt','w') as wyjscie:
    wyjscie.writelines(lista2)
   
