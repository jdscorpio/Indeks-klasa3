'''
Program sumuje n liczb od 1 do n
1+2+3+...+n

Specyfikacja
wejście:
n - liczba naturalna > 0
'''

n = input('Podaj n: ')
n = int(n)

sum_n = 0
for i in range(n+1):
    sum_n += i

print(sum_n)
