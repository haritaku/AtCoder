import sys

input = sys.stdin.readline

N, X, Y = map(int, input().split())
red = [1] + [0] * (N - 1)
blue = [0] * N

while sum(red[:-1]) != 0:
    for i, cnt in enumerate(red):
        if i == N - 1:
            continue
        if cnt != 0:
            red[i] = 0
            red[i + 1] += cnt
            blue[i] += cnt * X

    for i, cnt in enumerate(blue):
        if i == N - 1:
            continue
        if cnt != 0:
            blue[i] = 0
            red[i + 1] += cnt
            blue[i + 1] += cnt * Y

print(blue[-1])
