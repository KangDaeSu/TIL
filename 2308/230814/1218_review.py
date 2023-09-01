import sys
sys.stdin = open("1218.txt", "r")

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = input()
    
    result = 1
    stack = []
    for i in arr:
        if i in ['(', '{', '[', '<']:
            stack.append(i)
        elif i in [')', '}', ']', '>']:
            if stack:
                v = stack.pop()
                if v == '(' and i !=')' :
                    result = 0
                    break
                elif v == '{' and i !='}' :
                    result = 0
                    break
                elif v == '[' and i !=']' :
                    result = 0
                    break
                elif v == '<' and i !='>' :
                    result = 0
                    break
        elif stack == False:
            result = 0
            break
    else:
        if stack:
            result = 0
    print(f'#{tc} {result}')
