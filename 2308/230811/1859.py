# 백만장자

import sys
sys.stdin = open("1859.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))

    result = 0
    # s = 0
    # p = 0
    # max_v = price[s]
    # buy = 0
    #
    # while s < date:
    #     # p = s, N-1 지점사이에 최대값이 있는 위치를 구한다.
    #     for i in range(s, date):
    #         if max_v < price[i]:
    #             max_v = price[i]
    #             p = i
    #     # buy = s에서 p-1까지의 합을 구한다.
    #             buy += price[p]
    #             sell = (p-s) * price[p]
    #             s = p+1
    #     result += sell - buy


    curM = prices[N-1]
    for idx in range(N-2, -1, -1):
        if curM > prices[idx]:
            result += curM - prices[idx]
        else:
            if curM < prices[idx]:
                curM = prices[idx]
    print(f'#{tc} {result}')