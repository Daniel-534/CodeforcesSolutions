T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    c = abs(a-b)
    ans = 0
    if c % 5 == c:
        if c%2==0:
            ans += c//2
        elif c==3:
            ans +=2
        else:
            ans +=1
    elif c%5 == 0:
        ans+= c//5
    else:
        ans += c//5
        aux = c-5*ans
        if aux % 2 == 0:
            ans+= aux//2
        elif aux == 3:
            ans+=2
        else:
            ans+=1
    print(ans)
