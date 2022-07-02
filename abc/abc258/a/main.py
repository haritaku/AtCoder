import sys

input = sys.stdin.readline

K = int(input())

h, mm = divmod(K, 60)
hh = 21 + h

print(f"{hh}:{mm:02}")
