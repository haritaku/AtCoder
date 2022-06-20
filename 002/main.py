import sys
from itertools import product

input = sys.stdin.readline

N = int(input())

if N % 2 == 1:
    print()
    exit()

for s in product(("(", ")"), repeat=N):
    score = 0
    for c in s:
        if c == "(":
            score += 1
        else:
            score -= 1

        if score < 0:
            break
    if score == 0:
        print(*s, sep="")
