a, b = map(int, input().split())

n = 0

flag = True

while flag:

    l = 3**n * a
    r = 2**n * b
    n+=1

    if l>r:
        flag = False

print(n - 1) 
