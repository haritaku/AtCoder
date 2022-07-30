import sys

import numpy as np

input = sys.stdin.readline

N = int(input())
rects = [list(map(int, input().split())) for _ in range(N)]
M = 1_000

field = np.zeros((M + 1, M + 1), dtype=np.int64)

for lx, ly, rx, ry in rects:
    field[lx][ly] += 1
    field[rx][ry] += 1
    field[lx][ry] -= 1
    field[rx][ly] -= 1

field = np.cumsum(field, axis=0)
field = np.cumsum(field, axis=1)

ans = [0] * (N + 1)
unis, cnts = np.unique(field, return_counts=True)
for uni, cnt in zip(unis, cnts):
    ans[uni] = cnt
print(*ans[1:], sep="\n")
