g, c, l = map(int, input().split())

scores = [g, c, l]

if abs(min(scores) - max(scores)) >= 10:
    print("check again")
else:
    scores.sort()
    ans = scores[1]
    print(f"final {ans}")
