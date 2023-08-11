# 고대 유적

import sys
sys.stdin = open("9489.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    rows = [list(map(int, input().split())) for _ in range(N)]
    clums = [list(x) for x in zip(*rows)]

    max_v = 0
    for r in rows:
        cnt = 0
        for i in r:
            if i == 1:
                cnt += 1
                if cnt > max_v:
                    max_v = cnt
            else:
                cnt = 0
    for c in clums:
        cnt = 0
        for j in c:
            if j == 1:
                cnt += 1
                if cnt > max_v:
                    max_v = cnt
            else:
                cnt = 0
    print(f'#{tc} {max_v}')

