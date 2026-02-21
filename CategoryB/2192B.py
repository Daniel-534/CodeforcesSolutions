t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    count_0=s.count('0')
    count_1=s.count('1')
    if count_1%2==0:
        print(count_1)
        if count_1>0:
            posiciones=[str(i+1) for i in range(n) if s[i]=='1']
            print(' '.join(posiciones))
    elif count_0%2==1:
        print(count_0)
        posiciones=[str(i+1) for i in range(n) if s[i]=='0']
        print(' '.join(posiciones))
    else:
        print(-1)
