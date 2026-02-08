n = int(input())
M = [list(map(int, input().split())) for _ in range(n)]

a1_sq = (M[0][1] * M[0][2]) // M[1][2]
a1 = int(a1_sq**0.5)

res = [a1]
for j in range(1, n):
    res.append(M[0][j] // a1)

print(*res)
