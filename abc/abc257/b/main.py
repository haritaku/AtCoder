import sys

input = sys.stdin.readline

N, K, Q = list(map(int, input().split()))
A = list(map(int, input().split()))
L = list(map(int, input().split()))


for l in L:
    new_pos = A[l - 1] + 1
    if new_pos not in A and new_pos <= N:
        A[l - 1] = new_pos

print(*A)
