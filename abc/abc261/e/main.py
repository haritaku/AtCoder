import sys
from operator import and_, or_, xor

input = sys.stdin.readline

N, C = map(int, input().split())
TA = [list(map(int, input().split())) for _ in range(N)]

ref = {1: and_, 2: or_, 3: xor}

ans = [0] * N
for i in range(30):
    ope = [0, 1]
    x = 1 if C & (1 << i) else 0
    for j, (t, a) in enumerate(TA):
        a = 1 if a & (1 << i) else 0

        ope[0] = ref[t](ope[0], a)
        ope[1] = ref[t](ope[1], a)

        ans[j] += ope[x] << i
        x = ope[x]

print(*ans, sep="\n")
