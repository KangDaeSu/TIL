import sys
sys.stdin = open("4866.txt", "r")

T = int(input())

for tc in range(1, T+1):
    my_str = input()

    stack = []
    result = 1
    for i in my_str:
        if i in ['(', '{']:
            stack.append(i)
        elif i in [')', '}']:
            if stack:
                checki = stack.pop()
                if checki == '(' and i =='}':
                    result = 0
                    break
                elif checki == '{' and i == ')':
                    result = 0
                    break
            else:
                result = 0
                break
    else:
        if stack:
            result = 0
    
    print(f'#{tc} {result}')