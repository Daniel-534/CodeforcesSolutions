t = int(input())

lista = []

for _ in range(t):
	n = int(input())
	a = list(map(int, input().split()))
	a = sorted(a)[::-1]
	lista.append(a)

for i in range(t):
	max1 = lista[i][0]
	max2 = lista[i][1]
	print(max1+max2)		

