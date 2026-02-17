import math
t = int(input())
for _ in range(t):
    n, k, p = map(int, input().split())
    if -n*p<=k and k<=n*p:
        ans = (abs(k)+p-1)//p
        print(ans)
    else:
        print(-1)
