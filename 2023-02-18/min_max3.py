import random as rnd

n = 10
lista = [rnd.randint(-100,100) for _ in range(n)]
print(lista)

def min_max(tab):
    minn = tab[0]
    maks = tab[0]
    for i in range(1,len(tab)):
        if minn > tab[i]: minn = tab[i]
        if maks < tab[i]: maks = tab[i]
    
    return minn, maks

print(min_max(lista))

a = min_max(lista)
print(a)
print(a[0],a[1])
b = list(a)
print(b)
x,y = min_max(lista)
print(x,y)