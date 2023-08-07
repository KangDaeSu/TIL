import sys
sys.stdin = open("4865.txt", "r")

T =int(input())

for tc in range(1, T+1):
    N = input()
    M = input()
    # print(N, M)
    max = 0
    for i in N:
        cnt = 0
        for j in M:
            if j == i:
                cnt +=1

        if max < cnt:
            max = cnt

    print(f'#{tc} {max}')
