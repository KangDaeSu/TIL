import sys
sys.stdin = open("4861.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lstN = [list(input()) for _ in range(N)]
    
    result = 0
    # 가로
    for r in range(N):
        for c in range(N-M+1): # N에서 M의 크기만큼 반복
            strP = ''
            for k in range(M):
                strP += lstN[r][c+k]
        if strP == strP[::-1]: # 회문 여부
            result = strP
       
    # 세로   
    for r in range(N):
        for c in range(N-M+1):# N에서 M의 크기만큼 반복
            strP = ''
            for k in range(M):
                strP += lstN[c+k][r]
        if strP == strP[::-1]: # 회문 여부
            result = strP

    print(f'#{tc} {result}')


            
