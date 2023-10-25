import sys
open = sys.stdin.readline

N = int(input())
for i in range(1, N+1):
    j = 2*i-1
    print(' ' * (N-i) + '*' * j)
for j in range(N-1, 0, -1):
    i = 2*j-1
    print(' ' * (N-j) + '*' * i)