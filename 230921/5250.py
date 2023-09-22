# 최소 비용

import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

def solve(s):
    sr, sc = s
    visited[sr][sc] = 0
    q = deque([(sr, sc)])
    while q:
        v1, v2 = q.popleft()
        for r, c in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr = v1 + r
            nc = v2 + c
            if 0 <= nr < N and 0 <= nc < N:
                high = 0
                if lst[nr][nc] > lst[v1][v2]:
                    high = lst[nr][nc] - lst[v1][v2]

                new_visited = visited[v1][v2] + 1 + high
                if visited[nr][nc] > new_visited:
                    visited[nr][nc] = new_visited
                    q.append((nr, nc))


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    start = (0, 0)
    v = int(1e9)
    visited = [[v] * N for _ in range(N)]
    solve(start)
    print(f'#{tc} {visited[N-1][N-1]}')
