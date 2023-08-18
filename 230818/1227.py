# 미로2
import sys
sys.stdin = open("1227.txt", "r")

def start(N):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                return i, j

def bfs(sti, stj, N):
    q = []
    visited = [[False] * N for _ in range(N)]
    q.append((sti, stj))
    visited[sti][stj] = True
    result = 1
    while q:
        r, c = q.pop(0)
        if arr[r][c] == 3:
            return result
        for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            nr = r+dr
            nc = c+dc
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != 1 and visited[nr][nc] == False:
                q.append((nr, nc))
                visited[nr][nc] = True
    return 0

T = 10
for _ in range(1, T+1):
    tc = int(input())
    arr = [list(map(int, input())) for _ in range(100)]

    N = 100
    sti, stj = start(N)
    ans = bfs(sti, stj, N)

    print(f'#{tc} {ans}')
