import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(s):
    global cnt
    visited[s] = cnt
    G[s].sort()
    for i in G[s]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)

N, M, R = map(int, input().split())

G = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

cnt = 1
visited = [0] * (N+1)
dfs(R)
for i in range(1, N+1):
    print(visited[i])














