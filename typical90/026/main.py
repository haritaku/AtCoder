import sys

input = sys.stdin.readline

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N - 1)]

adj_list = [[] for _ in range(N)]
for a, b in AB:
    adj_list[a - 1].append(b - 1)
    adj_list[b - 1].append(a - 1)

stack = [[0, 0]]
searched = [False] * N
searched[0] = True

odd = []
even = []

while stack:
    curr_node, color = stack.pop()

    for next_node in adj_list[curr_node]:
        if searched[next_node]:
            continue
        searched[next_node] = True

        next_color = (color + 1) % 2
        if next_color % 2 == 0:
            even.append(next_node + 1)
        else:
            odd.append(next_node + 1)
        stack.append([next_node, next_color])

if len(odd) > len(even):
    print(*odd[: N // 2])
else:
    print(*even[: N // 2])
