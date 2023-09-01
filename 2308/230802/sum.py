import sys
sys.stdin = open("sum.txt", "r")

T = 10
for tc in range(1, T+1):
    testcase = int(input())
    N = 100
    M = 100
    arr = [list(map(int, input().split())) for _ in range(100)]

    maxR = 0
    for r in range(N):  # 행의 합
        sumR = 0
        for c in range(M):
            sumR += arr[r][c]
        if maxR < sumR:
            maxR = sumR
    
    
    for c in range(M):  # 열의 합
        sumL = 0
        for r in range(N):
            sumL += arr[r][c]
        if maxR < sumL:
            maxR = sumL
    
    
    sumD1 = 0
    sumD2 = 0
    for d1 in range(100):
        sumD1 += arr[d1][d1]
        sumD2 += arr[d1][99-d1]
    
    if maxR < sumD1:
        maxR = sumD1
    
    if maxR < sumD2:
        maxR = sumD2
    
    print(f'#{tc} {maxR}')
   
    





    