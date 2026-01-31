a, b, x, c, f = map(int, input().split())

L = b-a+1
left = max(a,x-c)
right = min(b, x+c)

longitud = max(0, right - left+1)
bien = L - longitud

ans = pow(bien,f,10**9+7)

print(ans)
