import sys
sys.stdin = open("1238.txt", "r")

def bfs(start):
    visited = [0] * 101
    q = [start]
    visited[start] = 1
    while q:
        lst = []
        for _ in range(len(q)):
            v = q.pop(0)
            lst.append(v)
            for w in graph[v]:
                if visited[w] == 0:
                    q.append(w)
                    visited[w] = 1
    return lst


T = 10
for tc in range(1, T+1):
    N, start = map(int, input().split())
    arr = list(map(int, input().split()))

    graph = [[] for _ in range(101)]
    for i in range(0, N, 2):
        v1, v2 = arr[i], arr[i+1]
        graph[v1].append(v2)

    result = bfs(start)
    sumV = 0
    for i in result:
        if sumV < i:
            sumV = i
    # result = max(bfs(start))
    print(f'#{tc} {sumV}')