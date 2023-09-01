import sys
sys.stdin = open("4881.txt", "r")

def partial():


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    A = [i for i in range(N)]
    sum_min = arr[0]
    # print(f'#{tc} {result}')