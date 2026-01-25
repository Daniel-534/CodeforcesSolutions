t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(str, input().split()))

    New = ""

    for i in range(n):
        New = min(New+a[i], a[i]+New)

    print(New)
