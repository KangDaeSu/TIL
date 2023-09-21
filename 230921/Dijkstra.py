'''
6 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 5

'''
# 최다 거리 문제 유형
# 1. 특정 지점 -> 도착 지점까지의 최단 거리 : 다익스트라
# 2. 가중치에 음수가 포함되어 있네? : 벨만포드
# 3. 여러 지점 -> 여러 지점까지의 최단 거리
#       - 여러 지점 모두 다익스트라 돌리기 -> 시간 복잡도 계산 잘해야함
#       - 플로이드 워샬

'''
# 내가 갈 수 있는 경로 중 누적거리가 제일 짧은 것부터 고르자!
import heapq

# 입력
n, m = map(int, input().split())

# 인접리스트
graph = [[] for _ in range(n)]
for _ in range(m):
    f, t, w = map(int, input().split())
    graph[f].append([t, w]) # 양방향이 아닌 단방향
    

# 1. 누적 거리를 계속 저장
INF = int(1e9)  # 최대값 = 매우 큰 수
distance = [INF] * n

def dijkstra(start):
    # 2. 우선순위 큐
    pq = []
    
    # 출발점 초기화
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        # 현재시점에서 누적 거리가 가장 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(pq)

        # 이미 방문한 지점 + 누적거리가 더 짧게 방문한 적이 있다면 pass
        if distance[now] < dist:
            continue
        
        # 인접 노드를 확인
        for next in graph[now]:
            next_node = next[0] # 갈 지점
            cost = next[1]      # 가는 데 필요한 거리

            # next_node로 가기 위한 누적 거리
            new_cost = dist + cost # dist - 지금까지 온 누적 거리

            # 누적 거리가 기존보다 크다면
            if distance[next_node] <= new_cost:
                continue
            
            distance[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))

dijkstra(0)
print(f'각 정점 까지의 최단 거리 = {distance}')
'''

def dijk(s):
    U = []
    D = [1000000] * N

    D[s] = 0
    for _ in range(N):
        minV = 1000000
        for i in range(N):
            if i in U:
                continue
            if D[i] < minV:
                minV = D[i]
                curN = i
    
        U.append(curN)

        for i in range(N):
            if G[curN][i] == 0:
                continue

            if D[i] > D[curN] + G[curN][i]:
                D[i] = D[curN] + G[curN][i]

        print(U)
        print(D)

N, E = map(int, input().split())

# 0이면 연결되어 있지 않다.
G = [[0] * N for _ in range(N)]
for i in range(E):
    v1, v2, w = map(int, input().split())
    G[v1][v2] = w
# print(G)

dijk(0)