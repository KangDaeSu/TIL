import sys
sys.stdin = open("5203.txt", "r")

def g(player):
    p = sorted(player)
    if len(p) >= 3:
        for i in range(len(p)-2):
            if p[i] == p[i+1] and p[i+1] == p[i+2]:
                return True
    p = sorted(list(set(player)))
    if len(p) >= 3:
        for i in range(len(p)-2):
            if p[i+2] - p[i+1] == 1 and p[i+1] - p[i] == 1:
                return True
    return False

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    p1 = []
    p2 = []

    result = 0
    while arr:
        v = arr.pop(0)
        p1.append(v)
        if g(p1):
            result = 1
            break
        v = arr.pop(0)
        p2.append(v)
        if g(p2):
            result = 2
            break
    print(f'#{tc} {result}')