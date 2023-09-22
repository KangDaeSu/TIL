# 격자판의 숫자 이어 붙이기

# 1. 재귀 돌리면서 숫자를 붙인다
# 2. 숫자가 7자리가 되면
# 3. set에 넣는다.

import sys
sys.stdin = open('input.txt', 'r')

# 특정 위치를 기점으로 상화좌우 문자를 뭍여야 하므로
# 파라미터로 좌표값도 받아야 한다.
def dfs(y, x, number):
    # 기저 조건 : 길이가 7이되면 재귀 종료
    if len(number) == 7:
        result.add(number)
        return

    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]

        # 갈 수 없는 위치면 continue
        if ny < 0 or ny >= 4:
            continue

        if nx < 0 or nx >= 4:
            continue

        # 갈 수 있다면, 다음 위치로 이동
        dfs(ny, nx, number + maps[ny][nx])


T = int(input())
for tc in range(1, T+1):
    # 서로 다른 수를 합친다 => 문자열이 더 좋다.
    maps = [input().split() for _ in range(4)]

    # 7자리 수를 중복 제거하여 저장
    result = set()

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    # 시작 지점 == 모두 모아야 한다.
    for i in range(4):
        for j in range(4):
            dfs(i, j, maps[i][j])

    print(f'#{tc} {len(result)}')