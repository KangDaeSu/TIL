# 비밀번호

import sys
sys.stdin = open('1234.txt', 'r')

T = 10
for tc in range(1, T+1):
    N, arr = input().split()

    n = int(N)
    stack = [0] * n
    top = -1
    for i in arr:
        # 스택이 비어 있거나, top 원소와 다르면
        if top == -1 or stack[top] != i:
            top += 1
            stack[top] = i
        else:
            top -= 1
    # ans = ''
    # for i in range(top+1):
    #     ans += stack[i]
    #     print(f'#{tc} {ans}')
    ans = ''.join(stack[:top+1])
    print(f'#{tc} {"".join(stack[:top+1])}')
