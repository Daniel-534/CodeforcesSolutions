t = int(input())
for _ in range(t):
	n = str(input())
	digitos = []
	for d in n:
		digitos.append(int(d))
	print(sum(digitos))
