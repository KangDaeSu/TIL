# 글자수
T = int(input())
for tc in range(1, T+1):
    N = input()
    M = input()

    result = 0
    for i in N:
        cnt = 0
        for j in M:
            if j == i:
                cnt += 1
        if result < cnt:
            result = cnt
    
    print(f'#{tc} {result}')