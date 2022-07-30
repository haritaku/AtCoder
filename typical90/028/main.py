import sys

input = sys.stdin.readline

N = int(input())
rects = [list(map(int, input().split())) for _ in range(N)]
M = 1_000

field = [[0] * (M + 1) for _ in range(M + 1)]

for lx, ly, rx, ry in rects:
    field[lx][ly] += 1
    field[rx][ry] += 1
    field[lx][ry] -= 1
    field[rx][ly] -= 1

for i in range(M):
    for j in range(M):
        field[i][j + 1] += field[i][j]

ans = [0] * (N + 1)
for j in range(M):
    for i in range(M):
        field[i + 1][j] += field[i][j]
        ans[field[i][j]] += 1

print(*ans[1:], sep="\n")
