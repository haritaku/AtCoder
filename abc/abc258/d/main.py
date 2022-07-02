import sys

input = sys.stdin.readline

N, X = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(N)]

ans = 10**19
ab = 0
for i in range(min(N, X)):
    a, b = AB[i]
    ab += a + b
    ans = min(ans, ab + b * (X - i - 1))

print(ans)
