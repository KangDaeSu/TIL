# def f(n):
#     if n == 1:
#         return 1
#     return n * f(n-1)
# print(f(5))
#
# def f1(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     return f(n-1) + f(n-2)
# print(f1(5))

# 재귀 - 부분집합
def partial(k):
    if k == N:
        print(result_i)
        for i in range(N):
            if result_i[i] == 1:
                print(arr[i], end = ' ')
        print()
        return

    # candidates = [0, 1]
    # for i in candidates:
    for i in range(2):
        result_i[k] = i
        partial(k+1)

    # result_i[k] = 1
    # partial(k+1)

# 순열
# def permutation(k):
#     if k == N:
#         print(result_i)
#         for i in range(N):
#             pos = result_i[i]   # 각 순열의 idx를 변수로 저장
#             print(arr[pos], end = ' ')  # 순열의 값을 출력
#         print()
#         return
#
#     # candidates = make_candidated()
#     for i in range(N):
#         if not used[i]:  # 위에서 사용하고 있지 않으면:
#             used[i] = True  # i는 사용
#             result_i[k] = i     # index
#             permutation(k+1)
#             used[i] = False     # i사용 해제
#
# N = 3
# arr = [2, 5, 7]
# result_i = [-1] * N
# used = [False] * N
# # partial(0)
# permutation(0)
def print_result():
    for i in range(N):
        if result_idx[i]:
            print(arr[i], end=' ')
    print()


def partial(k, curSum):
    if curSum > 10:
        return

    if k == N:
        if curSum == 10:
            print_result()
        return
        # print(result_idx)
        sumV = 0
        # for i in range(N):
        #     if result_idx[i]:
        #         # print(arr[i], end = ' ')
        #         sumV += arr[i]
        # # print(sumV)
        # if sumV == 10:
        #     print_result()


    result_idx[k] = 0
    partial(k+1, curSum)
    result_idx[k] = 1
    partial(k + 1, curSum + arr[k])

# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = 10
# arr = [5, 3, 2]
arr = [i for i in range(1, 11)]
result_idx = [-1] * N
curSum = 0
partial(0, curSum)
