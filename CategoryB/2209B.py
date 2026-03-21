import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    result = []
    for i in range(n):
        v = a[i]
        greater = 0
        less = 0
        for j in range(i + 1, n):
            if a[j] > v:
                greater += 1
            elif a[j] < v:
                less += 1
        result.append(max(greater, less))
    
    print(*result)
