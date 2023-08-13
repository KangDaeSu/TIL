import sys
sys.stdin = open("5432.txt", "r")

T = int(input())
for tc in range(1, T+1):
    arr = input() 
    
    stack = []
    result = 0
    for i in range(len(arr)):
        if arr[i] == '(':
            stack.append(i)
        elif i-1 == stack.pop():
            result += len(stack)
        else:
            result += 1
    
    print(f'#{tc} {result}')
            