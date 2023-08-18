# 노드의 거리
import sys
sys.stdin = open("5102.txt", "r")

def bfs(start, goal):
    visited = [-1] * (V+1)
    q = []
    q.append(start)
    visited[start] = 0

    while q:
        v = q.pop(0)
        if v == goal:
            return visited[v]

        for w in graph[v]:
            if visited[w] == -1:
                q.append(w)
                visited[w] = visited[v] + 1
    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)
    S, G = map(int, input().split())

    result = bfs(S, G)
    print(f'#{tc} {result}')