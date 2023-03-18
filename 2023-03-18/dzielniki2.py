'''
Program: Dzielniki pierwsze
Autor: Jarosław Drzeżdżon
Data: 2023-03-18
'''

number = int(input("Podaj liczbe: "))

dividor = 2
dividors = []
while number > 1:
    if number % dividor == 0:
        dividors.append(dividor)
        number //= dividor
    else:
        dividor += 1

print(dividors)

    
