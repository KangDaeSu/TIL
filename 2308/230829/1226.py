import sys
sys.stdin = open("1226.txt", "r")

def bfs(start, N):
    start_r, start_c = start
    visited = [[False] * N for _ in range(N)]
    Q = [(start)]
    visited[start_r][start_c] = True
    result = 1
    while Q:
        r, c = Q.pop(0)
        if arr[r][c] == 3:
            return result
        for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            newR = r + dr
            newC = c + dc
            if 0 <= newR < N and 0 <= newC < N and arr[newR][newC] != 1 and visited[newR][newC] == False:
                Q.append((newR, newC))
                visited[newR][newC] = True
    return 0
T = 10
for _ in range(1, T+1):
    tc = int(input())
    N = 16
    arr = [list(map(int, input())) for _ in range(16)]

    for r in range(N):
        for c in range(N):
            if arr[r][c] == 2:
                start = (r, c)
    ans = bfs(start, N)
    print(f'#{tc} {ans}')