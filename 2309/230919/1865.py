import sys
sys.stdin = open('input.txt', 'r')

def job(k, cursum):
    global res
    if res >= cursum:
        return

    if k == N:
        res = cursum
        return

    for i in range(N):
        if not used[i]:
            used[i] = True
            job(k+1, cursum * lst[k][i] * 0.01)
            used[i] = False


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    used = [False] * N
    res = -1
    job(0, 1)
    result = format(res*100, ".6f")
    print(f'#{tc} {result}')