n = int(input())
s = input()

CountAllPossible = n//11

CountEight = s.count("8")

ans = min(CountAllPossible, CountEight)

print(ans)
