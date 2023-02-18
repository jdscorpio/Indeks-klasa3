wejscie = open('dane2.txt','r')

lista = []

for el in wejscie:
    lista.append(el.strip())

wejscie.close()
lista = list(map(int,lista))

print(min(lista),max(lista))





