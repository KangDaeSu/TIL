# 이진수

import sys
sys.stdin = open("5185.txt", "r")

def HexToBin(HexC,N):
    result1 = 0
    result2 = ''
    for C in HexC:
        if C.isdecimal():
            decV = int(C)
        else:
            decV = ord(C) - ord('A') + 10
        result1 = result1 * 16 + decV
        
    L = 4 * int(N)
    for shiftBit in range(L):
        t = result1 & (1<<shiftBit)
        if t != 0:
            result2 = '1' + result2
        else:
            result2 = '0' + result2
    return result2

T = int(input())
for tc in range(1, T+1):
    N, nums = input().split()
    print(f'#{tc} {HexToBin(nums, N)}')
