import sys
sys.stdin = open("1223.txt", "r")

def fix(s):
    icp = {'+': 1, '*': 2}
    stack = []
    postfix = ''
    for i in s:
        if i.isdigit():
            postfix += i
        else: # s == '+', '*'
            while stack and icp[stack[-1]] >= icp[i]:
                v = stack.pop()
                postfix += v
            stack.append(i)
    while stack:
        v = stack.pop()
        postfix += v
    return postfix

def cal(v1, v2, op):
    if op == '+':
        return v1 + v2
    elif op == '*':
        return v1 * v2

def decimal(s):
    stack = []
    for i in s:
        if i.isdigit():
            stack.append(i)
        else:
            v2 = stack.pop()
            v1 = stack.pop()
            stack.append(cal(int(v1), int(v2), i))
    return stack

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = input()
    postfix = fix(arr)
    result = decimal(postfix)
    print(f'#{tc} {result[0]}')