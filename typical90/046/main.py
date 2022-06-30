import sys
from collections import defaultdict
from itertools import product

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

cnt_A = defaultdict(int)
cnt_B = defaultdict(int)
cnt_C = defaultdict(int)

for a, b, c in zip(A, B, C):
    cnt_A[a % 46] += 1
    cnt_B[b % 46] += 1
    cnt_C[c % 46] += 1

ans = 0
for a, b, c in product(range(46), repeat=3):
    if (a + b + c) % 46 == 0:
        ans += cnt_A[a] * cnt_B[b] * cnt_C[c]
print(ans)
