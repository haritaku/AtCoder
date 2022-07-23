import sys

input = sys.stdin.readline

L1, R1, L2, R2 = map(int, input().split())

length = min(R1, R2) - max(L1, L2)
print(max(0, length))
