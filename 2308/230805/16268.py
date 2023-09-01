import sys
sys.stdin = open("16268.txt", "r")

T = int(input())

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    max_v = 0
    for i in range(N):
        for j in range(M):
            cnt = arr[i][j]
            for r in range(4):
                ni, nj = i+di[r], j+dj[r]
                if 0 <= ni < N and 0 <= nj < M:
                    cnt += arr[ni][nj]
                    
            if max_v < cnt:
                max_v = cnt
    print(f'#{tc} {max_v}')
