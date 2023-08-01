import sys
sys.stdin = open("4835.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    lst = []

    for i in range(N-M+1):
        sum_arr = 0
        for j in range(i, i+M):
            sum_arr += arr[j]
        lst.append(sum_arr)

    maxL = lst[0]
    minL = lst[0]
    for l1 in lst:
        if maxL < l1:
            maxL = l1
        if minL > l1:
            minL = l1

    result = maxL - minL
    print(f'#{tc} {result}')
