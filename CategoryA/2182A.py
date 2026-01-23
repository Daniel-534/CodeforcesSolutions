t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    if ("2025" in s) and ("2026" not in s):
        print(1)
    else:
        print(0)
