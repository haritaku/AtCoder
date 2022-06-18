#!/usr/bin/env python3
from itertools import accumulate


def main():
    N = int(input())
    ST = [list(map(int, input().split())) for _ in range(N)]
    Q = int(input())
    LR = [list(map(int, input().split())) for _ in range(Q)]

    accs = []
    for cls_num in [1, 2]:
        acc = [0 for _ in range(N)]
        for i, (cls, score) in enumerate(ST):
            if cls == cls_num:
                acc[i] = score
        accs.append(list(accumulate(acc)))

    for l, r in LR:
        ans = []
        for acc in accs:
            l_acc = 0 if l - 2 < 0 else acc[l - 2]
            ans.append(acc[r - 1] - l_acc)

        print(*ans)


if __name__ == "__main__":
    main()
