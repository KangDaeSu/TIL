import sys
sys.stdin = open('input.txt', 'r')

def go(start, cnt, charged):
    global minC
    if charged == 0 or minC <= cnt:
        return

    if start == busstop-1:
        if minC > cnt:
            minC = cnt
        return

    if charged > 0:
        go(start+1, cnt, (charged-1)) # 충전 안한경우
    go(start+1, cnt+1, battery[start])  # 충전 한경우


T = int(input())

for tc in range(1, T+1):
    busstop, *battery = map(int, input().split())
    battery = battery+[0]
    minC = 100*100

    go(1, 0, battery[0])
    print(f'#{tc} {minC}')