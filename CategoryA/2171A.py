t = int(input())
for _ in range(t):
    n = int(input())
    if n%2 == 0:
        ans = (n+4)//4
    else:
        ans = 0
    print(ans)
