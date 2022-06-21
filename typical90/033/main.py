#!/usr/bin/env python3


def main():
    H, W = list(map(int, input().split()))

    if H == 1 or W == 1:
        print(H * W)
    else:
        print(((H + 1) // 2) * ((W + 1) // 2))


if __name__ == "__main__":
    main()
