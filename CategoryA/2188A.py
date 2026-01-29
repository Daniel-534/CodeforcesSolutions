t = int(input())
for _ in range(t):
    n = int(input())
    p = [0] * n
    low, high = 1, n
    for i in range(n-1, -1, -1):
        if (n-1 - i) % 2 == 0:
            p[i] = low
            low += 1
        else:
            p[i] = high
            high -= 1
    print(*p)
