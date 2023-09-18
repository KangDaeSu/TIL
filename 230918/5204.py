# 병합 정렬

import sys
sys.stdin = open('input.txt', 'r')

def merge(l, r):
    result = []
    lp = rp = 0
    global cnt
    if l[-1] > r[-1]:
        cnt += 1
    while lp < len(l) and rp < len(r):
        if l[lp] < r[rp]:
            result.append(l[lp])
            lp += 1
        else:
            result.append(r[rp])
            rp += 1

    result += l[lp:]
    result += r[rp:]

    return result

def merge_sort(lst):
    n = len(lst)

    if n == 1:
        return lst

    m = n // 2

    left_lst = merge_sort(lst[:m])
    right_lst = merge_sort(lst[m:])

    return merge(left_lst, right_lst)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    cnt = 0
    res = merge_sort(lst)
    result = res[N//2]
    print(f'#{tc} {result} {cnt}')