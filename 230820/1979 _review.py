# 어디에 단어가 들어갈 수 있을까
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cntA = 0
    for r in range(N):
        cnt =0
        for c in range(N):
            if arr[r][c] == 1:
                cnt += 1
            elif arr[r][c] == 0:
                if cnt == K:
                    cntA += 1
                cnt = 0
        if cnt == K:
            cntA += 1
    for r in range(N):
        cnt = 0
        for c in range(N):
            if arr[c][r] == 1:
                cnt += 1
            elif arr[c][r] == 0:
                if cnt == K:
                    cntA += 1
                cnt = 0
        if cnt == K:
            cntA += 1
    result = cntA
        
    print(f'#{tc} {result}')