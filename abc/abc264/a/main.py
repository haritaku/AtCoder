import sys

input = sys.stdin.readline

L, R = map(int, input().split())
L -= 1
R -= 1
s = "atcoder"

print(s[L : R + 1])
