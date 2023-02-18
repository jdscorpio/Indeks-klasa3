wejscie = open('dane2.txt','r')
wiersze = wejscie.readlines()

lista = []
for el in wiersze:
    x = el.strip()
    x = int(x)
    lista.append(x)

print(lista)
print(min(lista), max(lista))
lista = sorted(lista)
print(lista[0], lista[len(lista)-1])