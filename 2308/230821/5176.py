# 이진 탐색
import sys
sys.stdin = open("5176.txt", "r")

def in_order(root):
    global value
    if root > N:
        return
    in_order(root * 2)
    arr[root] = value
    value += 1
    in_order((root * 2) + 1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    arr = [0] * (N+1)
    value = 1
    in_order(1)

    T_root = arr[1]
    nod = arr[N//2]
    # print(arr)
    print(f'#{tc} {T_root} {nod}')


