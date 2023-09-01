import sys
sys.stdin = open("5432.txt", "r")

T = int(input())
for tc in range(1, T+1):
    lst = input()

    stick_cnt = 0
    result = 0
    # print(len(lst))
    for i in range(len(lst)):
        # print(i)
        if lst[i] == '(':
            if lst[i+1] == ')':    # 레이저면
               result += stick_cnt
            else:
                stick_cnt += 1
        else:
            if lst[i-1] != '(':  # 레이저가 아니면
                stick_cnt -= 1  # 스틱 수 하나 줄인다.
                result += 1

    print(f'#{tc} {result}')
    # 쌓인 수 cnt
    # 괄호가 '(' 면 +1, ')' -1
    # 조각수 ans