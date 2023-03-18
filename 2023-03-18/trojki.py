n = 1000

ile = 0
for i in range(1, n + 1):
	for j in range(i, n + 1):
		for k in range(j, n + 1):
			if i**2 + j**2 == k**2:
				ile += 1
print(ile)
