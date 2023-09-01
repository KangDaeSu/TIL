# 사칙연산
import sys
sys.stdin = open("1232.txt", "r")

def calc(vl, vr, op):
    if op == '+':
        return vl + vr
    elif op == '-':
        return vl - vr
    elif op == '*':
        return vl * vr
    elif op == '/':
        return vl // vr

def postorder(root):
    if TREE[root][0].isdecimal():   # TREE[root][0]이 숫자면 정수로 리턴
        return int(TREE[root][0])
    else:
        vl = postorder(int(TREE[root][1]))   # TREE[root]의 왼쪽
        vr = postorder(int(TREE[root][2]))   # TREE[root]의 오른쪽
        return calc(vl, vr, TREE[root][0])  # 연산 결과를 리턴

T = 10
for tc in range(1, T+1):
    N = int(input())
    TREE = [[0, 0] for _ in range(N+1)]
    for i in range(N):
        s = list(input().split())
        nodeNo = int(s[0])
        TREE[nodeNo] = s[1::]

    result = postorder(1)

    print(f'#{tc} {result}')