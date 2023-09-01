'''
# N의 크기만큼의 가로 줄 생성
rows = [list(map(int, input().split())) for _ in range(N)]

# 세로줄 생성
clums = [list(x) for x in zip(*rows)]

# 3 x 3 네모 박스 생성
boxes = [[rows[r+i][c+j] for i in range(3) for j in range(3)]
         for r in range(0,9,3) for c in range(0,9,3)]
'''