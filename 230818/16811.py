import sys
sys.stdin = open("16811.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    harvest = list(map(int, input().split()))
    