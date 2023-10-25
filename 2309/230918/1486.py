# 장훈이의 높은 선반

import sys
sys.stdin = open('1486_input.txt', 'r')

def subject(i, cur_sum):
    global min_sum
    if min_sum < cur_sum:
        return
    if i == N:
        if B <= cur_sum and cur_sum < min_sum:
            min_sum = cur_sum
        return
    bit[i] = 1
    subject(i + 1, cur_sum + lst[i])
    bit[i] = 0
    subject(i + 1, cur_sum)

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))
    min_sum = sum(lst)

    bit = [0] * N
    subject(0, 0)
    res = min_sum - B
    print(f'#{tc} {res}')