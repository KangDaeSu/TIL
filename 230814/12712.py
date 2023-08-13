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
    for r1 in range(N):
        for c1 in range(N):
            my_sum1 = arr[r1][c1]
            my_sum2 = arr[r1][c1]
            for l1 in range(1, M):
                for k1 in range(4):
                    newR1 = r1 + dr1[k1] * l1
                    newC1 = c1 + dc1[k1] * l1
                    newR2 = r1 + dr2[k1] * l1
                    newC2 = c1 + dc2[k1] * l1
                    if 0 <= newR1 < N and 0 <= newC1 < N:
                        my_sum1 += arr[newR1][newC1]
                    if 0 <= newR2 < N and 0 <= newC2 < N:
                        my_sum2 += arr[newR2][newC2]
                if max_sum < my_sum1:
                    max_sum = my_sum1                    
                if max_sum < my_sum2:
                    max_sum = my_sum2

    result = max_sum
    print(f'#{tc} {result}')
    