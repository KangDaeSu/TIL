# 숫자 만들기

import sys
sys.stdin = open('input.txt', 'r')

def solve(k, value):
    global maxv, minv

    if k == N-1:
        maxv = max(maxv, value)
        minv = min(minv, value)
        return

    if ops[0]:
        ops[0] -= 1
        solve(k + 1, value + num_lst[k+1])
        ops[0] += 1

        # new_ops = [ops[0]-1, ops[1], ops[2], ops[3]]
        # solve(k + 1, new_ops, value + num_lst[k + 1])

    if ops[1]:
        ops[1] -= 1
        solve(k + 1, value - num_lst[k+1])
        ops[1] += 1

    if ops[2]:
        ops[2] -= 1
        solve(k + 1, value * num_lst[k+1])
        ops[2] += 1

    if ops[3]:
        ops[3] -= 1
        solve(k + 1, int(value / num_lst[k+1]))
        ops[3] += 1

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ops = list(map(int, input().split()))
    num_lst = list(map(int, input().split()))

    maxv = -1e9
    minv = 1e9
    solve(0, num_lst[0])
    res = maxv - minv

    print(f'#{tc} {res}')