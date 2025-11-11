q = int(input())

for _ in range(q):
	n = int(input())
	s, t = map(str, input().split())
	
	condicion = True

	for i in set(s):
		if s.count(i) == t.count(i):
			condicion = True
		else:
			condicion = False
			break
	
	if condicion:
		print("YES")
	else:
		print("NO")
