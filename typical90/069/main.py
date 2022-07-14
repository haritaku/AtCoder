import sys

input = sys.stdin.readline

N, K = map(int, input().split())
MOD = 10**9 + 7

if N == 1:
    print(K)
else:
    print(pow(K - 2, N - 2, MOD) * ((K - 1) % MOD) * (K % MOD) % MOD)
