from collections import defaultdict
from itertools import groupby
from math import sqrt


def is_prime(x):
    if x == 1:
        return False

    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def prime_factorization(x):
    primes = []
    for i in range(2, int(sqrt(x)) + 1):
        while x % i == 0:
            primes.append(i)
            x //= i
    if x != 1:
        primes.append(x)
    return primes


def rle(string):
    """Run Length Encoding"""

    rle_list = []
    for k, group in groupby(string):
        rle_list.append((k, sum(1 for _ in group)))
    return rle_list


def boyer_moore(txt, pat):
    N, M = len(txt), len(pat)

    skip = defaultdict(lambda: M)
    for i, s in enumerate(pat, start=1):
        skip[s] = M - i

    idx = M - 1
    while idx < N:
        for j, s in enumerate(pat[::-1]):
            t = txt[idx - j]
            if t != s:
                idx += skip[t]
                break
        else:
            return idx - M + 1
    return -1


def binary_search(ng, ok, check):
    while abs(ok - ng) > 1:
        mid = (ng + ok) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid
    return ok


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
