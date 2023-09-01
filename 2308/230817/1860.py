import sys
sys.stdin = open("1860.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    person = list(map(int, input().split()))

    person.sort()
    cnt = 0
    result = 'Possible'
    for i in person:
        if i < M:
            result = 'Impossible'
            break
        elif i >= M:
            cnt += 1
            fishbread = (i // M) * K
            if fishbread < cnt:
                result = 'Impossible'
                break

    print(f'#{tc} {result}')
