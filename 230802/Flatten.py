import sys
sys.stdin = open("Flatten.txt", "r")

T = 10
for tc in range(1, T+1):
    N = int(input())
    BOX = list(map(int, input().split()))

    # 최대 인덱스 찾고 -1, 최소 인덱스 찾고 +1
    for _ in range(N):
        max_value = 0
        min_value = 100
        for s in range(100): 
            if max_value < BOX[s]: # 최대, 최소 인덱스 찾기
                max_value = BOX[s]
            if min_value > BOX[s]:
                min_value = BOX[s]
        max_idx = BOX.index(max_value)
        min_idx = BOX.index(min_value)
        BOX[max_idx] = max_value - 1
        BOX[min_idx] = min_value + 1
        # if max_value != min_value: # 최대값 위치에 대한 값-1, 최소값 인덱스에 대한 값+1
        #     max_idx = BOX.index(max_value)  
        #     min_idx = BOX.index(min_value)

        #     BOX[max_idx] = max_value - 1
        #     BOX[min_idx] = min_value + 1
        # else:
        #     break
    
    max_value = 0
    min_value = 100
    for s in range(100):
        if max_value < BOX[s]:
            max_value = BOX[s]
        if min_value > BOX[s]:
            min_value = BOX[s]
    
    result = max_value - min_value
    
    
    print(f'#{tc} {result}')
        


