t = int(input())
for _ in range(t):
    s = input()
    s = list(s)
    if len(set(s)) == 1:
        print("NO")
    else:
        for i in range(len(s)):
            if s[0] != s[i]:
                s[i],s[0] = s[0],s[i]
                print("YES")
                ans = "".join(s)
                print(ans)
                break
            else:
                continue
