# 파리퇴치
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    max_sum = 0
    for r in range(N-M+1):
        for c in range(N-M+1):
            sumV = 0
            for i in range(M):
                for j in range(M):
                    newR = r + i
                    newC = c + j
                        
            if max_sum < sumV:
                max_sum = sumV
    result = max_sum
    print(f'#{tc} {result}')
