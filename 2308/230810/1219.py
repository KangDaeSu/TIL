import sys
sys.stdin = open("1219.txt", "r")

def dfs(s, e):
    ST = []
    visited = [0] * (101)
    ST.append(s)
    visited[s] = 1
    while ST:
        v = ST.pop()
        if v == e:
            return 1
        for w in G[v]:
            if not visited[w]:
                ST.append(w)
                visited[w] = 1
    return 0

for _ in range(10):
    tc, N = map(int, input().split())
    arr = list(map(int, input().split()))

    S = 0
    E = 99
    G = [[] for _ in range(100)]
    for idx in range(0, len(arr), 2):
        v1 = arr[idx]
        v2 = arr[idx+1]
        G[v1].append(v2)

    result = dfs(S, E)
    print(f'#{tc} {result}')