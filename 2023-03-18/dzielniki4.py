'''
Program: Liczba dzielników pierwszych
Autor: Jarosław Drzeżdżon
Data: 2023-03-18
'''

number = int(input("Podaj liczbe: "))

dividors = {}
dividor = 2
while number > 1:
    if number % dividor == 0:
        if dividor in dividors:
            dividors[dividor] += 1
        else:
            dividors[dividor] = 1

        number //= dividor
    else:
        dividor += 1

print(dividors)

for el in dividors:
    print(el,dividors[el])

