t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    Count = 0
    for i in s:
        if i!= s[-1]:
            Count +=1
        else:
            continue
    print(Count)
