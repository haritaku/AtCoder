import sys

input = sys.stdin.readline

N, M = map(int, input().split())
X = list(map(int, input().split()))
CY = [list(map(int, input().split())) for _ in range(M)]
CY = {c: y for c, y in CY}

dp = [0] * (N + 1)

for i, x in enumerate(X, start=1):
    tmp = max(dp)
    for j in range(N, 0, -1):
        if j <= i:
            dp[j] = dp[j - 1] + x + CY.get(j, 0)
    dp[0] = tmp

print(max(dp))
