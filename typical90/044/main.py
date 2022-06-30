import sys

input = sys.stdin.readline

N, Q = list(map(int, input().split()))
A = list(map(int, input().split()))
Txy = [list(map(int, input().split())) for _ in range(Q)]

cnt_shift = 0

for T, x, y in Txy:
    if T == 1:
        idx1 = (x - cnt_shift) % N - 1
        idx2 = (y - cnt_shift) % N - 1
        A[idx1], A[idx2] = A[idx2], A[idx1]
    if T == 2:
        cnt_shift += 1
    if T == 3:
        idx = (x - cnt_shift) % N - 1
        print(A[idx])
