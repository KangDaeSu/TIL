import sys
sys.stdin = open("5202.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    lst.sort(key=lambda x:x[1])
    lst = [[0, 0]] + lst
    s = []
    j = 0
    for i in range(1, N+1):
        if lst[i][0] >= lst[j][1]:
            s.append(i)
            j = i

    result = len(s)
    print(f'#{tc} {result}')