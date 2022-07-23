import sys

input = sys.stdin.readline

N = int(input())
S = [input().rstrip() for _ in range(N)]

cnt_dict = {}
for s in S:
    if s not in cnt_dict:
        print(s)
        cnt_dict[s] = 1
    else:
        print(f"{s}({cnt_dict[s]})")
        cnt_dict[s] += 1
