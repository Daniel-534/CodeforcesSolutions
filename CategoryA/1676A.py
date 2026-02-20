t = int(input())
for _ in range(t):
    s = input()
    s1 = sum([int(i) for i in s[:3]])
    s2 = sum([int(i) for i in s[3:]])
    print("YES" if s1==s2 else "NO")
