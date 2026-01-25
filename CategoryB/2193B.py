t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    
    if n == 1:
        print(p[0])
        continue
    
    if p == list(range(n, 0, -1)):
        print(*p)
        continue
    
    i = 0
    
    while (i<n) and (p[i] == n-i):
        i += 1
    
    aux = n-i
    pos = p.index(aux)
    
    p[i:pos+1] = p[i:pos+1][::-1]
    
    print(*p)
