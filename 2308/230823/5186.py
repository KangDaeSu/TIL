# 이진수 2
import sys
sys.stdin = open("5186.txt", "r")


T = int(input())
for tc in range(1, T+1):
    nums = float(input())
   
    i = 0
    while i <= 13:
        i += 1
        lst = []
        v1 = nums % 2**(-i)
        nums = nums // 2**(-i)
        lst.append(v1)
        
        if nums == 0:
            print(lst)
            result = ''.join(lst)
            break
    
    if i > 12:
        result = 'overflow'

    print(f'#{tc} {result}')