import sys
sys.stdin = open("4837.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    
    result = 0
    for i in range(1<<12):
        sumV = 0
        cnt = 0
        for j in range(12):
            if i & (1<<j):
                sumV += arr[j]
                cnt += 1
        if cnt == N and sumV == K:
            result += 1
        
    print(f'#{tc} {result}')
 