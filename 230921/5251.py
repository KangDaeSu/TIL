import sys
sys.stdin = open('input.txt', 'r')

def dijkstra(s):
    U = []
    D = [1000000] * (N+1)

    D[s] = 0
    for _ in range(N):
        minv = 1000000
        for i in range(N+1):
            if i in U:
                continue
            if D[i] < minv:
                minv = D[i]
                curN = i

        U.append(curN)

        for i in range(N):
            if G[curN][i] == 0:
                continue

            if D[i] > D[curN] + G[curN][i]:
                D[i] = D[curN] + G[curN][i]

    print(U)


T = int(input())

for tc in range(1, T+1):
    N, E = map(int, input().split())

    G = [[0] * (N+1) for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        G[s][e] = w

    dijkstra(0)