def check():
        # STOPS의 간격이 K보다 크면 결과가 0
    for st in range(M+1):
        if STOPS[st+1] - STOPS[st] > K:
            return 0
    lastStop = 0
    cnt = 0
    for s in range(1, M+2):
        if lastStop + K < STOPS[s]:
            lastStop = STOPS[s-1]
            cnt += 1



T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    STOPS = [0] + list(map(int, input().split())) + [N]

    print('f#{tc} {check()}')
