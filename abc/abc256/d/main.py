import sys
from itertools import accumulate

input = sys.stdin.readline

N = int(input())
LR = [list(map(int, input().split())) for _ in range(N)]

arr = [0] * (3 * 10**6)

for l, r in LR:
    arr[l] += 1
    arr[r] -= 1

arr = list(accumulate(arr))

before = 0
for i, v in enumerate(arr):
    if before == 0 and v > 0:
        before = v
        left = i
        continue

    if before > 0 and v == 0:
        print(f"{left} {i}")
        before = v
