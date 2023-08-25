# 홈 방범 서비스
import sys
sys.stdin = open("2117.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 1. 집의 좌표만 수집
    home = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                home.append((i, j))

    # 2. 전체 좌표를 기준으로
    for r in range(N):
        for c in range(N):
            # 좌표별 거리의 conunts 배열을 만든다.
            dist = [0] * (2*N+1)
            for hr, hc in home:
                dis
            for k in range(2N+1):
                # 각 거리별 금액을 계산
                # 거리 내의 집의 수는
                cnt = sum(dis[:k+1])
