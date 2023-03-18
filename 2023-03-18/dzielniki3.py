'''
Program: Różne dzielniki pierwsze 
Autor: Jarosław Drzeżdżon
Data: 2023-03-18
'''

number = int(input("Podaj liczbe: "))

dividors = set()       # nieuporządkowany zbiór niepowtarzających się elementów
dividor = 2
while number > 1:
    if number % dividor == 0:
        dividors.add(dividor)
        number //= dividor
    else:
        dividor += 1

print(dividors)
print(len(dividors))
print(*(list(dividors)))