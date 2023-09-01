import sys
sys.stdin = open("2001.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    
    max_sum = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            sumM = 0
            for r in range(i, i+M):
                for c in range(j, j+M):
                    sumM += arr[r][c]
                if max_sum < sumM:
                    max_sum = sumM
    print(f'#{tc} {max_sum}')
                
