# N = 2 # 행의 크기
# M = 4 # 열의크기

# arr = [[0,1,2,3,], [4,5,6,7]]
# for i in range(N):
#     for j in range(M):
#         # if i % 2: # 홀수번 행인 경우
#         # else: # 짝수번 행인 경우
#         print(arr[i][j + (M-1-2*j) * (i % 2)])

# arr = [[0] * M for _ in range(N)]
# # arr2 = [[0] * M] * N # 잘못된 방법
# arr[0][0] = 1
# # arr2[0][0] = 1
# print(arr)

# arr = [[0, 1, 2, 3], [4, 5, 6, 7]]
#
#
# max_v = 0
# for i in range(N):
#     row_total = 0 # 각 행의 합
#     for j in range(M):
#         row_total += arr[i][j]
#     if max_v < row_total:
#         max_v = row_total
# print(max_v)
# '''
# 3
# 123
# 456
# 789
# '''
# #
# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# max_v = 0   # 모든 원소가 0이상이라면...
# for i in range(N):  # 모든 원소 arr[i][j]에 대해
#     for j in range(N):
#         s = arr[i][j] # arr[i][j] 중심으로
#         for k in range(4):
#             for p in range(1, m):
#
#                 ni, nj = i + di[k]*p, j + dj[k]*p
#                 if 0 <= ni <= N and 0 <= nj <= N: # 배열을 벗어나지 않으면...
#                     s += arr[ni][nj]
#         # 여기까지 주변 원소를 포함한 합
#         if max_v < s:   # s > max_v => 비추천
#             max_v = s
#
#
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# max_v = 0   # 모든 원소가 0이상이라면...
# for i in range(N):  # 모든 원소 arr[i][j]에 대해
#     for j in range(N):
#         s = arr[i][j] # arr[i][j] 중심으로
#         for di, dj [[0,1], [1, 0], [0, -1], [-1, 0]]:
#             ni, nj = i + di, j + dj
#             if 0 <= ni <= N and 0 <= nj <= N: # 배열을 벗어나지 않으면...
#                 s += arr[ni][nj]
#         # 여기까지 주변 원소를 포함한 합
#         if max_v < s:   # s > max_v => 비추천
#             max_v = s

# N = int(input)
# arr = [list(map(int, input().split()))for _ in range(N)]
# total1 = 0
# total2 = 0
# for i in range(N):
#     total1 += arr[i][i]
#     total2 += arr[i][N-1 - i]
# nums = [[1,2,3],
#         [4,5,6],
#         [7,8,9],
#         [1,1,1]]
#
# N = len(nums)
# M = len(nums[0])
# maxV = 0
# for r in range(N):
#     sumC = 0
#     for c in range(M):
#         print(nums[r][c], end=' ')
#         sumC += nums[r][c]
#     print(sumC)
#     if maxV < sumC:
#         maxV = sumC
# print('maxV', maxV)
# print("================================")

# for n in nums:  # 행우선만 가능
#     sumC = 0
#     for item in n:
#         print(item, end=' ')
#         sumC += item
#     print(sumC)
# print("================================")


# print("================================")
# for c in range(M):
#     sumC = 0
#     for r in range(N):
#         print(nums[r][c], end=' ')
#         sumC += nums[r][c]
#     print(sumC)
#     if maxV < sumC:
#         maxV = sumC
# print('maxV', maxV)
#
#
# sumC1 = 0
# sumC2 = 0
# for i in range(M):
#     sumC1 += nums[i][i]
#     sumC2 += nums[i][M - 1 - i]
# print(sumC1, sumC2)
# #
# # for i in range(M):
# #     sumC += nums[i][M-1-i]
# # print(sumC)

# def my_abs(value):
#     if value < 0:
#         return -value
#     return value
#
# def my_abs(value):
#     return value if value > 0 else -value
#
# N = 5
# nums = [[0] * N for _ in range(5)]
# nums[2][2] = 1
# d = 0   # 0:왼,  1:위, 2:오른, 3:아래,
# dr = [0, -1, 0, 1]
# dc = [-1, 0, 1, 0]
# sumN = 0
# for r in range(N):
#     for c in range(N):
#         print("==================")
#         print(r, c, nums[r][c])
#         for d in range(4):
#             newR = r+dr[d]
#             newC = c+dc[d]
#             if 0 <= newR < N and 0 <= newC < N:
#                 print(newR, newC, nums[newR][newC])
#                 sumN1 = nums[r][c] - nums[newR][newC]
#                 sumN += my_abs(sumN1)
#                 print(my_abs(sumN1))
#
# print(sumN)






# value = 1
# for r in range(N):
#     for c in range(N):
#         nums[r][c] = value
#         value += 1
#
# print(nums)



