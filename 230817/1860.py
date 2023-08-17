import sys
sys.stdin = open("1860.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort()

    repeat = 0
    cnt = 0
    while repeat < lst[-1] // M:
        for i in range(N):
            if lst[i]//M == 0:
                print("Impossible")
            else:
                cnt - 

        cnt += K
        repeat += 1


    # print(f'#{tc} {}')