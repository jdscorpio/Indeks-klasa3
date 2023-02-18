import random as rnd

n = 10
lista = [rnd.randint(-100,100) for _ in range(n)]
print(lista)

wyjscie = open('dane.txt','w')
for el in lista:
    wyjscie.write(str(el) + '\n')

wyjscie.close()