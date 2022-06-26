import sys
from math import atan, cos, pi, sin, sqrt, tan

input = sys.stdin.readline

T = int(input())
L, X, Y = list(map(int, input().split()))
Q = int(input())
E = [int(input()) for _ in range(Q)]

radps = -2 * pi / T

for e in E:
    rad = radps * e - pi / 2
    y = cos(rad) * L / 2
    z = sin(rad) * L / 2 + L / 2

    d_xy = sqrt(X**2 + (Y - y) ** 2)
    ans_rad = atan(z / d_xy)
    print(180 * ans_rad / pi)
