t = int(input())
for _ in range(t):
    p, q = map(int, input().split())
    D = 3*p - 2*q
    
    if D == 0:
        print("Bob")
    elif D < 0:
        print("Alice")
    else:
        if p <= q - 1:
            print("Bob")
        else:
            print("Alice")
