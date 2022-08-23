import sys

input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()
n_s, n_t = len(s), len(t)

dp = [0] * (n_t + 1)
ref = [0] * (n_t + 1)

for i in range(1, n_s + 1):
    nxt = [0] * (n_t + 1)
    nxt_ref = [0] * (n_t + 1)
    for j in range(1, n_t + 1):
        if s[i - 1] == t[j - 1]:
            nxt[j] = dp[j - 1] + 1
            nxt_ref[j] = ref[j - 1] + (1 << (i - 1))
        else:
            if dp[j] > nxt[j - 1]:
                nxt[j] = dp[j]
                nxt_ref[j] = ref[j]
            else:
                nxt[j] = nxt[j - 1]
                nxt_ref[j] = nxt_ref[j - 1]
    dp = nxt
    ref = nxt_ref

ans = ""
for i, val in enumerate(s):
    if (ref[-1] >> i) & 1:
        ans += val
print(ans)
