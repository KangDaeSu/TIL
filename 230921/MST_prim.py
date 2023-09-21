'''
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''

'''
# 힙큐 사용
import heapq

def prim(start):
    heap = []
    # MST에 포함되었는지 여부
    MST = [0] * V

    # 가중치, 정점 정보
    heapq.heappush(heap, (0, start))    

    #누적합 저장
    sum_weigh = 0

    while heap:
        # 가장 적은 가중치를 가진 정점을 꺼냄
        weight, v = heapq.heappop(heap)

        # 이미 방문한 노드라면 pass
        if MST[v]:
            continue
        
        # 방문 체크
        MST[v] = 1

        # 누적합 추가
        sum_weigh += weight

        # 갈 수 있는 노드들을 체크
        for next in range(V):
            # 갈 수 없거나 이미 방문 했다면 pass
            if graph[v][next] == 0 or MST[next]:
                continue
            
            heapq.heappush(heap, (graph[v][next], next))
            
    return sum_weigh
V, E = map(int, input().split())
# 인접 행렬

graph = [[0] * V for _ in range(V)]

for _ in range(E):
    f, t, w = map(int, input().split())
    graph[f][t] = w
    graph[t][f] = w     # 무방향 그래프

result = prim(0)
print(f'최소비용 = {result}')
'''

'''
# 힙큐 사용 x, 인접행렬 사용

def prim(s):
    # 연결된 node의 번호를 저장
    U = []
    D = [100000] * N    # 큰 값으로 초기값 설정
    P = [-1] * N
    D[s] = 0
    for _ in range(N):
        # D의 값 중 선택되지 않은 노드 중 최선을 고른다(제일 작은 값)
        minV = 1000000
        for i in range(N):
            if i in U:  # 이미 선택된 노드면 pass
                continue
            if D[i] < minV:
                minV = D[i]
                curN = i
        
        U.append(curN)  # curN 결정

        # curN와 연결되어 있는 node들의 값을 최선으로 변경
        for i in range(N):
            if i in U or G[curN][i] == 0:
                continue
            if D[i] > G[curN][i]:
                D[i] = G[curN][i]
                P[i] = curN

    print(U) # 노드가 선택된 순서
    print(D) # 각 노드들까지의 최소 거리
    print(P) # 선택된 노드가 어디에서 왔는지 출력

N, E = map(int, input().split())

# 0이면 연결되어 있지 않다.
G = [[0] * N for _ in range(N)]
for i in range(E):
    v1, v2, w = map(int, input().split())
    G[v1][v2] = w
    G[v2][v1] = w
# print(G)
prim(0)
'''