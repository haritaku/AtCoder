import sys

input = sys.stdin.readline

N = int(input())
a_arr = list(map(int, input().split()))

ans = cnt = 0
for i, a in enumerate(a_arr, start=1):
    if a == i:
        cnt += 1
    else:
        if i < a and a_arr[a - 1] == i:
            ans += 1

ans += cnt * (cnt - 1) // 2
print(ans)
