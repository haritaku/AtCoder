import sys

input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))
LRV = [list(map(int, input().split())) for _ in range(Q)]


B = []
for i in range(N):
    if i == 0:
        continue
    B.append(A[i] - A[i - 1])
ans = sum(map(abs, B))

for l, r, v in LRV:
    before, after = 0, 0
    if l - 2 >= 0:
        before += abs(B[l - 2])
        B[l - 2] += v
        after += abs(B[l - 2])
    if r - 1 <= N - 2:
        before += abs(B[r - 1])
        B[r - 1] += -v
        after += abs(B[r - 1])
    ans += after - before
    print(ans)
