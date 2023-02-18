lista = []
with open('dane2.txt','r') as wejscie:
    for el in wejscie:
        lista.append(el.strip())

lista = list(map(int,lista))
print(lista)    
print(min(lista),max(lista))