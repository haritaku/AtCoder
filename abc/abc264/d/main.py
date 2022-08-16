import sys

input = sys.stdin.readline

ref = {"a": 1, "t": 2, "c": 3, "o": 4, "d": 5, "e": 6, "r": 7}
S = input().rstrip()
order = [ref[s] for s in S]

ans = 0
for i in range(6, -1, -1):
    for j in range(i):
        if order[j] > order[j + 1]:
            ans += 1
            order[j], order[j + 1] = order[j + 1], order[j]
print(ans)
