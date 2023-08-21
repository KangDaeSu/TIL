# subtree
import sys
sys.stdin = open("5174.txt", "r")

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))



# 중위순위
N = int(input())
TREE = [[] for _ in range(N+1)]

for _ in range(N):
    s = input().split()
    no = int(s[0])
    TREE[no] = s[1::]
