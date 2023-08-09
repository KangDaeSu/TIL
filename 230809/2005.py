import sys
sys.stdin = open("2005.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    lst = [[1] * i for i in range(1, N+1)]
    for r in range(2, N):
        for c in range(1, r):
            lst[r][c] = lst[r-1][c-1] + lst[r-1][c]
    print(f'#{tc}')
    for a in lst:
        print(*a)


