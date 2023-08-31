import sys
sys.stdin = open("1244.txt", "r")

def solve(k, s):
    global maxV
    if k == cnt:
        if maxV < int(s):
            maxV = int(s)
        return

    if memo[k]:
        if s in memo[k]:
            return
    memo[k].append(s)

    tmplst = list(s)
    for i in range(N-1):
        for j in range(i+1, N):
            tmplst[i], tmplst[j] = tmplst[j], tmplst[i]
            solve(k+1, ''.join(tmplst))
            tmplst[i], tmplst[j] = tmplst[j], tmplst[i]

T = int(input())
for tc in range(1, T+1):
    s, c = input().split()
    N = len(s)
    cnt = int(c)

    maxV = 0
    memo = [[] for _ in range(cnt)]
    solve(0, s)
    print(f'#{tc} {maxV}')


