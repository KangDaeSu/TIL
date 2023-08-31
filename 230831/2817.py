import sys
sys.stdin = open("input.txt", "r")

def perm(k, sumV):
    global cnt
    if k == N:
        if sumV == K:
            cnt += 1
        return
    else:
        bits[k] = 0
        perm(k+1, sumV)
        bits[k] = 1
        perm(k+1, sumV + arr[k])

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    bits = [-1] * N
    cnt = 0
    perm(0, 0)
    print(f'#{tc} {cnt}')