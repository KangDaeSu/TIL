# 정사각형 방
import sys
sys.stdin = open("input.txt", "r")

# 1
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = 0
    max_start = 0
    for p in range(N):
        for q in range(N):
            i, j = p, q
            cnt = 1
            start = arr[i][j]

            while True:
                for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < N and arr[i][j] + 1 == arr[ni][nj]:
                        cnt += 1
                        i, j = ni, nj
                        break
                else:
                    break
            if max_cnt < cnt:
                max_cnt = cnt
                max_start = start
            elif max_cnt == cnt and max_start > start:
                max_start = start

    print(f'#{tc} {max_start} {max_cnt}')


# 2 (실행속도 개선)
didj = [(0, 1), (0, -1), (1, 0), (-1, 0)]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = [0] * (N * N + 1)  # 연속으로 1이 커지는 경우를 표시할 배열
    for i in range(N):
        for j in range(N):
            for di, dj in didj:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N and arr[i][j] + 1 == arr[ni][nj]:
                    cnt[arr[i][j]] = 1
    max_cnt = 0
    max_start = 0
    c = 0
    for k in range(N * N, 0, -1):
        if cnt[k]:
            c += 1
            if max_cnt < c:
                max_cnt = c
                max_start = k
            elif max_cnt == c:
                max_start = k
        else:  # ones[k]가 0이면
            c = 0
    print(f'#{tc} {max_start} {max_cnt + 1}')


# # 3 dfs 재귀
def dfs(r, c, value):
    # if memo[r][c] > 0:
    #     return memo[r][c]

    t = 0
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        newR = r + dr
        newC = c + dc
        if 0 <= newR < N and 0 <= newC < N and value+1 == ROOM[newR][newC]:
            t = dfs(newR, newC, value+1)
    # memo[newR][newC] = t+1
    return t + 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ROOM = [list(map(int, input().split())) for _ in range(N)]

    maxC = 0
    for r in range(N):
        for c in range(N):
            cnt = dfs(r, c, ROOM[r][c])
            if cnt > maxC:
                maxC = cnt
                maxV = ROOM[r][c]
            elif cnt == maxC and maxV > ROOM[r][c]:
                maxV = ROOM[r][c]
                
    print(f'#{tc} {cnt} {maxC}')