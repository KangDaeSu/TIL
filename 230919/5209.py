import sys
sys.stdin = open('input.txt', 'r')

def subset(row, cursum):
    global res
    if res <= cursum:
        return
    if row == N:
        res = cursum
        return

    for col in range(N):
        if not used[col]:
            used[col] = True
            subset(row+1, cursum+lst[row][col])
            used[col] = False


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    used = [False] * N
    res = 100**3
    subset(0, 0)
    print(f'#{tc} {res}')