T = int(input())
for tc in range(1, T+1):
    nums = int(input())
    arr = list(map(int, input().split()))
    max_idx = 0 # 최대값의 인덱스
    min_idx = 0 # 최소값의 인덱스
    for i in range(1, nums):
        if arr[min_idx] > arr[i]:
            min_idx = i
        if arr[max_idx] <= arr[i]:
            max_idx = i
    print(min_idx)
    print(max_idx)
    if max_idx > min_idx:
        ans = max_idx - min_idx
    # abs(max_idx - min_idx)

