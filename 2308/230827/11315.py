def findohmok(arr):
    dr = [0, 1, 1, 1]
    dc = [1, 1, 0, -1]

    for r in range(N):
        for c in range(N):
            if arr[r][c] == 'o':
                for k in range(4):
                    count = 1
                    for l in range(1, 5):
                        newR = r + dr[k] * l
                        newC = c + dc[k] * l
                        if 0 <= newR < N and 0 <= newC < N:
                            if arr[newR][newC] == 'o':
                                count += 1
                            else:
                                break
                    else:
                        if count >= 5:
                            return 'YES'
    return 'NO'

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]

    result = findohmok(arr)

    print(f'#{tc} {result}')
