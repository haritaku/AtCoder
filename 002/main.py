import sys
from itertools import accumulate

input = sys.stdin.readline

N = int(input())

if N % 2 == 1:
    print()
    exit()

ans = []
for bin_ in range(1 << N):

    s = ""
    for i in range(N):
        if bin_ >> i & 1:
            s += "("
        else:
            s += ")"

    if s.count("(") != s.count(")"):
        continue

    score = 0
    for c in s:
        if c == "(":
            score += 1
        else:
            score -= 1

        if score < 0:
            break
    if score == 0:
        ans.append(s)

ans.sort()

print(*ans, sep="\n")
