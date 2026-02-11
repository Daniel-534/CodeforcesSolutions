import math

t = int(input())
for _ in range(t):
    n, w = map(int, input().split())
    ans = n - n//w
    print(ans)
