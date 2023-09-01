# 재귀 부분집합
def partial(k, sumV, zlist, olist):
    # if ...  # 백트래킹 조건
    if k == N:
        print(bits)
        # sumV = 0
        # for i in range(N):
        #     if bits[i] == 1:
        #         sumV += numbers[i]
        #         # print(numbers[i], end=' ')
        print(sumV, zlist, olist)
        return

    bits[k] = 0
    partial(k + 1, sumV+0, zlist+[numbers[k]], olist)
    bits[k] = 1
    partial(k + 1, sumV+numbers[k], zlist, olist+[numbers[k]])

N = 4
numbers = [8, 10, 20, 3]
bits = [-1] * N
sumV = 0
# result = []
zlist = []
olist = []
partial(0, sumV, zlist, olist)
