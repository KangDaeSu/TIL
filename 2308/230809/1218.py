# 괄호 짝짓기

import sys
sys.stdin = open("1218.txt", "r")

T = 10
for tc in range(1, T+1):
    N = int(input())
    lst = input()
    stack = []
    result = 1
    for i in lst:
        if i in ['(', '{', '[', '<']:   # 여는 괄호일때 스택 리스트에 추가
            stack.append(i)
        elif i in [')', '}', ']', '>']:
            if stack:
                checki = stack.pop()    # 리스트 상단의 요소를 추출
                if checki == '(' and i != ')':  # '(' 와 ')'인지 비교
                    result = 0
                    break
                elif checki == '{' and i != '}':    # '{' 와 '}'인지 비교
                    result = 0
                    break
                elif checki == '[' and i != ']':    # '[' 와 ']'인지 비교
                    result = 0
                    break
                elif checki == '<' and i != '>':    # '<' 와 '>'인지 비교
                    result = 0
                    break
        elif stack == False: #
            result = 0
            break
    else:   # 모든 작업이 끝났을때 스택에 요소가 있는지 확인
        if stack:
            result = 0
    print(f'#{tc} {result}')