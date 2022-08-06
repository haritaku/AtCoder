import sys

input = sys.stdin.readline

Y = int(input())

q = Y % 4
ref = {0: 2, 1: 1, 2: 0, 3: 3}
print(f"{Y + ref[q]}")
