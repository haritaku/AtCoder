import sys

input = sys.stdin.readline

N, M, X, T, D = list(map(int, input().split()))

if M < X:
    print(T - D * (X - M))
else:
    print(T)
