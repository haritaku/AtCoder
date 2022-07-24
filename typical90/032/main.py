import sys

input = sys.stdin.readline
INF = 10**18

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
XY = [list(map(int, input().split())) for _ in range(M)]

ok = [[True] * N for _ in range(N)]
for x, y in XY:
    ok[x - 1][y - 1] = False
    ok[y - 1][x - 1] = False
for i in range(N):
    ok[i][i] = False

dp = [[INF] * N for _ in range(1 << N)]
for i in range(N):
    dp[0][i] = 0

for s in range(1 << N):
    for v in range(N):
        if s & (1 << v) == 0:
            continue
        cnt = bin(s).count("1")
        s_before = s ^ (1 << v)

        for u in range(N):
            if s_before == 0 or ok[v][u]:
                dp[s][v] = min(dp[s][v], dp[s_before][u] + A[v][cnt - 1])

ans = min(dp[-1])
print(-1 if ans == INF else ans)
