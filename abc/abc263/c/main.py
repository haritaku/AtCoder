import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())

ans = []
for arr in combinations(range(1, M + 1), r=N):
    print(*arr)
