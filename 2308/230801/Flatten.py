'''
counts = [3, 4, 5, 7, 8, 10, 3]
for c in counts:
    if curMax < c:
        curMax = c


# 인덱스1
N = len(counts)
curMax = counts[0]
curIdx = 0
for idx in range(N): # = for idx in (0, 1, 2, ...., N-1)
    # c(value) = counts[idx]
    if curMax < counts[idx]:
        curMax = counts[idx]
        curIdx = idx
print(curIdx, counts[curIdx])


# 인덱스2
curIdx = 0
for idx in range(N):
    if counts[curIdx] < counts[idx]:
        curIdx = idx
print(curIdx, counts[curIdx])

'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    BOX = list(map(int, input().split()))

    for cnt in range(N):
        idx1, value = getMaxIdx()
        idx2, value = getMinIdx()
        Box[idx1] -= 1
        Box[idx2] += 1

        if 