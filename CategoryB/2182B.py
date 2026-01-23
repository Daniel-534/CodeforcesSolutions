t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    count_a = 0
    k = 0
    while a>=0:
        a = a - 2*k*a
        if a >= 0:
            count_a += 1
        else:
            continue
        k += 1

    count_b = 0
    i = 0
    while b>=0:
        b = b - (2*i+1)
        if b >= 0:
            count_b += 1
        else:
            continue
        i += i

    ans = min(count_a,count_b)

    print(ans)
