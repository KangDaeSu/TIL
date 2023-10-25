import sys
input = sys.stdin.readline

def dfs(node, depth):
    global result
    if depth == 5:
        result = 1
        return
    visited[node] = True
    for v in g[node]:
        if not visited[v]:
            dfs(v, depth + 1)
    visited[node] = False


N, M = map(int, input().split())

g = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

visited = [False] * N
result = 0
for i in range(N):
    dfs(i, 1)
    if result == 1:
        break
print(result)