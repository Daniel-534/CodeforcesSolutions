q = int(input()) #queries instead of testcases :D
for _ in range(q):
    l, r, d = map(int, input().split())
    if d<l or d>r:
        print(d)
    else:
        c = r//d + 1
        print(c*d)
