import sys
from itertools import product

input = sys.stdin.readline

N = int(input())
A = [input() for _ in range(N)]

ds = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

ans = 0
for x, y in product(range(N), range(N)):
    for dx, dy in ds:
        route = A[x][y]
        i, j = x, y
        for _ in range(N - 1):
            i = (i + dx) % N
            j = (j + dy) % N
            route += A[i][j]
        ans = max(ans, int(route))

print(ans)
