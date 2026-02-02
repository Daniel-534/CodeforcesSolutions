vocales = "aeiouy"
s = input()
step1 = [i.lower() for i in s if i.lower() not in vocales]
step2 =".".join(step1)
ans = "."+step2
print(ans)
