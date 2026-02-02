NoLucky = "47"
n=input()

step1 = [i for i in n if i in NoLucky]
step2 = "".join(step1)

LuckyNumber = False

if step2 == n:
    LuckyNumber = True
    print("YES")
else:
    

