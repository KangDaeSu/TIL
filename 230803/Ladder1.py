import sys
sys.stdin = open("Ladder1.txt", "r")

T = 10
for _ in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    
    for c in range(100):
        if arr[99][c] == 2:
            break

    for r in range(99, 0, -1):

        if 0 <= c-1 <= 99 and arr[r][c-1] == 1:
            while 0 <= c-1 <= 99 and arr[r][c-1] == 1:
                c = c - 1
            continue

        if 0 <= c+1 <= 99 and arr[r][c+1] == 1:
            while 0 <= c+1 <= 99 and arr[r][c+1] == 1:
                c = c + 1 
            continue
    print(f'#{tc} {c}')