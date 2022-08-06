import sys

input = sys.stdin.readline

INF = 10**18
N, L, R = list(map(int, input().split()))
A = list(map(int, input().split()))

f = [0] * (N + 1)
for i in range(N):
    f[i + 1] = min(f[i] + A[i], L * (i + 1))

g = [0] * (N + 1)
for j in range(N):
    g[j + 1] = min(g[j] + A[-(j + 1)], R * (j + 1))

ans = INF
for i in range(N + 1):
    ans = min(ans, f[i] + g[N - i])
print(ans)
