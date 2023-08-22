# 이진 합
import sys
sys.stdin = open("5177.txt", "r")

def insert1(item):
    last = len(HEAP) - 1
    HEAP[last] = item
    c = last
    while c > 1:
        p = c//2
        if HEAP[p] > HEAP[c]:
            HEAP[p], HEAP[c] = HEAP[c], HEAP[p]
            c = p
        else:
            break

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    HEAP = [0]
    for i in arr:
        HEAP.append(0)
        insert1(i)
    c = N
    p = c//2
    sumV = 0
    while c > 1:
        sumV += HEAP[p]
        c = p
        p = c//2
    print(f'#{tc} {sumV}')
