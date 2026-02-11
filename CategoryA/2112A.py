t = int(input())
for _ in range(t):
    a, x, y = map(int, input().split())
    if (a<x) == (a<y):
        print("YES")
    else:
        print("NO")
