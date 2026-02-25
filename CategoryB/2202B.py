t = int(input())
for _ in range(t):
    n = int(input())
    X = input()
    
    posible = True
    
    if n %2 == 1:
        if X[0] == 'b':
            posible = False

        if posible:
            for i in range(1, n-1, 2):
                if X[i] != '?' and X[i+1] != '?' and X[i] == X[i+1]:
                    posible = False
                    break
    else:
        for i in range(0, n - 1, 2):
            if X[i] != '?' and X[i+1] != '?' and X[i] == X[i+1]:
                posible = False
                break
    
    print("YES" if posible else "NO")
