import sys

input = sys.stdin.readline

N, M = map(int, input().split())
X = list(map(int, input().split()))
CY = [list(map(int, input().split())) for _ in range(M)]
ref = [0] * (N + 1)
for c, y in CY:
    ref[c] = y

dp = [0] * (N + 1)
for i, x in enumerate(X, start=1):
    tmp = max(dp)
    for j in range(i, 0, -1):
        dp[j] = dp[j - 1] + x + ref[j]
    dp[0] = tmp

print(max(dp))
