import sys

input = sys.stdin.readline


N = int(input())
S = input()
W = list(map(int, input().split()))

SW = [(s, w) for s, w in zip(S, W)]
SW = sorted(SW, key=lambda x: x[1])

ans = num = S.count("1")
for i in range(N):
    num = num + 1 if SW[i][0] == "0" else num - 1

    if i == N - 1:
        ans = max(ans, num)
        continue

    if SW[i + 1][1] == SW[i][1]:
        continue
    else:
        ans = max(ans, num)

print(ans)
