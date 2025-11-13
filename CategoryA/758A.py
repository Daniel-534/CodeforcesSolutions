# Daniel.Soto - CosmologyAndGravitation_GravitationalWaves_LVK
# Contact: daniel.soto1@udea.edu.co

n = int(input())
a = list(map(int, input().split()))

maximo = max(a)

total = 0
for i in a:
    total += maximo - i

print(total)
