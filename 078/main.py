import sys

input = sys.stdin.readline

N, M = list(map(int, input().split()))
ab = [list(map(int, input().split())) for _ in range(M)]

cnts = [0] * (N + 1)
for a, b in ab:
    if a == b:
        continue
    cnts[max(a, b)] += 1

print(len(list(filter(lambda x: x == 1, cnts))))
