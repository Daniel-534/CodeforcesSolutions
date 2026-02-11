m, p = map(str, input().split())
planetas = {
    "Mercury": 4,
    "Venus": 9,
    "Earth": 10,
    "Mars": 4,
    "Jupiter": 25,
    "Saturn": 11,
    "Uranus": 9,
    "Neptune": 11,
    "Pluto": 1
}
ans = int(m)*planetas[p]
print(ans)
