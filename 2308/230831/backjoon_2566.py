import sys
sys.stdin = open("input.txt", "r")

arr = [list(map(int, input().split())) for _ in range(9)]

maxV = 0
for i in range(9):
    for j in range(9):
        maxV = max(maxV, arr[i][j])
        if arr[i][j] == maxV:
            x, y = i, j

print(maxV)
print(x+1, y+1)