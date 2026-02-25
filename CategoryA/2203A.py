t = int(input())
for _ in range(t):
    n, m, d = map(int, input().split())
    tower = 1 + (d//m)
    if n < tower:
        print(1)
    elif n % tower == 0: 
        ans = n//tower
        print(ans)
    else:
        ans = 1 + (n//tower)
        print(ans)
