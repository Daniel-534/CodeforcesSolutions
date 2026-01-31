n = int(input())
const = "abcdefghijklmnopqrstuvwxyz"

terms = []

for i in range(n, -1, -1):
    coef = const[n - i]
    if i == 0:
        terms.append(coef)
    elif i == 1:
        terms.append(f"{coef}x")
    else:
        terms.append(f"{coef}x^{i}")

print(" + ".join(terms))
