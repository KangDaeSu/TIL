import sys
sys.stdin = open("1222.txt", "r")

def fix(s):
    ST = []
    postfix = ''
    icp = {'+': 1}
    for i in s:
        if i.isdigit():
            postfix += i
        else:
            while ST and icp[ST[-1]] >= icp[i]:
                v = ST.pop()
                postfix += v
            ST.append(i)
    while ST:
        v = ST.pop()
        postfix += v
    return postfix

def cal(v1, v2, op):
    if op == '+':
        return v1 + v2

def decimal(s):
    ST = []
    for i in s:
        if i.isdigit():
            ST.append(i)
        else:
            v2 = ST.pop()
            v1 = ST.pop()
            ST.append(cal(int(v1), int(v2), i))
    return ST

T = 10

for tc in range(1, T+1):
    N = int(input())
    arr = input()

    postfix = fix(arr)
    result = decimal(postfix).pop()

    print(f'#{tc} {result}')


