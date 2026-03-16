t = int(input())
for _ in range(t):
    n = int(input())
    c = []
    for _ in range(n):
        c.append(list(map(int, input().split())))
    
    max_points = 0.0
    
    for i in range(n - 1, -1, -1):
        val = c[i][0]
        diff = c[i][1]
        puntos_si_tomo = val + max_points * (1 - diff / 100.0)
        if puntos_si_tomo > max_points:
            max_points = puntos_si_tomo
            
    print(f"{max_points:.10f}")
