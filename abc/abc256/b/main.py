import sys

input = sys.stdin.readline

_ = int(input())
xs = list(map(int, input().split()))

sum_ = 0
pos = []
for x in xs:
    pos.append(0)
    tmp = []
    for i in pos:
        next_ = i + x
        if next_ > 3:
            sum_ += 1
        else:
            tmp.append(next_)
    pos = tmp
print(sum_)
