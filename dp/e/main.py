import sys

input = sys.stdin.readline
INF = 10**18

N, W = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(N)]

n_dp = N * 10**3 + 1
dp = [INF] * n_dp

dp[0] = 0
ans = 0
for w, v in wv:
    for i in range(n_dp - 1, v - 1, -1):
        dp[i] = min(dp[i], dp[i - v] + w)
        if dp[i] <= W:
            ans = max(ans, i)

print(ans)
