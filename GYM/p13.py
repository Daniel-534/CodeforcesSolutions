A = int(input())
n = 1
for i in range(int(A**(0.5)),0,-1):
    if A %i == 0:
        n = i
        break
    else:
        continue

ans = 2*(n+A//n)

print(ans)
   
