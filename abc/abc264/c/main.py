import sys
from itertools import combinations

import numpy as np

input = sys.stdin.readline

H1, W1 = map(int, input().split())
A = np.array([list(map(int, input().split())) for _ in range(H1)])

H2, W2 = map(int, input().split())
B = np.array([list(map(int, input().split())) for _ in range(H2)])

diff_h = H1 - H2
diff_w = W1 - W2

flg = "No"
for idx_x in combinations(range(H1), r=H2):
    for idx_y in combinations(range(W1), r=W2):
        if np.all(A[idx_x, :][:, idx_y] == B):
            flg = "Yes"
print(flg)
