s = input()

step1 = [i for i in s if i!= "+"]
step2 = sorted(step1)
ans = "+".join(step2)

print(ans)
