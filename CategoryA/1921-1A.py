# Version inicial

t = int(input())

for _ in range(t):
	xy1 = list(map(int, input().split()))
	xy2 = list(map(int, input().split()))
	xy3 = list(map(int, input().split()))
	xy4 = list(map(int, input().split()))
	
	if xy1[0] != xy2[0]:
		aux = abs(xy1[0]-xy2[0])
		print(aux**2)
	else:
		aux = abs(xy1[1]-xy2[1])
		print(aux**2)


