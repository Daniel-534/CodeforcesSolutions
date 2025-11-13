import math

def sum_digits(x):
    return sum(int(d) for d in str(x))

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        while math.gcd(n, sum_digits(n)) == 1:
            n += 1
        print(n)

solve()

