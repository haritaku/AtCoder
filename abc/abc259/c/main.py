import sys

input = sys.stdin.readline

S = input().rstrip()
T = input().rstrip()


def rle(string):
    rle_list = []
    for i in range(len(string)):
        if i == 0:
            s, cnt = string[0], 1
            continue

        if string[i] == string[i - 1]:
            cnt += 1
        else:
            rle_list.append((s, cnt))
            s, cnt = string[i], 1

        if i == len(string) - 1:
            rle_list.append((s, cnt))
    return rle_list


S_rle, T_rle = rle(S), rle(T)

if len(S_rle) != len(T_rle):
    print("No")
    sys.exit()

ans = "Yes"
for s_rle, t_rle in zip(S_rle, T_rle):
    if s_rle[0] != t_rle[0]:
        ans = "No"
        break

    if s_rle[1] == t_rle[1]:
        continue
    elif s_rle[1] > 1 and s_rle[1] < t_rle[1]:
        continue
    else:
        ans = "No"
        break
print(ans)
