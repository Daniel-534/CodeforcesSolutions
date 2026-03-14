t = int(input())
for _ in range(t):
    n = int(input())
    d = []
    for i in range(n):
        a, b, c = map(int, input().split())
        d.append((a, b, c, i))
    
    d.sort(key=lambda x: (-x[0], x[1], -x[2]))
    
    a = [0] * n
    b = [0] * n
    c = [0] * n
    p = [0] * n
    
    for i in range(n):
        a[i] = d[i][0]
        b[i] = d[i][1]
        c[i] = d[i][2]
        p[i] = d[i][3]
    
    x = [1] * n
    y = [1] * n
    
    g = 0
    for j in range(n):
        if j == 0 or a[j] != a[j - 1] or b[j] != b[j - 1]:
            g = 0
        v = g + 1
        aj = a[j]
        bj = b[j]
        cj = c[j]
        for i in range(j):
            if a[i] == aj:
                continue
            A = a[i] - aj
            B = b[i] - bj
            C = c[i] - cj
            if B * B < 4 * A * C:
                u = x[i] + 1
                if u > v:
                    v = u
        x[j] = v
        if v > g:
            g = v
    
    g = 0
    for i in range(n - 1, -1, -1):
        if i == n - 1 or a[i] != a[i + 1] or b[i] != b[i + 1]:
            g = 0
        v = g + 1
        ai = a[i]
        bi = b[i]
        ci = c[i]
        for j in range(i + 1, n):
            if a[j] == ai:
                continue
            A = ai - a[j]
            B = bi - b[j]
            C = ci - c[j]
            if B * B < 4 * A * C:
                u = y[j] + 1
                if u > v:
                    v = u
        y[i] = v
        if v > g:
            g = v
    
    ans = [0] * n
    for i in range(n):
        ans[p[i]] = x[i] + y[i] - 1
    
    print(*ans)
