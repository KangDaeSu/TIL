import sys
sys.stdin = open("4871.txt", "r")

def dfs(s,g):
    ST=[]
    visited = [False] * (V+1)
    ST.append(s)
    visited[s] = True
    while ST:
        v = ST.pop()
        if v == g:
            return 1
        for w in G[v]:
            if not visited[w]:
                ST.append(w)
                visited[w] = True
    return 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())    # V : 노드의 개수, E : 간선의 개수
    info = [list(map(int, input().split())) for _ in range(E)]   # 출발, 도착 노드로 간선의 정보
    S, e = map(int, input().split())    # 경로의 존재를 확인할 출발 노드 S, 도착 노드 G

    lst = []
    for i in info:
        lst.extend(i)
    G = [[] for _ in range(V+1)]
    for idx in range(0, len(lst), 2):
        v1 = lst[idx]
        v2 = lst[idx+1]
        G[v1].append(v2)
    result = dfs(S, e)

    print(f'#{tc} {result}')
