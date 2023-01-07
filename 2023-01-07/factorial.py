'''
Program liczby silnię z danej liczby
'''

n = int(input())


product = 1
if n == 0:
    product = 1
else:
    for i in range(1, n+1):
        product *= i

print(product)
