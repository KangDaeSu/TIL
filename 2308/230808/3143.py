import sys
sys.stdin = open("3143.txt","r")

T = int(input())

for tc in range(1, T+1):
    A, B = input().split()
    
    N = len(A)
    M = len(B)

    tp = 0
    pp = 0

    cnt = 0
    while tp<N and pp<M:
        if A[tp] != B[pp]:
            tp = tp-pp+1
            pp=0
        else:
            tp += 1
            pp += 1
            if pp == M:
                cnt+=1
                pp=0
    print(f'#{tc} {N-M*cnt+cnt}')