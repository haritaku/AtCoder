import sys

import numpy as np

input = sys.stdin.readline

a, b, d = list(map(int, input().split()))

coord = np.array([a, b]).reshape(2, 1)
rad = np.deg2rad(d)
mat = np.array([[np.cos(rad), -np.sin(rad)], [np.sin(rad), np.cos(rad)]])

ans = (mat @ coord).reshape(2)
print(*ans)
