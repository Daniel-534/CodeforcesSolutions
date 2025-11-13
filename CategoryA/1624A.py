t = int(input())

for _ in range(t):
    n = int(input())
    lista = list(map(int, input().split()))
    print(max(lista) - min(lista))

