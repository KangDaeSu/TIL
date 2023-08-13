import sys
sys.stdin = open("1219.txt", "r")

def dfs(s,g):
    visited = [False] * 100
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

T = 10
for _ in range(1, T+1):
    S, G = 0, 99
    tc, N = map(int, input().split())
    lst = list(map(int, input().split()))
    
    graph = [[] for _ in range(100)]
    for idx in range(0, len(lst), 2):
        v1, v2 = lst[idx], lst[idx+1]
        graph[v1].append(v2)
    result = dfs(S,G)

    print(f'#{tc} {result}')


