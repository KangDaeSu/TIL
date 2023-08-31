# 베이비진이면 True / False
def isBabygin(cnts):
    for i in range(10):
        if cnts[i] >= 3:
            return True

        if cnts[i] >= 1 and cnts[i+1] >= 1 and cnts[i+2] >= 1:
            return True

    return False

# 6개의 숫자에 대하여 전체 확인 할 때
def isBabygin(cnts):
    i = 0
    while i < 10:
        if cnts[i] >= 3:
            cnts[i] -= 3
            continue

        if cnts[i] >= 1 and cnts[i+1] >= 1 and cnts[i+2] >= 1:
            return True

    return False


def isBabygin(cnts):
    i = 0
    tri = 0
    run = 0
    while i < 10:
        if cnts[i] >= 3:
            cnts[i] -= 3
            tri += 1
            continue

        if cnts[i] >= 1 and cnts[i + 1] >= 1 and cnts[i + 2] >= 1:
            cnts[i] -= 1
            cnts[i+1] -= 1
            cnts[i+2] -= 1
            run += 1
            continue
        i += 1
    if tri + run == 2:
        return True

    return False

'---------------------------------------------------------------------------'

T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input().split()))

    p1_cnts = [0] * 12
    p2_cnts = [0] * 12
    winner = 0
    for i in range(0, 12, 2):
        n1 = lst[i]
        n2 = lst[i+1]
        p1_cnts[n1] += 1
        p2_cnts[n2] += 1

        if isBabygin(p1_cnts):
            winner = 1
            break

        if isBabygin(p2_cnts):
            winner = 2
            break

    print(f'#{tc} {winner}')