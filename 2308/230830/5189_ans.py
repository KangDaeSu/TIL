# 전자카트

# 백트래킹 미적용
def perm(k):
    global result
    if k == N:
        sumV = 0
        for i in range(N-1):
            sp = bits[i]
            ep = bits[i+1]
            sumV += ARR[sp-1][ep-1]
        sumV += ARR[ep-1][0]
        if result > sumV:
            result = sumV
        return
    for i in range(1, N+1):
        if not used[i]:
            bits[k] = i
            used[i] = True
            perm(k + 1)
            used[i] = False

# 백트래킹 적용
def perm1(k, sumV):
    global result
    if result < sumV:
        return
    if k == N:
        ep = bits[-1]
        sumV += ARR[ep-1][0]
        if result > sumV:
            result = sumV
        return
    for i in range(1, N+1):
        if not used[i]:
            bits[k] = i
            used[i] = True
            # sp = bits[k-1]
            # ep = bits[k]
            # perm(k + 1, sumV + ARR[sp-1][ep[-1]])
            perm(k + 1, sumV + ARR[bits[k-1]-1][i-1])
            used[i] = False


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ARR = [list(map(int, input().split())) for _ in range(N)]

    bits = [-1] * N
    used = [False] * (N+1)
    bits[0] = 1
    used[1] = True
    result = 100 * 10
    # perm(1)         # 백트래킹 미적용
    perm1(1, 0)     # 백트래킹 적용
    print(f'#{tc} {result}')