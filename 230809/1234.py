import sys
sys.stdin = open("1234.txt", "r")

T = 10
for tc in range(1, T+1):
    N, arr = list(input().strip().split())
    # print(N, arr)
    stack = []
    for i in arr:
        if stack and i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    result = ''.join(stack)

    print(f'#{tc}', result)