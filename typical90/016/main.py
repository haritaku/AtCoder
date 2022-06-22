import sys

input = sys.stdin.readline

N = int(input())
A, B, C = list(map(int, input().split()))

a, b = N // A, N // B
a_min, b_min = min(a + 1, 10_000), min(b + 1, 10_000)

ans = 10_000
for i in range(a_min):
    for j in range(b_min):
        k = int((N - A * i - B * j) / C)
        if k >= 0 and A * i + B * j + k * C == N and i + j + k < ans:
            ans = i + j + k

print(ans)
