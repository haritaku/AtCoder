import sys

input = sys.stdin.readline
MOD = 10**9 + 7

L, R = map(int, input().split())
coef_L, coef_R = len(str(L)), len(str(R))

ans = 0
_sum = lambda x: x * (x + 1) // 2
for i in range(coef_L, coef_R + 1):
    l = max(10 ** (i - 1), L) - 1
    r = min(10**i - 1, R)
    ans += (_sum(r) - _sum(l)) * i % MOD

print(ans % MOD)
