# 이진 탐색 트리
# 입력이 가능하면 입력후 pos return, 이미 있어서 입력이 불가능 하면 -1을 return
def insert(key):
    pos = 1
    while TREE[pos] != 0:
        if TREE[pos] == key:  # 찾음
            return -1
        if TREE[pos] < key:  # 오른쪽
            pos = pos * 2 + 1
        else:  # 왼쪽
            pos = pos * 2
    TREE[pos] = key
    return pos

# key가 있는 위치를 return, 없으면 -1을 return
def find(key):
    pos = 1
    while TREE[pos] != 0:
        if TREE[pos] == key:    # 찾음
            return pos
        if TREE[pos] < key:     # 오른쪽
            pos = pos * 2 + 1
        else:                   # 왼쪽
            pos = pos * 2
    return -1


# TREE = [0, 9, 4, 12, 3, 6, 0, 15, 0, 0, 0, 0, 0, 0, 13, 17]
TREE = [0] * 100

# insert(9)
# print(TREE)
# insert(5)
# print(TREE)
# insert(7)
# print(TREE)
# insert(4)
# print(TREE)

# heapq (내장함수)
# import heapq
# heap = []            # creates an empty heap
# heapq.heappush(heap, 10) # pushes a new item on the heap
# heapq.heappush(heap, 20) # pushes a new item on the heap
# heapq.heappush(heap, 30) # pushes a new item on the heap
# heapq.heappush(heap, 5) # pushes a new item on the heap
# heapq.heappush(heap, 3) # pushes a new item on the heap
# print(heap)
#
# item = heapq.heappop(heap) # pops the smallest item from the heap
# print(item)
# print(heap)

# 힙
def deq():
    global last
    tmp = heap[1]       # 루트 백업
    heap[1] = heap[last]    # 삭제할 노드의 키를 루트에 복사
    last -= 1           # 마지막 노드 삭제
    p = 1           # 루트에 옮긴 값을 자식과 비교
    c = p * 2       # 왼쪽 자식(비교할 자식노드 번호)

    while c <= last:    # 자식이 하나라도 있으면...
        if c + 1 <= last and heap[c] < heap[c + 1]:     # 오른쪽 자식도 있고, 오른쪽 자식이 더 크면
            c += 1      # 비교 대상이 오른쪽 자식노드
        if heap[p] < heap[c]:   # 자식이 더 크면 최대힙 규칙에 어긋나므로
            heap[p], heap[c] = heap[c], heap[p]
            p = c   # 자식을 새로운 부모로
            c = p * 2   # 왼쪽 자식 번호를 계산
        else:   # 부모가 더 크면
            break   # 비교 중단
    return tmp


heap = [0] * 100
last = 0

# heap 삽입
def insert1(item):
    global last
    last += 1
    HEAP[last] = item
    c = last
    while c > 1:
        p = c//2
        if HEAP[p] < HEAP[c]:
            HEAP[p], HEAP[c] = HEAP[c], HEAP[p]
            c = p
        else:
            break

def insert2(item):
    global last
    last += 1
    HEAP[last] = item
    c = last
    p = c // 2
    while c > 1 and HEAP[p] < HEAP[c]:
        HEAP[p], HEAP[c] = HEAP[c], HEAP[p]
        c = p

# heap 삭제
def pop1():
    global last

    result = HEAP[1]
    HEAP[1] = HEAP[last]
    last -= 1
    p = 1

    while p * 2 <= last:
        c = p * 2
        if c+1 <= last and HEAP[c] < HEAP[c+1]:
            c = c + 1
        if HEAP[p] < HEAP[c]:
            HEAP[p], HEAP[c] = HEAP[c], HEAP[p]
            p = c
        else:
            break

    return result

def pop2():
    global last

    result = HEAP[1]
    HEAP[1] = HEAP[last]
    last -= 1

    p = 1
    c = p*2
    while c<=last:
        if c+1<=last and HEAP[c] < HEAP[c+1]:
            c = c+1
        if HEAP[p] < HEAP[c]:
            HEAP[p], HEAP[c] = HEAP[c], HEAP[p]
            p = c
            c = p*2
        else:
            break

    return result

HEAP = [0, 33, 31, 27, 21, 22, 18, 23, 14, 19] + [0] * 100
last = 9
# insert(20)
# print(HEAP)
print(pop2())
print(HEAP)
print(pop2())
print(HEAP)
print(pop2())
print(HEAP)