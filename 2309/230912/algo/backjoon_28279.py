import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt', 'r')

from collections import deque

def order(s):
    if s[0] == 1:
        dec.appendleft(s[1])

    elif s[0] == 2:
        dec.append(s[1])

    elif s[0] == 3:
        if dec:
            v = dec.popleft()
            print(v)
        else:
            print(-1)

    elif s[0] == 4:
        if dec:
            v1 = dec.pop()
            print(v1)
        else:
            print(-1)

    elif s[0] == 5:
        l = len(dec)
        print(l)

    elif s[0] == 6:
        if not dec:
            print(1)
        else:
            print(0)

    elif s[0] == 7:
        if dec:
            print(dec[0])
        else:
            print(-1)

    elif s[0] == 8:
        if dec:
            print(dec[-1])
        else:
            print(-1)

N = int(input())
dec = deque([])

for _ in range(N):
    s = list(map(int, input().split()))
    order(s)