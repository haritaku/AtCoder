import sys
from itertools import combinations


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)


input = sys.stdin.readline

N = int(input())
sx, sy, tx, ty = map(int, input().split())
xyris = [list(map(int, input().split())) + [i] for i in range(N)]

for x, y, r, i in xyris:
    if (sx - x) ** 2 + (sy - y) ** 2 == r**2:
        s_idx = i
    if (tx - x) ** 2 + (ty - y) ** 2 == r**2:
        t_idx = i

uf = UnionFind(N)
for (x1, y1, r1, i1), (x2, y2, r2, i2) in combinations(xyris, r=2):
    d = (x1 - x2) ** 2 + (y1 - y2) ** 2
    rm = (r1 - r2) ** 2
    rp = (r1 + r2) ** 2

    if rm <= d <= rp:
        uf.union(*[i1, i2])

if uf.find(s_idx) == uf.find(t_idx):
    print("Yes")
else:
    print("No")
