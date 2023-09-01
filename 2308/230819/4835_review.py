# 구간합
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    
    lst = []
    for i in range(N-M+1):
        sumV = 0
        for j in range(i, i+M):
            if i+3 <= N:
                sumV += arr[j]
        lst.append(sumV)
        
    max_sum = lst[0]
    min_sum = lst[0]
    for i in lst:
        if max_sum < i:
            max_sum = i
        if min_sum > i:
            min_sum = i
    result = max_sum - min_sum
    print(f'#{tc} {result}')