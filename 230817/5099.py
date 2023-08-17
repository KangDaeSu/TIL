import sys
sys.stdin = open("5099.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    C = [0] + list(map(int, input().split()))

    cheeze = C
    pans = [0] * N
    newpizza = 1
    while pans:
        # 1번 화덕에서 빼서
        pizzano = pans.pop(0)
        # 치즈량 감소
        cheeze[pizzano] //= 2
        # if 치즈량이 0이면
        if cheeze[pizzano] == 0:
            # 화덕에 넣을 피자가 있으면 피자를 화덕에 넣음
            if newpizza <= M:
                pans.append(newpizza)
                newpizza += 1

        # 남은 치즈가 있으면
        else:
            pans.append(pizzano)

    print(f'#{tc} {pizzano}')
