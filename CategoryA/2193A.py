t = int(input())
for _ in range(t):
    n, s, x = map(int, input().split())
    a = list(map(int, input().split()))
    if sum(a)<= s:
        if (s-sum(a)) % x == 0:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
