import sys
sys.stdin = open("4871.txt", "r")

def dfs(s, g):
    visited = [False] * (V+1)
    stack = [s]
    visited[s] = True
    while stack:
        v = stack.pop()
        if v == g:
            return 1
        for w in graph[v]:
            if not visited[w]:
                stack.append(w)
                visited[w] = True
    return 0 


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())

    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int, input().split())
        graph[s].append(e)
    
    S, G = map(int, input().split())
    result = dfs(S, G)
    print(f'#{tc} {result}')