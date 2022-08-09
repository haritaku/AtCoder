import sys

input = sys.stdin.readline

N = int(input())
hs = list(map(int, input().split()))

dp = [0] * N
dp[1] = abs(hs[1] - hs[0])
for i in range(2, N):
    dp[i] = min(dp[i - 1] + abs(hs[i] - hs[i - 1]), dp[i - 2] + abs(hs[i] - hs[i - 2]))

print(dp[-1])
