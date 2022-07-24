import sys

input = sys.stdin.readline
INF = 10**18

N, M = map(int, input().split())
X = list(map(int, input().split()))
CY = [list(map(int, input().split())) for _ in range(M)]
CY = {c: y for c, y in CY}

dp = [[-INF] * (N + 1) for _ in range(N + 1)]

max_ = 0
dp[0][0] = 0
for i in range(1, N + 1):
    dp[i][0] = max_
    max_ = 0
    for j in range(1, N + 1):
        dp[i][j] = dp[i - 1][j - 1] + CY.get(j, 0) + X[i - 1]
        max_ = max(max_, dp[i][j])

print(max_)
