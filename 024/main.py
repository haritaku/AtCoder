#!/usr/bin/env python3


def main():
    N, K = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    min_cnt = 0
    for i in range(N):
        min_cnt += abs(A[i] - B[i])

    if min_cnt > K or (K - min_cnt) % 2:
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    main()
