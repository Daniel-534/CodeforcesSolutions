t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    MaxValueIndex = a.index(max(a))

    a[0], a[MaxValueIndex] = a[MaxValueIndex], a[0]

    Count = 0

    for i in range(n):
        MaxValue = max(a[:i+1])
        Count += MaxValue

    print(Count)
