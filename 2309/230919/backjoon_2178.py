import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

def bfs(s):
    q = deque([s])
    sr, sc = s
    visited[sr][sc] = 1
    while q:
        r, c = q.popleft()
        for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and lst[nr][nc] != 0 and visited[nr][nc] == 0:
                q.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1

N, M = map(int, input().split())

lst = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
start = (0, 0)
bfs(start)

print(visited[N-1][M-1])