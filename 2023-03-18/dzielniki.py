'''
Program: Dzielniki liczby
Autor: Jarosław Drzeżdżon
Data: 2023-03-18
'''

number = int(input("Podaj liczbe: "))

dividers = []

for i in range(1,number+1):
    if number % i == 0:
        dividers.append(i)

print(*dividers)
