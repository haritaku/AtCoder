import sys
from collections import Counter, deque

input = sys.stdin.readline

N, K = map(int, input().split())
a_list = list(map(int, input().split()))

q = deque()
c = Counter()
ans = 0
for a in a_list:
    q.append(a)
    c[a] += 1

    while len(c) > K:
        rm = q.popleft()
        c[rm] -= 1
        if c[rm] == 0:
            c.pop(rm)
    ans = max(ans, len(q))

print(ans)
