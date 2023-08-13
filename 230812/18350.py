import sys
sys.stdin = open("18350.txt", "r")

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    result = 1
    cnt = 0
    for i in range(N):
        for j in range(M):
            for k in range(4):
                newR = i + dr[k]
                newC = j + dc[k]
                if 0 <= newR < N and 0 <= newC < M:
                    if arr[i][j] == 1 and arr[newR][newC] == 1:
                        cnt += 1
                        if cnt > 0:
                            result = 0

    print(f'#{tc} {result}')

            
