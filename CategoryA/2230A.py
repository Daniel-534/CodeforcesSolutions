t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    if n%3 == 0:
        print(n*b)
    elif n%3 ==1:
        print(n*b+a)
    else:
        print(b + 2*a)
