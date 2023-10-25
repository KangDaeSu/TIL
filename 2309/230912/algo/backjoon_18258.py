import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')
from collections import deque

def order(s):
    if 'push' in s:
        q.append(int(s[1]))

    if 'pop' in s:
        if not q:
            print(-1)
        else:
            v = q.popleft()
            print(v)

    if 'size' in s:
        v1 = len(q)
        print(v1)

    if 'empty' in s:
        if not q:
            print(1)
        else:
            print(0)

    if 'front' in s:
        if not q:
            print(-1)
        else:
            v2 = q[0]
            print(v2)

    if 'back' in s:
        if not q:
            print(-1)
        else:
            v3 = q[-1]
            print(v3)


N = int(input())
q = deque([])
for _ in range(N):
    s = list(input().split())
    order(s)
