import sys
from functools import reduce
from operator import mul

input = sys.stdin.readline

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

print(reduce(mul, [sum(a) for a in A]) % (10**9 + 7))
