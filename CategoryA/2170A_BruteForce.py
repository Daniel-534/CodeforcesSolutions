t = int(input())
for _ in range(t):
    n = int(input())
    maximo_costo = 0
    for fila in range(n):
        for columna in range(n):
            valor_celda = fila * n + columna + 1
            costo_actual = valor_celda
            if fila > 0:
                costo_actual += (fila - 1) * n + columna + 1
            if fila < n - 1:
                costo_actual += (fila + 1) * n + columna + 1
            if columna > 0:
                costo_actual += fila * n + (columna - 1) + 1
            if columna < n - 1:
                costo_actual += fila * n + (columna + 1) + 1
            if costo_actual > maximo_costo:
                maximo_costo = costo_actual
    print(maximo_costo)
