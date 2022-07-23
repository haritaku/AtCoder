import sys
from collections import deque


def bfs(n):
    dist = [-1] * N
    dist[n] = 0
    q = deque([n])

    max_nd = [0, 0]  # [node number, distance]
    while q:
        u = q.popleft()
        for next_u in adj_list[u]:
            if dist[next_u] == -1:
                dist[next_u] = dist[u] + 1
                q.append(next_u)

                if dist[next_u] > max_nd[1]:
                    max_nd = [next_u, dist[next_u]]
    return max_nd


input = sys.stdin.readline
INF = 10**18

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N - 1)]

adj_list = [[] for _ in range(N)]
for a, b in AB:
    adj_list[a - 1].append(b - 1)
    adj_list[b - 1].append(a - 1)

n1, d1 = bfs(0)
n2, d2 = bfs(n1)
print(d2 + 1)
