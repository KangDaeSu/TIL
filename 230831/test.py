# def subset(k):
#     if k == N:
#         print(bits)
#         return
#
#     bits[k] = 0
#     subset(k + 1)
#
#     bits[k] = 1
#     subset(k + 1)
#
#
# N = 5
# K = 3
# bits = [-1] * K
# subset(0)
#
# def perm(k):
#     if k == K:
#         print(bits)
#         return
#
#     for i in range(N):
#         if not used[i]:
#             used[i] = True
#             bits[k] = i
#             perm(k+1)
#             used[i] = False
#
# N = 5
# K = 3
# bits = [-1] * K
# used = [False] * N
# perm(0)

def comb(k, s):
    if k == K:
        print(bits)
        return

    for i in range(s, N-K+1+k):
        bits[k] = i
        comb(k+1, i+1)
N = 5
K = 2
bits = [-1] * K
used = [False] * N
comb(0, 0)

# 조합 2개 반복문
for i in range(N-1):
    for j in range(N):
        print(i, j)

