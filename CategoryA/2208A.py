from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    A = []

    for _ in range(n):
        A.append(list(map(int, input().split())))

    MatrizPlana = [num for fila in A for num in fila]
    freq = Counter(MatrizPlana)
    Condicion = True
    if max(freq.values()) > n * (n - 1):
        Condicion = False
    print("YES" if Condicion else "NO")
