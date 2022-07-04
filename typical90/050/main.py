import sys

input = sys.stdin.readline

N, L = list(map(int, input().split()))

dp = [None] * (N + 1)

for i in range(N + 1):
    if i == 0:
        dp[0] = 1
        continue

    dp[i] = dp[i - 1]
    if i - L >= 0:
        dp[i] += dp[i - L]

print(dp[N] % (10**9 + 7))
