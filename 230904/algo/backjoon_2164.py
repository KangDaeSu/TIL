import sys
sys.stdin = open("input.txt", "r")

from collections import deque
N = int(input())

dq = deque()

for i in range(1, N+1):
    dq.append(i)

result = 0
while dq:
    v1 = dq.popleft()
    if not dq:
        result = v1
    if dq:
        v2 = dq.popleft()
        dq.append(v2)
print(result)

