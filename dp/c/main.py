import sys

input = sys.stdin.readline

N = int(input())
abc = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * 3  # a, b, c

for a, b, c in abc:
    nxt = [0, 0, 0]
    nxt[0] = max(dp[1] + a, dp[2] + a)
    nxt[1] = max(dp[0] + b, dp[2] + b)
    nxt[2] = max(dp[0] + c, dp[1] + c)

    for i in range(3):
        dp[i] = nxt[i]

print(max(dp))
