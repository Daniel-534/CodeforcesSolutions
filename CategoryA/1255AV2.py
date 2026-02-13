# Solucion haciendo analisis desde teoria de numeros

"""
Sean $a, \,b,\, c,\, p,\, q,\, r \in \mathbb{Z}^+$ 
con $c=|a-b|$ y $c=5\cdot p + 2\cdot q + r$

Halle $x = \min{\{p+q+r\}}$

Solución:

$$x = \lfloor \frac{c}{5}\rfloor + \lceil\frac{c\mod 5}{2}\rceil$$
"""

import math
T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    c = abs(a-b)
    ans = math.floor(c/5) + math.ceil((c%5)/2)
    print(ans)
