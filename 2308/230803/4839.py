import sys
sys.stdin = open("4839.txt", "r")

T = int(input())
for tc in range(1, T+1):
    PAGE, PAGEA, PAGEB = map(int, input().split())

    al, ar = 1, PAGE
    bl, br = 1, PAGE

    while True:
        ac = int((al+ar)/2)
        bc = int((bl+br)/2)

        if ac == PAGEA and bc == PAGEB:
            result = '0'
            break

        elif ac == PAGEA:
            result = 'A'
            break

        elif bc == PAGEB:
            result = 'B'
            break

        if ac > PAGEA:
            ar = ac
        else:
            al = ac

        if bc > PAGEB:
            br = bc
        else:
            bl = bc



    print(f'#{tc} {result}')