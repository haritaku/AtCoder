import sys

input = sys.stdin.readline

N, K = list(map(int, input().split()))


def eight2ten(N: str) -> int:
    ten = 0
    for i, s in enumerate(reversed(N)):
        ten += int(s) * 8**i
    return ten


def ten2nine(N: int) -> str:
    nine = ""
    r = N
    while r:
        r, q = divmod(r, 9)
        nine = str(q) + nine
    return nine if nine != "" else "0"


eight = str(N)
for _ in range(K):
    nine = ten2nine(eight2ten(eight))
    eight = nine.replace("8", "5")


print(eight)
