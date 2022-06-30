import sys
from math import gcd

input = sys.stdin.readline

A, B = list(map(int, input().split()))

ans = A * B // gcd(A, B)
print("Large") if ans > 10**18 else print(ans)
