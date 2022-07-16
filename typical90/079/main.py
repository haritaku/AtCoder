import sys
from itertools import product

input = sys.stdin.readline

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]

cnt = 0
for i, j in product(range(H - 1), range(W - 1)):
    diff = B[i][j] - A[i][j]
    if diff != 0:
        cnt += abs(diff)
        A[i][j] += diff
        A[i][j + 1] += diff
        A[i + 1][j] += diff
        A[i + 1][j + 1] += diff

if A[-1] == B[-1]:
    print(f"Yes\n{cnt}")
else:
    print("No")
