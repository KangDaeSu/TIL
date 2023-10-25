# 인수의 생일 파티

import sys
sys.stdin = open('input.txt', 'r')
import heapq

def dijkstra(s):
    move = []

    heapq.heappush(move, (0, s))
    distance[s] = 0

    while move:
        dist, now = heapq.heappop(move)

        if distance[now] < dist:
            continue

        for next in graph[now]:
            next_node = next[0]
            cost = next[1]

            new_cost = dist + cost

            if distance[next_node] <= new_cost:
                continue

            distance[next_node] = new_cost
            heapq.heappush(move, (new_cost, next_node))


T = int(input())

for tc in range(1, T+1):
    N, M, X = map(int, input().split())


    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        x, y, c = map(int, input().split())
        graph[x].append([y, c])
    # print(graph)

    v = int(1e9)
    distance = [v] * (N + 1)
    res = 0
    for i in range(1, N+1):
        if i == X:
            continue

        distance = [v] * (N + 1)
        dijkstra(i)
        # print(distance)
        sumv = distance[X]
        distance = [v] * (N + 1)
        dijkstra(X)
        # print(distance)
        sumv += distance[i]
        if res < sumv:
            res = sumv
    print(f'#{tc} {res}')
