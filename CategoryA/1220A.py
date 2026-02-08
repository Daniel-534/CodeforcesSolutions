n = int(input())
s = input()

CountOnes = s.count("n")
CountZeros = s.count("z")

Ones = [1]*CountOnes
Zeros = [0]*CountZeros

ans = Ones + Zeros

print(*ans)
