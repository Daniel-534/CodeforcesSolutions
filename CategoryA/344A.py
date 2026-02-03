t = int(input())
count = 1
s = []
for _ in range(t):
    n = input()
    s.append(n)

aux = s[0]
for i in range(1,t):
    if aux != s[i]:
        count+=1
        aux = s[i]
    else:
        continue

print(count)
