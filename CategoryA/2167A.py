t = int(input())

for _ in range(t):
	l = map(int, input().split())
	if len(set(l)) == 1:
		print("YES")
	else:
		print("NO")
