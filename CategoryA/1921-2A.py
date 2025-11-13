# Segunda version mas optimizada

t = int(input())

for _ in range(t):
	xy = []
	for _ in range(4):
		coordenada = list(map(int, input().split()))	
		xy.append(coordenada)
	
	if xy[0][0] != xy[1][0]:
		aux = abs(xy[0][0]-xy[1][0])
		print(aux**2)
	else:
		aux = abs(xy[0][1]-xy[1][1])
		print(aux**2)
