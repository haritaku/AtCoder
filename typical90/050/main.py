import sys
from math import comb

input = sys.stdin.readline

N, L = list(map(int, input().split()))

n_L = N // L

ans = 0
for cnt_L in range(0, n_L + 1):
    cnt_1 = N - L * cnt_L
    ans += comb(cnt_L + cnt_1, cnt_1)

print(ans % (10**9 + 7))
