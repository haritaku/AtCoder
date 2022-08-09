import sys
from itertools import product

input = sys.stdin.readline

h1, h2, h3, w1, w2, w3 = map(int, input().split())

cnt = 0
for m11, m12, m21, m22 in product(range(1, 30), repeat=4):
    m13 = h1 - m11 - m12
    m23 = h2 - m21 - m22

    m31 = w1 - m11 - m21
    m32 = w2 - m12 - m22
    m33 = w3 - m13 - m23

    if m13 <= 0 or m23 <= 0 or m31 <= 0 or m32 <= 0 or m33 <= 0:
        continue

    if m31 + m32 + m33 == h3:
        cnt += 1

print(cnt)
