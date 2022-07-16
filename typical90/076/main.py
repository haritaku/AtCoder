import sys
from bisect import bisect_left
from itertools import accumulate

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

A += A[:-1]
B = [0] + list(accumulate(A + A[:-1]))

target = B[N] // 10
for i in range(N):
    idx = bisect_left(B, B[i] + target, lo=i + 1)
    if B[idx] == B[i] + target:
        print("Yes")
        break
else:
    print("No")
