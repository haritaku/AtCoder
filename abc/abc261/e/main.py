import sys
from operator import iand, ior, ixor

input = sys.stdin.readline

N, C = map(int, input().split())
TA = [list(map(int, input().split())) for _ in range(N)]

opes = {1: iand, 2: ior, 3: ixor}

ans = [0] * N
for i in range(30):
    comp_func = [0, 1]
    x = C >> i & 1
    for j, (t, a) in enumerate(TA):
        a = a >> i & 1

        ope = opes[t]
        comp_func[0] = ope(comp_func[0], a)
        comp_func[1] = ope(comp_func[1], a)

        ans[j] += comp_func[x] << i
        x = comp_func[x]

print(*ans, sep="\n")
