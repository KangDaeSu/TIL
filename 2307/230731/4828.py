import sys
sys.stdin = open("4828input.txt", "r")

T = int(input()) # 테이스케이스 개수

for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_v = arr[0]
    min_v = arr[0]
    for i in range(1, N):
        if max_v < arr[i]: # max와 arr의 값을 비교하여 arr의 값이 크면 max에 저장
            max_v = arr[i]
        if min_v > arr[i]: # min와 arr의 값을 비교하여 arr의 값이 작으면 min에 저장
            min_v = arr[i]
    ans = max_v - min_v

    print(f'#{test_case} {ans}')


