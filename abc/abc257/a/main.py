import sys

input = sys.stdin.readline

N, X = list(map(int, input().split()))

master = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

r, q = divmod(X, N)
idx = r if q > 0 else r - 1
print(master[idx])
