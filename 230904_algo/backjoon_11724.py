import sys
sys.stdin = open("input.txt", "r")

def dfs(s):
    ST = [s]
    visited[s] = True
    while ST:
        v = ST.pop()
        for w in G[v]:
            if not visited[w]:
                ST.append(w)
                visited[w] = True


N, M = map(int, input().split())

G = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

visited = [False] * (N + 1)
count = 0

for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        count += 1
print(count)



