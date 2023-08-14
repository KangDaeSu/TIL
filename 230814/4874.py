import sys
sys.stdin = open("4874.txt", "r")



def cal(v1, v2, op):
    if op == '+':
        return v1 + v2
    if op == '-':
        return v2 - v1
    if op == '*':
        return v1 * v2
    if op == '/':
        return v2 // v1

def STEP2(s):
    ST = []
    for c in s:
        if c.isdigit():
            ST.append(c)
        elif c in ['+', '-', '*', '/']:
            if len(ST) >= 2:
                v1 = ST.pop()
                v2 = ST.pop()
                ST.append((cal(int(v1), int(v2), c)))
            else:
                return 'error'
        else:
            if len(ST) == 1:
                return ST.pop()
            else:
                return 'error'

T = int(input())
for tc in range(1, T+1):
    lst = list(input().split())


    result = STEP2(lst)
    print(f'#{tc} {result}')