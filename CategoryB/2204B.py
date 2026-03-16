t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    count = 0
    prefix_max = 0
    
    for i in range(n):
        if a[i] >= prefix_max:
            count += 1
            prefix_max = a[i]
    
    print(count)
