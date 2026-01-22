t = int(input())

for _ in range(t):
    n = int(input())

    if n in [2, 3]:
        print(n)
    elif n%2 == 0:
        print(n%2)
    else:
        print(1)
