# 순열
def f(i, N):
    if i == N:
        print(A)
    else:
        for j in range(i, N):   # 자신부터 오른쪽끝까지
            A[i], A[j] = A[j], A[i]
            f(i+1, N)
            A[i], A[j] = A[j], A[i] # 중복을 방지하여 원상 복구

A = [0, 1, 2]
N = len(A)
f(0, N)
# arr =
# [2, 1, 2]
# [5, 8, 5]
# [7, 2, 2]
# total = 0
# for k: 0 -> 2
#     total += arr[k][A[k]]