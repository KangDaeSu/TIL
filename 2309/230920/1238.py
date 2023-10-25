import sys
sys.stdin = open('input.txt', 'r')
from collections import deque
def bfs(s):
    global visited
    q = deque([s])
    visited[s] = 0

    while q:
        v = q.popleft()
        for w in G[v]:
            if visited[w] == -1:
                q.append(w)
                visited[w] = visited[v] + 1


T = 10
for tc in range(1, T+1):
    l_date, start = map(int, input().split())
    lst = list(map(int, input().split()))
    # print(lst)
    G = [[] for _ in range(101)]
    for i in range(0, len(lst), 2):
        v1, v2 = lst[i], lst[i+1]
        G[v1].append(v2)
    # print(G)

    visited = [-1] * 101
    bfs(start)

    max_idx = 0
    max_value = 0
    for i in range(len(visited)):
        if max_value <= visited[i]:
            max_value = visited[i]
            max_idx = i

    print(f'#{tc} {max_idx}')