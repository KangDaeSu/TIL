'''
3
3
1 2 3
5
1 1 1 2 3
8
1 2 3 4 5 6 7 8
'''
# 당근
# S, M 을 구분짓는 경계 =>
# a 범위는 : 0 ~ N-3 S = [0:a+1]
# M, L을 구분짓는 경계 =>
# b 범위는 : a+1 ~ N-2
# M = [a+1:b+1]
# L = [b+1:N]
# original = [1, 2, 3, 4, 5, 6, 7, 8]
# counts = [0] * 50
# for v in original:
#     counts[v] += 1
# for a in range(0, N-2):
#     for b in range(a+1, N-1):
#         S = lst[0:a+1]
#         M = lst[a+1:b+1]
#         L = lst[b+1:N]




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Ci = list(map(int, input().split()))

    counts = [0] * 1001
    for v in Ci:
        counts[v] += 1
    
    minV = min(Ci)
    maxV = max(Ci)
    result = 10000000
    for a in range(minV, maxV-1):
        for b in range(a+1, maxV):
            S = sum(counts[minV:a+1])
            M = sum(counts[a+1:b+1])
            L = sum(counts[b+1:maxV+1])

            if  S == 0 or M == 0 or L == 0:     # 하나라도 빈 곳이 있으면:
                continue
            if  S > N//2 or M > N//2 or L > N//2:   # 하나라도 N//2 보다 큰 것이 있으면:
                continue
            
            d = max(S, M, L) - min(S, M, L)
            if result > d:
                result = d
    
    if result == 10000000:
        result = -1
    
    print(f'#{tc} {result}')