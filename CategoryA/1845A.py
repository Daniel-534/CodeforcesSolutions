t = int(input())

for _ in range(t):
	n, k, x = map(int, input().split())
	
	if x != 1:
		print("YES")
		print(n)
		l = [1]*n
		print(*l)
	else:
		if k ==1:
			print("NO")
		elif k==2:
			if n%2 == 0:
				print("YES")
				print(n//2)
				p = [2] * (n//2)
				print(*p)
			else:
				print("NO")
		else:
			if n%2 == 0:
				print("YES")
				print(n//2)
				q = [2] * (n//2)
				print(*q)
			else:
				print("YES")
				print(n//2)
				print("3 " + "2 " * ((n - 3) // 2))	
