'''
# 깊이 우선 탐색(Depth First Search, DFS) <= stack
# 빠짐없이, 중복없이 탐색, 순서는 중요 하지 않음
# 너비 우선 탐색(Breadth First Search, BFS) <= Queue

# DFS 알고리즘
vistied[], stack[] 초기화
DFS(v)
    시작점 v 방문;
    visited[v] <- true;
    while{
        if (v의 인접 정점 중 방문 안한 정점 w 가 있으면)
            push(v):
            v <- w; (w에 방문)
            visited[w] <- true;
        else
            if (스택이 비어 있지 않으면)
                v <- pop(stack);
            else
                break
    }
end DFS()
'''

# DFS 실습

'''
V E
V1 W1 V2 W2 .....
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
# 모든 경로를 찾고 출력할때 사용
def dfs(n, V, adj_m):
    stack = []  # stack 생성
    visited = [0] * (V+1)   # visited 생성
    visited[n] = 1  # 시작점 방문 표시
    print(n)    # do[n]
    while True:
        for w in range(1, V+1):   # 현재 정점 n에 인접하고 미방문 w 찾기
            if adj_m[n][w] == 1 and visited[w] == 0:
                stack.append(n) # push(n), n = w
                n = w
                print(n)   # do(w)
                visited[n] = 1  # w 방문 표시
                break   # for w, n에 인접인 w c 찾은경우
        else:
            if stack:   # 스택에 지나온 정점이 남아있으면
                n = stack.pop() # pop()해서 다시 다른 w 를 찾을 n 준비
            else:   # 스택이 비어 있으면
                break   # while True 탐색 끝
    return



V, E = map(int, input().split()) # 1번부터 V번 정점, E개의 간선
arr = list(map(int, input().split()))
print(f'arr:{arr}')
adj_m = [[0] * (V+1) for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_m[v1][v2] = 1
    adj_m[v2][v1] = 1
dfs(1, V, adj_m)


# # 단순 그룹의 개수를 확인할 때
# def dfs1(s):
#     ST = []
#     visited = [False] * (N+1)
#     ST.append(s)
#     while ST:
#         v = ST.pop()
#         if not visited[v]:
#             print(v)
#             visited[v] = True
#         for w in G[v]:
#             if not visited[w]:
#                 ST.append(w)

# def dfs(s):
#     ST = []
#     visited = [False] * (N+1)
#     ST.append(s)
#     visited[s] = True
#     # print(s)
#     while ST:
#         v = ST.pop()
#         print(v)
#         for w in G[v]:
#             if not visited[w]:
#                 ST.append(w)
#                 visited[v] = True
#                 # print(w)

# N = 7
# S = '1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7'
# lst = list(map(int, S.split(', ')))
# # print(lst)
# G = [[] for _ in range(N+1)]
# for idx in range(0, len(lst), 2):
#     v1 = lst[idx]
#     v2 = lst[idx+1]
#     G[v1].append(v2)
#     G[v2].append(v1)

# # 재귀 DFS
# N = 7
# visited = [False] * (N+1)
# def dfs(v):
#     print(v)
#     visited[v] = True
#     for w in G[v]:
#         if not visited[w]:
#             dfs(w)

# # print(G)
# dfs(1)
# # G = [
# #     [],
# #     [2, 3],
# #     [1, 4, 5],
# #     [1, 7],
# #     [2, 6],
# #     [2, 6],
# #     [4, 5, 7],
# #     [3, 6]
# # ]