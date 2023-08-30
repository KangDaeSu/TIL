import sys
sys.stdin = open("5188.txt", "r")

def solve(r, c, sumV):
    global result
    if result < sumV:
        return

    if r == N-1 and c == N-1:
        if result > sumV:
            result = sumV
        return

    if c < N-1:
        solve(r, c+1, sumV + ARR[r][c+1])
    if r < N-1:
        solve(r+1, c, sumV + ARR[r+1][c])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ARR = [list(map(int, input().split())) for _ in range(N)]

    result = 99999999

    solve(0, 0, ARR[0][0])
    print(f'#{tc} {result}')