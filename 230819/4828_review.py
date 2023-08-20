T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    maxN = arr[0]
    minN = arr[0]
    for i in arr:
        if maxN < i:
            maxN = i
        if minN > i:
            minN = i
    result = maxN - minN
    print(f'#{tc} {result}')