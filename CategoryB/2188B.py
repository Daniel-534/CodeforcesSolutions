def min_seated(s):
    n = len(s)
    new = 0
    i = 0
    while i < n:
        if s[i] == '1':
            i += 1
            continue
        left_occupied = (i > 0 and s[i-1] == '1')
        right_occupied = (i < n-1 and s[i+1] == '1')

        if left_occupied or right_occupied:
            i += 1
        else:
            if i == n-1:
                new += 1
                i += 1
            else:
                new += 1
                i += 3
    return new + s.count('1')
    
t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    ans = min_seated(s)
    print(ans)
