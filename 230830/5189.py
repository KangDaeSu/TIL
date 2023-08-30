import sys
sys.stdin = open("5189.txt", "r")

def perm(k):
    global min_value
    if k == N:
        res = bits + [1]
        sumV = 0
        for i in range(len(res)-1):
            sumV += arr[res[i] - 1][res[i+1] - 1]
        if min_value == -1:
            min_value = sumV
        if min_value > sumV:
            min_value = sumV
        return
    for i in range(1, N+1):
        if not used[i]:
            bits[k] = i
            used[i] = True
            perm(k+1)
            used[i] = False

T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 3
    arr = [list(map(int, input().split())) for _ in range(N)]   # [[0, 18, 34], [48, 0, 55], [18, 7, 0]]


    min_value = -1
    bits = [-1] * N
    used = [False] * (N+1)
    bits[0] = 1
    used[1] = True
    perm(1)
    print(f'#{tc} {min_value}')