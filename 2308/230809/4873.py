import sys
sys.stdin = open('4873.txt', "r")

T = int(input())
for tc in range(1, T+1):
    my_str = input().strip()

    stack = [] # 빈 리스트 생성
    for i in my_str:
        if stack and i == stack[-1]: # 스택 리스트가 True이고 i가 탑의 결과와 일치하면
            stack.pop()
        else:
            stack.append(i)
    result = len(stack)
    print(f'#{tc} {result}')
