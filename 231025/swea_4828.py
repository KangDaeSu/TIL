T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    Max = max(arr)
    Min = min(arr)
    result = Max - Min
    print(f'#{tc} {result}')