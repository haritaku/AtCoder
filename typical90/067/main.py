import sys


def deca2nona(N: int) -> str:
    nine = ""
    r = N
    while r:
        r, q = divmod(r, 9)
        nine = str(q) + nine
    return nine if nine != "" else "0"


input = sys.stdin.readline
N, K = list(map(int, input().split()))

octa = str(N)
for _ in range(K):
    nona = deca2nona(int(octa, 8))
    octa = nona.replace("8", "5")
print(octa)
