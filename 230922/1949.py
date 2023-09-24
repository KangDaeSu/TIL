# 등산로 조성

import sys
sys.stdin = open('input.txt', 'r')

def solve(r, c, curV, cnt, isCut):
    global maxC
    for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        nr = r + dr
        nc = c + dc
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            # 커팅 한 경우, 안한 경우
            if curV > maps[nr][nc]:
                visited[nr][nc] = 1
                solve(nr, nc, maps[nr][nc], cnt + 1, isCut)
                visited[nr][nc] = 0

            elif not isCut and curV > maps[nr][nc] - K:
                visited[nr][nc] = 1
                solve(nr, nc, curV - 1, cnt + 1, True)
                visited[nr][nc] = 0
        
        if maxC < cnt:
            maxC = cnt
            
            
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0] * N for _ in range(N)]

    maxC = 0
    # 2차원 배열의 최대값(max 함수 사용)
    hightest = max(map(max, maps))
    for row in range(N):
        for col in range(N):
            if maps[row][col] == hightest:
               visited[row][col] = 1
                # row, col, 현재의 값, 경로길이, 공사여부
               solve(row, col, maps[row][col], 0, False)
               visited[row][col] = 0

    print(f'#{tc}', maxC + 1)