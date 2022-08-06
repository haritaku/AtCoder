import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())

ans = []
for arr in combinations(range(1, M + 1), r=N):
    before = arr[0]
    for val in arr[1:]:
        if val < before:
            break
    else:
        ans.append(arr)

for arr in sorted(ans):
    print(*arr)
