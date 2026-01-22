t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(1,n):
        if len(a)>1:
            if a[0] <= a[i]:
                a.remove(a[0])
            else:
                a.remove(a[i])
    print(a)
