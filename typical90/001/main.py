import sys


def binary_search(ng, ok, check):
    while abs(ok - ng) > 1:
        mid = (ng + ok) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid
    return ok


def check(x):
    num = 0
    before = 0
    for a in A:
        if a - before >= x:
            num += 1
            before = a
    if L - before >= x:
        num += 1

    return num >= K + 1


input = sys.stdin.readline

N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

ans = binary_search(L + 1, 0, check)
print(ans)
