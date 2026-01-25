t = int(input())
for _ in range(t):
    a = input()

    b = list(a[::-1])
    
    for i in range(len(b)):
        if b[i] == "p":
            b[i] = "q"
        elif b[i] != "w":
            b[i] = "p"
        else:
            continue
    b = "".join(b)        
    print(b)
