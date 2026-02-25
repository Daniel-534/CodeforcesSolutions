t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    
    if (x - 2*y) %3 != 0:
        print("NO")
    else:
        if y >= 0:
            if x >= 2*y:
                print("YES")
            else:
                print("NO")
        else:
            if x >= -4*y:
                print("YES")
            else:
                print("NO")
