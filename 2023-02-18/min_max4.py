import random as rnd
import statistics as stats

n = 10
lista = [rnd.randint(-100,100) for _ in range(n)]
print(lista)

print(min(lista),max(lista))
print(sum(lista))
print(stats.mean(lista))    # średnia arytmetyczna

