# IM 대비 기지국
import sys
sys.stdin = open("13976.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(N + 1)]

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    cnt = 0
    for r in range(N + 1):
        for c in range(N):
            if arr[r][c] == 'A':    # A 기지국을 발견 했을 때
                for l in range(1, 2):
                    for k in range(4):
                        newR = r + dr[k] * l
                        newC = c + dc[k] * l
                        if 0 <= newR < N + 1 and 0 <= newC < N:
                            arr[newR][newC] = 'X'
            if arr[r][c] == 'B':    # B 기지국을 발견 했을 때
                for l in range(1, 3):
                    for k in range(4):
                        newR = r + dr[k] * l
                        newC = c + dc[k] * l
                        if 0 <= newR < N + 1 and 0 <= newC < N:
                            arr[newR][newC] = 'X'
            if arr[r][c] == 'C':    # C 기지국을 발견 했을 때
                for l in range(1, 4):
                    for k in range(4):
                        newR = r + dr[k] * l
                        newC = c + dc[k] * l
                        if 0 <= newR < N + 1 and 0 <= newC < N:
                            arr[newR][newC] = 'X'

    for i in range(N+1):    # 모든 과정이 끝나고 전체 범위를 탐색하여 커버 되지 않는 집의 개수를 구함
        for j in range(N):
            if arr[i][j] == 'H':
                cnt += 1
    print(f'#{tc} {cnt}')
