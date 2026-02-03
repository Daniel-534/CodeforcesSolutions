t = int(input())
for _ in range(t):
    x, y, a, b = map(int, input().split())
    # Hacer analisis matematico

    if a==b:
        if x!=y:
            print(-1)
        elif x%a != 0:
            print(-1)
        else:
            print(x//a)
    else:
        if (x+y)%(a+b)!=0:
            print(-1)
        elif (x-y)%(a-b)!=0:
            print(-1)
        else:
            p = (x+y)//(a+b)
            q = (x-y)//(a-b)
            if (p+q)%2 != 0:
                print(-1)
            else:
                m1 = (p+q)//2
                m2 = (p-q)//2
                if m1>=0 and m2>=0:
                    print(p)
                else:
                    print(-1)

