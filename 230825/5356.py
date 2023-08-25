# 의석이의 세로로 말해요
import sys
sys.stdin = open("5356.txt", "r")

T = int(input())
for tc in range(1, T+1):
    l_arr = 0

    arr = [list(map(str, input())) for _ in range(5)]
    for i in range(5):
        if len(arr[i]) > l_arr:
            l_arr = len(arr[i])

    lst = ''
    for c in range(l_arr):
        for r in range(5):
            if len(arr[r]) >= c + 1:
                lst += arr[r][c]
    print(f'#{tc} {lst}')
