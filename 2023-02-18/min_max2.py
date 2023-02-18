import random as rnd

n = 10
lista = [rnd.randint(-100,100) for _ in range(n)]
print(lista)

def funkcja(a:int,b:str,c:list)->int: 
    return None


def moje_min(tab):
    minn = tab[0]
    for i in range(1,len(tab)):
        if minn > tab[i]: minn = tab[i]
    return minn

def moje_max(tab):
    maks = tab[0]
    for i in range(1,len(tab)):
        if maks < tab[i]: maks = tab[i]
    return maks

print(moje_min(lista), moje_max(lista))

