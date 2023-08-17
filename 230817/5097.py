import sys
sys.stdin = open("5097.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    Q = arr
    for _ in range(M):
        v = Q.pop(0)
        Q.append(v)
    print(f'#{tc} {Q[0]}')


