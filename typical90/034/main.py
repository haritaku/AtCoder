import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N, K = map(int, input().split())
a_list = list(map(int, input().split()))

q = deque()
kind = 0
d = defaultdict(int)
ans = 0
for a in a_list:
    q.append(a)
    d[a] += 1
    if d[a] == 1:
        kind += 1

    while q and kind > K:
        rm = q.popleft()
        d[rm] -= 1
        if d[rm] == 0:
            kind -= 1
    ans = max(ans, len(q))

print(ans)
