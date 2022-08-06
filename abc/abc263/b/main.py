import sys

input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))

cnt = 1
idx = P[-1]
while idx != 1:
    cnt += 1
    idx = P[idx - 2]

print(cnt)
