T = int(input())
for tc in range(1, T+1):
    cnt = 0
    sumV = [[0] * 10 for _ in range(10)]
    N = int(input())
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                sumV[r][c] += color
                if sumV[r][c] == 3:
                    cnt += 1
    print(f'#{tc} {cnt}')