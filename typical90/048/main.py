import sys

input = sys.stdin.readline

N, K = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(N)]

points = []
for ab in AB:
    points.extend([ab[1], ab[0] - ab[1]])
sorted_points = sorted(points, reverse=True)

print(sum(sorted_points[:K]))
