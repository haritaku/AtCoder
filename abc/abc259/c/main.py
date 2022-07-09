import sys
from itertools import groupby

input = sys.stdin.readline

S = input().rstrip()
T = input().rstrip()


def rle(string):
    """Run Length Encoding"""
    rle_list = []
    for k, group in groupby(string):
        rle_list.append((k, len(tuple(group))))
    return rle_list


S_rle, T_rle = rle(S), rle(T)

if len(S_rle) != len(T_rle):
    print("No")
    sys.exit()

for s_rle, t_rle in zip(S_rle, T_rle):
    if s_rle[0] != t_rle[0] or s_rle[1] > t_rle[1]:
        print("No")
        sys.exit()

    if s_rle[1] == 1 and s_rle[1] < t_rle[1]:
        print("No")
        sys.exit()

print("Yes")
