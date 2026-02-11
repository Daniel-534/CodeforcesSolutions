n = int(input())
def ans(n):
    m = (n+1) % 4
    if m == 0:
        return 0
    elif m == 1:
        return 1
    elif m == 2:
        return 4
    else:
        return 3
print(ans(n))
