import sys
sys.stdin = open("18352.txt", "r")

def getMaxCnt(r, c):
    cnt = 0
    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        newR = r+dr
        newC = c+dc
        if 0 <= newR < N and 0 <= newC < M:
            if arr[newR][newC] > arr[r][c]:
                cnt += 1
    return cnt

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    resultC = 0
    resultMin = 100 * N * M
    for r in range(N):
        for c in range(M):
            if getMaxCnt(r, c) == 4:
                resultC += 1
                if resultMin > arr[r][c]:
                    resultMin = arr[r][c]

    if resultC == 0:
        resultMin = -1
    print(f'#{tc} {resultC} {resultMin}')