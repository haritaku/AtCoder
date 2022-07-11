import sys
from itertools import accumulate

input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))
LRV = [list(map(int, input().split())) for _ in range(Q)]

for l, r, v in LRV:
    diff = [0] * N
    diff[l - 1] = v
    if r < N:
        diff[r] = -v
    diff = list(accumulate(diff))

    ans = 0
    for i in range(N):
        A[i] += diff[i]
        if i == 0:
            continue
        ans += abs(A[i - 1] - A[i])
    print(ans)
