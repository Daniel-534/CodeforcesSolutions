#Nuevo estilo de Output

import math

t = int(input())

results = []

for _ in range(t):
    a, b, k = map(int, input().split())
    g = math.gcd(a, b)
    dx = a // g
    dy = b // g
    if dx <= k and dy <= k:
        results.append("1")
    else:
        results.append("2")

print("\n".join(results))
