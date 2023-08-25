# 진기의 최고급 붕어빵

import sys
sys.stdin = open("1860.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split()) #N : 손님 수, M 초마다 K개 생산
    time = list(map(int, input().split()))  # N 명이 각각 도착하는 시간
    time.sort() # 도착시간 순으로 정렬
    # i 손님이 붕어빵을 사려면, 도착시간 time[i]까지의 누적 손님수 <= arr[i] 시간까지의 생산량
    # 시간 * 단위 시간 생산량 = 총 생산량
    # time[i] // N * K
    result = 'Possible'
    for i in range(N):
        if i+1 > time[i]//M*K:
            result = 'Impossible'
            break
    
    print(f'#{tc}{result}')