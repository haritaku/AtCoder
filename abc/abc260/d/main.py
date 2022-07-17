import sys
from bisect import bisect_left

input = sys.stdin.readline

N, K = map(int, input().split())
P = list(map(int, input().split()))

ans = [-1] * N
front = []
deck = []

for i, p in enumerate(P, start=1):
    idx = bisect_left(front, p)
    if idx == len(front):
        front.append(p)
        deck.append([p])
    else:
        front[idx] = p
        deck[idx].append(p)

    if len(deck[idx]) == K:
        del front[idx]
        for j in deck.pop(idx):
            ans[j - 1] = i

print(*ans, sep="\n")
