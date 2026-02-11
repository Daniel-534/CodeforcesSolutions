import math
a = int(input())

ans = 0
for i in range(2,a+1):
    ans += math.log10(i)

print(int(ans))
