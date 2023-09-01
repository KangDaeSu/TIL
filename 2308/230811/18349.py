T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    R, C = map(int, input().split())
    result = 0
    arr[R][C] = 1
    for r in range(1, N-1):
        for c in range(1, N-1):
            if arr[r][c] == 2:
                cnt = 0
                for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    newR = r + dr
                    newC = c + dc
                    if arr[newR][newC] == 1:
                        cnt += 1
                        if cnt == 4:
                            result += 1
    print(f'#{tc} {result}')