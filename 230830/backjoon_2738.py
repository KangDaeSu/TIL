N, M = map(int, input().split())
lstA = [list(map(int, input().split())) for _ in range(N)]
lstB = [list(map(int, input().split())) for _ in range(N)]


for r in range(N):
    for c in range(M):
        res = lstA[r][c] + lstB[r][c]
        print(res, end=' ')
    print()

