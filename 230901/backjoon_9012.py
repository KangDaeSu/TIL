import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    s = list(input())

    stack = []
    result = 'YES'
    for i in s:
        if i == '(':    # '(' 일 때
            stack.append(i)
        else:
            if stack:
                v = stack.pop()
                if v == '(' and i != ')':  # '('와 ')'가 짝이 아닐 때
                    result = 'NO'
                    break

            else:
                result = 'NO'
                break
    else:
        if stack:
            result = 'NO'
    print(result)