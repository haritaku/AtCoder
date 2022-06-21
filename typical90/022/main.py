#!/usr/bin/env python3

from math import gcd


def main():
    A, B, C = list(map(int, input().split()))
    x = gcd(A, B)
    x = gcd(x, C)
    print(A // x + B // x + C // x - 3)


if __name__ == "__main__":
    main()
