# 미로의 거리
import sys
sys.stdin = open("5105.txt", "r")

def start(N):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                return i, j

def bfs(sr, sc, N):
    visited = [[0]*N for _ in range(N)]
    Q = []
    Q.append((sr, sc))
    visited[sr][sc] = 1

    while Q:
        i, j = Q.pop(0)
        if arr[i][j] == 3:
            return visited[i][j]-2
        for di, dj in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 1 and visited[ni][nj] == 0:
                Q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    return 0




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    sti, stj = start(N)
    ans = bfs(sti, stj, N)
    print(f'#{tc} {ans}')