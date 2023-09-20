import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

def bfs(s, cnt):
    q = deque([(s, cnt)])

    while q:
        v1, c1 = q.popleft()
        c1 += 1

        for newv1 in [v1+1, v1-1, v1*2, v1-10]:
            if 1 <= newv1 <= 1000000 and not used[newv1]:
                if newv1 == M:
                    return c1
                q.append((newv1, c1))
                used[newv1] = True


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    used = [False] * 1000001
    print(f'#{tc} {bfs(N, 0)}')

