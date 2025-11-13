t = int(input())

for _ in range(t):
	n, k = map(int, input().split())
	a = [0] + list(map(int, input().split()))

	ans = 0
	count = 0
	
	for i in range(1, n+1):
		if a[i] == 1:
			ans += (count + 1)//(k + 1)
			count = 0
			continue
		else:
			count += 1
	ans += (count+1)//(k+1)
	print(ans)	
