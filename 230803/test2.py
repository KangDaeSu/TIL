# key가 nums에 있으면 위치를 return하고 없으면 -1을 return합니다
# nums = [4, 9, 11, 23, 2, 19, 7]
# nums = [2, 4, 7, 9, 11, 19, 23]
# N = 7

# def bFind(key):
#     l = 0
#     r = N-1

#     while l <= r:
#         m = (l + r) // 2
#         if key == nums[m]:
#             return m
#         if key > nums[m]:
#             l = m + 1
#         else:
#             r = m - 1 
#     return -1 # 검색실패 시 -1 리턴

# def sFind(key):
#     for idx in range(N):
#         if key == nums[idx]:
#             return idx
#         if key < nums[idx]:
#             return -1
#     return -1

#     # idx = 0
#     # while idx<N:
#     #     if key == nums[idx]:
#     #         return idx
#     #     idx += 1
#     # return -1


# print(sFind(4))
# print(sFind(9))
# print(sFind(11))
# print(sFind(23))
# print(sFind(2))
# print(sFind(19))
# print(sFind(7))

nums = [64, 25, 10, 22, 11]
N = 5
# 0: [10, 25, 64, 22, 11]
# 1: [10, 11, 64, 22, 25]
# 2: [10, 11, 22, 64, 25]
# 3: [10, 11, 22, 25, 64]

for s in range(N-1):
    # 최소를 구한다. s -> N-1
    curMinIdx = s
    for idx in range(s, N):
        if nums[curMinIdx] > nums[idx]:
            curMinIdx = idx
    nums[curMinIdx], nums[s] = nums[s], nums[curMinIdx]
print(nums)

# N-1 : [11, 25, 10, 22, 64]
# N-2 : [11, 22, 10, 25, 64]
# N-3 : [11, 10, 22, 25, 64]
# N-4(1) : [10, 11, 22, 25, 64]

for e in range(N-1, 0):
    curMinIdx = 0
    for idx in range(1, e+1):
        if nums[curMinIdx] < nums[idx]:
            curMinIdx = idx
    nums[curMinIdx], nums[s] = nums[s], nums[curMinIdx]
print(nums)

#nums = [64, 25, 10, 22, 11]
# N-1: [25,64,...], [25, 10, 64, ...], [25, 10, 22, 64, 11]..

for phase in range(N-1, 0, -1):
    for dix in range(phase):
        if nums[idx] < nums[idx+1]:
            nums[idx], nums[idx+1] = nums[idx+1], nums[idx]
        