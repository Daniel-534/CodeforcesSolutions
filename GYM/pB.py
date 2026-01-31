n = int(input())

if n == 0:
    print(0)
elif n == 1:
    print(67)
else:
    f0 = 0
    f1 = 67

    for _ in range(2, n + 1):
        if f0 == 0:
            print(-1)
            exit()
        fn = f1 * f1 + f1 // f0
        f0, f1 = f1, fn

    print(f1)
