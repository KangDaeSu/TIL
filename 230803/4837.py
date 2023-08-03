import sys
sys.stdin = open("4837.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    print(N, K)