import sys

input = sys.stdin.readline

N, Q = list(map(int, input().split()))
S = input()
q = [list(map(int, input().split())) for _ in range(Q)]

cnt_move = 0

for t, x in q:
    if t == 1:
        cnt_move += x
    else:
        idx = (x - 1 - cnt_move) % N
        print(S[idx])
