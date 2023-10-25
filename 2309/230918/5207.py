import sys
sys.stdin = open('5207_input.txt', 'r')

def binarysearch(low, high, target):
    global tem
    if low > high:
        return -1

    mid = (low + high) // 2

    if target == A[mid]:
        return mid

    elif A[mid] < target:
        if tem != 'R':
            tem = 'R'
            return binarysearch(mid + 1, high, target)
        else:
            return -1

    else:
        if tem != 'L':
            tem = 'L'
            return binarysearch(low, mid - 1, target)
        else:
            return -1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()

    cnt = 0
    for i in range(len(B)):
        tem = ''
        res = binarysearch(0, len(A) - 1, B[i])
        if res != -1:
            cnt += 1

    print(f'#{tc} {cnt}')