import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_sorted = sorted(A)
B_sorted = sorted(B)

print(sum([abs(A_sorted[i] - B_sorted[i]) for i in range(N)]))
