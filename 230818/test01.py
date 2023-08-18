# q = [4] => 4
# q = [2, 6] => 2
# q = [6, 1, 5] =>6
# q = [1, 5, 7] => 1
# q = [5, 7, 3] => 5
# q = [7, 3] => 7
# q = [3] => 3
# q = []

# 1차원 bfs
def bfs(s):
    Q = []
    visited = [0] * (N+1)
    Q.append(s)
    visited[s] = 1
    
    while Q:
        v = Q.pop(0)
        print(v)

        for w in G[v]: # => 연결되어 있는 좌표
            if visited[w] == 0: # => 좌표 범위 체크, 연결된 좌표 중 1이 아닌 것들, 방문여부
                Q.append(w)
                visited[w] = visited[v] + 1
    print(visited)

# 2차원 bfs
def bfs(sr, sc):
    Q = []
    visited = [[False] * (N+1) for _ in range(N+1)]
    
    Q.append((sr, sc, 0))
    visited[sr][sc] = True
    while Q:
        vr, vc, dis = Q.pop(0)
        print(vr, vc, arr[vr][vc])

        for dr, dc in [(0,1), (0, -1), (1, 0), (-1, 0)]: # => 연결되어 있는 좌표
            if .... : # => 좌표 범위 체크, 연결된 좌표 중 1이 아닌 것들, 방문여부
                nr = 
                nc = 
                Q.append((nr, nc, dis+1))
                visited[nr][nc] = True
    print(visited)

#dfs
def dfs(s):
    ST = []
    visited = [False] * (N+1)

    ST.append(s)
    while ST:
        v = ST.pop()
        if not visited[v]:
            visited[v] = True
            print(v)

            for w in G[v]: 
                if not visited[w]:
                    ST.append(w)



s = '1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7'
lst = list(map(int, s.split(',')))

N = 7
# G = [[], [2, 3], [1, 4], [1, 7], [2, 6], [2, 6], [4, 5, 7], [3, 6]]
G = [[] * (N+1) for _ in range(N+1)]
for i in range(0, len(lst), 2):
    v1 = lst[i]
    v2 = lst[i+1]
    G[v1].append(v2)
    G[v2].append(v1)
print(G)
bfs(1)
print('----------------------')
dfs(4)