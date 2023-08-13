import sys
sys.stdin = open("9490.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(N, M, arr)

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    max_sum = 0
    
    for r in range(N):
        for c in range(M):
            my_sum = arr[r][c]
            for l in range(1, my_sum+1):
                for k in range(4):
                    newR = r+dr[k] * l
                    newC = c+dc[k] * l
                    if 0 <= newR < N and 0 <= newC < M:
                        my_sum += arr[newR][newC]
            if max_sum < my_sum:
                max_sum = my_sum
    print(f'#{tc} {max_sum}')