import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
XY = [set(list(map(int, input().split()))) for _ in range(M)]

ans = 200_000
for order in permutations(range(N), N):
    time = 0
    for sec, player in enumerate(order):
        if sec != N - 1 and {player + 1, order[sec + 1] + 1} in XY:
            time = None
            break
        time += A[player][sec]

    if time is not None:
        ans = min(time, ans)

print("-1") if ans == 200_000 else print(ans)
