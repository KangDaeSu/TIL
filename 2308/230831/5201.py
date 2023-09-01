import sys
sys.stdin = open("5201.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())        # N : 컨터이너 수, M : 트럭 수
    W = list(map(int, input().split()))     # 화물의 무게
    LC = list(map(int, input().split()))    # 트럭의 적재 용량
    W.sort(reverse=True)
    LC.sort(reverse=True)

    result = 0
    for i in range(M):
        for j in W:
            if LC[i] >= j:
                result += j
                W.remove(j)
                break

    print(f'#{tc} {result}')
