#!/usr/bin/env python3


def main():
    N = int(input())
    S = [input() for _ in range(N)]

    unique_users = set()
    for i, user in enumerate(S, start=1):
        if user in unique_users:
            continue
        unique_users.add(user)
        print(i)


if __name__ == "__main__":
    main()
