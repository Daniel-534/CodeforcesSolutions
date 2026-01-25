t = int(input())
for _ in range(t):
    s = list(map(str, input().split()))
    ans = ""
    for i in s:
        ans+=i[0]
    print(ans)
