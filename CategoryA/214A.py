import math

# Leer entrada
n, m = map(int, input().split())

count = 0

# Iterar a desde 0 hasta sqrt(n)
# Usamos int(math.sqrt(n)) + 1 para asegurar el rango correcto
for a in range(int(math.sqrt(n)) + 1):
    # Calcular b usando la primera ecuación: a^2 + b = n
	    b = n - a * a

		    # Verificar si b es no negativo y satisface la segunda ecuación: a + b^2 = m
			    if b >= 0 and a + b * b == m:
				        count += 1

						print(count)
