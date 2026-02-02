t = int(input())
for _ in range(t):
    n = int(input())
    c1 = max(1, n-52)
    c2 = max(1, n-c1-26)
    c3 = n-c1-c2
    ans = chr(ord("a")+c1-1) + chr(ord("a")+c2-1) + chr(ord("a")+c3-1)
    print(ans)
