import sys
from collections import defaultdict


class UnionFind:
    """Union Find Algorithm
    参考: https://note.nkmk.me/python-union-find/
    """

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

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return "\n".join(f"{r}: {m}" for r, m in self.all_group_members().items())


def calc_id(x, y):
    return x * (W + 2) + y


input = sys.stdin.readline

H, W = map(int, input().split())
Q = int(input())
q = [list(map(int, input().split())) for _ in range(Q)]

HW = [[-1] + [0] * W + [-1] for _ in range(H + 2)]
HW[0] = [-1] * (W + 2)
HW[-1] = [-1] * (W + 2)

uf = UnionFind((H + 2) * (W + 2))
ds = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for t, *arr in q:
    if t == 1:
        r, c = arr
        HW[r][c] = 1
        for dy, dx in ds:
            new_r, new_c = r + dy, c + dx
            if HW[new_r][new_c] == 1:
                id1, id2 = calc_id(r, c), calc_id(new_r, new_c)
                uf.union(id1, id2)

    elif t == 2:
        ra, ca, rb, cb = arr
        id1, id2 = calc_id(ra, ca), calc_id(rb, cb)
        if HW[ra][ca] and HW[rb][cb] and uf.same(id1, id2):
            print("Yes")
        else:
            print("No")
