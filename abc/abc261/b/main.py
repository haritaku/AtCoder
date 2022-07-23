import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())
A = [input().rstrip() for _ in range(N)]

for i, j in combinations(range(N), 2):
    if A[i][j] != "D" and (A[i][j] == A[j][i] or A[j][i] == "D"):
        print("incorrect")
        break
    if A[i][j] == "D" and A[j][i] != "D":
        print("incorrect")
        break
else:
    print("correct")
