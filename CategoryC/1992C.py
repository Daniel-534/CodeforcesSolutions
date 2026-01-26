t = int(input())

for _ in range(t):
    n, m, k = map(int, input().split())
    
    case1 = list(range(n, k-1, -1))
    case2 = list(range(m+1, k))
    case3 = list(range(1, m+1))
    
    p = case1+case2+case3

    print(*p)
