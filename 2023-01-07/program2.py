'''
Sumowanie cyfr danej liczby
Autor: Jarosław Drzeżdżon
Data: 2023-01-07
'''

number = input('Podaj liczbę naturalną: ')

sum_digits = 0
for ch in number:
    sum_digits += int(ch)

print(sum_digits)

sum_digits = 0
for i in range(len(number)):
    sum_digits += int(number[i])

print(sum_digits)
