import sys 
sys.stdin = open("1989.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = input()
    for _ in N:
        if list(N) == list(reversed(N)):
            result = '1'
        else:
            result = '0'
    print(f'#{tc} {result}')