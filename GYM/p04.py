x = input()
y = input()

if x.lower() == y.lower():
    print(0)
elif x.lower() < y.lower():
    print(-1)
else:
    print(1)
