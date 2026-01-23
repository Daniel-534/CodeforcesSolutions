t = int(input())

for _ in range(t):
    n, h, l = map(int, input().split())
    a = list(map(int, input().split()))

    CountMin = 0
    CountMax = 0

    aux = []
    for i in range(n):
        if (a[i] <= h) or (a[i] <= l):
            aux.append(a[i])

    for i in range(len(aux)):
        if a[i]<= min(h, l):
            CountMin += 1
        else:
            CountMax += 1

    ans = min(CountMin, CountMax)

    print(ans)
