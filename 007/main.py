import sys
from bisect import bisect_left

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
B = [int(input()) for _ in range(Q)]

sorted_A = sorted(A)

for b in B:
    idx = bisect_left(sorted_A, b)
    print(min(abs(sorted_A[min(idx, N - 1)] - b), abs(sorted_A[max(idx - 1, 0)] - b)))
