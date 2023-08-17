import sys
sys.stdin = open("12712.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr1 = [-1, 0, 1, 0]
    dc1 = [0, 1, 0, -1]
    dr2 = [-1, -1, 1, 1]
    dc2 = [-1, 1, 1, -1]


    max_sum = 0
    for r in range(N):
        for c in range(N):
            sum1 = arr[r][c]
            sum2 = arr[r][c]
            for l in range(1, M):
                for k in range(4):
                    newR1 = r+dr1[k]*l
                    newC1 = c+dc1[k]*l
                    newR2 = r+dr2[k]*l
                    newC2 = c+dc2[k]*l
                    if 0 <= newR1 < N and 0 <= newC1 < N:
                        sum1 += arr[newR1][newC1]
                    if 0 <= newR2 < N and 0 <= newC2 < N:
                        sum2 += arr[newR2][newC2]
            if max_sum < sum1:
                max_sum = sum1
            if max_sum < sum2:
                max_sum = sum2
    print(f'#{tc} {max_sum}')

