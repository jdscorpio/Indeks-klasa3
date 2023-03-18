'''
Program: Dzielniki
Autor: Jarosław Drzeżdżon
Data: 2023-03-18
'''

number = int(input("Podaj liczbe: "))

dividors = set()

sqrt = int(number**(1/2))
for i in range(1,sqrt+1):
    if number % i == 0:
        dividors.add(i)
        dividors.add(number//i)
print(sorted(dividors))


    
