import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
UV = [list(map(int, input().split())) for _ in range(M)]

adj_set = [set() for _ in range(N + 1)]
for u, v in UV:
    adj_set[u].add(v)
    adj_set[v].add(u)


ans = 0
for a, b, c in combinations(range(1, N + 1), r=3):
    if b in adj_set[a] and c in adj_set[b] and a in adj_set[c]:
        ans += 1
print(ans)
