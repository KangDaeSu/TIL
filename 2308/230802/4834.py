import sys
sys.stdin = open("4834.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    value = list(map(int, input()))
    
    count = [0] * 10
    for i in value:
        count[i] += 1
    print(count)

    max_value = 0
    max_idx = 0
    for v in range(len(count)):
        if max_value <= count[v]:
            max_value = count[v]
            max_idx = v
    
    print(f'#{tc} {max_idx} {max_value}')
