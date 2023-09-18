import sys
input = sys.stdin.readline

def binarysearch(low, high, target):
    if low > high:
        return 0

    mid = (low + high) // 2

    if A[mid] == target:
        return 1

    elif A[mid] < target:
        return binarysearch(mid + 1, high, target)

    else:
        return binarysearch(low, mid - 1, target)


N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
B = list(map(int, input().split()))

for i in range(len(B)):
    res = binarysearch(0, len(A)-1, B[i])
    print(res)