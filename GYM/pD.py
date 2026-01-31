n, k = map(int, input().split())

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

S = 0

for i in range(1,n+1):
    S += gcd(i,k)

print(S)
