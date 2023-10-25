T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    mins = 999999999999
    maxs = 0
    for i in range(N-M+1):
        cursum = 0
        for j in range(M):
            cursum += arr[i + j]
        if mins > cursum:
            mins = cursum
        if maxs < cursum:
            maxs = cursum

    result = maxs - mins
    print(f'#{tc} {result}')