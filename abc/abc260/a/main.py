import sys
from collections import Counter

input = sys.stdin.readline

S = input().rstrip()

cnt = Counter(S)
for k, v in cnt.items():
    if v == 1:
        print(k)
else:
    print(-1)
