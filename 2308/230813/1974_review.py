import sys
sys.stdin = open("1974.txt", "r")

T = int(input())
for tc in range(1, T+1):
    rows = [list(map(int, input().split())) for _ in range(9)]
    clums = [list(X) for X in zip(*rows)]
    boxes = [[rows[r+i][c+j] for i in range(3) for j in range(3)]
             for r in range(0, 9, 3) for c in range(0, 9, 3)]
    
    result = 1
    for row in rows:
        for i in range(1, 10):
            if i not in row:
                result = 0

    for clum in clums:
        for j in range(1, 10):
            if j not in clum:
                result = 0

    for box in boxes:
        for k in range(1, 10):
            if k not in box:
                result = 0
                
    print(f'#{tc} {result}')
