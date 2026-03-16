t = int(input())

for _ in range(t):
    n, k, p, m = map(int, input().split())
    a = list(map(int, input().split()))
    
    costo_ganador = a[p-1]
    otros = a[:p-1] + a[p:]
    otros.sort()
    
    costo_ciclo = costo_ganador + sum(otros[:n-k])
    
    if p > k:
        prefijo = a[:p-1]
        prefijo.sort()
        costo_alcanzar = sum(prefijo[:p-k])
        
        if m < costo_alcanzar + costo_ganador:
            print(0)
        else:
            m -= (costo_alcanzar + costo_ganador)
            print(1 + m // costo_ciclo)
    else:
        if m < costo_ganador:
            print(0)
        else:
            m -= costo_ganador
            print(1 + m // costo_ciclo)
