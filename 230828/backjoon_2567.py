N = int(input())

board = [[0] * 100 for _ in range(100)]

cnt1 = 0

for _ in range(N):
    sx, sy = map(int, input().split())
    for x in range(sx, sx+10):
        for y in range(sy, sy+10):
            board[x][y] = 1

for i in range(100):
    for j in range(100):
        if board[i][j] == 1:
            cnt1 += 1
print(cnt1)