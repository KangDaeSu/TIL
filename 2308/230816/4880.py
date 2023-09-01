import sys
sys.stdin = open("4880.txt", "r")

def winner(a, b):
    if people[a] == people[b]:
        return a
    elif people[a] > people[b]:
        if people[a] == 3 and people[b] == 1:
            return b
        return a
    elif people[a] < people[b]:
        if people[a] == 1 and people[b] == 3:
            return a
        return b


def game(s, e):
    if s == e:
        return s    # 위치? or 값?
    w1 = game(s, (s+e)//2)
    w2 = game(((s+e)//2)+1, e)
    return winner(w1, w2)

# 빠져나가는 조건 : 남아있는 사람이 1명일 때

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    people = [0] + list(map(int, input().split()))
    i = 1
    j = N
    print(f'#{tc} {game(i, j)}')