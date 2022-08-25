import sys

input = sys.stdin.readline
MOD = 10**9 + 7

K = int(input())

if K % 9 != 0:
    print(0)
    exit()

dp = [0] * (K+1)
dp[0] = 1

for i in range(1, K+1):
    for v in range(1, 10):
        if i - v >= 0:
            dp[i] += dp[i - v]
    dp[i] %= MOD

print(dp[K])
