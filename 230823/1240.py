# 단순 2진 암호코드
import sys
sys.stdin = open("1240.txt", "r")
code = {
    (0,0,0,1,1,0,1):0,
    (0,0,1,1,0,0,1):1,
    (0,0,1,0,0,1,1):2,
    (0,1,1,1,1,0,1):3,
    (0,1,0,0,0,1,1):4,
    (0,1,1,0,0,0,1):5,
    (0,1,0,1,1,1,1):6,
    (0,1,1,1,0,1,1):7,
    (0,1,1,0,1,1,1):8,
    (0,0,0,1,0,1,1):9
}
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]
    # print(arr)
    for r in range(N):
        for k in range(M-1, -1, -1):
            if arr[r][k] == 1:
                s = arr[r][k-55:k+1]
                break
    
    lst = []
    for i in range(0, len(s), 7):
        num = tuple(s[i:i+7])
        lst.append(code[num])


    sumI = 0
    sumJ = 0
    for i in range(1, len(lst)+1, 2):
        sumI += lst[i]
    
    for j in range(0, len(lst), 2):
        sumJ += lst[j]*3

    if (sumI + sumJ) % 10 != 0:
        result = 0
    else:
        result = sum(lst)

    print(f'#{tc} {result}')

# '0111011/0110001/0111011/0110001/0110001/0001101/0010011/0111011'
# 7 5 7 5 5 0 2 7