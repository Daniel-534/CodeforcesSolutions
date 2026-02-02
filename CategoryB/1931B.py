t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    k = sum(a)//n
    flag=True
    for i in range(n-1):
        if a[i] < k:
            print("NO")
            flag = False
            break
        a[i+1] += a[i] - k
        a[i] = k
    if flag:
        print("YES")
    
