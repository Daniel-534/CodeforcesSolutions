t = int(input())
for _ in range(t):

    n = int(input())
    a = list(map(int, input().split()))

    assert len(a) == len(set(a)), "numbers must be different"

    aux = []
    
    for i in range(n):
        if i%2 == 0:
            aux.append(a[i])
            
    if all(i % 2 == 0 for i in aux):
        print("YES")
    elif all(i % 2 != 0 for i in aux):
        print("YES")
    else:
        print("NO")
