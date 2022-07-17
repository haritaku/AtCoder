import sys
from bisect import bisect_left

input = sys.stdin.readline

N, K = map(int, input().split())
P = list(map(int, input().split()))

ans = [-1] * N
front = []
deck = {}

for i, p in enumerate(P, start=1):
    idx = bisect_left(front, p)
    if idx == len(front):
        front.append(p)
        deck[p] = [p]
    else:
        front[idx] = p
        deck[p] = deck.pop(front[idx]) + [p]

    if len(deck[p]) == K:
        del front[idx]
        for j in deck.pop(p):
            ans[j - 1] = i

print(*ans, sep="\n")
