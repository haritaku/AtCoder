import sys
from itertools import groupby


def rle(string):
    """Run Length Encoding"""

    rle_list = []
    for k, group in groupby(string):
        rle_list.append((k, sum(1 for _ in group)))
    return rle_list


_sum = lambda x: x * (x + 1) // 2

input = sys.stdin.readline
N = int(input())
S = input().rstrip()

ans = _sum(N)
for _, cnt in rle(S):
    ans -= _sum(cnt)
print(ans)
