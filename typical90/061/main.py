import sys
from collections import deque

input = sys.stdin.readline

Q = int(input())
tx = [list(map(int, input().split())) for _ in range(Q)]


d = deque()
for t, x in tx:
    if t == 1:
        d.appendleft(x)
    elif t == 2:
        d.append(x)
    else:
        print(d[x - 1])
