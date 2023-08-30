import sys
sys.stdin = open("5188.txt", "r")

def move(start, sumV):
    global res
    if res != -1:
        if res < sumV:
            return
    (r, c) = start
    if (r, c) == (N-1, N-1):
        if res == -1:
            res = sumV
        if res > sumV:
            res = sumV
        return
    if r+1 < N:
        move((r+1, c), sumV+arr[r+1][c])
    if c+1 < N:
        move((r, c+1), sumV+arr[r][c+1])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    start = (0, 0)
    sumV = arr[0][0]
    res = -1
    move(start, sumV)
    print(f'#{tc} {res}')