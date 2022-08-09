import sys

input = sys.stdin.readline

N, W = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * (W + 1)
for w, v in wv:
    for i in range(W, -1, -1):
        if i - w >= 0:
            dp[i] = max(dp[i], dp[i - w] + v)
print(dp[-1])
