t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    max_bloques=0
    for inicio in range(n):
        bloques=1
        for j in range(1,n):
            if s[(inicio+j)%n]!=s[(inicio+j-1)%n]:
                bloques+=1
        max_bloques=max(max_bloques,bloques)
    print(max_bloques)
