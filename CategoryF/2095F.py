a, b  = map(int,input().split())

ans = 12*a+14*a*b+abs(a-b) + (a-3*b)*b+2

print(ans)
