# 창용 마을 무리의 개수
import sys
sys.stdin = open('input.txt', 'r')

# 스택
def dfs(s):
    stack = [s]
    visited[s] = True

    while stack:
        v = stack.pop()
        for w in graph[v]:
            if visited[w] == False:
                stack.append(w)
                visited[w] = True

# 재귀
def dfs2(s):
    visited[s] = True

    for v in graph[s]:
        if not visited[v]:
            dfs2(v)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    visited = [False] * (N+1)
    cnt = 0
    for i in range(1, N+1):
        if visited[i] == False:
            dfs2(i)
            cnt += 1

    print(f'#{tc} {cnt}')