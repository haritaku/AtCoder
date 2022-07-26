import sys

input = sys.stdin.readline

N, C = map(int, input().split())
TA = [list(map(int, input().split())) for _ in range(N)]

ans = [0] * N
for i in range(30):
    ope = [0, 1]

    x = 1 if C & (1 << i) else 0
    for j, (t, a) in enumerate(TA):
        a = 1 if a & (1 << i) else 0
        if t == 1:
            ope[0] &= a
            ope[1] &= a
        elif t == 2:
            ope[0] |= a
            ope[1] |= a
        elif t == 3:
            ope[0] ^= a
            ope[1] ^= a
        ans[j] += ope[x] << i
        x = ope[x]

print(*ans, sep="\n")
