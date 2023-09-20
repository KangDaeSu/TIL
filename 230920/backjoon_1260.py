import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

def dfs(start):
    print(start, end=' ')
    visited[start] = True
    for w in sorted(G[start]):
        if not visited[w]:
            dfs(w)

def bfs(start):
    visited = [False] * (N+1)
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        print(v, end=' ')
        for w in sorted(G[v]):
            if not visited[w]:
                q.append(w)
                visited[w] = True


N, M, v = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    v1, v2 = map(int, input().split())
    G[v1].append(v2)
    G[v2].append(v1)

visited = [False] * (N+1)
dfs(v)
print()
bfs(v)

