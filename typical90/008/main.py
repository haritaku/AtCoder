import sys

input = sys.stdin.readline
MOD = 10**9 + 7

N = int(input())
S = input().rstrip()

target = "atcoder"
M = len(target)
dp = [[0] * (N + 1) for _ in range(M + 1)]
dp[0] = [1] * (N + 1)

for i in range(1, M + 1):
    for j in range(1, N + 1):
        dp[i][j] = dp[i][j - 1] % MOD
        if target[i - 1] == S[j - 1]:
            dp[i][j] += dp[i - 1][j - 1] % MOD

print(dp[-1][-1] % MOD)
