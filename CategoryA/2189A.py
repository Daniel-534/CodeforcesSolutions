t = int(input())

for _ in range(t):
    n, h, l = map(int, input().split())
    a = list(map(int, input().split()))

    Count_h = 0
    Count_l = 0 
    Count_sirve = 0
    
    for x in a:
        sirve_h = (x <= h)
        sirve_l = (x <= l)
        
        if sirve_h:
            Count_h += 1
        if sirve_l:
            Count_l += 1
        if sirve_h or sirve_l:
            Count_sirve += 1

    ans = min(Count_h, Count_l, Count_sirve // 2)
    print(ans)
