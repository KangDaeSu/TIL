import sys
sys.stdin = open("4869.txt", "r")

def cnt(n):
    if n < 20:
        return 1
    return cnt(n-10) + 2*cnt(n-20)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = cnt(N)
    print(f'#{tc} {result}')