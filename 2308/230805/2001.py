import sys
sys.stdin = open("2001.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum = 0
            for r in range(i, M+i):
                for c in range(j, M+j):
                    sum += arr[r][c]
                    # print(sum)
            if max_v < sum:
                max_v = sum
    print(f'#{tc} {max_v}')
