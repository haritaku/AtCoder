#!/usr/bin/env python3


def main():
    H, W = list(map(int, input().split()))
    mat = [list(map(int, input().split())) for _ in range(H)]

    ans = mat[:]

    ref_h = [sum(mat[i]) for i in range(H)]
    ref_w = []
    for j in range(W):
        ref_w.append(sum([mat[i][j] for i in range(H)]))

    for i in range(H):
        for j in range(W):
            ans[i][j] = ref_h[i] + ref_w[j] - mat[i][j]

    for list_ in ans:
        print(*list_)


if __name__ == "__main__":
    main()
