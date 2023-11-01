T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    maxV = 0
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    res = 0
    for r in range(N):
        for c in range(M):
            maxV = arr[r][c]
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 <= nr < N and 0 <= nc < M:
                    maxV += arr[nr][nc]
            if res < maxV:
                res = maxV
    print(f'#{tc} {res}')