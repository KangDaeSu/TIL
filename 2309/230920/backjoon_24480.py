import sys
sys.stdin = open('input.txt', 'r')

def dfs(s):
    visited[s] = 1
    stack = [s]
    while stack:
        v = stack.pop()
        print(v)
        lst = sorted(G[v])
        for w in lst:
            if visited[w] == 0:
                stack.append(w)
                visited[w] = 1
N, M, R = map(int, input().split())

G = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

visited = [0] * (N+1)


dfs(R)
for i in range(1, N+1):
    if visited[i] == 0:
        print(0)

