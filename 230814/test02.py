def dfs(s,g):
    visited = [False] * (V+1)
    stack=[s]
    visited[s] == True
    while stack:
        v = stack.pop()
        if v == g:
            return 1
        for w in graph[v]:
            if not visited[w]:
                stack.append(w)
                visited[w] = True
    retrun 0
