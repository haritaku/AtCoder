import sys

input = sys.stdin.readline

N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


arr = [(i + 1, A[i], B[i], A[i] + B[i]) for i in range(N)]

ans = []
for i, rank in enumerate([X, Y, Z], start=1):
    arr = sorted(arr, key=lambda x: (x[i], -x[0]), reverse=True)
    ans += [nums[0] for nums in arr[:rank]]
    if i < 3:
        arr = arr[rank:]
print(*sorted(ans), sep="\n")
