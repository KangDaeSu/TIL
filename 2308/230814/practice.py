# stack = [0] * 100
# top = -1
# icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}
# isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}
#
# fx = '(6+5*(2-8)/2)'
# susik = ''
# for x in fx:
#     if x not in '(+-*/)':   # 피연산자
#         susik += x
#     elif x == ')':  # '('까지 pop()
#         while stack[top] != '(':     # peak
#             top -= 1
#         top -= 1    # '(' 버림.pop
#     else:    # '(+-*/'
#         if top == -1 or isp[stack[top]] < icp[x]:   # 토큰의 우선순위가 더 높으면
#             top += 1     # push
#             stack[top] = x
#         elif isp[stack[top]] >= icp[x]:
#             while top > -1 and isp[stack[top]] >= icp[x]:
#                 susik += stack[top]
#                 top -= 1
#                 stack[top] = x

s = '(6+5*(2-8)/2)'

def STEP1():
    result = []
    ST = []
    icp = {'(': 3, '+': 1, '-': 1, '*': 2, '/': 2}  # 연산자가 들어올 때
    isp = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}  # 스택에 있을 때
    for c in s:
        if c.isdigit():  # c가 숫자면
            result.append(c)
        # elif c == '(':
        elif c == ')':
            while ST and ST[-1] != '(':
                v = ST.pop()
                result.append(v)
            ST.pop()  # '(' 버림
        else:    # c == ['(', '+', '-', '*', '/']
            while ST and isp[ST[-1]] >= icp[c]: # ST가 존재하고 isp의 탑이 icp[c]보다 크거나 같을때
                v = ST.pop()
                result.append(v)
            ST.append(c)

    while ST:
        v = ST.pop()
        result.append(v)

    return result

def cal(v1, v2, op):
    if op == '+':
        return v1 + v2
    if op == '-':
        return v2 - v1
    if op == '*':
        return v1 * v2
    if op == '/':
        return v2 / v1

def STEP2(s):
    ST = []
    for c in s:
        if c.isdigit():  # 숫자인지 확인
            ST.append(c)
        else:
            v1 = ST.pop()
            v2 = ST.pop()
            ST.append(cal(int(v1), int(v2), c))
    return ST.pop()

step1_s = STEP1()   # 중위표현을 후위표현으로 변경
print(step1_s)
result = STEP2(step1_s)  # 후위표현식을 계산
print(result)



