import sys
from collections import Counter

input = sys.stdin.readline

card = list(map(int, input().split()))

cnt = Counter(card)

if 2 in cnt.values() and 3 in cnt.values():
    print("Yes")
else:
    print("No")
