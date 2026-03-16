import math

def lcm(x, y):
    return x * y // math.gcd(x, y)

t = int(input())

for _ in range(t):
    a, b, c, m = map(int, input().split())

    v = [a, b, c]

    visits = [m // x for x in v]

    ab = m // lcm(a, b)
    ac = m // lcm(a, c)
    bc = m // lcm(b, c)

    abc = m // lcm(lcm(a, b), c)

    only = [
        visits[0] - ab - ac + abc,
        visits[1] - ab - bc + abc,
        visits[2] - ac - bc + abc
    ]

    pairs = [ab - abc, ac - abc, bc - abc]

    alice = only[0]*6 + pairs[0]*3 + pairs[1]*3 + abc*2
    bob   = only[1]*6 + pairs[0]*3 + pairs[2]*3 + abc*2
    carol = only[2]*6 + pairs[1]*3 + pairs[2]*3 + abc*2

    print(alice, bob, carol)
