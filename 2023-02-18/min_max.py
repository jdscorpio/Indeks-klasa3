import random as rnd

lista = []
n = 10
for i in range(n):
    lista.append(rnd.randint(-100,100))

print(lista)
minn = lista[0]
maks = lista[0]

for i in range(1,n):
    if minn > lista[i]: minn = lista[i]
    if maks < lista[i]: maks = lista[i]

print(minn,maks)