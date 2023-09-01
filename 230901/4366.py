# 정식이의 은행업무
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    A = input()
    B = list(map(int, input()))

    N = len(A)  # N자릿수 2진수
    M = len(B)  # M자릿수 3진수
    ans = 0

    binary = int(A, 2)  # 정수로 변환
    bin_list = [0] * N  # 각 비트를 반전시킨 수 N개 저장
    for i in range(N):  # 각 비트를 반전시킨 2진수 만들기
        bin_list[i] = binary ^ (1 << i)

    for i in range(M):  # 3진수의 B[i]자리를 바꾼 숫자 만들기
        num1 = 0    # (B[i]+1) % 3
        num2 = 0    # (B[i]+2) % 3
        for j in range(M):
            if i != j:
                num1 = num1 * 3 + B[j]
                num2 = num2 * 3 + B[j]
            else:
                num1 = num1 * 3 + (B[j]+1) % 3
                num2 = num2 * 3 + (B[j]+2) % 3
        if num1 in bin_list:
            ans = num1
            break   # for i
        if num2 in bin_list:
            ans = num2
            break

    print(f'#{tc} {ans}')