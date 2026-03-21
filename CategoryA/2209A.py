t = int(input())
for _ in range(t):
    n, c, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    a.sort()
    
    for i in range(n):
        if a[i] <= c:
            max_flips = c - a[i]
            flips_usados = min(k, max_flips)
            
            c += a[i] + flips_usados
            k -= flips_usados
        else:
            break
    
    print(c)
