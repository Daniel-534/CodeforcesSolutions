t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ans = a.count(0)
    
    if a.count(-1) %2 != 0:
        ans +=2

    print(ans)
