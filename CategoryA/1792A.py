# Daniel.Soto - CosmologyAndGravitation_GravitationalWaves_LVK
# Contact: daniel.soto1@udea.edu.co

t = int(input())

for _ in range(t):
	n = int(input())	
	h = list(map(int, input().split()))
	
	contador = 0

	for i in h:
		if i==1:
			contador +=1

	print(n - contador//2)
