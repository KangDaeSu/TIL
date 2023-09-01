import sys
sys.stdin = open("1959.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    if N > M:
        N, M = M, N
        A, B = B, A

    max_sum = 0
    for k in range(N):
        max_sum += A[k] * B[k]

    for i in range(M-N+1):
        my_sum = 0
        for j in range(N):
            my_sum += A[j] * B[j+i]
        if max_sum < my_sum:
            max_sum = my_sum

    print(f'#{tc} {max_sum}')


