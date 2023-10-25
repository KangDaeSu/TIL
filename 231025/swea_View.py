T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    cnt = 0
    for i in range(2, N-2):
        Max_b = max(arr[i-2], arr[i-1], arr[i+1], arr[i+2])
        if arr[i] > Max_b:
            cnt += (arr[i] - Max_b)
    print(f'#{tc} {cnt}')