# 보물상자
import sys
sys.stdin = open("5658.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())

    arr = input()
    L = len(arr) // 4   # 한변에 몇개의 숫자
    lst = set()
    arr += arr
    for rot in range(L):
        for idx in range(rot, N, L):
            t = int(arr[idx:idx+L], 16)     # 16진수를 10진수로 바꿈
            lst.add(t)

    result = []
    for i in lst:
        result.append(i)
    result.sort()
    print(f'#{tc} {result[-K]}')