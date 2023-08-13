import sys
sys.stdin = open("1289.txt", "r")

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input()))
    
    stack = 0
    cnt = 0
    for i in arr:
        if i != stack:
            stack = i
            cnt += 1
    
    print(f'#{tc} {cnt}')
